"""NumPy-based ring buffer for tick storage."""

import numpy as np

from nanoedge.core.types import TICK_DTYPE, MarketTick


class TickRingBuffer:
    """
    Fixed-size circular buffer for tick data using NumPy.

    Provides O(1) append operations and efficient batch retrieval.
    When capacity is reached, oldest ticks are overwritten.
    """

    __slots__ = (
        "capacity",
        "_buffer",
        "_head",
        "_count",
        "_symbol_to_idx",
        "_idx_to_symbol",
    )

    def __init__(self, capacity: int = 1_000_000):
        """
        Initialize ring buffer with given capacity.

        Args:
            capacity: Maximum number of ticks to store
        """
        self.capacity = capacity
        self._buffer = np.zeros(capacity, dtype=TICK_DTYPE)
        self._head = 0  # Next write position
        self._count = 0  # Current number of items
        self._symbol_to_idx: dict[str, int] = {}
        self._idx_to_symbol: dict[int, str] = {}

    def _get_symbol_idx(self, symbol: str) -> int:
        """Get or create symbol index for compact storage."""
        if symbol not in self._symbol_to_idx:
            idx = len(self._symbol_to_idx)
            self._symbol_to_idx[symbol] = idx
            self._idx_to_symbol[idx] = symbol
        return self._symbol_to_idx[symbol]

    def append(self, tick: MarketTick) -> None:
        """
        Add tick to buffer (O(1) operation).

        Args:
            tick: MarketTick to store
        """
        idx = self._head
        self._buffer[idx]["timestamp_ns"] = tick.timestamp_ns
        self._buffer[idx]["symbol_idx"] = self._get_symbol_idx(tick.symbol)
        self._buffer[idx]["price"] = tick.price
        self._buffer[idx]["volume"] = tick.volume
        self._buffer[idx]["side"] = tick.side

        self._head = (self._head + 1) % self.capacity
        self._count = min(self._count + 1, self.capacity)

    def get_recent(self, n: int, symbol: str | None = None) -> np.ndarray:
        """
        Get most recent n ticks, optionally filtered by symbol.

        Args:
            n: Number of ticks to retrieve
            symbol: Optional symbol filter

        Returns:
            NumPy array of tick data (newest last)
        """
        if self._count == 0:
            return np.array([], dtype=TICK_DTYPE)

        # Calculate actual number of items to retrieve
        actual_n = min(n, self._count)

        # Calculate start and end indices
        end = self._head
        start = (end - actual_n) % self.capacity

        # Extract data handling wraparound
        if start < end:
            data = self._buffer[start:end].copy()
        else:
            data = np.concatenate([self._buffer[start:], self._buffer[:end]])

        # Filter by symbol if specified
        if symbol is not None:
            symbol_idx = self._symbol_to_idx.get(symbol)
            if symbol_idx is not None:
                mask = data["symbol_idx"] == symbol_idx
                data = data[mask]
            else:
                return np.array([], dtype=TICK_DTYPE)

        return data

    def get_symbol(self, idx: int) -> str | None:
        """Get symbol name from index."""
        return self._idx_to_symbol.get(idx)

    def __len__(self) -> int:
        """Return current number of items in buffer."""
        return self._count

    @property
    def is_full(self) -> bool:
        """Return True if buffer has reached capacity."""
        return self._count >= self.capacity

    def clear(self) -> None:
        """Clear all data from buffer."""
        self._head = 0
        self._count = 0
        # Note: We don't clear symbol mappings as they're still valid
