"""Base WebSocket client with reconnection and message handling."""

import asyncio
import time
from collections.abc import Awaitable, Callable
from typing import Any

import structlog
import websockets
from websockets.asyncio.client import ClientConnection

logger = structlog.get_logger(__name__)

# Type aliases for callbacks
MessageCallback = Callable[[bytes], Awaitable[None]]
ConnectCallback = Callable[[], Awaitable[None]]


class BinanceWebSocketClient:
    """
    Reusable WebSocket client with automatic reconnection.

    Features:
    - Exponential backoff reconnection (1s -> 60s cap)
    - Binance ping/pong handling (server pings every 20s)
    - Callback-based message handling
    - Graceful shutdown
    """

    __slots__ = (
        "url",
        "on_message",
        "on_connect",
        "on_disconnect",
        "_ws",
        "_running",
        "_reconnect_delay",
        "_max_reconnect_delay",
        "_connect_task",
        "_connection_start_time",
        "_max_connection_age",
    )

    def __init__(
        self,
        url: str,
        on_message: MessageCallback,
        on_connect: ConnectCallback | None = None,
        on_disconnect: Callable[[], Awaitable[None]] | None = None,
    ):
        """
        Initialize WebSocket client.

        Args:
            url: WebSocket URL to connect to
            on_message: Async callback for each received message
            on_connect: Optional async callback on successful connection
            on_disconnect: Optional async callback on disconnection
        """
        self.url = url
        self.on_message = on_message
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect

        self._ws: ClientConnection | None = None
        self._running = False
        self._reconnect_delay = 1.0
        self._max_reconnect_delay = 60.0
        self._connect_task: asyncio.Task[Any] | None = None

        # Binance disconnects after 24 hours - proactively reconnect at 23 hours
        self._connection_start_time: float | None = None
        self._max_connection_age = 23 * 60 * 60  # 23 hours in seconds

    async def _connect_loop(self) -> None:
        """Main connection loop with reconnection."""
        while self._running:
            try:
                logger.info("ws_connecting", url=self.url)

                async with websockets.connect(
                    self.url,
                    ping_interval=20,  # Binance sends ping every 20s
                    ping_timeout=30,
                    close_timeout=10,
                    max_size=10 * 1024 * 1024,  # 10MB max message
                ) as ws:
                    self._ws = ws
                    self._reconnect_delay = 1.0  # Reset on successful connect
                    self._connection_start_time = time.time()

                    logger.info("ws_connected", url=self.url)

                    if self.on_connect:
                        try:
                            await self.on_connect()
                        except Exception as e:
                            logger.error("on_connect_error", error=str(e))

                    await self._receive_loop(ws)

            except websockets.ConnectionClosed as e:
                logger.warning(
                    "ws_connection_closed",
                    url=self.url,
                    code=e.code,
                    reason=e.reason,
                )
            except Exception as e:
                logger.warning(
                    "ws_connection_error",
                    url=self.url,
                    error=str(e),
                    error_type=type(e).__name__,
                )

            self._ws = None

            if self.on_disconnect:
                try:
                    await self.on_disconnect()
                except Exception as e:
                    logger.error("on_disconnect_error", error=str(e))

            if self._running:
                logger.info(
                    "ws_reconnecting",
                    url=self.url,
                    delay=self._reconnect_delay,
                )
                await asyncio.sleep(self._reconnect_delay)
                self._reconnect_delay = min(
                    self._reconnect_delay * 2, self._max_reconnect_delay
                )

    async def _receive_loop(self, ws: ClientConnection) -> None:
        """Process incoming messages."""
        async for message in ws:
            # Check connection age - Binance disconnects after 24h, reconnect at 23h
            if self._connection_start_time is not None:
                connection_age = time.time() - self._connection_start_time
                if connection_age > self._max_connection_age:
                    logger.info(
                        "proactive_reconnect",
                        url=self.url,
                        reason="24h_limit",
                        connection_age_hours=connection_age / 3600,
                    )
                    await ws.close()
                    return  # Will trigger reconnect in _connect_loop

            try:
                if isinstance(message, str):
                    message = message.encode("utf-8")
                await self.on_message(message)
            except Exception as e:
                logger.error(
                    "message_handler_error",
                    error=str(e),
                    error_type=type(e).__name__,
                )

    async def send(self, data: str | bytes) -> None:
        """
        Send message through WebSocket.

        Args:
            data: Message to send (string or bytes)
        """
        if self._ws is not None:
            await self._ws.send(data)
        else:
            logger.warning("send_failed_not_connected")

    async def start(self) -> None:
        """Start the WebSocket client."""
        if self._running:
            return

        self._running = True
        self._connect_task = asyncio.create_task(self._connect_loop())

    async def stop(self) -> None:
        """Stop the WebSocket client gracefully."""
        self._running = False

        if self._ws is not None:
            await self._ws.close()
            self._ws = None

        if self._connect_task is not None:
            self._connect_task.cancel()
            try:
                await self._connect_task
            except asyncio.CancelledError:
                pass
            self._connect_task = None

        logger.info("ws_stopped", url=self.url)

    @property
    def is_connected(self) -> bool:
        """Return True if WebSocket is connected."""
        return self._ws is not None and self._ws.state.name == "OPEN"

    async def __aenter__(self) -> "BinanceWebSocketClient":
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.stop()
