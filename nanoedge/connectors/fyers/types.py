"""Fyers API response types using msgspec for fast parsing."""

from __future__ import annotations

import numpy as np
import msgspec


# -----------------------------------------------------------------------------
# TBT (Tick-by-Tick) 50-Depth Types
# -----------------------------------------------------------------------------

# Max depth levels for TBT (Fyers provides up to 50)
MAX_TBT_DEPTH_LEVELS = 50

# NumPy dtype for single depth level (for ring buffer storage)
TBT_LEVEL_DTYPE = np.dtype([
    ("price", "i8"),    # Price in paise (divide by 100 for INR)
    ("qty", "u4"),      # Quantity
    ("orders", "u4"),   # Number of orders at this level
])

# NumPy dtype for full 50-level depth snapshot
TBT_DEPTH50_DTYPE = np.dtype([
    ("timestamp_ns", "u8"),           # Feed timestamp in nanoseconds
    ("symbol_idx", "u2"),             # Index into symbol table
    ("total_buy_qty", "u8"),          # Total bid quantity
    ("total_sell_qty", "u8"),         # Total ask quantity
    ("bid_prices", "i8", (50,)),      # Bid prices (paise)
    ("bid_qtys", "u4", (50,)),        # Bid quantities
    ("bid_orders", "u4", (50,)),      # Bid order counts
    ("ask_prices", "i8", (50,)),      # Ask prices (paise)
    ("ask_qtys", "u4", (50,)),        # Ask quantities
    ("ask_orders", "u4", (50,)),      # Ask order counts
])


class TBTDepthLevel(msgspec.Struct, frozen=True):
    """Single depth level from TBT feed.

    Prices are in paise (1 INR = 100 paise). Divide by 100 for INR.
    """

    price: int      # Price in paise
    qty: int        # Quantity at this level
    orders: int     # Number of orders at this level
    level: int      # Level number (0-49)


class TBTDepth50(msgspec.Struct):
    """50-level depth snapshot from Fyers TBT WebSocket.

    This is the parsed/normalized representation of Fyers protobuf Depth message.
    Maintains full state (snapshot + applied diffs).
    """

    symbol: str                       # Fyers symbol (e.g., "NSE:NIFTY25MARFUT")
    token: str                        # Fyers token for the symbol
    timestamp_ns: int                 # Feed timestamp in nanoseconds
    sequence_no: int                  # Sequence number for ordering
    is_snapshot: bool                 # True if this is a full snapshot

    total_buy_qty: int                # Total bid quantity
    total_sell_qty: int               # Total ask quantity

    # Lists of TBTDepthLevel (up to 50 each)
    bids: list[TBTDepthLevel]
    asks: list[TBTDepthLevel]


class TBTQuote(msgspec.Struct, frozen=True):
    """Quote data from TBT feed (LTP, volume, OI)."""

    ltp: int              # Last traded price (paise)
    ltt: int              # Last traded time (epoch seconds)
    ltq: int              # Last traded quantity
    volume: int           # Volume traded today
    volume_diff: int      # Volume difference from last update
    oi: int               # Open interest
    ltp_change: int       # LTP change from previous close (paise)


class TBTSubscription(msgspec.Struct):
    """TBT subscription request payload."""

    subs: int                    # 1 = subscribe, -1 = unsubscribe
    symbols: list[str]           # Symbol list
    mode: str = "depth"          # "depth" for 50-level depth
    channel: str = "1"           # Channel number (1-50)


class TBTChannelSwitch(msgspec.Struct):
    """TBT channel switch request payload."""

    resumeChannels: list[str]    # Channels to resume
    pauseChannels: list[str]     # Channels to pause


class FyersHistoryResponse(msgspec.Struct):
    """Response from /data/history endpoint."""

    s: str  # "ok" or "error"
    candles: list[list] | None = None  # [[ts, o, h, l, c, v], ...]
    code: int | None = None
    message: str | None = None
    nextTime: int | None = None  # Hint: last available data timestamp (epoch seconds)


class FyersQuoteData(msgspec.Struct):
    """Individual quote data from /data/quotes."""

    n: str  # Symbol name
    s: str  # Short name
    v: dict  # Quote values


class FyersQuotesResponse(msgspec.Struct):
    """Response from /data/quotes endpoint."""

    s: str  # "ok" or "error"
    d: list[FyersQuoteData] | None = None
    code: int | None = None
    message: str | None = None


class FyersDepthLevel(msgspec.Struct):
    """Single depth level."""

    price: float
    quantity: int
    orders: int


class FyersDepthData(msgspec.Struct):
    """Market depth data."""

    totalbuyqty: int
    totalsellqty: int
    bids: list[FyersDepthLevel]
    ask: list[FyersDepthLevel]


class FyersDepthResponse(msgspec.Struct):
    """Response from /data/depth endpoint."""

    s: str  # "ok" or "error"
    d: dict | None = None
    code: int | None = None
    message: str | None = None


class FyersTokenResponse(msgspec.Struct):
    """Response from /api/v3/validate-authcode."""

    s: str  # "ok" or "error"
    access_token: str | None = None
    refresh_token: str | None = None
    code: int | None = None
    message: str | None = None


# Decoders for fast parsing
history_decoder = msgspec.json.Decoder(FyersHistoryResponse)
quotes_decoder = msgspec.json.Decoder(FyersQuotesResponse)
depth_decoder = msgspec.json.Decoder(FyersDepthResponse)
token_decoder = msgspec.json.Decoder(FyersTokenResponse)


# Resolution mapping: internal format → Fyers API format
# Fyers supports sub-second, minute, hourly, and daily resolutions
RESOLUTION_MAP = {
    # Sub-second resolutions
    "5s": "5S",
    "10s": "10S",
    "15s": "15S",
    "30s": "30S",
    "45s": "45S",
    # Minute resolutions
    "1m": "1",
    "2m": "2",
    "3m": "3",
    "5m": "5",
    "10m": "10",
    "15m": "15",
    "20m": "20",
    "30m": "30",
    "45m": "45",
    # Hourly resolutions
    "1h": "60",
    "2h": "120",
    "3h": "180",
    "4h": "240",
    # Daily resolution
    "1d": "D",
    "1D": "D",  # Alternative casing
}

# Reverse mapping for converting Fyers format to internal
RESOLUTION_MAP_REVERSE = {v: k for k, v in RESOLUTION_MAP.items()}
