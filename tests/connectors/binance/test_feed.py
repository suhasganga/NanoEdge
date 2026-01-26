"""Tests for BinanceFeedHandler."""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from hft.connectors.binance.feed import BinanceFeedHandler
from hft.core.types import OHLCV, MarketStats, MarketTick, Trade


class TestBinanceFeedHandlerInit:
    """Tests for BinanceFeedHandler initialization."""

    def test_symbols_uppercased(self):
        """Test symbols are converted to uppercase."""
        handler = BinanceFeedHandler(
            symbols=["btcusdt", "ethusdt"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        assert handler.symbols == ["BTCUSDT", "ETHUSDT"]

    def test_url_construction(self):
        """Test combined stream URL is built correctly."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT", "ETHUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        # Should include aggTrade, kline, and ticker for each symbol
        assert "btcusdt@aggTrade" in handler.url
        assert "btcusdt@kline_1m" in handler.url
        assert "btcusdt@ticker" in handler.url
        assert "ethusdt@aggTrade" in handler.url
        assert "ethusdt@kline_1m" in handler.url
        assert "ethusdt@ticker" in handler.url
        assert handler.url.startswith("wss://stream.binance.com:9443/stream?streams=")

    def test_custom_base_url(self):
        """Test custom base URL is used."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
            base_url="wss://testnet.binance.vision",
        )

        assert handler.url.startswith("wss://testnet.binance.vision")

    def test_initial_stats_counters(self):
        """Test initial stats counters are zero."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        assert handler._tick_count == 0
        assert handler._kline_count == 0


class TestProcessAggTrade:
    """Tests for _process_agg_trade method."""

    def test_creates_market_tick(self):
        """Test aggTrade is converted to MarketTick correctly."""
        on_tick = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=on_tick,
            on_kline=MagicMock(),
        )

        data = {
            "e": "aggTrade",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "a": 123456789,
            "p": "93000.50",
            "q": "1.234",
            "f": 100,
            "l": 105,
            "T": 1672515782130,
            "m": False,  # buyer is NOT maker, so this was a buy
        }

        handler._process_agg_trade(data)

        on_tick.assert_called_once()
        tick = on_tick.call_args[0][0]
        assert isinstance(tick, MarketTick)
        assert tick.symbol == "BTCUSDT"
        assert tick.price == 93000.50
        assert tick.volume == 1.234
        assert tick.side == 1  # buy
        assert tick.exchange == "binance"
        assert tick.market == "spot"

    def test_sell_side_when_buyer_is_maker(self):
        """Test side is -1 when buyer is maker."""
        on_tick = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=on_tick,
            on_kline=MagicMock(),
        )

        data = {
            "e": "aggTrade",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "a": 123456789,
            "p": "93000.50",
            "q": "1.234",
            "f": 100,
            "l": 105,
            "T": 1672515782130,
            "m": True,  # buyer IS maker, so this was a sell
        }

        handler._process_agg_trade(data)

        tick = on_tick.call_args[0][0]
        assert tick.side == -1  # sell

    def test_creates_trade_when_callback_provided(self):
        """Test Trade is created when on_trade callback is provided."""
        on_tick = MagicMock()
        on_trade = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=on_tick,
            on_kline=MagicMock(),
            on_trade=on_trade,
        )

        data = {
            "e": "aggTrade",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "a": 123456789,
            "p": "93000.50",
            "q": "1.234",
            "f": 100,
            "l": 105,
            "T": 1672515782130,
            "m": False,
        }

        handler._process_agg_trade(data)

        on_trade.assert_called_once()
        trade = on_trade.call_args[0][0]
        assert isinstance(trade, Trade)
        assert trade.symbol == "BTCUSDT"
        assert trade.price == 93000.50
        assert trade.quantity == 1.234
        assert trade.is_buyer_maker is False
        assert trade.trade_id == 123456789

    def test_no_trade_when_callback_not_provided(self):
        """Test Trade is not created when on_trade callback is None."""
        on_tick = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=on_tick,
            on_kline=MagicMock(),
            on_trade=None,  # No callback
        )

        data = {
            "e": "aggTrade",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "a": 123456789,
            "p": "93000.50",
            "q": "1.234",
            "f": 100,
            "l": 105,
            "T": 1672515782130,
            "m": False,
        }

        # Should not raise
        handler._process_agg_trade(data)
        on_tick.assert_called_once()

    def test_increments_tick_count(self):
        """Test tick count is incremented."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        data = {
            "e": "aggTrade",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "a": 123456789,
            "p": "93000.50",
            "q": "1.234",
            "f": 100,
            "l": 105,
            "T": 1672515782130,
            "m": False,
        }

        assert handler._tick_count == 0
        handler._process_agg_trade(data)
        assert handler._tick_count == 1


