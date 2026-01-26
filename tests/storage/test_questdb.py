"""Tests for QuestDB client."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from hft.core.types import OHLCV
from hft.storage.questdb import QuestDBClient


class TestQuestDBClientInit:
    """Tests for QuestDBClient initialization."""

    def test_default_ports(self):
        """Default ports are correct."""
        client = QuestDBClient()
        assert client.host == "localhost"
        assert client.ilp_port == 9009
        assert client.http_port == 9000

    def test_custom_host_ports(self):
        """Can set custom host and ports."""
        client = QuestDBClient(host="questdb.local", ilp_port=19009, http_port=19000)
        assert client.host == "questdb.local"
        assert client.ilp_port == 19009
        assert client.http_port == 19000


class TestInitSchema:
    """Tests for init_schema method."""

    @pytest.mark.asyncio
    async def test_creates_table(self):
        """Creates candles_1m table."""
        client = QuestDBClient()

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = {}
            await client.init_schema()

            mock_exec.assert_called_once()
            call_sql = mock_exec.call_args[0][0]
            assert "CREATE TABLE IF NOT EXISTS candles_1m" in call_sql
            assert "PARTITION BY DAY" in call_sql
            assert "DEDUP UPSERT KEYS" in call_sql

    @pytest.mark.asyncio
    async def test_handles_existing_table(self):
        """Handles case where table already exists."""
        client = QuestDBClient()

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.side_effect = Exception("Table already exists")
            # Should not raise
            await client.init_schema()


class TestWriteCandle:
    """Tests for write_candle method."""

    def test_write_success(self):
        """Write candle successfully."""
        client = QuestDBClient()
        candle = OHLCV(
            timestamp=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
            is_closed=True,
        )

        mock_sender = MagicMock()
        with patch.object(client, "_get_sender", return_value=mock_sender):
            client.write_candle(candle)

            mock_sender.row.assert_called_once()
            call_args = mock_sender.row.call_args
            assert call_args[0][0] == "candles_1m"
            assert call_args[1]["symbols"]["symbol"] == "BTCUSDT"
            assert call_args[1]["symbols"]["exchange"] == "binance"
            assert call_args[1]["columns"]["open"] == 50000.0
            mock_sender.flush.assert_called_once()

    def test_write_error_closes_sender(self):
        """Write error closes sender for reconnection."""
        client = QuestDBClient()
        candle = OHLCV(
            timestamp=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )

        mock_sender = MagicMock()
        mock_sender.row.side_effect = Exception("Connection lost")

        with patch.object(client, "_get_sender", return_value=mock_sender):
            with patch.object(client, "_close_sender") as mock_close:
                client.write_candle(candle)
                mock_close.assert_called_once()


class TestWriteCandlesBatch:
    """Tests for write_candles_batch method."""

    def test_empty_list_returns_zero(self):
        """Empty candle list returns 0."""
        client = QuestDBClient()
        count = client.write_candles_batch([])
        assert count == 0

    def test_write_multiple(self):
        """Write multiple candles."""
        client = QuestDBClient()
        candles = [
            OHLCV(timestamp=1704067200000, exchange="binance", market="spot", symbol="BTCUSDT", open=50000.0, high=50100.0, low=49900.0, close=50050.0, volume=100.0),
            OHLCV(timestamp=1704067260000, exchange="binance", market="spot", symbol="BTCUSDT", open=50050.0, high=50150.0, low=50000.0, close=50100.0, volume=110.0),
        ]

        mock_sender = MagicMock()
        with patch.object(client, "_get_sender", return_value=mock_sender):
            count = client.write_candles_batch(candles)

            assert count == 2
            assert mock_sender.row.call_count == 2
            mock_sender.flush.assert_called_once()

    def test_write_error_returns_zero(self):
        """Write error returns 0."""
        client = QuestDBClient()
        candles = [
            OHLCV(timestamp=1704067200000, exchange="binance", market="spot", symbol="BTCUSDT", open=50000.0, high=50100.0, low=49900.0, close=50050.0, volume=100.0),
        ]

        mock_sender = MagicMock()
        mock_sender.row.side_effect = Exception("Write failed")

        with patch.object(client, "_get_sender", return_value=mock_sender):
            with patch.object(client, "_close_sender"):
                count = client.write_candles_batch(candles)
                assert count == 0


class TestQueryCandles:
    """Tests for query_candles method."""

    @pytest.mark.asyncio
    async def test_query_1m_no_aggregation(self):
        """1m interval queries without aggregation."""
        client = QuestDBClient()

        mock_result = {
            "columns": [
                {"name": "timestamp"},
                {"name": "exchange"},
                {"name": "market"},
                {"name": "symbol"},
                {"name": "open"},
                {"name": "high"},
                {"name": "low"},
                {"name": "close"},
                {"name": "volume"},
                {"name": "quote_volume"},
                {"name": "trade_count"},
                {"name": "vwap"},
            ],
            "dataset": [
                [1704067260000000, "binance", "spot", "BTCUSDT", 50050.0, 50150.0, 50000.0, 50100.0, 110.0, 5500000.0, 500, 50075.0],
                [1704067200000000, "binance", "spot", "BTCUSDT", 50000.0, 50100.0, 49900.0, 50050.0, 100.0, 5000000.0, 450, 50025.0],
            ],
        }

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = mock_result
            candles = await client.query_candles("BTCUSDT", interval="1m", limit=10)

            # Results are reversed to chronological order
            assert len(candles) == 2
            assert candles[0]["timestamp"] == 1704067200000000
            assert candles[1]["timestamp"] == 1704067260000000

    @pytest.mark.asyncio
    async def test_query_higher_interval_uses_aggregation(self):
        """Higher intervals use GROUP BY aggregation."""
        client = QuestDBClient()

        mock_result = {
            "columns": [{"name": "period_ts"}, {"name": "exchange"}, {"name": "market"}, {"name": "symbol"}, {"name": "open"}, {"name": "high"}, {"name": "low"}, {"name": "close"}, {"name": "volume"}, {"name": "quote_volume"}, {"name": "trade_count"}, {"name": "vwap"}],
            "dataset": [[1704067200000000, "binance", "spot", "BTCUSDT", 50000.0, 50200.0, 49800.0, 50150.0, 500.0, 25000000.0, 2000, 50050.0]],
        }

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = mock_result
            candles = await client.query_candles("BTCUSDT", interval="5m", limit=10)

            # Check aggregation SQL was used
            call_sql = mock_exec.call_args[0][0]
            assert "timestamp_floor" in call_sql
            assert "GROUP BY" in call_sql
            assert "first(open)" in call_sql
            assert "max(high)" in call_sql

            # period_ts should be renamed to timestamp
            assert candles[0]["timestamp"] == 1704067200000000
            assert "period_ts" not in candles[0]

    @pytest.mark.asyncio
    async def test_query_empty_result(self):
        """Empty result returns empty list."""
        client = QuestDBClient()

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = {"columns": [], "dataset": []}
            candles = await client.query_candles("BTCUSDT")
            assert candles == []

    @pytest.mark.asyncio
    async def test_query_with_time_range(self):
        """Time range parameters are included."""
        client = QuestDBClient()

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = {"columns": [], "dataset": []}
            await client.query_candles(
                "BTCUSDT",
                start_time=1704067200,
                end_time=1704070800,
            )

            call_sql = mock_exec.call_args[0][0]
            # Timestamps converted to microseconds
            assert "1704067200000000" in call_sql
            assert "1704070800000000" in call_sql


class TestQueryDistinctSymbols:
    """Tests for query_distinct_symbols method."""

    @pytest.mark.asyncio
    async def test_returns_symbols(self):
        """Returns list of symbols with metadata."""
        client = QuestDBClient()

        mock_result = {
            "columns": [{"name": "symbol"}, {"name": "exchange"}, {"name": "market"}, {"name": "latest_ts"}],
            "dataset": [
                ["BTCUSDT", "binance", "spot", 1704067200000000],
                ["ETHUSDT", "binance", "spot", 1704067140000000],
            ],
        }

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = mock_result
            symbols = await client.query_distinct_symbols(since_days=7)

            assert len(symbols) == 2
            assert symbols[0]["symbol"] == "BTCUSDT"
            assert symbols[0]["exchange"] == "binance"
            # Microseconds converted to milliseconds
            assert symbols[0]["latest_ts"] == 1704067200000

    @pytest.mark.asyncio
    async def test_handles_null_market(self):
        """Handles NULL market values."""
        client = QuestDBClient()

        mock_result = {
            "columns": [{"name": "symbol"}, {"name": "exchange"}, {"name": "market"}, {"name": "latest_ts"}],
            "dataset": [["BTCUSDT", "binance", None, 1704067200000000]],
        }

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = mock_result
            symbols = await client.query_distinct_symbols()

            assert symbols[0]["market"] == "spot"  # Default


class TestGetLatestTimestamp:
    """Tests for get_latest_timestamp method."""

    @pytest.mark.asyncio
    async def test_returns_timestamp_ms(self):
        """Returns timestamp in milliseconds."""
        client = QuestDBClient()

        mock_result = {
            "columns": [{"name": "latest"}],
            "dataset": [[1704067200000000]],  # microseconds
        }

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = mock_result
            ts = await client.get_latest_timestamp("BTCUSDT")

            # Converted to milliseconds
            assert ts == 1704067200000

    @pytest.mark.asyncio
    async def test_returns_none_if_no_data(self):
        """Returns None if no data exists."""
        client = QuestDBClient()

        mock_result = {"columns": [{"name": "latest"}], "dataset": [[None]]}

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.return_value = mock_result
            ts = await client.get_latest_timestamp("BTCUSDT")
            assert ts is None

    @pytest.mark.asyncio
    async def test_returns_none_on_error(self):
        """Returns None on query error."""
        client = QuestDBClient()

        with patch.object(client, "_execute_sql", new_callable=AsyncMock) as mock_exec:
            mock_exec.side_effect = Exception("Query failed")
            ts = await client.get_latest_timestamp("BTCUSDT")
            assert ts is None


class TestLifecycle:
    """Tests for client lifecycle."""

    @pytest.mark.asyncio
    async def test_close_closes_connections(self):
        """Close closes both sender and HTTP client."""
        client = QuestDBClient()

        with patch.object(client, "_close_sender") as mock_close_sender:
            with patch.object(client._http, "aclose", new_callable=AsyncMock) as mock_close_http:
                await client.close()

                mock_close_sender.assert_called_once()
                mock_close_http.assert_called_once()

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Works as async context manager."""
        with patch.object(QuestDBClient, "close", new_callable=AsyncMock) as mock_close:
            async with QuestDBClient() as client:
                assert client is not None
            mock_close.assert_called_once()


class TestSenderManagement:
    """Tests for ILP sender management."""

    def test_get_sender_creates_new(self):
        """First call creates new sender."""
        client = QuestDBClient()

        with patch("hft.storage.questdb.Sender") as MockSender:
            mock_sender = MagicMock()
            MockSender.return_value = mock_sender

            sender = client._get_sender()

            assert sender is mock_sender
            MockSender.assert_called_once()
            mock_sender.establish.assert_called_once()

    def test_get_sender_reuses_existing(self):
        """Subsequent calls reuse existing sender."""
        client = QuestDBClient()

        with patch("hft.storage.questdb.Sender") as MockSender:
            mock_sender = MagicMock()
            MockSender.return_value = mock_sender

            sender1 = client._get_sender()
            sender2 = client._get_sender()

            assert sender1 is sender2
            MockSender.assert_called_once()

    def test_close_sender_clears_reference(self):
        """Close sender clears the reference."""
        client = QuestDBClient()
        client._sender = MagicMock()

        client._close_sender()

        assert client._sender is None
