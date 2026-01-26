"""
On-demand subscription manager for multi-exchange market data.

When user selects a symbol:
1. Unsubscribe from previous symbol (if different exchange/symbol)
2. Subscribe to new symbol's streams
3. Start receiving data through callbacks

Supports caching last N symbols for quick switching.
"""

from __future__ import annotations

import asyncio
import time
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable

import structlog

from hft.config import settings
from hft.core.types import OHLCV, MarketStats, MarketTick, OrderBookSnapshot, Trade

if TYPE_CHECKING:
    from hft.connectors.binance.feed import BinanceFeedHandler
    from hft.connectors.fyers.feed import FyersFeedHandler

logger = structlog.get_logger(__name__)

# Type aliases for callbacks
TickCallback = Callable[[MarketTick], None]
KlineCallback = Callable[[OHLCV], None]
DepthCallback = Callable[[OrderBookSnapshot], None]
TradeCallback = Callable[[Trade], None]
StatsCallback = Callable[[MarketStats], None]


@dataclass
class ActiveSubscription:
    """Tracks an active symbol subscription."""

    exchange: str
    market: str
    symbol: str
    subscribed_at: float
    streams: list[str] = field(default_factory=list)
    feed_handler: BinanceFeedHandler | FyersFeedHandler | None = None

    @property
    def key(self) -> str:
        """Unique subscription key."""
        return f"{self.exchange}:{self.market}:{self.symbol}"


