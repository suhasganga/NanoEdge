"""Historical data REST endpoints."""

import time as time_module
from datetime import datetime

import structlog
from fastapi import APIRouter, HTTPException, Query

from hft.api.dependencies import app_state, _broadcast_stats
from hft.storage.gap_fill import (
    INTERVAL_MS,
    backfill_gaps,
    backfill_time_range,
    detect_gaps,
    fetch_missing_candles,
    infer_exchange_from_symbol,
)

from hft.core.types import OHLCV, MarketStats

logger = structlog.get_logger(__name__)
router = APIRouter()


def calculate_stats_from_candles(
    candles: list[OHLCV],
    symbol: str,
    exchange: str,
    market: str,
) -> MarketStats | None:
    """
    Calculate 24h market statistics from historical candles.

    Used to provide stats for symbols when live WebSocket data is not available
    (e.g., Indian stocks when market is closed).

    Args:
        candles: List of 1m OHLCV candles (should cover at least 24h)
        symbol: Trading symbol
        exchange: Exchange name
        market: Market type

    Returns:
        MarketStats with calculated values, or None if insufficient data
    """
    if not candles:
        return None

    # Get candles from last 24 hours
    now_ms = int(time_module.time() * 1000)
    ms_24h = 24 * 60 * 60 * 1000
    cutoff_ms = now_ms - ms_24h

    # Filter to 24h window
    candles_24h = [c for c in candles if c.timestamp >= cutoff_ms]

    # If no 24h candles, use all available candles
    if not candles_24h:
        candles_24h = candles

    if not candles_24h:
        return None

    # Sort by timestamp to ensure correct order
    candles_24h = sorted(candles_24h, key=lambda c: c.timestamp)

    # Calculate stats
    first_candle = candles_24h[0]
    last_candle = candles_24h[-1]

    open_price = first_candle.open
    last_price = last_candle.close
    high_24h = max(c.high for c in candles_24h)
    low_24h = min(c.low for c in candles_24h)
    volume_24h = sum(c.volume for c in candles_24h)
    quote_volume_24h = sum(c.quote_volume for c in candles_24h)
    trade_count_24h = sum(c.trade_count for c in candles_24h)

    price_change = last_price - open_price
    price_change_percent = (price_change / open_price * 100) if open_price > 0 else 0.0

    return MarketStats(
        timestamp_ms=now_ms,
        exchange=exchange,
        market=market,
        symbol=symbol,
        price_change=price_change,
        price_change_percent=price_change_percent,
        high_24h=high_24h,
        low_24h=low_24h,
        volume_24h=volume_24h,
        quote_volume_24h=quote_volume_24h,
        trade_count_24h=trade_count_24h,
        last_price=last_price,
        open_price=open_price,
    )


def _calculate_stats_from_formatted(
    candles: list[dict],
    symbol: str,
    exchange: str,
    market: str,
) -> MarketStats | None:
    """
    Calculate 24h stats from formatted candle dicts (from QuestDB).

    Args:
        candles: List of formatted candle dicts with time in seconds
        symbol: Trading symbol
        exchange: Exchange name
        market: Market type

    Returns:
        MarketStats or None if insufficient data
    """
    if not candles:
        return None

    now_sec = int(time_module.time())
    sec_24h = 24 * 60 * 60
    cutoff_sec = now_sec - sec_24h

    # Filter to 24h window
    candles_24h = [c for c in candles if c.get("time", 0) >= cutoff_sec]

    # Use all candles if no 24h data
    if not candles_24h:
        candles_24h = candles

    if not candles_24h:
        return None

    # Sort by time
    candles_24h = sorted(candles_24h, key=lambda c: c.get("time", 0))

    first = candles_24h[0]
    last = candles_24h[-1]

    open_price = first.get("open", 0)
    last_price = last.get("close", 0)
    high_24h = max(c.get("high", 0) for c in candles_24h)
    low_24h = min(c.get("low", float("inf")) for c in candles_24h)
    volume_24h = sum(c.get("volume", 0) for c in candles_24h)

    price_change = last_price - open_price
    price_change_percent = (price_change / open_price * 100) if open_price > 0 else 0.0

    return MarketStats(
        timestamp_ms=int(now_sec * 1000),
        exchange=exchange,
        market=market,
        symbol=symbol,
        price_change=price_change,
        price_change_percent=price_change_percent,
        high_24h=high_24h,
        low_24h=low_24h if low_24h != float("inf") else 0,
        volume_24h=volume_24h,
        quote_volume_24h=0,  # Not available from candle data
        trade_count_24h=0,  # Not available from candle data
        last_price=last_price,
        open_price=open_price,
    )


