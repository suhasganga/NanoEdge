# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role

Act as an expert High-Frequency Trading Systems Architect.

## Project Overview

NanoEdge (High-Frequency Trading) platform for algorithmic trading and tick-by-tick analytics. Connects to NSE (via Fyers broker) and Binance exchanges using a hybrid Python/C++ architecture.

## Build & Run Commands

```bash
# Python environment (Python 3.12+ required)
# Using uv (recommended):
uv sync
uv run python main.py

# Adding dependencies (prefer uv add over uv pip install):
uv add fastapi structlog numpy

# Docker services (QuestDB, KeyDB)
docker run -p 9000:9000 -p 9009:9009 -p 8812:8812 questdb/questdb
docker run -p 6379:6379 eqalpha/keydb
```

## Architecture

### Core Design Principles

- **Dual-Source Data Strategy**: Ticks stay in memory (ring buffers), candles go to database (QuestDB)
- **Split-Plane Architecture**: C++ for hot path (feed handlers, execution), Python for warm path (strategy, API)
- **IPC Layer**: Aeron shared memory for tick data (<1μs latency), ZeroMQ for control plane

### Data Flow

```
Exchange WebSockets → C++ Feed Handlers (simdjson/SBE) → Aeron IPC
    → Memory Ring Buffers (live ticks)
    → Python OHLCV Aggregator → QuestDB (1-min candles)
    → FastAPI WebSocket Server → TradingView Lightweight Charts
```

### Key Technology Stack

| Component          | Technology                           |
| ------------------ | ------------------------------------ |
| Time-Series DB     | QuestDB (SAMPLE BY for aggregations) |
| IPC                | Aeron (data) + ZeroMQ (control)      |
| Frontend Framework | SolidJS + TypeScript + Vite          |
| Frontend Charts    | TradingView Lightweight Charts v5.1  |
| Frontend Styling   | Tailwind CSS + shadcn-solid          |
| C++/Python Interop | nanobind                             |
| JSON Parsing       | simdjson (C++)                       |
| API Server         | FastAPI + uvicorn                    |

### Exchange Connectors

- **NSE/Fyers**: WebSocket with JSON/Protobuf, 50-depth market data, 15 symbols max for TBT
- **Binance**: SBE binary protocol for HFT path, 1024 streams/connection, 24-hour auto-disconnect

### Python/C++ Boundary

- C++: Feed handlers, order book, pre-trade risk checks, execution engine
- Python: Strategy research, signal generation, backtesting, API server, database queries

## Reference Documentation

All API documentation is in `downloaded_docs/`. **Always consult these files when building connectors, schemas, or data types.**

### Fyers (NSE/India) - `downloaded_docs/fyers/`

| What You Need | Where to Look |
|---------------|---------------|
| **Complete API Reference** | `API - FYERS.md` (comprehensive, 70k+ tokens) |
| **WebSocket Market Data** | Search for "Market Data Symbol Update" in `API - FYERS.md` |
| **WebSocket Depth (5-level)** | Search for "Market Data Depth Update" in `API - FYERS.md` |
| **Order WebSocket Events** | Search for "General Socket (orders)" in `API - FYERS.md` |
| **Trade WebSocket Events** | Search for "General Socket (trades)" in `API - FYERS.md` |
| **Position WebSocket Events** | Search for "General Socket (positions)" in `API - FYERS.md` |
| **REST Market Depth (50-level)** | Search for "Market Depth" in `API - FYERS.md` |
| **Order Placement/Modify** | Search for "Order Placement" in `API - FYERS.md` |
| **Symbol Master** | Search for "Symbol Master" in `API - FYERS.md` |

**Fyers TBT (Tick-by-Tick) 50-Depth** - Implementation in `nanoedge/connectors/fyers/`:

| File | Purpose |
|------|---------|
| `tbt_feed.py` | Single TBT WebSocket handler (max 5 symbols) with `SymbolDepthState` incremental updates |
| `tbt_pool.py` | Connection pool (auto-manages up to 3 connections, 15 symbols) |
| `proto/msg_pb2.py` | Compiled protobuf for TBT messages |
| `types.py` | TBT types (`TBTDepth50`, `TBTDepthLevel`, `TBTQuote`, `TBTSubscription`) |

- Proto schema: `https://public.fyers.in/tbtproto/1.0.0/msg.proto`
- WebSocket endpoint: `wss://rtsocket-api.fyers.in/versova`
- Rate limits: 3 connections/user, 5 symbols/connection, 50 channels

**TBT Connection Pool Usage:**
```python
from nanoedge.connectors.fyers import FyersTBTConnectionPool

pool = FyersTBTConnectionPool(
    app_id="your_app_id",
    access_token="your_token",
    on_depth=handle_depth,        # TBTDepth50 callback
    on_orderbook=handle_orderbook, # OrderBookSnapshot callback
)

# Add symbols (connections created automatically)
await pool.add_symbols(["NSE:NIFTY25MARFUT", "NSE:BANKNIFTY25MARFUT", ...])
await pool.start()

# Switch symbols dynamically - connections managed automatically
await pool.add_symbol("NSE:RELIANCE-EQ")  # Creates new connection if needed
await pool.remove_symbol("NSE:NIFTY25MARFUT")  # Destroys connection if empty

await pool.stop()
```

**TBT Depth State (Incremental Updates):**
```python
# Snapshot + diff update pattern for 50-level order book
state = SymbolDepthState(symbol="NSE:NIFTY25MARFUT")

# Apply initial snapshot
state.apply_snapshot(feed_time_ns, sequence, token, tbq, tsq, bid_levels, ask_levels)

# Apply incremental diffs (only changed levels)
state.apply_diff(feed_time_ns, sequence, tbq, tsq, bid_levels, ask_levels)

# Convert to normalized types
depth50: TBTDepth50 = state.to_depth50(is_snapshot=False)
order_book: OrderBookSnapshot = state.to_order_book_snapshot()
```

**TBT Price Format:** Prices are in **paise** (1 INR = 100 paise). Divide by 100 for INR.

### Binance (Spot) - `downloaded_docs/binance-spot-api/`

