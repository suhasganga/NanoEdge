# Unified Production-Grade Architecture Plan — Algo Trading + TBT Analytics (NSE via FYERS, Binance Direct)

**Goal:** A single-machine, production-grade trading stack for live trading + tick-by-tick (TBT) analytics and visualization.

- **Exchanges**
  - **NSE via FYERS**: 50-depth market data (TBT/L2/L3-style depth depending on API payload).
  - **Binance**: direct WebSocket market data (trades + optional order book), optional SBE streams where available.
- **Storage constraint**: Persist **only 1-minute candles (and higher)** in the database.
- **Visualization constraint**: Still show **real-time tick-by-tick movement** on the chart during trading hours.
- **Budget**: 100% free/open-source stack.
- **Language preference**: Python-first, but must meet speed requirements.

This plan unifies the justifications across your three drafts into one coherent, buildable architecture:
- **Dual-source data strategy** (ticks in memory, candles in DB)
- **C++ hot path** for deterministic performance
- **QuestDB** for 1m storage and fast resampling
- **Lightweight Charts** with real-time `series.update()` and lazy history loading

---

## 1) Core design principles (the “why”)

### 1.1 Keep the DB light without losing real-time fidelity
You want the DB to store only **1m+ candles**. That’s compatible with TBT visualization if and only if you separate:

- **Historical truth**: 1-minute candles in DB (QuestDB)
- **Live truth**: ticks (and depth) in-memory for the trading session

This is the central design that resolves the tension between “DB-light” and “TBT UI”.

### 1.2 Separate the system into planes
A production-grade stack uses a split-plane topology:

- **Execution/Data Plane (C++20)** — deterministic, low jitter, processes every tick and owns order lifecycle
- **Strategy/Serving Plane (Python)** — rapid iteration, research, orchestration, APIs
- **UI Plane (JS/TS)** — TradingView Lightweight Charts

This avoids GC/GIL jitter on the critical path while preserving Python productivity.

---

## 2) High-level topology

### 2.1 Processes (single host)

```
                 ┌────────────────────────────┐
                 │  FYERS WS (NSE) + Binance  │
                 └──────────────┬─────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────┐
│        CORE ENGINE (C++20) — HOT PATH / CRITICAL PATH      │
│  Feed Handlers: FYERS, Binance (WS; optional SBE)          │
│  Parsers: protobuf/json; simdjson recommended for JSON     │
│  Normalizer: unified MarketEvent schema                    │
│  Order Book: 50-depth (per symbol)                         │
│  Bar Engine: tick/sec/range/custom minutes + 1m builder    │
│  Risk Engine: hard pre-trade checks + kill switch          │
│  Order Gateway: order state machine + broker/exchange I/O  │
│  Tick Store: rolling in-memory (session) + optional journal│
│                                                          │
│  Outputs (separate streams):                               │
│   A) Lossless event stream -> Strategy                     │
│   B) Conflated UI stream  -> API/WS                        │
│   C) 1m bar closes       -> DB writer                      │
└──────────────┬──────────────────────┬──────────────────────┘
               │                      │
               │ (shared memory rings)│
               ▼                      ▼
┌───────────────────────────┐   ┌────────────────────────────┐
│ Strategy Service (Python)  │   │ API + WS Service (Python)   │
│ - strategies, research     │   │ - REST history (QuestDB)    │
│ - soft risk, portfolio     │   │ - WS ticks/bars (conflated) │
│ - emits OrderIntent        │   │ - subscriptions, auth       │
└──────────────┬────────────┘   └──────────────┬─────────────┘
               │                                 │
               ▼                                 ▼
     OrderIntent -> C++ gateway            Browser UI (Lightweight Charts)

┌───────────────────────────┐
│ QuestDB (DB, candles_1m)   │
│ stores only 1m+ candles    │
└───────────────────────────┘

(Optional)
┌───────────────────────────┐
│ KeyDB (Redis-compatible)   │
│ session state, latest vals │
│ NOT on trading critical path│
└───────────────────────────┘
```

### 2.2 Why shared-memory rings (vs “always Kafka/Redis”)
You want a free, single-host, low-latency system. Shared-memory SPSC rings (or Aeron IPC) provide:
- near-zero-copy transport
- deterministic backpressure
- no broker process required for the hot path

You can still use **ZeroMQ** for non-critical distribution (e.g., copying data to other local tools), and **KeyDB** for session state.

---

## 3) Exact C++ vs Python responsibilities

### 3.1 What must be C++ (performance-critical)
These modules touch every tick or must be deterministic.

1) **Feed handlers + parsing/decoding**
- FYERS depth updates are heavy; parse efficiently.
- Binance can be high-rate; decode cheaply; SBE where feasible.