async def _fetch_24h_stats(
    symbol: str,
    exchange: str,
    market: str,
) -> MarketStats | None:
    """
    Fetch and calculate 24h stats from QuestDB.

    Always queries the last 24h of 1m candles regardless of what the user is viewing.
    This ensures stats are accurate and don't change when panning the chart.
    """
    if app_state.questdb is None:
        return None

    # Always fetch last 24h of 1m candles for stats
    now_sec = int(time_module.time())
    start_sec = now_sec - (24 * 60 * 60)

    candles = await app_state.questdb.query_candles(
        symbol=symbol,
        interval="1m",  # Always use 1m for accurate stats
        limit=1440,  # 24 hours of 1m candles
        start_time=start_sec,
        end_time=now_sec,
        exchange=exchange,
        market=market,
    )

    if not candles:
        return None

    # Convert QuestDB results to stats
    # Timestamps from QuestDB are in microseconds or ISO format
    now_ms = now_sec * 1000
    ms_24h = 24 * 60 * 60 * 1000
    cutoff_ms = now_ms - ms_24h

    # Parse timestamps and filter
    valid_candles = []
    for c in candles:
        ts = c.get("timestamp")
        if ts is None:
            continue

        # Convert timestamp to milliseconds
        if isinstance(ts, int):
            ts_ms = ts // 1000  # microseconds to ms
        elif isinstance(ts, str):
            from datetime import datetime
            dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            ts_ms = int(dt.timestamp() * 1000)
        else:
            continue

        if ts_ms >= cutoff_ms:
            valid_candles.append({
                "timestamp_ms": ts_ms,
                "open": c.get("open", 0),
                "high": c.get("high", 0),
                "low": c.get("low", 0),
                "close": c.get("close", 0),
                "volume": c.get("volume", 0),
            })

    if not valid_candles:
        return None

    # Sort by timestamp
    valid_candles.sort(key=lambda x: x["timestamp_ms"])

    first = valid_candles[0]
    last = valid_candles[-1]

    open_price = first["open"]
    last_price = last["close"]
    high_24h = max(c["high"] for c in valid_candles)
    low_24h = min(c["low"] for c in valid_candles)
    volume_24h = sum(c["volume"] for c in valid_candles)

    price_change = last_price - open_price
    price_change_percent = (price_change / open_price * 100) if open_price > 0 else 0.0

    return MarketStats(
        timestamp_ms=now_ms,
        exchange=exchange,
        market=market,
        symbol=symbol,
        price_change=price_change,
        price_change_percent=price_change_percent,
        high_24h=high_24h,
        low_24h=low_24h,
        volume_24h=volume_24h,
        quote_volume_24h=0,
        trade_count_24h=0,
        last_price=last_price,
        open_price=open_price,
    )


