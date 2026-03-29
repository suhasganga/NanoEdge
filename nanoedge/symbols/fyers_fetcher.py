"""Fetch symbols from Fyers symbol master CSVs."""

import csv
import io
import re

import httpx
import structlog

from nanoedge.core.types import InstrumentType, SymbolInfo

logger = structlog.get_logger(__name__)

# Fyers symbol master CSV URLs
FYERS_NSE_CM_URL = "https://public.fyers.in/sym_details/NSE_CM.csv"
FYERS_NSE_FO_URL = "https://public.fyers.in/sym_details/NSE_FO.csv"
FYERS_NSE_CD_URL = "https://public.fyers.in/sym_details/NSE_CD.csv"
FYERS_MCX_URL = "https://public.fyers.in/sym_details/MCX_COM.csv"
FYERS_BSE_CM_URL = "https://public.fyers.in/sym_details/BSE_CM.csv"


def _parse_fo_symbol(symbol: str) -> tuple[str, str | None, float | None, str | None]:
    """
    Parse F&O symbol to extract underlying, expiry, strike, option type.

    Examples:
        - NIFTY25JAN24000CE → (NIFTY, 25JAN, 24000, CE)
        - RELIANCE25MARFUT → (RELIANCE, 25MAR, None, FUT)
        - BANKNIFTY2510223200PE → (BANKNIFTY, 251022, 23200, PE)

    Returns:
        (underlying, expiry, strike, type)
    """
    # Pattern for options: <UNDERLYING><EXPIRY><STRIKE><CE|PE>
    option_match = re.match(
        r"^([A-Z]+)(\d{2}[A-Z]{3}|\d{6})(\d+)(CE|PE)$",
        symbol,
    )
    if option_match:
        underlying = option_match.group(1)
        expiry = option_match.group(2)
        strike = float(option_match.group(3))
        opt_type = option_match.group(4)
        return underlying, expiry, strike, opt_type

    # Pattern for futures: <UNDERLYING><EXPIRY>FUT
    future_match = re.match(
        r"^([A-Z]+)(\d{2}[A-Z]{3}|\d{6})FUT$",
        symbol,
    )
    if future_match:
        underlying = future_match.group(1)
        expiry = future_match.group(2)
        return underlying, expiry, None, "FUT"

    return symbol, None, None, None


def _determine_instrument_type(
    symbol: str,
    underlying: str | None,
    opt_type: str | None,
) -> str:
    """Determine instrument type from symbol pattern."""
    # Index symbols
    index_underlyings = {"NIFTY", "BANKNIFTY", "FINNIFTY", "MIDCPNIFTY"}

    if opt_type == "CE":
        if underlying in index_underlyings:
            return InstrumentType.INDEX_OPTION_CE.value
        return InstrumentType.EQUITY_OPTION_CE.value
    elif opt_type == "PE":
        if underlying in index_underlyings:
            return InstrumentType.INDEX_OPTION_PE.value
        return InstrumentType.EQUITY_OPTION_PE.value
    elif opt_type == "FUT":
        if underlying in index_underlyings:
            return InstrumentType.INDEX_FUTURE.value
        return InstrumentType.EQUITY_FUTURE.value
    elif "-INDEX" in symbol:
        return InstrumentType.INDEX.value
    elif "-EQ" in symbol:
        return InstrumentType.EQUITY.value

    return InstrumentType.EQUITY.value


