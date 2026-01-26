"""Symbol search API endpoints."""

from fastapi import APIRouter, HTTPException, Query

from hft.symbols.service import get_symbol_service
from hft.symbols.types import FILTER_PRESETS

router = APIRouter(prefix="/api/symbols", tags=["symbols"])


@router.get("")
async def get_symbols(
    exchange: str | None = Query(None, description="Filter by exchange (binance, fyers)"),
    market: str | None = Query(None, description="Filter by market (spot, futures, equity, etc.)"),
    types: str | None = Query(
        None,
        description="Comma-separated instrument types (spot, futures, options, stocks, index_fo, etc.)",
    ),
    limit: int = Query(500, ge=1, le=5000, description="Max results"),
):
    """
    Get available symbols for trading.

    Returns a simple list of symbols suitable for dropdown population.
    Use /api/symbols/search for full-text search with autocomplete.

    Examples:
    - /api/symbols → All symbols (default limit 500)
    - /api/symbols?exchange=binance → Binance symbols only
    - /api/symbols?exchange=binance&market=spot → Binance spot pairs
    - /api/symbols?exchange=fyers&types=stocks → NSE equities
    - /api/symbols?types=futures → All futures across exchanges
    """
    service = get_symbol_service()

    # Resolve types filter
    instrument_types: list[str] | None = None
    if types:
        if types in FILTER_PRESETS:
            instrument_types = FILTER_PRESETS[types]
        else:
            instrument_types = [t.strip() for t in types.split(",") if t.strip()]

    # Get all symbols matching filters
    results = service.get_all(
        exchange=exchange,
        market=market,
        instrument_types=instrument_types,
        limit=limit,
    )

    return {
        "symbols": [
            {
                "symbol": s.symbol,
                "exchange": s.exchange,
                "market": s.market,
                "description": s.description,
                "type": s.instrument_type,
                "base": s.base_asset,
                "quote": s.quote_asset,
            }
            for s in results
        ],
        "count": len(results),
        "filters": {
            "exchange": exchange,
            "market": market,
            "types": instrument_types,
        },
    }


@router.get("/search")
async def search_symbols(
    q: str = Query(..., min_length=1, description="Search query (e.g., 'BTC', 'NIFTY')"),
    exchange: str | None = Query(None, description="Filter by exchange (binance, fyers)"),
    types: str | None = Query(
        None,
        description="Comma-separated instrument types or preset name (spot, futures, options, stocks, index_fo, equity_fo, currency, commodity)",
    ),
    limit: int = Query(50, ge=1, le=200, description="Max results"),
):
    """
    Search symbols across all exchanges.

    Examples:
    - /api/symbols/search?q=BTC → All BTC pairs
    - /api/symbols/search?q=NIFTY&exchange=fyers → NSE NIFTY symbols
    - /api/symbols/search?q=ETH&types=spot → ETH spot pairs only
    - /api/symbols/search?q=ETH&types=futures → ETH perpetuals and quarterly futures
    - /api/symbols/search?q=RELIANCE&types=stocks → RELIANCE equity
    - /api/symbols/search?q=BANKNIFTY&types=index_fo → BANKNIFTY futures and options
    """
    service = get_symbol_service()

    # Resolve types filter
    instrument_types: list[str] | None = None
    if types:
        # Check if it's a preset name
        if types in FILTER_PRESETS:
            instrument_types = FILTER_PRESETS[types]
        else:
            # Treat as comma-separated list
            instrument_types = [t.strip() for t in types.split(",") if t.strip()]

    results = service.search(
        query=q,
        exchange=exchange,
        instrument_types=instrument_types,
        limit=limit,
    )

    return {
        "results": [
            {
                "symbol": s.symbol,
                "exchange": s.exchange,
                "market": s.market,
                "description": s.description,
                "type": s.instrument_type,
                "base": s.base_asset,
                "quote": s.quote_asset,
                "underlying": s.underlying,
                "expiry": s.expiry_date,
                "strike": s.strike_price,
                "option_type": s.option_type,
            }
            for s in results
        ],
        "count": len(results),
        "query": q,
        "filters": {
            "exchange": exchange,
            "types": instrument_types,
        },
    }


@router.get("/filters")
async def get_filter_presets():
    """
    Get available filter presets for the search UI.

    Returns preset names and their corresponding instrument types.
    """
    return {
        "presets": {
            name: types for name, types in FILTER_PRESETS.items()
        },
        "description": {
            "all": "All instrument types",
            "spot": "Spot trading pairs (Binance)",
            "futures": "Perpetual and quarterly futures",
            "options": "Call and put options",
            "stocks": "Equities (NSE via Fyers)",
            "index_fo": "Index futures and options (NIFTY, BANKNIFTY)",
            "equity_fo": "Stock futures and options (RELIANCE, TCS, etc.)",
            "currency": "Currency futures and options (USDINR, EURINR)",
            "commodity": "Commodity futures and options (MCX: GOLD, CRUDE, etc.)",
        },
    }


@router.get("/stats")
async def get_symbol_stats():
    """
    Get symbol counts by exchange and type.

    Useful for displaying symbol counts in the UI.
    """
    service = get_symbol_service()

    return {
        "total": service.get_count(),
        "by_exchange": {
            "binance": service.get_count("binance"),
            "fyers": service.get_count("fyers"),
        },
    }


@router.get("/{exchange}/{market}/{symbol}")
async def get_symbol_info(
    exchange: str,
    market: str,
    symbol: str,
):
    """
    Get detailed information for a specific symbol.

    Args:
        exchange: Exchange name (binance, fyers)
        market: Market type (spot, futures, options, equity, etc.)
        symbol: Symbol name (BTCUSDT, NSE:RELIANCE-EQ)

    Returns:
        Full SymbolInfo object
    """
    service = get_symbol_service()
    info = service.get_symbol(exchange, market, symbol)

    if not info:
        raise HTTPException(
            status_code=404,
            detail=f"Symbol not found: {exchange}:{market}:{symbol}",
        )

    return {
        "symbol": info.symbol,
        "exchange": info.exchange,
        "market": info.market,
        "base_asset": info.base_asset,
        "quote_asset": info.quote_asset,
        "description": info.description,
        "instrument_type": info.instrument_type,
        "contract_type": info.contract_type,
        "expiry_date": info.expiry_date,
        "strike_price": info.strike_price,
        "option_type": info.option_type,
        "underlying": info.underlying,
        "tick_size": info.tick_size,
        "lot_size": info.lot_size,
        "min_notional": info.min_notional,
        "is_trading": info.is_trading,
    }


@router.post("/refresh")
async def refresh_symbols():
    """
    Manually trigger symbol refresh from all exchanges.

    This fetches the latest symbol lists from Binance and Fyers APIs.
    Normally symbols are refreshed on startup.
    """
    service = get_symbol_service()
    await service.refresh()

    return {
        "status": "success",
        "total": service.get_count(),
        "by_exchange": {
            "binance": service.get_count("binance"),
            "fyers": service.get_count("fyers"),
        },
    }
