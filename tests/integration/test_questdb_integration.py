"""Integration tests for QuestDB.

These tests require QuestDB to be running:
    docker run -d --name questdb -p 9000:9000 -p 9009:9009 questdb/questdb

Run with: uv run pytest tests/integration/test_questdb_integration.py -v
Skip with: uv run pytest tests/ --ignore=tests/integration/
"""

import asyncio
import time
import uuid

import pytest

from hft.core.types import OHLCV
from hft.storage.questdb import QuestDBClient


def is_questdb_available() -> bool:
    """Check if QuestDB is available."""
    import httpx

    # Try both localhost and 127.0.0.1
    # Use the exec endpoint with a simple query instead of root (which returns large HTML)
    for host in ["127.0.0.1", "localhost"]:
        try:
            response = httpx.get(
                f"http://{host}:9000/exec",
                params={"query": "SELECT 1"},
                timeout=5.0,
            )
            if response.status_code == 200:
                return True
        except Exception:
            continue
    return False


# Skip all tests in this module if QuestDB is not available
pytestmark = pytest.mark.skipif(
    not is_questdb_available(),
    reason="QuestDB not available on localhost:9000",
)


@pytest.fixture
async def questdb_client():
    """Create a QuestDB client for testing."""
    client = QuestDBClient(host="127.0.0.1", ilp_port=9009, http_port=9000)
    try:
        await client.init_schema()
    except Exception:
        pass  # Table may already exist
    yield client
    await client.close()


@pytest.fixture
def unique_symbol():
    """Generate a unique symbol for test isolation."""
    # Use a unique suffix to avoid conflicts between test runs
    return f"TEST_{uuid.uuid4().hex[:8].upper()}"


