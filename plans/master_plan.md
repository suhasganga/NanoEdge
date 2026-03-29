# HFT Platform Master Plan

## Executive Summary

This master plan consolidates the three architectural plans (New Plan 1, 2, 3) into a single implementation roadmap for a **production-grade HFT platform** supporting NSE (via Fyers) and Binance exchanges.

### User Requirements (Confirmed)

| Requirement | Choice | Notes |
|-------------|--------|-------|
| **Platform** | Windows (WSL2 if needed) | Local development only, no server deployment |
| **Phase 1 Exchange** | Binance first | Then add Fyers/NSE later |
| **Initial Scope** | Market data + visualization | Order execution deferred to Phase 4+ |
| **Depth Visualization** | 50-level | Fyers TBT when added; Binance via order book reconstruction |

### Core Design Decisions (Unanimous Across All Plans)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Architecture | **Split-Plane** (C++ hot path / Python warm path) | Determinism + dev velocity |
| Time-Series DB | **QuestDB** | Native SAMPLE BY, streaming ILP, simple ops |
| IPC (Data Plane) | **Aeron** | <1μs shared memory, 25M+ msg/sec |
| IPC (Control Plane) | **ZeroMQ** | Simple command distribution |
| C++/Python Binding | **nanobind** | 3-10x faster than pybind11 |
| JSON Parsing | **simdjson** | 2.5 GB/s, SIMD-accelerated |
| Binary Protocol | **SBE** | Zero-copy field access for Binance |
| Visualization | **TradingView Lightweight Charts v5.1** | 60fps real-time, open source |
| Data Strategy | **Dual-Source** | Ticks in memory, 1m candles in DB |

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EXCHANGE CONNECTIVITY LAYER                          │
├─────────────────────────────────────┬───────────────────────────────────────┤
│        NSE (via Fyers API v3)       │           Binance Exchange            │
│   Market Data: wss://api-t1.fyers.in│     Spot: wss://stream.binance.com    │
│   TBT 50-depth: wss://rtsocket-api  │     SBE: wss://stream-sbe.binance.com │
│   Orders: wss://general-socket-ws   │     Futures: wss://fstream.binance.com│
└─────────────────────────────────────┴───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     DATA INGESTION LAYER (C++20 Hot Path)                   │
├─────────────────────────────────────┬───────────────────────────────────────┤
│       Fyers Feed Handler            │         Binance Feed Handler          │
│       • simdjson On-Demand API      │         • SBE decoder (zero-copy)     │
│       • Protobuf for TBT 50-depth   │         • JSON fallback               │
│       • Boost.Beast WebSocket       │         • Boost.Beast WebSocket       │
└─────────────────────────────────────┴───────────────────────────────────────┘
                                      │
                              ┌───────┴───────┐
                              │ Normalization │
                              │ alignas(64)   │
                              │ MarketTick    │
                              └───────┬───────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AERON IPC LAYER (Shared Memory)                          │
│                    • 25M+ msg/sec throughput                                │
│                    • <1μs latency                                           │
│                    • Lock-free SPSC ring buffers                            │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
│  MEMORY RING        │   │   OHLCV AGGREGATOR  │   │   STRATEGY ENGINE   │
│  BUFFERS            │   │   (Python)          │   │   (Python)          │
│  • Per-symbol ticks │   │   • Real-time only  │   │   • Signal gen      │
│  • Session retention│   │   • WebSocket push  │   │   • NumPy/Pandas    │
│  • ~150MB/symbol/day│   │   • No DB writes    │   │   • Risk checks     │
└─────────┬───────────┘   └─────────┬───────────┘   └─────────┬───────────┘
          │                         │                         │
          │                         │                         │
          │    ┌────────────────────┴──────────────────────┐  │
          │    │          KLINE STREAM HANDLER             │  │
          │    │   • @kline_1m stream from Binance         │  │
          │    │   • Only writes when is_closed=true       │  │
          │    │   • Ensures clean data on server restart  │  │
          │    └────────────────────┬──────────────────────┘  │
          │                         ▼                         │
          │               ┌─────────────────────┐             │
          │               │   QuestDB           │             │
          │               │   • candles_1m      │             │
          │               │   • ILP ingestion   │             │
          │               │   • SAMPLE BY agg   │             │
          │               └─────────────────────┘             │
          │                                                   │
          │    ┌──────────────────────────────────────────┐   │
          └───►│       FastAPI WebSocket Server           │◄──┘
               │   • /ws/ticks/{symbol} - Live ticks      │
               │   • /api/history - QuestDB candles       │
               │   • Conflated stream (20-60 Hz)          │
               └──────────────────────────┬───────────────┘
                                          │
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FRONTEND (TradingView Lightweight Charts)                │
│   • series.setData() for history (QuestDB)                                  │
│   • series.update() for real-time ticks (WebSocket)                         │
│   • Lazy loading via subscribeVisibleLogicalRangeChange()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

