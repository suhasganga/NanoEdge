"""Core data types for the HFT platform."""

from dataclasses import dataclass
from enum import Enum
from typing import Literal

import numpy as np

# Exchange identifiers
Exchange = Literal["binance", "fyers"]

# Market types
Market = Literal["spot", "futures", "options", "equity", "index", "currency", "commodity"]


class InstrumentType(str, Enum):
    """Classification of trading instruments across exchanges."""

    # Binance
    SPOT = "spot"  # BTCUSDT spot
    PERP_LINEAR = "perp_linear"  # BTCUSDT perpetual (USDT-M)
    PERP_INVERSE = "perp_inverse"  # BTCUSD perpetual (COIN-M)
    FUTURE_LINEAR = "future_linear"  # BTCUSDT_250328 quarterly
    FUTURE_INVERSE = "future_inverse"
    OPTION_CALL = "option_call"
    OPTION_PUT = "option_put"

    # NSE/Fyers
    EQUITY = "equity"  # RELIANCE-EQ
    INDEX = "index"  # NIFTY50-INDEX
    EQUITY_FUTURE = "equity_future"  # RELIANCE25MARFUT
    EQUITY_OPTION_CE = "equity_option_ce"
    EQUITY_OPTION_PE = "equity_option_pe"
    INDEX_FUTURE = "index_future"  # NIFTY25MARFUT
    INDEX_OPTION_CE = "index_option_ce"
    INDEX_OPTION_PE = "index_option_pe"
    CURRENCY_FUTURE = "currency_future"
    CURRENCY_OPTION_CE = "currency_option_ce"
    CURRENCY_OPTION_PE = "currency_option_pe"
    COMMODITY_FUTURE = "commodity_future"
    COMMODITY_OPTION_CE = "commodity_option_ce"
    COMMODITY_OPTION_PE = "commodity_option_pe"

# NumPy dtypes for ring buffer storage
TICK_DTYPE = np.dtype(
    [
        ("timestamp_ns", "u8"),  # Nanoseconds since epoch
        ("symbol_idx", "u2"),  # Index into symbol table (max 65535 symbols)
        ("price", "f8"),  # Last trade price
        ("volume", "f8"),  # Trade volume
        ("side", "i1"),  # 1=buy, -1=sell, 0=unknown
    ]
)

OHLCV_DTYPE = np.dtype(
    [
        ("timestamp", "u8"),  # Candle open time (epoch ms)
        ("exchange_idx", "u1"),  # Index into exchange table (0=binance, 1=fyers)
        ("market_idx", "u1"),  # Index into market table
        ("symbol_idx", "u2"),
        ("open", "f8"),
        ("high", "f8"),
        ("low", "f8"),
        ("close", "f8"),
        ("volume", "f8"),
        ("quote_volume", "f8"),
        ("trade_count", "u4"),
        ("vwap", "f8"),
    ]
)


@dataclass(slots=True)
class SymbolInfo:
    """Symbol metadata for search and display."""

    symbol: str  # BTCUSDT, NSE:RELIANCE-EQ
    exchange: str  # "binance" or "fyers"
    market: str  # "spot", "futures", "equity", etc.
    base_asset: str  # BTC, RELIANCE
    quote_asset: str  # USDT, INR
    description: str  # "Bitcoin / TetherUS"
    instrument_type: str  # InstrumentType value

    # Optional derivative fields
    contract_type: str | None = None  # "perpetual", "quarterly", "monthly"
    expiry_date: str | None = None  # "2025-03-28"
    strike_price: float | None = None
    option_type: str | None = None  # "call" or "put"
    underlying: str | None = None  # "BTCUSDT" for options

    # Trading params
    tick_size: float = 0.01
    lot_size: float = 1.0
    min_notional: float | None = None
    is_trading: bool = True


@dataclass(slots=True)
class MarketTick:
    """Normalized tick data from any exchange."""

    timestamp_ns: int  # Nanoseconds since epoch (T0: exchange event time)
    exchange: str  # "binance" or "fyers"
    market: str  # "spot", "futures", "equity", etc.
    symbol: str
    price: float
    volume: float
    side: int  # 1=buy, -1=sell, 0=unknown
    recv_ts_ms: int = 0  # T1: Server received from exchange WS (ms)


@dataclass(slots=True)
class OHLCV:
    """OHLCV candle data."""

    timestamp: int  # Candle open time in milliseconds (T0: exchange event time)
    exchange: str  # "binance" or "fyers"
    market: str  # "spot", "futures", "equity", etc.
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    quote_volume: float = 0.0  # Quote asset volume (for crypto pairs)
    trade_count: int = 0
    vwap: float = 0.0
    is_closed: bool = False
    recv_ts_ms: int = 0  # T1: Server received from exchange WS (ms)


@dataclass(slots=True)
class DepthLevel:
    """Single price level in order book."""

    price: float
    size: float


@dataclass(slots=True)
class OrderBookSnapshot:
    """Order book snapshot with top N levels."""

    timestamp_ms: int  # T0: Exchange event time (ms)
    exchange: str  # "binance" or "fyers"
    market: str  # "spot", "futures", "equity", etc.
    symbol: str
    bids: list[DepthLevel]  # Sorted descending by price
    asks: list[DepthLevel]  # Sorted ascending by price
    last_update_id: int
    recv_ts_ms: int = 0  # T1: Server received from exchange WS (ms)


@dataclass(slots=True)
class Trade:
    """Individual trade for recent trades display."""

    timestamp_ms: int  # T0: Exchange event time (ms)
    exchange: str  # "binance" or "fyers"
    market: str  # "spot", "futures", "equity", etc.
    symbol: str
    price: float
    quantity: float
    is_buyer_maker: bool  # True = sell (red), False = buy (green)
    trade_id: int
    recv_ts_ms: int = 0  # T1: Server received from exchange WS (ms)


@dataclass(slots=True)
class MarketStats:
    """24h rolling window market statistics."""

    timestamp_ms: int  # T0: Exchange event time (ms)
    exchange: str  # "binance" or "fyers"
    market: str  # "spot", "futures", "equity", etc.
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
    recv_ts_ms: int = 0  # T1: Server received from exchange WS (ms)
