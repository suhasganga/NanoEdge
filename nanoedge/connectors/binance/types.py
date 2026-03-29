"""Binance-specific data types using msgspec for fast JSON parsing."""

import msgspec


class BinanceAggTrade(msgspec.Struct):
    """
    Binance aggregate trade stream payload (@aggTrade).

    Example:
        {
            "e": "aggTrade",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "a": 12345,
            "p": "50000.00",
            "q": "0.001",
            "f": 100,
            "l": 105,
            "T": 1672515782136,
            "m": true
        }
    """

    e: str  # Event type ("aggTrade")
    E: int  # Event time (ms)
    s: str  # Symbol
    a: int  # Aggregate trade ID
    p: str  # Price (string for precision)
    q: str  # Quantity (string for precision)
    f: int  # First trade ID
    l: int  # Last trade ID
    T: int  # Trade time (ms)
    m: bool  # Is buyer the market maker?


class BinanceKlineData(msgspec.Struct):
    """Nested kline data within kline event."""

    t: int  # Kline start time (ms)
    T: int  # Kline close time (ms)
    s: str  # Symbol
    i: str  # Interval
    f: int  # First trade ID
    L: int  # Last trade ID
    o: str  # Open price
    c: str  # Close price
    h: str  # High price
    l: str  # Low price
    v: str  # Base asset volume
    n: int  # Number of trades
    x: bool  # Is this kline closed?
    q: str  # Quote asset volume
    V: str  # Taker buy base asset volume
    Q: str  # Taker buy quote asset volume


class BinanceKline(msgspec.Struct):
    """
    Binance kline/candlestick stream payload (@kline_1m).

    Example:
        {
            "e": "kline",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "k": { ... }
        }
    """

    e: str  # Event type ("kline")
    E: int  # Event time (ms)
    s: str  # Symbol
    k: BinanceKlineData  # Kline data


class BinanceDepthUpdate(msgspec.Struct):
    """
    Binance depth update stream payload (@depth).

    Example:
        {
            "e": "depthUpdate",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "U": 157,
            "u": 160,
            "b": [["50000.00", "1.5"]],
            "a": [["50001.00", "0.5"]]
        }
    """

    e: str  # Event type ("depthUpdate")
    E: int  # Event time (ms)
    s: str  # Symbol
    U: int  # First update ID in event
    u: int  # Final update ID in event
    b: list[list[str]]  # Bids: [[price, qty], ...]
    a: list[list[str]]  # Asks: [[price, qty], ...]


class BinanceDepthSnapshot(msgspec.Struct):
    """
    Binance REST depth snapshot response (/api/v3/depth).

    Example:
        {
            "lastUpdateId": 160,
            "bids": [["50000.00", "1.5"]],
            "asks": [["50001.00", "0.5"]]
        }
    """

    lastUpdateId: int
    bids: list[list[str]]  # [[price, qty], ...]
    asks: list[list[str]]  # [[price, qty], ...]


class BinanceTicker24h(msgspec.Struct):
    """
    Binance 24hr ticker stream payload (@ticker).

    Example:
        {
            "e": "24hrTicker",
            "E": 1672515782136,
            "s": "BTCUSDT",
            "p": "100.50",
            "P": "0.20",
            "c": "50100.00",
            "o": "50000.00",
            "h": "50500.00",
            "l": "49500.00",
            "v": "10000.5",
            "q": "500000000.00",
            "n": 100000
        }
    """

    e: str  # Event type ("24hrTicker")
    E: int  # Event time (ms)
    s: str  # Symbol
    p: str  # Price change
    P: str  # Price change percent
    c: str  # Last price (close)
    o: str  # Open price
    h: str  # High price
    l: str  # Low price
    v: str  # Total traded base asset volume
    q: str  # Total traded quote asset volume
    n: int  # Total number of trades


class BinanceCombinedStream(msgspec.Struct):
    """
    Wrapper for combined stream messages.

    Example:
        {
            "stream": "btcusdt@aggTrade",
            "data": { ... }
        }
    """

    stream: str
    data: dict  # Raw data, parse based on stream name


# Decoders for fast parsing
agg_trade_decoder = msgspec.json.Decoder(BinanceAggTrade)
kline_decoder = msgspec.json.Decoder(BinanceKline)
depth_update_decoder = msgspec.json.Decoder(BinanceDepthUpdate)
depth_snapshot_decoder = msgspec.json.Decoder(BinanceDepthSnapshot)
ticker_24h_decoder = msgspec.json.Decoder(BinanceTicker24h)
combined_stream_decoder = msgspec.json.Decoder(BinanceCombinedStream)
