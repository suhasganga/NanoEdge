"""
In-memory symbol search service with SQLite persistence.

Features:
- Prefix search: "BTC" → BTCUSDT, BTCBUSD, BTC-PERP
- Filter by type: Spot, Futures, Options, Stocks
- Filter by exchange: Binance, Fyers
- <1ms search latency for 50k+ symbols
"""

import asyncio
import sqlite3
from pathlib import Path

import structlog

from hft.core.types import SymbolInfo
from hft.symbols.binance_fetcher import fetch_all_binance
from hft.symbols.fyers_fetcher import fetch_all_fyers

logger = structlog.get_logger(__name__)

# Default database path
DB_PATH = Path("hft/data/symbols.db")

# Instrument type priority for search ranking (lower = higher priority)
_INSTRUMENT_PRIORITY: dict[str, int] = {
    # Primary symbols - highest priority (0)
    "spot": 0,
    "equity": 0,
    "index": 0,
    # Futures - medium priority (1)
    "perp_linear": 1,
    "perp_inverse": 1,
    "future_linear": 1,
    "future_inverse": 1,
    "equity_future": 1,
    "index_future": 1,
    "currency_future": 1,
    "commodity_future": 1,
    # Options - lowest priority (2)
    "option_call": 2,
    "option_put": 2,
    "equity_option_ce": 2,
    "equity_option_pe": 2,
    "index_option_ce": 2,
    "index_option_pe": 2,
    "currency_option_ce": 2,
    "currency_option_pe": 2,
    "commodity_option_ce": 2,
    "commodity_option_pe": 2,
}


def _get_instrument_priority(instrument_type: str) -> int:
    """Get sort priority for instrument type. Lower = higher priority."""
    return _INSTRUMENT_PRIORITY.get(instrument_type, 99)


