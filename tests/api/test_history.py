"""Tests for history REST endpoints."""

import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from nanoedge.api.history import (
    _aggregate_candles,
    _calculate_stats_from_formatted,
    calculate_stats_from_candles,
    router,
)
from nanoedge.core.types import OHLCV, MarketStats


@pytest.fixture
def app():
    """Create FastAPI app with history router."""
    app = FastAPI()
    app.include_router(router)
    return app


@pytest.fixture
def mock_app_state():
    """Create mock app state."""
    state = MagicMock()
    state.questdb = MagicMock()
    state.rest_client = MagicMock()
    state.binance_rest_client = MagicMock()
    state.fyers_rest_client = None
    state.aggregators = {"BTCUSDT": MagicMock()}
    state.orderbooks = {}
    state.tick_buffer = MagicMock()
    state.tick_buffer.__len__ = MagicMock(return_value=1000)
    state.feed_handler = MagicMock()
    state.feed_handler.is_connected = True
    state.latest_stats = {}
    return state


class TestCalculateStatsFromCandles:
    """Tests for calculate_stats_from_candles function."""

    def test_empty_candles_returns_none(self):
        """Empty candle list returns None."""
        result = calculate_stats_from_candles([], "BTCUSDT", "binance", "spot")
        assert result is None

    def test_single_candle(self):
        """Single candle calculates stats correctly."""
        now_ms = int(time.time() * 1000)
        candle = OHLCV(
            timestamp=now_ms,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
            quote_volume=5000000.0,
            trade_count=500,
        )

        result = calculate_stats_from_candles([candle], "BTCUSDT", "binance", "spot")

        assert result is not None
        assert result.symbol == "BTCUSDT"
        assert result.open_price == 50000.0
        assert result.last_price == 50050.0
        assert result.high_24h == 50100.0
        assert result.low_24h == 49900.0
        assert result.volume_24h == 100.0

    def test_multiple_candles(self):
        """Multiple candles aggregate correctly."""
        now_ms = int(time.time() * 1000)
        candles = [
            OHLCV(
                timestamp=now_ms - 60000,  # 1 min ago
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=50000.0,
                high=50100.0,
                low=49900.0,
                close=50050.0,
                volume=100.0,
                quote_volume=5000000.0,
                trade_count=500,
            ),
            OHLCV(
                timestamp=now_ms,  # now
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=50050.0,
                high=50200.0,  # New high
                low=49800.0,  # New low
                close=50150.0,
                volume=150.0,
                quote_volume=7500000.0,
                trade_count=600,
            ),
        ]

        result = calculate_stats_from_candles(candles, "BTCUSDT", "binance", "spot")

        assert result is not None
        assert result.open_price == 50000.0  # First candle open
        assert result.last_price == 50150.0  # Last candle close
        assert result.high_24h == 50200.0  # Max high
        assert result.low_24h == 49800.0  # Min low
        assert result.volume_24h == 250.0  # Sum of volumes

    def test_price_change_calculation(self):
        """Price change is calculated correctly."""
        now_ms = int(time.time() * 1000)
        candles = [
            OHLCV(
                timestamp=now_ms - 60000,
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=50000.0,
                high=50100.0,
                low=49900.0,
                close=50050.0,
                volume=100.0,
            ),
            OHLCV(
                timestamp=now_ms,
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=50050.0,
                high=50200.0,
                low=49800.0,
                close=50500.0,  # +500 from open
                volume=150.0,
            ),
        ]

        result = calculate_stats_from_candles(candles, "BTCUSDT", "binance", "spot")

        assert result is not None
        assert result.price_change == 500.0  # 50500 - 50000
        assert result.price_change_percent == 1.0  # 500/50000 * 100

    def test_filters_to_24h_window(self):
        """Only candles within 24h are included."""
        now_ms = int(time.time() * 1000)
        ms_25h = 25 * 60 * 60 * 1000

        candles = [
            OHLCV(
                timestamp=now_ms - ms_25h,  # 25 hours ago - should be excluded
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=45000.0,  # Very different price
                high=45100.0,
                low=44900.0,
                close=45050.0,
                volume=500.0,
            ),
            OHLCV(
                timestamp=now_ms,
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=50000.0,
                high=50100.0,
                low=49900.0,
                close=50050.0,
                volume=100.0,
            ),
        ]

        result = calculate_stats_from_candles(candles, "BTCUSDT", "binance", "spot")

        # Only the recent candle should be used
        assert result is not None
        assert result.open_price == 50000.0
        assert result.volume_24h == 100.0  # Not 600


