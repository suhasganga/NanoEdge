"""msgspec types for WebSocket output messages.

Pre-compiled encoders for high-performance JSON serialization.
Using msgspec provides 2-5x faster serialization compared to FastAPI's send_json().
"""

import msgspec


class HeartbeatMsg(msgspec.Struct, frozen=True):
    """Heartbeat message sent to keep WebSocket connections alive."""

    type: str = "heartbeat"


class TickMsg(msgspec.Struct):
    """Real-time tick data message."""

    type: str
    symbol: str
    price: float
    volume: float
    side: int
    timestamp: int  # T0: Exchange event time (ms)
    recv_ts: int = 0  # T1: Server received from exchange WS (ms)
    api_ts: int = 0  # T3: API push initiated (ms)


class DepthMsg(msgspec.Struct):
    """Order book depth update message."""

    type: str
    symbol: str
    bids: list[list[float]]  # [[price, size], ...]
    asks: list[list[float]]
    lastUpdateId: int
    exch_ts: int = 0  # T0: Exchange event time (ms)
    recv_ts: int = 0  # T1: Server received from exchange WS (ms)
    api_ts: int = 0  # T3: API push initiated (ms)


class TradeMsg(msgspec.Struct):
    """Individual trade message for recent trades feed."""

    type: str
    symbol: str
    price: float
    quantity: float
    is_buyer_maker: bool
    timestamp: int  # T0: Exchange event time (ms)
    trade_id: int
    recv_ts: int = 0  # T1: Server received from exchange WS (ms)
    api_ts: int = 0  # T3: API push initiated (ms)


class StatsMsg(msgspec.Struct):
    """24h market statistics message."""

    type: str
    symbol: str
    price_change: float
    price_change_percent: float
    high_24h: float
    low_24h: float
    volume_24h: float
    quote_volume_24h: float
    trade_count_24h: int
    last_price: float
    open_price: float
    exch_ts: int = 0  # T0: Exchange event time (ms)
    recv_ts: int = 0  # T1: Server received from exchange WS (ms)
    api_ts: int = 0  # T3: API push initiated (ms)


class CandleMsg(msgspec.Struct):
    """OHLCV candle message."""

    type: str
    time: int  # Candle open time (seconds for TradingView)
    open: float
    high: float
    low: float
    close: float
    volume: float
    closed: bool = False
    exch_ts: int = 0  # T0: Exchange event time (ms) - kline event time
    recv_ts: int = 0  # T1: Server received from exchange WS (ms)
    api_ts: int = 0  # T3: API push initiated (ms)


class SubscribedMsg(msgspec.Struct):
    """Subscription confirmation message."""

    type: str
    exchange: str
    market: str
    symbol: str


class UnsubscribedMsg(msgspec.Struct, frozen=True):
    """Unsubscription confirmation message."""

    type: str = "unsubscribed"


# Pre-compiled encoder (single instance for all message types)
# msgspec.json.Encoder() can encode any msgspec.Struct
encoder = msgspec.json.Encoder()

# Pre-computed singleton bytes for static messages (avoid repeated encoding)
HEARTBEAT_BYTES = encoder.encode(HeartbeatMsg())
UNSUBSCRIBED_BYTES = encoder.encode(UnsubscribedMsg())

# Pre-decoded text versions for WebSocket send_text() (frontend expects text, not binary)
HEARTBEAT_TEXT = HEARTBEAT_BYTES.decode("utf-8")
UNSUBSCRIBED_TEXT = UNSUBSCRIBED_BYTES.decode("utf-8")


def encode_tick(
    symbol: str,
    price: float,
    volume: float,
    side: int,
    timestamp: int,
    recv_ts: int = 0,
    api_ts: int = 0,
) -> bytes:
    """Encode a tick message to JSON bytes."""
    return encoder.encode(
        TickMsg(
            type="tick",
            symbol=symbol,
            price=price,
            volume=volume,
            side=side,
            timestamp=timestamp,
            recv_ts=recv_ts,
            api_ts=api_ts,
        )
    )


def encode_depth(
    symbol: str,
    bids: list[list[float]],
    asks: list[list[float]],
    last_update_id: int,
    exch_ts: int = 0,
    recv_ts: int = 0,
    api_ts: int = 0,
) -> bytes:
    """Encode a depth message to JSON bytes."""
    return encoder.encode(
        DepthMsg(
            type="depth",
            symbol=symbol,
            bids=bids,
            asks=asks,
            lastUpdateId=last_update_id,
            exch_ts=exch_ts,
            recv_ts=recv_ts,
            api_ts=api_ts,
        )
    )


def encode_trade(
    symbol: str,
    price: float,
    quantity: float,
    is_buyer_maker: bool,
    timestamp: int,
    trade_id: int,
    recv_ts: int = 0,
    api_ts: int = 0,
) -> bytes:
    """Encode a trade message to JSON bytes."""
    return encoder.encode(
        TradeMsg(
            type="trade",
            symbol=symbol,
            price=price,
            quantity=quantity,
            is_buyer_maker=is_buyer_maker,
            timestamp=timestamp,
            trade_id=trade_id,
            recv_ts=recv_ts,
            api_ts=api_ts,
        )
    )


def encode_stats(
    symbol: str,
    price_change: float,
    price_change_percent: float,
    high_24h: float,
    low_24h: float,
    volume_24h: float,
    quote_volume_24h: float,
    trade_count_24h: int,
    last_price: float,
    open_price: float,
    exch_ts: int = 0,
    recv_ts: int = 0,
    api_ts: int = 0,
) -> bytes:
    """Encode a stats message to JSON bytes."""
    return encoder.encode(
        StatsMsg(
            type="stats",
            symbol=symbol,
            price_change=price_change,
            price_change_percent=price_change_percent,
            high_24h=high_24h,
            low_24h=low_24h,
            volume_24h=volume_24h,
            quote_volume_24h=quote_volume_24h,
            trade_count_24h=trade_count_24h,
            last_price=last_price,
            open_price=open_price,
            exch_ts=exch_ts,
            recv_ts=recv_ts,
            api_ts=api_ts,
        )
    )


def encode_candle(
    time: int,
    open: float,
    high: float,
    low: float,
    close: float,
    volume: float,
    closed: bool = False,
    exch_ts: int = 0,
    recv_ts: int = 0,
    api_ts: int = 0,
) -> bytes:
    """Encode a candle message to JSON bytes."""
    return encoder.encode(
        CandleMsg(
            type="candle",
            time=time,
            open=open,
            high=high,
            low=low,
            close=close,
            volume=volume,
            closed=closed,
            exch_ts=exch_ts,
            recv_ts=recv_ts,
            api_ts=api_ts,
        )
    )


def encode_subscribed(exchange: str, market: str, symbol: str) -> bytes:
    """Encode a subscribed confirmation message to JSON bytes."""
    return encoder.encode(
        SubscribedMsg(
            type="subscribed",
            exchange=exchange,
            market=market,
            symbol=symbol,
        )
    )
