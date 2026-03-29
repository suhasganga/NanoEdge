"""Tests for Binance REST client."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from nanoedge.connectors.binance.rest_client import BinanceRestClient
from nanoedge.connectors.binance.types import BinanceDepthSnapshot
from nanoedge.core.exceptions import ExchangeError


class TestBinanceRestClientInit:
    """Tests for BinanceRestClient initialization."""

    def test_default_base_url(self):
        """Default base URL is Binance API."""
        client = BinanceRestClient()
        assert client.base_url == "https://api.binance.com"

    def test_custom_base_url(self):
        """Can set custom base URL."""
        client = BinanceRestClient(base_url="https://testnet.binance.vision")
        assert client.base_url == "https://testnet.binance.vision"


class TestGetDepthSnapshot:
    """Tests for get_depth_snapshot method."""

    @pytest.mark.asyncio
    async def test_success(self):
        """Fetch depth snapshot successfully."""
        mock_response = MagicMock()
        mock_response.content = b'{"lastUpdateId":12345,"bids":[["50000.00","1.5"]],"asks":[["50001.00","0.5"]]}'
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                snapshot = await client.get_depth_snapshot("BTCUSDT")

            assert isinstance(snapshot, BinanceDepthSnapshot)
            assert snapshot.lastUpdateId == 12345
            assert len(snapshot.bids) == 1
            assert len(snapshot.asks) == 1

    @pytest.mark.asyncio
    async def test_symbol_uppercase(self):
        """Symbol is converted to uppercase."""
        mock_response = MagicMock()
        mock_response.content = b'{"lastUpdateId":1,"bids":[],"asks":[]}'
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                await client.get_depth_snapshot("btcusdt")

            # Check that symbol was uppercased
            call_args = mock_get.call_args
            assert call_args[1]["params"]["symbol"] == "BTCUSDT"

    @pytest.mark.asyncio
    async def test_limit_parameter(self):
        """Limit parameter is passed correctly."""
        mock_response = MagicMock()
        mock_response.content = b'{"lastUpdateId":1,"bids":[],"asks":[]}'
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                await client.get_depth_snapshot("BTCUSDT", limit=5000)

            call_args = mock_get.call_args
            assert call_args[1]["params"]["limit"] == 5000

    @pytest.mark.asyncio
    async def test_http_error_raises_exchange_error(self):
        """HTTP error raises ExchangeError."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_response.raise_for_status = MagicMock(
            side_effect=httpx.HTTPStatusError(
                "Bad Request", request=MagicMock(), response=mock_response
            )
        )

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                with pytest.raises(ExchangeError) as exc_info:
                    await client.get_depth_snapshot("INVALID")

            assert exc_info.value.code == 400


class TestGetKlines:
    """Tests for get_klines method."""

    @pytest.mark.asyncio
    async def test_success(self):
        """Fetch klines successfully."""
        mock_klines = [
            [1704067200000, "50000", "50100", "49900", "50050", "100", 1704067259999, "5000000", 500, "50", "2500000", "0"],
            [1704067260000, "50050", "50150", "50000", "50100", "110", 1704067319999, "5500000", 550, "55", "2750000", "0"],
        ]

        mock_response = MagicMock()
        mock_response.json.return_value = mock_klines
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                klines = await client.get_klines("BTCUSDT")

            assert len(klines) == 2
            assert klines[0][0] == 1704067200000  # Open time
            assert klines[0][1] == "50000"  # Open price

    @pytest.mark.asyncio
    async def test_with_time_range(self):
        """Fetch klines with time range."""
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                await client.get_klines(
                    "BTCUSDT",
                    start_time=1704067200000,
                    end_time=1704070800000,
                )

            call_args = mock_get.call_args
            assert call_args[1]["params"]["startTime"] == 1704067200000
            assert call_args[1]["params"]["endTime"] == 1704070800000

    @pytest.mark.asyncio
    async def test_limit_capped_at_1000(self):
        """Limit is capped at 1000."""
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                await client.get_klines("BTCUSDT", limit=5000)

            call_args = mock_get.call_args
            assert call_args[1]["params"]["limit"] == 1000  # Capped

    @pytest.mark.asyncio
    async def test_interval_parameter(self):
        """Interval parameter is passed correctly."""
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                await client.get_klines("BTCUSDT", interval="1h")

            call_args = mock_get.call_args
            assert call_args[1]["params"]["interval"] == "1h"

    @pytest.mark.asyncio
    async def test_http_error_raises_exchange_error(self):
        """HTTP error raises ExchangeError."""
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.raise_for_status = MagicMock(
            side_effect=httpx.HTTPStatusError(
                "Rate Limited", request=MagicMock(), response=mock_response
            )
        )

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                with pytest.raises(ExchangeError) as exc_info:
                    await client.get_klines("BTCUSDT")

            assert exc_info.value.code == 429


class TestGetExchangeInfo:
    """Tests for get_exchange_info method."""

    @pytest.mark.asyncio
    async def test_all_symbols(self):
        """Fetch exchange info for all symbols."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "timezone": "UTC",
            "serverTime": 1704067200000,
            "symbols": [{"symbol": "BTCUSDT"}, {"symbol": "ETHUSDT"}],
        }
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                info = await client.get_exchange_info()

            assert "symbols" in info
            assert len(info["symbols"]) == 2

    @pytest.mark.asyncio
    async def test_single_symbol(self):
        """Fetch exchange info for single symbol."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"symbols": [{"symbol": "BTCUSDT"}]}
        mock_response.raise_for_status = MagicMock()

        with patch.object(httpx.AsyncClient, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response

            async with BinanceRestClient() as client:
                await client.get_exchange_info(symbol="btcusdt")

            call_args = mock_get.call_args
            assert call_args[1]["params"]["symbol"] == "BTCUSDT"


class TestLifecycle:
    """Tests for client lifecycle."""

    @pytest.mark.asyncio
    async def test_close(self):
        """Close closes the HTTP client."""
        client = BinanceRestClient()

        with patch.object(client._client, "aclose", new_callable=AsyncMock) as mock_close:
            await client.close()
            mock_close.assert_called_once()

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Client works as async context manager."""
        with patch.object(httpx.AsyncClient, "aclose", new_callable=AsyncMock):
            async with BinanceRestClient() as client:
                assert client is not None

    @pytest.mark.asyncio
    async def test_context_manager_closes_on_exit(self):
        """Context manager closes client on exit."""
        with patch.object(httpx.AsyncClient, "aclose", new_callable=AsyncMock) as mock_close:
            async with BinanceRestClient():
                pass
            mock_close.assert_called_once()