class TestCalculateStatsFromFormatted:
    """Tests for _calculate_stats_from_formatted function."""

    def test_empty_returns_none(self):
        """Empty list returns None."""
        result = _calculate_stats_from_formatted([], "BTCUSDT", "binance", "spot")
        assert result is None

    def test_formats_correctly(self):
        """Formatted candle dicts work correctly."""
        now_sec = int(time.time())
        candles = [
            {
                "time": now_sec - 60,
                "open": 50000.0,
                "high": 50100.0,
                "low": 49900.0,
                "close": 50050.0,
                "volume": 100.0,
            },
            {
                "time": now_sec,
                "open": 50050.0,
                "high": 50200.0,
                "low": 49800.0,
                "close": 50150.0,
                "volume": 150.0,
            },
        ]

        result = _calculate_stats_from_formatted(candles, "BTCUSDT", "binance", "spot")

        assert result is not None
        assert result.open_price == 50000.0
        assert result.last_price == 50150.0
        assert result.high_24h == 50200.0
        assert result.low_24h == 49800.0
        assert result.volume_24h == 250.0

    def test_handles_missing_low(self):
        """Handles missing low price gracefully."""
        now_sec = int(time.time())
        candles = [
            {
                "time": now_sec,
                "open": 50000.0,
                "high": 50100.0,
                # No low field
                "close": 50050.0,
                "volume": 100.0,
            },
        ]

        result = _calculate_stats_from_formatted(candles, "BTCUSDT", "binance", "spot")

        assert result is not None
        assert result.low_24h == 0  # Default when low is inf


class TestAggregateCandles:
    """Tests for _aggregate_candles function."""

    def test_empty_returns_empty(self):
        """Empty candle list returns empty list."""
        result = _aggregate_candles([], "5m", 10)
        assert result == []

    def test_1m_passthrough(self):
        """1m candles pass through with formatting."""
        candles = [
            OHLCV(
                timestamp=1704067200000,
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                open=50000.0,
                high=50100.0,
                low=49900.0,
                close=50050.0,
                volume=100.0,
            ),
        ]

        # With 1m interval, each candle is its own bucket
        result = _aggregate_candles(candles, "1m", 10)

        assert len(result) == 1
        assert result[0]["time"] == 1704067200  # ms to seconds
        assert result[0]["open"] == 50000.0
        assert result[0]["close"] == 50050.0

    def test_5m_aggregation(self):
        """5 x 1m candles aggregate to 1 x 5m candle."""
        base_ts = 1704067200000  # Start of 5m bucket
        candles = []
        for i in range(5):
            candles.append(
                OHLCV(
                    timestamp=base_ts + (i * 60000),  # Each minute
                    exchange="binance",
                    market="spot",
                    symbol="BTCUSDT",
                    open=50000.0 + i * 10,
                    high=50050.0 + i * 10,
                    low=49950.0 + i * 10,
                    close=50010.0 + i * 10,
                    volume=100.0,
                )
            )

        result = _aggregate_candles(candles, "5m", 10)

        assert len(result) == 1
        assert result[0]["time"] == 1704067200  # Bucket start time
        assert result[0]["open"] == 50000.0  # First candle open
        assert result[0]["close"] == 50050.0  # Last candle close (50010 + 4*10)
        assert result[0]["high"] == 50090.0  # Max high
        assert result[0]["low"] == 49950.0  # Min low
        assert result[0]["volume"] == 500.0  # Sum of volumes

    def test_respects_limit(self):
        """Limit parameter restricts output size."""
        base_ts = 1704067200000
        candles = []
        for i in range(20):  # 20 x 1m = 4 x 5m buckets
            candles.append(
                OHLCV(
                    timestamp=base_ts + (i * 60000),
                    exchange="binance",
                    market="spot",
                    symbol="BTCUSDT",
                    open=50000.0,
                    high=50100.0,
                    low=49900.0,
                    close=50050.0,
                    volume=100.0,
                )
            )

        result = _aggregate_candles(candles, "5m", 2)

        # Should return only 2 most recent buckets
        assert len(result) == 2


