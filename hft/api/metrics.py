"""Metrics API endpoint for latency statistics."""

from fastapi import APIRouter

from hft.core.clock_sync import clock_sync_registry
from hft.core.metrics import metrics

router = APIRouter()


@router.get("/metrics")
async def get_metrics():
    """
    Get server-side latency metrics.

    Returns percentile statistics for all tracked histograms:
    - ws_network: WebSocket network latency
    - parse_json: JSON parsing latency
    - parse_protobuf: Protobuf parsing latency
    - normalize: Data normalization latency
    - agg_update: Aggregator update latency
    - api_ws_push: API WebSocket push latency
    - db_write: Database write latency
    - orderbook_update: Order book update latency

    Also includes per-exchange clock_sync info:
    - binance: {offset_ms, rtt_ms}
    - fyers: {offset_ms, rtt_ms}
    """
    stats = metrics.get_all_stats()
    stats["clock_sync"] = clock_sync_registry.get_all_offsets()
    return stats