async def fetch_fyers_equity(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch NSE equity (cash market) symbols.

    Fyers CSV format (no header):
    0: Fytoken, 1: Name, 2: ?, 3: Lot size, 4: Tick size, 5: ISIN,
    6: Trading hours, 7: Last update, 8: Expiry, 9: Fyers Symbol,
    10: Exchange, 11: Segment, 12: Scrip code, 13: Ticker, ...

    Returns:
        List of SymbolInfo for NSE equities
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(FYERS_NSE_CM_URL)
            resp.raise_for_status()
            content = resp.text
        except Exception as e:
            logger.error("fyers_equity_fetch_error", error=str(e))
            return []

    symbols = []
    reader = csv.reader(io.StringIO(content))

    for row in reader:
        try:
            if len(row) < 14:
                continue

            # Column indices based on actual CSV structure
            name = row[1].strip()
            tick_size = float(row[4]) if row[4] else 0.05
            fyers_symbol = row[9].strip()  # Already in NSE:SYMBOL-EQ format
            ticker = row[13].strip()

            if not fyers_symbol or not ticker:
                continue

            info = SymbolInfo(
                symbol=fyers_symbol,
                exchange="fyers",
                market="equity",
                base_asset=ticker,
                quote_asset="INR",
                description=name,
                instrument_type=InstrumentType.EQUITY.value,
                tick_size=tick_size,
                lot_size=1.0,
                is_trading=True,
            )
            symbols.append(info)

        except Exception as e:
            logger.warning("fyers_equity_parse_error", error=str(e))
            continue

    logger.info("fyers_equity_fetched", count=len(symbols))
    return symbols


async def fetch_fyers_fo(timeout: float = 60.0) -> list[SymbolInfo]:
    """
    Fetch NSE F&O (futures + options) symbols.

    Fyers CSV format (no header):
    0: Fytoken, 1: Name, 2: ?, 3: Lot size, 4: Tick size, 5: ?,
    6: Trading hours, 7: Last update, 8: Expiry timestamp, 9: Fyers Symbol,
    10: Exchange, 11: Segment, 12: Scrip code, 13: Underlying, ...

    Returns:
        List of SymbolInfo for futures and options
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(FYERS_NSE_FO_URL)
            resp.raise_for_status()
            content = resp.text
        except Exception as e:
            logger.error("fyers_fo_fetch_error", error=str(e))
            return []

    symbols = []
    reader = csv.reader(io.StringIO(content))

    for row in reader:
        try:
            if len(row) < 14:
                continue

            name = row[1].strip()
            lot_size = float(row[3]) if row[3] else 1
            tick_size = float(row[4]) if row[4] else 0.05
            expiry_ts = row[8].strip() if len(row) > 8 else None
            fyers_symbol = row[9].strip()
            underlying = row[13].strip()

            if not fyers_symbol:
                continue

            # Extract ticker from fyers_symbol (NSE:BANKNIFTY26JANFUT -> BANKNIFTY26JANFUT)
            ticker = fyers_symbol.split(":")[-1] if ":" in fyers_symbol else fyers_symbol

            # Parse F&O symbol
            parsed_underlying, expiry, strike, opt_type = _parse_fo_symbol(ticker)
            inst_type = _determine_instrument_type(ticker, parsed_underlying or underlying, opt_type)

            # Determine market type
            if "option" in inst_type:
                market = "options"
            else:
                market = "futures"

            info = SymbolInfo(
                symbol=fyers_symbol,
                exchange="fyers",
                market=market,
                base_asset=parsed_underlying or underlying,
                quote_asset="INR",
                description=name,
                instrument_type=inst_type,
                expiry_date=expiry or expiry_ts,
                strike_price=strike,
                option_type="call" if opt_type == "CE" else "put" if opt_type == "PE" else None,
                underlying=parsed_underlying or underlying,
                tick_size=tick_size,
                lot_size=lot_size,
                is_trading=True,
            )
            symbols.append(info)

        except Exception as e:
            logger.warning("fyers_fo_parse_error", error=str(e))
            continue

    logger.info("fyers_fo_fetched", count=len(symbols))
    return symbols


async def fetch_fyers_currency(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch NSE currency derivatives (USDINR, etc.).

    Returns:
        List of SymbolInfo for currency futures and options
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(FYERS_NSE_CD_URL)
            resp.raise_for_status()
            content = resp.text
        except Exception as e:
            logger.error("fyers_currency_fetch_error", error=str(e))
            return []

    symbols = []
    reader = csv.reader(io.StringIO(content))

    for row in reader:
        try:
            if len(row) < 14:
                continue

            name = row[1].strip()
            lot_size = float(row[3]) if row[3] else 1000
            tick_size = float(row[4]) if row[4] else 0.0025
            expiry_ts = row[8].strip() if len(row) > 8 else None
            fyers_symbol = row[9].strip()
            underlying = row[13].strip()

            if not fyers_symbol:
                continue

            ticker = fyers_symbol.split(":")[-1] if ":" in fyers_symbol else fyers_symbol

            # Determine type
            if ticker.endswith("CE"):
                inst_type = InstrumentType.CURRENCY_OPTION_CE.value
                market = "options"
            elif ticker.endswith("PE"):
                inst_type = InstrumentType.CURRENCY_OPTION_PE.value
                market = "options"
            else:
                inst_type = InstrumentType.CURRENCY_FUTURE.value
                market = "currency"

            info = SymbolInfo(
                symbol=fyers_symbol,
                exchange="fyers",
                market=market,
                base_asset=underlying,
                quote_asset="INR",
                description=name,
                instrument_type=inst_type,
                expiry_date=expiry_ts,
                tick_size=tick_size,
                lot_size=lot_size,
                is_trading=True,
            )
            symbols.append(info)

        except Exception as e:
            logger.warning("fyers_currency_parse_error", error=str(e))
            continue

    logger.info("fyers_currency_fetched", count=len(symbols))
    return symbols


async def fetch_fyers_commodity(timeout: float = 30.0) -> list[SymbolInfo]:
    """
    Fetch MCX commodity derivatives.

    Returns:
        List of SymbolInfo for commodity futures and options
    """
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(FYERS_MCX_URL)
            resp.raise_for_status()
            content = resp.text
        except Exception as e:
            logger.error("fyers_commodity_fetch_error", error=str(e))
            return []

    symbols = []
    reader = csv.reader(io.StringIO(content))

    for row in reader:
        try:
            if len(row) < 14:
                continue

            name = row[1].strip()
            lot_size = float(row[3]) if row[3] else 1
            tick_size = float(row[4]) if row[4] else 1.0
            expiry_ts = row[8].strip() if len(row) > 8 else None
            fyers_symbol = row[9].strip()
            underlying = row[13].strip()

            if not fyers_symbol:
                continue

            ticker = fyers_symbol.split(":")[-1] if ":" in fyers_symbol else fyers_symbol

            # Determine type
            if ticker.endswith("CE"):
                inst_type = InstrumentType.COMMODITY_OPTION_CE.value
                market = "options"
            elif ticker.endswith("PE"):
                inst_type = InstrumentType.COMMODITY_OPTION_PE.value
                market = "options"
            else:
                inst_type = InstrumentType.COMMODITY_FUTURE.value
                market = "commodity"

            info = SymbolInfo(
                symbol=fyers_symbol,
                exchange="fyers",
                market=market,
                base_asset=underlying,
                quote_asset="INR",
                description=name,
                instrument_type=inst_type,
                expiry_date=expiry_ts,
                tick_size=tick_size,
                lot_size=lot_size,
                is_trading=True,
            )
            symbols.append(info)

        except Exception as e:
            logger.warning("fyers_commodity_parse_error", error=str(e))
            continue

    logger.info("fyers_commodity_fetched", count=len(symbols))
    return symbols


async def fetch_all_fyers(timeout: float = 60.0) -> list[SymbolInfo]:
    """
    Fetch symbols from all Fyers markets.

    Returns:
        Combined list of all Fyers symbols
    """
    import asyncio

    # Fetch all markets in parallel
    results = await asyncio.gather(
        fetch_fyers_equity(timeout),
        fetch_fyers_fo(timeout),
        fetch_fyers_currency(timeout),
        fetch_fyers_commodity(timeout),
        return_exceptions=True,
    )

    symbols = []
    for result in results:
        if isinstance(result, list):
            symbols.extend(result)
        elif isinstance(result, Exception):
            logger.error("fyers_fetch_error", error=str(result))

    logger.info("fyers_all_fetched", total=len(symbols))
    return symbols
