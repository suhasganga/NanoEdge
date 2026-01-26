"""Application state and lifecycle management.

Supports multi-exchange configuration:
- Binance: Spot, USDT-M Futures, COIN-M Futures
- Fyers: NSE Equity, F&O, Currency, Commodity
"""

from __future__ import annotations

import asyncio
import gc
import time
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import structlog

from hft.config import Settings, settings
from hft.connectors.binance.feed import BinanceFeedHandler
from hft.connectors.binance.orderbook import BinanceOrderBook
from hft.connectors.binance.rest_client import BinanceRestClient
from hft.core.aggregator import StreamingOHLCV
from hft.core.clock_sync import ClockSync, clock_sync_registry
from hft.core.logging import configure_logging
from hft.core.ring_buffer import TickRingBuffer
from hft.core.types import OHLCV, MarketStats, MarketTick, OrderBookSnapshot, Trade
from hft.storage.questdb import QuestDBClient

if TYPE_CHECKING:
    from hft.connectors.fyers.feed import FyersFeedHandler
    from hft.connectors.fyers.rest_client import FyersRestClient
    from hft.subscriptions.manager import SubscriptionManager
    from hft.symbols.service import SymbolMasterService

logger = structlog.get_logger(__name__)


@dataclass
class AppState:
    """Global application state container for multi-exchange support."""

    settings: Settings = field(default_factory=Settings)

    # Database
    questdb: QuestDBClient | None = None

    # Binance clients
    binance_rest_client: BinanceRestClient | None = None
    binance_feed_handler: BinanceFeedHandler | None = None

    # Fyers clients
    fyers_rest_client: FyersRestClient | None = None
    fyers_feed_handler: FyersFeedHandler | None = None

    # Background tasks
    backfill_task: asyncio.Task | None = None

    # Legacy alias for backward compatibility
    @property
    def rest_client(self) -> BinanceRestClient | None:
        return self.binance_rest_client

    # Multi-exchange support
    tick_buffer: TickRingBuffer | None = None
    aggregators: dict[str, StreamingOHLCV] = field(default_factory=dict)
    orderbooks: dict[str, BinanceOrderBook] = field(default_factory=dict)

    # Legacy alias for backward compatibility
    @property
    def feed_handler(self) -> BinanceFeedHandler | None:
        return self.binance_feed_handler

    # Symbol service for search
    symbol_service: SymbolMasterService | None = None

    # On-demand subscription manager
    subscription_manager: SubscriptionManager | None = None

    # WebSocket broadcast queues (keyed by "exchange:market:symbol")
    tick_subscribers: dict[str, set[asyncio.Queue]] = field(default_factory=dict)
    depth_subscribers: dict[str, set[asyncio.Queue]] = field(default_factory=dict)
    candle_subscribers: dict[str, set[asyncio.Queue]] = field(default_factory=dict)
    trade_subscribers: dict[str, set[asyncio.Queue]] = field(default_factory=dict)
    stats_subscribers: dict[str, set[asyncio.Queue]] = field(default_factory=dict)

    # Cache for latest stats (for immediate send on connect)
    latest_stats: dict[str, MarketStats] = field(default_factory=dict)


# Global state instance
app_state = AppState()


def handle_tick(tick: MarketTick) -> None:
    """Process incoming tick from feed handler."""
    # Store in ring buffer
    if app_state.tick_buffer:
        app_state.tick_buffer.append(tick)

    # Update aggregator for real-time candle state (WebSocket updates)
    # Note: We don't write to QuestDB here - use kline stream for that
    agg = app_state.aggregators.get(tick.symbol)
    if agg:
        agg.update(tick)

    # Broadcast tick to subscribers
    _broadcast_tick(tick.symbol, tick)


def handle_kline(kline) -> None:
    """
    Process incoming kline from Binance.

    Only write to QuestDB when candle is closed (is_closed=True).
    This ensures we always have complete, accurate candle data
    directly from Binance instead of partial aggregated data.
    """
    if not kline.is_closed:
        return

    # Validate timestamp - Jan 1, 2020 00:00:00 UTC in milliseconds
    MIN_VALID_TIMESTAMP_MS = 1577836800000
    if kline.timestamp < MIN_VALID_TIMESTAMP_MS:
        logger.warning(
            "invalid_kline_timestamp",
            symbol=kline.symbol,
            timestamp=kline.timestamp,
        )
        return

    # Write closed candle to QuestDB
    if app_state.questdb:
        app_state.questdb.write_candle(kline)
        logger.info(
            "kline_closed",
            symbol=kline.symbol,
            timestamp=kline.timestamp,
            close=kline.close,
            volume=kline.volume,
        )

    # Broadcast completed candle to WebSocket subscribers
    _broadcast_candle(kline.symbol, kline)


