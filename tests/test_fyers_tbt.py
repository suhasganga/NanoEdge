"""Tests for Fyers TBT (Tick-by-Tick) 50-depth connector."""

import time

import pytest

from nanoedge.connectors.fyers.tbt_feed import SymbolDepthState
from nanoedge.connectors.fyers.types import (
    MAX_TBT_DEPTH_LEVELS,
    TBT_DEPTH50_DTYPE,
    TBT_LEVEL_DTYPE,
    TBTDepth50,
    TBTDepthLevel,
    TBTQuote,
)


class TestTBTDepthLevel:
    """Tests for TBTDepthLevel type."""

    def test_create_level(self):
        """Test creating a depth level."""
        level = TBTDepthLevel(price=2350050, qty=100, orders=5, level=0)

        assert level.price == 2350050  # paise
        assert level.qty == 100
        assert level.orders == 5
        assert level.level == 0

    def test_price_conversion(self):
        """Test price conversion from paise to INR."""
        level = TBTDepthLevel(price=2350050, qty=100, orders=5, level=0)

        # Convert paise to INR
        price_inr = level.price / 100.0
        assert price_inr == 23500.50

    def test_frozen_struct(self):
        """Test that TBTDepthLevel is immutable."""
        level = TBTDepthLevel(price=2350050, qty=100, orders=5, level=0)

        with pytest.raises(AttributeError):
            level.price = 2350100


