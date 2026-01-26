"""Latency histogram and metrics collection for HFT platform.

Provides rolling-window latency histograms with percentile calculations (p50, p95, p99).
Logs summary statistics periodically to track system performance.
"""

import time
from collections import deque
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import numpy as np
import structlog

if TYPE_CHECKING:
    from collections.abc import Iterable

logger = structlog.get_logger(__name__)


@dataclass
class LatencyHistogram:
    """Rolling window latency histogram with percentile calculations.

    Maintains a fixed-size window of latency samples and provides
    efficient percentile calculations using numpy.

    Attributes:
        name: Identifier for this histogram (used in logging)
        window_size: Maximum number of samples to retain
    """

    name: str
    window_size: int = 10000
    _samples: deque = field(default_factory=lambda: deque(maxlen=10000))
    _count: int = 0
    _sum: float = 0.0
    _min: float = float("inf")
    _max: float = 0.0

    def __post_init__(self) -> None:
        """Ensure deque has correct maxlen."""
        if self._samples.maxlen != self.window_size:
            self._samples = deque(maxlen=self.window_size)

    def record(self, latency_us: float) -> None:
        """Record a latency sample in microseconds.

        Args:
            latency_us: Latency value in microseconds
        """
        self._samples.append(latency_us)
        self._count += 1
        self._sum += latency_us
        if latency_us < self._min:
            self._min = latency_us
        if latency_us > self._max:
            self._max = latency_us

    def record_batch(self, latencies: "Iterable[float]") -> None:
        """Record multiple latency samples.

        Args:
            latencies: Iterable of latency values in microseconds
        """
        for latency in latencies:
            self.record(latency)

    def percentile(self, p: float) -> float:
        """Get percentile value.

        Args:
            p: Percentile to calculate (0-100)

        Returns:
            Percentile value in microseconds, or 0.0 if no samples
        """
        if not self._samples:
            return 0.0
        return float(np.percentile(list(self._samples), p))

    @property
    def p50(self) -> float:
        """Median latency in microseconds."""
        return self.percentile(50)

    @property
    def p95(self) -> float:
        """95th percentile latency in microseconds."""
        return self.percentile(95)

    @property
    def p99(self) -> float:
        """99th percentile latency in microseconds."""
        return self.percentile(99)

    @property
    def p999(self) -> float:
        """99.9th percentile latency in microseconds."""
        return self.percentile(99.9)

    @property
    def mean(self) -> float:
        """Mean latency in microseconds."""
        if not self._samples:
            return 0.0
        return float(np.mean(list(self._samples)))

    @property
    def stddev(self) -> float:
        """Standard deviation of latency in microseconds."""
        if len(self._samples) < 2:
            return 0.0
        return float(np.std(list(self._samples)))

    @property
    def min_latency(self) -> float:
        """Minimum recorded latency in microseconds."""
        return self._min if self._min != float("inf") else 0.0

    @property
    def max_latency(self) -> float:
        """Maximum recorded latency in microseconds."""
        return self._max

    @property
    def count(self) -> int:
        """Total number of samples recorded (including evicted)."""
        return self._count

    @property
    def current_samples(self) -> int:
        """Number of samples currently in the window."""
        return len(self._samples)

    def reset(self) -> None:
        """Reset the histogram, clearing all samples and stats."""
        self._samples.clear()
        self._count = 0
        self._sum = 0.0
        self._min = float("inf")
        self._max = 0.0

    def to_dict(self) -> dict:
        """Export histogram stats as a dictionary."""
        return {
            "name": self.name,
            "count": self._count,
            "current_samples": len(self._samples),
            "p50_us": self.p50,
            "p95_us": self.p95,
            "p99_us": self.p99,
            "mean_us": self.mean,
            "min_us": self.min_latency,
            "max_us": self.max_latency,
        }