| What You Need | Where to Look |
|---------------|---------------|
| **WebSocket Trade Streams** | `docs/web-socket-streams.md` → "Trade Streams", "Aggregate Trade Streams" |
| **WebSocket Kline/OHLCV** | `docs/web-socket-streams.md` → "Kline/Candlestick Streams" |
| **WebSocket Depth Updates** | `docs/web-socket-streams.md` → "Partial Book Depth", "Diff. Depth Stream" |
| **WebSocket Ticker/BBO** | `docs/web-socket-streams.md` → "Book Ticker", "Individual Symbol Ticker" |
| **User Data (Orders/Fills)** | `docs/user-data-stream.md` → "executionReport", "outboundAccountPosition" |
| **Enums (OrderStatus, Side, etc.)** | `docs/enums.md` |
| **Error Codes** | `docs/errors.md` |
| **REST Trading Endpoints** | `docs/rest-api/trading-endpoints.md` |
| **REST Market Data** | `docs/rest-api/market-data-endpoints.md` |
| **Rate Limits** | `docs/rest-api/limits.md`, `docs/websocket-api/rate-limits.md` |
| **SBE Binary Protocol** | `docs/sbe-market-data-streams.md`, `schemas/sbe/schemas/` |
| **FIX Protocol Schemas** | `schemas/fix/schemas/spot-fix-*.xml` |
| **Symbol Filters** | `docs/filters.md` (PRICE_FILTER, LOT_SIZE, MIN_NOTIONAL - critical for order validation) |
| **Testnet** | `docs/testnet/` (development without real funds) |
| **Authentication** | `docs/rest-api/request-security.md`, `docs/websocket-api/session-authentication.md` |

**Key SBE Schema Files** (for C++ feed handlers):
- `schemas/sbe/schemas/spot_3_2.xml` - Latest spot schema
- `schemas/sbe/schemas/stream_1_0.xml` - WebSocket stream schema

### Binance (Futures/Derivatives) - `downloaded_docs/binance-derivatives/`

| What You Need | Where to Look |
|---------------|---------------|
| **USDT-M Futures Overview** | `usds-margined-futures/general-info.md` |
| **Futures Order Update Event** | `usds-margined-futures/user-data-streams/Event-Order-Update.md` |
| **Futures Position Update Event** | `usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update.md` |
| **Futures WebSocket Streams** | `usds-margined-futures/websocket-market-streams.md` |
| **Futures REST Trading** | `usds-margined-futures/trade/rest-api.md` |
| **Futures REST Account** | `usds-margined-futures/account/rest-api.md` |
| **Coin-M Futures** | `coin-margined-futures/` (same structure as usds-margined) |
| **Options Trading** | `options-trading/` |
| **Portfolio Margin** | `portfolio-margin/`, `portfolio-margin-pro/` |
| **Enums & Error Codes** | `usds-margined-futures/common-definition.md`, `usds-margined-futures/error-code.md` |
| **WebSocket API (bidirectional)** | `usds-margined-futures/websocket-api-general-info.md` |
| **Leverage & Margin** | `usds-margined-futures/account/rest-api/Change-Initial-Leverage.md`, `Change-Margin-Type.md` |

**Key Futures Event Types:**
- `ORDER_TRADE_UPDATE` - Order created/filled/canceled (includes `ps` = LONG/SHORT/BOTH)
- `ACCOUNT_UPDATE` - Balance/position changes (includes `B[]` balances, `P[]` positions)

### TradingView Lightweight Charts - `downloaded_docs/lightweight-charts/`

| What You Need | Where to Look |
|---------------|---------------|
| **Chart API** | `docs/api/interfaces/IChartApi.md` |
| **Series API** | `docs/api/interfaces/ISeriesApi.md` |
| **Creating Charts** | `docs/api/functions/createChart.md` |
| **Series Types** | `docs/series-types.md` |
| **Real-time Updates** | `tutorials/demos/realtime-updates.md` |
| **Price Scale** | `docs/price-scale.md` |
| **Time Scale** | `docs/time-scale.md` |

### QuestDB - `downloaded_docs/questdb/`

| What You Need | Where to Look |
|---------------|---------------|
| **Schema Design** | `schema-design-essentials.md` (critical for candle tables) |
| **Partitioning** | `concepts/partitions.md` (DAY/HOUR based on volume) |
| **Designated Timestamp** | `concepts/designated-timestamp.md` (required for perf) |
| **Symbol Type** | `concepts/symbol.md` (for tickers, enums) |
| **ILP Ingestion** | `ingestion/ilp/overview.md` (fast data insertion) |
| **SQL Functions** | `query/functions/` (SAMPLE BY, LATEST ON, aggregates) |
| **Finance SQL Patterns** | `cookbook/sql/finance/` |
| **Time-Series Patterns** | `cookbook/sql/time-series/` |
| **Architecture** | `architecture/` (storage engine, JIT compiler) |
| **Troubleshooting** | `troubleshooting/` |

### QuestDB Python Client - `downloaded_docs/questdb-python-client/`

| What You Need | Where to Look |
|---------------|---------------|
| **Overview** | `index.md` (ILP via HTTP/TCP, v4.1.0) |
| **Installation** | `installation.md` (`pip install questdb[dataframe]`) |
| **Sender API** | `sender.md` (row/dataframe insertion) |
| **Configuration** | `conf.md` (http/tcp, auth, TLS, env vars) |
| **Full API Reference** | `api.md` (all public methods) |
| **Examples** | `examples.md` (batch patterns, DataFrames) |

### C++ Libraries - `downloaded_docs/`

| Library | Location | Use For |
|---------|----------|---------|
| **Boost.Beast** | `boost-beast/` | WebSocket client (C++) |
| **ZeroMQ** | `zeromq/` | IPC control plane |

### Quick Reference: WebSocket Message Payloads

**Fyers Symbol Update (type="sf")**:
```
symbol, ltp, vol_traded_today, last_traded_time, exch_feed_time,
bid_size, ask_size, bid_price, ask_price, last_traded_qty,
tot_buy_qty, tot_sell_qty, avg_trade_price, low_price, high_price,
open_price, prev_close_price, ch, chp
```

**Fyers Depth Update (type="dp")**: `bid_price1-5, ask_price1-5, bid_size1-5, ask_size1-5, bid_order1-5, ask_order1-5`

**Fyers Order Update**: `id, exchOrdId, symbol, qty, filledQty, status (1=Cancel,2=Filled,4=Transit,5=Reject,6=Pending,7=Expired), side (1=Buy,-1=Sell), type (1=Limit,2=Market,3=Stop,4=StopLimit)`