| Layer | Component | Technology | License |
|-------|-----------|------------|---------|
| Feed Handler | NSE Parser | C++20 + simdjson | Apache 2.0 |
| Feed Handler | Binance Parser | C++20 + SBE (Real Logic) | Apache 2.0 |
| Feed Handler | WebSocket Client | Boost.Beast | BSL-1.0 |
| IPC | Data Plane | Aeron | Apache 2.0 |
| IPC | Control Plane | ZeroMQ | LGPL |
| Database | Time-Series | QuestDB | Apache 2.0 |
| Cache | Session State | KeyDB | BSD-3 |
| API Server | REST/WebSocket | FastAPI + uvicorn | MIT |
| Binding | C++/Python | nanobind | BSD |
| Frontend | Framework | SolidJS + TypeScript + Vite | MIT |
| Frontend | Charts | TradingView Lightweight Charts v5.1 | Apache 2.0 |
| Frontend | Styling | Tailwind CSS + shadcn-solid | MIT |
| Monitoring | Metrics | Prometheus | Apache 2.0 |
| Monitoring | Dashboards | Grafana | AGPL |

---

## Data Model

### QuestDB Schema (1-minute candles only)

```sql
CREATE TABLE candles_1m (
    timestamp TIMESTAMP,
    exchange SYMBOL CAPACITY 10 CACHE INDEX,
    market SYMBOL CAPACITY 20 CACHE INDEX,
    symbol SYMBOL CAPACITY 50000 CACHE INDEX,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume DOUBLE,
    quote_volume DOUBLE,
    trade_count INT,
    vwap DOUBLE
) TIMESTAMP(timestamp)
PARTITION BY DAY
WAL
DEDUP UPSERT KEYS(timestamp, exchange, market, symbol);
```

**WAL Benefits**: Write-Ahead Logging provides crash recovery, concurrent writes, and DELETE support for data cleanup.

### Higher Timeframes (computed on-demand)

```sql
-- Example: 5-minute candles
SELECT
    timestamp_floor('5m', timestamp) as time,
    first(open) as open,
    max(high) as high,
    min(low) as low,
    last(close) as close,
    sum(volume) as volume
FROM candles_1m
WHERE symbol = 'NSE:NIFTY25JANFUT'
SAMPLE BY 5m ALIGN TO CALENDAR;
```

### Memory Ring Buffer (session ticks)

```python
import numpy as np

TICK_DTYPE = np.dtype([
    ('timestamp_ns', 'u8'),    # Nanoseconds since epoch
    ('symbol_idx', 'u2'),      # Index into symbol table
    ('price', 'f8'),           # Last trade price
    ('volume', 'f8'),          # Trade volume
    ('side', 'i1'),            # 1=buy, -1=sell, 0=unknown
])

# Memory sizing: 50 symbols × 150MB/day = 7.5GB ring buffer allocation
```

---

## Python/C++ Responsibility Matrix

| Component | Language | Latency Budget | Justification |
|-----------|----------|----------------|---------------|
| Feed Handlers | C++ | <1ms | Binary protocol parsing |
| JSON Parsing (Fyers) | C++ (simdjson) | <1ms | 50-depth heavy payloads |
| SBE Decoding (Binance) | C++ | <100ns | Zero-copy binary access |
| Order Book Maintenance | C++ | 50-150ns | Real-time state, lock-free |
| Pre-trade Risk Checks | C++ | <100ns | On critical path |
| **Tick-to-Candle Aggregation** | Python | 1-10ms | Acceptable for 1m candles |
| **Strategy/Signal Generation** | Python | 10-100ms | Development velocity |
| **API Server** | Python (FastAPI) | 1-10ms | I/O-bound, async |
| **Database Queries** | Python | 10-100ms | QuestDB client fast |

---

## Exchange Connector Specifications

### Fyers (NSE)

| Aspect | Specification |
|--------|---------------|
| Market Data WS | `wss://api-t1.fyers.in/feed/data-ws` |
| TBT 50-Depth WS | `wss://rtsocket-api.fyers.in/versova` |
| Orders WS | `wss://api-t1.fyers.in/general-socket-ws` |
| Data Format | JSON (standard), Protobuf (TBT) |
| Rate Limits | 10 req/sec, 3 TBT connections, 5 symbols/TBT conn |
| Symbol Format | `NSE:SBIN-EQ`, `NSE:NIFTY25JANFUT` |
| Timestamps | Epoch seconds (multiply by 1000 for ms) |
| Order Status | Integer: 1=Cancel, 2=Filled, 4=Transit, 5=Reject, 6=Pending |
| Side | Integer: 1=Buy, -1=Sell |

