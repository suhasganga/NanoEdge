"""Fyers TBT (Tick-by-Tick) 50-Depth WebSocket Feed Handler.

Provides 50-level order book depth via protobuf-encoded WebSocket stream.

Key features:
- Direct WebSocket connection (not using SDK) for maximum control
- Protobuf message parsing using compiled msg_pb2.py
- Incremental depth updates (snapshot + diffs) with state management
- Channel management for efficient symbol grouping
- Exponential backoff reconnection

Rate limits:
- 3 active connections per app per user
- 5 symbols per connection (market depth mode)
- 50 channels per connection

WebSocket endpoint: wss://rtsocket-api.fyers.in/versova
Auth header: Authorization: <app_id>:<access_token>
"""

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any

import structlog
import websockets
from websockets.asyncio.client import ClientConnection

from hft.connectors.fyers.types import (
    MAX_TBT_DEPTH_LEVELS,
    TBTChannelSwitch,
    TBTDepth50,
    TBTDepthLevel,
    TBTQuote,
    TBTSubscription,
)
from hft.core.types import DepthLevel, MarketTick, OrderBookSnapshot

logger = structlog.get_logger(__name__)

# TBT WebSocket endpoint
TBT_WS_ENDPOINT = "wss://rtsocket-api.fyers.in/versova"

# Constants
PING_INTERVAL_SEC = 25.0  # Send ping every 25s to keep connection alive
RECONNECT_DELAY_BASE = 1.0
RECONNECT_DELAY_MAX = 60.0
MAX_RECONNECT_ATTEMPTS = 50

# Minimum valid timestamp (Jan 1, 2020)
MIN_VALID_TIMESTAMP_S = 1577836800


class TBTMessageType(IntEnum):
    """TBT request message types."""

    SUBSCRIBE = 1
    CHANNEL_SWITCH = 2


class ChannelState(IntEnum):
    """Channel state for tracking."""

    PAUSED = 0
    RESUMED = 1


# Callback types
TBTDepthCallback = Callable[[TBTDepth50], None]
TBTQuoteCallback = Callable[[TBTQuote, str], None]  # (quote, symbol)
TBTTickCallback = Callable[[MarketTick], None]
TBTOrderBookCallback = Callable[[OrderBookSnapshot], None]