**Binance Trade**: `e, E, s, t, p, q, T, m` (event, time, symbol, tradeId, price, qty, tradeTime, isMaker)

**Binance executionReport (Spot)**: `e, E, s, c, S, o, f, q, p, x, X, i, l, z, L, n, N, T, t` (40+ fields, see `docs/user-data-stream.md`)

**Binance ORDER_TRADE_UPDATE (Futures)**: `e, E, T, o.{s, c, S, o, f, q, p, ap, sp, x, X, i, l, z, L, N, n, T, t, ps, rp}` (includes `ps`=LONG/SHORT/BOTH)

**Binance ACCOUNT_UPDATE (Futures)**: `e, E, T, a.{m, B[{a,wb,cw,bc}], P[{s,pa,ep,up,mt,iw,ps}]}` (balances + positions)

### Exchange Normalization Gotchas

When converting between exchanges, watch for these differences:

| Aspect | Fyers (NSE) | Binance | Conversion Note |
|--------|-------------|---------|-----------------|
| **Timestamps** | Epoch seconds | Epoch milliseconds | `fyers_ts * 1000` |
| **Symbol Format** | `NSE:RELIANCE-EQ` | `BTCUSDT` | Split on `:`, strip suffix |
| **Order Status** | `1=Cancel, 2=Filled, 4=Transit, 5=Reject, 6=Pending, 7=Expired` | `"NEW"`, `"FILLED"`, `"CANCELED"`, `"REJECTED"`, `"EXPIRED"` | Integer→String enum |
| **Side** | `1=Buy, -1=Sell` | `"BUY"`, `"SELL"` | Integer→String |
| **Order Type** | `1=Limit, 2=Market, 3=Stop, 4=StopLimit` | `"LIMIT"`, `"MARKET"`, `"STOP_LOSS"`, `"STOP_LOSS_LIMIT"` | Integer→String |
| **Position Side** | N/A (NSE is delivery/intraday) | `"LONG"`, `"SHORT"`, `"BOTH"` | Futures hedge mode only |
| **Price Format** | Float | String (to preserve precision) | `Decimal(binance_price)` |
| **Quantity Format** | Integer (lots) | String | Parse with precision rules |

### WebSocket Endpoints

| Exchange | Type | URL | Notes |
|----------|------|-----|-------|
| **Fyers** | Market Data | `wss://api-t1.fyers.in/feed/data-ws` | JSON, 5-level depth |
| **Fyers** | TBT 50-Depth | `wss://rtsocket-api.fyers.in/versova` | Protobuf, 50-level depth |
| **Fyers** | Orders/Trades | `wss://api-t1.fyers.in/general-socket-ws` | Account events |
| **Binance Spot** | Single Stream | `wss://stream.binance.com:9443/ws/<streamName>` | e.g., `btcusdt@trade` |
| **Binance Spot** | Combined | `wss://stream.binance.com:9443/stream?streams=<s1>/<s2>` | Up to 1024 streams |
| **Binance Spot** | User Data | `wss://stream.binance.com:9443/ws/<listenKey>` | Keep-alive every 30min |
| **Binance Futures** | Streams | `wss://fstream.binance.com/ws/<streamName>` | USDT-M perpetuals |
| **Binance Futures** | User Data | `wss://fstream.binance.com/ws/<listenKey>` | Orders + positions |
| **Binance Coin-M** | Streams | `wss://dstream.binance.com/ws/<streamName>` | Coin-margined |

### Rate Limits Quick Reference

| Exchange | Limit Type | Value | Doc Reference |
|----------|------------|-------|---------------|
| **Fyers** | TBT connections | 3 per user | TBT docs |
| **Fyers** | Symbols per TBT conn | 5 | TBT docs |
| **Fyers** | Total TBT channels | 50 | TBT docs |
| **Fyers** | API calls | ~10 req/sec | `API - FYERS.md` |
| **Binance Spot** | Request weight | 6000/min | `docs/rest-api/limits.md` |
| **Binance Spot** | Raw requests | 61000/5min | `docs/rest-api/limits.md` |
| **Binance Spot** | Order rate | 10 orders/sec, 200000/day | `docs/rest-api/limits.md` |
| **Binance Spot** | WS connections | 5 per IP | `docs/websocket-api/rate-limits.md` |
| **Binance Spot** | Streams/connection | 1024 | `docs/web-socket-streams.md` |
| **Binance Futures** | Request weight | 2400/min | `usds-margined-futures/general-info.md` |
| **Binance** | ListenKey keep-alive | PUT every 30 min | `docs/user-data-stream.md` |

### Post-Reconnect Recovery Checklist

After WebSocket disconnect >5s, reconcile state:

```
[ ] Fetch open orders     → GET /api/v3/openOrders (Spot) or /fapi/v1/openOrders (Futures)
[ ] Fetch positions       → GET /fapi/v2/positionRisk (Futures only)
[ ] Fetch account balance → GET /api/v3/account (Spot) or /fapi/v2/balance (Futures)
[ ] Gap-fill candles      → REST klines API if disconnect > candle interval
[ ] Resubscribe streams   → WebSocket subscription may have been dropped
[ ] Refresh listenKey     → POST new key if >24h or connection dropped
```

For Fyers:
```
[ ] Fetch orders   → GET /api/v3/orders
[ ] Fetch positions → GET /api/v3/positions
[ ] Fetch holdings  → GET /api/v3/holdings
```

### Schema Design Guidelines

When building data types/schemas:
1. Use `msgspec.Struct` with `__slots__ = ()` for all high-frequency types
2. Use `numpy.dtype` for ring buffer storage
3. Create **raw types** that match exchange JSON exactly (for parsing)
4. Create **unified types** that normalize across exchanges (for internal logic)
5. Create **converters** to transform raw → unified

**Example numpy dtypes for ring buffers:**