def handle_depth_update(symbol: str, snapshot: OrderBookSnapshot) -> None:
    """Process order book update."""
    _broadcast_depth(symbol, snapshot)


def handle_trade(trade: Trade) -> None:
    """Process incoming trade for recent trades display and order simulation."""
    _broadcast_trade(trade.symbol, trade)

    # Process trade for market making simulation (if simulator exists for this symbol)
    try:
        from hft.mm.routes import process_trade_for_simulation

        process_trade_for_simulation(trade)
    except ImportError:
        pass  # MM module not available


def handle_stats(stats: MarketStats) -> None:
    """Process incoming 24h stats, cache and broadcast."""
    # Debug log for latency troubleshooting
    logger.debug(
        "handle_stats_called",
        symbol=stats.symbol,
        timestamp_ms=stats.timestamp_ms,
        recv_ts_ms=stats.recv_ts_ms,
        last_price=stats.last_price,
    )
    # Cache latest stats for immediate send on WebSocket connect
    app_state.latest_stats[stats.symbol] = stats
    _broadcast_stats(stats.symbol, stats)


def _broadcast_tick(symbol: str, tick: MarketTick) -> None:
    """Send tick to all subscribers."""
    subscribers = app_state.tick_subscribers.get(symbol, set())
    for queue in list(subscribers):
        try:
            queue.put_nowait(tick)
        except asyncio.QueueFull:
            pass  # Drop if client is slow


def _broadcast_depth(symbol: str, snapshot: OrderBookSnapshot) -> None:
    """Send depth to all subscribers."""
    subscribers = app_state.depth_subscribers.get(symbol, set())
    for queue in list(subscribers):
        try:
            queue.put_nowait(snapshot)
        except asyncio.QueueFull:
            pass


def _broadcast_candle(symbol: str, candle) -> None:
    """Send candle to all subscribers."""
    subscribers = app_state.candle_subscribers.get(symbol, set())
    for queue in list(subscribers):
        try:
            queue.put_nowait(candle)
        except asyncio.QueueFull:
            pass


def _broadcast_trade(symbol: str, trade: Trade) -> None:
    """Send trade to all subscribers."""
    subscribers = app_state.trade_subscribers.get(symbol, set())
    for queue in list(subscribers):
        try:
            queue.put_nowait(trade)
        except asyncio.QueueFull:
            pass


def _broadcast_stats(symbol: str, stats: MarketStats) -> None:
    """Send stats to all subscribers."""
    subscribers = app_state.stats_subscribers.get(symbol, set())
    for queue in list(subscribers):
        try:
            queue.put_nowait(stats)
        except asyncio.QueueFull:
            pass


def ensure_symbol_infrastructure(exchange: str, market: str, symbol: str) -> None:
    """
    Create subscriber sets and aggregator for a symbol if they don't exist.

    Called dynamically when a client subscribes to a new symbol via /ws/subscribe.
    """
    if symbol not in app_state.tick_subscribers:
        app_state.tick_subscribers[symbol] = set()
    if symbol not in app_state.depth_subscribers:
        app_state.depth_subscribers[symbol] = set()
    if symbol not in app_state.candle_subscribers:
        app_state.candle_subscribers[symbol] = set()
    if symbol not in app_state.trade_subscribers:
        app_state.trade_subscribers[symbol] = set()
    if symbol not in app_state.stats_subscribers:
        app_state.stats_subscribers[symbol] = set()

    if symbol not in app_state.aggregators:
        app_state.aggregators[symbol] = StreamingOHLCV(
            symbol=symbol,
            exchange=exchange,
            market=market,
        )
        logger.debug("symbol_infrastructure_created", symbol=symbol, exchange=exchange)