class SubscriptionManager:
    """
    Manages on-demand subscriptions across exchanges.

    Features:
    - Subscribe to single symbol at a time (TradingView-style)
    - Cache last N symbols for quick switching
    - Automatic unsubscribe when switching
    - Callbacks for tick/kline/depth/trade/stats data
    """

    def __init__(
        self,
        on_tick: TickCallback | None = None,
        on_kline: KlineCallback | None = None,
        on_depth: DepthCallback | None = None,
        on_trade: TradeCallback | None = None,
        on_stats: StatsCallback | None = None,
        max_cached_symbols: int = 5,
    ):
        """
        Initialize subscription manager.

        Args:
            on_tick: Callback for tick data
            on_kline: Callback for candle updates
            on_depth: Callback for order book updates
            on_trade: Callback for individual trades
            on_stats: Callback for 24h market stats
            max_cached_symbols: Max symbols to keep in cache
        """
        self.on_tick = on_tick
        self.on_kline = on_kline
        self.on_depth = on_depth
        self.on_trade = on_trade
        self.on_stats = on_stats
        self.max_cached_symbols = max_cached_symbols

        # Current active subscription
        self._active: ActiveSubscription | None = None

        # LRU cache of recent subscriptions (key → subscription)
        self._cached: OrderedDict[str, ActiveSubscription] = OrderedDict()

        # Lock for subscription operations
        self._lock = asyncio.Lock()

    @property
    def current_symbol(self) -> tuple[str, str, str] | None:
        """Get current active symbol as (exchange, market, symbol) or None."""
        if self._active:
            return (self._active.exchange, self._active.market, self._active.symbol)
        return None

    @property
    def is_subscribed(self) -> bool:
        """Check if there's an active subscription."""
        return self._active is not None

    def _validate_and_correct_exchange(
        self, exchange: str, market: str, symbol: str
    ) -> tuple[str, str]:
        """
        Validate and auto-correct exchange/market based on symbol format.

        NSE:*, MCX:*, BSE:* symbols should use Fyers, not Binance.
        """
        symbol_upper = symbol.upper()

        # NSE/MCX/BSE symbols must use Fyers
        if symbol_upper.startswith(("NSE:", "MCX:", "BSE:")):
            if exchange != "fyers":
                logger.warning(
                    "exchange_auto_corrected",
                    original_exchange=exchange,
                    corrected_exchange="fyers",
                    symbol=symbol,
                )
                exchange = "fyers"

            # Auto-correct market based on symbol suffix
            if "-EQ" in symbol_upper:
                market = "equity"
            elif "-INDEX" in symbol_upper:
                market = "index"
            elif symbol_upper.startswith("MCX:"):
                market = "commodity"
            elif "FUT" in symbol_upper or "CE" in symbol_upper or "PE" in symbol_upper:
                market = "futures" if "FUT" in symbol_upper else "options"

        return exchange, market

    async def subscribe(
        self,
        exchange: str,
        market: str,
        symbol: str,
    ) -> bool:
        """
        Subscribe to a symbol's market data.

        Args:
            exchange: Exchange name ("binance" or "fyers")
            market: Market type ("spot", "futures", "equity", etc.)
            symbol: Symbol name

        Returns:
            True if subscription successful, False otherwise
        """
        async with self._lock:
            # Auto-correct exchange/market based on symbol format
            exchange, market = self._validate_and_correct_exchange(exchange, market, symbol)
            key = f"{exchange}:{market}:{symbol}"

            # Check if already subscribed to this exact symbol
            if self._active and self._active.key == key:
                logger.debug("already_subscribed", symbol=key)
                return True

            # Clean up any cached entries for the same symbol but different exchange/market
            # This prevents stale cache entries from accumulating
            stale_keys = [
                k for k in self._cached
                if k.endswith(f":{symbol}") and k != key
            ]
            for stale_key in stale_keys:
                stale_sub = self._cached.pop(stale_key)
                await self._stop_subscription(stale_sub)
                logger.info("stale_cache_cleaned", removed_key=stale_key, current_key=key)

            # Check cache for quick restore
            if key in self._cached:
                logger.info("restoring_cached_subscription", symbol=key)
                # Move from cache to active
                cached_sub = self._cached.pop(key)

                # Move current active to cache
                if self._active:
                    await self._move_to_cache(self._active)

                self._active = cached_sub
                return True

            # Need to create new subscription
            logger.info(
                "subscribing",
                exchange=exchange,
                market=market,
                symbol=symbol,
            )

            # Move current active to cache
            if self._active:
                await self._move_to_cache(self._active)

            # Create new subscription
            try:
                feed_handler = await self._create_feed_handler(exchange, market, symbol)

                self._active = ActiveSubscription(
                    exchange=exchange,
                    market=market,
                    symbol=symbol,
                    subscribed_at=time.time(),
                    streams=self._get_streams(exchange, market),
                    feed_handler=feed_handler,
                )

                # Start the feed handler
                if feed_handler:
                    await feed_handler.start()

                logger.info("subscribed", symbol=key)
                return True

            except Exception as e:
                logger.error(
                    "subscription_failed",
                    exchange=exchange,
                    symbol=symbol,
                    error=str(e),
                )
                return False

    async def unsubscribe(self) -> None:
        """Unsubscribe from current symbol."""
        async with self._lock:
            if self._active:
                await self._stop_subscription(self._active)
                self._active = None
                logger.info("unsubscribed")

    async def unsubscribe_all(self) -> None:
        """Unsubscribe from all symbols (active + cached)."""
        async with self._lock:
            # Stop active
            if self._active:
                await self._stop_subscription(self._active)
                self._active = None

            # Stop all cached
            for sub in list(self._cached.values()):
                await self._stop_subscription(sub)
            self._cached.clear()

            logger.info("all_subscriptions_cleared")

    async def _create_feed_handler(
        self,
        exchange: str,
        market: str,
        symbol: str,
    ) -> BinanceFeedHandler | FyersFeedHandler | None:
        """
        Create appropriate feed handler for exchange.

        Returns feed handler or None if exchange not supported.
        """
        if exchange == "binance":
            return await self._create_binance_handler(market, symbol)
        elif exchange == "fyers":
            return await self._create_fyers_handler(market, symbol)
        else:
            logger.error("unsupported_exchange", exchange=exchange)
            return None

    async def _create_binance_handler(
        self,
        market: str,
        symbol: str,
    ) -> BinanceFeedHandler:
        """Create Binance feed handler for symbol."""
        from hft.connectors.binance.feed import BinanceFeedHandler

        # Determine base URL based on market type
        if market == "spot":
            base_url = "wss://stream.binance.com:9443"
        elif market in ("futures", "perp_linear", "future_linear"):
            base_url = "wss://fstream.binance.com"
        elif market in ("coin_futures", "perp_inverse", "future_inverse"):
            base_url = "wss://dstream.binance.com"
        else:
            base_url = "wss://stream.binance.com:9443"

        handler = BinanceFeedHandler(
            symbols=[symbol],
            on_tick=self._handle_tick,
            on_kline=self._handle_kline,
            on_trade=self._handle_trade,
            on_stats=self._handle_stats,
            base_url=base_url,
        )

        return handler

    async def _create_fyers_handler(
        self,
        market: str,
        symbol: str,
    ) -> FyersFeedHandler | None:
        """Create Fyers feed handler for symbol."""
        from hft.connectors.fyers.feed import FyersFeedHandler

        # Check for required credentials
        if not settings.fyers_app_id or not settings.fyers_access_token:
            logger.warning(
                "fyers_credentials_missing",
                has_app_id=bool(settings.fyers_app_id),
                has_token=bool(settings.fyers_access_token),
            )
            return None

        handler = FyersFeedHandler(
            app_id=settings.fyers_app_id,
            access_token=settings.fyers_access_token,
            symbols=[symbol],
            on_tick=self._handle_tick,
            on_kline=self._handle_kline,
            on_depth=self._handle_depth,
            on_trade=self._handle_trade,
            on_stats=self._handle_stats,
        )

        return handler

    async def _move_to_cache(self, sub: ActiveSubscription) -> None:
        """Move subscription to cache (keep connection for quick restore)."""
        key = sub.key

        # Evict oldest if cache full
        if len(self._cached) >= self.max_cached_symbols:
            oldest_key, oldest_sub = self._cached.popitem(last=False)
            await self._stop_subscription(oldest_sub)
            logger.debug("cache_evicted", symbol=oldest_key)

        self._cached[key] = sub
        logger.debug("subscription_cached", symbol=key)

    async def _stop_subscription(self, sub: ActiveSubscription) -> None:
        """Stop a subscription's feed handler."""
        if sub.feed_handler:
            try:
                await sub.feed_handler.stop()
            except Exception as e:
                logger.error(
                    "stop_subscription_error",
                    symbol=sub.key,
                    error=str(e),
                )

    def _get_streams(self, exchange: str, market: str) -> list[str]:
        """Get stream names for exchange/market combination."""
        if exchange == "binance":
            if market == "spot":
                return ["aggTrade", "kline_1m", "depth@100ms", "ticker"]
            elif market in ("futures", "perp_linear", "future_linear"):
                return ["aggTrade", "kline_1m", "depth@100ms", "markPrice"]
            elif market in ("coin_futures", "perp_inverse", "future_inverse"):
                return ["aggTrade", "kline_1m", "depth@100ms", "markPrice"]
        elif exchange == "fyers":
            return ["symbol", "depth"]  # Fyers stream names

        return []

    def _handle_tick(self, tick: MarketTick) -> None:
        """Handle incoming tick data."""
        if self.on_tick:
            self.on_tick(tick)

    def _handle_kline(self, kline: OHLCV) -> None:
        """Handle incoming kline data."""
        if self.on_kline:
            self.on_kline(kline)

    def _handle_depth(self, depth: OrderBookSnapshot) -> None:
        """Handle incoming depth data."""
        if self.on_depth:
            self.on_depth(depth)

    def _handle_trade(self, trade: Trade) -> None:
        """Handle incoming trade data."""
        if self.on_trade:
            self.on_trade(trade)

    def _handle_stats(self, stats: MarketStats) -> None:
        """Handle incoming stats data."""
        if self.on_stats:
            self.on_stats(stats)

    def get_cached_symbols(self) -> list[tuple[str, str, str]]:
        """Get list of cached symbols as (exchange, market, symbol) tuples."""
        return [(s.exchange, s.market, s.symbol) for s in self._cached.values()]