class TestSymbolDepthState:
    """Tests for SymbolDepthState incremental updates."""

    @pytest.fixture
    def empty_state(self) -> SymbolDepthState:
        """Create empty depth state."""
        return SymbolDepthState(symbol="NSE:NIFTY25MARFUT")

    @pytest.fixture
    def sample_bid_levels(self) -> list[TBTDepthLevel]:
        """Generate sample bid levels (descending prices)."""
        return [
            TBTDepthLevel(price=2350050, qty=100, orders=5, level=0),
            TBTDepthLevel(price=2350000, qty=200, orders=10, level=1),
            TBTDepthLevel(price=2349950, qty=150, orders=8, level=2),
        ]

    @pytest.fixture
    def sample_ask_levels(self) -> list[TBTDepthLevel]:
        """Generate sample ask levels (ascending prices)."""
        return [
            TBTDepthLevel(price=2350100, qty=80, orders=4, level=0),
            TBTDepthLevel(price=2350150, qty=120, orders=6, level=1),
            TBTDepthLevel(price=2350200, qty=90, orders=5, level=2),
        ]

    def test_apply_snapshot(
        self,
        empty_state: SymbolDepthState,
        sample_bid_levels: list[TBTDepthLevel],
        sample_ask_levels: list[TBTDepthLevel],
    ):
        """Test applying a full snapshot."""
        ts = int(time.time_ns())

        empty_state.apply_snapshot(
            feed_time_ns=ts,
            sequence=1,
            token="101011250127",
            tbq=5000,
            tsq=4000,
            bid_levels=sample_bid_levels,
            ask_levels=sample_ask_levels,
        )

        assert empty_state.timestamp_ns == ts
        assert empty_state.sequence_no == 1
        assert empty_state.token == "101011250127"
        assert empty_state.total_buy_qty == 5000
        assert empty_state.total_sell_qty == 4000
        assert len(empty_state.bids) == 3
        assert len(empty_state.asks) == 3

        # Verify levels are indexed correctly
        assert empty_state.bids[0].price == 2350050
        assert empty_state.bids[1].price == 2350000
        assert empty_state.asks[0].price == 2350100

    def test_apply_diff_update_level(
        self,
        empty_state: SymbolDepthState,
        sample_bid_levels: list[TBTDepthLevel],
        sample_ask_levels: list[TBTDepthLevel],
    ):
        """Test applying diff that updates existing levels."""
        ts = int(time.time_ns())

        # Apply initial snapshot
        empty_state.apply_snapshot(
            feed_time_ns=ts,
            sequence=1,
            token="101011250127",
            tbq=5000,
            tsq=4000,
            bid_levels=sample_bid_levels,
            ask_levels=sample_ask_levels,
        )

        # Apply diff that updates level 0 bid
        updated_bid = TBTDepthLevel(price=2350060, qty=150, orders=7, level=0)

        empty_state.apply_diff(
            feed_time_ns=ts + 1000000,
            sequence=2,
            tbq=5100,
            tsq=None,  # No update
            bid_levels=[updated_bid],
            ask_levels=[],
        )

        assert empty_state.sequence_no == 2
        assert empty_state.total_buy_qty == 5100
        assert empty_state.total_sell_qty == 4000  # Unchanged
        assert empty_state.bids[0].price == 2350060
        assert empty_state.bids[0].qty == 150

    def test_apply_diff_remove_level(
        self,
        empty_state: SymbolDepthState,
        sample_bid_levels: list[TBTDepthLevel],
        sample_ask_levels: list[TBTDepthLevel],
    ):
        """Test applying diff that removes a level (qty=0)."""
        ts = int(time.time_ns())

        # Apply initial snapshot
        empty_state.apply_snapshot(
            feed_time_ns=ts,
            sequence=1,
            token="101011250127",
            tbq=5000,
            tsq=4000,
            bid_levels=sample_bid_levels,
            ask_levels=sample_ask_levels,
        )

        # Apply diff that removes level 1 bid (qty=0)
        removed_level = TBTDepthLevel(price=0, qty=0, orders=0, level=1)

        empty_state.apply_diff(
            feed_time_ns=ts + 1000000,
            sequence=2,
            tbq=None,
            tsq=None,
            bid_levels=[removed_level],
            ask_levels=[],
        )

        assert len(empty_state.bids) == 2
        assert 1 not in empty_state.bids

    def test_apply_diff_out_of_order_skipped(
        self,
        empty_state: SymbolDepthState,
        sample_bid_levels: list[TBTDepthLevel],
        sample_ask_levels: list[TBTDepthLevel],
    ):
        """Test that out-of-order diffs are skipped."""
        ts = int(time.time_ns())

        # Apply initial snapshot with sequence 5
        empty_state.apply_snapshot(
            feed_time_ns=ts,
            sequence=5,
            token="101011250127",
            tbq=5000,
            tsq=4000,
            bid_levels=sample_bid_levels,
            ask_levels=sample_ask_levels,
        )

        # Apply diff with older sequence (should be skipped)
        old_bid = TBTDepthLevel(price=2350060, qty=150, orders=7, level=0)

        empty_state.apply_diff(
            feed_time_ns=ts + 1000000,
            sequence=3,  # Older than 5
            tbq=9999,
            tsq=None,
            bid_levels=[old_bid],
            ask_levels=[],
        )

        # State should be unchanged
        assert empty_state.sequence_no == 5
        assert empty_state.total_buy_qty == 5000
        assert empty_state.bids[0].price == 2350050

    def test_to_depth50(
        self,
        empty_state: SymbolDepthState,
        sample_bid_levels: list[TBTDepthLevel],
        sample_ask_levels: list[TBTDepthLevel],
    ):
        """Test converting state to TBTDepth50."""
        ts = int(time.time_ns())

        empty_state.apply_snapshot(
            feed_time_ns=ts,
            sequence=1,
            token="101011250127",
            tbq=5000,
            tsq=4000,
            bid_levels=sample_bid_levels,
            ask_levels=sample_ask_levels,
        )

        depth50 = empty_state.to_depth50(is_snapshot=True)

        assert isinstance(depth50, TBTDepth50)
        assert depth50.symbol == "NSE:NIFTY25MARFUT"
        assert depth50.token == "101011250127"
        assert depth50.is_snapshot is True
        assert depth50.total_buy_qty == 5000
        assert len(depth50.bids) == 3
        assert len(depth50.asks) == 3

    def test_to_order_book_snapshot(
        self,
        empty_state: SymbolDepthState,
        sample_bid_levels: list[TBTDepthLevel],
        sample_ask_levels: list[TBTDepthLevel],
    ):
        """Test converting state to OrderBookSnapshot."""
        ts = int(time.time_ns())

        empty_state.apply_snapshot(
            feed_time_ns=ts,
            sequence=1,
            token="101011250127",
            tbq=5000,
            tsq=4000,
            bid_levels=sample_bid_levels,
            ask_levels=sample_ask_levels,
        )

        order_book = empty_state.to_order_book_snapshot()

        assert order_book.exchange == "fyers"
        assert order_book.symbol == "NSE:NIFTY25MARFUT"
        assert order_book.market == "futures"  # Inferred from symbol
        assert len(order_book.bids) == 3
        assert len(order_book.asks) == 3

        # Prices should be converted from paise to INR
        assert order_book.bids[0].price == 23500.50  # 2350050 / 100
        assert order_book.asks[0].price == 23501.00  # 2350100 / 100

        # Bids sorted descending by price
        assert order_book.bids[0].price > order_book.bids[1].price
        # Asks sorted ascending by price
        assert order_book.asks[0].price < order_book.asks[1].price