### Binance (Spot + Futures)

| Aspect | Spot | Futures (USDT-M) |
|--------|------|------------------|
| Stream WS | `wss://stream.binance.com:9443` | `wss://fstream.binance.com` |
| SBE WS | `wss://stream-sbe.binance.com` | N/A |
| REST Base | `https://api.binance.com` | `https://fapi.binance.com` |
| Rate Limit | 6000 weight/min | 2400 weight/min |
| WS Streams | 1024/connection | 1024/connection |
| Ping Interval | 20 seconds | 3 minutes |
| 24h Disconnect | Yes | Yes |
| Timestamps | Milliseconds (μs for SBE) | Milliseconds |
| Order Status | String: NEW, FILLED, CANCELED | Same + CALCULATED |
| Position Side | N/A | LONG, SHORT, BOTH |

### Binance Local Order Book Management (for 50-level+ depth)

Binance does not provide a direct 50-level depth stream. Full depth requires building a **local order book**:

**Procedure** (from Binance docs):
1. Open WebSocket to `wss://stream.binance.com:9443/ws/{symbol}@depth` or `@depth@100ms`
2. Buffer all incoming events (note first `U` update ID)
3. Fetch REST snapshot: `GET /api/v3/depth?symbol={SYMBOL}&limit=5000`
4. Discard buffered events where `u` <= snapshot's `lastUpdateId`
5. Initialize local book with snapshot, then apply buffered events
6. For each subsequent event:
   - Skip if `u` < local book ID
   - If `U` > (local ID + 1) → **restart** (missed updates)
   - Apply price level updates (insert/update/remove)
   - Set local ID = event's `u`

**Constraints:**
- Snapshot max: 5000 levels per side (weight: 250)
- Update speeds: 1000ms or 100ms
- Must handle reconnection and resync

```python
# Example diff event structure
{
    "e": "depthUpdate",
    "E": 1672515782136,      # Event time (ms)
    "s": "BTCUSDT",          # Symbol
    "U": 160,                # First update ID
    "u": 165,                # Final update ID
    "b": [["0.0024", "10"]], # Bids: [price, qty]
    "a": [["0.0026", "100"]] # Asks: [price, qty]
}
```

---

## Implementation Phases

### Platform Notes (Windows/WSL2)

**Windows Native:**
- Python WebSocket clients work natively
- QuestDB runs via Docker Desktop
- TradingView frontend works in any browser
- IPC options: Named pipes, TCP sockets, memory-mapped files

**WSL2 (if needed for performance):**
- Full Linux environment for Aeron shared memory (/dev/shm)
- CPU pinning (taskset) available
- Can access Windows filesystem via /mnt/c/
- Docker integration with Docker Desktop

**Recommendation:** Start with Windows native for Phase 1-2. Move to WSL2 in Phase 3 if C++ IPC performance requires it.

---

### Phase 1: Binance Market Data + Visualization (Python)
**Goal**: End-to-end data flow with Binance

**Status: COMPLETE**

**Infrastructure:**
- [x] Set up Docker Desktop with QuestDB container
- [x] Create `candles_1m` schema in QuestDB
- [x] Set up Python environment with `uv` (Python 3.12+)

**Binance Connector:**
- [x] WebSocket client for `@trade` stream (real-time trades)
- [x] WebSocket client for `@kline_1m` stream (candle updates)
- [x] Local order book manager (`@depth` + REST snapshot)
- [x] Handle 24-hour disconnect with reconnection logic
- [x] 23-hour proactive reconnection timer

