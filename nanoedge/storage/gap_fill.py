"""Gap detection and backfill service for historical candle data.

Supports multi-exchange backfill:
- Binance: Spot, USDT-M Futures, COIN-M Futures
- Fyers: NSE Equity, F&O, Currency, Commodity

Always fetches 1m candles as the base interval. Higher timeframes
are derived via QuestDB SAMPLE BY.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from nanoedge.core.types import OHLCV

if TYPE_CHECKING:
    from nanoedge.connectors.binance.rest_client import BinanceRestClient
    from nanoedge.connectors.fyers.rest_client import FyersRestClient
    from nanoedge.storage.questdb import QuestDBClient

logger = structlog.get_logger(__name__)

# Interval to milliseconds mapping
INTERVAL_MS = {
    "1m": 60_000,
    "5m": 300_000,
    "15m": 900_000,
    "30m": 1_800_000,
    "1h": 3_600_000,
    "4h": 14_400_000,
    "1d": 86_400_000,
}


def detect_gaps(
    candles: list[dict], interval: str = "1m"
) -> list[tuple[int, int]]:
    """
    Detect time gaps in candle data.

    Args:
        candles: List of candle dicts with 'timestamp' key (in microseconds from QuestDB)
        interval: Candle interval

    Returns:
        List of (start_ms, end_ms) tuples representing gaps
    """
    if len(candles) < 2:
        return []

    interval_ms = INTERVAL_MS.get(interval, 60_000)
    gaps = []

    for i in range(1, len(candles)):
        # QuestDB timestamps are in microseconds, convert to ms
        prev_ts = candles[i - 1].get("timestamp")
        curr_ts = candles[i].get("timestamp")

        if prev_ts is None or curr_ts is None:
            continue

        # Handle string timestamps from QuestDB
        if isinstance(prev_ts, str):
            from datetime import datetime
            prev_ts = int(datetime.fromisoformat(prev_ts.replace("Z", "+00:00")).timestamp() * 1000)
            curr_ts = int(datetime.fromisoformat(curr_ts.replace("Z", "+00:00")).timestamp() * 1000)
        else:
            # Microseconds to milliseconds
            prev_ts = prev_ts // 1000
            curr_ts = curr_ts // 1000

        expected_next = prev_ts + interval_ms
        actual_gap = curr_ts - prev_ts

        # If gap is more than 1 interval, we have missing data
        if actual_gap > interval_ms * 1.5:  # 1.5x tolerance for timing jitter
            gaps.append((expected_next, curr_ts - interval_ms))

    return gaps


async def fetch_missing_candles(
    symbol: str,
    start_ms: int,
    end_ms: int,
    exchange: str = "binance",
    market: str = "spot",
    interval: str = "1m",
    max_candles: int = 50000,
    binance_client: BinanceRestClient | None = None,
    fyers_client: FyersRestClient | None = None,
) -> list[OHLCV]:
    """
    Fetch missing candles from exchange REST API.

    Supports both Binance and Fyers exchanges.

    Args:
        symbol: Trading pair (e.g., "BTCUSDT" or "NSE:RELIANCE-EQ")
        start_ms: Start time in milliseconds
        end_ms: End time in milliseconds
        exchange: Exchange name ("binance" or "fyers")
        market: Market type ("spot", "futures", "equity", etc.)
        interval: Candle interval
        max_candles: Maximum candles to fetch (default 50000 for ~35 days of 1m data)
        binance_client: Binance REST client (required for Binance symbols)
        fyers_client: Fyers REST client (required for Fyers symbols)

    Returns:
        List of OHLCV candles with timestamps in milliseconds
    """
    if exchange == "binance":
        return await _fetch_binance_candles(
            binance_client, symbol, start_ms, end_ms, market, interval, max_candles
        )
    elif exchange == "fyers":
        return await _fetch_fyers_candles(
            fyers_client, symbol, start_ms, end_ms, market, interval, max_candles
        )
    else:
        logger.error("unknown_exchange", exchange=exchange)
        return []


async def _fetch_binance_candles(
    rest_client: BinanceRestClient | None,
    symbol: str,
    start_ms: int,
    end_ms: int,
    market: str,
    interval: str,
    max_candles: int,
) -> list[OHLCV]:
    """Fetch candles from Binance REST API."""
    if not rest_client:
        logger.error("binance_client_not_provided")
        return []

    candles = []
    current_start = start_ms

    while current_start <= end_ms:
        try:
            # Binance API returns max 1000 candles per request
            klines = await rest_client.get_klines(
                symbol=symbol,
                interval=interval,
                start_time=current_start,
                end_time=end_ms,
                limit=1000,
            )

            if not klines:
                break

            for kline in klines:
                # Binance kline format:
                # [open_time, open, high, low, close, volume, close_time,
                #  quote_volume, trades, taker_buy_base, taker_buy_quote, ignore]
                ohlcv = OHLCV(
                    timestamp=int(kline[0]),  # open_time in ms
                    exchange="binance",
                    market=market,
                    symbol=symbol,
                    open=float(kline[1]),
                    high=float(kline[2]),
                    low=float(kline[3]),
                    close=float(kline[4]),
                    volume=float(kline[5]),
                    quote_volume=float(kline[7]),  # quote_volume
                    trade_count=int(kline[8]),
                    vwap=float(kline[4]),  # Use close as approximation
                    is_closed=True,
                )
                candles.append(ohlcv)

            # Move to next batch
            if klines:
                last_open_time = int(klines[-1][0])
                current_start = last_open_time + INTERVAL_MS.get(interval, 60_000)
            else:
                break

            # Prevent infinite loop - higher limit for higher timeframes
            if len(candles) >= max_candles:
                logger.warning(
                    "gap_fill_limit_reached",
                    exchange="binance",
                    count=len(candles),
                    max_candles=max_candles,
                )
                break

        except Exception as e:
            logger.error(
                "binance_gap_fill_error",
                symbol=symbol,
                start=current_start,
                error=str(e),
            )
            break

    return candles


async def _fetch_fyers_candles(
    rest_client: FyersRestClient | None,
    symbol: str,
    start_ms: int,
    end_ms: int,
    market: str,
    interval: str,
    max_candles: int,
) -> list[OHLCV]:
    """
    Fetch candles from Fyers REST API.

    Note: Fyers API has a 100-day limit for minute data per request.
    We paginate to handle larger ranges.
    """
    if not rest_client:
        logger.error("fyers_client_not_provided")
        return []

    candles = []
    current_start = start_ms

    # Fyers allows ~100 days of 1m data per request
    # For safety, request 90 days at a time
    MAX_RANGE_MS = 90 * 24 * 60 * 60 * 1000  # 90 days in ms

    while current_start <= end_ms:
        try:
            # Calculate chunk end (max 90 days)
            chunk_end = min(current_start + MAX_RANGE_MS, end_ms)

            # Fyers get_klines already converts ms to seconds internally
            # and returns candles with ms timestamps
            chunk_candles = await rest_client.get_klines(
                symbol=symbol,
                interval=interval,
                start_time=current_start,
                end_time=chunk_end,
            )

            if not chunk_candles:
                # No more data, move to next chunk
                current_start = chunk_end + INTERVAL_MS.get(interval, 60_000)
                continue

            candles.extend(chunk_candles)

            # Move to next batch
            last_timestamp = chunk_candles[-1].timestamp
            current_start = last_timestamp + INTERVAL_MS.get(interval, 60_000)

            # Prevent infinite loop
            if len(candles) >= max_candles:
                logger.warning(
                    "gap_fill_limit_reached",
                    exchange="fyers",
                    count=len(candles),
                    max_candles=max_candles,
                )
                break

        except Exception as e:
            logger.error(
                "fyers_gap_fill_error",
                symbol=symbol,
                start=current_start,
                error=str(e),
            )
            break

    return candles


async def backfill_gaps(
    questdb: QuestDBClient,
    symbol: str,
    candles: list[dict],
    exchange: str = "binance",
    market: str = "spot",
    interval: str = "1m",
    binance_client: BinanceRestClient | None = None,
    fyers_client: FyersRestClient | None = None,
) -> int:
    """
    Detect and fill gaps in candle data.

    Args:
        questdb: QuestDB client
        symbol: Trading pair
        candles: Existing candles from QuestDB (can be any interval)
        exchange: Exchange name ("binance" or "fyers")
        market: Market type ("spot", "futures", "equity", etc.)
        interval: Candle interval of the provided candles
        binance_client: Binance REST client (for Binance symbols)
        fyers_client: Fyers REST client (for Fyers symbols)

    Returns:
        Number of 1m candles backfilled
    """
    gaps = detect_gaps(candles, interval)

    if not gaps:
        return 0

    logger.info(
        "gaps_detected",
        exchange=exchange,
        symbol=symbol,
        gap_count=len(gaps),
        display_interval=interval,
    )

    total_filled = 0

    for start_ms, end_ms in gaps:
        # Always fetch 1m candles (base interval)
        missing = await fetch_missing_candles(
            symbol=symbol,
            start_ms=start_ms,
            end_ms=end_ms,
            exchange=exchange,
            market=market,
            interval="1m",  # Always backfill 1m data
            binance_client=binance_client,
            fyers_client=fyers_client,
        )

        if missing:
            # Write to QuestDB
            written = questdb.write_candles_batch(missing)
            total_filled += written

            logger.info(
                "gap_filled",
                exchange=exchange,
                symbol=symbol,
                start_ms=start_ms,
                end_ms=end_ms,
                candles_written=written,
            )

    return total_filled


async def backfill_time_range(
    questdb: QuestDBClient,
    symbol: str,
    start_ms: int,
    end_ms: int,
    exchange: str = "binance",
    market: str = "spot",
    binance_client: BinanceRestClient | None = None,
    fyers_client: FyersRestClient | None = None,
) -> tuple[int, list[OHLCV]]:
    """
    Backfill 1m candles for an entire time range.

    Used when no data exists for a requested period.

    Args:
        questdb: QuestDB client
        symbol: Trading pair
        start_ms: Start time in milliseconds
        end_ms: End time in milliseconds
        exchange: Exchange name ("binance" or "fyers")
        market: Market type ("spot", "futures", "equity", etc.)
        binance_client: Binance REST client (for Binance symbols)
        fyers_client: Fyers REST client (for Fyers symbols)

    Returns:
        Tuple of (count of candles written, list of OHLCV candles)
        Returns candles directly to avoid QuestDB WAL commit delay
    """
    # Always fetch 1m candles
    missing = await fetch_missing_candles(
        symbol=symbol,
        start_ms=start_ms,
        end_ms=end_ms,
        exchange=exchange,
        market=market,
        interval="1m",
        binance_client=binance_client,
        fyers_client=fyers_client,
    )

    if missing:
        written = questdb.write_candles_batch(missing)
        logger.info(
            "time_range_backfilled",
            exchange=exchange,
            symbol=symbol,
            start_ms=start_ms,
            end_ms=end_ms,
            candles_written=written,
        )
        return written, missing

    return 0, []


def infer_exchange_from_symbol(symbol: str) -> tuple[str, str]:
    """
    Infer exchange and market from symbol format.

    Args:
        symbol: Trading symbol

    Returns:
        Tuple of (exchange, market)

    Examples:
        - "BTCUSDT" → ("binance", "spot")
        - "NSE:RELIANCE-EQ" → ("fyers", "equity")
        - "NSE:NIFTY25JANFUT" → ("fyers", "futures")
        - "MCX:GOLD" → ("fyers", "commodity")
    """
    symbol_upper = symbol.upper()

    # Fyers symbols have exchange prefix
    if symbol_upper.startswith("NSE:") or symbol_upper.startswith("BSE:"):
        if "-EQ" in symbol_upper:
            return "fyers", "equity"
        elif "-INDEX" in symbol_upper:
            return "fyers", "index"
        elif "FUT" in symbol_upper:
            return "fyers", "futures"
        elif "CE" in symbol_upper or "PE" in symbol_upper:
            return "fyers", "options"
        else:
            return "fyers", "equity"

    elif symbol_upper.startswith("MCX:"):
        if "CE" in symbol_upper or "PE" in symbol_upper:
            return "fyers", "options"
        return "fyers", "commodity"

    # Default to Binance spot
    return "binance", "spot"
