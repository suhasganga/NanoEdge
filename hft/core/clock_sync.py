"""Clock synchronization with exchange servers.

Calculates and maintains the offset between local time and exchange time
to enable accurate latency measurements.

Supports multiple exchanges with independent clock offsets:
- Binance: Uses /api/v3/time endpoint (public, no auth)
- Fyers: Uses HTTP Date header from /data/marketStatus (requires auth)
"""

import asyncio
import time
from dataclasses import dataclass
from email.utils import parsedate_to_datetime

import httpx
import structlog

logger = structlog.get_logger(__name__)


@dataclass
class ClockOffset:
    """Clock offset measurement result."""

    offset_ms: float  # Local time - Exchange time (positive = local ahead)
    rtt_ms: float  # Round-trip time of the measurement
    measured_at: float  # Local timestamp when measured


class ClockSync:
    """Maintains clock synchronization with exchange servers.

    Uses NTP-style algorithm:
    1. Record local time T1
    2. Send request to exchange /time endpoint
    3. Receive exchange time Te
    4. Record local time T2
    5. Estimate offset = ((T1 + T2) / 2) - Te

    The offset represents: local_time - exchange_time
    To convert exchange timestamp to local: exch_ts + offset
    """

    def __init__(
        self,
        exchange: str = "binance",
        sync_interval_sec: float = 60.0,
        sample_count: int = 5,
        auth_header: str | None = None,
    ):
        """Initialize clock sync for an exchange.

        Args:
            exchange: Exchange name (binance, binance_futures, fyers)
            sync_interval_sec: Interval between sync cycles
            sample_count: Number of samples per sync cycle
            auth_header: Optional auth header for exchanges that require it (e.g., Fyers)
        """
        self.exchange = exchange
        self.sync_interval_sec = sync_interval_sec
        self.sample_count = sample_count
        self._auth_header = auth_header

        self._offset_ms: float = 0.0
        self._rtt_ms: float = 0.0
        self._last_sync: float = 0.0
        self._running = False
        self._task: asyncio.Task | None = None
        self._client: httpx.AsyncClient | None = None

        # Exchange time endpoints
        self._time_urls = {
            "binance": "https://api.binance.com/api/v3/time",
            "binance_futures": "https://fapi.binance.com/fapi/v1/time",
            "fyers": "https://api-t1.fyers.in/data/marketStatus",
        }

        # Exchanges that use HTTP Date header instead of JSON response
        self._uses_header_time: set[str] = {"fyers"}

    @property
    def offset_ms(self) -> float:
        """Current clock offset in milliseconds (local - exchange)."""
        return self._offset_ms

    @property
    def rtt_ms(self) -> float:
        """Last measured round-trip time in milliseconds."""
        return self._rtt_ms

    def adjust_exchange_ts(self, exch_ts_ms: int) -> int:
        """Adjust exchange timestamp to local time.

        Args:
            exch_ts_ms: Timestamp from exchange in milliseconds

        Returns:
            Adjusted timestamp in local time (milliseconds)
        """
        return int(exch_ts_ms + self._offset_ms)

    async def _measure_offset(self) -> ClockOffset | None:
        """Perform a single clock offset measurement."""
        if not self._client:
            return None

        url = self._time_urls.get(self.exchange)
        if not url:
            logger.warning("clock_sync_unknown_exchange", exchange=self.exchange)
            return None

        try:
            # Prepare headers (auth required for some exchanges)
            headers = {}
            if self._auth_header and self.exchange in self._uses_header_time:
                headers["Authorization"] = self._auth_header

            t1 = time.time() * 1000  # Local time before request (ms)
            response = await self._client.get(url, headers=headers, timeout=5.0)
            t2 = time.time() * 1000  # Local time after response (ms)

            if response.status_code != 200:
                logger.warning(
                    "clock_sync_request_failed",
                    exchange=self.exchange,
                    status=response.status_code,
                )
                return None

            # Extract exchange time based on exchange type
            te: int = 0
            if self.exchange in self._uses_header_time:
                # Extract time from HTTP Date header (RFC 2822 format)
                date_str = response.headers.get("Date")
                if date_str:
                    try:
                        dt = parsedate_to_datetime(date_str)
                        te = int(dt.timestamp() * 1000)
                    except Exception as e:
                        logger.warning(
                            "clock_sync_date_parse_error",
                            exchange=self.exchange,
                            date_str=date_str,
                            error=str(e),
                        )
                        return None
            else:
                # Extract from JSON response (Binance style)
                data = response.json()
                te = data.get("serverTime", 0)

            if te == 0:
                logger.warning(
                    "clock_sync_no_server_time",
                    exchange=self.exchange,
                )
                return None

            # NTP-style offset calculation
            # Assumes symmetric network delay
            rtt = t2 - t1
            local_estimate = (t1 + t2) / 2
            offset = local_estimate - te

            return ClockOffset(
                offset_ms=offset,
                rtt_ms=rtt,
                measured_at=t2,
            )

        except Exception as e:
            logger.warning("clock_sync_error", exchange=self.exchange, error=str(e))
            return None

    async def _sync_once(self) -> bool:
        """Perform clock synchronization with multiple samples."""
        samples: list[ClockOffset] = []

        for _ in range(self.sample_count):
            result = await self._measure_offset()
            if result:
                samples.append(result)
            await asyncio.sleep(0.1)  # Small delay between samples

        if not samples:
            logger.warning("clock_sync_no_samples", exchange=self.exchange)
            return False

        # Use median offset (robust to outliers)
        samples.sort(key=lambda x: x.offset_ms)
        median_idx = len(samples) // 2
        best = samples[median_idx]

        self._offset_ms = best.offset_ms
        self._rtt_ms = best.rtt_ms
        self._last_sync = best.measured_at

        logger.info(
            "clock_sync_complete",
            exchange=self.exchange,
            offset_ms=round(self._offset_ms, 2),
            rtt_ms=round(self._rtt_ms, 2),
            samples=len(samples),
        )
        return True

    async def _sync_loop(self) -> None:
        """Background loop for periodic clock synchronization."""
        while self._running:
            try:
                await self._sync_once()
                await asyncio.sleep(self.sync_interval_sec)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(
                    "clock_sync_loop_error", exchange=self.exchange, error=str(e)
                )
                await asyncio.sleep(5.0)  # Retry after error

    async def start(self) -> None:
        """Start background clock synchronization."""
        if self._running:
            return

        self._running = True
        self._client = httpx.AsyncClient()

        # Initial sync
        await self._sync_once()

        # Start background sync
        self._task = asyncio.create_task(self._sync_loop())
        logger.info("clock_sync_started", exchange=self.exchange)

    async def stop(self) -> None:
        """Stop background clock synchronization."""
        self._running = False

        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None

        if self._client:
            await self._client.aclose()
            self._client = None

        logger.info("clock_sync_stopped", exchange=self.exchange)


