"""Tests for BinanceOrderBook."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from hft.connectors.binance.orderbook import BinanceOrderBook
from hft.connectors.binance.types import BinanceDepthUpdate
from hft.core.types import OrderBookSnapshot


class TestBinanceOrderBookInit:
    """Tests for BinanceOrderBook initialization."""

    def test_symbol_uppercased(self):
        """Test symbol is converted to uppercase."""
        on_update = MagicMock()
        rest_client = MagicMock()

        book = BinanceOrderBook(
            symbol="btcusdt",
            on_update=on_update,
            rest_client=rest_client,
        )

        assert book.symbol == "BTCUSDT"

    def test_default_depth_levels(self):
        """Test default depth levels is 50."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        assert book.depth_levels == 50

    def test_custom_depth_levels(self):
        """Test custom depth levels."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
            depth_levels=20,
        )

        assert book.depth_levels == 20

    def test_initial_state(self):
        """Test initial state is empty and not initialized."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        assert len(book._bids) == 0
        assert len(book._asks) == 0
        assert book._last_update_id == 0
        assert book._initialized is False
        assert book._update_count == 0
        assert book._resync_count == 0


class TestResetState:
    """Tests for _reset_state method."""

    def test_clears_all_state(self):
        """Test reset clears bids, asks, and flags."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        # Add some state
        book._bids[-93000.0] = 1.5
        book._asks[93001.0] = 2.0
        book._last_update_id = 12345
        book._initialized = True
        book._first_event_u = 12340

        book._reset_state()

        assert len(book._bids) == 0
        assert len(book._asks) == 0
        assert book._last_update_id == 0
        assert book._initialized is False
        assert book._first_event_u is None


class TestApplyEvent:
    """Tests for _apply_event method."""

    def test_applies_bid_updates(self):
        """Test bid level is added/updated."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True
        book._last_update_id = 100

        event = BinanceDepthUpdate(
            e="depthUpdate",
            E=1672515782136,
            s="BTCUSDT",
            U=101,
            u=101,
            b=[["93000.00", "1.5"]],
            a=[],
        )

        result = book._apply_event(event)

        assert result is True
        # Price is negated for descending sort
        assert book._bids[-93000.0] == 1.5
        assert book._last_update_id == 101

    def test_applies_ask_updates(self):
        """Test ask level is added/updated."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True
        book._last_update_id = 100

        event = BinanceDepthUpdate(
            e="depthUpdate",
            E=1672515782136,
            s="BTCUSDT",
            U=101,
            u=101,
            b=[],
            a=[["93001.00", "2.0"]],
        )

        result = book._apply_event(event)

        assert result is True
        assert book._asks[93001.0] == 2.0

    def test_removes_level_when_qty_zero(self):
        """Test level is removed when quantity is 0."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True
        book._last_update_id = 100

        # Add levels first
        book._bids[-93000.0] = 1.5
        book._asks[93001.0] = 2.0

        # Remove them with qty=0
        event = BinanceDepthUpdate(
            e="depthUpdate",
            E=1672515782136,
            s="BTCUSDT",
            U=101,
            u=101,
            b=[["93000.00", "0"]],
            a=[["93001.00", "0"]],
        )

        result = book._apply_event(event)

        assert result is True
        assert -93000.0 not in book._bids
        assert 93001.0 not in book._asks

    def test_skips_old_events(self):
        """Test events with u <= last_update_id are skipped."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True
        book._last_update_id = 100

        event = BinanceDepthUpdate(
            e="depthUpdate",
            E=1672515782136,
            s="BTCUSDT",
            U=98,
            u=99,  # Old event
            b=[["93000.00", "1.5"]],
            a=[],
        )

        result = book._apply_event(event)

        assert result is False
        assert -93000.0 not in book._bids

    def test_detects_gap(self):
        """Test gap detection triggers resync."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True
        book._last_update_id = 100

        # Event with U > last_update_id + 1 (gap)
        event = BinanceDepthUpdate(
            e="depthUpdate",
            E=1672515782136,
            s="BTCUSDT",
            U=105,  # Gap: expected 101
            u=110,
            b=[["93000.00", "1.5"]],
            a=[],
        )

        with patch.object(BinanceOrderBook, "_schedule_sync"):
            result = book._apply_event(event)

        assert result is False
        assert book._resync_count == 1
        assert book._initialized is False

    def test_increments_update_count(self):
        """Test update count is incremented on success."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True
        book._last_update_id = 100

        event = BinanceDepthUpdate(
            e="depthUpdate",
            E=1672515782136,
            s="BTCUSDT",
            U=101,
            u=101,
            b=[["93000.00", "1.5"]],
            a=[],
        )

        assert book._update_count == 0
        book._apply_event(event)
        assert book._update_count == 1


class TestEmitSnapshot:
    """Tests for _emit_snapshot method."""

    def test_builds_correct_snapshot(self):
        """Test snapshot contains correct bids and asks."""
        on_update = MagicMock()
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=on_update,
            rest_client=MagicMock(),
            depth_levels=10,
        )

        # Add some levels (bids stored with negated keys)
        book._bids[-93000.0] = 1.5
        book._bids[-92999.0] = 2.0
        book._bids[-92998.0] = 3.0

        book._asks[93001.0] = 1.0
        book._asks[93002.0] = 2.0

        book._last_update_id = 12345

        book._emit_snapshot()

        on_update.assert_called_once()
        snapshot = on_update.call_args[0][0]

        assert isinstance(snapshot, OrderBookSnapshot)
        assert snapshot.symbol == "BTCUSDT"
        assert snapshot.exchange == "binance"
        assert snapshot.market == "spot"
        assert snapshot.last_update_id == 12345

        # Check bids are sorted descending by price
        assert len(snapshot.bids) == 3
        assert snapshot.bids[0].price == 93000.0  # Highest
        assert snapshot.bids[1].price == 92999.0
        assert snapshot.bids[2].price == 92998.0

        # Check asks are sorted ascending by price
        assert len(snapshot.asks) == 2
        assert snapshot.asks[0].price == 93001.0  # Lowest
        assert snapshot.asks[1].price == 93002.0

    def test_respects_depth_levels_limit(self):
        """Test snapshot is limited to depth_levels."""
        on_update = MagicMock()
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=on_update,
            rest_client=MagicMock(),
            depth_levels=2,  # Only 2 levels
        )

        # Add more levels than limit
        book._bids[-93000.0] = 1.0
        book._bids[-92999.0] = 2.0
        book._bids[-92998.0] = 3.0

        book._asks[93001.0] = 1.0
        book._asks[93002.0] = 2.0
        book._asks[93003.0] = 3.0

        book._emit_snapshot()

        snapshot = on_update.call_args[0][0]
        assert len(snapshot.bids) == 2
        assert len(snapshot.asks) == 2


class TestProperties:
    """Tests for property methods."""

    def test_is_initialized_false_initially(self):
        """Test is_initialized returns False initially."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        assert book.is_initialized is False

    def test_is_initialized_true_after_sync(self):
        """Test is_initialized returns True after sync."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )
        book._initialized = True

        assert book.is_initialized is True

    def test_best_bid_returns_highest_bid(self):
        """Test best_bid returns highest bid price."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        # Add bids (keys are negated)
        book._bids[-93000.0] = 1.0
        book._bids[-92999.0] = 2.0

        assert book.best_bid == 93000.0

    def test_best_bid_returns_none_when_empty(self):
        """Test best_bid returns None when no bids."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        assert book.best_bid is None

    def test_best_ask_returns_lowest_ask(self):
        """Test best_ask returns lowest ask price."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        book._asks[93001.0] = 1.0
        book._asks[93002.0] = 2.0

        assert book.best_ask == 93001.0

    def test_best_ask_returns_none_when_empty(self):
        """Test best_ask returns None when no asks."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        assert book.best_ask is None

    def test_spread_calculation(self):
        """Test spread is calculated correctly."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        book._bids[-93000.0] = 1.0
        book._asks[93001.0] = 1.0

        assert book.spread == 1.0

    def test_spread_returns_none_when_no_bids(self):
        """Test spread returns None when no bids."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        book._asks[93001.0] = 1.0

        assert book.spread is None

    def test_spread_returns_none_when_no_asks(self):
        """Test spread returns None when no asks."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        book._bids[-93000.0] = 1.0

        assert book.spread is None