```python
import numpy as np

# Tick data (unified format)
TICK_DTYPE = np.dtype([
    ('timestamp_ns', 'u8'),    # nanoseconds since epoch
    ('symbol_idx', 'u2'),      # index into symbol table (max 65535 symbols)
    ('price', 'f8'),           # last trade price
    ('volume', 'f8'),          # trade volume
    ('side', 'i1'),            # 1=buy, -1=sell, 0=unknown
])

# Single depth level
DEPTH_LEVEL_DTYPE = np.dtype([
    ('price', 'f8'),
    ('size', 'f8'),
    ('orders', 'u4'),          # order count (Fyers provides this)
])

# 5-level depth (Fyers standard WebSocket)
DEPTH5_DTYPE = np.dtype([
    ('timestamp_ns', 'u8'),
    ('symbol_idx', 'u2'),
    ('bids', DEPTH_LEVEL_DTYPE, (5,)),
    ('asks', DEPTH_LEVEL_DTYPE, (5,)),
])

# 50-level depth (Fyers TBT / Binance depth)
DEPTH50_DTYPE = np.dtype([
    ('timestamp_ns', 'u8'),
    ('symbol_idx', 'u2'),
    ('bid_prices', 'f8', (50,)),
    ('bid_sizes', 'f8', (50,)),
    ('ask_prices', 'f8', (50,)),
    ('ask_sizes', 'f8', (50,)),
])

# OHLCV candle
OHLCV_DTYPE = np.dtype([
    ('timestamp', 'u8'),       # candle open time (epoch ms)
    ('symbol_idx', 'u2'),
    ('open', 'f8'),
    ('high', 'f8'),
    ('low', 'f8'),
    ('close', 'f8'),
    ('volume', 'f8'),
    ('trade_count', 'u4'),
    ('vwap', 'f8'),
])
```

## QuestDB Schema

1-minute candles are the base storage unit. Higher timeframes derived via `SAMPLE BY`:

```sql
CREATE TABLE candles_1m (
    timestamp TIMESTAMP,
    symbol SYMBOL CAPACITY 8192 CACHE INDEX,
    exchange SYMBOL,
    open DOUBLE, high DOUBLE, low DOUBLE, close DOUBLE,
    volume DOUBLE, trade_count INT, vwap DOUBLE
) TIMESTAMP(timestamp) PARTITION BY DAY WAL;
```

## Development Approach

- **Clarify first**: Ask about ambiguous requirements before implementing
- **Explore options**: Evaluate multiple approaches and their trade-offs
- **Present choices**: When multiple valid solutions exist, show pros/cons
- **Suggest improvements**: Proactively recommend optimizations and better patterns
- **Validate early**: Confirm assumptions before building on uncertain foundations

## Logging Standards

Use `structlog` for structured, high-performance logging throughout the codebase.

```python
import structlog

logger = structlog.get_logger(__name__)

# Log with context - always include relevant identifiers
logger.info("tick_received", symbol=symbol, price=price, exchange="binance")
logger.error("order_failed", order_id=order_id, reason=str(e), latency_ms=latency)
```

### Logging Requirements

- **Every external call**: Log entry/exit with latency for WebSocket, REST, database operations
- **Every state change**: Order status, position changes, connection state transitions
- **Every error**: Full context including stack trace, relevant IDs, and system state
- **Performance metrics**: Tick processing latency, queue depths, memory usage at regular intervals
- **Use log levels correctly**: DEBUG for development tracing, INFO for operational events, WARNING for recoverable issues, ERROR for failures requiring attention

### Log Format

All logs must include: `timestamp`, `level`, `logger_name`, `event`, and relevant context fields. Configure JSON output for production, human-readable for development.

## Performance & Optimization

### Critical Path Rules

- **No allocations in hot path**: Use `__slots__`, pre-allocated buffers, object pools
- **O(1) operations only**: Avoid loops, list comprehensions, dict lookups in tick handlers
- **Batch I/O operations**: Aggregate database writes, use async for network calls
- **Profile before optimizing**: Use `py-spy` for Python, measure actual latency histograms

### Memory Optimization

```python
# Always use __slots__ for high-frequency data classes
class MarketTick:
    __slots__ = ('timestamp', 'symbol', 'price', 'volume', 'side')

# Pre-allocate numpy arrays instead of growing lists
buffer = np.empty((BUFFER_SIZE,), dtype=tick_dtype)
```

### Async/Concurrency

- Use `asyncio` for I/O-bound operations (WebSocket, HTTP, database queries)
- Use `multiprocessing` for CPU-bound work that needs to bypass GIL
- Disable GC during trading hours: `gc.disable()` after initialization
- Prefer `uvloop` over default asyncio event loop

### Benchmarking

Log latency histograms (p50, p95, p99) for all critical operations. Target latencies:
- Tick processing: <100μs
- Signal generation: <10ms
- Database write: <1ms (async batched)

## Code Formatting & Imports

### Import Order (enforced by `ruff`)

```python
# 1. Standard library
import asyncio
import logging
from collections import deque
from typing import TYPE_CHECKING

# 2. Third-party packages
import numpy as np
import structlog
from fastapi import FastAPI

# 3. Local application imports
from nanoedge.core.types import MarketTick
from nanoedge.connectors.binance import BinanceConnector
```

### Formatting Rules

- **Formatter**: `ruff format` (Black-compatible, faster)
- **Linter**: `ruff check --fix`
- **Line length**: 88 characters
- **Quotes**: Double quotes for strings
- **Trailing commas**: Always in multi-line structures

### Type Hints

All functions must have complete type annotations:

```python
async def process_tick(
    tick: MarketTick,
    aggregators: dict[str, OHLCVAggregator],
) -> list[CompletedCandle]:
    ...
```

### Naming Conventions

- `snake_case` for functions, variables, modules
- `PascalCase` for classes
- `SCREAMING_SNAKE_CASE` for constants
- Suffix async functions with context: `fetch_candles`, `subscribe_ticks` (not `fetch_candles_async`)

## User-Handled Operations

- **GPU/CUDA**: If any task requires GPU processing or CUDA support, flag it for the user to configure manually
- **Long-running processes**: User will run these directly (trading bots, data collectors, WebSocket listeners)

## Project Structure

```
nanoedge/
├── connectors/      # Exchange WebSocket/REST clients (Fyers, Binance)
├── core/            # Types, ring buffers, OHLCV aggregators
├── strategies/      # Trading signal generators
├── api/             # FastAPI server, WebSocket handlers
├── risk/            # Pre-trade checks, position limits
├── storage/         # QuestDB client, data models
└── tests/           # Mirrors src structure
```

## Frontend (SolidJS + TradingView Lightweight Charts v5.1)

### Build Commands

```bash
cd frontend

# Install dependencies
pnpm install

# Development server (hot reload)
pnpm dev

# Production build (outputs to dist/)
pnpm build

# Type checking
pnpm typecheck
```

### Frontend Structure

