"""Tests for core data types."""

import numpy as np
import pytest

from nanoedge.core.types import (
    DepthLevel,
    InstrumentType,
    MarketStats,
    MarketTick,
    OHLCV,
    OHLCV_DTYPE,
    OrderBookSnapshot,
    SymbolInfo,
    TICK_DTYPE,
    Trade,
)


class TestMarketTick:
    """Tests for MarketTick dataclass."""

    def test_creation_with_all_fields(self):
        """Create MarketTick with all fields."""
        tick = MarketTick(
            timestamp_ns=1704067200000000000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            volume=0.1,
            side=1,
        )
        assert tick.timestamp_ns == 1704067200000000000
        assert tick.exchange == "binance"
        assert tick.market == "spot"
        assert tick.symbol == "BTCUSDT"
        assert tick.price == 50000.0
        assert tick.volume == 0.1
        assert tick.side == 1

    def test_side_buy(self):
        """Side 1 represents buy."""
        tick = MarketTick(
            timestamp_ns=1704067200000000000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            volume=0.1,
            side=1,
        )
        assert tick.side == 1  # buy

    def test_side_sell(self):
        """Side -1 represents sell."""
        tick = MarketTick(
            timestamp_ns=1704067200000000000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            volume=0.1,
            side=-1,
        )
        assert tick.side == -1  # sell

    def test_side_unknown(self):
        """Side 0 represents unknown."""
        tick = MarketTick(
            timestamp_ns=1704067200000000000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            volume=0.1,
            side=0,
        )
        assert tick.side == 0  # unknown

    def test_has_slots(self):
        """MarketTick uses __slots__ for memory efficiency."""
        tick = MarketTick(
            timestamp_ns=1704067200000000000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            volume=0.1,
            side=1,
        )
        assert hasattr(tick, "__slots__")


class TestOHLCV:
    """Tests for OHLCV dataclass."""

    def test_creation_with_required_fields(self):
        """Create OHLCV with required fields."""
        candle = OHLCV(
            timestamp=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )
        assert candle.timestamp == 1704067200000
        assert candle.open == 50000.0
        assert candle.high == 50100.0
        assert candle.low == 49900.0
        assert candle.close == 50050.0
        assert candle.volume == 100.0

    def test_default_values(self):
        """OHLCV has correct default values."""
        candle = OHLCV(
            timestamp=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )
        assert candle.quote_volume == 0.0
        assert candle.trade_count == 0
        assert candle.vwap == 0.0
        assert candle.is_closed is False

    def test_is_closed_flag(self):
        """is_closed flag can be set."""
        candle = OHLCV(
            timestamp=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
            is_closed=True,
        )
        assert candle.is_closed is True

    def test_has_slots(self):
        """OHLCV uses __slots__."""
        candle = OHLCV(
            timestamp=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            open=50000.0,
            high=50100.0,
            low=49900.0,
            close=50050.0,
            volume=100.0,
        )
        assert hasattr(candle, "__slots__")


class TestDepthLevel:
    """Tests for DepthLevel dataclass."""

    def test_creation(self):
        """Create DepthLevel."""
        level = DepthLevel(price=50000.0, size=1.5)
        assert level.price == 50000.0
        assert level.size == 1.5

    def test_has_slots(self):
        """DepthLevel uses __slots__."""
        level = DepthLevel(price=50000.0, size=1.5)
        assert hasattr(level, "__slots__")


class TestOrderBookSnapshot:
    """Tests for OrderBookSnapshot dataclass."""

    def test_creation(self):
        """Create OrderBookSnapshot."""
        bids = [DepthLevel(50000.0, 1.0), DepthLevel(49999.0, 2.0)]
        asks = [DepthLevel(50001.0, 1.5), DepthLevel(50002.0, 0.5)]

        snapshot = OrderBookSnapshot(
            timestamp_ms=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            bids=bids,
            asks=asks,
            last_update_id=12345,
        )

        assert snapshot.timestamp_ms == 1704067200000
        assert len(snapshot.bids) == 2
        assert len(snapshot.asks) == 2
        assert snapshot.bids[0].price == 50000.0
        assert snapshot.asks[0].price == 50001.0
        assert snapshot.last_update_id == 12345

    def test_bids_asks_are_lists(self):
        """Bids and asks are list types."""
        snapshot = OrderBookSnapshot(
            timestamp_ms=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            bids=[],
            asks=[],
            last_update_id=0,
        )
        assert isinstance(snapshot.bids, list)
        assert isinstance(snapshot.asks, list)


class TestTrade:
    """Tests for Trade dataclass."""

    def test_creation(self):
        """Create Trade."""
        trade = Trade(
            timestamp_ms=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            quantity=0.1,
            is_buyer_maker=False,
            trade_id=123456789,
        )
        assert trade.timestamp_ms == 1704067200000
        assert trade.price == 50000.0
        assert trade.quantity == 0.1
        assert trade.is_buyer_maker is False
        assert trade.trade_id == 123456789

    def test_is_buyer_maker_buy(self):
        """is_buyer_maker False = buy (green in UI)."""
        trade = Trade(
            timestamp_ms=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            quantity=0.1,
            is_buyer_maker=False,
            trade_id=1,
        )
        # False = taker was buyer = green (buy)
        assert trade.is_buyer_maker is False

    def test_is_buyer_maker_sell(self):
        """is_buyer_maker True = sell (red in UI)."""
        trade = Trade(
            timestamp_ms=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price=50000.0,
            quantity=0.1,
            is_buyer_maker=True,
            trade_id=1,
        )
        # True = taker was seller = red (sell)
        assert trade.is_buyer_maker is True


