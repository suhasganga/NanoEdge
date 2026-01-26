"""Binance market data feed handler for trades and klines."""

import time
from collections.abc import Callable

import msgspec
import structlog

from hft.connectors.binance.types import (
    BinanceAggTrade,
    BinanceKlineData,
    BinanceTicker24h,
    combined_stream_decoder,
)
from hft.connectors.binance.ws_client import BinanceWebSocketClient
from hft.core.metrics import metrics
from hft.core.types import OHLCV, MarketStats, MarketTick, Trade

logger = structlog.get_logger(__name__)

# Type aliases
TickCallback = Callable[[MarketTick], None]
KlineCallback = Callable[[OHLCV], None]
TradeCallback = Callable[[Trade], None]
StatsCallback = Callable[[MarketStats], None]


class BinanceFeedHandler:
    """
    Combined feed handler for multiple symbols.

    Subscribes to:
    - @aggTrade streams for real-time tick data
    - @kline_1m streams for candle updates

    Uses combined stream endpoint for efficiency.
    """

    __slots__ = (
        "symbols",
        "on_tick",
        "on_kline",
        "on_trade",
        "on_stats",
        "url",
        "_ws_client",
        "_tick_count",
        "_kline_count",
        "_last_stats_time",
    )

    def __init__(
        self,
        symbols: list[str],
        on_tick: TickCallback,
        on_kline: KlineCallback,
        on_trade: TradeCallback | None = None,
        on_stats: StatsCallback | None = None,
        base_url: str = "wss://stream.binance.com:9443",
    ):
        """
        Initialize feed handler.

        Args:
            symbols: List of trading pairs (e.g., ["BTCUSDT", "ETHUSDT"])
            on_tick: Callback for each trade tick
            on_kline: Callback for kline updates
            on_trade: Optional callback for individual trades (for recent trades)
            on_stats: Optional callback for 24h market stats
            base_url: Binance WebSocket base URL
        """
        self.symbols = [s.upper() for s in symbols]
        self.on_tick = on_tick
        self.on_kline = on_kline
        self.on_trade = on_trade
        self.on_stats = on_stats

        # Build combined stream URL
        streams = []
        for sym in self.symbols:
            sym_lower = sym.lower()
            streams.append(f"{sym_lower}@aggTrade")
            streams.append(f"{sym_lower}@kline_1m")
            streams.append(f"{sym_lower}@ticker")

        stream_path = "/".join(streams)
        self.url = f"{base_url}/stream?streams={stream_path}"

        self._ws_client = BinanceWebSocketClient(
            url=self.url,
            on_message=self._handle_message,
            on_connect=self._on_connect,
        )

        # Stats
        self._tick_count = 0
        self._kline_count = 0
        self._last_stats_time = time.time()

    async def _on_connect(self) -> None:
        """Log connection info."""
        logger.info(
            "feed_connected",
            symbols=self.symbols,
            stream_count=len(self.symbols) * 3,  # aggTrade, kline, ticker per symbol
        )

    async def _handle_message(self, raw: bytes) -> None:
        """Parse and route incoming messages."""
        recv_ns = time.time_ns()  # T1: receive time
        recv_ts_ms = recv_ns // 1_000_000  # Convert to milliseconds for types

        try:
            # Parse combined stream wrapper using typed decoder
            msg = combined_stream_decoder.decode(raw)
            parse_ns = time.time_ns()  # T2: parse complete

            # Record parse latency (nanoseconds to microseconds)
            metrics.parse_json_latency.record((parse_ns - recv_ns) / 1000)

            stream_name = msg.stream
            data = msg.data

            if "@aggTrade" in stream_name:
                self._process_agg_trade(data, recv_ts_ms)
            elif "@kline" in stream_name:
                self._process_kline(data, recv_ts_ms)
            elif "@ticker" in stream_name:
                self._process_ticker(data, recv_ts_ms)

            # Log stats periodically (includes latency metrics)
            self._maybe_log_stats()
            metrics.maybe_log_stats()

        except msgspec.DecodeError as e:
            logger.error(
                "message_decode_error",
                error=str(e),
                raw=raw[:200].decode("utf-8", errors="replace"),
            )
        except Exception as e:
            logger.error(
                "message_handle_error",
                error=str(e),
                raw=raw[:200].decode("utf-8", errors="replace"),
            )

    def _process_agg_trade(self, data: dict, recv_ts_ms: int) -> None:
        """Convert Binance aggTrade to MarketTick and Trade."""
        try:
            # Use msgspec.convert for efficient dict → struct conversion
            agg_trade = msgspec.convert(data, BinanceAggTrade)

            # Convert string prices to float once
            price = float(agg_trade.p)
            quantity = float(agg_trade.q)

            tick = MarketTick(
                timestamp_ns=agg_trade.T * 1_000_000,  # ms to ns
                exchange="binance",
                market="spot",
                symbol=agg_trade.s,
                price=price,
                volume=quantity,
                # m=True means buyer is maker, so the trade was a sell
                side=-1 if agg_trade.m else 1,
                recv_ts_ms=recv_ts_ms,  # T1: Server receive time
            )

            self._tick_count += 1
            self.on_tick(tick)

            # Also emit Trade for recent trades display (reuse converted values)
            if self.on_trade:
                trade = Trade(
                    timestamp_ms=agg_trade.T,
                    exchange="binance",
                    market="spot",
                    symbol=agg_trade.s,
                    price=price,
                    quantity=quantity,
                    is_buyer_maker=agg_trade.m,
                    trade_id=agg_trade.a,
                    recv_ts_ms=recv_ts_ms,  # T1: Server receive time
                )
                self.on_trade(trade)

        except msgspec.ValidationError as e:
            logger.error("agg_trade_validation_error", error=str(e), data=data)
        except Exception as e:
            logger.error("agg_trade_process_error", error=str(e), data=data)

    def _process_kline(self, data: dict, recv_ts_ms: int) -> None:
        """Convert Binance kline to OHLCV."""
        try:
            # Use msgspec.convert for nested kline data
            k = msgspec.convert(data["k"], BinanceKlineData)

            ohlcv = OHLCV(
                timestamp=k.t,  # Kline start time (ms)
                exchange="binance",
                market="spot",
                symbol=data["s"],
                open=float(k.o),
                high=float(k.h),
                low=float(k.l),
                close=float(k.c),
                volume=float(k.v),
                trade_count=k.n,
                vwap=0.0,  # Binance doesn't provide VWAP
                is_closed=k.x,
                recv_ts_ms=recv_ts_ms,  # T1: Server receive time
            )

            self._kline_count += 1
            self.on_kline(ohlcv)

        except msgspec.ValidationError as e:
            logger.error("kline_validation_error", error=str(e), data=data)
        except Exception as e:
            logger.error("kline_process_error", error=str(e), data=data)

    def _process_ticker(self, data: dict, recv_ts_ms: int) -> None:
        """Convert Binance 24hr ticker to MarketStats."""
        if not self.on_stats:
            return

        try:
            # Use msgspec.convert for efficient dict → struct conversion
            ticker = msgspec.convert(data, BinanceTicker24h)

            stats = MarketStats(
                timestamp_ms=ticker.E,
                exchange="binance",
                market="spot",
                symbol=ticker.s,
                price_change=float(ticker.p),
                price_change_percent=float(ticker.P),
                high_24h=float(ticker.h),
                low_24h=float(ticker.l),
                volume_24h=float(ticker.v),
                quote_volume_24h=float(ticker.q),
                trade_count_24h=ticker.n,
                last_price=float(ticker.c),
                open_price=float(ticker.o),
                recv_ts_ms=recv_ts_ms,  # T1: Server receive time
            )

            self.on_stats(stats)

        except msgspec.ValidationError as e:
            logger.error("ticker_validation_error", error=str(e), data=data)
        except Exception as e:
            logger.error("ticker_process_error", error=str(e), data=data)

    def _maybe_log_stats(self) -> None:
        """Log stats every 60 seconds."""
        now = time.time()
        if now - self._last_stats_time >= 60:
            logger.info(
                "feed_stats",
                ticks_received=self._tick_count,
                klines_received=self._kline_count,
                symbols=len(self.symbols),
            )
            self._tick_count = 0
            self._kline_count = 0
            self._last_stats_time = now

    async def start(self) -> None:
        """Start the feed handler."""
        logger.info("feed_starting", symbols=self.symbols)
        await self._ws_client.start()

    async def stop(self) -> None:
        """Stop the feed handler."""
        await self._ws_client.stop()
        logger.info("feed_stopped")

    @property
    def is_connected(self) -> bool:
        """Return True if connected."""
        return self._ws_client.is_connected