class TestGetHistoryEndpoint:
    """Tests for GET /history endpoint."""

    def test_invalid_interval_returns_400(self, app, mock_app_state):
        """Invalid interval returns 400 error."""
        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/history?symbol=BTCUSDT&interval=2m")

            assert response.status_code == 400
            assert "Invalid interval" in response.json()["detail"]

    def test_no_db_returns_503(self, app, mock_app_state):
        """No database returns 503 error."""
        mock_app_state.questdb = None

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/history?symbol=BTCUSDT")

            assert response.status_code == 503
            assert "Database not available" in response.json()["detail"]

    def test_valid_request_returns_candles(self, app, mock_app_state):
        """Valid request returns formatted candles."""
        mock_app_state.questdb.query_candles = AsyncMock(
            return_value=[
                {
                    "timestamp": 1704067200000000,  # microseconds
                    "open": 50000.0,
                    "high": 50100.0,
                    "low": 49900.0,
                    "close": 50050.0,
                    "volume": 100.0,
                },
            ]
        )

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/history?symbol=BTCUSDT&interval=1m&limit=10")

            assert response.status_code == 200
            data = response.json()
            assert len(data) == 1
            assert data[0]["time"] == 1704067200  # seconds
            assert data[0]["open"] == 50000.0

    def test_symbol_uppercased(self, app, mock_app_state):
        """Symbol parameter is uppercased."""
        mock_app_state.questdb.query_candles = AsyncMock(return_value=[])

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/history?symbol=btcusdt")

            # Should work even with lowercase
            assert response.status_code == 200

    def test_handles_iso_timestamps(self, app, mock_app_state):
        """Handles ISO format timestamps from QuestDB."""
        mock_app_state.questdb.query_candles = AsyncMock(
            return_value=[
                {
                    "timestamp": "2024-01-01T00:00:00.000000Z",
                    "open": 50000.0,
                    "high": 50100.0,
                    "low": 49900.0,
                    "close": 50050.0,
                    "volume": 100.0,
                },
            ]
        )

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/history?symbol=BTCUSDT")

            assert response.status_code == 200
            data = response.json()
            assert len(data) == 1
            assert data[0]["time"] == 1704067200  # Jan 1, 2024 00:00:00 UTC

    def test_backfill_disabled(self, app, mock_app_state):
        """Backfill can be disabled."""
        mock_app_state.questdb.query_candles = AsyncMock(return_value=[])

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/history?symbol=BTCUSDT&backfill=false")

            assert response.status_code == 200
            assert response.json() == []


class TestBackfillEndpoint:
    """Tests for POST /backfill endpoint."""

    def test_no_db_returns_503(self, app, mock_app_state):
        """No database returns 503 error."""
        mock_app_state.questdb = None

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.post("/backfill?symbol=BTCUSDT&hours=24")

            assert response.status_code == 503

    def test_no_client_returns_503(self, app, mock_app_state):
        """No REST client returns 503 error."""
        mock_app_state.rest_client = None
        mock_app_state.binance_rest_client = None

        with patch("nanoedge.api.history.app_state", mock_app_state):
            with patch("nanoedge.api.history.infer_exchange_from_symbol") as mock_infer:
                mock_infer.return_value = ("binance", "spot")
                client = TestClient(app)
                response = client.post("/backfill?symbol=BTCUSDT&hours=24")

                assert response.status_code == 503

    def test_successful_backfill(self, app, mock_app_state):
        """Successful backfill returns count."""
        mock_app_state.questdb.write_candles_batch = MagicMock(return_value=1440)

        with patch("nanoedge.api.history.app_state", mock_app_state):
            with patch("nanoedge.api.history.fetch_missing_candles", new_callable=AsyncMock) as mock_fetch:
                mock_fetch.return_value = [MagicMock()] * 1440

                client = TestClient(app)
                response = client.post("/backfill?symbol=BTCUSDT&hours=24")

                assert response.status_code == 200
                data = response.json()
                assert data["status"] == "success"
                assert data["symbol"] == "BTCUSDT"
                assert data["hours"] == 24
                assert data["candles_written"] == 1440

    def test_no_data_response(self, app, mock_app_state):
        """No data returns no_data status."""
        with patch("nanoedge.api.history.app_state", mock_app_state):
            with patch("nanoedge.api.history.fetch_missing_candles", new_callable=AsyncMock) as mock_fetch:
                mock_fetch.return_value = []

                client = TestClient(app)
                response = client.post("/backfill?symbol=BTCUSDT&hours=24")

                assert response.status_code == 200
                data = response.json()
                assert data["status"] == "no_data"
                assert data["candles_written"] == 0

    def test_handles_fyers_symbol(self, app, mock_app_state):
        """Handles Fyers symbol format."""
        mock_app_state.fyers_rest_client = MagicMock()
        mock_app_state.questdb.write_candles_batch = MagicMock(return_value=100)

        with patch("nanoedge.api.history.app_state", mock_app_state):
            with patch("nanoedge.api.history.fetch_missing_candles", new_callable=AsyncMock) as mock_fetch:
                mock_fetch.return_value = [MagicMock()] * 100

                client = TestClient(app)
                response = client.post("/backfill?symbol=NSE:RELIANCE-EQ&hours=24")

                assert response.status_code == 200
                data = response.json()
                assert data["exchange"] == "fyers"