```
frontend/
├── src/
│   ├── App.tsx              # Root component, state management
│   ├── index.tsx            # Entry point
│   ├── components/
│   │   ├── Chart.tsx             # TradingView chart with all features
│   │   ├── Header.tsx            # Toolbar with controls
│   │   ├── TradingSidebar.tsx    # Tabbed sidebar (Book/Trades/Orders)
│   │   ├── MarketStatsBar.tsx    # 24h stats bar with live indicator
│   │   ├── OrderBook.tsx         # Order book with price grouping
│   │   ├── RecentTrades.tsx      # Live trade feed
│   │   ├── MyOrders.tsx          # Placeholder for auth
│   │   ├── IndicatorDialog.tsx   # TradingView-style indicator picker
│   │   └── IndicatorConfigPanel.tsx # Indicator period/color config
│   ├── hooks/
│   │   └── useWebSocket.ts  # WebSocket hooks for candles/depth/trades/stats
│   ├── stores/
│   │   └── indicatorStore.ts    # Dynamic indicator state with localStorage
│   └── lib/
│       ├── indicators.ts        # IndicatorManager (SMA, EMA, BB)
│       ├── indicatorTemplates.ts # Indicator definitions and colors
│       └── utils.ts             # Utilities (cn for classnames)
├── dist/                    # Production build output
└── package.json
```

### Chart Features

| Feature | Implementation |
|---------|----------------|
| **Chart Type Switching** | Candlestick, Bar, Line, Area, Baseline via `ChartApi.setChartType()` |
| **Volume Histogram** | Separate series on overlay price scale (15% height) |
| **Technical Indicators** | IndicatorManager with dynamic add/remove, any period (SMA 29, EMA 46, etc.) |
| **Indicator Dialog** | TradingView-style searchable dialog with category tabs |
| **Legend Display** | Shows O/H/L/C values on crosshair move (all chart types) |
| **Tooltip** | Follows cursor with detailed candle info (UTC, DD/MM/YYYY format) |
| **Scale Modes** | Normal, Logarithmic, Percentage, IndexedTo100 |
| **Infinite Scroll** | Loads history on scroll via visibleLogicalRangeChange |

### Chart Component API

The Chart component exposes a `ChartApi` interface to parent components:

```typescript
// frontend/src/components/Chart.tsx

export type ChartType = "candlestick" | "bar" | "line" | "area" | "baseline";

export interface ChartApi {
  scrollToRealtime: () => void;       // Jump to current time
  fitContent: () => void;             // Fit all data in view
  setChartType: (type: ChartType) => void;  // Switch chart type
  setScaleMode: (mode: number) => void;     // 0=Normal, 1=Log, 2=%, 3=Index
  toggleVolume: () => boolean;        // Toggle volume, returns new state
  toggleIndicator: (name: string) => boolean;  // Toggle indicator
  isIndicatorVisible: (name: string) => boolean;
}

// Usage in App.tsx
let chartApi: ChartApi | undefined;

const handleChartReady = (api: ChartApi) => {
  chartApi = api;
};

// Call methods via API
chartApi?.setChartType("line");
chartApi?.toggleIndicator("sma_20");
```

### Chart Type Switching

The chart supports 5 TradingView-style chart types with icon buttons in the toolbar:

| Type | Series | Data Format | Use Case |
|------|--------|-------------|----------|
| **Candlestick** | `CandlestickSeries` | OHLC | Default, full price action |
| **Bar** | `BarSeries` | OHLC | Traditional OHLC bars |
| **Line** | `LineSeries` | `{time, value}` | Clean trend visualization |
| **Area** | `AreaSeries` | `{time, value}` | Filled area under price |
| **Baseline** | `BaselineSeries` | `{time, value}` | Above/below reference price |

**Implementation Details:**
- Data always stored as OHLC in `candleData` array
- `getFormattedData()` converts to `{time, value}` for single-value types
- Legend/tooltip shows OHLC for all chart types by looking up original data
- Visible range preserved across type switches
- WebSocket updates use correct format based on `usesOHLC` flag

### IndicatorManager API

```typescript
// frontend/src/lib/indicators.ts

import { IndicatorManager } from "~/lib/indicators";
import type { IndicatorConfig } from "~/stores/indicatorStore";

// Initialize with chart instance
const indicators = new IndicatorManager(chart);

// Dynamic indicator management (TradingView-style)
const config: IndicatorConfig = {
  id: "sma_29_abc123",
  type: "sma",
  period: 29,
  color: "#2962FF",
  visible: true,
};
indicators.addDynamicIndicator(config);  // Add with unique ID
indicators.removeIndicator("sma_29_abc123");  // Remove by ID
indicators.setIndicatorVisibility("sma_29_abc123", false);  // Toggle visibility
indicators.updateIndicatorColor("sma_29_abc123", "#FF6D00");  // Change color

// Legacy methods (still supported)
indicators.addSMA(20, "#2962FF");     // Blue SMA 20
indicators.addEMA(12, "#00E676");     // Green EMA 12
indicators.addBollingerBands(20, 2);  // BB with 2 std dev

// Update with full candle data
indicators.update(candleData);

// Update last candle only (for real-time)
indicators.updateLast(latestCandle);

// Query indicators
indicators.hasIndicator("sma_29_abc123");  // Check if exists
indicators.getIndicatorIds();              // Get all IDs
indicators.isVisible("sma_20");            // Check visibility

// Cleanup
indicators.clear();    // Clear data but keep series
indicators.destroy();  // Remove all series from chart
```

### Indicator Store

```typescript
// frontend/src/stores/indicatorStore.ts

import { indicators, addIndicator, removeIndicator, toggleIndicator } from "~/stores/indicatorStore";

// Reactive signal with all indicators
const allIndicators = indicators();  // IndicatorConfig[]

// Add custom indicator
addIndicator({
  id: "sma_29_abc123",
  type: "sma",
  period: 29,
  color: "#2962FF",
  visible: true,
});

// Remove by ID
removeIndicator("sma_29_abc123");

// Toggle visibility
toggleIndicator("sma_29_abc123");

// Persisted to localStorage automatically
```

### Header Component

The Header component provides all chart controls in a toolbar:

```typescript
// frontend/src/components/Header.tsx

interface HeaderProps {
  symbol: string;
  interval: string;
  chartType: ChartType;
  scaleMode: number;
  volumeVisible: boolean;
  activeIndicatorCount: number;  // Badge count for Indicators button
  searchOpen: boolean;
  searchInitialChar?: string;
  onSearchOpenChange: (open: boolean) => void;
  onSymbolChange: (symbol: string) => void;
  onIntervalChange: (interval: string) => void;
  onChartTypeChange: (type: ChartType) => void;
  onScaleModeChange: (mode: number) => void;
  onGoLive: () => void;
  onToggleVolume: () => void;
  onOpenIndicatorDialog: () => void;  // Opens TradingView-style dialog
  onSymbolSelect?: (exchange: string, market: string, symbol: string) => void;
}
```

**Toolbar Controls:**
- Symbol selector with search (194k+ symbols)
- Interval buttons (1m, 5m, 15m, 30m, 1h, 4h, 1d)
- Go Live button (scrolls to realtime)
- Chart type icons (5 SVG buttons)
- **Indicators button** (opens dialog, shows active count badge)
- **Vol button** (toggles volume histogram)
- Scale mode dropdown (Normal, Log, %, Index)
- Timezone selector

### TradingSidebar Component

The TradingSidebar provides a tabbed interface for market data:

```typescript
// frontend/src/components/TradingSidebar.tsx

interface TradingSidebarProps {
  symbol: string;
}
```

**Structure:**
```
┌─────────────────────────────┐
│     MarketStatsBar          │ ← Always visible (24h stats + live indicator)
├─────────────────────────────┤
│  [Book] [Trades] [Orders]   │ ← Tab buttons
├─────────────────────────────┤
│    Tab Content Area         │ ← Switches between OrderBook/RecentTrades/MyOrders
└─────────────────────────────┘
```

### MarketStatsBar Component

Displays 24h market statistics from the `@ticker` stream:

```typescript
// frontend/src/components/MarketStatsBar.tsx

interface MarketStatsBarProps {
  symbol: string;
}
```

**Features:**
- Last price with 24h change (value + percentage)
- 24h High/Low/Volume grid
- Single connection status indicator (green/red dot)
- Real-time updates via `useStatsWebSocket` hook

### OrderBook Component

The OrderBook component displays live depth data:

```typescript
// frontend/src/components/OrderBook.tsx

interface OrderBookProps {
  symbol: string;
}
```

**Features:**
- Price grouping selector (None, 0.01, 0.1, 1, 10, 100)
- Gradient depth bars with hover states
- Cumulative totals column
- Compact spread indicator
- Hidden scrollbars with scroll functionality
- MAX_DEPTH_LEVELS=100 to prevent DOM explosion
- Real-time updates via `useDepthWebSocket` hook

### RecentTrades Component

Displays live trade feed:

```typescript
// frontend/src/components/RecentTrades.tsx

interface RecentTradesProps {
  symbol: string;
  maxTrades?: number;  // Default: 50
}
```

**Features:**
- Color-coded by side (green=buy, red=sell)
- Flash animation on new trades
- Timestamp validation (rejects pre-2020 dates)
- Optimized array operations for high-frequency updates
- Real-time updates via `useTradesWebSocket` hook

### WebSocket Message Format

**Candle Update** (sent every 500ms + on candle close):
```json
{
  "type": "candle",
  "symbol": "BTCUSDT",
  "time": 1705689600,
  "open": 93000.5,
  "high": 93150.0,
  "low": 92900.0,
  "close": 93050.0,
  "volume": 125.5,
  "is_closed": false
}
```

**Depth Update**:
```json
{
  "type": "depth",
  "symbol": "BTCUSDT",
  "bids": [[93000, 1.5], [92999, 2.0]],
  "asks": [[93001, 1.2], [93002, 0.8]],
  "lastUpdateId": 12345
}
```

**Trade Update** (from `@aggTrade` stream):
```json
{
  "type": "trade",
  "symbol": "BTCUSDT",
  "price": 93050.5,
  "quantity": 0.1,
  "is_buyer_maker": false,
  "timestamp": 1672515782136,
  "trade_id": 123456789
}
```

**Stats Update** (from `@ticker` stream, ~1s updates):
```json
{
  "type": "stats",
  "symbol": "BTCUSDT",
  "price_change": 100.5,
  "price_change_percent": 0.2,
  "high_24h": 93500,
  "low_24h": 91200,
  "volume_24h": 50000,
  "last_price": 93050
}
```

### WebSocket Hooks (SolidJS)

```typescript
// frontend/src/hooks/useWebSocket.ts

import {
  useCandleWebSocket,
  useDepthWebSocket,
  useTradesWebSocket,
  useStatsWebSocket,
} from "~/hooks/useWebSocket";

// Candle updates for chart
const { data: candleData, isConnected } = useCandleWebSocket(() => props.symbol);

// Depth updates for order book
const { data: depthData, isConnected } = useDepthWebSocket(() => props.symbol);

// Trade updates for recent trades
const { data: tradeData, isConnected } = useTradesWebSocket(() => props.symbol);

// 24h stats updates for market stats bar
const { data: statsData, isConnected } = useStatsWebSocket(() => props.symbol);

// All hooks handle:
// - Auto-reconnection with exponential backoff
// - Symbol switching (closes old connection, opens new)
// - Connection state tracking
// - Heartbeat handling (30s timeout on backend)
```

### Live Aggregation for Higher Timeframes

WebSocket always sends 1m candles. Frontend aggregates them into higher timeframes:

```typescript
// Interval durations in seconds
const INTERVAL_SECONDS: Record<string, number> = {
  "1m": 60, "5m": 300, "15m": 900, "30m": 1800,
  "1h": 3600, "4h": 14400, "1d": 86400,
};

// Floor timestamp to interval boundary (e.g., midnight for 1d)
const floorTimestamp = (timestamp: number, interval: string): number => {
  const intervalSec = INTERVAL_SECONDS[interval] || 60;
  return Math.floor(timestamp / intervalSec) * intervalSec;
};

// Volume tracking: Map of 1m timestamps → volumes (prevents double-counting)
let wsMinuteVolumes = new Map<number, number>();
let currentPeriodCandle: AggregatedCandle | null = null;

// Aggregate incoming 1m candle into current period
const aggregateCandle = (incoming: CandleData): AggregatedCandle => {
  const periodTime = floorTimestamp(incoming.time, props.interval);

  if (!currentPeriodCandle || currentPeriodCandle.time !== periodTime) {
    // New period - track entirely from WebSocket
    wsMinuteVolumes.clear();
    currentPeriodCandle = {
      time: periodTime,
      open: incoming.open,
      high: incoming.high,
      low: incoming.low,
      close: incoming.close,
      volume: incoming.volume,
    };
    wsMinuteVolumes.set(incoming.time, incoming.volume);
  } else {
    // Same period - update OHLCV
    currentPeriodCandle.high = Math.max(currentPeriodCandle.high, incoming.high);
    currentPeriodCandle.low = Math.min(currentPeriodCandle.low, incoming.low);
    currentPeriodCandle.close = incoming.close;
    wsMinuteVolumes.set(incoming.time, incoming.volume);
    currentPeriodCandle.volume = Array.from(wsMinuteVolumes.values())
      .reduce((a, b) => a + b, 0);
  }
  return { ...currentPeriodCandle };
};

// In createEffect for WebSocket updates
const candle = props.interval === "1m" ? incoming : aggregateCandle(incoming);
mainSeries.update(candle);
```

**Flow**: 1m candle → floor timestamp → aggregate into period → update chart

## Data Integrity

### Kline Stream Approach for Clean Candle Data

**Problem**: Server restarts caused partial/corrupted candle data in QuestDB because the tick aggregator would write incomplete candles.

**Solution**: Separate concerns between real-time updates and database persistence:

```
@aggTrade stream → Tick Handler → Ring Buffer (memory)
                         ↓
                   Aggregator → WebSocket (real-time display only)

@kline_1m stream → Kline Handler → QuestDB (only when is_closed=true)
```

**Implementation** (`nanoedge/api/dependencies.py`):

```python
def handle_tick(tick: MarketTick) -> None:
    """Process tick - update aggregator for WebSocket, but DON'T write to DB."""
    if app_state.tick_buffer:
        app_state.tick_buffer.append(tick)
    agg = app_state.aggregators.get(tick.symbol)
    if agg:
        agg.update(tick)  # For real-time WebSocket updates
    _broadcast_tick(tick.symbol, tick)

def handle_kline(kline) -> None:
    """Process kline - ONLY write to QuestDB when candle is complete."""
    if not kline.is_closed:
        return  # Skip partial candles
    if app_state.questdb:
        app_state.questdb.write_candle(kline)  # Only complete candles
    _broadcast_candle(kline.symbol, kline)
```

**Benefits**:
- Clean data even after server restarts (no partial candle artifacts)
- QuestDB DEDUP UPSERT handles duplicate candles automatically
- Aggregator provides sub-second WebSocket updates for responsive UI
- Kline stream provides authoritative, complete candle data from Binance

### Auto Gap-Fill (All Timeframes)

When historical data has gaps (e.g., server was down), the system automatically:
1. Detects gaps by comparing consecutive candle timestamps (works for any interval)
2. **Always fetches 1m candles** from Binance REST API (`GET /api/v3/klines`)
3. Writes to QuestDB with DEDUP UPSERT (handles duplicates)
4. QuestDB `SAMPLE BY` aggregates 1m data to requested timeframe

**Higher Timeframe Behavior**:
- Panning a 1h chart → detects gaps in 1h candles → backfills 1m data → re-queries 1h
- Panning a 1D chart → detects gaps in 1D candles → backfills all required 1m data → re-queries 1D
- Maximum ~50,000 1m candles per backfill (~35 days)

**API Endpoints**:
- `GET /api/history?interval=1h&backfill=true` - Auto-fills gaps with 1m data, returns 1h
- `GET /api/history?interval=1d&limit=30` - Backfills up to 30 days of 1m data
- `POST /api/backfill?symbol=BTCUSDT&hours=24` - Manual backfill for large gaps

## Symbol Master Service

The platform supports 194k+ tradable symbols from Binance (spot/futures/options) and NSE (equity/F&O) with fast in-memory search.

### Symbol API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/symbols` | All symbols with filters (exchange, market, types) |
| `GET /api/symbols/search?q=BTC` | Prefix search with autocomplete |
| `GET /api/symbols/stats` | Symbol counts by exchange |
| `GET /api/active-symbols` | Currently subscribed symbols with live feeds |

### Symbol API Usage

```bash
# Get all symbols (default limit: 500)
GET /api/symbols

# Filter by exchange
GET /api/symbols?exchange=binance

# Filter by market type
GET /api/symbols?exchange=binance&market=spot

# Filter by instrument types (comma-separated)
GET /api/symbols?types=spot,perp_linear

# Use filter presets
GET /api/symbols?types=futures    # All futures types
GET /api/symbols?types=options    # All option types
GET /api/symbols?types=stocks     # NSE equities

# Search with autocomplete
GET /api/symbols/search?q=BTC&limit=20

# Get symbol counts
GET /api/symbols/stats
# Response: {"binance": 3500, "fyers": 190000, "total": 193500}
```

### Filter Presets

| Preset | Instrument Types Included |
|--------|---------------------------|
| `all` | No filter (all types) |
| `spot` | Spot trading pairs |
| `futures` | Perpetuals, dated futures, equity/index/currency/commodity futures |
| `options` | All call/put options (crypto + equity) |
| `stocks` | NSE equities |
| `index_fo` | Index futures & options |
| `equity_fo` | Stock futures & options |
| `currency` | Currency futures & options |
| `commodity` | Commodity futures & options |

### Symbol Service Architecture

```python
from nanoedge.symbols.service import SymbolMasterService, get_symbol_service

# Initialize on startup (auto-refreshes from exchanges)
service = SymbolMasterService(db_path="nanoedge/data/symbols.db")
await service.initialize(refresh=True)

# Search symbols (<1ms latency)
results = service.search("BTC", exchange="binance", limit=50)

# Get specific symbol
info = service.get_symbol("binance", "spot", "BTCUSDT")

# Get all symbols with filters
symbols = service.get_all(exchange="binance", market="spot", limit=500)

# Get counts
total = service.get_count()
binance_count = service.get_count(exchange="binance")
```

**Storage**: SQLite database (`nanoedge/data/symbols.db`) with in-memory indexes for O(1) lookups and prefix search

### Auto-Backfill on Startup & Symbol Switch

The system automatically fills data gaps in two scenarios:

