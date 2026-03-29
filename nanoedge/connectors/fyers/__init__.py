"""Fyers (NSE/India) exchange connector.

Provides multiple WebSocket feed options:
1. FyersFeedHandler - Standard 5-level depth via SDK (easier setup)
2. FyersTBTFeedHandler - 50-level TBT depth via protobuf (single connection, max 5 symbols)
3. FyersTBTConnectionPool - Auto-managed TBT connections (up to 15 symbols across 3 connections)
"""

from nanoedge.connectors.fyers.aggregator import FyersOHLCVAggregator
from nanoedge.connectors.fyers.auth import generate_app_id_hash, generate_auth_url, get_access_token
from nanoedge.connectors.fyers.feed import FyersFeedHandler
from nanoedge.connectors.fyers.rest_client import FyersRestClient
from nanoedge.connectors.fyers.tbt_feed import (
    FyersTBTFeedHandler,
    SymbolDepthState,
    TBT_WS_ENDPOINT,
)
from nanoedge.connectors.fyers.tbt_pool import (
    FyersTBTConnectionPool,
    MAX_CONNECTIONS,
    SYMBOLS_PER_CONNECTION,
)
from nanoedge.connectors.fyers.types import (
    MAX_TBT_DEPTH_LEVELS,
    TBT_DEPTH50_DTYPE,
    TBT_LEVEL_DTYPE,
    TBTChannelSwitch,
    TBTDepth50,
    TBTDepthLevel,
    TBTQuote,
    TBTSubscription,
)

__all__ = [
    # REST client
    "FyersRestClient",
    # Standard WebSocket (5-level depth)
    "FyersFeedHandler",
    # TBT WebSocket (50-level depth) - single connection
    "FyersTBTFeedHandler",
    "SymbolDepthState",
    "TBT_WS_ENDPOINT",
    # TBT Connection Pool - auto-managed multiple connections
    "FyersTBTConnectionPool",
    "MAX_CONNECTIONS",
    "SYMBOLS_PER_CONNECTION",
    # TBT types
    "MAX_TBT_DEPTH_LEVELS",
    "TBT_DEPTH50_DTYPE",
    "TBT_LEVEL_DTYPE",
    "TBTChannelSwitch",
    "TBTDepth50",
    "TBTDepthLevel",
    "TBTQuote",
    "TBTSubscription",
    # OHLCV aggregation
    "FyersOHLCVAggregator",
    # Auth utilities
    "generate_app_id_hash",
    "generate_auth_url",
    "get_access_token",
]
