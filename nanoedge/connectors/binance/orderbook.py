"""Local order book manager with Binance sync procedure."""

import asyncio
import time
from collections import deque
from collections.abc import Callable

import structlog
from sortedcontainers import SortedDict

from nanoedge.connectors.binance.rest_client import BinanceRestClient
from nanoedge.connectors.binance.types import BinanceDepthUpdate, depth_update_decoder
from nanoedge.connectors.binance.ws_client import BinanceWebSocketClient
from nanoedge.core.types import DepthLevel, OrderBookSnapshot

logger = structlog.get_logger(__name__)

# Type alias
OrderBookCallback = Callable[[OrderBookSnapshot], None]


class BinanceOrderBook:
    """
    Local order book with Binance 7-step sync procedure.

    Maintains accurate order book state by:
    1. Connecting to depth stream
    2. Buffering events until REST snapshot is fetched
    3. Validating snapshot against buffered events
    4. Applying events with gap detection

    See: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#how-to-manage-a-local-order-book-correctly
    """

    __slots__ = (
        "symbol",
        "on_update",
        "rest_client",
        "depth_levels",
        "_bids",
        "_asks",
        "_last_update_id",
        "_initialized",
        "_buffer",
        "_first_event_u",
        "_syncing",
        "_sync_task",
        "_ws_client",
        "_update_count",
        "_resync_count",
    )

    def __init__(
        self,
        symbol: str,
        on_update: OrderBookCallback,
        rest_client: BinanceRestClient,
        ws_base_url: str = "wss://stream.binance.com:9443",
        depth_levels: int = 50,
    ):
        """
        Initialize order book manager.

        Args:
            symbol: Trading pair (e.g., "BTCUSDT")
            on_update: Callback for order book updates
            rest_client: REST client for snapshots
            ws_base_url: WebSocket base URL
            depth_levels: Number of levels to emit (default: 50)
        """
        self.symbol = symbol.upper()
        self.on_update = on_update
        self.rest_client = rest_client
        self.depth_levels = depth_levels

        # Order book state - SortedDict for O(log n) operations
        # Bids: sorted by price descending (negate key)
        # Asks: sorted by price ascending
        self._bids: SortedDict[float, float] = SortedDict()
        self._asks: SortedDict[float, float] = SortedDict()
        self._last_update_id: int = 0
        self._initialized = False

        # Event buffer for sync procedure
        self._buffer: deque[BinanceDepthUpdate] = deque(maxlen=1000)
        self._first_event_u: int | None = None

        # Sync state
        self._syncing = False
        self._sync_task: asyncio.Task | None = None

        # WebSocket client
        ws_url = f"{ws_base_url}/ws/{symbol.lower()}@depth@100ms"
        self._ws_client = BinanceWebSocketClient(
            url=ws_url,
            on_message=self._handle_ws_message,
            on_connect=self._on_ws_connect,
            on_disconnect=self._on_ws_disconnect,
        )

        # Stats
        self._update_count = 0
        self._resync_count = 0

    async def _on_ws_connect(self) -> None:
        """Handle WebSocket connection - trigger sync."""
        logger.info("orderbook_ws_connected", symbol=self.symbol)
        self._reset_state()
        self._schedule_sync()

    async def _on_ws_disconnect(self) -> None:
        """Handle WebSocket disconnection."""
        logger.warning("orderbook_ws_disconnected", symbol=self.symbol)
        self._initialized = False

    def _reset_state(self) -> None:
        """Reset order book state for resync."""
        self._bids.clear()
        self._asks.clear()
        self._last_update_id = 0
        self._initialized = False
        self._buffer.clear()
        self._first_event_u = None

    def _schedule_sync(self) -> None:
        """Schedule async sync task."""
        if self._sync_task is not None:
            self._sync_task.cancel()
        self._sync_task = asyncio.create_task(self._sync_order_book())

    async def _sync_order_book(self) -> None:
        """
        Binance 7-step order book sync procedure.

        Steps:
        1. Already connected to @depth stream
        2. Buffer events, note first U
        3. Get REST snapshot
        4. Validate snapshot freshness
        5. Discard old events
        6. Initialize book from snapshot
        7. Apply buffered events
        """
        self._syncing = True
        logger.info("orderbook_sync_starting", symbol=self.symbol)

        try:
            # Wait for first event to arrive
            retry_count = 0
            while self._first_event_u is None and retry_count < 50:
                await asyncio.sleep(0.1)
                retry_count += 1

            if self._first_event_u is None:
                logger.error("orderbook_no_events", symbol=self.symbol)
                return

            # Step 3: Get REST snapshot
            snapshot = await self.rest_client.get_depth_snapshot(
                self.symbol, limit=1000
            )

            # Step 4: Validate snapshot freshness
            if snapshot.lastUpdateId < self._first_event_u:
                logger.warning(
                    "orderbook_snapshot_stale",
                    symbol=self.symbol,
                    snapshot_id=snapshot.lastUpdateId,
                    first_event_u=self._first_event_u,
                )
                # Retry sync
                await asyncio.sleep(0.5)
                self._schedule_sync()
                return

            # Step 6: Initialize book from snapshot
            for price_str, qty_str in snapshot.bids:
                price = float(price_str)
                qty = float(qty_str)
                if qty > 0:
                    # Negate price for descending sort
                    self._bids[-price] = qty

            for price_str, qty_str in snapshot.asks:
                price = float(price_str)
                qty = float(qty_str)
                if qty > 0:
                    self._asks[price] = qty

            self._last_update_id = snapshot.lastUpdateId

            # Step 5 & 7: Apply buffered events
            applied_count = 0
            for event in self._buffer:
                if event.u <= self._last_update_id:
                    continue  # Discard old events
                if self._apply_event(event):
                    applied_count += 1

            self._buffer.clear()
            self._initialized = True
            self._syncing = False

            logger.info(
                "orderbook_initialized",
                symbol=self.symbol,
                bid_levels=len(self._bids),
                ask_levels=len(self._asks),
                last_update_id=self._last_update_id,
                buffered_events_applied=applied_count,
            )

            # Emit initial snapshot
            self._emit_snapshot()

        except Exception as e:
            logger.error(
                "orderbook_sync_error",
                symbol=self.symbol,
                error=str(e),
            )
            self._syncing = False
            # Retry after delay
            await asyncio.sleep(1.0)
            self._schedule_sync()

    async def _handle_ws_message(self, raw: bytes) -> None:
        """Process depth update message."""
        try:
            event = depth_update_decoder.decode(raw)

            # Step 2: Buffer events and note first U
            if self._first_event_u is None:
                self._first_event_u = event.U

            if not self._initialized:
                # Still syncing, buffer the event
                self._buffer.append(event)
                return

            # Apply event to initialized book
            if self._apply_event(event):
                self._emit_snapshot()

        except Exception as e:
            logger.error(
                "orderbook_message_error",
                symbol=self.symbol,
                error=str(e),
            )

    def _apply_event(self, event: BinanceDepthUpdate) -> bool:
        """
        Apply depth update event to local book.

        Returns True if update was applied, False if skipped/error.
        """
        # Check for sequence gap
        if event.U > self._last_update_id + 1:
            logger.error(
                "orderbook_gap_detected",
                symbol=self.symbol,
                expected=self._last_update_id + 1,
                got=event.U,
            )
            self._resync_count += 1
            self._reset_state()
            self._schedule_sync()
            return False

        # Skip old events
        if event.u <= self._last_update_id:
            return False

        # Apply bid updates
        for price_str, qty_str in event.b:
            price = float(price_str)
            qty = float(qty_str)
            if qty == 0:
                # Remove level
                self._bids.pop(-price, None)
            else:
                # Insert/update level (negate for descending sort)
                self._bids[-price] = qty

        # Apply ask updates
        for price_str, qty_str in event.a:
            price = float(price_str)
            qty = float(qty_str)
            if qty == 0:
                # Remove level
                self._asks.pop(price, None)
            else:
                # Insert/update level
                self._asks[price] = qty

        self._last_update_id = event.u
        self._update_count += 1

        return True

    def _emit_snapshot(self) -> None:
        """Build and emit order book snapshot."""
        # Get top N bids (keys are negated, so smallest keys = highest prices)
        top_bids = []
        for neg_price in self._bids.keys()[:self.depth_levels]:
            price = -neg_price
            size = self._bids[neg_price]
            top_bids.append(DepthLevel(price=price, size=size))

        # Get top N asks (sorted ascending)
        top_asks = []
        for price in self._asks.keys()[:self.depth_levels]:
            size = self._asks[price]
            top_asks.append(DepthLevel(price=price, size=size))

        snapshot = OrderBookSnapshot(
            timestamp_ms=int(time.time() * 1000),
            exchange="binance",
            market="spot",
            symbol=self.symbol,
            bids=top_bids,
            asks=top_asks,
            last_update_id=self._last_update_id,
        )

        try:
            self.on_update(snapshot)
        except Exception as e:
            logger.error("orderbook_callback_error", error=str(e))

    async def start(self) -> None:
        """Start the order book manager."""
        logger.info("orderbook_starting", symbol=self.symbol)
        await self._ws_client.start()

    async def stop(self) -> None:
        """Stop the order book manager."""
        if self._sync_task is not None:
            self._sync_task.cancel()
            try:
                await self._sync_task
            except asyncio.CancelledError:
                pass

        await self._ws_client.stop()
        logger.info(
            "orderbook_stopped",
            symbol=self.symbol,
            updates_processed=self._update_count,
            resyncs=self._resync_count,
        )

    @property
    def is_initialized(self) -> bool:
        """Return True if order book is synced and ready."""
        return self._initialized

    @property
    def best_bid(self) -> float | None:
        """Return best bid price."""
        if self._bids:
            return -self._bids.keys()[0]
        return None

    @property
    def best_ask(self) -> float | None:
        """Return best ask price."""
        if self._asks:
            return self._asks.keys()[0]
        return None

    @property
    def spread(self) -> float | None:
        """Return current spread."""
        bid = self.best_bid
        ask = self.best_ask
        if bid is not None and ask is not None:
            return ask - bid
        return None
