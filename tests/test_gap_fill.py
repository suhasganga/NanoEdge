"""Tests for gap detection and backfill service."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from hft.core.types import OHLCV
from hft.storage.gap_fill import (
    INTERVAL_MS,
    backfill_gaps,
    backfill_time_range,
    detect_gaps,
    fetch_missing_candles,
    infer_exchange_from_symbol,
)


class TestDetectGaps:
    """Tests for detect_gaps function."""

    def test_empty_candles(self):
        """Empty candle list returns no gaps."""
        gaps = detect_gaps([])
        assert gaps == []

    def test_single_candle(self):
        """Single candle returns no gaps."""
        candles = [{"timestamp": 1704067200000000}]  # microseconds
        gaps = detect_gaps(candles)
        assert gaps == []

    def test_no_gaps(self):
        """Consecutive candles return no gaps."""
        # 1m interval = 60_000 ms = 60_000_000 μs
        candles = [
            {"timestamp": 1704067200000000},  # 00:00
            {"timestamp": 1704067260000000},  # 00:01
            {"timestamp": 1704067320000000},  # 00:02
            {"timestamp": 1704067380000000},  # 00:03
        ]
        gaps = detect_gaps(candles, interval="1m")
        assert gaps == []

    def test_single_gap(self):
        """Detect single gap in candle sequence."""
        candles = [
            {"timestamp": 1704067200000000},  # 00:00
            {"timestamp": 1704067260000000},  # 00:01
            {"timestamp": 1704067500000000},  # 00:05 (gap of 4 minutes)
            {"timestamp": 1704067560000000},  # 00:06
        ]
        gaps = detect_gaps(candles, interval="1m")
        assert len(gaps) == 1
        # Gap should start after 00:01 and end before 00:05
        start_ms, end_ms = gaps[0]
        assert start_ms == 1704067320000  # Expected: 00:02
        assert end_ms == 1704067440000  # Expected: 00:04

    def test_multiple_gaps(self):
        """Detect multiple gaps in candle sequence."""
        candles = [
            {"timestamp": 1704067200000000},  # 00:00
            {"timestamp": 1704067500000000},  # 00:05 (gap 1)
            {"timestamp": 1704067800000000},  # 00:10 (gap 2)
        ]
        gaps = detect_gaps(candles, interval="1m")
        assert len(gaps) == 2

    def test_1_5x_tolerance(self):
        """Small timing jitter (< 1.5x interval) is not a gap."""
        # 80 seconds apart (< 90 seconds = 1.5 * 60)
        candles = [
            {"timestamp": 1704067200000000},  # 00:00:00
            {"timestamp": 1704067280000000},  # 00:01:20 (80s later, but <1.5x)
        ]
        gaps = detect_gaps(candles, interval="1m")
        assert gaps == []

    def test_different_intervals(self):
        """Gap detection works with different intervals."""
        # 5m interval = 300_000 ms
        candles = [
            {"timestamp": 1704067200000000},  # 00:00
            {"timestamp": 1704067500000000},  # 00:05
            {"timestamp": 1704068400000000},  # 00:20 (gap of 15 minutes)
        ]
        gaps = detect_gaps(candles, interval="5m")
        assert len(gaps) == 1

    def test_string_timestamps(self):
        """Handle ISO format string timestamps from QuestDB."""
        candles = [
            {"timestamp": "2024-01-01T00:00:00Z"},
            {"timestamp": "2024-01-01T00:01:00Z"},
            {"timestamp": "2024-01-01T00:05:00Z"},  # 4 min gap
        ]
        gaps = detect_gaps(candles, interval="1m")
        assert len(gaps) == 1

    def test_none_timestamps_skipped(self):
        """Candles with None timestamps are skipped."""
        candles = [
            {"timestamp": 1704067200000000},
            {"timestamp": None},
            {"timestamp": 1704067320000000},
        ]
        gaps = detect_gaps(candles, interval="1m")
        # Should not crash and should detect gap
        assert isinstance(gaps, list)


class TestInferExchangeFromSymbol:
    """Tests for infer_exchange_from_symbol function."""

    def test_binance_spot(self):
        """Binance spot symbol detection."""
        exchange, market = infer_exchange_from_symbol("BTCUSDT")
        assert exchange == "binance"
        assert market == "spot"

    def test_binance_spot_lowercase(self):
        """Symbol case is normalized."""
        exchange, market = infer_exchange_from_symbol("btcusdt")
        assert exchange == "binance"
        assert market == "spot"

    def test_fyers_equity(self):
        """Fyers equity symbol detection."""
        exchange, market = infer_exchange_from_symbol("NSE:RELIANCE-EQ")
        assert exchange == "fyers"
        assert market == "equity"

    def test_fyers_index(self):
        """Fyers index symbol detection."""
        exchange, market = infer_exchange_from_symbol("NSE:NIFTY50-INDEX")
        assert exchange == "fyers"
        assert market == "index"

    def test_fyers_futures(self):
        """Fyers futures symbol detection."""
        exchange, market = infer_exchange_from_symbol("NSE:NIFTY25JANFUT")
        assert exchange == "fyers"
        assert market == "futures"

    def test_fyers_options_ce(self):
        """Fyers call option detection."""
        exchange, market = infer_exchange_from_symbol("NSE:NIFTY25JAN24000CE")
        assert exchange == "fyers"
        assert market == "options"

    def test_fyers_options_pe(self):
        """Fyers put option detection."""
        exchange, market = infer_exchange_from_symbol("NSE:NIFTY25JAN23000PE")
        assert exchange == "fyers"
        assert market == "options"

    def test_fyers_commodity(self):
        """Fyers commodity symbol detection."""
        exchange, market = infer_exchange_from_symbol("MCX:GOLDM")
        assert exchange == "fyers"
        assert market == "commodity"

    def test_fyers_commodity_options(self):
        """Fyers commodity option detection."""
        exchange, market = infer_exchange_from_symbol("MCX:GOLD25FEB75000CE")
        assert exchange == "fyers"
        assert market == "options"

    def test_bse_equity(self):
        """BSE equity symbol detection."""
        exchange, market = infer_exchange_from_symbol("BSE:RELIANCE-EQ")
        assert exchange == "fyers"
        assert market == "equity"


class TestFetchMissingCandles:
    """Tests for fetch_missing_candles function."""

    @pytest.mark.asyncio
    async def test_binance_candles_success(self):
        """Fetch candles from Binance REST API."""
        mock_client = AsyncMock()
        # Return data once, then empty to stop pagination
        mock_client.get_klines.side_effect = [
            [
                [1704067200000, "50000", "50100", "49900", "50050", "100", 1704067259999, "5000000", 1234, "50", "2500000", "0"],
                [1704067260000, "50050", "50150", "50000", "50100", "110", 1704067319999, "5500000", 1300, "55", "2750000", "0"],
            ],
            [],  # Stop pagination
        ]

        candles = await fetch_missing_candles(
            symbol="BTCUSDT",
            start_ms=1704067200000,
            end_ms=1704067320000,
            exchange="binance",
            market="spot",
            binance_client=mock_client,
        )

        assert len(candles) == 2
        assert all(isinstance(c, OHLCV) for c in candles)
        assert candles[0].symbol == "BTCUSDT"
        assert candles[0].open == 50000.0
        assert candles[0].is_closed is True

    @pytest.mark.asyncio
    async def test_binance_candles_pagination(self):
        """Binance pagination for large requests."""
        mock_client = AsyncMock()
        # First call returns 1000 candles, second returns 500
        batch1 = [[1704067200000 + i * 60000, "50000", "50100", "49900", "50050", "100", 0, "5000000", 100, "50", "2500000", "0"] for i in range(1000)]
        batch2 = [[1704127200000 + i * 60000, "50000", "50100", "49900", "50050", "100", 0, "5000000", 100, "50", "2500000", "0"] for i in range(500)]

        mock_client.get_klines.side_effect = [batch1, batch2, []]

        candles = await fetch_missing_candles(
            symbol="BTCUSDT",
            start_ms=1704067200000,
            end_ms=1704157200000,
            exchange="binance",
            market="spot",
            binance_client=mock_client,
        )

        assert len(candles) == 1500
        assert mock_client.get_klines.call_count == 3

    @pytest.mark.asyncio
    async def test_fyers_candles_success(self):
        """Fetch candles from Fyers REST API."""
        mock_client = AsyncMock()
        mock_candles = [
            OHLCV(timestamp=1704067200000, exchange="fyers", market="equity", symbol="NSE:RELIANCE-EQ", open=2500.0, high=2510.0, low=2490.0, close=2505.0, volume=10000, is_closed=True),
            OHLCV(timestamp=1704067260000, exchange="fyers", market="equity", symbol="NSE:RELIANCE-EQ", open=2505.0, high=2515.0, low=2500.0, close=2510.0, volume=11000, is_closed=True),
        ]
        # Return candles once, then empty to stop pagination
        mock_client.get_klines.side_effect = [mock_candles, []]

        candles = await fetch_missing_candles(
            symbol="NSE:RELIANCE-EQ",
            start_ms=1704067200000,
            end_ms=1704067320000,
            exchange="fyers",
            market="equity",
            fyers_client=mock_client,
        )

        assert len(candles) == 2
        assert candles[0].symbol == "NSE:RELIANCE-EQ"

    @pytest.mark.asyncio
    async def test_unknown_exchange_returns_empty(self):
        """Unknown exchange returns empty list."""
        candles = await fetch_missing_candles(
            symbol="UNKNOWN",
            start_ms=1704067200000,
            end_ms=1704067320000,
            exchange="unknown_exchange",
            market="spot",
        )
        assert candles == []

    @pytest.mark.asyncio
    async def test_binance_client_not_provided(self):
        """Missing Binance client returns empty list."""
        candles = await fetch_missing_candles(
            symbol="BTCUSDT",
            start_ms=1704067200000,
            end_ms=1704067320000,
            exchange="binance",
            market="spot",
            binance_client=None,
        )
        assert candles == []

    @pytest.mark.asyncio
    async def test_max_candles_limit(self):
        """Backfill respects max_candles limit."""
        mock_client = AsyncMock()
        # Return 1000 candles each time
        batch = [[1704067200000 + i * 60000, "50000", "50100", "49900", "50050", "100", 0, "5000000", 100, "50", "2500000", "0"] for i in range(1000)]
        mock_client.get_klines.return_value = batch

        candles = await fetch_missing_candles(
            symbol="BTCUSDT",
            start_ms=1704067200000,
            end_ms=1704200000000,  # Very large range
            exchange="binance",
            market="spot",
            max_candles=500,
            binance_client=mock_client,
        )

        # Should stop at max_candles
        assert len(candles) <= 1000  # One batch


class TestBackfillGaps:
    """Tests for backfill_gaps function."""

    @pytest.mark.asyncio
    async def test_no_gaps_returns_zero(self):
        """No gaps detected returns 0 filled."""
        mock_questdb = MagicMock()
        candles = [
            {"timestamp": 1704067200000000},
            {"timestamp": 1704067260000000},
        ]

        filled = await backfill_gaps(
            questdb=mock_questdb,
            symbol="BTCUSDT",
            candles=candles,
            exchange="binance",
            market="spot",
        )

        assert filled == 0
        mock_questdb.write_candles_batch.assert_not_called()

    @pytest.mark.asyncio
    async def test_gaps_detected_and_filled(self):
        """Gaps are detected and filled."""
        mock_questdb = MagicMock()
        mock_questdb.write_candles_batch.return_value = 3

        mock_binance = AsyncMock()
        mock_binance.get_klines.return_value = [
            [1704067320000, "50000", "50100", "49900", "50050", "100", 0, "5000000", 100, "50", "2500000", "0"],
            [1704067380000, "50050", "50150", "50000", "50100", "110", 0, "5500000", 100, "55", "2750000", "0"],
            [1704067440000, "50100", "50200", "50050", "50150", "120", 0, "6000000", 100, "60", "3000000", "0"],
        ]

        candles = [
            {"timestamp": 1704067200000000},  # 00:00
            {"timestamp": 1704067260000000},  # 00:01
            {"timestamp": 1704067500000000},  # 00:05 (gap)
        ]

        filled = await backfill_gaps(
            questdb=mock_questdb,
            symbol="BTCUSDT",
            candles=candles,
            exchange="binance",
            market="spot",
            binance_client=mock_binance,
        )

        assert filled == 3
        mock_questdb.write_candles_batch.assert_called_once()


class TestBackfillTimeRange:
    """Tests for backfill_time_range function."""

    @pytest.mark.asyncio
    async def test_backfill_time_range_success(self):
        """Backfill time range fetches and writes candles."""
        mock_questdb = MagicMock()
        mock_questdb.write_candles_batch.return_value = 5

        mock_binance = AsyncMock()
        # Return 5 candles, then empty to stop pagination
        mock_binance.get_klines.side_effect = [
            [
                [1704067200000 + i * 60000, "50000", "50100", "49900", "50050", "100", 0, "5000000", 100, "50", "2500000", "0"]
                for i in range(5)
            ],
            [],  # Stop pagination
        ]

        written, candles = await backfill_time_range(
            questdb=mock_questdb,
            symbol="BTCUSDT",
            start_ms=1704067200000,
            end_ms=1704067500000,
            exchange="binance",
            market="spot",
            binance_client=mock_binance,
        )

        assert written == 5
        assert len(candles) == 5
        mock_questdb.write_candles_batch.assert_called_once()

    @pytest.mark.asyncio
    async def test_backfill_time_range_no_data(self):
        """Backfill with no data returns 0 and empty list."""
        mock_questdb = MagicMock()
        mock_binance = AsyncMock()
        mock_binance.get_klines.return_value = []

        written, candles = await backfill_time_range(
            questdb=mock_questdb,
            symbol="BTCUSDT",
            start_ms=1704067200000,
            end_ms=1704067500000,
            exchange="binance",
            market="spot",
            binance_client=mock_binance,
        )

        assert written == 0
        assert candles == []


class TestIntervalConstants:
    """Tests for INTERVAL_MS constants."""

    def test_all_intervals_present(self):
        """All expected intervals are defined."""
        expected = ["1m", "5m", "15m", "30m", "1h", "4h", "1d"]
        for interval in expected:
            assert interval in INTERVAL_MS

    def test_interval_values_correct(self):
        """Interval values are correct in milliseconds."""
        assert INTERVAL_MS["1m"] == 60_000
        assert INTERVAL_MS["5m"] == 300_000
        assert INTERVAL_MS["15m"] == 900_000
        assert INTERVAL_MS["1h"] == 3_600_000
        assert INTERVAL_MS["1d"] == 86_400_000
