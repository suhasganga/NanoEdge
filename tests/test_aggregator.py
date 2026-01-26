"""Tests for OHLCV aggregator."""

import pytest

from hft.core.aggregator import StreamingOHLCV
from hft.core.types import MarketTick


class TestStreamingOHLCV:
    """Test cases for StreamingOHLCV aggregator."""

    def test_first_tick_starts_candle(self):
        """First tick should initialize candle state."""
        agg = StreamingOHLCV(symbol="BTCUSDT", interval_ms=60_000)

        # First tick at minute boundary
        tick = MarketTick(
            timestamp_ns=1704067200000 * 1_000_000,  # 2024-01-01 00:00:00
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            volume=1.0,
            side=1,
        )

        result = agg.update(tick)

        assert result is None  # No completed candle
        assert agg.open_time == 1704067200000
        assert agg.open == 50000.0
        assert agg.high == 50000.0
        assert agg.low == 50000.0
        assert agg.close == 50000.0
        assert agg.volume == 1.0
        assert agg.trade_count == 1

    def test_update_within_same_candle(self):
        """Multiple ticks within same interval update candle state."""
        agg = StreamingOHLCV(symbol="BTCUSDT", interval_ms=60_000)

        base_ns = 1704067200000 * 1_000_000

        # First tick
        agg.update(MarketTick(base_ns, "binance", "spot", "BTCUSDT", 50000.0, 1.0, 1))

        # Second tick - higher price
        agg.update(MarketTick(base_ns + 1_000_000_000, "binance", "spot", "BTCUSDT", 50100.0, 0.5, -1))

        # Third tick - lower price
        agg.update(MarketTick(base_ns + 2_000_000_000, "binance", "spot", "BTCUSDT", 49900.0, 2.0, 1))

        candle = agg.get_current()

        assert candle is not None
        assert candle.open == 50000.0
        assert candle.high == 50100.0
        assert candle.low == 49900.0
        assert candle.close == 49900.0
        assert candle.volume == 3.5
        assert candle.trade_count == 3
        assert candle.is_closed is False

    def test_candle_completion_on_new_interval(self):
        """Tick in new interval should complete previous candle."""
        agg = StreamingOHLCV(symbol="BTCUSDT", interval_ms=60_000)

        base_ns = 1704067200000 * 1_000_000  # 00:00:00

        # First minute
        agg.update(MarketTick(base_ns, "binance", "spot", "BTCUSDT", 50000.0, 1.0, 1))
        agg.update(MarketTick(base_ns + 30_000_000_000, "binance", "spot", "BTCUSDT", 50100.0, 0.5, 1))

        # Next minute - should complete first candle
        next_minute_ns = (1704067200000 + 60_000) * 1_000_000  # 00:01:00
        completed = agg.update(
            MarketTick(next_minute_ns, "binance", "spot", "BTCUSDT", 50500.0, 0.5, 1)
        )

        assert completed is not None
        assert completed.is_closed is True
        assert completed.timestamp == 1704067200000
        assert completed.open == 50000.0
        assert completed.high == 50100.0
        assert completed.close == 50100.0

        # Current candle should be the new one
        current = agg.get_current()
        assert current.timestamp == 1704067200000 + 60_000
        assert current.open == 50500.0

    def test_vwap_calculation(self):
        """VWAP should be correctly calculated."""
        agg = StreamingOHLCV(symbol="BTCUSDT", interval_ms=60_000)

        base_ns = 1704067200000 * 1_000_000

        # Price 100 with volume 2 + Price 200 with volume 3
        # VWAP = (100*2 + 200*3) / (2+3) = 800/5 = 160
        agg.update(MarketTick(base_ns, "binance", "spot", "BTCUSDT", 100.0, 2.0, 1))
        agg.update(MarketTick(base_ns + 1_000_000_000, "binance", "spot", "BTCUSDT", 200.0, 3.0, 1))

        candle = agg.get_current()
        assert candle.vwap == pytest.approx(160.0)

    def test_reset_clears_state(self):
        """Reset should clear all candle state."""
        agg = StreamingOHLCV(symbol="BTCUSDT", interval_ms=60_000)

        base_ns = 1704067200000 * 1_000_000
        agg.update(MarketTick(base_ns, "binance", "spot", "BTCUSDT", 50000.0, 1.0, 1))

        assert agg.open_time > 0

        agg.reset()

        assert agg.open_time == 0
        assert agg.get_current() is None
