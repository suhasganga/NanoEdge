"""Tests for BinanceWebSocketClient."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from nanoedge.connectors.binance.ws_client import BinanceWebSocketClient


class TestBinanceWebSocketClientInit:
    """Tests for BinanceWebSocketClient initialization."""

    def test_init_with_required_params(self):
        """Test initialization with only required parameters."""
        on_message = AsyncMock()
        client = BinanceWebSocketClient(
            url="wss://stream.binance.com:9443/ws/btcusdt@trade",
            on_message=on_message,
        )

        assert client.url == "wss://stream.binance.com:9443/ws/btcusdt@trade"
        assert client.on_message is on_message
        assert client.on_connect is None
        assert client.on_disconnect is None
        assert client._running is False
        assert client._ws is None

    def test_init_with_all_callbacks(self):
        """Test initialization with all optional callbacks."""
        on_message = AsyncMock()
        on_connect = AsyncMock()
        on_disconnect = AsyncMock()

        client = BinanceWebSocketClient(
            url="wss://stream.binance.com:9443/ws/btcusdt@trade",
            on_message=on_message,
            on_connect=on_connect,
            on_disconnect=on_disconnect,
        )

        assert client.on_message is on_message
        assert client.on_connect is on_connect
        assert client.on_disconnect is on_disconnect

    def test_default_reconnect_delay(self):
        """Test default reconnect delay configuration."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        assert client._reconnect_delay == 1.0
        assert client._max_reconnect_delay == 60.0

    def test_default_max_connection_age(self):
        """Test default max connection age is 23 hours."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        # 23 hours in seconds
        assert client._max_connection_age == 23 * 60 * 60


class TestIsConnected:
    """Tests for is_connected property."""

    def test_not_connected_when_ws_is_none(self):
        """Test is_connected returns False when ws is None."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        assert client.is_connected is False

    def test_connected_when_ws_state_is_open(self):
        """Test is_connected returns True when ws state is OPEN."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        mock_ws = MagicMock()
        mock_ws.state.name = "OPEN"
        client._ws = mock_ws

        assert client.is_connected is True

    def test_not_connected_when_ws_state_is_closed(self):
        """Test is_connected returns False when ws state is not OPEN."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        mock_ws = MagicMock()
        mock_ws.state.name = "CLOSED"
        client._ws = mock_ws

        assert client.is_connected is False


class TestReconnectDelay:
    """Tests for reconnection delay logic."""

    def test_exponential_backoff(self):
        """Test that reconnect delay doubles on each failure."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        # Initial delay
        assert client._reconnect_delay == 1.0

        # Simulate first reconnect
        client._reconnect_delay = min(
            client._reconnect_delay * 2, client._max_reconnect_delay
        )
        assert client._reconnect_delay == 2.0

        # Simulate second reconnect
        client._reconnect_delay = min(
            client._reconnect_delay * 2, client._max_reconnect_delay
        )
        assert client._reconnect_delay == 4.0

        # Simulate third reconnect
        client._reconnect_delay = min(
            client._reconnect_delay * 2, client._max_reconnect_delay
        )
        assert client._reconnect_delay == 8.0

    def test_backoff_capped_at_max(self):
        """Test that reconnect delay is capped at max_reconnect_delay."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        # Set delay close to max
        client._reconnect_delay = 32.0

        # Double it
        client._reconnect_delay = min(
            client._reconnect_delay * 2, client._max_reconnect_delay
        )
        assert client._reconnect_delay == 60.0

        # Try to double again - should stay at 60
        client._reconnect_delay = min(
            client._reconnect_delay * 2, client._max_reconnect_delay
        )
        assert client._reconnect_delay == 60.0


class TestSend:
    """Tests for send method."""

    @pytest.mark.asyncio
    async def test_send_when_connected(self):
        """Test send works when connected."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        mock_ws = AsyncMock()
        client._ws = mock_ws

        await client.send('{"method": "SUBSCRIBE"}')

        mock_ws.send.assert_called_once_with('{"method": "SUBSCRIBE"}')

    @pytest.mark.asyncio
    async def test_send_when_not_connected(self):
        """Test send does nothing when not connected (ws is None)."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        # No error should be raised
        await client.send('{"method": "SUBSCRIBE"}')


