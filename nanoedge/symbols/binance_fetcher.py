"""Fetch symbols from Binance exchange APIs."""

import httpx
import structlog

from nanoedge.core.types import InstrumentType, SymbolInfo

logger = structlog.get_logger(__name__)

# Binance API endpoints
BINANCE_SPOT_URL = "https://api.binance.com/api/v3/exchangeInfo"
BINANCE_FUTURES_URL = "https://fapi.binance.com/fapi/v1/exchangeInfo"
BINANCE_COIN_URL = "https://dapi.binance.com/dapi/v1/exchangeInfo"
BINANCE_OPTIONS_URL = "https://eapi.binance.com/eapi/v1/exchangeInfo"


def _get_tick_size(filters: list) -> float:
    """Extract tick size from symbol filters."""
    for f in filters:
        if f.get("filterType") == "PRICE_FILTER":
            return float(f.get("tickSize", 0.01))
    return 0.01


def _get_lot_size(filters: list) -> float:
    """Extract lot size (step size) from symbol filters."""
    for f in filters:
        if f.get("filterType") == "LOT_SIZE":
            return float(f.get("stepSize", 1.0))
    return 1.0


def _get_min_notional(filters: list) -> float | None:
    """Extract minimum notional from symbol filters."""
    for f in filters:
        if f.get("filterType") == "NOTIONAL":
            return float(f.get("minNotional", 0))
        elif f.get("filterType") == "MIN_NOTIONAL":
            return float(f.get("minNotional", 0))
    return None


async def fetch_binance_spot(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch all Binance spot trading pairs.

    Returns:
        List of SymbolInfo for active trading pairs
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(BINANCE_SPOT_URL)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error("binance_spot_fetch_error", error=str(e))
            return []

    symbols = []
    for s in data.get("symbols", []):
        if s.get("status") != "TRADING":
            continue

        filters = s.get("filters", [])
        info = SymbolInfo(
            symbol=s["symbol"],
            exchange="binance",
            market="spot",
            base_asset=s["baseAsset"],
            quote_asset=s["quoteAsset"],
            description=f"{s['baseAsset']} / {s['quoteAsset']}",
            instrument_type=InstrumentType.SPOT.value,
            tick_size=_get_tick_size(filters),
            lot_size=_get_lot_size(filters),
            min_notional=_get_min_notional(filters),
            is_trading=True,
        )
        symbols.append(info)

    logger.info("binance_spot_fetched", count=len(symbols))
    return symbols


async def fetch_binance_futures(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch all Binance USDT-M futures.

    Returns:
        List of SymbolInfo for perpetuals and quarterlies
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(BINANCE_FUTURES_URL)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error("binance_futures_fetch_error", error=str(e))
            return []

    symbols = []
    for s in data.get("symbols", []):
        if s.get("status") != "TRADING":
            continue

        # Determine contract type
        contract_type = s.get("contractType", "PERPETUAL")
        if contract_type == "PERPETUAL":
            inst_type = InstrumentType.PERP_LINEAR.value
            expiry = None
            desc_suffix = "Perpetual"
        else:
            inst_type = InstrumentType.FUTURE_LINEAR.value
            expiry = s.get("deliveryDate")
            desc_suffix = "Quarterly"

        filters = s.get("filters", [])
        info = SymbolInfo(
            symbol=s["symbol"],
            exchange="binance",
            market="futures",
            base_asset=s["baseAsset"],
            quote_asset=s["quoteAsset"],
            description=f"{s['baseAsset']} / {s['quoteAsset']} {desc_suffix}",
            instrument_type=inst_type,
            contract_type=contract_type.lower() if contract_type else None,
            expiry_date=str(expiry) if expiry else None,
            underlying=s.get("pair"),
            tick_size=_get_tick_size(filters),
            lot_size=_get_lot_size(filters),
            min_notional=_get_min_notional(filters),
            is_trading=True,
        )
        symbols.append(info)

    logger.info("binance_futures_fetched", count=len(symbols))
    return symbols


async def fetch_binance_coin_futures(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch all Binance COIN-M futures (inverse contracts).

    Returns:
        List of SymbolInfo for inverse perpetuals and quarterlies
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(BINANCE_COIN_URL)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error("binance_coin_fetch_error", error=str(e))
            return []

    symbols = []
    for s in data.get("symbols", []):
        if s.get("contractStatus") != "TRADING":
            continue

        contract_type = s.get("contractType", "PERPETUAL")
        if contract_type == "PERPETUAL":
            inst_type = InstrumentType.PERP_INVERSE.value
            desc_suffix = "Perpetual (Inverse)"
        else:
            inst_type = InstrumentType.FUTURE_INVERSE.value
            desc_suffix = "Quarterly (Inverse)"

        filters = s.get("filters", [])
        info = SymbolInfo(
            symbol=s["symbol"],
            exchange="binance",
            market="coin_futures",
            base_asset=s["baseAsset"],
            quote_asset=s["quoteAsset"],
            description=f"{s['baseAsset']} / {s['quoteAsset']} {desc_suffix}",
            instrument_type=inst_type,
            contract_type=contract_type.lower() if contract_type else None,
            expiry_date=str(s.get("deliveryDate")) if s.get("deliveryDate") else None,
            underlying=s.get("pair"),
            tick_size=_get_tick_size(filters),
            lot_size=_get_lot_size(filters),
            is_trading=True,
        )
        symbols.append(info)

    logger.info("binance_coin_futures_fetched", count=len(symbols))
    return symbols


async def fetch_binance_options(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch Binance options (European-style).

    Returns:
        List of SymbolInfo for call and put options
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(BINANCE_OPTIONS_URL)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error("binance_options_fetch_error", error=str(e))
            return []

    symbols = []
    for s in data.get("optionSymbols", []):
        # Parse option details
        side = s.get("side", "").upper()
        if side == "CALL":
            inst_type = InstrumentType.OPTION_CALL.value
        elif side == "PUT":
            inst_type = InstrumentType.OPTION_PUT.value
        else:
            continue

        strike = float(s.get("strikePrice", 0))
        expiry = s.get("expiryDate")

        info = SymbolInfo(
            symbol=s["symbol"],
            exchange="binance",
            market="options",
            base_asset=s.get("underlying", ""),
            quote_asset=s.get("quoteAsset", "USDT"),
            description=f"{s.get('underlying', '')} {strike} {side}",
            instrument_type=inst_type,
            strike_price=strike,
            option_type="call" if side == "CALL" else "put",
            expiry_date=str(expiry) if expiry else None,
            underlying=s.get("underlying"),
            tick_size=float(s.get("minPrice", 0.01)),
            lot_size=float(s.get("minQty", 1.0)),
            is_trading=True,
        )
        symbols.append(info)

    logger.info("binance_options_fetched", count=len(symbols))
    return symbols


async def fetch_all_binance(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch symbols from all Binance markets.

    Returns:
        Combined list of all Binance symbols
    """
    import asyncio

    # Fetch all markets in parallel
    results = await asyncio.gather(
        fetch_binance_spot(timeout),
        fetch_binance_futures(timeout),
        fetch_binance_coin_futures(timeout),
        fetch_binance_options(timeout),
        return_exceptions=True,
    )

    symbols = []
    for result in results:
        if isinstance(result, list):
            symbols.extend(result)
        elif isinstance(result, Exception):
            logger.error("binance_fetch_error", error=str(result))

    logger.info("binance_all_fetched", total=len(symbols))
    return symbols
