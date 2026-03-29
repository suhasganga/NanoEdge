"""Tick-to-candle aggregator for Fyers data.

Since Fyers WebSocket only provides tick data (no @kline_1m stream like Binance),
we must aggregate ticks into candles ourselves.
"""

from collections.abc import Callable

import structlog

from nanoedge.core.types import OHLCV, MarketTick

logger = structlog.get_logger(__name__)

# Minimum valid timestamp: Jan 1, 2020 00:00:00 UTC in milliseconds
MIN_VALID_TIMESTAMP_MS = 1577836800000


class FyersOHLCVAggregator:
    """
    Aggregates Fyers ticks into 1-minute candles.

    Unlike Binance (which sends complete candles via @kline_1m),
    Fyers only sends tick data. We must:
    1. Aggregate ticks into candles
    2. Flush completed candles on minute boundary
    3. Write to QuestDB when candle closes

    Usage:
        aggregator = FyersOHLCVAggregator(
            symbol="NSE:RELIANCE-EQ",
            on_candle_close=lambda c: questdb.write_candle(c),
        )

        # On each tick from WebSocket
        completed = aggregator.update(tick)
        if completed:
            print(f"Candle closed: {completed}")
    """

    __slots__ = (
        "symbol",
        "exchange",
        "market",
        "interval_ms",
        "on_candle_close",
        "_current_candle",
        "_current_minute",
        "_tick_count",
        "_volume_sum",
    )

    def __init__(
        self,
        symbol: str,
        exchange: str = "fyers",
        market: str | None = None,
        interval_ms: int = 60_000,
        on_candle_close: Callable[[OHLCV], None] | None = None,
    ):
        """
        Initialize Fyers OHLCV aggregator.

        Args:
            symbol: Fyers symbol (e.g., "NSE:RELIANCE-EQ")
            exchange: Exchange name (default: "fyers")
            market: Market type (auto-detected if None)
            interval_ms: Candle interval in milliseconds (default: 60000 = 1 minute)
            on_candle_close: Callback when candle closes (e.g., write to DB)
        """
        self.symbol = symbol
        self.exchange = exchange
        self.market = market or self._detect_market(symbol)
        self.interval_ms = interval_ms
        self.on_candle_close = on_candle_close

        # Current candle state
        self._current_candle: OHLCV | None = None
        self._current_minute: int = 0
        self._tick_count: int = 0
        self._volume_sum: float = 0.0  # sum(price * volume) for VWAP

    def _detect_market(self, symbol: str) -> str:
        """Detect market type from symbol format."""
        symbol_upper = symbol.upper()
        if "-EQ" in symbol_upper:
            return "equity"
        elif "-INDEX" in symbol_upper:
            return "index"
        elif "FUT" in symbol_upper:
            return "futures"
        elif "CE" in symbol_upper or "PE" in symbol_upper:
            return "options"
        elif symbol_upper.startswith("MCX:"):
            return "commodity"
        return "equity"

    def update(self, tick: MarketTick) -> OHLCV | None:
        """
        Update aggregator with new tick.

        Args:
            tick: Market tick with timestamp_ns, price, volume

        Returns:
            Completed candle if minute boundary crossed, None otherwise
        """
        tick_ms = tick.timestamp_ns // 1_000_000
        tick_minute = tick_ms // self.interval_ms

        # Validate timestamp (reject pre-2020 data)
        if tick_ms < MIN_VALID_TIMESTAMP_MS:
            logger.warning(
                "fyers_invalid_tick_timestamp",
                symbol=self.symbol,
                tick_ms=tick_ms,
            )
            return None

        # Check if we crossed minute boundary
        completed_candle = None
        if self._current_minute != 0 and tick_minute > self._current_minute:
            # Close current candle
            if self._current_candle:
                self._current_candle.is_closed = True
                completed_candle = self._current_candle

                # Callback to write to DB
                if self.on_candle_close:
                    try:
                        self.on_candle_close(completed_candle)
                    except Exception as e:
                        logger.error(
                            "fyers_candle_close_callback_error",
                            symbol=self.symbol,
                            error=str(e),
                        )

                logger.info(
                    "fyers_candle_closed",
                    symbol=self.symbol,
                    timestamp=self._current_candle.timestamp,
                    open=self._current_candle.open,
                    close=self._current_candle.close,
                    volume=self._current_candle.volume,
                    trades=self._current_candle.trade_count,
                )

            # Reset for new candle
            self._current_candle = None

        # Initialize or update current candle
        if self._current_candle is None:
            candle_open_ms = tick_minute * self.interval_ms
            self._current_candle = OHLCV(
                timestamp=candle_open_ms,
                exchange=self.exchange,
                market=self.market,
                symbol=self.symbol,
                open=tick.price,
                high=tick.price,
                low=tick.price,
                close=tick.price,
                volume=tick.volume,
                trade_count=1,
                vwap=tick.price,
                is_closed=False,
            )
            self._current_minute = tick_minute
            self._tick_count = 1
            self._volume_sum = tick.price * tick.volume
        else:
            # Update OHLCV
            self._current_candle.high = max(self._current_candle.high, tick.price)
            self._current_candle.low = min(self._current_candle.low, tick.price)
            self._current_candle.close = tick.price
            self._current_candle.volume += tick.volume
            self._current_candle.trade_count += 1
            self._tick_count += 1
            self._volume_sum += tick.price * tick.volume
            self._current_candle.vwap = (
                self._volume_sum / self._current_candle.volume
                if self._current_candle.volume > 0
                else tick.price
            )

        return completed_candle

    def get_current(self) -> OHLCV | None:
        """
        Get current partial candle for UI updates.

        Returns:
            Current incomplete candle or None if no data yet
        """
        return self._current_candle

    def flush(self) -> OHLCV | None:
        """
        Force-close current candle (e.g., on market close or disconnect).

        Returns:
            Completed candle or None if no data
        """
        if self._current_candle:
            self._current_candle.is_closed = True
            completed = self._current_candle

            if self.on_candle_close:
                try:
                    self.on_candle_close(completed)
                except Exception as e:
                    logger.error(
                        "fyers_candle_flush_callback_error",
                        symbol=self.symbol,
                        error=str(e),
                    )

            logger.info(
                "fyers_candle_flushed",
                symbol=self.symbol,
                timestamp=completed.timestamp,
            )

            self._current_candle = None
            self._current_minute = 0
            self._tick_count = 0
            self._volume_sum = 0.0
            return completed

        return None

    def reset(self) -> None:
        """Reset aggregator state without emitting candle."""
        self._current_candle = None
        self._current_minute = 0
        self._tick_count = 0
        self._volume_sum = 0.0
