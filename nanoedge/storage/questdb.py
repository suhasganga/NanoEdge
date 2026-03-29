"""QuestDB client for candle storage and queries."""

import httpx
import structlog
from questdb.ingress import Sender, TimestampNanos, IngressError, Protocol

from nanoedge.core.types import OHLCV

logger = structlog.get_logger(__name__)


class QuestDBClient:
    """
    QuestDB client for time-series candle storage.

    Uses:
    - ILP (InfluxDB Line Protocol) for high-performance writes
    - HTTP API for SQL queries with SAMPLE BY aggregation
    """

    def __init__(
        self,
        host: str = "localhost",
        ilp_port: int = 9009,
        http_port: int = 9000,
    ):
        """
        Initialize QuestDB client.

        Args:
            host: QuestDB server hostname
            ilp_port: ILP ingestion port (default: 9009)
            http_port: HTTP API port (default: 9000)
        """
        self.host = host
        self.ilp_port = ilp_port
        self.http_port = http_port

        self._http = httpx.AsyncClient(
            base_url=f"http://{host}:{http_port}",
            timeout=30.0,
        )

        # Persistent ILP sender (HTTP protocol for better error handling)
        self._sender: Sender | None = None

    async def init_schema(self) -> None:
        """Create candles table if it doesn't exist."""
        create_sql = """
        CREATE TABLE IF NOT EXISTS candles_1m (
            timestamp TIMESTAMP,
            exchange SYMBOL CAPACITY 10 CACHE INDEX,
            market SYMBOL CAPACITY 20 CACHE INDEX,
            symbol SYMBOL CAPACITY 50000 CACHE INDEX,
            open DOUBLE,
            high DOUBLE,
            low DOUBLE,
            close DOUBLE,
            volume DOUBLE,
            quote_volume DOUBLE,
            trade_count INT,
            vwap DOUBLE
        ) TIMESTAMP(timestamp)
        PARTITION BY DAY
        WAL
        DEDUP UPSERT KEYS(timestamp, exchange, market, symbol);
        """

        try:
            await self._execute_sql(create_sql)
            logger.info("questdb_schema_initialized")
        except Exception as e:
            # Table might already exist with slightly different schema
            logger.warning("questdb_schema_init_warning", error=str(e))

    async def _execute_sql(self, sql: str) -> dict | None:
        """Execute SQL query via HTTP API."""
        try:
            response = await self._http.get("/exec", params={"query": sql})
            response.raise_for_status()
            return response.json() if response.content else None
        except httpx.HTTPStatusError as e:
            logger.error(
                "questdb_query_error",
                status=e.response.status_code,
                error=e.response.text[:500],
                sql=sql[:200],
            )
            raise
        except Exception as e:
            logger.error("questdb_query_error", error=str(e), sql=sql[:200])
            raise

    def _get_sender(self) -> Sender:
        """Get or create persistent ILP sender using TCP protocol."""
        if self._sender is None:
            # Use TCP protocol (port 9009) which is simpler and doesn't require HTTP ILP setup
            self._sender = Sender(Protocol.Tcp, self.host, self.ilp_port)
            self._sender.establish()  # CRITICAL: Must establish connection before use
            logger.info(
                "questdb_sender_created",
                host=self.host,
                port=self.ilp_port,
                protocol="tcp",
            )
        return self._sender

    def _close_sender(self) -> None:
        """Close ILP sender for cleanup or reconnection."""
        if self._sender is not None:
            try:
                self._sender.close()
            except Exception as e:
                logger.warning("questdb_sender_close_error", error=str(e))
            self._sender = None

    def write_candle(self, candle: OHLCV) -> None:
        """
        Write completed candle via ILP using persistent TCP sender.

        This is synchronous for use in callbacks. ILP is already
        very fast and non-blocking at the network level.

        Args:
            candle: OHLCV candle to write (includes exchange/market fields)
        """
        logger.debug(
            "candle_write_starting",
            symbol=candle.symbol,
            exchange=candle.exchange,
            timestamp=candle.timestamp,
        )
        try:
            # Use persistent sender (reuse connection)
            sender = self._get_sender()
            sender.row(
                "candles_1m",
                symbols={
                    "exchange": candle.exchange,
                    "market": candle.market,
                    "symbol": candle.symbol,
                },
                columns={
                    "open": candle.open,
                    "high": candle.high,
                    "low": candle.low,
                    "close": candle.close,
                    "volume": candle.volume,
                    "quote_volume": candle.quote_volume,
                    "trade_count": candle.trade_count,
                    "vwap": candle.vwap,
                },
                at=TimestampNanos(candle.timestamp * 1_000_000),  # ms to ns
            )
            sender.flush()

            logger.info(
                "candle_written",
                symbol=candle.symbol,
                exchange=candle.exchange,
                timestamp=candle.timestamp,
            )

        except IngressError as e:
            # HTTP protocol provides proper error feedback
            logger.error(
                "candle_write_error",
                symbol=candle.symbol,
                error=str(e),
                error_type="IngressError",
            )
            # Reset sender on error for reconnection
            self._close_sender()

        except Exception as e:
            logger.error(
                "candle_write_error",
                symbol=candle.symbol,
                error=str(e),
                error_type=type(e).__name__,
            )
            # Reset sender on unexpected errors
            self._close_sender()

    def write_candles_batch(self, candles: list[OHLCV]) -> int:
        """
        Write multiple candles in a single batch.

        Args:
            candles: List of OHLCV candles to write (includes exchange/market fields)

        Returns:
            Number of candles successfully written
        """
        if not candles:
            return 0

        try:
            sender = self._get_sender()

            for candle in candles:
                sender.row(
                    "candles_1m",
                    symbols={
                        "exchange": candle.exchange,
                        "market": candle.market,
                        "symbol": candle.symbol,
                    },
                    columns={
                        "open": candle.open,
                        "high": candle.high,
                        "low": candle.low,
                        "close": candle.close,
                        "volume": candle.volume,
                        "quote_volume": candle.quote_volume,
                        "trade_count": candle.trade_count,
                        "vwap": candle.vwap,
                    },
                    at=TimestampNanos(candle.timestamp * 1_000_000),
                )

            sender.flush()
            logger.info(
                "candles_batch_written",
                symbol=candles[0].symbol,
                exchange=candles[0].exchange,
                count=len(candles),
            )
            return len(candles)

        except Exception as e:
            logger.error(
                "candles_batch_write_error",
                error=str(e),
                count=len(candles),
            )
            self._close_sender()
            return 0

    async def query_candles(
        self,
        symbol: str,
        interval: str = "1m",
        limit: int = 500,
        start_time: int | None = None,
        end_time: int | None = None,
        exchange: str = "binance",
        market: str = "spot",
    ) -> list[dict]:
        """
        Query candles with optional SAMPLE BY aggregation.

        Args:
            symbol: Trading pair (e.g., "BTCUSDT")
            interval: Candle interval (1m, 5m, 15m, 1h, 1d)
            limit: Maximum number of candles
            start_time: Start time (Unix seconds)
            end_time: End time (Unix seconds)
            exchange: Exchange filter
            market: Market type filter

        Returns:
            List of candle dicts with time, open, high, low, close, volume
        """
        import time as time_module

        # Build WHERE clause
        # Note: market may be NULL for historical data (before market column was added)
        # so we use (market = X OR market IS NULL) for backward compatibility
        where_parts = [
            f"exchange = '{exchange}'",
            f"(market = '{market}' OR market IS NULL)",
            f"symbol = '{symbol}'",
        ]

        # Calculate default lookback if no start_time provided
        # This fixes QuestDB SAMPLE BY + ORDER BY DESC LIMIT bug with large datasets
        interval_seconds = {
            "1m": 60,
            "5m": 300,
            "15m": 900,
            "30m": 1800,
            "1h": 3600,
            "4h": 14400,
            "1d": 86400,
        }
        if not start_time and interval != "1m":
            # For aggregated queries, add a default lookback to help SAMPLE BY
            # Use 2x the requested candles as buffer
            lookback_seconds = interval_seconds.get(interval, 86400) * limit * 2
            default_start = int(time_module.time()) - lookback_seconds
            where_parts.append(f"timestamp >= {default_start * 1_000_000}")

        if start_time:
            # Convert seconds to microseconds for QuestDB
            where_parts.append(f"timestamp >= {start_time * 1_000_000}")
        if end_time:
            where_parts.append(f"timestamp <= {end_time * 1_000_000}")

        where_clause = " AND ".join(where_parts)

        # Build query based on interval
        if interval == "1m":
            # No aggregation needed
            sql = f"""
            SELECT
                timestamp,
                exchange,
                market,
                symbol,
                open,
                high,
                low,
                close,
                volume,
                quote_volume,
                trade_count,
                vwap
            FROM candles_1m
            WHERE {where_clause}
            ORDER BY timestamp DESC
            LIMIT {limit}
            """
        else:
            # Use GROUP BY with timestamp_floor for aggregation
            # This is more reliable than SAMPLE BY for queries with ORDER BY DESC LIMIT
            # timestamp_floor ensures the returned timestamp is at the period boundary
            # (e.g., midnight for 1d, top of hour for 1h)
            sql = f"""
            SELECT
                timestamp_floor('{interval}', timestamp) as period_ts,
                first(exchange) as exchange,
                first(market) as market,
                first(symbol) as symbol,
                first(open) as open,
                max(high) as high,
                min(low) as low,
                last(close) as close,
                sum(volume) as volume,
                sum(quote_volume) as quote_volume,
                sum(trade_count) as trade_count,
                sum(vwap * volume) / sum(volume) as vwap
            FROM candles_1m
            WHERE {where_clause}
            GROUP BY timestamp_floor('{interval}', timestamp)
            ORDER BY period_ts DESC
            LIMIT {limit}
            """

        try:
            logger.debug(
                "questdb_query_executing",
                symbol=symbol,
                interval=interval,
                sql=sql[:500],
            )
            result = await self._execute_sql(sql)

            if not result or "dataset" not in result:
                return []

            columns = result["columns"]
            col_names = [c["name"] for c in columns]

            candles = []
            for row in result["dataset"]:
                candle = dict(zip(col_names, row))
                # Rename period_ts back to timestamp for consistency
                if "period_ts" in candle:
                    candle["timestamp"] = candle.pop("period_ts")
                candles.append(candle)

            logger.debug(
                "questdb_query_result",
                symbol=symbol,
                interval=interval,
                count=len(candles),
                first_ts=candles[0].get("timestamp") if candles else None,
                last_ts=candles[-1].get("timestamp") if candles else None,
            )

            # Return in chronological order (oldest first)
            return list(reversed(candles))

        except Exception as e:
            logger.error(
                "candle_query_error",
                symbol=symbol,
                interval=interval,
                error=str(e),
            )
            return []

    async def query_distinct_symbols(self, since_days: int = 30) -> list[dict]:
        """
        Get all unique symbols with data in the last N days.

        Used for startup backfill to find all symbols that need gap-filling.

        Args:
            since_days: Only consider symbols with data in last N days

        Returns:
            List of dicts with keys: symbol, exchange, market, latest_ts (ms)
        """
        sql = f"""
        SELECT symbol, exchange, market, max(timestamp) as latest_ts
        FROM candles_1m
        WHERE timestamp > dateadd('d', -{since_days}, now())
        GROUP BY symbol, exchange, market
        ORDER BY symbol
        """

        try:
            result = await self._execute_sql(sql)

            if not result or "dataset" not in result:
                return []

            symbols = []
            for row in result["dataset"]:
                symbol_name, exchange, market, latest_ts = row
                # Convert QuestDB timestamp to milliseconds
                # QuestDB may return microseconds (int) or ISO string depending on version
                if isinstance(latest_ts, str):
                    from datetime import datetime
                    dt = datetime.fromisoformat(latest_ts.replace("Z", "+00:00"))
                    latest_ts_ms = int(dt.timestamp() * 1000)
                elif latest_ts:
                    latest_ts_ms = latest_ts // 1000  # microseconds to ms
                else:
                    latest_ts_ms = None
                symbols.append({
                    "symbol": symbol_name,
                    "exchange": exchange or "binance",
                    "market": market or "spot",
                    "latest_ts": latest_ts_ms,
                })

            logger.info(
                "questdb_distinct_symbols",
                count=len(symbols),
                since_days=since_days,
            )
            return symbols

        except Exception as e:
            logger.error("distinct_symbols_query_error", error=str(e))
            return []

    async def get_latest_timestamp(
        self,
        symbol: str,
        exchange: str = "binance",
        market: str = "spot",
    ) -> int | None:
        """
        Get timestamp of most recent candle.

        Returns:
            Timestamp in milliseconds, or None if no data
        """
        sql = f"""
        SELECT max(timestamp) as latest
        FROM candles_1m
        WHERE exchange = '{exchange}' AND (market = '{market}' OR market IS NULL) AND symbol = '{symbol}'
        """

        try:
            result = await self._execute_sql(sql)
            if result and "dataset" in result and result["dataset"]:
                latest = result["dataset"][0][0]
                if latest:
                    # QuestDB may return microseconds (int) or ISO string depending on version
                    if isinstance(latest, str):
                        from datetime import datetime
                        dt = datetime.fromisoformat(latest.replace("Z", "+00:00"))
                        return int(dt.timestamp() * 1000)
                    else:
                        # QuestDB returns microseconds, convert to ms
                        return latest // 1000
        except Exception as e:
            logger.error("latest_timestamp_query_error", error=str(e))

        return None

    async def close(self) -> None:
        """Close all connections."""
        self._close_sender()
        await self._http.aclose()
        logger.debug("questdb_client_closed")

    async def __aenter__(self) -> "QuestDBClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