@dataclass(slots=True)
class SymbolDepthState:
    """Maintains full depth state for a symbol (snapshot + applied diffs).

    TBT sends snapshots on first subscribe and diffs thereafter.
    This class applies diffs to maintain current state.
    """

    symbol: str
    token: str = ""
    timestamp_ns: int = 0
    sequence_no: int = 0
    total_buy_qty: int = 0
    total_sell_qty: int = 0

    # Depth levels indexed by level number (0-49)
    # Using dicts for O(1) update on diff packets
    bids: dict[int, TBTDepthLevel] = field(default_factory=dict)
    asks: dict[int, TBTDepthLevel] = field(default_factory=dict)

    def apply_snapshot(
        self,
        feed_time_ns: int,
        sequence: int,
        token: str,
        tbq: int,
        tsq: int,
        bid_levels: list[TBTDepthLevel],
        ask_levels: list[TBTDepthLevel],
    ) -> None:
        """Apply a full snapshot, replacing all state."""
        self.token = token
        self.timestamp_ns = feed_time_ns
        self.sequence_no = sequence
        self.total_buy_qty = tbq
        self.total_sell_qty = tsq

        # Replace all levels
        self.bids.clear()
        self.asks.clear()

        for level in bid_levels:
            self.bids[level.level] = level
        for level in ask_levels:
            self.asks[level.level] = level

    def apply_diff(
        self,
        feed_time_ns: int,
        sequence: int,
        tbq: int | None,
        tsq: int | None,
        bid_levels: list[TBTDepthLevel],
        ask_levels: list[TBTDepthLevel],
    ) -> None:
        """Apply incremental diff to current state.

        Only provided fields are updated. Levels with qty=0 are removed.
        """
        if sequence <= self.sequence_no:
            # Out-of-order or duplicate, skip
            return

        self.timestamp_ns = feed_time_ns
        self.sequence_no = sequence

        if tbq is not None:
            self.total_buy_qty = tbq
        if tsq is not None:
            self.total_sell_qty = tsq

        # Apply bid updates
        for level in bid_levels:
            if level.qty == 0:
                # Remove level
                self.bids.pop(level.level, None)
            else:
                self.bids[level.level] = level

        # Apply ask updates
        for level in ask_levels:
            if level.qty == 0:
                # Remove level
                self.asks.pop(level.level, None)
            else:
                self.asks[level.level] = level

    def to_depth50(self, is_snapshot: bool = False) -> TBTDepth50:
        """Convert current state to TBTDepth50 object."""
        # Sort bids by level number, then convert
        sorted_bids = [self.bids[k] for k in sorted(self.bids.keys())]
        sorted_asks = [self.asks[k] for k in sorted(self.asks.keys())]

        return TBTDepth50(
            symbol=self.symbol,
            token=self.token,
            timestamp_ns=self.timestamp_ns,
            sequence_no=self.sequence_no,
            is_snapshot=is_snapshot,
            total_buy_qty=self.total_buy_qty,
            total_sell_qty=self.total_sell_qty,
            bids=sorted_bids,
            asks=sorted_asks,
        )

    def to_order_book_snapshot(self, tick_size: float = 0.01) -> OrderBookSnapshot:
        """Convert to OrderBookSnapshot for frontend display.

        Args:
            tick_size: Tick size for price conversion (paise to INR)
        """
        # Sort and convert - bids descending by price, asks ascending
        bids_sorted = sorted(self.bids.values(), key=lambda x: -x.price)
        asks_sorted = sorted(self.asks.values(), key=lambda x: x.price)

        return OrderBookSnapshot(
            timestamp_ms=self.timestamp_ns // 1_000_000,
            exchange="fyers",
            market=self._infer_market(),
            symbol=self.symbol,
            bids=[DepthLevel(price=b.price / 100.0, size=float(b.qty)) for b in bids_sorted],
            asks=[DepthLevel(price=a.price / 100.0, size=float(a.qty)) for a in asks_sorted],
            last_update_id=self.sequence_no,
        )

    def _infer_market(self) -> str:
        """Infer market type from symbol."""
        sym = self.symbol.upper()
        # Check specific suffixes first (order matters)
        if "-EQ" in sym:
            return "equity"
        elif "-INDEX" in sym:
            return "index"
        elif "FUT" in sym:
            return "futures"
        elif sym.endswith("CE") or sym.endswith("PE"):
            # Options end with CE/PE (not just contain)
            return "options"
        return "equity"


@dataclass(slots=True)
class TBTChannel:
    """Represents a TBT channel with its subscribed symbols."""

    channel_id: str
    symbols: list[str] = field(default_factory=list)
    state: ChannelState = ChannelState.PAUSED


