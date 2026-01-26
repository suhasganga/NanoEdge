"""Fyers TBT Connection Pool for dynamic multi-symbol management.

Automatically manages multiple WebSocket connections to handle more than
5 symbols (TBT depth mode limit per connection).

Rate limits:
- 3 active connections per app per user (MAX_CONNECTIONS)
- 5 symbols per connection for depth mode (SYMBOLS_PER_CONNECTION)
- Total: 15 symbols max across all connections

The pool automatically:
- Creates new connections when symbols are added beyond capacity
- Destroys empty connections when symbols are removed
- Routes callbacks from all connections to unified handlers
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import structlog

from hft.connectors.fyers.tbt_feed import (
    FyersTBTFeedHandler,
    SymbolDepthState,
    TBTDepthCallback,
    TBTOrderBookCallback,
    TBTQuoteCallback,
    TBTTickCallback,
)
from hft.connectors.fyers.types import TBTDepth50, TBTQuote
from hft.core.types import MarketTick, OrderBookSnapshot

logger = structlog.get_logger(__name__)

# Connection limits
MAX_CONNECTIONS = 3  # Per app per user
SYMBOLS_PER_CONNECTION = 5  # For depth mode


@dataclass(slots=True)
class ConnectionInfo:
    """Tracks a single TBT connection and its symbols."""

    connection_id: int
    handler: FyersTBTFeedHandler
    symbols: set[str] = field(default_factory=set)
    channel: str = "1"

    @property
    def is_full(self) -> bool:
        """Return True if connection is at symbol capacity."""
        return len(self.symbols) >= SYMBOLS_PER_CONNECTION

    @property
    def is_empty(self) -> bool:
        """Return True if connection has no symbols."""
        return len(self.symbols) == 0

    @property
    def available_slots(self) -> int:
        """Return number of available symbol slots."""
        return SYMBOLS_PER_CONNECTION - len(self.symbols)


class FyersTBTConnectionPool:
    """
    Connection pool for Fyers TBT 50-depth WebSocket.

    Automatically manages multiple connections to handle more than 5 symbols.
    Creates connections on-demand and destroys them when empty.

    Usage:
        pool = FyersTBTConnectionPool(
            app_id="your_app_id",
            access_token="your_token",
            on_depth=handle_depth,
            on_orderbook=handle_orderbook,
        )

        # Add symbols (connections created automatically)
        await pool.add_symbols(["NSE:NIFTY25MARFUT", "NSE:BANKNIFTY25MARFUT", ...])

        # Start all connections
        await pool.start()

        # Add more symbols later
        await pool.add_symbol("NSE:RELIANCE-EQ")

        # Remove symbols (connections destroyed when empty)
        await pool.remove_symbol("NSE:NIFTY25MARFUT")

        # Stop all
        await pool.stop()

    Limits:
        - 3 connections max (15 symbols total for depth mode)
        - 5 symbols per connection
    """

    __slots__ = (
        "app_id",
        "access_token",
        "on_depth",
        "on_orderbook",
        "on_tick",
        "on_quote",
        "_connections",
        "_next_connection_id",
        "_symbol_to_connection",
        "_running",
        "_lock",
    )

    def __init__(
        self,
        app_id: str,
        access_token: str,
        on_depth: TBTDepthCallback | None = None,
        on_orderbook: TBTOrderBookCallback | None = None,
        on_tick: TBTTickCallback | None = None,
        on_quote: TBTQuoteCallback | None = None,
    ):
        """
        Initialize TBT connection pool.

        Args:
            app_id: Fyers app ID
            access_token: OAuth2 access token
            on_depth: Callback for TBTDepth50 updates (from any connection)
            on_orderbook: Callback for OrderBookSnapshot updates
            on_tick: Callback for tick data
            on_quote: Callback for quote data
        """
        self.app_id = app_id
        self.access_token = access_token

        # User callbacks (aggregated from all connections)
        self.on_depth = on_depth
        self.on_orderbook = on_orderbook
        self.on_tick = on_tick
        self.on_quote = on_quote

        # Connection management
        self._connections: dict[int, ConnectionInfo] = {}
        self._next_connection_id = 1
        self._symbol_to_connection: dict[str, int] = {}  # symbol -> connection_id

        # State
        self._running = False
        self._lock = asyncio.Lock()

    @property
    def total_symbols(self) -> int:
        """Return total number of subscribed symbols across all connections."""
        return len(self._symbol_to_connection)

    @property
    def connection_count(self) -> int:
        """Return number of active connections."""
        return len(self._connections)

    @property
    def max_symbols(self) -> int:
        """Return maximum symbols that can be subscribed."""
        return MAX_CONNECTIONS * SYMBOLS_PER_CONNECTION

    @property
    def available_slots(self) -> int:
        """Return number of available symbol slots."""
        return self.max_symbols - self.total_symbols

    def get_all_symbols(self) -> list[str]:
        """Return list of all subscribed symbols."""
        return list(self._symbol_to_connection.keys())

    async def add_symbols(self, symbols: list[str]) -> list[str]:
        """
        Add multiple symbols to the pool.

        Automatically creates new connections as needed.

        Args:
            symbols: List of Fyers symbols to subscribe

        Returns:
            List of symbols that were successfully added
        """
        added = []
        for symbol in symbols:
            if await self.add_symbol(symbol):
                added.append(symbol)
        return added

    async def add_symbol(self, symbol: str) -> bool:
        """
        Add a symbol to the pool.

        Creates a new connection if all existing connections are full.

        Args:
            symbol: Fyers symbol to subscribe

        Returns:
            True if symbol was added, False if at capacity or already subscribed
        """
        async with self._lock:
            # Already subscribed?
            if symbol in self._symbol_to_connection:
                logger.debug("tbt_pool_symbol_exists", symbol=symbol)
                return True

            # Find connection with available slot
            conn = self._find_available_connection()

            if conn is None:
                # Need to create new connection
                if len(self._connections) >= MAX_CONNECTIONS:
                    logger.warning(
                        "tbt_pool_at_capacity",
                        symbol=symbol,
                        max_connections=MAX_CONNECTIONS,
                        max_symbols=self.max_symbols,
                    )
                    return False

                conn = await self._create_connection()
                if conn is None:
                    return False

            # Add symbol to connection
            conn.symbols.add(symbol)
            self._symbol_to_connection[symbol] = conn.connection_id

            # If running, subscribe on the connection
            if self._running and conn.handler.is_connected:
                await conn.handler.add_symbol(symbol, conn.channel)

            logger.info(
                "tbt_pool_symbol_added",
                symbol=symbol,
                connection_id=conn.connection_id,
                connection_symbols=len(conn.symbols),
            )
            return True

    async def remove_symbol(self, symbol: str) -> bool:
        """
        Remove a symbol from the pool.

        Destroys the connection if it becomes empty.

        Args:
            symbol: Fyers symbol to unsubscribe

        Returns:
            True if symbol was removed, False if not found
        """
        async with self._lock:
            conn_id = self._symbol_to_connection.get(symbol)
            if conn_id is None:
                return False

            conn = self._connections.get(conn_id)
            if conn is None:
                del self._symbol_to_connection[symbol]
                return False

            # Unsubscribe if running
            if self._running and conn.handler.is_connected:
                await conn.handler.remove_symbol(symbol, conn.channel)

            # Remove from tracking
            conn.symbols.discard(symbol)
            del self._symbol_to_connection[symbol]

            logger.info(
                "tbt_pool_symbol_removed",
                symbol=symbol,
                connection_id=conn_id,
                remaining_symbols=len(conn.symbols),
            )

            # Destroy connection if empty
            if conn.is_empty:
                await self._destroy_connection(conn_id)

            return True

    async def remove_symbols(self, symbols: list[str]) -> list[str]:
        """
        Remove multiple symbols from the pool.

        Args:
            symbols: List of symbols to unsubscribe

        Returns:
            List of symbols that were successfully removed
        """
        removed = []
        for symbol in symbols:
            if await self.remove_symbol(symbol):
                removed.append(symbol)
        return removed

    async def start(self) -> None:
        """Start all connections in the pool."""
        if self._running:
            return

        self._running = True
        logger.info(
            "tbt_pool_starting",
            connections=len(self._connections),
            total_symbols=self.total_symbols,
        )

        # Start all existing connections
        start_tasks = []
        for conn in self._connections.values():
            start_tasks.append(conn.handler.start())

        if start_tasks:
            await asyncio.gather(*start_tasks)

    async def stop(self) -> None:
        """Stop all connections and clear the pool."""
        self._running = False

        # Stop all connections
        stop_tasks = []
        for conn in self._connections.values():
            stop_tasks.append(conn.handler.stop())

        if stop_tasks:
            await asyncio.gather(*stop_tasks)

        # Clear state
        self._connections.clear()
        self._symbol_to_connection.clear()

        logger.info("tbt_pool_stopped")

    def _find_available_connection(self) -> ConnectionInfo | None:
        """Find a connection with available symbol slots."""
        for conn in self._connections.values():
            if not conn.is_full:
                return conn
        return None

    async def _create_connection(self) -> ConnectionInfo | None:
        """Create a new TBT connection."""
        conn_id = self._next_connection_id
        self._next_connection_id += 1

        # Each connection gets its own channel for isolation
        channel = str(conn_id)

        # Create handler with routing callbacks
        handler = FyersTBTFeedHandler(
            app_id=self.app_id,
            access_token=self.access_token,
            symbols=[],  # Symbols added dynamically
            on_depth=self._make_depth_callback(conn_id),
            on_orderbook=self._make_orderbook_callback(conn_id),
            on_tick=self._make_tick_callback(conn_id),
            on_quote=self._make_quote_callback(conn_id),
            default_channel=channel,
        )

        conn = ConnectionInfo(
            connection_id=conn_id,
            handler=handler,
            symbols=set(),
            channel=channel,
        )

        self._connections[conn_id] = conn

        # Start if pool is running
        if self._running:
            await handler.start()

        logger.info(
            "tbt_pool_connection_created",
            connection_id=conn_id,
            channel=channel,
            total_connections=len(self._connections),
        )

        return conn

    async def _destroy_connection(self, conn_id: int) -> None:
        """Destroy a TBT connection."""
        conn = self._connections.pop(conn_id, None)
        if conn is None:
            return

        # Stop the handler
        await conn.handler.stop()

        logger.info(
            "tbt_pool_connection_destroyed",
            connection_id=conn_id,
            remaining_connections=len(self._connections),
        )

    # --- Callback routing ---

    def _make_depth_callback(self, conn_id: int) -> TBTDepthCallback | None:
        """Create depth callback that routes to user callback with validation."""
        if self.on_depth is None:
            return None

        def callback(depth: TBTDepth50) -> None:
            # Validate symbol is still on this connection (prevent stale data)
            expected_conn = self._symbol_to_connection.get(depth.symbol)
            if expected_conn != conn_id:
                logger.debug(
                    "tbt_pool_stale_depth",
                    symbol=depth.symbol,
                    from_conn=conn_id,
                    expected_conn=expected_conn,
                )
                return
            self.on_depth(depth)

        return callback

    def _make_orderbook_callback(self, conn_id: int) -> TBTOrderBookCallback | None:
        """Create orderbook callback that routes to user callback with validation."""
        if self.on_orderbook is None:
            return None

        def callback(orderbook: OrderBookSnapshot) -> None:
            # Validate symbol is still on this connection
            expected_conn = self._symbol_to_connection.get(orderbook.symbol)
            if expected_conn != conn_id:
                logger.debug(
                    "tbt_pool_stale_orderbook",
                    symbol=orderbook.symbol,
                    from_conn=conn_id,
                    expected_conn=expected_conn,
                )
                return
            self.on_orderbook(orderbook)

        return callback

    def _make_tick_callback(self, conn_id: int) -> TBTTickCallback | None:
        """Create tick callback that routes to user callback with validation."""
        if self.on_tick is None:
            return None

        def callback(tick: MarketTick) -> None:
            # Validate symbol is still on this connection
            expected_conn = self._symbol_to_connection.get(tick.symbol)
            if expected_conn != conn_id:
                return
            self.on_tick(tick)

        return callback

    def _make_quote_callback(self, conn_id: int) -> TBTQuoteCallback | None:
        """Create quote callback that routes to user callback with validation."""
        if self.on_quote is None:
            return None

        def callback(quote: TBTQuote, symbol: str) -> None:
            # Validate symbol is still on this connection
            expected_conn = self._symbol_to_connection.get(symbol)
            if expected_conn != conn_id:
                return
            self.on_quote(quote, symbol)

        return callback

    # --- State access ---

    def get_depth_state(self, symbol: str) -> SymbolDepthState | None:
        """Get depth state for a symbol from its connection."""
        conn_id = self._symbol_to_connection.get(symbol)
        if conn_id is None:
            return None

        conn = self._connections.get(conn_id)
        if conn is None:
            return None

        return conn.handler.get_depth_state(symbol)

    def get_order_book(self, symbol: str) -> OrderBookSnapshot | None:
        """Get order book snapshot for a symbol."""
        conn_id = self._symbol_to_connection.get(symbol)
        if conn_id is None:
            return None

        conn = self._connections.get(conn_id)
        if conn is None:
            return None

        return conn.handler.get_order_book(symbol)

    def get_connection_stats(self) -> list[dict]:
        """Get stats for all connections."""
        stats = []
        for conn_id, conn in self._connections.items():
            stats.append({
                "connection_id": conn_id,
                "channel": conn.channel,
                "symbols": list(conn.symbols),
                "symbol_count": len(conn.symbols),
                "is_full": conn.is_full,
                "is_connected": conn.handler.is_connected,
            })
        return stats

    @property
    def is_connected(self) -> bool:
        """Return True if at least one connection is active."""
        return any(conn.handler.is_connected for conn in self._connections.values())

    @property
    def all_connected(self) -> bool:
        """Return True if all connections are active."""
        if not self._connections:
            return False
        return all(conn.handler.is_connected for conn in self._connections.values())
