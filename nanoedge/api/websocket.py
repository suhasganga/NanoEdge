"""WebSocket endpoints for live data streaming.

Uses msgspec for high-performance JSON serialization (2-5x faster than send_json).
"""

import asyncio
import time

import structlog
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from nanoedge.api.dependencies import app_state
from nanoedge.api.ws_types import (
    HEARTBEAT_BYTES,
    UNSUBSCRIBED_BYTES,
    encode_candle,
    encode_depth,
    encode_stats,
    encode_subscribed,
    encode_tick,
    encode_trade,
)
from nanoedge.config import settings
from nanoedge.core.clock_sync import clock_sync_registry
from nanoedge.core.metrics import metrics

logger = structlog.get_logger(__name__)
router = APIRouter()


def _get_api_ts_ms() -> int:
    """Get current API push timestamp in milliseconds."""
    return int(time.time() * 1000)


def _adjust_exch_ts(exch_ts_ms: int, exchange: str = "binance") -> int:
    """Adjust exchange timestamp to local time using per-exchange clock offset.

    This ensures consistent time base for latency calculations:
    - exch_ts (T0): Adjusted to local time using exchange-specific offset
    - recv_ts (T1): Already in local time
    - api_ts (T3): Already in local time
    - client_ts (T4): Already in local time (browser)

    Args:
        exch_ts_ms: Exchange timestamp in milliseconds
        exchange: Exchange name (binance, fyers) to get correct clock offset
    """
    return clock_sync_registry.adjust_timestamp(exchange, exch_ts_ms)


async def send_with_timing(websocket: WebSocket, data: bytes) -> None:
    """Send WebSocket message and record latency."""
    start_ns = time.perf_counter_ns()
    # Binary is faster - frontend handles ArrayBuffer with TextDecoder
    await websocket.send_bytes(data)
    elapsed_us = (time.perf_counter_ns() - start_ns) / 1000
    metrics.api_ws_push_latency.record(elapsed_us)

# Queue timeout in seconds - prevents client hangs if feed stops
QUEUE_TIMEOUT_SECONDS = 30.0

# Minimum valid timestamp: Jan 1, 2020 00:00:00 UTC in milliseconds
MIN_VALID_TIMESTAMP_MS = 1577836800000