2) **Event normalization + timestamping + sequencing**
- Convert exchange-specific messages into a unified schema
- Attach monotonic sequence numbers to detect gaps and reorder issues

3) **In-memory event transport (IPC)**
- Shared-memory SPSC rings OR Aeron IPC

4) **Order book maintenance (50-depth)**
- Update bids/asks, compute microstructure features if needed

5) **Bar engine (live)**
- Builds: tick bars, second bars, range bars, custom minute bars
- Also builds canonical 1m bar that will be persisted

6) **Hard risk checks + order gateway**
- kill switch
- fat-finger limits
- position limits
- order state machine (acks/fills/cancels/rejects)

> Practical note: for many retail setups, broker/exchange network latency dominates execution latency. Still, keeping the state machine and risk checks in C++ reduces tail jitter and failure modes.

### 3.2 What can remain Python (high leverage, non-hot-path)
1) **Strategy logic & research**
- indicators, ML, feature engineering
- run multiple strategies safely

2) **Portfolio analytics, reporting, dashboards**

3) **Historical backfill jobs**
- REST pulls of historical candles

4) **DB writes of 1m candles**
- write rate is small; Python is more than sufficient

5) **REST + WebSocket servers**
- FastAPI for history endpoints and WebSocket fanout

### 3.3 Interop choices (C++ ↔ Python)
- Preferred: **shared-memory rings** (language-agnostic, fast)
- If you want in-process native acceleration: wrap C++ modules with **nanobind** (or pybind11)

---

## 4) Data model and storage strategy (DB-light)

### 4.1 What is persisted
- **Persist:** 1-minute OHLCV (+ optional vwap/trades count)
- **Do not persist in DB:** ticks/trades/depth

### 4.2 What is kept in memory
Maintain a rolling **session tick store**, per symbol:
- capacity configured by ticks/sec × retention window
- used for:
  - TBT UI overlay
  - tick/seconds/range bar generation during the session
  - short lookback for intraday strategies

### 4.3 Optional (recommended) tick journal (NOT in DB)
If you ever want replay/debugging/backtests for non-1m bar types, add an append-only journal:
- Parquet + zstd, or a compact binary log with LZ4/zstd
- rotated by day/symbol

This keeps the DB light while giving you recoverability.

---

## 5) Database selection: QuestDB vs ClickHouse (for your use case)

### 5.1 Your workload
- **Write volume:** tiny (1 row/min/symbol)
- **Read volume:** time range reads + resampling into higher timeframes
- **Need:** easy time-bucketing + simple ops

### 5.2 Decision
**Pick QuestDB**.

**Why QuestDB fits your design**
- Time-series SQL extensions like `SAMPLE BY` make resampling trivial and fast.
- Great ergonomics for candle queries and chart backfills.
- Simple single-node ops.

**Why not ClickHouse here**
- ClickHouse is excellent at large-scale OLAP, but MergeTree tables can hit “Too many parts” if you do many small inserts without batching (more relevant for tick storage; less for 1m candles). Still, it increases operational surface area.

---

## 6) QuestDB schema (canonical table)

### 6.1 One canonical table: `candles_1m`
Store one row per (exchange, symbol, minute).

```sql
CREATE TABLE candles_1m (
  ts        TIMESTAMP,
  exchange  SYMBOL,
  symbol    SYMBOL,
  open      DOUBLE,
  high      DOUBLE,
  low       DOUBLE,
  close     DOUBLE,
  volume    DOUBLE,
  vwap      DOUBLE,
  trades    LONG
) TIMESTAMP(ts)
PARTITION BY DAY
WAL;

-- Optional idempotency (replays/backfills):
ALTER TABLE candles_1m DEDUP ENABLE UPSERT KEYS(ts, exchange, symbol);
```

### 6.2 Higher timeframes from 1m
For timeframe >= 1m, compute on demand using `SAMPLE BY`.

Example (conceptual 5m):
```sql
SELECT
  ts,
  first(open) AS open,
  max(high) AS high,
  min(low) AS low,
  last(close) AS close,
  sum(volume) AS volume
FROM candles_1m
WHERE exchange = $EXCHANGE
  AND symbol = $SYMBOL
  AND ts BETWEEN $FROM AND $TO
SAMPLE BY 5m ALIGN TO CALENDAR;
```

---

## 7) Real-time + history visualization (Lightweight Charts)

### 7.1 Dual-source chart model (required)
- **History:** REST from QuestDB-derived bars
- **Live:** WebSocket push from in-memory tick/bar engine