async def _startup_backfill() -> None:
    """
    Auto-backfill all symbols with data in QuestDB.

    Runs in background after server starts - doesn't block startup.
    Fills gaps from latest data timestamp to now for each symbol.
    """
    from hft.storage.gap_fill import fetch_missing_candles

    if not app_state.questdb:
        logger.warning("startup_backfill_no_questdb")
        return

    # Find all symbols with data in QuestDB
    symbols = await app_state.questdb.query_distinct_symbols(since_days=30)

    if not symbols:
        logger.info("startup_backfill_no_symbols")
        return

    logger.info(
        "startup_backfill_starting",
        symbol_count=len(symbols),
        lookback_days=settings.startup_backfill_days,
    )

    total_filled = 0

    for sym_info in symbols:
        symbol = sym_info["symbol"]
        exchange = sym_info["exchange"]
        market = sym_info["market"]
        latest_ts = sym_info["latest_ts"]

        if latest_ts is None:
            continue

        # Calculate gap from latest data to now
        now_ms = int(time.time() * 1000)
        gap_ms = now_ms - latest_ts
        gap_hours = gap_ms / (1000 * 60 * 60)

        if gap_hours < 1:
            # Skip if less than 1 hour gap
            continue

        # Backfill from latest timestamp to now
        start_ms = latest_ts
        end_ms = now_ms

        try:
            filled = await fetch_missing_candles(
                symbol=symbol,
                start_ms=start_ms,
                end_ms=end_ms,
                exchange=exchange,
                market=market,
                interval="1m",
                binance_client=app_state.binance_rest_client if exchange == "binance" else None,
                fyers_client=app_state.fyers_rest_client if exchange == "fyers" else None,
            )

            if filled:
                written = app_state.questdb.write_candles_batch(filled)
                total_filled += written
                logger.info(
                    "startup_backfill_symbol",
                    symbol=symbol,
                    exchange=exchange,
                    candles=written,
                    gap_hours=f"{gap_hours:.1f}",
                )

        except Exception as e:
            logger.error(
                "startup_backfill_failed",
                symbol=symbol,
                exchange=exchange,
                error=str(e),
            )

    logger.info("startup_backfill_complete", total_candles=total_filled)