**Data Pipeline:**
- [x] Trade-to-candle aggregator (StreamingOHLCV class - for WebSocket real-time updates only)
- [x] QuestDB ILP writer for completed 1m candles (TCP with establish())
- [x] NumPy ring buffer for session tick storage
- [x] Auto gap-fill from Binance REST API when data missing (all timeframes)
- [x] Batch candle writer for backfill operations
- [x] **Kline stream approach**: Only closed candles (`is_closed=true`) from Binance kline stream written to QuestDB (prevents partial candle data on server restart)
- [x] **Higher timeframe backfill**: Panning in 5m/15m/1h/1D fetches required 1m candles, QuestDB aggregates via SAMPLE BY
- [x] **Auto-backfill on startup**: Server queries all symbols with data in QuestDB, detects gaps > 1 hour, backfills from Binance REST API (runs in background, doesn't block startup)

**API Server:**
- [x] FastAPI server with uvicorn
- [x] `GET /api/history` - Query candles with auto-backfill from Binance
- [x] `POST /api/backfill` - Manual historical data fetch
- [x] `WS /ws/candles/{symbol}` - Live candle stream with volume
- [x] `WS /ws/depth/{symbol}` - Live order book (50 levels)
- [x] `WS /ws/trades/{symbol}` - Live trade stream from `@aggTrade`
- [x] `WS /ws/stats/{symbol}` - 24h market stats from `@ticker`
- [x] Heartbeat handling (30s timeout prevents client hangs)
- [x] Timestamp validation (rejects pre-2020 dates)

**Frontend (SolidJS + TypeScript + Vite):**
- [x] SolidJS + TypeScript + Vite + Tailwind CSS setup
- [x] TradingView Lightweight Charts v5.1 integration
- [x] Chart component with `ChartApi` interface for parent control
- [x] 5 chart types (Candlestick, Bar, Line, Area, Baseline)
- [x] Real-time updates via `series.update()` with symbol validation
- [x] Lazy loading (infinite history) on scroll
- [x] Volume histogram series with toggle
- [x] Technical indicators via IndicatorManager (SMA 20/50, EMA 12/26, Bollinger Bands)
- [x] **Custom Indicators Dialog** - TradingView-style searchable dialog for adding indicators with any period
- [x] **Indicator Store** - Dynamic indicator state management with localStorage persistence
- [x] Legend display (O/H/L/C values on crosshair move)
- [x] Tooltip following cursor with detailed candle info
- [x] Scale mode selector (Normal/Log/%/Index)
- [x] Header component with all chart controls
- [x] WebSocket hooks (`useCandleWebSocket`, `useDepthWebSocket`, `useTradesWebSocket`, `useStatsWebSocket`)
- [x] **Live higher TF updates**: Frontend aggregates 1m candles into 5m/15m/1h/1D in real-time

**Trading Sidebar (Enhanced):**
- [x] TradingSidebar component with tabbed interface (Book/Trades/Orders)
- [x] MarketStatsBar component (24h price change value + %, high/low/volume, single live indicator)
- [x] OrderBook component with price grouping selector (0.01, 0.1, 1, 10, 100)
- [x] Gradient depth bars with hover states and cumulative totals
- [x] Hidden scrollbars with scroll functionality (CSS `scrollbar-hide`)
- [x] MAX_DEPTH_LEVELS=100 to prevent DOM explosion
- [x] RecentTrades component with color-coded trade feed
- [x] Trade flash animation on new trades
- [x] Timestamp validation (rejects pre-2020 dates)
- [x] Optimized array operations for high-frequency updates
- [x] MyOrders placeholder for future auth

**Verification:**
- [ ] Compare candles against Binance historical API
- [ ] Verify order book state against REST snapshots

**Deliverable**: Live Binance chart with 50-level depth, historical candles from QuestDB

---

### Phase 2: Add Fyers/NSE Connector
**Goal**: Multi-exchange support with unified data model

**Status: IN PROGRESS**

**Fyers TBT 50-Depth Connector (COMPLETE):**
- [x] TBT Protobuf client (`tbt_feed.py`) - Single connection, max 5 symbols
- [x] TBT Connection Pool (`tbt_pool.py`) - Auto-manages up to 3 connections, 15 symbols total
- [x] Protobuf parsing (`proto/msg_pb2.py`) - Compiled from Fyers proto schema
- [x] TBT types (`TBTDepth50`, `TBTDepthLevel`, `TBTQuote`, `TBTSubscription`)
- [x] Incremental depth state (`SymbolDepthState`) - Snapshot + diff updates
- [x] Normalize to `OrderBookSnapshot` for unified order book handling
- [x] Race condition prevention for rapid symbol switching across connections
- [x] Callback routing with connection validation

**Fyers Standard Connector (Remaining):**
- [x] WebSocket client for standard market data (`feed.py`)
- [x] REST client for historical data (`rest_client.py`)
- [x] OAuth2 authentication helpers (`auth.py`)
- [x] OHLCV aggregator for tick-to-candle conversion (`aggregator.py`)
- [ ] Handle daily token refresh (3:00 AM IST)

**Data Normalization:**
- [x] Exchange-agnostic MarketTick struct with exchange/market fields
- [x] Normalize Fyers data to unified types
- [x] Timestamp normalization (Fyers seconds → milliseconds)
- [x] Price conversion (TBT paise → INR)
- [ ] Symbol mapping: `NSE:SBIN-EQ` ↔ internal ID

**Auto-Backfill on Symbol Switch:**
- [x] **Symbol switch backfill**: When subscribing via `/ws/subscribe`, auto-backfill if gap > 30 minutes
- [x] Config settings: `auto_backfill_on_startup`, `startup_backfill_days`, `backfill_on_symbol_switch`, `symbol_switch_backfill_hours`

**Symbol Master Service (COMPLETE):**
- [x] SQLite database for persistent symbol storage (`nanoedge/data/symbols.db`)
- [x] In-memory indexes for O(1) lookups and prefix search (<1ms latency)
- [x] Binance fetcher - spot, futures (perp/dated), options (3500+ symbols)
- [x] Fyers fetcher - NSE/BSE equity, F&O, currency, commodity (190k+ symbols)
- [x] Instrument type classification (InstrumentType enum with 20+ types)
- [x] Filter presets (spot, futures, options, stocks, index_fo, equity_fo, currency, commodity)
- [x] Auto-refresh from exchanges on startup

**Symbol API Endpoints (COMPLETE):**
- [x] `GET /api/symbols` - All symbols with filters (exchange, market, types, limit up to 5000)
- [x] `GET /api/symbols/search?q=BTC` - Prefix search with autocomplete
- [x] `GET /api/symbols/stats` - Symbol counts by exchange
- [x] `GET /api/active-symbols` - Currently subscribed symbols (renamed from `/api/symbols`)

**Frontend:**
- [x] Symbol search API integration
- [x] SymbolSearch component with filters
- [ ] Dynamic `/ws/subscribe` WebSocket endpoint for multi-symbol switching
- [ ] Exchange selector in UI
- [ ] Support both Binance and NSE symbols in UI

**Deliverable**: Both exchanges streaming through unified pipeline

---

### Phase 3: Performance Optimization
**Goal**: Sub-100ms tick-to-chart latency

**Status: COMPLETE**

**Profiling:**
- [x] Profile with `py-spy` to identify bottlenecks (script: `scripts/profile_server.py`)
- [x] Measure latency histograms (p50, p95, p99) (`nanoedge/core/metrics.py` + `/api/metrics` endpoint)

**Python Optimizations:**
- [x] `__slots__` on all high-frequency classes (7 classes: BinanceOrderBook, BinanceWebSocketClient, BinanceFeedHandler, FyersTBTFeedHandler, FyersTBTConnectionPool, SymbolDepthState, ConnectionInfo)
- [x] `gc.freeze()` after initialization (`nanoedge/api/dependencies.py`)
- [x] Pre-allocated NumPy buffers (already optimized in `ring_buffer.py`)
- [x] msgspec for fast JSON serialization (`nanoedge/api/ws_types.py` + WebSocket binary output)

**Latency Infrastructure:**
- [x] TimestampChain for pipeline latency tracking (`nanoedge/core/timestamps.py`)
- [x] LatencyHistogram with rolling window (`nanoedge/core/metrics.py`)
- [x] MetricsCollector with p50/p95/p99/mean/min/max
- [x] Hot path instrumentation (feed.py, websocket.py)
- [x] Metrics API endpoint (`GET /api/metrics`)
- [x] Latency report script (`scripts/latency_report.py`)

**Consider WSL2 Migration (if needed):**
- [ ] Benchmark Windows vs WSL2 performance (optional - defer if targets met)
- [ ] Set up Aeron Media Driver in WSL2
- [ ] Test shared memory IPC latency

**Deliverable**: Documented latency profile, <100ms tick-to-chart

---

### Phase 4: C++ Hot Path (Optional)
**Goal**: Sub-millisecond feed handling (only if Phase 3 is insufficient)

- [ ] C++ Feed Handler with Boost.Beast WebSocket
- [ ] simdjson for Fyers JSON parsing
- [ ] SBE decoder for Binance (compile schema with sbe-tool)
- [ ] Aeron IPC (requires WSL2/Linux)
- [ ] nanobind Python bindings
- [ ] Lock-free SPSC ring buffers

**Deliverable**: <1ms feed handler latency

---

### Phase 5: Order Execution (Future)
**Goal**: Complete trading capability

- [ ] Pre-trade risk checks (fat-finger, position limits)
- [ ] Binance REST/WebSocket order API
- [ ] Fyers REST order API
- [ ] Order state machine (place → ack → fill/cancel)
- [ ] Position tracking and P&L calculation
- [ ] Kill switch implementation

**Deliverable**: End-to-end order flow

---

### Phase 6: Production Hardening (Future)
**Goal**: Reliability and observability

- [ ] Exponential backoff reconnection
- [ ] Binance 24-hour warm standby reconnect
- [ ] Post-reconnect state reconciliation
- [ ] Prometheus metrics + Grafana dashboards
- [ ] structlog JSON logging
- [ ] Circuit breaker pattern

**Deliverable**: Production-ready system

---

## Logging & Latency Tracking

### Configuration Decisions

| Decision | Choice |
|----------|--------|
| **Log Storage** | Stdout + rotating files (`logs/hft.log`, daily rotation, 30 days) |
| **Metrics Persistence** | Prometheus only (no QuestDB metrics storage) |
| **Alerting** | Log-based (ERROR level when thresholds exceeded) |
| **Frontend RTT** | Yes - browser reports timestamp back for true E2E measurement |

### Timestamp Chain Architecture

Every piece of market data carries a **timestamp chain** through the entire pipeline:

```
Exchange Server
     │
     ▼ exchange_ts (T0) ────────────────────────────────────────────────►
─ ─ ─ ─ ─ ─ ─ ─ ─ Network ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
     │
     ▼ recv_ts (T1) ── Network Latency = T1 - T0 ──────────────────────►
WebSocket Frame Received
     │
     ▼ parse_ts (T2) ── Parse Latency = T2 - T1 ───────────────────────►
JSON/SBE Decoded
     │
     ▼ norm_ts (T3) ── Normalize Latency = T3 - T2 ────────────────────►
Normalized to MarketTick
     │
     ▼ ring_ts (T4) ── Ring Buffer Write = T4 - T3 ────────────────────►
Written to Memory Ring Buffer
     │
     ▼ agg_ts (T5) ── Aggregation Latency = T5 - T4 ───────────────────►
OHLCV Updated
     │
     ▼ db_ts (T6) ── DB Write Latency = T6 - T5 ───────────────────────►
QuestDB ILP Write
     │
     ▼ api_ts (T7) ── API Push Latency = T7 - T6 ──────────────────────►
FastAPI WebSocket Push
     │
     ▼ client_ts (T8) ── Client Latency = T8 - T7 ─────────────────────►
Browser Receives

TOTAL END-TO-END: T8 - T0
EXCHANGE DELTA (our lag): T_now - T0
```

### Latency Metrics to Track

| Metric Name | Description | Target | Alert Threshold |
|-------------|-------------|--------|-----------------|
| `ws.network_latency` | Exchange ts → WS receive | <50ms | >200ms |
| `ws.frame_size` | WebSocket message bytes | - | >1MB |
| `parse.json_latency` | JSON decode time | <100μs | >1ms |
| `parse.sbe_latency` | SBE decode time | <10μs | >100μs |
| `normalize.latency` | Raw → unified type | <10μs | >100μs |
| `ring.write_latency` | Ring buffer write | <1μs | >10μs |
| `agg.update_latency` | OHLCV aggregator update | <100ns | >1μs |
| `db.ilp_batch_latency` | QuestDB ILP batch write | <1ms | >10ms |
| `db.query_latency` | QuestDB SQL query | <10ms | >100ms |
| `api.ws_push_latency` | API → client push | <1ms | >10ms |
| `orderbook.update_latency` | Order book apply diff | <10μs | >100μs |
| `orderbook.snapshot_latency` | Order book snapshot apply | <1ms | >10ms |
| `client.rtt_latency` | Full round-trip to browser | <50ms | >100ms |

### Core Logging Types

```python
# nanoedge/core/timestamps.py
@dataclass(slots=True)
class TimestampChain:
    """Nanosecond timestamps at each pipeline stage"""
    exchange_ns: int          # T0: Exchange event time
    recv_ns: int = 0          # T1: WebSocket frame received
    parse_ns: int = 0         # T2: JSON/SBE decode complete
    norm_ns: int = 0          # T3: Normalized to internal type
    ring_ns: int = 0          # T4: Written to ring buffer
    agg_ns: int = 0           # T5: Aggregator processed
    db_ns: int = 0            # T6: Database write initiated
    api_ns: int = 0           # T7: API push initiated

    @property
    def network_latency_us(self) -> float:
        return (self.recv_ns - self.exchange_ns) / 1000

    @property
    def exchange_age_us(self) -> float:
        return (time.time_ns() - self.exchange_ns) / 1000
```

### Logging Standards by Component

**WebSocket Client:**
```python
logger.info("ws_connected", exchange="binance", url=url, reconnect_count=count)
logger.info("ws_stats", exchange="binance", messages_received=count,
            avg_network_latency_us=avg, p99_network_latency_us=p99)
logger.debug("ws_message", symbol=symbol, network_latency_us=latency)
```

**Parser:**
```python
logger.error("parse_error", exchange="binance", raw_message=msg[:500], error=str(e))
logger.info("parse_stats", messages_parsed=count, avg_parse_latency_us=avg)
```

**Aggregator:**
```python
logger.info("candle_completed", symbol=symbol, interval="1m", open=o, high=h, low=l, close=c)
logger.warning("candle_gap_detected", symbol=symbol, gap_seconds=gap)
```

**Order Book:**
```python
logger.info("orderbook_initialized", symbol=symbol, bid_levels=len(bids), ask_levels=len(asks))
logger.warning("orderbook_resync_required", symbol=symbol, reason="sequence_gap")
logger.info("orderbook_stats", symbol=symbol, avg_update_latency_us=avg, spread_bps=spread)
```

**Database:**
```python
logger.info("db_batch_written", table="candles_1m", rows=count, batch_latency_ms=latency)
logger.error("db_write_failed", table="candles_1m", error=str(e), rows_lost=count)
```

### Metrics Infrastructure

**HDR Histogram for Percentiles:**
- Track p50, p95, p99, p999, min, max for all latency metrics
- Report every 10 seconds via periodic logging
- Expose via `/metrics` endpoint for Prometheus scraping

**Clock Synchronization:**
- NTP sync on startup and every 60 seconds
- Track `ntp_offset_ms` to correct for local clock drift
- Accurate "exchange delta" calculation requires NTP correction

**Log-Based Alerting:**
- Log at ERROR level when any latency exceeds threshold
- External tools (Grafana Alertmanager) handle notifications
- Thresholds defined in `nanoedge/core/alerts.py`

### Frontend RTT Measurement

Browser sends acknowledgment with timestamps:
```javascript
ws.send(JSON.stringify({
    type: "ack",
    server_ts_ns: lastServerTs,
    client_recv_ts_ns: clientRecvNs,
    client_send_ts_ns: clientSendNs,
}));
```

Server calculates:
- `server_to_client_us`: How long to reach browser
- `client_to_server_us`: How long for ack to return
- `total_rtt_us`: Full round-trip

### Files for Logging Infrastructure

| File | Purpose |
|------|---------|
| `nanoedge/core/logging.py` | structlog config with file rotation |
| `nanoedge/core/timestamps.py` | TimestampChain dataclass |
| `nanoedge/core/metrics.py` | LatencyHistogram, MetricsRegistry |
| `nanoedge/core/alerts.py` | Threshold checking, ERROR logging |
| `nanoedge/core/clock.py` | NTP sync, corrected time |
| `nanoedge/api/metrics.py` | `/metrics` Prometheus endpoint |

---

## Verification Plan

### Data Correctness
- Compare 1m candles against exchange historical data
- Verify OHLCV aggregation matches exchange candles
- Check timestamp alignment (floor to minute boundary)

### Performance Benchmarks
| Metric | Target | How to Measure |
|--------|--------|----------------|
| Tick processing | <100μs | py-spy flame graph |
| Feed handler (C++) | <1ms | HdrHistogram |
| OHLCV update | <100ns | Inline timing |
| QuestDB write | <1ms | ILP batch latency |
| WebSocket push | <10ms | Round-trip measurement |
| Chart update | 60fps | Browser DevTools |

### Integration Tests
- WebSocket reconnection after network drop
- Candle correctness across day boundaries
- Symbol subscription/unsubscription
- Order lifecycle (place → fill → position update)

### Latency Verification
- [ ] All ticks have complete TimestampChain
- [ ] Network latency (T1-T0) correlates with ping times
- [ ] Parse latency <100μs for JSON, <10μs for SBE
- [ ] End-to-end (T8-T0) <100ms for 99th percentile
- [ ] Metrics endpoint returns valid Prometheus format
- [ ] Periodic log output includes all metric types
- [ ] ERROR logs appear when thresholds exceeded

---

## Project Structure

```
nanoedge/
├── core/               # Shared types, ring buffers, aggregators
│   ├── types.py        # MarketTick, OHLCV, Order structs
│   ├── ring_buffer.py  # NumPy-based tick storage
│   └── aggregator.py   # Tick-to-candle logic
├── connectors/         # Exchange WebSocket/REST clients
│   ├── fyers/
│   │   ├── feed.py     # Market data WebSocket
│   │   ├── orders.py   # Order WebSocket + REST
│   │   └── types.py    # Fyers-specific schemas
│   └── binance/
│       ├── feed.py     # Trade/depth streams
│       ├── orders.py   # User data stream + REST
│       └── types.py    # Binance-specific schemas
├── storage/            # Database clients
│   ├── questdb.py      # ILP writer, SQL queries
│   └── keydb.py        # Session state cache
├── api/                # FastAPI server
│   ├── main.py         # App setup, routes
│   ├── websocket.py    # Live tick/candle streams
│   └── history.py      # Historical data endpoints
├── strategies/         # Trading logic (Phase 4+)
├── risk/               # Pre-trade checks (Phase 4+)
├── cpp/                # C++ hot path (Phase 3+)
│   ├── feed_handler/
│   ├── ipc/
│   └── bindings/
├── frontend/           # SolidJS + TypeScript + Vite
│   ├── src/
│   │   ├── App.tsx           # Root component, state management
│   │   ├── components/
│   │   │   ├── Chart.tsx     # TradingView chart with all features
│   │   │   ├── Header.tsx    # Toolbar with controls
│   │   │   ├── OrderBook.tsx # Order book with ticker display
│   │   │   ├── IndicatorDialog.tsx      # TradingView-style indicator picker
│   │   │   └── IndicatorConfigPanel.tsx # Indicator period/color config
│   │   ├── hooks/
│   │   │   └── useWebSocket.ts  # WebSocket hooks
│   │   ├── stores/
│   │   │   └── indicatorStore.ts # Dynamic indicator state with localStorage
│   │   └── lib/
│   │       ├── indicators.ts        # IndicatorManager (SMA, EMA, BB)
│   │       └── indicatorTemplates.ts # Indicator definitions and colors
│   ├── dist/                 # Production build output
│   └── package.json
├── tests/
├── config/
└── infra/              # Docker, systemd
```

---

## Phase 1 Deliverable Summary

At the end of Phase 1, you will have:

1. **Live Binance Chart**
   - Candlestick chart updating in real-time
   - Multiple timeframes (1m, 5m, 15m, 1h) via SAMPLE BY
   - Infinite scroll history from QuestDB

2. **50-Level Order Book**
   - Real-time bid/ask ladder visualization
   - Local order book maintained from depth stream + snapshots

3. **Data Pipeline**
   - Trades aggregated into 1m candles
   - Candles persisted to QuestDB
   - Session ticks in memory ring buffer

4. **API Endpoints**
   ```
   GET  /api/history?symbol=BTCUSDT&interval=1m&limit=500
   GET  /api/symbols?exchange=binance&market=spot&limit=500
   GET  /api/symbols/search?q=BTC&limit=50
   GET  /api/symbols/stats
   GET  /api/active-symbols
   POST /api/backfill?symbol=BTCUSDT&hours=24
   WS   /ws/candles/BTCUSDT
   WS   /ws/depth/BTCUSDT
   WS   /ws/trades/BTCUSDT
   WS   /ws/stats/BTCUSDT
   ```

---

## Quick Start Commands (Phase 1)

```bash
# QuestDB via Docker Desktop
docker run -d --name questdb -p 9000:9000 -p 9009:9009 -p 8812:8812 questdb/questdb

# Python environment
uv sync
uv add fastapi uvicorn websockets questdb numpy structlog

# Run the API server
uv run uvicorn hft.api.main:app --reload

# Open frontend
start http://localhost:8000/static/index.html
```

---

## Key Files to Implement (Phase 1)

| File | Purpose |
|------|---------|
| `nanoedge/connectors/binance/feed.py` | WebSocket client for trades/kline/ticker streams |
| `nanoedge/connectors/binance/orderbook.py` | Local order book manager |
| `nanoedge/core/aggregator.py` | StreamingOHLCV tick-to-candle |
| `nanoedge/core/ring_buffer.py` | NumPy-based tick storage |
| `nanoedge/core/types.py` | MarketTick, OHLCV, Trade, MarketStats dataclasses |
| `nanoedge/storage/questdb.py` | ILP writer + SQL queries |
| `nanoedge/api/main.py` | FastAPI app setup |
| `nanoedge/api/websocket.py` | Live candle/depth/trades/stats WebSocket endpoints |
| `nanoedge/api/history.py` | Historical candle endpoint |
| `frontend/src/App.tsx` | Root component, state management |
| `frontend/src/components/Chart.tsx` | TradingView chart with ChartApi |
| `frontend/src/components/Header.tsx` | Toolbar with all controls |
| `frontend/src/components/TradingSidebar.tsx` | Tabbed sidebar container |
| `frontend/src/components/MarketStatsBar.tsx` | 24h stats with live indicator |
| `frontend/src/components/OrderBook.tsx` | Order book with price grouping |
| `frontend/src/components/RecentTrades.tsx` | Live trade feed |
| `frontend/src/components/MyOrders.tsx` | Placeholder for auth |
| `frontend/src/components/IndicatorDialog.tsx` | TradingView-style indicator picker |
| `frontend/src/components/IndicatorConfigPanel.tsx` | Indicator period/color config |
| `frontend/src/hooks/useWebSocket.ts` | WebSocket hooks (candles/depth/trades/stats) |
| `frontend/src/stores/indicatorStore.ts` | Dynamic indicator state with localStorage |
| `frontend/src/lib/indicators.ts` | IndicatorManager with dynamic add/remove |
| `frontend/src/lib/indicatorTemplates.ts` | Indicator definitions and colors |

---

## References

- [Binance WebSocket Streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams)
- [Binance Local Order Book](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#how-to-manage-a-local-order-book-correctly)
- [QuestDB SAMPLE BY](https://questdb.com/docs/query/sql/sample-by/)
- [TradingView Lightweight Charts](https://tradingview.github.io/lightweight-charts/)
- [TradingView Realtime Updates](https://tradingview.github.io/lightweight-charts/tutorials/demos/realtime-updates)
- [Fyers API Documentation](downloaded_docs/fyers/API%20-%20FYERS.md)