### 7.2 Live updates on 1m chart (TBT feel)
Even though the DB stores only 1m candles, you can make the current candle move tick-by-tick:
- Backend maintains the **forming 1m candle** in memory.
- On each tick (or at a conflated rate), send an update message.
- Frontend calls `series.update()` on the candlestick series.

### 7.3 Lazy loading history on pan
- Start with a window (e.g., last 2000 bars)
- When user scrolls left near edge:
  - fetch older bars from REST
  - prepend to the series

### 7.4 Supporting ALL timeframes
**Timeframes >= 1m**
- Full history available (QuestDB 1m + resample)

**Tick/seconds/range/custom sub-minute**
- Generated from **tick store**
- Historical depth limited to tick retention (unless optional tick journal enabled)

**UX rule (honest + production-grade):**
- In the UI, label tick/seconds/range history as “session-only” (or “last N hours”) unless journal is enabled.

### 7.5 UI stream conflation (mandatory)
Do not push every tick to the browser. Instead:
- keep ticks lossless in C++ core
- expose a **conflated stream** to the UI (e.g., 20–60Hz)

---

## 8) API contract (minimal and solid)

### 8.1 REST
- `GET /history/candles`
  - params: `exchange, symbol, timeframe>=1m, from, to, limit`
  - server: queries QuestDB (resample server-side)

- `GET /history/ticks`
  - params: `exchange, symbol, from, to`
  - source: in-memory tick store (and optional journal)

- `GET /meta/symbols`
- `GET /health`
- `GET /metrics` (Prometheus)

### 8.2 WebSocket
Single endpoint: `/ws/stream`

Client → server:
```json
{ "type": "subscribe", "exchange":"NSE", "symbol":"NIFTY", "streams":["ticks","bars"], "barSpec":{"type":"time","interval":"1s"} }
```

Server → client messages:
- `tick`: last price, qty, ts
- `barUpdate`: for the subscribed bar type
- `order`: fills/acks (optional overlay on chart)

---

## 9) Reliability and fault tolerance

### 9.1 WebSocket resilience
- reconnect with exponential backoff
- heartbeat/ping-pong handling
- sequence gap detection (log and optionally resync)

### 9.2 Kill switch
Hard kill-switch in C++ core:
- if risk limits tripped
- if feed becomes inconsistent
- if position mismatch

### 9.3 Observability (FOSS)
- Prometheus + Grafana
- JSON logs
- key metrics:
  - ticks/sec per symbol
  - consumer lag (ring depth)
  - reconnect count
  - order latency stats
  - DB writer lag

---

## 10) Deployment blueprint (single machine)

### 10.1 Suggested layout
- `core/` (C++ engine)
- `services/api/` (FastAPI)
- `services/strategy/` (Python strategy runner)
- `frontend/` (Lightweight Charts SPA)
- `infra/` (docker-compose, systemd)

### 10.2 Running components
- QuestDB (Docker or binary)
- KeyDB (optional)
- core engine (systemd)
- api/ws service (systemd)
- strategy service (systemd)
- frontend served by API or static server

---

## 11) Build plan / milestones

### Phase 1 — End-to-end prototype
- QuestDB + candles_1m schema
- Python-only feed ingestion for validation
- API endpoints + Lightweight Charts UI
- Live candle updates via `series.update()`

### Phase 2 — Move the hot path to C++
- C++ feed handlers + normalization
- shared-memory ring buffers
- C++ bar engine

### Phase 3 — Execution correctness
- C++ order gateway + hard risk
- integration with Python strategy order intents
- fill/ack events to UI

### Phase 4 — Optional replay
- tick journal + deterministic replay tooling

---

## 12) Technology stack (all FOSS)

- **Core engine:** C++20 (Boost.Asio/Beast or equivalent), simdjson for heavy JSON
- **IPC:** shared-memory SPSC rings (recommended); Aeron IPC optional
- **DB:** QuestDB (candles_1m only)
- **Cache (optional):** KeyDB (session state)
- **API:** FastAPI + Uvicorn
- **Frontend:** TradingView Lightweight Charts
- **Monitoring:** Prometheus + Grafana

---

## 13) Key references (official/high-signal)

QuestDB
- SAMPLE BY: https://questdb.com/docs/query/sql/sample-by/
- Dedup/UPSERT keys: https://questdb.com/docs/query/sql/alter-table-enable-deduplication/

Lightweight Charts
- Realtime updates via `series.update()`: https://tradingview.github.io/lightweight-charts/tutorials/demos/realtime-updates

ClickHouse
- “Too many parts” explanation: https://clickhouse.com/docs/knowledgebase/exception-too-many-parts

Binance
- WebSocket streams overview: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams

Aeron (optional)
- IPC shared-memory architecture overview: https://aeron.io/docs/aeron-cookbook/ipc/