class TestProcessKline:
    """Tests for _process_kline method."""

    def test_creates_ohlcv(self):
        """Test kline is converted to OHLCV correctly."""
        on_kline = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=on_kline,
        )

        data = {
            "e": "kline",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "k": {
                "t": 1672515780000,
                "T": 1672515839999,
                "s": "BTCUSDT",
                "i": "1m",
                "f": 100,
                "L": 200,
                "o": "93000.00",
                "c": "93050.50",
                "h": "93100.00",
                "l": "92900.00",
                "v": "125.5",
                "n": 500,
                "x": False,
                "q": "11675000.00",
                "V": "62.5",
                "Q": "5837500.00",
                "B": "0",
            },
        }

        handler._process_kline(data)

        on_kline.assert_called_once()
        ohlcv = on_kline.call_args[0][0]
        assert isinstance(ohlcv, OHLCV)
        assert ohlcv.symbol == "BTCUSDT"
        assert ohlcv.open == 93000.00
        assert ohlcv.high == 93100.00
        assert ohlcv.low == 92900.00
        assert ohlcv.close == 93050.50
        assert ohlcv.volume == 125.5
        assert ohlcv.trade_count == 500
        assert ohlcv.is_closed is False
        assert ohlcv.exchange == "binance"
        assert ohlcv.market == "spot"

    def test_closed_candle(self):
        """Test is_closed flag is captured."""
        on_kline = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=on_kline,
        )

        data = {
            "e": "kline",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "k": {
                "t": 1672515780000,
                "T": 1672515839999,
                "s": "BTCUSDT",
                "i": "1m",
                "f": 100,
                "L": 200,
                "o": "93000.00",
                "c": "93050.50",
                "h": "93100.00",
                "l": "92900.00",
                "v": "125.5",
                "n": 500,
                "x": True,  # Closed!
                "q": "11675000.00",
                "V": "62.5",
                "Q": "5837500.00",
                "B": "0",
            },
        }

        handler._process_kline(data)

        ohlcv = on_kline.call_args[0][0]
        assert ohlcv.is_closed is True

    def test_increments_kline_count(self):
        """Test kline count is incremented."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        data = {
            "e": "kline",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "k": {
                "t": 1672515780000,
                "T": 1672515839999,
                "s": "BTCUSDT",
                "i": "1m",
                "f": 100,
                "L": 200,
                "o": "93000.00",
                "c": "93050.50",
                "h": "93100.00",
                "l": "92900.00",
                "v": "125.5",
                "n": 500,
                "x": False,
                "q": "11675000.00",
                "V": "62.5",
                "Q": "5837500.00",
                "B": "0",
            },
        }

        assert handler._kline_count == 0
        handler._process_kline(data)
        assert handler._kline_count == 1


class TestProcessTicker:
    """Tests for _process_ticker method."""

    def test_creates_market_stats(self):
        """Test ticker is converted to MarketStats correctly."""
        on_stats = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
            on_stats=on_stats,
        )

        data = {
            "e": "24hrTicker",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "p": "100.50",
            "P": "0.11",
            "w": "93000.00",
            "c": "93050.50",
            "Q": "0.001",
            "o": "92950.00",
            "h": "93500.00",
            "l": "92500.00",
            "v": "50000.00",
            "q": "4650000000.00",
            "O": 1672429382136,
            "C": 1672515782136,
            "F": 12345,
            "L": 123456,
            "n": 111000,
        }

        handler._process_ticker(data)

        on_stats.assert_called_once()
        stats = on_stats.call_args[0][0]
        assert isinstance(stats, MarketStats)
        assert stats.symbol == "BTCUSDT"
        assert stats.price_change == 100.50
        assert stats.price_change_percent == 0.11
        assert stats.high_24h == 93500.00
        assert stats.low_24h == 92500.00
        assert stats.volume_24h == 50000.00
        assert stats.trade_count_24h == 111000
        assert stats.last_price == 93050.50
        assert stats.open_price == 92950.00

    def test_skipped_when_no_callback(self):
        """Test ticker is skipped when on_stats callback is None."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
            on_stats=None,  # No callback
        )

        data = {
            "e": "24hrTicker",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "p": "100.50",
            "P": "0.11",
            "w": "93000.00",
            "c": "93050.50",
            "Q": "0.001",
            "o": "92950.00",
            "h": "93500.00",
            "l": "92500.00",
            "v": "50000.00",
            "q": "4650000000.00",
            "O": 1672429382136,
            "C": 1672515782136,
            "F": 12345,
            "L": 123456,
            "n": 111000,
        }

        # Should not raise
        handler._process_ticker(data)