class TestMarketStats:
    """Tests for MarketStats dataclass."""

    def test_creation(self):
        """Create MarketStats."""
        stats = MarketStats(
            timestamp_ms=1704067200000,
            exchange="binance",
            market="spot",
            symbol="BTCUSDT",
            price_change=100.5,
            price_change_percent=0.2,
            high_24h=50500.0,
            low_24h=49500.0,
            volume_24h=50000.0,
            quote_volume_24h=2500000000.0,
            trade_count_24h=1000000,
            last_price=50100.0,
            open_price=50000.0,
        )
        assert stats.price_change == 100.5
        assert stats.price_change_percent == 0.2
        assert stats.high_24h == 50500.0
        assert stats.low_24h == 49500.0
        assert stats.volume_24h == 50000.0
        assert stats.last_price == 50100.0


class TestSymbolInfo:
    """Tests for SymbolInfo dataclass."""

    def test_basic_creation(self):
        """Create SymbolInfo with required fields."""
        info = SymbolInfo(
            symbol="BTCUSDT",
            exchange="binance",
            market="spot",
            base_asset="BTC",
            quote_asset="USDT",
            description="Bitcoin / TetherUS",
            instrument_type="spot",
        )
        assert info.symbol == "BTCUSDT"
        assert info.base_asset == "BTC"
        assert info.quote_asset == "USDT"

    def test_derivative_fields(self):
        """SymbolInfo supports derivative fields."""
        info = SymbolInfo(
            symbol="BTCUSDT_250328",
            exchange="binance",
            market="futures",
            base_asset="BTC",
            quote_asset="USDT",
            description="Bitcoin Quarterly",
            instrument_type="future_linear",
            contract_type="quarterly",
            expiry_date="2025-03-28",
            underlying="BTCUSDT",
        )
        assert info.contract_type == "quarterly"
        assert info.expiry_date == "2025-03-28"
        assert info.underlying == "BTCUSDT"

    def test_option_fields(self):
        """SymbolInfo supports option fields."""
        info = SymbolInfo(
            symbol="BTC-250328-50000-C",
            exchange="binance",
            market="options",
            base_asset="BTC",
            quote_asset="USDT",
            description="BTC Call Option",
            instrument_type="option_call",
            strike_price=50000.0,
            option_type="call",
            expiry_date="2025-03-28",
        )
        assert info.strike_price == 50000.0
        assert info.option_type == "call"

    def test_default_trading_params(self):
        """Default trading parameters."""
        info = SymbolInfo(
            symbol="BTCUSDT",
            exchange="binance",
            market="spot",
            base_asset="BTC",
            quote_asset="USDT",
            description="Test",
            instrument_type="spot",
        )
        assert info.tick_size == 0.01
        assert info.lot_size == 1.0
        assert info.min_notional is None
        assert info.is_trading is True


class TestInstrumentType:
    """Tests for InstrumentType enum."""

    def test_binance_types(self):
        """Binance instrument types."""
        assert InstrumentType.SPOT.value == "spot"
        assert InstrumentType.PERP_LINEAR.value == "perp_linear"
        assert InstrumentType.PERP_INVERSE.value == "perp_inverse"
        assert InstrumentType.OPTION_CALL.value == "option_call"

    def test_fyers_types(self):
        """Fyers/NSE instrument types."""
        assert InstrumentType.EQUITY.value == "equity"
        assert InstrumentType.INDEX.value == "index"
        assert InstrumentType.INDEX_FUTURE.value == "index_future"
        assert InstrumentType.INDEX_OPTION_CE.value == "index_option_ce"

    def test_is_string_enum(self):
        """InstrumentType is a string enum."""
        assert isinstance(InstrumentType.SPOT, str)
        assert InstrumentType.SPOT == "spot"


class TestTickDtype:
    """Tests for TICK_DTYPE numpy dtype."""

    def test_dtype_fields(self):
        """TICK_DTYPE has correct fields."""
        names = TICK_DTYPE.names
        assert "timestamp_ns" in names
        assert "symbol_idx" in names
        assert "price" in names
        assert "volume" in names
        assert "side" in names

    def test_dtype_size(self):
        """TICK_DTYPE has expected size."""
        # u8 + u2 + f8 + f8 + i1 = 8 + 2 + 8 + 8 + 1 = 27 bytes (with padding ~32)
        assert TICK_DTYPE.itemsize > 0

    def test_can_create_array(self):
        """Can create numpy array with TICK_DTYPE."""
        arr = np.zeros(10, dtype=TICK_DTYPE)
        assert arr.shape == (10,)
        arr[0]["timestamp_ns"] = 1704067200000000000
        arr[0]["price"] = 50000.0
        arr[0]["side"] = 1
        assert arr[0]["price"] == 50000.0


class TestOHLCVDtype:
    """Tests for OHLCV_DTYPE numpy dtype."""

    def test_dtype_fields(self):
        """OHLCV_DTYPE has correct fields."""
        names = OHLCV_DTYPE.names
        assert "timestamp" in names
        assert "exchange_idx" in names
        assert "market_idx" in names
        assert "symbol_idx" in names
        assert "open" in names
        assert "high" in names
        assert "low" in names
        assert "close" in names
        assert "volume" in names
        assert "vwap" in names

    def test_can_create_array(self):
        """Can create numpy array with OHLCV_DTYPE."""
        arr = np.zeros(10, dtype=OHLCV_DTYPE)
        assert arr.shape == (10,)
        arr[0]["open"] = 50000.0
        arr[0]["high"] = 50100.0
        arr[0]["low"] = 49900.0
        arr[0]["close"] = 50050.0
        assert arr[0]["close"] == 50050.0