**On Server Startup** (`_startup_backfill()` in `dependencies.py`):
- Runs as background task (doesn't block server startup)
- Queries all symbols with data in QuestDB (last 30 days)
- For each symbol with gap > 1 hour, fetches missing 1m candles
- Logs: `startup_backfill_starting`, `startup_backfill_symbol`, `startup_backfill_complete`

**On Symbol Switch** (`_backfill_symbol_on_switch()` in `websocket.py`):
- Triggered when user subscribes via `/ws/subscribe`
- Runs as background task (doesn't block subscription)
- Backfills if gap > 30 minutes or no data exists
- Logs: `symbol_switch_backfill`

**Configuration** (`config.py`):
```python
auto_backfill_on_startup: bool = True   # Enable startup backfill
startup_backfill_days: int = 7          # Lookback for finding symbols
backfill_on_symbol_switch: bool = True  # Enable switch backfill
symbol_switch_backfill_hours: int = 24  # How far back to check
```

**QuestDB Query for Distinct Symbols**:
```python
# Find all symbols with data in last N days
symbols = await questdb.query_distinct_symbols(since_days=30)
# Returns: [{"symbol": "BTCUSDT", "exchange": "binance", "market": "spot", "latest_ts": 1706054400000}, ...]
```

### Timestamp Validation

All timestamps are validated at multiple layers to prevent invalid data (e.g., 1970 dates):

| Layer | File | Validation |
|-------|------|------------|
| Frontend | `Chart.tsx` | Rejects WebSocket candles with `time < 1577836800` (Jan 1, 2020) |
| WebSocket | `websocket.py` | Skips sending candles with `timestamp < 1577836800000` ms |
| Aggregator | `aggregator.py` | Skips ticks with `tick_ms < 1577836800000` |
| Kline Handler | `dependencies.py` | Skips klines with `timestamp < 1577836800000` |

```python
# Minimum valid timestamp: Jan 1, 2020 00:00:00 UTC
MIN_VALID_TIMESTAMP_MS = 1577836800000

# In aggregator - skip invalid ticks
if tick_ms < MIN_VALID_TIMESTAMP_MS:
    logger.warning("invalid_tick_timestamp", symbol=self.symbol, tick_ms=tick_ms)
    return None
```

## Error Handling & Recovery

### WebSocket Reconnection

```python
async def connect_with_backoff(url: str, max_retries: int = 10) -> WebSocket:
    """Exponential backoff: 1s, 2s, 4s, 8s... capped at 60s"""
    delay = 1.0
    for attempt in range(max_retries):
        try:
            return await websockets.connect(url)
        except Exception as e:
            logger.warning("ws_connect_failed", attempt=attempt, delay=delay, error=str(e))
            await asyncio.sleep(delay)
            delay = min(delay * 2, 60.0)
    raise ConnectionError(f"Failed after {max_retries} attempts")
```

### Circuit Breaker

- Open circuit after 5 consecutive failures
- Half-open after 30 seconds, allow single test request
- Close circuit on successful request

### Recovery Patterns

- **Order state**: Query open orders on reconnect, reconcile with local state
- **Position sync**: Fetch positions from exchange after any disconnect >5s
- **Data gaps**: Request missing candles from REST API when WebSocket reconnects

## Historical Data Gap-Fill

### Auto-Backfill System

The `/api/history` endpoint automatically detects and fills gaps in QuestDB data:

```
User pans chart → GET /api/history?end_time=X
                        ↓
               Query QuestDB for candles
                        ↓
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
   No data         Gaps found      Complete data
        ↓               ↓               ↓
 Fetch from      Backfill gaps    Return directly
 Binance REST    from Binance
        ↓               ↓
   Store in QuestDB (persisted)
        ↓               ↓
      Return complete candle data
```

### Gap Detection (`storage/gap_fill.py`)

```python
from nanoedge.storage.gap_fill import detect_gaps, fetch_missing_candles, backfill_gaps

# Detect time gaps in candle data
gaps = detect_gaps(candles, interval="1m")
# Returns: [(start_ms, end_ms), ...]

# Fetch missing candles from Binance
missing = await fetch_missing_candles(rest_client, "BTCUSDT", start_ms, end_ms)

# Full backfill workflow
filled_count = await backfill_gaps(questdb, rest_client, "BTCUSDT", candles, "1m")
```

### Interval Constants

```python
INTERVAL_MS = {
    "1m": 60_000,
    "5m": 300_000,
    "15m": 900_000,
    "30m": 1_800_000,
    "1h": 3_600_000,
    "4h": 14_400_000,
    "1d": 86_400_000,
}
```

### Manual Backfill Endpoint

```bash
# Fetch last 24 hours of 1m candles from Binance
POST /api/backfill?symbol=BTCUSDT&hours=24

# Response:
{
  "status": "success",
  "symbol": "BTCUSDT",
  "hours": 24,
  "candles_written": 1440
}
```

## Testing Standards

### Test Commands

```bash
# Backend tests (Python)
uv run pytest
uv run pytest --cov=nanoedge --cov-report=html
uv run pytest tests/test_aggregator.py -v
uv run pytest tests/benchmarks/ --benchmark-only

# Frontend tests (TypeScript)
cd frontend
pnpm typecheck          # Type checking
pnpm build              # Build validation
```

### Test Categories

- **Unit tests**: Pure functions, data transformations, aggregators
- **Integration tests**: Database operations, WebSocket mocks
- **Benchmarks**: Tick processing latency, serialization speed

### Fixtures

```python
@pytest.fixture
def sample_ticks() -> list[MarketTick]:
    """Generate realistic tick sequence for testing"""
    ...

@pytest.fixture
async def mock_exchange():
    """Async mock that simulates exchange WebSocket"""
    ...
```

## Configuration Management

### Environment Variables

```bash
# .env (never commit this file)
FYERS_APP_ID=xxx
FYERS_SECRET=xxx
BINANCE_API_KEY=xxx
BINANCE_SECRET=xxx
QUESTDB_HOST=localhost
QUESTDB_ILP_PORT=9009
```

### Typed Config with pydantic-settings

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    fyers_app_id: str
    fyers_secret: str
    binance_api_key: str
    binance_secret: str
    questdb_host: str = "localhost"
    questdb_ilp_port: int = 9009

    model_config = {"env_file": ".env"}

settings = Settings()
```

### Config Files

- `.env` - Local secrets (gitignored)
- `.env.example` - Template with dummy values (committed)
- `config/dev.toml`, `config/prod.toml` - Non-secret settings per environment
