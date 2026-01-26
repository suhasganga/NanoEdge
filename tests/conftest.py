"""pytest configuration and fixtures."""

import time

import pytest

from hft.core.types import MarketTick, OHLCV


@pytest.fixture
def sample_ticks() -> list[MarketTick]:
    """Generate sample tick sequence for testing."""
    base_time = int(time.time() * 1e9)  # nanoseconds
    ticks = []

    for i in range(100):
        tick = MarketTick(
            timestamp_ns=base_time + i * 100_000_000,  # 100ms apart
            symbol="BTCUSDT",
            price=50000.0 + (i % 10) * 10,  # Price oscillates 50000-50090
            volume=0.1 + (i % 5) * 0.01,
            side=1 if i % 2 == 0 else -1,
        )
        ticks.append(tick)

    return ticks


@pytest.fixture
def sample_ohlcv() -> OHLCV:
    """Generate sample OHLCV candle."""
    return OHLCV(
        timestamp=1704067200000,  # 2024-01-01 00:00:00 UTC
        symbol="BTCUSDT",
        open=50000.0,
        high=50100.0,
        low=49900.0,
        close=50050.0,
        volume=100.5,
        trade_count=1234,
        vwap=50025.0,
        is_closed=True,
    )
