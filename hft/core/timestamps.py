"""Timestamp chain for end-to-end latency tracking.

Tracks nanosecond timestamps at each stage of the data pipeline:
- Exchange event time (T0)
- WebSocket receive time (T1)
- Parse complete time (T2)
- Normalization complete time (T3)
- Aggregator processed time (T4)
- API push initiated time (T5)
"""

import time
from dataclasses import dataclass


@dataclass(slots=True)
class TimestampChain:
    """Nanosecond timestamps at each pipeline stage.

    All timestamps are in nanoseconds since epoch (time.time_ns() format).
    Use the latency properties to get microsecond values for logging.
    """

    exchange_ns: int  # T0: Exchange event time
    recv_ns: int = 0  # T1: WebSocket frame received
    parse_ns: int = 0  # T2: JSON/protobuf decode complete
    norm_ns: int = 0  # T3: Normalized to internal type
    agg_ns: int = 0  # T4: Aggregator processed
    api_ns: int = 0  # T5: API push initiated

    @property
    def network_latency_us(self) -> float:
        """Exchange to receive latency in microseconds."""
        if self.recv_ns == 0:
            return 0.0
        return (self.recv_ns - self.exchange_ns) / 1000

    @property
    def parse_latency_us(self) -> float:
        """Parse latency in microseconds."""
        if self.parse_ns == 0 or self.recv_ns == 0:
            return 0.0
        return (self.parse_ns - self.recv_ns) / 1000

    @property
    def normalize_latency_us(self) -> float:
        """Normalization latency in microseconds."""
        if self.norm_ns == 0 or self.parse_ns == 0:
            return 0.0
        return (self.norm_ns - self.parse_ns) / 1000

    @property
    def agg_latency_us(self) -> float:
        """Aggregator processing latency in microseconds."""
        if self.agg_ns == 0 or self.norm_ns == 0:
            return 0.0
        return (self.agg_ns - self.norm_ns) / 1000

    @property
    def api_latency_us(self) -> float:
        """API push latency in microseconds."""
        if self.api_ns == 0 or self.agg_ns == 0:
            return 0.0
        return (self.api_ns - self.agg_ns) / 1000

    @property
    def total_latency_us(self) -> float:
        """Total end-to-end latency in microseconds (excluding network)."""
        if self.api_ns == 0 or self.recv_ns == 0:
            return 0.0
        return (self.api_ns - self.recv_ns) / 1000

    @property
    def exchange_age_ms(self) -> float:
        """How old this data is from exchange time in milliseconds."""
        return (time.time_ns() - self.exchange_ns) / 1_000_000

    def mark_recv(self) -> None:
        """Mark WebSocket receive time."""
        self.recv_ns = time.time_ns()

    def mark_parse(self) -> None:
        """Mark parse complete time."""
        self.parse_ns = time.time_ns()

    def mark_norm(self) -> None:
        """Mark normalization complete time."""
        self.norm_ns = time.time_ns()

    def mark_agg(self) -> None:
        """Mark aggregator processed time."""
        self.agg_ns = time.time_ns()

    def mark_api(self) -> None:
        """Mark API push initiated time."""
        self.api_ns = time.time_ns()

    def to_dict(self) -> dict:
        """Convert to dict for logging."""
        return {
            "exchange_ns": self.exchange_ns,
            "recv_ns": self.recv_ns,
            "parse_ns": self.parse_ns,
            "norm_ns": self.norm_ns,
            "agg_ns": self.agg_ns,
            "api_ns": self.api_ns,
            "network_latency_us": self.network_latency_us,
            "parse_latency_us": self.parse_latency_us,
            "total_latency_us": self.total_latency_us,
            "exchange_age_ms": self.exchange_age_ms,
        }


def create_timestamp_chain(exchange_time_ms: int) -> TimestampChain:
    """Create a TimestampChain from exchange millisecond timestamp.

    Args:
        exchange_time_ms: Exchange event time in milliseconds since epoch

    Returns:
        TimestampChain with exchange_ns set and recv_ns marked
    """
    chain = TimestampChain(exchange_ns=exchange_time_ms * 1_000_000)
    chain.mark_recv()
    return chain
