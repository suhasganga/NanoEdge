"""Tick-to-candle OHLCV aggregation."""

import structlog

from nanoedge.core.types import OHLCV, MarketTick

logger = structlog.get_logger(__name__)

# Minimum valid timestamp: Jan 1, 2020 00:00:00 UTC in milliseconds
MIN_VALID_TIMESTAMP_MS = 1577836800000


class StreamingOHLCV:
    """
    Real-time tick-to-candle aggregator for a single symbol.

    Accumulates ticks and produces completed OHLCV candles
    when the interval boundary is crossed.
    """

    __slots__ = (
        "symbol",
        "exchange",
        "market",
        "interval_ms",
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "trade_count",
        "vwap_sum",
    )

    def __init__(
        self,
        symbol: str,
        exchange: str = "binance",
        market: str = "spot",
        interval_ms: int = 60_000,
    ):
        """
        Initialize aggregator for a symbol.

        Args:
            symbol: Trading pair symbol (e.g., "BTCUSDT")
            exchange: Exchange identifier ("binance" or "fyers")
            market: Market type ("spot", "futures", "equity", etc.)
            interval_ms: Candle interval in milliseconds (default: 1 minute)
        """
        self.symbol = symbol
        self.exchange = exchange
        self.market = market
        self.interval_ms = interval_ms

        # Current candle state
        self.open_time: int = 0
        self.open: float = 0.0
        self.high: float = 0.0
        self.low: float = 0.0
        self.close: float = 0.0
        self.volume: float = 0.0
        self.trade_count: int = 0
        self.vwap_sum: float = 0.0  # sum(price * volume) for VWAP calculation

    def _floor_to_interval(self, timestamp_ms: int) -> int:
        """Floor timestamp to interval boundary."""
        return (timestamp_ms // self.interval_ms) * self.interval_ms

    def update(self, tick: MarketTick) -> OHLCV | None:
        """
        Process a tick and return completed candle if interval closed.

        Args:
            tick: MarketTick to process

        Returns:
            Completed OHLCV candle if interval closed, None otherwise
        """
        tick_ms = tick.timestamp_ns // 1_000_000

        # Validate timestamp - skip ticks with invalid timestamps
        if tick_ms < MIN_VALID_TIMESTAMP_MS:
            logger.warning(
                "invalid_tick_timestamp",
                symbol=self.symbol,
                tick_ms=tick_ms,
                timestamp_ns=tick.timestamp_ns,
            )
            return None

        candle_time = self._floor_to_interval(tick_ms)

        # Check if this tick starts a new candle
        if candle_time > self.open_time and self.open_time > 0:
            # Complete previous candle
            completed = self._build_candle()
            self._start_new_candle(candle_time, tick)
            return completed

        if self.open_time == 0:
            # First tick ever
            self._start_new_candle(candle_time, tick)
            return None

        # Update current candle
        self.high = max(self.high, tick.price)
        self.low = min(self.low, tick.price)
        self.close = tick.price
        self.volume += tick.volume
        self.trade_count += 1
        self.vwap_sum += tick.price * tick.volume

        return None

    def _start_new_candle(self, open_time: int, tick: MarketTick) -> None:
        """Start a new candle with the given tick."""
        self.open_time = open_time
        self.open = tick.price
        self.high = tick.price
        self.low = tick.price
        self.close = tick.price
        self.volume = tick.volume
        self.trade_count = 1
        self.vwap_sum = tick.price * tick.volume

    def _build_candle(self) -> OHLCV:
        """Build completed candle from current state."""
        vwap = self.vwap_sum / self.volume if self.volume > 0 else self.close
        return OHLCV(
            timestamp=self.open_time,
            exchange=self.exchange,
            market=self.market,
            symbol=self.symbol,
            open=self.open,
            high=self.high,
            low=self.low,
            close=self.close,
            volume=self.volume,
            trade_count=self.trade_count,
            vwap=vwap,
            is_closed=True,
        )

    def get_current(self) -> OHLCV | None:
        """
        Get current (incomplete) candle state.

        Returns:
            Current OHLCV candle or None if no data yet
        """
        if self.open_time == 0:
            return None

        vwap = self.vwap_sum / self.volume if self.volume > 0 else self.close
        return OHLCV(
            timestamp=self.open_time,
            exchange=self.exchange,
            market=self.market,
            symbol=self.symbol,
            open=self.open,
            high=self.high,
            low=self.low,
            close=self.close,
            volume=self.volume,
            trade_count=self.trade_count,
            vwap=vwap,
            is_closed=False,
        )

    def reset(self) -> None:
        """Reset aggregator state."""
        self.open_time = 0
        self.open = 0.0
        self.high = 0.0
        self.low = 0.0
        self.close = 0.0
        self.volume = 0.0
        self.trade_count = 0
        self.vwap_sum = 0.0