class SymbolMasterService:
    """
    Fast in-memory symbol search with SQLite backup.

    The service maintains:
    - In-memory dict for O(1) symbol lookup
    - Prefix index for fast search
    - SQLite database for persistence

    Usage:
        service = SymbolMasterService()
        await service.initialize()

        # Search symbols
        results = service.search("BTC", exchange="binance", limit=50)

        # Get specific symbol
        info = service.get_symbol("binance", "spot", "BTCUSDT")
    """

    def __init__(self, db_path: Path | str | None = None):
        """
        Initialize symbol master service.

        Args:
            db_path: Path to SQLite database (default: hft/data/symbols.db)
        """
        self.db_path = Path(db_path) if db_path else DB_PATH

        # In-memory storage
        self._symbols: dict[str, SymbolInfo] = {}  # key → SymbolInfo
        self._by_exchange: dict[str, list[str]] = {}  # exchange → [keys]
        self._by_type: dict[str, list[str]] = {}  # instrument_type → [keys]
        self._search_index: dict[str, set[str]] = {}  # prefix → {keys}

        # Database connection
        self._db: sqlite3.Connection | None = None

    async def initialize(self, refresh: bool = True) -> None:
        """
        Initialize the service.

        Args:
            refresh: If True, refresh symbols from exchanges
        """
        self._init_db()
        self._load_from_db()

        if refresh:
            # Background refresh from exchanges
            await self._refresh_from_exchanges()

    def _init_db(self) -> None:
        """Initialize SQLite database."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(str(self.db_path), check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._create_schema()

    def _create_schema(self) -> None:
        """Create tables if not exist."""
        self._db.executescript(
            """
            CREATE TABLE IF NOT EXISTS symbols (
                id INTEGER PRIMARY KEY,
                symbol TEXT NOT NULL,
                exchange TEXT NOT NULL,
                market TEXT NOT NULL,
                base_asset TEXT,
                quote_asset TEXT,
                description TEXT,
                instrument_type TEXT NOT NULL,
                contract_type TEXT,
                expiry_date TEXT,
                strike_price REAL,
                option_type TEXT,
                underlying TEXT,
                tick_size REAL,
                lot_size REAL,
                min_notional REAL,
                is_trading INTEGER DEFAULT 1,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(symbol, exchange, market)
            );

            CREATE INDEX IF NOT EXISTS idx_symbols_search
                ON symbols(symbol, base_asset);
            CREATE INDEX IF NOT EXISTS idx_symbols_type
                ON symbols(exchange, instrument_type);
            CREATE INDEX IF NOT EXISTS idx_symbols_market
                ON symbols(exchange, market);
        """
        )
        self._db.commit()

    def _load_from_db(self) -> None:
        """Load all symbols from SQLite into memory."""
        if not self._db:
            return

        cursor = self._db.execute(
            "SELECT * FROM symbols WHERE is_trading = 1"
        )
        count = 0
        for row in cursor:
            info = self._row_to_symbol_info(row)
            self._add_to_memory(info)
            count += 1

        logger.info("symbols_loaded_from_db", count=count)

    def _row_to_symbol_info(self, row: sqlite3.Row) -> SymbolInfo:
        """Convert database row to SymbolInfo."""
        return SymbolInfo(
            symbol=row["symbol"],
            exchange=row["exchange"],
            market=row["market"],
            base_asset=row["base_asset"] or "",
            quote_asset=row["quote_asset"] or "",
            description=row["description"] or "",
            instrument_type=row["instrument_type"],
            contract_type=row["contract_type"],
            expiry_date=row["expiry_date"],
            strike_price=row["strike_price"],
            option_type=row["option_type"],
            underlying=row["underlying"],
            tick_size=row["tick_size"] or 0.01,
            lot_size=row["lot_size"] or 1.0,
            min_notional=row["min_notional"],
            is_trading=bool(row["is_trading"]),
        )

    def _add_to_memory(self, info: SymbolInfo) -> None:
        """Add symbol to in-memory indexes."""
        key = f"{info.exchange}:{info.market}:{info.symbol}"
        self._symbols[key] = info

        # Index by exchange
        self._by_exchange.setdefault(info.exchange, []).append(key)

        # Index by type
        self._by_type.setdefault(info.instrument_type, []).append(key)

        # Build prefix search index
        for term in [info.symbol, info.base_asset, info.description or ""]:
            if not term:
                continue
            term_upper = term.upper()
            # Add prefixes (limit to reasonable length for memory)
            for i in range(1, min(len(term_upper) + 1, 20)):
                prefix = term_upper[:i]
                self._search_index.setdefault(prefix, set()).add(key)

    def _save_to_db(self, info: SymbolInfo) -> None:
        """Save or update symbol in database."""
        if not self._db:
            return

        self._db.execute(
            """
            INSERT OR REPLACE INTO symbols (
                symbol, exchange, market, base_asset, quote_asset,
                description, instrument_type, contract_type, expiry_date,
                strike_price, option_type, underlying, tick_size, lot_size,
                min_notional, is_trading, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """,
            (
                info.symbol,
                info.exchange,
                info.market,
                info.base_asset,
                info.quote_asset,
                info.description,
                info.instrument_type,
                info.contract_type,
                info.expiry_date,
                info.strike_price,
                info.option_type,
                info.underlying,
                info.tick_size,
                info.lot_size,
                info.min_notional,
                1 if info.is_trading else 0,
            ),
        )

    def search(
        self,
        query: str,
        exchange: str | None = None,
        instrument_types: list[str] | None = None,
        limit: int = 50,
    ) -> list[SymbolInfo]:
        """
        Search symbols by prefix.

        Args:
            query: Search query (e.g., "BTC", "NIFTY", "REL")
            exchange: Filter by exchange ("binance", "fyers")
            instrument_types: Filter by types (["spot", "perp_linear"])
            limit: Max results

        Returns:
            List of matching SymbolInfo sorted by relevance
        """
        if not query:
            return []

        query_upper = query.upper()

        # Get candidate keys from prefix index
        candidates = self._search_index.get(query_upper, set())

        # Collect ALL matching candidates first, then sort, then limit
        # This ensures ranking works correctly (equity before futures before options)
        results = []
        for key in candidates:
            info = self._symbols.get(key)
            if not info:
                continue

            # Apply filters
            if exchange and info.exchange != exchange:
                continue
            if instrument_types and info.instrument_type not in instrument_types:
                continue

            results.append(info)

        # Sort by relevance:
        # 1. Exact symbol match
        # 2. Exact base_asset match
        # 3. Symbol starts with query (RELIANCE-EQ before RCOM-BE for "relianc")
        # 4. Base asset starts with query
        # 5. Instrument type priority (equity/spot before futures before options)
        # 6. Symbol length (shorter = more relevant)
        # 7. Alphabetical
        results.sort(
            key=lambda x: (
                0 if x.symbol.upper() == query_upper else 1,
                0 if x.base_asset.upper() == query_upper else 1,
                0 if x.symbol.upper().startswith(query_upper) else 1,
                0 if x.base_asset.upper().startswith(query_upper) else 1,
                _get_instrument_priority(x.instrument_type),
                len(x.symbol),
                x.symbol,
            )
        )

        return results[:limit]

    def get_symbol(
        self,
        exchange: str,
        market: str,
        symbol: str,
    ) -> SymbolInfo | None:
        """
        Get specific symbol info.

        Args:
            exchange: Exchange name
            market: Market type
            symbol: Symbol name

        Returns:
            SymbolInfo or None if not found
        """
        key = f"{exchange}:{market}:{symbol}"
        return self._symbols.get(key)

    def get_all_by_exchange(self, exchange: str) -> list[SymbolInfo]:
        """Get all symbols for an exchange."""
        keys = self._by_exchange.get(exchange, [])
        return [self._symbols[k] for k in keys if k in self._symbols]

    def get_all(
        self,
        exchange: str | None = None,
        market: str | None = None,
        instrument_types: list[str] | None = None,
        limit: int = 500,
    ) -> list[SymbolInfo]:
        """
        Get all symbols with optional filters.

        Args:
            exchange: Filter by exchange ("binance", "fyers")
            market: Filter by market ("spot", "futures", "equity", etc.)
            instrument_types: Filter by instrument types
            limit: Max results

        Returns:
            List of SymbolInfo sorted by symbol name
        """
        # Start with all symbols or filter by exchange
        if exchange:
            keys = self._by_exchange.get(exchange, [])
        else:
            keys = list(self._symbols.keys())

        results = []
        for key in keys:
            if len(results) >= limit:
                break

            info = self._symbols.get(key)
            if not info:
                continue

            # Apply filters
            if market and info.market != market:
                continue
            if instrument_types and info.instrument_type not in instrument_types:
                continue

            results.append(info)

        # Sort by symbol name for consistent ordering
        results.sort(key=lambda x: (x.exchange, x.symbol))

        return results[:limit]

    def get_count(self, exchange: str | None = None) -> int:
        """Get total symbol count."""
        if exchange:
            return len(self._by_exchange.get(exchange, []))
        return len(self._symbols)

    async def _refresh_from_exchanges(self) -> None:
        """Fetch latest symbols from all exchanges."""
        logger.info("symbols_refresh_starting")

        # Fetch in parallel
        binance_task = asyncio.create_task(fetch_all_binance())
        fyers_task = asyncio.create_task(fetch_all_fyers())

        binance_symbols, fyers_symbols = await asyncio.gather(
            binance_task,
            fyers_task,
            return_exceptions=True,
        )

        # Process Binance symbols
        if isinstance(binance_symbols, list):
            for info in binance_symbols:
                self._add_to_memory(info)
                self._save_to_db(info)
            logger.info("binance_symbols_loaded", count=len(binance_symbols))
        else:
            logger.error("binance_fetch_failed", error=str(binance_symbols))

        # Process Fyers symbols
        if isinstance(fyers_symbols, list):
            for info in fyers_symbols:
                self._add_to_memory(info)
                self._save_to_db(info)
            logger.info("fyers_symbols_loaded", count=len(fyers_symbols))
        else:
            logger.error("fyers_fetch_failed", error=str(fyers_symbols))

        # Commit all changes
        if self._db:
            self._db.commit()

        logger.info("symbols_refresh_complete", total=len(self._symbols))

    async def refresh(self) -> None:
        """Manually trigger symbol refresh."""
        await self._refresh_from_exchanges()

    def close(self) -> None:
        """Close database connection."""
        if self._db:
            self._db.close()
            self._db = None


# Global service instance (set during app initialization)
_symbol_service: SymbolMasterService | None = None


def get_symbol_service() -> SymbolMasterService:
    """Get global symbol service instance."""
    global _symbol_service
    if _symbol_service is None:
        raise RuntimeError(
            "Symbol service not initialized. Call set_symbol_service() during app startup."
        )
    return _symbol_service


def set_symbol_service(service: SymbolMasterService) -> None:
    """Set the global symbol service instance."""
    global _symbol_service
    _symbol_service = service


async def init_symbol_service(
    db_path: str | None = None, refresh: bool = True
) -> SymbolMasterService:
    """Initialize and return global symbol service."""
    global _symbol_service
    _symbol_service = SymbolMasterService(db_path=db_path)
    await _symbol_service.initialize(refresh=refresh)
    return _symbol_service