def _aggregate_candles(candles: list[OHLCV], interval: str, limit: int) -> list[dict]:
    """
    Aggregate 1m candles into higher timeframes.

    This is used when returning backfilled data directly from memory
    to avoid QuestDB WAL commit delay.

    Args:
        candles: List of 1m OHLCV candles
        interval: Target interval (5m, 15m, 1h, etc.)
        limit: Maximum number of candles to return

    Returns:
        List of aggregated candle dicts formatted for TradingView
    """
    if not candles:
        return []

    interval_ms = INTERVAL_MS.get(interval, 60_000)

    # Group candles by interval bucket
    buckets: dict[int, list[OHLCV]] = {}
    for c in candles:
        bucket_time = (c.timestamp // interval_ms) * interval_ms
        if bucket_time not in buckets:
            buckets[bucket_time] = []
        buckets[bucket_time].append(c)

    # Aggregate each bucket
    aggregated = []
    for bucket_time in sorted(buckets.keys()):
        bucket_candles = buckets[bucket_time]
        if not bucket_candles:
            continue

        agg = {
            "time": bucket_time // 1000,  # ms to seconds for TradingView
            "open": bucket_candles[0].open,
            "high": max(c.high for c in bucket_candles),
            "low": min(c.low for c in bucket_candles),
            "close": bucket_candles[-1].close,
            "volume": sum(c.volume for c in bucket_candles),
        }
        aggregated.append(agg)

    # Apply limit (return most recent)
    return aggregated[-limit:]


@router.get("/history")
async def get_history(
    symbol: str = Query(..., description="Trading pair (e.g., BTCUSDT)"),
    interval: str = Query("1m", description="Candle interval: 1m, 5m, 15m, 1h, 1d"),
    limit: int = Query(500, ge=1, le=1000, description="Number of candles"),
    start_time: int | None = Query(None, description="Start time (Unix seconds)"),
    end_time: int | None = Query(None, description="End time (Unix seconds)"),
    backfill: bool = Query(True, description="Auto-backfill gaps from Binance"),
):
    """
    Get historical OHLCV candles from QuestDB.

    Returns candles in chronological order (oldest first) formatted for
    TradingView Lightweight Charts (time in Unix seconds).

    If gaps are detected in the data and backfill=True, missing candles
    will be automatically fetched from Binance and stored in QuestDB.
    """
    if app_state.questdb is None:
        raise HTTPException(status_code=503, detail="Database not available")

    # Validate interval
    valid_intervals = {"1m", "5m", "15m", "30m", "1h", "4h", "1d"}
    if interval not in valid_intervals:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid interval. Must be one of: {', '.join(valid_intervals)}",
        )

    symbol = symbol.upper()

    # Detect exchange from symbol format
    detected_exchange, detected_market = infer_exchange_from_symbol(symbol)

    candles = await app_state.questdb.query_candles(
        symbol=symbol,
        interval=interval,
        limit=limit,
        start_time=start_time,
        end_time=end_time,
    )

    # Backfill logic - always fetch 1m candles, display any interval
    # Check for appropriate client based on detected exchange
    has_client = (
        (detected_exchange == "binance" and app_state.rest_client)
        or (detected_exchange == "fyers" and app_state.fyers_rest_client)
    )
    if backfill and has_client:
        interval_ms = INTERVAL_MS.get(interval, 60_000)
        expected_candles = limit

        # Calculate time range for backfill based on requested interval
        if end_time:
            end_ms = end_time * 1000
        else:
            end_ms = int(time_module.time() * 1000)

        if start_time:
            start_ms = start_time * 1000
        else:
            # Calculate start based on limit and interval
            start_ms = end_ms - (limit * interval_ms)

        # Case 1: No data at all - fetch 1m candles for entire range
        if not candles:
            logger.info(
                "history_no_data",
                symbol=symbol,
                interval=interval,
                start_ms=start_ms,
                end_ms=end_ms,
            )
            # Clear Fyers cache for this symbol to ensure fresh fetch
            # This handles the case where user switches back to a symbol
            # and QuestDB hasn't committed the data yet (WAL delay)
            if detected_exchange == "fyers" and app_state.fyers_rest_client:
                app_state.fyers_rest_client.clear_cache(symbol)

            # Always backfill 1m candles - returns candles directly to avoid WAL delay
            written, backfilled_candles = await backfill_time_range(
                questdb=app_state.questdb,
                symbol=symbol,
                start_ms=start_ms,
                end_ms=end_ms,
                exchange=detected_exchange,
                market=detected_market,
                binance_client=app_state.rest_client if detected_exchange == "binance" else None,
                fyers_client=app_state.fyers_rest_client if detected_exchange == "fyers" else None,
            )
            if written > 0 and backfilled_candles:
                logger.info(
                    "history_fetched_from_exchange",
                    exchange=detected_exchange,
                    symbol=symbol,
                    interval=interval,
                    candles_written=written,
                )

                # Calculate and cache 24h stats if not already cached
                # Use dedicated function that always fetches proper 24h window
                if symbol not in app_state.latest_stats:
                    stats = await _fetch_24h_stats(
                        symbol, detected_exchange, detected_market
                    )
                    if stats:
                        app_state.latest_stats[symbol] = stats
                        _broadcast_stats(symbol, stats)
                        logger.info(
                            "stats_calculated_24h",
                            symbol=symbol,
                            last_price=stats.last_price,
                            change_pct=stats.price_change_percent,
                        )

                # Return backfilled candles directly (avoids QuestDB WAL commit delay)
                # For 1m interval, return directly; for higher intervals, aggregate in Python
                if interval == "1m":
                    # Return OHLCV objects directly formatted for TradingView
                    return [
                        {
                            "time": c.timestamp // 1000,  # ms to seconds
                            "open": c.open,
                            "high": c.high,
                            "low": c.low,
                            "close": c.close,
                            "volume": c.volume,
                        }
                        for c in backfilled_candles[-limit:]  # Apply limit
                    ]
                else:
                    # For higher timeframes, aggregate the 1m candles in Python
                    aggregated = _aggregate_candles(backfilled_candles, interval, limit)
                    return aggregated

        # Case 2: Have some data but less than expected - check for gaps
        elif len(candles) < expected_candles * 0.9:  # Less than 90% of expected
            gaps = detect_gaps(candles, interval)
            if gaps:
                logger.info(
                    "history_gaps_detected",
                    symbol=symbol,
                    interval=interval,
                    gap_count=len(gaps),
                    candles_found=len(candles),
                    expected=expected_candles,
                )
                # Backfill gaps with 1m candles
                filled = await backfill_gaps(
                    questdb=app_state.questdb,
                    symbol=symbol,
                    candles=candles,
                    exchange=detected_exchange,
                    market=detected_market,
                    interval=interval,
                    binance_client=app_state.rest_client if detected_exchange == "binance" else None,
                    fyers_client=app_state.fyers_rest_client if detected_exchange == "fyers" else None,
                )
                if filled > 0:
                    candles = await app_state.questdb.query_candles(
                        symbol=symbol,
                        interval=interval,
                        limit=limit,
                        start_time=start_time,
                        end_time=end_time,
                    )
                    logger.info(
                        "history_gaps_filled",
                        symbol=symbol,
                        interval=interval,
                        candles_added=filled,
                    )

        # Case 3: Have data but check for gaps anyway
        elif candles:
            gaps = detect_gaps(candles, interval)
            if gaps:
                logger.info(
                    "history_gaps_detected",
                    symbol=symbol,
                    interval=interval,
                    gap_count=len(gaps),
                )
                # Backfill gaps with 1m candles
                filled = await backfill_gaps(
                    questdb=app_state.questdb,
                    symbol=symbol,
                    candles=candles,
                    exchange=detected_exchange,
                    market=detected_market,
                    interval=interval,
                    binance_client=app_state.rest_client if detected_exchange == "binance" else None,
                    fyers_client=app_state.fyers_rest_client if detected_exchange == "fyers" else None,
                )
                if filled > 0:
                    candles = await app_state.questdb.query_candles(
                        symbol=symbol,
                        interval=interval,
                        limit=limit,
                        start_time=start_time,
                        end_time=end_time,
                    )
                    logger.info(
                        "history_gaps_filled",
                        symbol=symbol,
                        interval=interval,
                        candles_added=filled,
                    )

    # Format for TradingView (time in seconds)
    formatted = []
    for c in candles:
        # QuestDB returns timestamp in microseconds
        ts = c.get("timestamp")
        if ts is None:
            continue

        # Convert to seconds for TradingView
        if isinstance(ts, int):
            time_sec = ts // 1_000_000  # microseconds to seconds
        elif isinstance(ts, str):
            # Handle ISO format timestamp from QuestDB (e.g., '2026-01-19T18:45:00.000000Z')
            dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            time_sec = int(dt.timestamp())
        else:
            continue

        formatted.append(
            {
                "time": time_sec,
                "open": c.get("open", 0),
                "high": c.get("high", 0),
                "low": c.get("low", 0),
                "close": c.get("close", 0),
                "volume": c.get("volume", 0),
            }
        )

    # Calculate and cache 24h stats if not already cached
    # Use dedicated function that always fetches proper 24h window (not affected by pan)
    if symbol not in app_state.latest_stats:
        stats = await _fetch_24h_stats(symbol, detected_exchange, detected_market)
        if stats:
            app_state.latest_stats[symbol] = stats
            _broadcast_stats(symbol, stats)
            logger.info(
                "stats_calculated_24h",
                symbol=symbol,
                last_price=stats.last_price,
                change_pct=stats.price_change_percent,
            )

    return formatted


