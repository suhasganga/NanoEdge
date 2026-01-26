"""Binance REST API client for snapshots and historical data."""

import httpx
import structlog

from hft.connectors.binance.types import BinanceDepthSnapshot, depth_snapshot_decoder
from hft.core.exceptions import ExchangeError

logger = structlog.get_logger(__name__)


class BinanceRestClient:
    """
    Async REST client for Binance API.

    Used for:
    - Order book snapshots (for local book initialization)
    - Historical klines (for backfilling)
    """

    def __init__(self, base_url: str = "https://api.binance.com"):
        """
        Initialize REST client.

        Args:
            base_url: Binance REST API base URL
        """
        self.base_url = base_url
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=httpx.Timeout(10.0, connect=5.0),
            limits=httpx.Limits(max_connections=10, max_keepalive_connections=5),
        )

    async def get_depth_snapshot(
        self, symbol: str, limit: int = 1000
    ) -> BinanceDepthSnapshot:
        """
        Fetch order book snapshot.

        Args:
            symbol: Trading pair (e.g., "BTCUSDT")
            limit: Number of levels (5, 10, 20, 50, 100, 500, 1000, 5000)
                   Weight: 5/10/20/50/100=5, 500=10, 1000=50, 5000=250

        Returns:
            BinanceDepthSnapshot with lastUpdateId, bids, asks

        Raises:
            ExchangeError: On API error
        """
        try:
            response = await self._client.get(
                "/api/v3/depth",
                params={"symbol": symbol.upper(), "limit": limit},
            )
            response.raise_for_status()

            snapshot = depth_snapshot_decoder.decode(response.content)
            logger.debug(
                "depth_snapshot_fetched",
                symbol=symbol,
                last_update_id=snapshot.lastUpdateId,
                bid_levels=len(snapshot.bids),
                ask_levels=len(snapshot.asks),
            )
            return snapshot

        except httpx.HTTPStatusError as e:
            logger.error(
                "depth_snapshot_failed",
                symbol=symbol,
                status=e.response.status_code,
                body=e.response.text[:500],
            )
            raise ExchangeError(
                f"Failed to fetch depth snapshot: {e.response.status_code}",
                code=e.response.status_code,
            ) from e

    async def get_klines(
        self,
        symbol: str,
        interval: str = "1m",
        limit: int = 500,
        start_time: int | None = None,
        end_time: int | None = None,
    ) -> list[list]:
        """
        Fetch historical klines/candlesticks.

        Args:
            symbol: Trading pair (e.g., "BTCUSDT")
            interval: Kline interval (1m, 5m, 15m, 1h, 1d, etc.)
            limit: Number of klines (max 1000)
            start_time: Start time in milliseconds
            end_time: End time in milliseconds

        Returns:
            List of kline arrays:
            [open_time, open, high, low, close, volume, close_time,
             quote_volume, trades, taker_buy_base, taker_buy_quote, ignore]

        Raises:
            ExchangeError: On API error
        """
        params: dict = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": min(limit, 1000),
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        try:
            response = await self._client.get("/api/v3/klines", params=params)
            response.raise_for_status()

            klines = response.json()
            logger.debug(
                "klines_fetched",
                symbol=symbol,
                interval=interval,
                count=len(klines),
            )
            return klines

        except httpx.HTTPStatusError as e:
            logger.error(
                "klines_fetch_failed",
                symbol=symbol,
                interval=interval,
                status=e.response.status_code,
            )
            raise ExchangeError(
                f"Failed to fetch klines: {e.response.status_code}",
                code=e.response.status_code,
            ) from e

    async def get_exchange_info(self, symbol: str | None = None) -> dict:
        """
        Fetch exchange info (symbol filters, rate limits).

        Args:
            symbol: Optional specific symbol to query

        Returns:
            Exchange info dictionary
        """
        params = {}
        if symbol:
            params["symbol"] = symbol.upper()

        response = await self._client.get("/api/v3/exchangeInfo", params=params)
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()
        logger.debug("rest_client_closed")

    async def __aenter__(self) -> "BinanceRestClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
