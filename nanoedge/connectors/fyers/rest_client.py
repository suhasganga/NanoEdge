"""Fyers REST API client for historical data and backfill."""

import httpx
import structlog

from nanoedge.connectors.fyers.types import (
    RESOLUTION_MAP,
    depth_decoder,
    history_decoder,
    quotes_decoder,
)
from nanoedge.core.exceptions import ExchangeError
from nanoedge.core.types import OHLCV

logger = structlog.get_logger(__name__)


class FyersRestClient:
    """
    Async REST client for Fyers API.

    Used for:
    - Historical candles (for backfilling and chart data)
    - Market depth snapshots
    - Real-time quotes
    - Symbol master CSV download

    Note:
    - Fyers API uses SECONDS for timestamps, not milliseconds
    - Max 100 days of minute data per request
    - Requires OAuth2 authentication
    """

    BASE_URL = "https://api-t1.fyers.in"

    def __init__(
        self,
        app_id: str,
        access_token: str,
    ):
        """
        Initialize Fyers REST client.

        Args:
            app_id: Fyers app ID
            access_token: OAuth2 access token (from login flow)
        """
        self.app_id = app_id
        self.access_token = access_token

        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=httpx.Timeout(15.0, connect=5.0),
            headers={
                "Authorization": f"{app_id}:{access_token}",
                "Content-Type": "application/json",
            },
        )

        # Cache of last known data timestamp per symbol (epoch seconds)
        # Used to avoid repeated API calls for time ranges after market close
        self._last_data_time: dict[str, int] = {}

    async def get_klines(
        self,
        symbol: str,
        interval: str = "1m",
        start_time: int | None = None,
        end_time: int | None = None,
        cont_flag: int = 1,
        _is_retry: bool = False,
    ) -> list[OHLCV]:
        """
        Fetch historical candles from Fyers.

        Args:
            symbol: Fyers symbol (e.g., "NSE:RELIANCE-EQ", "NSE:NIFTY50-INDEX")
            interval: Candle interval ("1m", "5m", "15m", "1h", "1d")
            start_time: Start time in MILLISECONDS (converted to seconds for API)
            end_time: End time in MILLISECONDS (converted to seconds for API)
            cont_flag: Set to 1 for continuous data (required for futures/options)
            _is_retry: Internal flag to prevent infinite recursion

        Returns:
            List of OHLCV candles with timestamps in milliseconds

        Notes:
            - Fyers API uses SECONDS, we convert from/to milliseconds
            - Max 100 days of minute data per request
            - cont_flag=1 is required for continuous data and F&O instruments
            - Response: {"s": "ok", "candles": [[ts, o, h, l, c, v], ...]}
            - If no_data with nextTime, auto-retries with adjusted time range
        """
        resolution = RESOLUTION_MAP.get(interval, "1")

        # Check if requested range is entirely after last known data (market closed)
        # This prevents repeated futile API calls for time ranges after market close
        # Note: Only skip if BOTH start AND end are after last known data
        if start_time and end_time and not _is_retry:
            start_sec = start_time // 1000
            end_sec = end_time // 1000
            last_data = self._last_data_time.get(symbol)
            if last_data:
                # Only skip if the ENTIRE range is after last known data
                # If start_time is before last_data, we should still fetch
                if start_sec > last_data and end_sec > last_data:
                    logger.info(
                        "fyers_skip_future_request",
                        symbol=symbol,
                        start_time=start_sec,
                        end_time=end_sec,
                        last_data_time=last_data,
                        message="Skipping request - entire range is after last known data",
                    )
                    return []
                else:
                    logger.debug(
                        "fyers_cache_check_passed",
                        symbol=symbol,
                        start_time=start_sec,
                        end_time=end_sec,
                        last_data_time=last_data,
                        message="Request range overlaps with available data - proceeding",
                    )

        params = {
            "symbol": symbol,
            "resolution": resolution,
            "date_format": "0",  # 0 = epoch timestamp (seconds)
        }

        # cont_flag=1 is ONLY for F&O continuous data, NOT for equity/index
        # Per Fyers docs: "set cont flag 1 for continues data and future options"
        # For equity, don't send cont_flag at all (as shown in their curl example)
        symbol_upper = symbol.upper()
        if cont_flag == 1 and not ("-EQ" in symbol_upper or "-INDEX" in symbol_upper):
            params["cont_flag"] = str(cont_flag)

        if start_time:
            params["range_from"] = str(start_time // 1000)  # ms → seconds
        if end_time:
            params["range_to"] = str(end_time // 1000)  # ms → seconds

        try:
            # Log request with human-readable timestamps for debugging
            from datetime import datetime, timezone

            range_from_str = ""
            range_to_str = ""
            if start_time:
                range_from_str = datetime.fromtimestamp(
                    start_time // 1000, tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M UTC")
            if end_time:
                range_to_str = datetime.fromtimestamp(
                    end_time // 1000, tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M UTC")

            logger.info(
                "fyers_history_request",
                symbol=symbol,
                interval=interval,
                range_from=range_from_str,
                range_to=range_to_str,
                params=params,
            )

            response = await self._client.get("/data/history", params=params)
            response.raise_for_status()

            # Log raw response for debugging
            logger.info(
                "fyers_history_response",
                symbol=symbol,
                status=response.status_code,
                content_preview=response.text[:200] if response.text else "empty",
            )

            data = history_decoder.decode(response.content)

            if data.s != "ok":
                # "no_data" with nextTime means data exists but not in requested range
                # Retry with adjusted time range ending at nextTime (only once)
                if data.s == "no_data" and data.nextTime and not _is_retry:
                    # Cache the nextTime to avoid repeated calls for future ranges
                    self._last_data_time[symbol] = data.nextTime

                    next_time_str = datetime.fromtimestamp(
                        data.nextTime, tz=timezone.utc
                    ).strftime("%Y-%m-%d %H:%M UTC")
                    logger.info(
                        "fyers_no_data_retrying",
                        symbol=symbol,
                        interval=interval,
                        next_time=next_time_str,
                        next_time_epoch=data.nextTime,
                        message="No data in range, retrying with nextTime hint",
                    )
                    # Retry with end_time = nextTime (convert to ms for recursive call)
                    # and start_time adjusted to get requested amount of data
                    new_end_ms = data.nextTime * 1000
                    interval_ms = {
                        "1m": 60_000, "5m": 300_000, "15m": 900_000,
                        "1h": 3_600_000, "1d": 86_400_000,
                    }.get(interval, 60_000)
                    # Request enough candles (500 by default)
                    new_start_ms = new_end_ms - (500 * interval_ms)
                    return await self.get_klines(
                        symbol=symbol,
                        interval=interval,
                        start_time=new_start_ms,
                        end_time=new_end_ms,
                        cont_flag=cont_flag,
                        _is_retry=True,  # Prevent infinite recursion
                    )

                # "no_data" without nextTime OR after retry means truly no data available
                if data.s == "no_data":
                    logger.info(
                        "fyers_no_data",
                        symbol=symbol,
                        interval=interval,
                        message="No data available (market may be closed or no history)",
                    )
                    return []  # Return empty list instead of raising error

                logger.error(
                    "fyers_api_error",
                    symbol=symbol,
                    status=data.s,
                    code=data.code,
                    message=data.message,
                    response_preview=response.text[:500] if response.text else "empty",
                )
                raise ExchangeError(
                    f"Fyers API error: {data.message or 'Unknown error'} (code: {data.code})",
                    code=data.code or -1,
                )

            candles = []
            market = self._get_market_from_symbol(symbol)

            for c in data.candles or []:
                # Fyers format: [timestamp_sec, open, high, low, close, volume]
                ohlcv = OHLCV(
                    timestamp=int(c[0]) * 1000,  # seconds → milliseconds
                    exchange="fyers",
                    market=market,
                    symbol=symbol,
                    open=float(c[1]),
                    high=float(c[2]),
                    low=float(c[3]),
                    close=float(c[4]),
                    volume=float(c[5]),
                    is_closed=True,
                )
                candles.append(ohlcv)

            # Update last data time cache with the latest candle timestamp
            if candles:
                last_candle_sec = candles[-1].timestamp // 1000
                current_cached = self._last_data_time.get(symbol, 0)
                if last_candle_sec > current_cached:
                    self._last_data_time[symbol] = last_candle_sec

            logger.debug(
                "fyers_klines_fetched",
                symbol=symbol,
                interval=interval,
                count=len(candles),
            )
            return candles

        except httpx.HTTPStatusError as e:
            logger.error(
                "fyers_klines_failed",
                symbol=symbol,
                status=e.response.status_code,
            )
            raise ExchangeError(
                f"Failed to fetch Fyers klines: {e.response.status_code}",
                code=e.response.status_code,
            ) from e

    async def get_depth(self, symbol: str) -> dict:
        """
        Fetch market depth snapshot.

        Args:
            symbol: Fyers symbol (e.g., "NSE:RELIANCE-EQ")

        Returns:
            Depth data dict with bids, asks, totalbuyqty, totalsellqty
        """
        try:
            response = await self._client.get(
                "/data/depth",
                params={"symbol": symbol, "ohlcv_flag": 1},
            )
            response.raise_for_status()

            data = depth_decoder.decode(response.content)

            if data.s != "ok":
                if data.s == "no_data":
                    logger.info("fyers_depth_no_data", symbol=symbol)
                    return {}  # Return empty dict instead of raising error
                raise ExchangeError(
                    f"Fyers depth error: {data.message or 'Unknown error'}",
                    code=data.code or -1,
                )

            return data.d or {}

        except httpx.HTTPStatusError as e:
            logger.error(
                "fyers_depth_failed",
                symbol=symbol,
                status=e.response.status_code,
            )
            raise ExchangeError(
                f"Failed to fetch Fyers depth: {e.response.status_code}",
                code=e.response.status_code,
            ) from e

    async def get_quotes(self, symbols: list[str]) -> dict:
        """
        Fetch real-time quotes for multiple symbols.

        Args:
            symbols: List of Fyers symbols

        Returns:
            Quote data dict
        """
        try:
            response = await self._client.get(
                "/data/quotes",
                params={"symbols": ",".join(symbols)},
            )
            response.raise_for_status()

            data = quotes_decoder.decode(response.content)

            if data.s != "ok":
                if data.s == "no_data":
                    logger.info("fyers_quotes_no_data", symbols=symbols)
                    return {"quotes": []}  # Return empty list instead of raising error
                raise ExchangeError(
                    f"Fyers quotes error: {data.message or 'Unknown error'}",
                    code=data.code or -1,
                )

            return {"quotes": data.d or []}

        except httpx.HTTPStatusError as e:
            logger.error(
                "fyers_quotes_failed",
                symbols=symbols,
                status=e.response.status_code,
            )
            raise ExchangeError(
                f"Failed to fetch Fyers quotes: {e.response.status_code}",
                code=e.response.status_code,
            ) from e

    def _get_market_from_symbol(self, symbol: str) -> str:
        """
        Infer market type from Fyers symbol format.

        Fyers symbol formats:
        - NSE:RELIANCE-EQ → equity
        - NSE:NIFTY50-INDEX → index
        - NSE:NIFTY25JAN24000CE → options
        - NSE:NIFTY25JANFUT → futures
        - MCX:GOLD → commodity
        - NSE:USDINR → currency
        """
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
        elif "USDINR" in symbol_upper or "EURINR" in symbol_upper:
            return "currency"
        return "equity"  # Default

    def clear_cache(self, symbol: str | None = None) -> None:
        """
        Clear the last data time cache.

        Args:
            symbol: Specific symbol to clear, or None to clear all.

        This is useful when switching back to a symbol where QuestDB might
        not have committed data yet (WAL delay), ensuring we re-fetch from API.
        """
        if symbol:
            if symbol in self._last_data_time:
                logger.debug("fyers_cache_cleared", symbol=symbol)
                del self._last_data_time[symbol]
        else:
            self._last_data_time.clear()
            logger.debug("fyers_cache_cleared_all")

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()
        logger.debug("fyers_rest_client_closed")

    async def __aenter__(self) -> "FyersRestClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