@router.post("/backfill")
async def backfill_history(
    symbol: str = Query(..., description="Trading pair (e.g., BTCUSDT or NSE:RELIANCE-EQ)"),
    hours: int = Query(24, ge=1, le=168, description="Hours of history to fetch (max 168 = 1 week)"),
):
    """
    Manually backfill historical candles from exchange.

    Fetches the specified hours of 1m candle history and stores in QuestDB.
    Useful for initial setup or filling large gaps.
    Automatically detects exchange (Binance/Fyers) from symbol format.
    """
    if app_state.questdb is None:
        raise HTTPException(status_code=503, detail="Database not available")

    symbol = symbol.upper()

    # Detect exchange from symbol format
    detected_exchange, detected_market = infer_exchange_from_symbol(symbol)

    # Check for appropriate client
    if detected_exchange == "binance" and not app_state.rest_client:
        raise HTTPException(status_code=503, detail="Binance REST client not available")
    if detected_exchange == "fyers" and not app_state.fyers_rest_client:
        raise HTTPException(status_code=503, detail="Fyers REST client not available")

    # Calculate time range
    end_ms = int(time_module.time() * 1000)
    start_ms = end_ms - (hours * 3600 * 1000)

    try:
        candles = await fetch_missing_candles(
            symbol=symbol,
            start_ms=start_ms,
            end_ms=end_ms,
            exchange=detected_exchange,
            market=detected_market,
            interval="1m",
            binance_client=app_state.rest_client if detected_exchange == "binance" else None,
            fyers_client=app_state.fyers_rest_client if detected_exchange == "fyers" else None,
        )

        if candles:
            written = app_state.questdb.write_candles_batch(candles)
            logger.info(
                "manual_backfill_complete",
                symbol=symbol,
                exchange=detected_exchange,
                hours=hours,
                candles_written=written,
            )
            return {
                "status": "success",
                "symbol": symbol,
                "exchange": detected_exchange,
                "hours": hours,
                "candles_written": written,
            }
        else:
            return {
                "status": "no_data",
                "symbol": symbol,
                "exchange": detected_exchange,
                "hours": hours,
                "candles_written": 0,
            }

    except Exception as e:
        logger.error("manual_backfill_error", symbol=symbol, error=str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/active-symbols")
async def get_active_symbols():
    """
    Get list of currently active/subscribed symbols.

    These are symbols with live data feeds. For the full symbol catalog,
    use /api/symbols (all symbols) or /api/symbols/search (search).
    """
    return {"symbols": list(app_state.aggregators.keys())}


@router.get("/status")
async def get_status():
    """Get system status."""
    status = {
        "symbols": list(app_state.aggregators.keys()),
        "feed_connected": (
            app_state.feed_handler.is_connected if app_state.feed_handler else False
        ),
        "orderbooks": {},
        "tick_buffer_size": len(app_state.tick_buffer) if app_state.tick_buffer else 0,
    }

    for symbol, ob in app_state.orderbooks.items():
        status["orderbooks"][symbol] = {
            "initialized": ob.is_initialized,
            "best_bid": ob.best_bid,
            "best_ask": ob.best_ask,
            "spread": ob.spread,
        }

    return status


@router.get("/metrics")
async def get_metrics():
    """
    Get current latency metrics for performance monitoring.

    Returns p50, p95, p99, mean, min, and max latencies in microseconds
    for all tracked pipeline stages.
    """
    from hft.core.metrics import metrics

    def histogram_to_dict(hist) -> dict:
        """Convert LatencyHistogram to dict."""
        return {
            "count": hist.count,
            "current_samples": hist.current_samples,
            "p50_us": round(hist.p50, 2),
            "p95_us": round(hist.p95, 2),
            "p99_us": round(hist.p99, 2),
            "mean_us": round(hist.mean, 2),
            "min_us": round(hist.min_latency, 2),
            "max_us": round(hist.max_latency, 2),
        }

    return {
        "parse_json": histogram_to_dict(metrics.parse_json_latency),
        "api_ws_push": histogram_to_dict(metrics.api_ws_push_latency),
        "orderbook_update": histogram_to_dict(metrics.orderbook_update_latency),
        "ws_network": histogram_to_dict(metrics.ws_network_latency),
        "db_write": histogram_to_dict(metrics.db_write_latency),
        "normalize": histogram_to_dict(metrics.normalize_latency),
        "agg_update": histogram_to_dict(metrics.agg_update_latency),
    }