class TestGetActiveSymbolsEndpoint:
    """Tests for GET /active-symbols endpoint."""

    def test_returns_symbols(self, app, mock_app_state):
        """Returns list of aggregator symbols."""
        mock_app_state.aggregators = {
            "BTCUSDT": MagicMock(),
            "ETHUSDT": MagicMock(),
        }

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/active-symbols")

            assert response.status_code == 200
            data = response.json()
            assert "symbols" in data
            assert "BTCUSDT" in data["symbols"]
            assert "ETHUSDT" in data["symbols"]


class TestGetStatusEndpoint:
    """Tests for GET /status endpoint."""

    def test_returns_status(self, app, mock_app_state):
        """Returns system status."""
        mock_orderbook = MagicMock()
        mock_orderbook.is_initialized = True
        mock_orderbook.best_bid = 50000.0
        mock_orderbook.best_ask = 50001.0
        mock_orderbook.spread = 1.0

        mock_app_state.orderbooks = {"BTCUSDT": mock_orderbook}

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/status")

            assert response.status_code == 200
            data = response.json()
            assert "symbols" in data
            assert "feed_connected" in data
            assert data["feed_connected"] is True
            assert "orderbooks" in data
            assert "tick_buffer_size" in data
            assert data["tick_buffer_size"] == 1000

    def test_orderbook_status_included(self, app, mock_app_state):
        """Orderbook status is included."""
        mock_orderbook = MagicMock()
        mock_orderbook.is_initialized = True
        mock_orderbook.best_bid = 50000.0
        mock_orderbook.best_ask = 50001.0
        mock_orderbook.spread = 1.0

        mock_app_state.orderbooks = {"BTCUSDT": mock_orderbook}

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)
            response = client.get("/status")

            data = response.json()
            assert "BTCUSDT" in data["orderbooks"]
            ob_status = data["orderbooks"]["BTCUSDT"]
            assert ob_status["initialized"] is True
            assert ob_status["best_bid"] == 50000.0
            assert ob_status["best_ask"] == 50001.0
            assert ob_status["spread"] == 1.0


class TestValidIntervals:
    """Tests for interval validation."""

    def test_all_valid_intervals_accepted(self, app, mock_app_state):
        """All valid intervals are accepted."""
        mock_app_state.questdb.query_candles = AsyncMock(return_value=[])

        valid_intervals = ["1m", "5m", "15m", "30m", "1h", "4h", "1d"]

        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)

            for interval in valid_intervals:
                response = client.get(f"/history?symbol=BTCUSDT&interval={interval}")
                assert response.status_code == 200, f"Interval {interval} should be valid"

    def test_invalid_intervals_rejected(self, app, mock_app_state):
        """Invalid intervals are rejected."""
        with patch("nanoedge.api.history.app_state", mock_app_state):
            client = TestClient(app)

            invalid_intervals = ["2m", "3m", "10m", "2h", "6h", "1w", "1M"]

            for interval in invalid_intervals:
                response = client.get(f"/history?symbol=BTCUSDT&interval={interval}")
                assert response.status_code == 400, f"Interval {interval} should be invalid"


class TestGetMetricsEndpoint:
    """Tests for GET /metrics endpoint."""

    def test_returns_metrics(self, app):
        """Returns latency metrics."""
        client = TestClient(app)
        response = client.get("/metrics")

        assert response.status_code == 200
        data = response.json()

        # Check all expected metric categories are present
        expected_metrics = [
            "parse_json",
            "api_ws_push",
            "orderbook_update",
            "ws_network",
            "db_write",
            "normalize",
            "agg_update",
        ]
        for metric in expected_metrics:
            assert metric in data, f"Missing metric: {metric}"

    def test_metrics_have_required_fields(self, app):
        """Each metric has required fields."""
        client = TestClient(app)
        response = client.get("/metrics")

        data = response.json()
        required_fields = [
            "count",
            "current_samples",
            "p50_us",
            "p95_us",
            "p99_us",
            "mean_us",
            "min_us",
            "max_us",
        ]

        for metric_name, metric_data in data.items():
            for field in required_fields:
                assert field in metric_data, f"Missing field {field} in {metric_name}"

    def test_metrics_values_are_numeric(self, app):
        """Metric values are numeric."""
        client = TestClient(app)
        response = client.get("/metrics")

        data = response.json()

        for metric_name, metric_data in data.items():
            assert isinstance(metric_data["count"], int)
            assert isinstance(metric_data["current_samples"], int)
            assert isinstance(metric_data["p50_us"], (int, float))
            assert isinstance(metric_data["p99_us"], (int, float))