class ClockSyncRegistry:
    """Manages clock synchronization for multiple exchanges.

    Provides a central registry for per-exchange clock sync instances,
    allowing each exchange to have its own independent clock offset.
    """

    def __init__(self):
        self._syncs: dict[str, ClockSync] = {}

    def register(self, exchange: str, sync: ClockSync) -> None:
        """Register a clock sync instance for an exchange.

        Args:
            exchange: Exchange name
            sync: ClockSync instance for this exchange
        """
        self._syncs[exchange] = sync
        logger.info("clock_sync_registered", exchange=exchange)

    def get(self, exchange: str) -> ClockSync | None:
        """Get clock sync instance for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            ClockSync instance or None if not registered
        """
        return self._syncs.get(exchange)

    def adjust_timestamp(self, exchange: str, ts_ms: int) -> int:
        """Adjust timestamp for a specific exchange.

        Args:
            exchange: Exchange name
            ts_ms: Timestamp in milliseconds

        Returns:
            Adjusted timestamp (or original if no sync available)
        """
        sync = self._syncs.get(exchange)
        if sync:
            return sync.adjust_exchange_ts(ts_ms)
        return ts_ms  # No adjustment if no sync registered

    async def start_all(self) -> None:
        """Start all registered clock syncs."""
        for exchange, sync in self._syncs.items():
            try:
                await sync.start()
            except Exception as e:
                logger.error(
                    "clock_sync_start_error", exchange=exchange, error=str(e)
                )

    async def stop_all(self) -> None:
        """Stop all registered clock syncs."""
        for exchange, sync in self._syncs.items():
            try:
                await sync.stop()
            except Exception as e:
                logger.error("clock_sync_stop_error", exchange=exchange, error=str(e))

    def get_all_offsets(self) -> dict[str, dict]:
        """Get offset info for all registered exchanges.

        Returns:
            Dict mapping exchange name to offset info
        """
        return {
            name: {
                "offset_ms": round(sync.offset_ms, 2),
                "rtt_ms": round(sync.rtt_ms, 2),
            }
            for name, sync in self._syncs.items()
        }


# Global registry for the application
clock_sync_registry = ClockSyncRegistry()

# Legacy global instance for backward compatibility (Binance only)
# TODO: Remove once all code uses clock_sync_registry
clock_sync = ClockSync()
