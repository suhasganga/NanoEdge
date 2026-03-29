"""Tests for ring buffer."""

import pytest

from nanoedge.core.ring_buffer import TickRingBuffer
from nanoedge.core.types import MarketTick


class TestTickRingBuffer:
    """Test cases for TickRingBuffer."""

    def test_append_and_length(self):
        """Appending ticks should update length."""
        buffer = TickRingBuffer(capacity=100)

        assert len(buffer) == 0

        for i in range(10):
            buffer.append(
                MarketTick(
                    timestamp_ns=i * 1_000_000_000,
                    exchange="binance",
                    market="spot",
                    symbol="BTCUSDT",
                    price=50000.0 + i,
                    volume=1.0,
                    side=1,
                )
            )

        assert len(buffer) == 10

    def test_get_recent(self):
        """get_recent should return most recent ticks."""
        buffer = TickRingBuffer(capacity=100)

        for i in range(20):
            buffer.append(
                MarketTick(
                    timestamp_ns=i * 1_000_000_000,
                    exchange="binance",
                    market="spot",
                    symbol="BTCUSDT",
                    price=50000.0 + i,
                    volume=1.0,
                    side=1,
                )
            )

        recent = buffer.get_recent(5)

        assert len(recent) == 5
        # Most recent should be last (price 50019)
        assert recent[-1]["price"] == 50019.0
        assert recent[0]["price"] == 50015.0

    def test_capacity_wraparound(self):
        """Buffer should wrap around when capacity is reached."""
        buffer = TickRingBuffer(capacity=10)

        for i in range(25):
            buffer.append(
                MarketTick(
                    timestamp_ns=i * 1_000_000_000,
                    exchange="binance",
                    market="spot",
                    symbol="BTCUSDT",
                    price=float(i),
                    volume=1.0,
                    side=1,
                )
            )

        assert len(buffer) == 10
        assert buffer.is_full

        recent = buffer.get_recent(10)
        # Should have ticks 15-24
        assert recent[0]["price"] == 15.0
        assert recent[-1]["price"] == 24.0

    def test_filter_by_symbol(self):
        """get_recent should filter by symbol."""
        buffer = TickRingBuffer(capacity=100)

        for i in range(10):
            symbol = "BTCUSDT" if i % 2 == 0 else "ETHUSDT"
            buffer.append(
                MarketTick(
                    timestamp_ns=i * 1_000_000_000,
                    exchange="binance",
                    market="spot",
                    symbol=symbol,
                    price=50000.0 + i,
                    volume=1.0,
                    side=1,
                )
            )

        btc_ticks = buffer.get_recent(100, symbol="BTCUSDT")
        eth_ticks = buffer.get_recent(100, symbol="ETHUSDT")

        assert len(btc_ticks) == 5
        assert len(eth_ticks) == 5

    def test_symbol_mapping(self):
        """Symbol indices should be correctly mapped."""
        buffer = TickRingBuffer(capacity=100)

        buffer.append(
            MarketTick(
                timestamp_ns=0,
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                price=50000.0,
                volume=1.0,
                side=1,
            )
        )
        buffer.append(
            MarketTick(
                timestamp_ns=1,
                exchange="binance",
                market="spot",
                symbol="ETHUSDT",
                price=3000.0,
                volume=1.0,
                side=1,
            )
        )

        assert buffer.get_symbol(0) == "BTCUSDT"
        assert buffer.get_symbol(1) == "ETHUSDT"
        assert buffer.get_symbol(2) is None

    def test_clear(self):
        """Clear should reset count but preserve symbol mappings."""
        buffer = TickRingBuffer(capacity=100)

        buffer.append(
            MarketTick(
                timestamp_ns=0,
                exchange="binance",
                market="spot",
                symbol="BTCUSDT",
                price=50000.0,
                volume=1.0,
                side=1,
            )
        )

        assert len(buffer) == 1

        buffer.clear()

        assert len(buffer) == 0
        # Symbol mapping should still exist
        assert buffer.get_symbol(0) == "BTCUSDT"
