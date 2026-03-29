"""Fyers WebSocket market data feed handler using official SDK.

Uses fyers_apiv3 SDK which handles:
- WebSocket connection management
- Authentication
- Auto-reconnection
- Message parsing

Fyers WebSocket provides:
- Symbol updates (SymbolUpdate): LTP, volume, bid/ask prices
- Depth updates (DepthUpdate): 5-level order book
- Lite mode: LTP only for minimal data

Note: Fyers does NOT have a @kline_1m stream like Binance.
Candles must be aggregated from tick data using FyersOHLCVAggregator.
"""

from __future__ import annotations

import asyncio
import threading
import time
from collections.abc import Callable
from typing import Any

import structlog

from nanoedge.connectors.fyers.aggregator import FyersOHLCVAggregator
from nanoedge.core.types import OHLCV, DepthLevel, MarketStats, MarketTick, OrderBookSnapshot, Trade

logger = structlog.get_logger(__name__)

# Type aliases
TickCallback = Callable[[MarketTick], None]
KlineCallback = Callable[[OHLCV], None]
DepthCallback = Callable[[OrderBookSnapshot], None]
TradeCallback = Callable[[Trade], None]
StatsCallback = Callable[[MarketStats], None]


class FyersFeedHandler:
    """
    Fyers WebSocket feed handler using official fyers_apiv3 SDK.

    Handles:
    - Symbol updates (ticks with LTP, volume, bid/ask)
    - Depth updates (5-level order book)
    - Candle aggregation (since Fyers has no kline stream)

    Usage:
        handler = FyersFeedHandler(
            app_id="your_app_id",
            access_token="your_token",
            symbols=["NSE:RELIANCE-EQ", "NSE:NIFTY50-INDEX"],
            on_tick=handle_tick,
            on_kline=handle_kline,
        )
        await handler.start()
    """

    def __init__(
        self,
        app_id: str,
        access_token: str,
        symbols: list[str],
        on_tick: TickCallback | None = None,
        on_kline: KlineCallback | None = None,
        on_depth: DepthCallback | None = None,
        on_trade: TradeCallback | None = None,
        on_stats: StatsCallback | None = None,
        lite_mode: bool = False,
    ):
        """
        Initialize Fyers feed handler.

        Args:
            app_id: Fyers app ID (e.g., "XXXXXX-100")
            access_token: OAuth2 access token
            symbols: List of Fyers symbols (e.g., ["NSE:RELIANCE-EQ"])
            on_tick: Callback for tick data
            on_kline: Callback for aggregated candles
            on_depth: Callback for depth updates
            on_trade: Callback for individual trades
            on_stats: Callback for market stats
            lite_mode: If True, receive only LTP updates (less data)
        """
        self.app_id = app_id
        self.access_token = access_token
        self.symbols = symbols
        self.on_tick = on_tick
        self.on_kline = on_kline
        self.on_depth = on_depth
        self.on_trade = on_trade
        self.on_stats = on_stats
        self.lite_mode = lite_mode

        # SDK instance
        self._fyers_socket = None
        self._running = False
        self._connected = False

        # Thread for SDK (it runs in its own thread)
        self._sdk_thread: threading.Thread | None = None

        # Tick-to-candle aggregators (one per symbol)
        self._aggregators: dict[str, FyersOHLCVAggregator] = {}

        # Stats tracking
        self._tick_count = 0
        self._last_stats_time = time.time()

        # Initialize aggregators
        for symbol in symbols:
            market = self._get_market_from_symbol(symbol)
            self._aggregators[symbol] = FyersOHLCVAggregator(
                symbol=symbol,
                exchange="fyers",
                market=market,
                on_candle_close=self._on_candle_close,
            )

    async def start(self) -> None:
        """Start the feed handler (non-blocking)."""
        if self._running:
            return

        self._running = True
        logger.info("fyers_feed_starting", symbols=self.symbols, lite_mode=self.lite_mode)

        # Start SDK in background thread
        self._sdk_thread = threading.Thread(target=self._run_sdk, daemon=True)
        self._sdk_thread.start()

    def _run_sdk(self) -> None:
        """Run the Fyers SDK in a separate thread."""
        try:
            from fyers_apiv3.FyersWebsocket import data_ws
        except ImportError:
            logger.error("fyers_sdk_not_installed", hint="Run: uv add fyers-apiv3")
            return

        # Access token format: "appid:accesstoken"
        full_token = f"{self.app_id}:{self.access_token}"

        def on_message(message: dict) -> None:
            """Handle incoming WebSocket message."""
            try:
                self._process_message(message)
            except Exception as e:
                logger.error("fyers_message_error", error=str(e))

        def on_error(message: Any) -> None:
            """Handle WebSocket error."""
            logger.error("fyers_ws_error", error=str(message))

        def on_close(message: Any) -> None:
            """Handle WebSocket close."""
            self._connected = False
            logger.warning("fyers_ws_closed", message=str(message))

        def on_open() -> None:
            """Handle WebSocket open - subscribe to symbols."""
            self._connected = True
            logger.info("fyers_ws_connected")

            # Subscribe to symbol updates
            data_type = "SymbolUpdate"
            self._fyers_socket.subscribe(symbols=self.symbols, data_type=data_type)
            logger.info("fyers_subscribed", symbols=self.symbols, data_type=data_type)

            # Also subscribe to depth if callback provided
            if self.on_depth:
                self._fyers_socket.subscribe(symbols=self.symbols, data_type="DepthUpdate")
                logger.info("fyers_depth_subscribed", symbols=self.symbols)

        try:
            # Create FyersDataSocket instance
            self._fyers_socket = data_ws.FyersDataSocket(
                access_token=full_token,
                log_path="",
                litemode=self.lite_mode,
                write_to_file=False,
                reconnect=True,
                on_connect=on_open,
                on_close=on_close,
                on_error=on_error,
                on_message=on_message,
                reconnect_retry=50,  # Max retries
            )

            # Connect and keep running
            self._fyers_socket.connect()
            self._fyers_socket.keep_running()

        except Exception as e:
            logger.error("fyers_sdk_error", error=str(e))
            self._running = False

    def _process_message(self, message: dict | list) -> None:
        """Process incoming message from Fyers WebSocket."""
        # Fyers can send single dict or list of dicts
        if isinstance(message, list):
            for msg in message:
                self._process_single_message(msg)
        else:
            self._process_single_message(message)

        # Log stats periodically
        self._maybe_log_stats()

    def _process_single_message(self, data: dict) -> None:
        """Process a single message."""
        # Check message type
        msg_type = data.get("type") or data.get("t")

        if msg_type == "sf" or "ltp" in data:
            # Symbol update (full or lite mode)
            self._process_symbol_update(data)
        elif msg_type == "dp" or "bids" in data:
            # Depth update
            self._process_depth_update(data)
        elif msg_type == "error":
            logger.error("fyers_api_error", message=data)
        else:
            # Log unknown message types for debugging
            logger.debug("fyers_unknown_message", data=data)

    def _process_symbol_update(self, data: dict) -> None:
        """Process symbol update message and emit tick + stats."""
        try:
            # Handle different field names (full vs lite mode)
            symbol = data.get("symbol", "") or data.get("n", "")
            ltp = float(data.get("ltp", 0) or data.get("lp", 0))
            volume = int(data.get("last_traded_qty", 0) or data.get("ltq", 0) or data.get("v", 0))
            timestamp_sec = int(
                data.get("last_traded_time", 0) or data.get("ltt", 0) or data.get("tt", 0) or time.time()
            )

            if not symbol or ltp <= 0:
                return

            # Create MarketTick
            tick = MarketTick(
                timestamp_ns=timestamp_sec * 1_000_000_000,  # seconds to nanoseconds
                exchange="fyers",
                market=self._get_market_from_symbol(symbol),
                symbol=symbol,
                price=ltp,
                volume=float(volume) if volume else 1.0,
                side=0,  # Fyers doesn't provide trade direction
            )

            self._tick_count += 1

            # Emit tick callback
            if self.on_tick:
                self.on_tick(tick)

            # Update aggregator for candle building
            aggregator = self._aggregators.get(symbol)
            if aggregator:
                completed = aggregator.update(tick)
                # Completed candle is handled by on_candle_close callback

                # Emit partial candle updates periodically
                if self.on_kline:
                    current = aggregator.get_current()
                    if current:
                        self.on_kline(current)

            # Also emit trade for recent trades display
            if self.on_trade:
                trade = Trade(
                    timestamp_ms=timestamp_sec * 1000,
                    exchange="fyers",
                    market=self._get_market_from_symbol(symbol),
                    symbol=symbol,
                    price=ltp,
                    quantity=float(volume) if volume else 1.0,
                    is_buyer_maker=False,  # Unknown from Fyers data
                    trade_id=timestamp_sec,  # Use timestamp as trade ID
                )
                self.on_trade(trade)

            # Emit market stats
            if self.on_stats:
                stats = MarketStats(
                    timestamp_ms=timestamp_sec * 1000,
                    exchange="fyers",
                    market=self._get_market_from_symbol(symbol),
                    symbol=symbol,
                    price_change=float(data.get("ch", 0) or data.get("c", 0)),
                    price_change_percent=float(data.get("chp", 0) or data.get("cp", 0)),
                    high_24h=float(data.get("high_price", 0) or data.get("h", 0)),
                    low_24h=float(data.get("low_price", 0) or data.get("l", 0)),
                    volume_24h=float(data.get("vol_traded_today", 0) or data.get("v", 0)),
                    quote_volume_24h=0.0,  # Not provided by Fyers
                    trade_count_24h=0,  # Not provided by Fyers
                    last_price=ltp,
                    open_price=float(data.get("open_price", 0) or data.get("o", 0)),
                )
                self.on_stats(stats)

        except Exception as e:
            logger.error("fyers_symbol_update_error", error=str(e), data=data)

    def _process_depth_update(self, data: dict) -> None:
        """Process depth update message."""
        if not self.on_depth:
            return

        try:
            symbol = data.get("symbol", "") or data.get("n", "")
            if not symbol:
                return

            # Parse bid/ask levels (Fyers provides up to 5 levels)
            bids: list[DepthLevel] = []
            asks: list[DepthLevel] = []

            # Try different formats
            if "bids" in data and "asks" in data:
                # Already parsed format
                for level in data.get("bids", [])[:5]:
                    if isinstance(level, dict):
                        bids.append(DepthLevel(
                            price=float(level.get("price", 0)),
                            size=float(level.get("size", 0) or level.get("qty", 0)),
                        ))
                    elif isinstance(level, (list, tuple)) and len(level) >= 2:
                        bids.append(DepthLevel(price=float(level[0]), size=float(level[1])))

                for level in data.get("asks", [])[:5]:
                    if isinstance(level, dict):
                        asks.append(DepthLevel(
                            price=float(level.get("price", 0)),
                            size=float(level.get("size", 0) or level.get("qty", 0)),
                        ))
                    elif isinstance(level, (list, tuple)) and len(level) >= 2:
                        asks.append(DepthLevel(price=float(level[0]), size=float(level[1])))
            else:
                # Indexed format: bid_price1, bid_size1, etc.
                for i in range(1, 6):
                    bid_price = float(data.get(f"bid_price{i}", 0) or data.get(f"bp{i}", 0) or 0)
                    bid_size = float(data.get(f"bid_size{i}", 0) or data.get(f"bq{i}", 0) or 0)
                    ask_price = float(data.get(f"ask_price{i}", 0) or data.get(f"sp{i}", 0) or 0)
                    ask_size = float(data.get(f"ask_size{i}", 0) or data.get(f"sq{i}", 0) or 0)

                    if bid_price > 0:
                        bids.append(DepthLevel(price=bid_price, size=bid_size))
                    if ask_price > 0:
                        asks.append(DepthLevel(price=ask_price, size=ask_size))

            timestamp_ms = int(time.time() * 1000)
            snapshot = OrderBookSnapshot(
                timestamp_ms=timestamp_ms,
                exchange="fyers",
                market=self._get_market_from_symbol(symbol),
                symbol=symbol,
                bids=bids,
                asks=asks,
                last_update_id=timestamp_ms,
            )

            self.on_depth(snapshot)

        except Exception as e:
            logger.error("fyers_depth_update_error", error=str(e), data=data)

    def _on_candle_close(self, candle: OHLCV) -> None:
        """Handle closed candle from aggregator."""
        if self.on_kline:
            self.on_kline(candle)

        logger.debug(
            "fyers_candle_closed",
            symbol=candle.symbol,
            timestamp=candle.timestamp,
            close=candle.close,
            volume=candle.volume,
        )

    def _get_market_from_symbol(self, symbol: str) -> str:
        """Infer market type from Fyers symbol format."""
        symbol_upper = symbol.upper()

        if "-EQ" in symbol_upper:
            return "equity"
        elif "-INDEX" in symbol_upper:
            return "index"
        elif "FUT" in symbol_upper:
            return "futures"
        elif "CE" in symbol_upper or "PE" in symbol_upper:
            return "options"
        elif symbol_upper.startswith("MCX:"):
            return "commodity"
        elif "USDINR" in symbol_upper or "EURINR" in symbol_upper:
            return "currency"

        return "equity"

    def _maybe_log_stats(self) -> None:
        """Log stats every 60 seconds."""
        now = time.time()
        if now - self._last_stats_time >= 60:
            logger.info(
                "fyers_feed_stats",
                ticks_received=self._tick_count,
                symbols=len(self.symbols),
                connected=self._connected,
            )
            self._tick_count = 0
            self._last_stats_time = now

    async def stop(self) -> None:
        """Stop the feed handler."""
        self._running = False

        # Unsubscribe and close
        if self._fyers_socket:
            try:
                self._fyers_socket.unsubscribe(symbols=self.symbols, data_type="SymbolUpdate")
                if self.on_depth:
                    self._fyers_socket.unsubscribe(symbols=self.symbols, data_type="DepthUpdate")
                self._fyers_socket.close_connection()
            except Exception as e:
                logger.warning("fyers_close_error", error=str(e))
            self._fyers_socket = None

        self._connected = False
        logger.info("fyers_feed_stopped")

    @property
    def is_connected(self) -> bool:
        """Return True if connected."""
        return self._connected