class TestStartStop:
    """Tests for start/stop methods."""

    @pytest.mark.asyncio
    async def test_start_delegates_to_ws_client(self):
        """Test start() calls ws_client.start()."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        book._ws_client = AsyncMock()

        await book.start()

        book._ws_client.start.assert_called_once()

    @pytest.mark.asyncio
    async def test_stop_cancels_sync_task(self):
        """Test stop() cancels any running sync task."""
        import asyncio

        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        book._ws_client = AsyncMock()

        # Create a real task that we can cancel
        async def long_running():
            await asyncio.sleep(100)

        book._sync_task = asyncio.create_task(long_running())

        await book.stop()

        # Task should be cancelled
        assert book._sync_task.cancelled() or book._sync_task.done()
        book._ws_client.stop.assert_called_once()


class TestHandleWsMessage:
    """Tests for _handle_ws_message method."""

    @pytest.mark.asyncio
    async def test_buffers_events_when_not_initialized(self):
        """Test events are buffered while syncing."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        # Not initialized yet
        assert book._initialized is False

        msg = b'{"e":"depthUpdate","E":1672515782136,"s":"BTCUSDT","U":100,"u":105,"b":[["93000.00","1.5"]],"a":[]}'

        await book._handle_ws_message(msg)

        # First event U should be recorded
        assert book._first_event_u == 100
        # Event should be buffered
        assert len(book._buffer) == 1

    @pytest.mark.asyncio
    async def test_applies_events_when_initialized(self):
        """Test events are applied when initialized."""
        on_update = MagicMock()
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=on_update,
            rest_client=MagicMock(),
        )

        # Simulate initialized state
        book._initialized = True
        book._last_update_id = 99

        msg = b'{"e":"depthUpdate","E":1672515782136,"s":"BTCUSDT","U":100,"u":105,"b":[["93000.00","1.5"]],"a":[]}'

        await book._handle_ws_message(msg)

        # Event should be applied
        assert book._bids[-93000.0] == 1.5
        assert book._last_update_id == 105
        # Snapshot should be emitted
        on_update.assert_called_once()


class TestBidAskOrdering:
    """Tests for bid/ask ordering logic."""

    def test_bids_sorted_descending(self):
        """Test bids are sorted by price descending (highest first)."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        # Add bids in random order
        book._bids[-92990.0] = 1.0
        book._bids[-93010.0] = 2.0  # Highest
        book._bids[-93000.0] = 3.0

        # Keys should be sorted ascending (most negative = highest price first)
        keys = list(book._bids.keys())
        assert keys == [-93010.0, -93000.0, -92990.0]

        # Best bid should be highest
        assert book.best_bid == 93010.0

    def test_asks_sorted_ascending(self):
        """Test asks are sorted by price ascending (lowest first)."""
        book = BinanceOrderBook(
            symbol="BTCUSDT",
            on_update=MagicMock(),
            rest_client=MagicMock(),
        )

        # Add asks in random order
        book._asks[93010.0] = 1.0
        book._asks[92990.0] = 2.0  # Lowest
        book._asks[93000.0] = 3.0

        # Keys should be sorted ascending
        keys = list(book._asks.keys())
        assert keys == [92990.0, 93000.0, 93010.0]

        # Best ask should be lowest
        assert book.best_ask == 92990.0