@asynccontextmanager
async def lifespan(app):
    """Application lifespan manager with multi-exchange support."""
    # Startup
    configure_logging()
    logger.info("app_starting", symbols=settings.symbols)

    # Initialize QuestDB
    app_state.questdb = QuestDBClient(
        host=settings.questdb_host,
        ilp_port=settings.questdb_ilp_port,
        http_port=settings.questdb_http_port,
    )

    try:
        await app_state.questdb.init_schema()
    except Exception as e:
        logger.warning("questdb_init_warning", error=str(e))

    # Initialize Binance REST client
    app_state.binance_rest_client = BinanceRestClient(settings.binance_rest_url)

    # Initialize clock synchronization for Binance
    binance_clock = ClockSync(exchange="binance")
    clock_sync_registry.register("binance", binance_clock)

    # Initialize Fyers REST client (if credentials available)
    if settings.fyers_app_id and settings.fyers_access_token:
        try:
            from hft.connectors.fyers.rest_client import FyersRestClient

            app_state.fyers_rest_client = FyersRestClient(
                app_id=settings.fyers_app_id,
                access_token=settings.fyers_access_token,
            )
            logger.info("fyers_rest_client_initialized")

            # Initialize clock synchronization for Fyers
            fyers_auth = f"{settings.fyers_app_id}:{settings.fyers_access_token}"
            fyers_clock = ClockSync(exchange="fyers", auth_header=fyers_auth)
            clock_sync_registry.register("fyers", fyers_clock)
        except Exception as e:
            logger.warning("fyers_rest_client_init_failed", error=str(e))

    # Start all clock syncs
    await clock_sync_registry.start_all()

    # Initialize Symbol Master Service
    try:
        from hft.symbols.service import SymbolMasterService, set_symbol_service

        app_state.symbol_service = SymbolMasterService(
            db_path=settings.symbol_db_path
        )
        await app_state.symbol_service.initialize(
            refresh=settings.symbol_refresh_on_startup
        )
        # Register globally so API endpoints can access it
        set_symbol_service(app_state.symbol_service)
        logger.info(
            "symbol_service_initialized",
            total_symbols=app_state.symbol_service.get_count(),
        )
    except Exception as e:
        logger.warning("symbol_service_init_failed", error=str(e))

    # Initialize Subscription Manager
    try:
        from hft.subscriptions.manager import SubscriptionManager

        app_state.subscription_manager = SubscriptionManager(
            on_tick=handle_tick,
            on_kline=handle_kline,
            on_depth=lambda snap: handle_depth_update(snap.symbol, snap),
            on_trade=handle_trade,
            on_stats=handle_stats,
            max_cached_symbols=settings.max_cached_symbols,
        )
        logger.info("subscription_manager_initialized")
    except Exception as e:
        logger.warning("subscription_manager_init_failed", error=str(e))

    # Initialize tick buffer
    app_state.tick_buffer = TickRingBuffer(capacity=settings.ring_buffer_capacity)

    # Initialize aggregators and subscriber sets for default symbols
    for symbol in settings.symbols:
        app_state.aggregators[symbol] = StreamingOHLCV(
            symbol=symbol,
            exchange="binance",
            market="spot",
        )
        app_state.tick_subscribers[symbol] = set()
        app_state.depth_subscribers[symbol] = set()
        app_state.candle_subscribers[symbol] = set()
        app_state.trade_subscribers[symbol] = set()
        app_state.stats_subscribers[symbol] = set()

    # Initialize order books for default symbols
    for symbol in settings.symbols:
        ob = BinanceOrderBook(
            symbol=symbol,
            on_update=lambda snap, s=symbol: handle_depth_update(s, snap),
            rest_client=app_state.binance_rest_client,
            ws_base_url=settings.binance_ws_url,
        )
        app_state.orderbooks[symbol] = ob

    # Initialize Binance feed handler for default symbols
    app_state.binance_feed_handler = BinanceFeedHandler(
        symbols=settings.symbols,
        on_tick=handle_tick,
        on_kline=handle_kline,
        on_trade=handle_trade,
        on_stats=handle_stats,
        base_url=settings.binance_ws_url,
    )

    # Start background tasks
    tasks = []

    # Start Binance feed handler
    tasks.append(asyncio.create_task(app_state.binance_feed_handler.start()))

    # Start order books
    for ob in app_state.orderbooks.values():
        tasks.append(asyncio.create_task(ob.start()))

    # Auto-backfill on startup (background - doesn't block server)
    if settings.auto_backfill_on_startup:
        app_state.backfill_task = asyncio.create_task(_startup_backfill())
        logger.info("startup_backfill_task_started")

    logger.info("app_started", symbols=settings.symbols)

    # Freeze GC after initialization to reduce pauses during trading
    # All current objects are marked as "frozen" and won't be collected
    gc.collect()  # Full collection first
    gc.freeze()  # Freeze all current objects
    logger.info("gc_frozen", generation_0=gc.get_count()[0])

    yield

    # Shutdown
    logger.info("app_stopping")

    # Unfreeze GC before shutdown to allow cleanup
    gc.unfreeze()

    # Cancel backfill task if running
    if app_state.backfill_task and not app_state.backfill_task.done():
        app_state.backfill_task.cancel()
        try:
            await app_state.backfill_task
        except asyncio.CancelledError:
            pass
        logger.info("startup_backfill_task_cancelled")

    # Stop subscription manager
    if app_state.subscription_manager:
        await app_state.subscription_manager.unsubscribe_all()

    # Stop all clock syncs
    await clock_sync_registry.stop_all()

    # Stop Binance feed handler
    if app_state.binance_feed_handler:
        await app_state.binance_feed_handler.stop()

    # Stop Fyers feed handler
    if app_state.fyers_feed_handler:
        await app_state.fyers_feed_handler.stop()

    # Stop order books
    for ob in app_state.orderbooks.values():
        await ob.stop()

    # Close symbol service
    if app_state.symbol_service:
        app_state.symbol_service.close()

    # Close clients
    if app_state.questdb:
        await app_state.questdb.close()

    if app_state.binance_rest_client:
        await app_state.binance_rest_client.close()

    if app_state.fyers_rest_client:
        await app_state.fyers_rest_client.close()

    # Cancel background tasks
    for task in tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

    logger.info("app_stopped")