class TestTBTQuote:
    """Tests for TBTQuote type."""

    def test_create_quote(self):
        """Test creating a quote."""
        quote = TBTQuote(
            ltp=2350050,
            ltt=1706054400,  # Unix timestamp
            ltq=100,
            volume=1000000,
            volume_diff=500,
            oi=50000,
            ltp_change=500,
        )

        assert quote.ltp == 2350050
        assert quote.ltq == 100

        # Price in INR
        ltp_inr = quote.ltp / 100.0
        assert ltp_inr == 23500.50


class TestTBTDtypes:
    """Tests for numpy dtypes."""

    def test_level_dtype_size(self):
        """Test TBT_LEVEL_DTYPE structure."""
        assert TBT_LEVEL_DTYPE.itemsize == 16  # i8 + u4 + u4

    def test_depth50_dtype_size(self):
        """Test TBT_DEPTH50_DTYPE structure."""
        # Should be able to hold 50 levels on each side
        assert "bid_prices" in TBT_DEPTH50_DTYPE.names
        assert "ask_prices" in TBT_DEPTH50_DTYPE.names
        assert TBT_DEPTH50_DTYPE["bid_prices"].shape == (50,)
        assert TBT_DEPTH50_DTYPE["ask_prices"].shape == (50,)


class TestMarketInference:
    """Tests for market type inference from symbol."""

    def test_futures_symbol(self):
        """Test futures market inference."""
        state = SymbolDepthState(symbol="NSE:NIFTY25MARFUT")
        order_book = state.to_order_book_snapshot()
        assert order_book.market == "futures"

    def test_options_ce_symbol(self):
        """Test options CE market inference."""
        state = SymbolDepthState(symbol="NSE:NIFTY2530124500CE")
        order_book = state.to_order_book_snapshot()
        assert order_book.market == "options"

    def test_options_pe_symbol(self):
        """Test options PE market inference."""
        state = SymbolDepthState(symbol="NSE:NIFTY2530124000PE")
        order_book = state.to_order_book_snapshot()
        assert order_book.market == "options"

    def test_equity_symbol(self):
        """Test equity market inference."""
        state = SymbolDepthState(symbol="NSE:RELIANCE-EQ")
        order_book = state.to_order_book_snapshot()
        assert order_book.market == "equity"

    def test_index_symbol(self):
        """Test index market inference."""
        state = SymbolDepthState(symbol="NSE:NIFTY50-INDEX")
        order_book = state.to_order_book_snapshot()
        assert order_book.market == "index"


class TestConstants:
    """Tests for TBT constants."""

    def test_max_depth_levels(self):
        """Test max depth levels constant."""
        assert MAX_TBT_DEPTH_LEVELS == 50