class MetricsCollector:
    """Central metrics collection for the HFT platform.

    Collects latency histograms for all critical paths and provides
    periodic logging of statistics.

    Usage:
        from hft.core.metrics import metrics

        # Record a latency sample
        metrics.parse_json_latency.record(elapsed_us)

        # Periodically call to log stats (usually in a tick handler)
        metrics.maybe_log_stats()
    """

    __slots__ = (
        "ws_network_latency",
        "parse_json_latency",
        "parse_protobuf_latency",
        "normalize_latency",
        "agg_update_latency",
        "api_ws_push_latency",
        "db_write_latency",
        "orderbook_update_latency",
        "_last_log_time",
        "_log_interval",
        "_enabled",
    )

    def __init__(self, log_interval_sec: float = 60.0, enabled: bool = True):
        """Initialize metrics collector.

        Args:
            log_interval_sec: How often to log summary statistics
            enabled: Whether to actually collect metrics (disable for benchmarks)
        """
        self._enabled = enabled
        self._log_interval = log_interval_sec
        self._last_log_time = time.time()

        # Create histograms for each metric
        self.ws_network_latency = LatencyHistogram("ws.network")
        self.parse_json_latency = LatencyHistogram("parse.json")
        self.parse_protobuf_latency = LatencyHistogram("parse.protobuf")
        self.normalize_latency = LatencyHistogram("normalize")
        self.agg_update_latency = LatencyHistogram("agg.update")
        self.api_ws_push_latency = LatencyHistogram("api.ws_push")
        self.db_write_latency = LatencyHistogram("db.write")
        self.orderbook_update_latency = LatencyHistogram("orderbook.update")

    @property
    def enabled(self) -> bool:
        """Whether metrics collection is enabled."""
        return self._enabled

    def enable(self) -> None:
        """Enable metrics collection."""
        self._enabled = True

    def disable(self) -> None:
        """Disable metrics collection."""
        self._enabled = False

    def maybe_log_stats(self) -> None:
        """Log statistics if the log interval has passed.

        Call this periodically (e.g., in a tick handler) to emit
        latency statistics at regular intervals.
        """
        if not self._enabled:
            return

        now = time.time()
        if now - self._last_log_time < self._log_interval:
            return

        self._last_log_time = now
        self._log_all_stats()

    def force_log_stats(self) -> None:
        """Force logging of statistics immediately."""
        self._log_all_stats()

    def _log_all_stats(self) -> None:
        """Log all histogram statistics."""
        histograms = [
            self.ws_network_latency,
            self.parse_json_latency,
            self.parse_protobuf_latency,
            self.normalize_latency,
            self.agg_update_latency,
            self.api_ws_push_latency,
            self.db_write_latency,
            self.orderbook_update_latency,
        ]

        for hist in histograms:
            if hist.count > 0:
                logger.info(
                    "latency_stats",
                    metric=hist.name,
                    count=hist.count,
                    samples=hist.current_samples,
                    p50_us=f"{hist.p50:.1f}",
                    p95_us=f"{hist.p95:.1f}",
                    p99_us=f"{hist.p99:.1f}",
                    mean_us=f"{hist.mean:.1f}",
                    min_us=f"{hist.min_latency:.1f}",
                    max_us=f"{hist.max_latency:.1f}",
                )

    def reset_all(self) -> None:
        """Reset all histograms."""
        self.ws_network_latency.reset()
        self.parse_json_latency.reset()
        self.parse_protobuf_latency.reset()
        self.normalize_latency.reset()
        self.agg_update_latency.reset()
        self.api_ws_push_latency.reset()
        self.db_write_latency.reset()
        self.orderbook_update_latency.reset()

    def get_all_stats(self) -> dict:
        """Get all histogram stats as a dictionary."""
        return {
            "ws_network": self.ws_network_latency.to_dict(),
            "parse_json": self.parse_json_latency.to_dict(),
            "parse_protobuf": self.parse_protobuf_latency.to_dict(),
            "normalize": self.normalize_latency.to_dict(),
            "agg_update": self.agg_update_latency.to_dict(),
            "api_ws_push": self.api_ws_push_latency.to_dict(),
            "db_write": self.db_write_latency.to_dict(),
            "orderbook_update": self.orderbook_update_latency.to_dict(),
        }


# Global metrics instance - import this in other modules
metrics = MetricsCollector()