@router.websocket("/ws/ticks/{symbol}")
async def ws_ticks(websocket: WebSocket, symbol: str):
    """
    Live tick stream for a symbol.

    Sends messages in format:
    {"type": "tick", "symbol": "BTCUSDT", "price": 50000.0,
     "volume": 0.1, "side": 1, "timestamp": 1672515782136}
    """
    await websocket.accept()
    symbol = symbol.upper()

    # Check if symbol is valid
    if symbol not in app_state.tick_subscribers:
        await websocket.close(code=4000, reason=f"Unknown symbol: {symbol}")
        return

    queue: asyncio.Queue = asyncio.Queue(maxsize=100)
    app_state.tick_subscribers[symbol].add(queue)

    logger.info("ws_tick_connected", symbol=symbol)

    try:
        while True:
            try:
                tick = await asyncio.wait_for(
                    queue.get(), timeout=QUEUE_TIMEOUT_SECONDS
                )
            except asyncio.TimeoutError:
                # Send heartbeat to keep connection alive
                await websocket.send_bytes(HEARTBEAT_BYTES)
                continue

            await send_with_timing(
                websocket,
                encode_tick(
                    symbol=tick.symbol,
                    price=tick.price,
                    volume=tick.volume,
                    side=tick.side,
                    timestamp=_adjust_exch_ts(tick.timestamp_ns // 1_000_000, tick.exchange),  # T0 adjusted
                    recv_ts=tick.recv_ts_ms,  # T1
                    api_ts=_get_api_ts_ms(),  # T3
                ),
            )
    except WebSocketDisconnect:
        pass
    except Exception as e:
        logger.error("ws_tick_error", symbol=symbol, error=str(e))
    finally:
        app_state.tick_subscribers[symbol].discard(queue)
        logger.info("ws_tick_disconnected", symbol=symbol)


@router.websocket("/ws/depth/{symbol}")
async def ws_depth(websocket: WebSocket, symbol: str):
    """
    Live order book depth stream.

    Sends messages in format:
    {"type": "depth", "symbol": "BTCUSDT",
     "bids": [[price, size], ...], "asks": [[price, size], ...],
     "lastUpdateId": 12345}
    """
    await websocket.accept()
    symbol = symbol.upper()

    if symbol not in app_state.depth_subscribers:
        await websocket.close(code=4000, reason=f"Unknown symbol: {symbol}")
        return

    queue: asyncio.Queue = asyncio.Queue(maxsize=50)
    app_state.depth_subscribers[symbol].add(queue)

    logger.info("ws_depth_connected", symbol=symbol)

    try:
        while True:
            try:
                snapshot = await asyncio.wait_for(
                    queue.get(), timeout=QUEUE_TIMEOUT_SECONDS
                )
            except asyncio.TimeoutError:
                await websocket.send_bytes(HEARTBEAT_BYTES)
                continue

            await websocket.send_bytes(
                encode_depth(
                    symbol=snapshot.symbol,
                    bids=[[level.price, level.size] for level in snapshot.bids],
                    asks=[[level.price, level.size] for level in snapshot.asks],
                    last_update_id=snapshot.last_update_id,
                    exch_ts=_adjust_exch_ts(snapshot.timestamp_ms, snapshot.exchange),  # T0 adjusted
                    recv_ts=snapshot.recv_ts_ms,  # T1
                    api_ts=_get_api_ts_ms(),  # T3
                )
            )
    except WebSocketDisconnect:
        pass
    except Exception as e:
        logger.error("ws_depth_error", symbol=symbol, error=str(e))
    finally:
        app_state.depth_subscribers[symbol].discard(queue)
        logger.info("ws_depth_disconnected", symbol=symbol)


@router.websocket("/ws/trades/{symbol}")
async def ws_trades(websocket: WebSocket, symbol: str):
    """
    Live recent trades stream.

    Sends messages in format:
    {"type": "trade", "symbol": "BTCUSDT", "price": 50000.0,
     "quantity": 0.1, "is_buyer_maker": false, "timestamp": 1672515782136}
    """
    await websocket.accept()
    symbol = symbol.upper()

    if symbol not in app_state.trade_subscribers:
        await websocket.close(code=4000, reason=f"Unknown symbol: {symbol}")
        return

    queue: asyncio.Queue = asyncio.Queue(maxsize=100)
    app_state.trade_subscribers[symbol].add(queue)

    logger.info("ws_trades_connected", symbol=symbol)

    try:
        while True:
            try:
                trade = await asyncio.wait_for(
                    queue.get(), timeout=QUEUE_TIMEOUT_SECONDS
                )
            except asyncio.TimeoutError:
                await websocket.send_bytes(HEARTBEAT_BYTES)
                continue

            await websocket.send_bytes(
                encode_trade(
                    symbol=trade.symbol,
                    price=trade.price,
                    quantity=trade.quantity,
                    is_buyer_maker=trade.is_buyer_maker,
                    timestamp=_adjust_exch_ts(trade.timestamp_ms, trade.exchange),  # T0 adjusted
                    trade_id=trade.trade_id,
                    recv_ts=trade.recv_ts_ms,  # T1
                    api_ts=_get_api_ts_ms(),  # T3
                )
            )
    except WebSocketDisconnect:
        pass
    except Exception as e:
        logger.error("ws_trades_error", symbol=symbol, error=str(e))
    finally:
        app_state.trade_subscribers[symbol].discard(queue)
        logger.info("ws_trades_disconnected", symbol=symbol)


@router.websocket("/ws/stats/{symbol}")
async def ws_stats(websocket: WebSocket, symbol: str):
    """
    Live 24h market statistics stream (~1s updates).

    Sends messages in format:
    {"type": "stats", "symbol": "BTCUSDT", "price_change": 100.5,
     "price_change_percent": 0.2, "high_24h": 51000, "low_24h": 49000,
     "volume_24h": 50000, "last_price": 50100}
    """
    await websocket.accept()
    symbol = symbol.upper()

    if symbol not in app_state.stats_subscribers:
        await websocket.close(code=4000, reason=f"Unknown symbol: {symbol}")
        return

    queue: asyncio.Queue = asyncio.Queue(maxsize=10)
    app_state.stats_subscribers[symbol].add(queue)

    # Send cached stats immediately if available
    if symbol in app_state.latest_stats:
        stats = app_state.latest_stats[symbol]
        await websocket.send_bytes(_encode_stats(stats))

    logger.info("ws_stats_connected", symbol=symbol)

    try:
        while True:
            try:
                stats = await asyncio.wait_for(
                    queue.get(), timeout=QUEUE_TIMEOUT_SECONDS
                )
            except asyncio.TimeoutError:
                await websocket.send_bytes(HEARTBEAT_BYTES)
                continue

            await websocket.send_bytes(_encode_stats(stats))
    except WebSocketDisconnect:
        pass
    except Exception as e:
        logger.error("ws_stats_error", symbol=symbol, error=str(e))
    finally:
        app_state.stats_subscribers[symbol].discard(queue)
        logger.info("ws_stats_disconnected", symbol=symbol)


def _encode_stats(stats) -> bytes:
    """Encode MarketStats to JSON bytes using msgspec."""
    recv_ts = stats.recv_ts_ms
    api_ts = _get_api_ts_ms()

    # Debug log for latency troubleshooting
    if recv_ts == 0:
        logger.debug(
            "stats_no_recv_ts",
            symbol=stats.symbol,
            timestamp_ms=stats.timestamp_ms,
        )

    return encode_stats(
        symbol=stats.symbol,
        price_change=stats.price_change,
        price_change_percent=stats.price_change_percent,
        high_24h=stats.high_24h,
        low_24h=stats.low_24h,
        volume_24h=stats.volume_24h,
        quote_volume_24h=stats.quote_volume_24h,
        trade_count_24h=stats.trade_count_24h,
        last_price=stats.last_price,
        open_price=stats.open_price,
        exch_ts=_adjust_exch_ts(stats.timestamp_ms, stats.exchange),  # T0 adjusted
        recv_ts=recv_ts,  # T1
        api_ts=api_ts,  # T3
    )


async def _backfill_symbol_on_switch(
    symbol: str,
    exchange: str,
    market: str,
) -> None:
    """
    Ensure symbol has recent data when switching.

    Called on symbol subscribe via /ws/subscribe endpoint.
    Runs as background task - doesn't block the subscription.
    """
    from nanoedge.storage.gap_fill import fetch_missing_candles

    if not settings.backfill_on_symbol_switch:
        return

    if not app_state.questdb:
        return

    try:
        # Check latest data for this symbol
        latest_ts = await app_state.questdb.get_latest_timestamp(symbol, exchange, market)
        now_ms = int(time.time() * 1000)
        lookback_hours = settings.symbol_switch_backfill_hours

        if latest_ts is None:
            # No data - backfill last N hours
            start_ms = now_ms - (lookback_hours * 60 * 60 * 1000)
            gap_hours = lookback_hours
        else:
            gap_ms = now_ms - latest_ts
            gap_hours = gap_ms / (1000 * 60 * 60)

            if gap_hours < 0.5:  # Less than 30 min gap - skip
                return

            start_ms = latest_ts

        # Fetch and write missing candles
        filled = await fetch_missing_candles(
            symbol=symbol,
            start_ms=start_ms,
            end_ms=now_ms,
            exchange=exchange,
            market=market,
            interval="1m",
            binance_client=app_state.binance_rest_client if exchange == "binance" else None,
            fyers_client=app_state.fyers_rest_client if exchange == "fyers" else None,
        )

        if filled:
            written = app_state.questdb.write_candles_batch(filled)
            logger.info(
                "symbol_switch_backfill",
                symbol=symbol,
                exchange=exchange,
                candles=written,
                gap_hours=f"{gap_hours:.1f}",
            )

    except Exception as e:
        logger.warning(
            "symbol_switch_backfill_failed",
            symbol=symbol,
            exchange=exchange,
            error=str(e),
        )


@router.websocket("/ws/candles/{symbol}")
async def ws_candles(websocket: WebSocket, symbol: str):
    """
    Live candle updates.

    Sends current candle state every 500ms and completed candles immediately.

    Format:
    {"type": "candle", "time": 1672515780, "open": 50000.0,
     "high": 50100.0, "low": 49900.0, "close": 50050.0}
    """
    await websocket.accept()
    symbol = symbol.upper()

    if symbol not in app_state.aggregators:
        await websocket.close(code=4000, reason=f"Unknown symbol: {symbol}")
        return

    # Queue for completed candles
    queue: asyncio.Queue = asyncio.Queue(maxsize=10)
    app_state.candle_subscribers.setdefault(symbol, set()).add(queue)

    logger.info("ws_candle_connected", symbol=symbol)

    # Track tasks for proper cleanup
    current_task: asyncio.Task | None = None
    completed_task: asyncio.Task | None = None

    async def send_current_candle():
        """Send current candle state periodically."""
        while True:
            try:
                agg = app_state.aggregators.get(symbol)
                if agg:
                    candle = agg.get_current()
                    if candle and candle.timestamp >= MIN_VALID_TIMESTAMP_MS:
                        await websocket.send_bytes(
                            encode_candle(
                                time=candle.timestamp // 1000,  # ms to seconds
                                open=candle.open,
                                high=candle.high,
                                low=candle.low,
                                close=candle.close,
                                volume=candle.volume,
                                closed=False,
                                exch_ts=_adjust_exch_ts(candle.timestamp, candle.exchange),  # T0 adjusted
                                recv_ts=candle.recv_ts_ms,  # T1
                                api_ts=_get_api_ts_ms(),  # T3
                            )
                        )
                    elif candle:
                        logger.warning(
                            "invalid_candle_timestamp",
                            symbol=symbol,
                            timestamp=candle.timestamp,
                        )
                await asyncio.sleep(0.05)  # Update every 50ms (20 updates/sec)
            except asyncio.CancelledError:
                break
            except Exception:
                break

    async def send_completed_candles():
        """Send completed candles from queue."""
        while True:
            try:
                candle = await asyncio.wait_for(
                    queue.get(), timeout=QUEUE_TIMEOUT_SECONDS
                )
                if candle.timestamp >= MIN_VALID_TIMESTAMP_MS:
                    await websocket.send_bytes(
                        encode_candle(
                            time=candle.timestamp // 1000,
                            open=candle.open,
                            high=candle.high,
                            low=candle.low,
                            close=candle.close,
                            volume=candle.volume,
                            closed=True,
                            exch_ts=_adjust_exch_ts(candle.timestamp, candle.exchange),  # T0 adjusted
                            recv_ts=candle.recv_ts_ms,  # T1
                            api_ts=_get_api_ts_ms(),  # T3
                        )
                    )
                else:
                    logger.warning(
                        "invalid_completed_candle_timestamp",
                        symbol=symbol,
                        timestamp=candle.timestamp,
                    )
            except asyncio.TimeoutError:
                # No completed candles, continue waiting
                continue
            except asyncio.CancelledError:
                break
            except Exception:
                break

    try:
        # Run both tasks concurrently
        current_task = asyncio.create_task(send_current_candle())
        completed_task = asyncio.create_task(send_completed_candles())

        # Wait for either task to complete (usually due to disconnect)
        await asyncio.gather(current_task, completed_task)

    except WebSocketDisconnect:
        pass
    except Exception as e:
        logger.error("ws_candle_error", symbol=symbol, error=str(e))
    finally:
        # Properly cancel both tasks on disconnect
        if current_task and not current_task.done():
            current_task.cancel()
            try:
                await current_task
            except asyncio.CancelledError:
                pass
        if completed_task and not completed_task.done():
            completed_task.cancel()
            try:
                await completed_task
            except asyncio.CancelledError:
                pass

        app_state.candle_subscribers[symbol].discard(queue)
        logger.info("ws_candle_disconnected", symbol=symbol)


@router.websocket("/ws/subscribe")
async def ws_dynamic_subscribe(websocket: WebSocket):
    """
    Dynamic subscription WebSocket - enables multi-symbol switching.

    Client sends: {"action": "subscribe", "exchange": "binance", "market": "spot", "symbol": "SOLUSDT"}
    Server responds: {"type": "subscribed", ...} then streams candle/depth/trade/stats

    Client sends: {"action": "unsubscribe"}
    Server responds: {"type": "unsubscribed"}
    """
    from nanoedge.api.dependencies import ensure_symbol_infrastructure

    await websocket.accept()
    logger.info("ws_dynamic_connected")

    # Per-client queues for all data types
    candle_queue: asyncio.Queue = asyncio.Queue(maxsize=10)
    depth_queue: asyncio.Queue = asyncio.Queue(maxsize=50)
    trade_queue: asyncio.Queue = asyncio.Queue(maxsize=100)
    stats_queue: asyncio.Queue = asyncio.Queue(maxsize=10)

    current_symbol: str | None = None
    sender_task: asyncio.Task | None = None

    async def cleanup():
        """Remove queues from subscriber sets."""
        nonlocal current_symbol
        if current_symbol:
            app_state.candle_subscribers.get(current_symbol, set()).discard(candle_queue)
            app_state.depth_subscribers.get(current_symbol, set()).discard(depth_queue)
            app_state.trade_subscribers.get(current_symbol, set()).discard(trade_queue)
            app_state.stats_subscribers.get(current_symbol, set()).discard(stats_queue)
            current_symbol = None

    async def subscribe_to_symbol(exchange: str, market: str, symbol: str):
        nonlocal current_symbol

        # Cleanup previous subscription queues
        await cleanup()

        # Ensure infrastructure exists for this symbol
        ensure_symbol_infrastructure(exchange, market, symbol)

        # Register queues for this symbol
        app_state.candle_subscribers[symbol].add(candle_queue)
        app_state.depth_subscribers[symbol].add(depth_queue)
        app_state.trade_subscribers[symbol].add(trade_queue)
        app_state.stats_subscribers[symbol].add(stats_queue)

        current_symbol = symbol

        # Use SubscriptionManager to start feed handler
        if app_state.subscription_manager:
            await app_state.subscription_manager.subscribe(exchange, market, symbol)

        # Auto-backfill on symbol switch (background - doesn't block)
        asyncio.create_task(_backfill_symbol_on_switch(symbol, exchange, market))

        # Send cached stats immediately if available
        if symbol in app_state.latest_stats:
            await websocket.send_bytes(_encode_stats(app_state.latest_stats[symbol]))

        await websocket.send_bytes(encode_subscribed(exchange, market, symbol))
        logger.info("ws_dynamic_subscribed", exchange=exchange, market=market, symbol=symbol)

    async def send_data():
        """Send data from queues to client."""
        # Track current iteration tasks for proper cleanup
        current_tasks: dict[asyncio.Task, str] = {}

        async def cleanup_tasks():
            """Cancel and await all current tasks."""
            for task in current_tasks:
                if not task.done():
                    task.cancel()
            for task in current_tasks:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            current_tasks.clear()

        try:
            while True:
                try:
                    # Create tasks for each queue
                    current_tasks = {
                        asyncio.create_task(candle_queue.get()): "candle",
                        asyncio.create_task(depth_queue.get()): "depth",
                        asyncio.create_task(trade_queue.get()): "trade",
                        asyncio.create_task(stats_queue.get()): "stats",
                    }
                    done, pending = await asyncio.wait(
                        current_tasks.keys(),
                        timeout=QUEUE_TIMEOUT_SECONDS,
                        return_when=asyncio.FIRST_COMPLETED,
                    )

                    # Cancel pending tasks
                    for task in pending:
                        task.cancel()
                    for task in pending:
                        try:
                            await task
                        except asyncio.CancelledError:
                            pass

                    if not done:
                        # Timeout - send heartbeat
                        await websocket.send_bytes(HEARTBEAT_BYTES)
                        current_tasks.clear()
                        continue

                    for task in done:
                        data_type = current_tasks[task]
                        try:
                            data = task.result()
                        except asyncio.CancelledError:
                            continue

                        if data_type == "candle":
                            # Get current candle from aggregator
                            agg = app_state.aggregators.get(current_symbol)
                            if agg:
                                candle = agg.get_current()
                                if candle and candle.timestamp >= MIN_VALID_TIMESTAMP_MS:
                                    await websocket.send_bytes(
                                        encode_candle(
                                            time=candle.timestamp // 1000,
                                            open=candle.open,
                                            high=candle.high,
                                            low=candle.low,
                                            close=candle.close,
                                            volume=candle.volume,
                                            closed=False,
                                            exch_ts=_adjust_exch_ts(candle.timestamp, candle.exchange),  # T0 adjusted
                                            recv_ts=candle.recv_ts_ms,  # T1
                                            api_ts=_get_api_ts_ms(),  # T3
                                        )
                                    )
                        elif data_type == "depth":
                            await websocket.send_bytes(
                                encode_depth(
                                    symbol=data.symbol,
                                    bids=[[level.price, level.size] for level in data.bids],
                                    asks=[[level.price, level.size] for level in data.asks],
                                    last_update_id=data.last_update_id,
                                    exch_ts=_adjust_exch_ts(data.timestamp_ms, data.exchange),  # T0 adjusted
                                    recv_ts=data.recv_ts_ms,  # T1
                                    api_ts=_get_api_ts_ms(),  # T3
                                )
                            )
                        elif data_type == "trade":
                            await websocket.send_bytes(
                                encode_trade(
                                    symbol=data.symbol,
                                    price=data.price,
                                    quantity=data.quantity,
                                    is_buyer_maker=data.is_buyer_maker,
                                    timestamp=_adjust_exch_ts(data.timestamp_ms, data.exchange),  # T0 adjusted
                                    trade_id=data.trade_id,
                                    recv_ts=data.recv_ts_ms,  # T1
                                    api_ts=_get_api_ts_ms(),  # T3
                                )
                            )
                        elif data_type == "stats":
                            await websocket.send_bytes(_encode_stats(data))

                    current_tasks.clear()

                except asyncio.CancelledError:
                    raise  # Re-raise to exit the loop
                except Exception as e:
                    logger.error("ws_dynamic_send_error", error=str(e))
                    break
        finally:
            # Ensure all tasks are cleaned up when function exits
            await cleanup_tasks()

    try:
        # Start sender task
        sender_task = asyncio.create_task(send_data())

        # Receive and process messages
        while True:
            msg = await websocket.receive_json()
            action = msg.get("action")

            if action == "subscribe":
                exchange = msg.get("exchange", "binance")
                market = msg.get("market", "spot")
                symbol = msg.get("symbol")
                if symbol:
                    await subscribe_to_symbol(exchange, market, symbol)

            elif action == "unsubscribe":
                await cleanup()
                await websocket.send_bytes(UNSUBSCRIBED_BYTES)

    except WebSocketDisconnect:
        logger.info("ws_dynamic_disconnected")
    except Exception as e:
        logger.error("ws_dynamic_error", error=str(e))
    finally:
        if sender_task:
            sender_task.cancel()
            try:
                await sender_task
            except asyncio.CancelledError:
                pass
        await cleanup()