class TestTBTConnectionPool:
    """Tests for FyersTBTConnectionPool."""

    @pytest.fixture
    def pool(self):
        """Create a connection pool for testing."""
        from nanoedge.connectors.fyers.tbt_pool import FyersTBTConnectionPool

        return FyersTBTConnectionPool(
            app_id="TEST-100",
            access_token="test_token",
        )

    @pytest.mark.asyncio
    async def test_add_single_symbol(self, pool):
        """Test adding a single symbol."""
        result = await pool.add_symbol("NSE:NIFTY25MARFUT")

        assert result is True
        assert pool.total_symbols == 1
        assert pool.connection_count == 1
        assert "NSE:NIFTY25MARFUT" in pool.get_all_symbols()

    @pytest.mark.asyncio
    async def test_add_multiple_symbols_same_connection(self, pool):
        """Test adding multiple symbols to same connection."""
        symbols = [
            "NSE:NIFTY25MARFUT",
            "NSE:BANKNIFTY25MARFUT",
            "NSE:FINNIFTY25MARFUT",
        ]
        added = await pool.add_symbols(symbols)

        assert len(added) == 3
        assert pool.total_symbols == 3
        assert pool.connection_count == 1  # All fit in one connection

    @pytest.mark.asyncio
    async def test_add_symbols_creates_new_connection(self, pool):
        """Test that adding >5 symbols creates a new connection."""
        symbols = [
            "NSE:SYM1",
            "NSE:SYM2",
            "NSE:SYM3",
            "NSE:SYM4",
            "NSE:SYM5",
            "NSE:SYM6",  # Should trigger new connection
        ]
        added = await pool.add_symbols(symbols)

        assert len(added) == 6
        assert pool.total_symbols == 6
        assert pool.connection_count == 2  # 5 + 1 = 2 connections

    @pytest.mark.asyncio
    async def test_max_connections_limit(self, pool):
        """Test that pool respects max 3 connections (15 symbols)."""
        # Add 15 symbols (max capacity)
        symbols = [f"NSE:SYM{i}" for i in range(15)]
        added = await pool.add_symbols(symbols)

        assert len(added) == 15
        assert pool.connection_count == 3

        # Try to add 16th symbol - should fail
        result = await pool.add_symbol("NSE:SYM16")

        assert result is False
        assert pool.total_symbols == 15

    @pytest.mark.asyncio
    async def test_remove_symbol(self, pool):
        """Test removing a symbol."""
        await pool.add_symbol("NSE:NIFTY25MARFUT")
        await pool.add_symbol("NSE:BANKNIFTY25MARFUT")

        result = await pool.remove_symbol("NSE:NIFTY25MARFUT")

        assert result is True
        assert pool.total_symbols == 1
        assert "NSE:NIFTY25MARFUT" not in pool.get_all_symbols()

    @pytest.mark.asyncio
    async def test_remove_symbol_destroys_empty_connection(self, pool):
        """Test that removing last symbol from connection destroys it."""
        await pool.add_symbol("NSE:NIFTY25MARFUT")
        assert pool.connection_count == 1

        await pool.remove_symbol("NSE:NIFTY25MARFUT")

        assert pool.connection_count == 0
        assert pool.total_symbols == 0

    @pytest.mark.asyncio
    async def test_duplicate_symbol_ignored(self, pool):
        """Test that adding same symbol twice returns True but doesn't duplicate."""
        await pool.add_symbol("NSE:NIFTY25MARFUT")
        result = await pool.add_symbol("NSE:NIFTY25MARFUT")

        assert result is True
        assert pool.total_symbols == 1

    @pytest.mark.asyncio
    async def test_available_slots(self, pool):
        """Test available slots calculation."""
        assert pool.available_slots == 15  # 3 connections * 5 symbols

        await pool.add_symbols(["NSE:SYM1", "NSE:SYM2", "NSE:SYM3"])

        assert pool.available_slots == 12

    @pytest.mark.asyncio
    async def test_get_connection_stats(self, pool):
        """Test getting connection statistics."""
        await pool.add_symbols(["NSE:SYM1", "NSE:SYM2"])

        stats = pool.get_connection_stats()

        assert len(stats) == 1
        assert stats[0]["symbol_count"] == 2
        assert stats[0]["is_full"] is False
        assert set(stats[0]["symbols"]) == {"NSE:SYM1", "NSE:SYM2"}