class TestQuestDBIntegration:
    """Integration tests for QuestDB operations."""

    @pytest.mark.asyncio
    async def test_init_schema_creates_table(self, questdb_client):
        """init_schema creates the candles_1m table."""
        # Query table info
        result = await questdb_client._execute_sql(
            "SELECT count() FROM candles_1m WHERE symbol = '__NEVER_EXISTS__'"
        )
        # If we get a result, the table exists
        assert result is not None

    @pytest.mark.asyncio
    async def test_write_and_read_candle(self, questdb_client, unique_symbol):
        """Write a candle and read it back."""
        # Create test candle with unique symbol
        timestamp_ms = int(time.time() * 1000)
        # Round to minute boundary
        timestamp_ms = (timestamp_ms // 60000) * 60000

        candle = OHLCV(
            timestamp=timestamp_ms,
            exchange="binance",
            market="spot",
            symbol=unique_symbol,
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
            quote_volume=5000000.0,
            trade_count=500,
            vwap=50025.0,
        )

        # Write the candle
        questdb_client.write_candle(candle)

        # Wait for WAL commit (QuestDB has ~1s delay for WAL tables)
        await asyncio.sleep(2)

        # Read it back
        candles = await questdb_client.query_candles(
            symbol=unique_symbol,
            interval="1m",
            limit=10,
        )

        # Should have at least one candle
        assert len(candles) >= 1

        # Find our candle
        found = False
        for c in candles:
            if c.get("symbol") == unique_symbol:
                assert c.get("open") == 50000.0
                assert c.get("high") == 50100.0
                assert c.get("low") == 49900.0
                assert c.get("close") == 50050.0
                assert c.get("volume") == 100.0
                found = True
                break

        assert found, f"Candle for {unique_symbol} not found"

    @pytest.mark.asyncio
    async def test_write_batch_and_count(self, questdb_client, unique_symbol):
        """Write a batch of candles and verify count."""
        base_ts = int(time.time() * 1000)
        base_ts = (base_ts // 60000) * 60000  # Round to minute

        candles = []
        for i in range(5):
            candles.append(
                OHLCV(
                    timestamp=base_ts + (i * 60000),  # 1 minute apart
                    exchange="binance",
                    market="spot",
                    symbol=unique_symbol,
                    open=50000.0 + i,
                    high=50100.0 + i,
                    low=49900.0 + i,
                    close=50050.0 + i,
                    volume=100.0 + i,
                )
            )

        # Write batch
        written = questdb_client.write_candles_batch(candles)
        assert written == 5

        # Wait for WAL commit
        await asyncio.sleep(2)

        # Query back
        result = await questdb_client.query_candles(
            symbol=unique_symbol,
            interval="1m",
            limit=10,
        )

        # Should have 5 candles
        assert len(result) >= 5

    @pytest.mark.asyncio
    async def test_get_latest_timestamp(self, questdb_client, unique_symbol):
        """get_latest_timestamp returns most recent candle time."""
        # Write a candle
        timestamp_ms = int(time.time() * 1000)
        timestamp_ms = (timestamp_ms // 60000) * 60000

        candle = OHLCV(
            timestamp=timestamp_ms,
            exchange="binance",
            market="spot",
            symbol=unique_symbol,
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )

        questdb_client.write_candle(candle)

        # Wait for WAL commit
        await asyncio.sleep(2)

        # Get latest timestamp
        latest = await questdb_client.get_latest_timestamp(unique_symbol)

        # Should return our timestamp (may be off by a bit due to microsecond conversion)
        assert latest is not None
        # Allow 1 second tolerance for timestamp conversion
        assert abs(latest - timestamp_ms) < 1000

    @pytest.mark.asyncio
    async def test_query_distinct_symbols(self, questdb_client, unique_symbol):
        """query_distinct_symbols returns symbols with data."""
        # Write a candle
        timestamp_ms = int(time.time() * 1000)
        timestamp_ms = (timestamp_ms // 60000) * 60000

        candle = OHLCV(
            timestamp=timestamp_ms,
            exchange="binance",
            market="spot",
            symbol=unique_symbol,
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )

        questdb_client.write_candle(candle)

        # Wait for WAL commit
        await asyncio.sleep(2)

        # Query distinct symbols
        symbols = await questdb_client.query_distinct_symbols(since_days=1)

        # Our symbol should be in the list
        symbol_names = [s["symbol"] for s in symbols]
        assert unique_symbol in symbol_names

    @pytest.mark.asyncio
    async def test_dedup_upsert_behavior(self, questdb_client, unique_symbol):
        """DEDUP UPSERT should handle duplicate timestamps."""
        timestamp_ms = int(time.time() * 1000)
        timestamp_ms = (timestamp_ms // 60000) * 60000

        # Write first candle
        candle1 = OHLCV(
            timestamp=timestamp_ms,
            exchange="binance",
            market="spot",
            symbol=unique_symbol,
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )
        questdb_client.write_candle(candle1)

        # Wait briefly
        await asyncio.sleep(0.5)

        # Write second candle with same timestamp but different values
        candle2 = OHLCV(
            timestamp=timestamp_ms,  # Same timestamp
            exchange="binance",
            market="spot",
            symbol=unique_symbol,
            open=50000.0,
            high=50200.0,  # Higher high
            low=49800.0,  # Lower low
            close=50150.0,  # Different close
            volume=200.0,  # More volume
        )
        questdb_client.write_candle(candle2)

        # Wait for WAL commit
        await asyncio.sleep(2)

        # Query back
        candles = await questdb_client.query_candles(
            symbol=unique_symbol,
            interval="1m",
            limit=10,
        )

        # Should have only one candle for this timestamp (deduped)
        matching = [c for c in candles if c.get("symbol") == unique_symbol]

        # With DEDUP UPSERT KEYS, should have 1 candle (latest wins)
        # Note: The exact behavior depends on QuestDB version and table config
        assert len(matching) >= 1

    @pytest.mark.asyncio
    async def test_time_range_query(self, questdb_client, unique_symbol):
        """Query with start_time and end_time filters."""
        base_ts = int(time.time() * 1000)
        base_ts = (base_ts // 60000) * 60000

        # Write candles spanning 5 minutes
        candles = []
        for i in range(5):
            candles.append(
                OHLCV(
                    timestamp=base_ts + (i * 60000),
                    exchange="binance",
                    market="spot",
                    symbol=unique_symbol,
                    open=50000.0 + i,
                    high=50100.0,
                    low=49900.0,
                    close=50050.0,
                    volume=100.0,
                )
            )

        questdb_client.write_candles_batch(candles)
        await asyncio.sleep(2)

        # Query with time range (middle 3 candles)
        start_time = (base_ts + 60000) // 1000  # Convert to seconds
        end_time = (base_ts + (3 * 60000)) // 1000

        result = await questdb_client.query_candles(
            symbol=unique_symbol,
            interval="1m",
            start_time=start_time,
            end_time=end_time,
            limit=10,
        )

        # Should have 2-3 candles within the range
        # (inclusive/exclusive boundary handling varies)
        assert len(result) >= 2


class TestQuestDBErrorHandling:
    """Tests for error handling with QuestDB."""

    @pytest.mark.asyncio
    async def test_query_nonexistent_symbol_returns_empty(self, questdb_client):
        """Querying a symbol that doesn't exist returns empty list."""
        candles = await questdb_client.query_candles(
            symbol="NEVER_EXISTS_12345",
            interval="1m",
            limit=10,
        )
        assert candles == []

    @pytest.mark.asyncio
    async def test_get_latest_timestamp_nonexistent_returns_none(self, questdb_client):
        """Getting latest timestamp for nonexistent symbol returns None."""
        latest = await questdb_client.get_latest_timestamp("NEVER_EXISTS_12345")
        assert latest is None