class TestStartStop:
    """Tests for start/stop lifecycle."""

    @pytest.mark.asyncio
    async def test_start_sets_running_flag(self):
        """Test start sets _running to True."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        # Mock _connect_loop at class level (required for __slots__ classes)
        with patch.object(
            BinanceWebSocketClient, "_connect_loop", new_callable=AsyncMock
        ):
            await client.start()

            assert client._running is True
            assert client._connect_task is not None

            # Clean up
            await client.stop()

    @pytest.mark.asyncio
    async def test_start_is_idempotent(self):
        """Test calling start multiple times is safe."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        connect_loop_mock = AsyncMock()
        with patch.object(BinanceWebSocketClient, "_connect_loop", connect_loop_mock):
            await client.start()
            task1 = client._connect_task

            await client.start()  # Second call
            task2 = client._connect_task

            # Should be the same task (not restarted)
            assert task1 is task2

            await client.stop()

    @pytest.mark.asyncio
    async def test_stop_clears_state(self):
        """Test stop clears running flag and task."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        with patch.object(
            BinanceWebSocketClient, "_connect_loop", new_callable=AsyncMock
        ):
            await client.start()
            await client.stop()

            assert client._running is False
            assert client._connect_task is None

    @pytest.mark.asyncio
    async def test_stop_closes_websocket(self):
        """Test stop closes websocket connection."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        mock_ws = AsyncMock()
        client._ws = mock_ws
        client._running = True

        await client.stop()

        mock_ws.close.assert_called_once()
        assert client._ws is None


class TestContextManager:
    """Tests for async context manager support."""

    @pytest.mark.asyncio
    async def test_context_manager_starts_and_stops(self):
        """Test context manager calls start and stop."""
        on_message = AsyncMock()

        with patch.object(
            BinanceWebSocketClient, "start", new_callable=AsyncMock
        ) as mock_start:
            with patch.object(
                BinanceWebSocketClient, "stop", new_callable=AsyncMock
            ) as mock_stop:
                async with BinanceWebSocketClient(
                    url="wss://example.com",
                    on_message=on_message,
                ) as client:
                    mock_start.assert_called_once()
                    assert client is not None

                mock_stop.assert_called_once()


class TestConnectionAgeCheck:
    """Tests for 23-hour connection age limit."""

    def test_connection_start_time_initialized_to_none(self):
        """Test connection start time is None before connecting."""
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        assert client._connection_start_time is None

    @pytest.mark.asyncio
    async def test_receive_loop_checks_connection_age(self):
        """Test receive loop checks connection age against max."""
        import time

        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=AsyncMock(),
        )

        # Simulate connection started 24 hours ago
        client._connection_start_time = time.time() - (24 * 60 * 60)

        # Create async iterator
        async def async_gen():
            yield b"test_message"

        mock_ws = MagicMock()
        mock_ws.__aiter__ = lambda _: async_gen()
        mock_ws.close = AsyncMock()

        # Should close connection due to age
        await client._receive_loop(mock_ws)

        mock_ws.close.assert_called_once()


class TestCallbackInvocation:
    """Tests for callback invocation."""

    @pytest.mark.asyncio
    async def test_on_message_receives_bytes(self):
        """Test on_message callback receives bytes."""
        on_message = AsyncMock()
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=on_message,
        )

        # Set connection_start_time so age check doesn't close
        import time

        client._connection_start_time = time.time()

        # Create async iterator
        async def async_gen():
            yield b"test_message"

        mock_ws = MagicMock()
        mock_ws.__aiter__ = lambda _: async_gen()

        await client._receive_loop(mock_ws)

        on_message.assert_called_once_with(b"test_message")

    @pytest.mark.asyncio
    async def test_on_message_converts_string_to_bytes(self):
        """Test string messages are converted to bytes."""
        on_message = AsyncMock()
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=on_message,
        )

        import time

        client._connection_start_time = time.time()

        # Create async iterator with string message
        async def async_gen():
            yield "string_message"

        mock_ws = MagicMock()
        mock_ws.__aiter__ = lambda _: async_gen()

        await client._receive_loop(mock_ws)

        on_message.assert_called_once_with(b"string_message")

    @pytest.mark.asyncio
    async def test_on_message_error_is_logged(self):
        """Test errors in on_message handler are caught and logged."""
        on_message = AsyncMock(side_effect=ValueError("Handler error"))
        client = BinanceWebSocketClient(
            url="wss://example.com",
            on_message=on_message,
        )

        import time

        client._connection_start_time = time.time()

        # Create async iterator
        async def async_gen():
            yield b"test"

        mock_ws = MagicMock()
        mock_ws.__aiter__ = lambda _: async_gen()

        # Should not raise, error is logged
        await client._receive_loop(mock_ws)

        on_message.assert_called_once()