class TestHandleMessage:
    """Tests for _handle_message method."""

    @pytest.mark.asyncio
    async def test_routes_agg_trade(self):
        """Test aggTrade messages are routed correctly."""
        on_tick = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=on_tick,
            on_kline=MagicMock(),
        )

        msg = {
            "stream": "btcusdt@aggTrade",
            "data": {
                "e": "aggTrade",
                "E": 1672515782136,
                "s": "BTCUSDT",
                "a": 123456789,
                "p": "93000.50",
                "q": "1.234",
                "f": 100,
                "l": 105,
                "T": 1672515782130,
                "m": False,
            },
        }

        await handler._handle_message(json.dumps(msg).encode())

        on_tick.assert_called_once()

    @pytest.mark.asyncio
    async def test_routes_kline(self):
        """Test kline messages are routed correctly."""
        on_kline = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=on_kline,
        )

        msg = {
            "stream": "btcusdt@kline_1m",
            "data": {
                "e": "kline",
                "E": 1672515782136,
                "s": "BTCUSDT",
                "k": {
                    "t": 1672515780000,
                    "T": 1672515839999,
                    "s": "BTCUSDT",
                    "i": "1m",
                    "f": 100,
                    "L": 200,
                    "o": "93000.00",
                    "c": "93050.50",
                    "h": "93100.00",
                    "l": "92900.00",
                    "v": "125.5",
                    "n": 500,
                    "x": False,
                    "q": "11675000.00",
                    "V": "62.5",
                    "Q": "5837500.00",
                    "B": "0",
                },
            },
        }

        await handler._handle_message(json.dumps(msg).encode())

        on_kline.assert_called_once()

    @pytest.mark.asyncio
    async def test_routes_ticker(self):
        """Test ticker messages are routed correctly."""
        on_stats = MagicMock()
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
            on_stats=on_stats,
        )

        msg = {
            "stream": "btcusdt@ticker",
            "data": {
                "e": "24hrTicker",
                "E": 1672515782136,
                "s": "BTCUSDT",
                "p": "100.50",
                "P": "0.11",
                "w": "93000.00",
                "c": "93050.50",
                "Q": "0.001",
                "o": "92950.00",
                "h": "93500.00",
                "l": "92500.00",
                "v": "50000.00",
                "q": "4650000000.00",
                "O": 1672429382136,
                "C": 1672515782136,
                "F": 12345,
                "L": 123456,
                "n": 111000,
            },
        }

        await handler._handle_message(json.dumps(msg).encode())

        on_stats.assert_called_once()


class TestIsConnected:
    """Tests for is_connected property."""

    def test_delegates_to_ws_client(self):
        """Test is_connected delegates to WebSocket client."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        # Mock the internal WS client
        handler._ws_client = MagicMock()
        handler._ws_client.is_connected = True

        assert handler.is_connected is True

        handler._ws_client.is_connected = False
        assert handler.is_connected is False


class TestStartStop:
    """Tests for start/stop methods."""

    @pytest.mark.asyncio
    async def test_start_delegates_to_ws_client(self):
        """Test start() calls ws_client.start()."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        handler._ws_client = AsyncMock()

        await handler.start()

        handler._ws_client.start.assert_called_once()

    @pytest.mark.asyncio
    async def test_stop_delegates_to_ws_client(self):
        """Test stop() calls ws_client.stop()."""
        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        handler._ws_client = AsyncMock()

        await handler.stop()

        handler._ws_client.stop.assert_called_once()


class TestMaybeLogStats:
    """Tests for _maybe_log_stats method."""

    def test_logs_after_60_seconds(self):
        """Test stats are logged after 60 seconds."""
        import time

        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        # Set last stats time to 61 seconds ago
        handler._last_stats_time = time.time() - 61
        handler._tick_count = 100
        handler._kline_count = 50

        with patch("hft.connectors.binance.feed.logger") as mock_logger:
            handler._maybe_log_stats()
            mock_logger.info.assert_called_once()

        # Counters should be reset
        assert handler._tick_count == 0
        assert handler._kline_count == 0

    def test_no_log_before_60_seconds(self):
        """Test stats are not logged before 60 seconds."""
        import time

        handler = BinanceFeedHandler(
            symbols=["BTCUSDT"],
            on_tick=MagicMock(),
            on_kline=MagicMock(),
        )

        # Set last stats time to 30 seconds ago
        handler._last_stats_time = time.time() - 30
        handler._tick_count = 100
        handler._kline_count = 50

        with patch("hft.connectors.binance.feed.logger") as mock_logger:
            handler._maybe_log_stats()
            mock_logger.info.assert_not_called()

        # Counters should NOT be reset
        assert handler._tick_count == 100
        assert handler._kline_count == 50