class FyersTBTFeedHandler:
    """
    Fyers TBT 50-Depth WebSocket Feed Handler.

    Connects to Fyers TBT WebSocket for 50-level order book depth.
    Uses protobuf for efficient message parsing and maintains
    incremental state for each subscribed symbol.

    Usage:
        handler = FyersTBTFeedHandler(
            app_id="your_app_id",
            access_token="your_token",
            symbols=["NSE:NIFTY25MARFUT", "NSE:BANKNIFTY25MARFUT"],
            on_depth=handle_depth_update,
            on_orderbook=handle_orderbook,  # For frontend
        )
        await handler.start()

    Rate limits (per connection):
        - 5 symbols max for depth mode
        - 50 channels max
        - 3 connections max per user
    """

    __slots__ = (
        "app_id",
        "access_token",
        "symbols",
        "default_channel",
        "on_depth",
        "on_orderbook",
        "on_tick",
        "on_quote",
        "_ws",
        "_running",
        "_connected",
        "_reconnect_count",
        "_depth_states",
        "_removing_symbols",
        "_channels",
        "_msg_count",
        "_last_stats_time",
        "_last_ping_time",
        "_pb_module",
    )

    def __init__(
        self,
        app_id: str,
        access_token: str,
        symbols: list[str],
        on_depth: TBTDepthCallback | None = None,
        on_orderbook: TBTOrderBookCallback | None = None,
        on_tick: TBTTickCallback | None = None,
        on_quote: TBTQuoteCallback | None = None,
        default_channel: str = "1",
    ):
        """
        Initialize TBT feed handler.

        Args:
            app_id: Fyers app ID (e.g., "XXXXX-100")
            access_token: OAuth2 access token
            symbols: List of Fyers symbols (max 5 for depth, 15 for TBT total)
            on_depth: Callback for TBTDepth50 updates
            on_orderbook: Callback for OrderBookSnapshot (frontend-friendly)
            on_tick: Callback for tick data (extracted from quote)
            on_quote: Callback for quote data
            default_channel: Default channel for subscriptions ("1"-"50")
        """
        if len(symbols) > 5:
            logger.warning(
                "tbt_symbol_limit",
                count=len(symbols),
                max=5,
                hint="TBT depth mode allows max 5 symbols per connection",
            )

        self.app_id = app_id
        self.access_token = access_token
        self.symbols = symbols[:5]  # Enforce limit
        self.default_channel = default_channel

        # Callbacks
        self.on_depth = on_depth
        self.on_orderbook = on_orderbook
        self.on_tick = on_tick
        self.on_quote = on_quote

        # State
        self._ws: ClientConnection | None = None
        self._running = False
        self._connected = False
        self._reconnect_count = 0

        # Depth state per symbol
        self._depth_states: dict[str, SymbolDepthState] = {}
        for sym in self.symbols:
            self._depth_states[sym] = SymbolDepthState(symbol=sym)

        # Track symbols being removed (to avoid race conditions)
        self._removing_symbols: set[str] = set()

        # Channel tracking
        self._channels: dict[str, TBTChannel] = {}
        self._channels[default_channel] = TBTChannel(
            channel_id=default_channel,
            symbols=list(self.symbols),
            state=ChannelState.PAUSED,
        )

        # Stats
        self._msg_count = 0
        self._last_stats_time = time.time()
        self._last_ping_time = time.time()

        # Import protobuf lazily to handle import errors gracefully
        self._pb_module = None

    def _load_protobuf(self) -> bool:
        """Load protobuf module lazily."""
        if self._pb_module is not None:
            return True

        try:
            from hft.connectors.fyers.proto import SocketMessage

            self._pb_module = SocketMessage
            return True
        except ImportError as e:
            logger.error(
                "protobuf_import_failed",
                error=str(e),
                hint="Ensure protobuf is installed: uv add protobuf",
            )
            return False

    async def start(self) -> None:
        """Start the TBT feed handler with reconnection loop."""
        if self._running:
            return

        if not self._load_protobuf():
            return

        self._running = True
        logger.info("tbt_feed_starting", symbols=self.symbols, channel=self.default_channel)

        # Start main loop
        asyncio.create_task(self._connection_loop())

    async def _connection_loop(self) -> None:
        """Main connection loop with reconnection logic."""
        delay = RECONNECT_DELAY_BASE

        while self._running:
            try:
                await self._connect_and_run()
            except websockets.exceptions.ConnectionClosed as e:
                logger.warning("tbt_ws_closed", code=e.code, reason=e.reason)
            except Exception as e:
                logger.error("tbt_ws_error", error=str(e), type=type(e).__name__)

            if not self._running:
                break

            self._connected = False
            self._reconnect_count += 1

            if self._reconnect_count > MAX_RECONNECT_ATTEMPTS:
                logger.error("tbt_max_reconnects_reached", attempts=MAX_RECONNECT_ATTEMPTS)
                break

            # Exponential backoff
            logger.info("tbt_reconnecting", delay=delay, attempt=self._reconnect_count)
            await asyncio.sleep(delay)
            delay = min(delay * 2, RECONNECT_DELAY_MAX)

    async def _connect_and_run(self) -> None:
        """Connect to WebSocket and process messages."""
        auth_header = f"{self.app_id}:{self.access_token}"

        logger.debug("tbt_connecting", endpoint=TBT_WS_ENDPOINT)

        async with websockets.connect(
            TBT_WS_ENDPOINT,
            additional_headers={"Authorization": auth_header},
            ping_interval=None,  # We'll handle pings manually
            ping_timeout=None,
            max_size=10 * 1024 * 1024,  # 10MB max message
        ) as ws:
            self._ws = ws
            self._connected = True
            self._reconnect_count = 0
            self._last_ping_time = time.time()

            logger.info("tbt_connected")

            # Subscribe to symbols on connect (if any)
            if self.symbols:
                await self._subscribe(self.symbols, self.default_channel)
                # Resume the channel to start receiving data
                await self._switch_channels(resume=[self.default_channel], pause=[])

            # Start ping task
            ping_task = asyncio.create_task(self._ping_loop())

            try:
                await self._message_loop()
            finally:
                ping_task.cancel()
                try:
                    await ping_task
                except asyncio.CancelledError:
                    pass

    async def _message_loop(self) -> None:
        """Process incoming WebSocket messages."""
        while self._running and self._ws:
            try:
                message = await asyncio.wait_for(self._ws.recv(), timeout=35.0)
                await self._process_message(message)
            except asyncio.TimeoutError:
                logger.warning("tbt_recv_timeout")
                break

    async def _ping_loop(self) -> None:
        """Send periodic pings to keep connection alive."""
        while self._running and self._ws:
            await asyncio.sleep(PING_INTERVAL_SEC)
            try:
                await self._ws.send("ping")
                self._last_ping_time = time.time()
                logger.debug("tbt_ping_sent")
            except Exception as e:
                logger.warning("tbt_ping_failed", error=str(e))
                break

    async def _subscribe(
        self,
        symbols: list[str],
        channel: str,
        mode: str = "depth",
    ) -> None:
        """Subscribe to symbols on a channel."""
        if not self._ws:
            return

        payload = {
            "type": TBTMessageType.SUBSCRIBE,
            "data": {
                "subs": 1,
                "symbols": symbols,
                "mode": mode,
                "channel": channel,
            },
        }

        await self._ws.send(json.dumps(payload))
        logger.info("tbt_subscribed", symbols=symbols, channel=channel, mode=mode)

    async def _unsubscribe(
        self,
        symbols: list[str],
        channel: str,
        mode: str = "depth",
    ) -> None:
        """Unsubscribe from symbols on a channel."""
        if not self._ws:
            return

        payload = {
            "type": TBTMessageType.SUBSCRIBE,
            "data": {
                "subs": -1,
                "symbols": symbols,
                "mode": mode,
                "channel": channel,
            },
        }

        await self._ws.send(json.dumps(payload))
        logger.info("tbt_unsubscribed", symbols=symbols, channel=channel)

    async def _switch_channels(
        self,
        resume: list[str],
        pause: list[str],
    ) -> None:
        """Switch channel states (resume/pause)."""
        if not self._ws:
            return

        payload = {
            "type": TBTMessageType.CHANNEL_SWITCH,
            "data": {
                "resumeChannels": resume,
                "pauseChannels": pause,
            },
        }

        await self._ws.send(json.dumps(payload))
        logger.info("tbt_channels_switched", resumed=resume, paused=pause)

        # Update local state
        for ch in resume:
            if ch in self._channels:
                self._channels[ch].state = ChannelState.RESUMED
        for ch in pause:
            if ch in self._channels:
                self._channels[ch].state = ChannelState.PAUSED

    async def _process_message(self, message: bytes | str) -> None:
        """Process incoming WebSocket message (protobuf or text)."""
        self._msg_count += 1

        # Handle string messages (pong, errors)
        if isinstance(message, str):
            if message == "pong":
                logger.debug("tbt_pong_received")
                return
            # Try to parse as JSON error
            try:
                data = json.loads(message)
                if data.get("error"):
                    logger.error("tbt_server_error", msg=data.get("msg"))
                return
            except json.JSONDecodeError:
                logger.debug("tbt_unknown_string_msg", msg=message[:100])
                return

        # Parse protobuf message
        try:
            from hft.connectors.fyers.proto import SocketMessage

            socket_msg = SocketMessage()
            socket_msg.ParseFromString(message)

            # Check for error
            if socket_msg.error:
                logger.error("tbt_protobuf_error", msg=socket_msg.msg)
                return

            # Process each feed in the message
            is_snapshot = socket_msg.snapshot

            for symbol, feed in socket_msg.feeds.items():
                await self._process_feed(symbol, feed, is_snapshot)

        except Exception as e:
            logger.error("tbt_parse_error", error=str(e), msg_len=len(message))

        # Log stats periodically
        self._maybe_log_stats()

    async def _process_feed(self, symbol: str, feed: Any, is_snapshot: bool) -> None:
        """Process a single MarketFeed message."""
        # Skip if symbol is being removed (race condition prevention)
        if symbol in self._removing_symbols:
            logger.debug("tbt_skip_removing_symbol", symbol=symbol)
            return

        # Skip if symbol is not subscribed (unexpected message)
        if symbol not in self.symbols:
            logger.debug("tbt_skip_unsubscribed_symbol", symbol=symbol)
            return

        # Get or create depth state (only for subscribed symbols)
        state = self._depth_states.get(symbol)
        if state is None:
            state = SymbolDepthState(symbol=symbol)
            self._depth_states[symbol] = state

        # Extract timestamp
        feed_time_ns = 0
        if feed.HasField("feed_time"):
            # feed_time is in milliseconds from Fyers
            feed_time_ns = feed.feed_time.value * 1_000_000

        sequence_no = feed.sequence_no if feed.sequence_no else 0
        token = feed.token if feed.token else ""

        # Determine if this is a snapshot (first packet or explicit)
        is_snapshot = is_snapshot or feed.snapshot

        # Process depth data
        if feed.HasField("depth"):
            depth = feed.depth

            # Extract total quantities
            tbq = depth.tbq.value if depth.HasField("tbq") else None
            tsq = depth.tsq.value if depth.HasField("tsq") else None

            # Parse bid levels
            bid_levels = self._parse_market_levels(depth.bids)
            ask_levels = self._parse_market_levels(depth.asks)

            # Apply to state
            if is_snapshot:
                state.apply_snapshot(
                    feed_time_ns=feed_time_ns,
                    sequence=sequence_no,
                    token=token,
                    tbq=tbq or 0,
                    tsq=tsq or 0,
                    bid_levels=bid_levels,
                    ask_levels=ask_levels,
                )
            else:
                state.apply_diff(
                    feed_time_ns=feed_time_ns,
                    sequence=sequence_no,
                    tbq=tbq,
                    tsq=tsq,
                    bid_levels=bid_levels,
                    ask_levels=ask_levels,
                )

            # Emit callbacks
            if self.on_depth:
                depth50 = state.to_depth50(is_snapshot=is_snapshot)
                self.on_depth(depth50)

            if self.on_orderbook:
                order_book = state.to_order_book_snapshot()
                self.on_orderbook(order_book)

        # Process quote data (if present)
        if feed.HasField("quote"):
            quote = feed.quote
            tbt_quote = TBTQuote(
                ltp=quote.ltp.value if quote.HasField("ltp") else 0,
                ltt=quote.ltt.value if quote.HasField("ltt") else 0,
                ltq=quote.ltq.value if quote.HasField("ltq") else 0,
                volume=quote.vtt.value if quote.HasField("vtt") else 0,
                volume_diff=quote.vtt_diff.value if quote.HasField("vtt_diff") else 0,
                oi=quote.oi.value if quote.HasField("oi") else 0,
                ltp_change=quote.ltpc.value if quote.HasField("ltpc") else 0,
            )

            if self.on_quote:
                self.on_quote(tbt_quote, symbol)

            # Also emit as tick
            if self.on_tick and tbt_quote.ltp > 0:
                tick = MarketTick(
                    timestamp_ns=feed_time_ns or int(time.time_ns()),
                    exchange="fyers",
                    market=state._infer_market(),
                    symbol=symbol,
                    price=tbt_quote.ltp / 100.0,  # paise to INR
                    volume=float(tbt_quote.ltq),
                    side=0,
                )
                self.on_tick(tick)

    def _parse_market_levels(self, levels: Any) -> list[TBTDepthLevel]:
        """Parse protobuf MarketLevel repeated field to TBTDepthLevel list."""
        result = []
        for level in levels:
            price = level.price.value if level.HasField("price") else 0
            qty = level.qty.value if level.HasField("qty") else 0
            orders = level.nord.value if level.HasField("nord") else 0
            level_num = level.num.value if level.HasField("num") else 0

            result.append(TBTDepthLevel(
                price=price,
                qty=qty,
                orders=orders,
                level=level_num,
            ))
        return result

    def _maybe_log_stats(self) -> None:
        """Log stats every 60 seconds."""
        now = time.time()
        if now - self._last_stats_time >= 60:
            logger.info(
                "tbt_feed_stats",
                messages=self._msg_count,
                symbols=len(self._depth_states),
                connected=self._connected,
            )
            self._msg_count = 0
            self._last_stats_time = now

    async def stop(self) -> None:
        """Stop the feed handler gracefully."""
        self._running = False

        if self._ws:
            try:
                # Unsubscribe before closing
                await self._unsubscribe(self.symbols, self.default_channel)
                await self._ws.close()
            except Exception as e:
                logger.warning("tbt_close_error", error=str(e))
            self._ws = None

        self._connected = False
        logger.info("tbt_feed_stopped")

    @property
    def is_connected(self) -> bool:
        """Return True if connected to WebSocket."""
        return self._connected

    def get_depth_state(self, symbol: str) -> SymbolDepthState | None:
        """Get current depth state for a symbol."""
        return self._depth_states.get(symbol)

    def get_order_book(self, symbol: str) -> OrderBookSnapshot | None:
        """Get current order book snapshot for a symbol."""
        state = self._depth_states.get(symbol)
        if state and state.sequence_no > 0:
            return state.to_order_book_snapshot()
        return None

    # --- Public API for dynamic subscription management ---

    async def add_symbol(self, symbol: str, channel: str | None = None) -> bool:
        """Add a symbol to subscription.

        Returns False if at limit (5 symbols for depth mode).
        """
        channel = channel or self.default_channel

        if symbol in self._depth_states:
            return True  # Already subscribed

        if len(self._depth_states) >= 5:
            logger.warning("tbt_symbol_limit_reached", symbol=symbol)
            return False

        # Track in symbols list
        if symbol not in self.symbols:
            self.symbols.append(symbol)

        # Create depth state
        self._depth_states[symbol] = SymbolDepthState(symbol=symbol)

        # Update channel tracking
        if channel in self._channels:
            if symbol not in self._channels[channel].symbols:
                self._channels[channel].symbols.append(symbol)

        # Subscribe if connected
        if self._connected and self._ws:
            await self._subscribe([symbol], channel)
            # Resume channel if it was paused (first symbol case)
            if self._channels.get(channel, TBTChannel(channel)).state == ChannelState.PAUSED:
                await self._switch_channels(resume=[channel], pause=[])

        logger.debug("tbt_symbol_added", symbol=symbol, channel=channel)
        return True

    async def remove_symbol(self, symbol: str, channel: str | None = None) -> None:
        """Remove a symbol from subscription."""
        channel = channel or self.default_channel

        if symbol not in self._depth_states:
            return

        # Mark as being removed FIRST (blocks message processing)
        self._removing_symbols.add(symbol)

        try:
            # Unsubscribe if connected
            if self._connected and self._ws:
                await self._unsubscribe([symbol], channel)

            # Remove from tracking
            if symbol in self.symbols:
                self.symbols.remove(symbol)

            # Remove depth state
            self._depth_states.pop(symbol, None)

            # Update channel tracking
            if channel in self._channels:
                if symbol in self._channels[channel].symbols:
                    self._channels[channel].symbols.remove(symbol)
        finally:
            # Always remove from pending set
            self._removing_symbols.discard(symbol)

        logger.debug("tbt_symbol_removed", symbol=symbol, channel=channel)

    async def pause_channel(self, channel: str) -> None:
        """Pause a channel (stop receiving data)."""
        if self._connected and self._ws:
            await self._switch_channels(resume=[], pause=[channel])

    async def resume_channel(self, channel: str) -> None:
        """Resume a channel (start receiving data)."""
        if self._connected and self._ws:
            await self._switch_channels(resume=[channel], pause=[])
