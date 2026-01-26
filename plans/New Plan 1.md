# Unified Production-Grade HFT Architecture Plan
## NSE (Fyers) + Binance Trading Stack

---

## 1. Executive Summary

This document presents a unified architecture for a production-grade Algo Trading and Tick-by-Tick (TBT) Analytics platform, synthesizing the best practices from three architectural approaches. The system bridges two market environments—NSE (via Fyers broker) and Binance—using a hybrid Python/C++ computing model.

### Core Design Principles

1. **Dual-Source Data Strategy**: Ticks stay in memory, candles go to database
2. **Split-Plane Architecture**: C++ for hot path (execution), Python for warm path (strategy)
3. **100% Open Source**: No vendor lock-in, enterprise-grade capabilities
4. **Pragmatic Performance**: Optimize only where profiling demands it

### Key Technology Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Time-Series DB | **QuestDB** | Native SAMPLE BY, streaming-friendly ILP ingestion |
| IPC Layer | **Aeron** (data) + **ZeroMQ** (control) | Sub-microsecond for ticks, simple for commands |
| Frontend Charts | **TradingView Lightweight Charts** | 60K+ candles, real-time updates, open source |
| C++/Python Interop | **nanobind** | 3-10x faster than pybind11 |
| JSON Parsing | **simdjson** | 2.5 GB/s parsing with AVX2/SIMD |

---

## 2. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EXCHANGE CONNECTIVITY LAYER                          │
├─────────────────────────────────────┬───────────────────────────────────────┤
│        NSE (via Fyers API)          │           Binance Exchange            │
│   wss://rtsocket-api.fyers.in       │     wss://stream.binance.com         │
│   TBT: 50-depth, 1000+ ticks/sec    │     Combined streams, <15ms latency  │
│   JSON/Protobuf over WebSocket      │     SBE Binary for HFT path          │
└─────────────────────────────────────┴───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     DATA INGESTION LAYER (C++ - Critical Path)              │
├─────────────────────────────────────┬───────────────────────────────────────┤
│       Fyers Connector               │         Binance Connector             │
│       simdjson Parser               │         SBE Decoder                   │
│       Boost.Beast WebSocket         │         Boost.Beast WebSocket         │
└─────────────────────────────────────┴───────────────────────────────────────┘
                                      │
                              ┌───────┴───────┐
                              │ Normalization │
                              │ Unified Tick  │
                              │    Format     │
                              └───────┬───────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AERON IPC LAYER (Lock-free Shared Memory)                │
│                         25M+ msg/sec, <1μs latency                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
│  SHARED MEMORY      │   │   OHLCV AGGREGATOR  │   │   STRATEGY ENGINE   │
│  RING BUFFERS       │   │   (Python/Cython)   │   │   (Python)          │
│  (per symbol)       │   │                     │   │                     │
│  ~150MB/symbol/day  │   │   1s, 5s, 1m, 5m   │   │   Signal Generation │
│  50K ticks = 5MB    │   │   VWAP/CVD Calc     │   │   NumPy/Pandas      │
└─────────┬───────────┘   └─────────┬───────────┘   └─────────┬───────────┘
          │                         │                         │
          │                         ▼                         │
          │               ┌─────────────────────┐             │
          │               │   QuestDB           │             │
          │               │   1-Minute OHLCV    │             │
          │               │   ILP over TCP      │             │
          │               │   SAMPLE BY for     │             │
          │               │   higher timeframes │             │
          │               └─────────────────────┘             │
          │                                                   │
          │    ┌──────────────────────────────────────────┐   │
          └───►│           WebSocket Server               │◄──┘
               │           (Python FastAPI)               │
               │   Live ticks from memory ring buffer     │
               │   Candle updates from aggregator         │
               └──────────────────────┬───────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER (Browser)                                  │
│                                                                              │
│   TradingView Lightweight Charts v5.1                                       │
│   • Real-time TBT from WebSocket (memory)                                   │
│   • Historical candles from REST API (QuestDB)                              │
│   • Client-side aggregation for tick/range/custom bars                      │
│   • Lazy loading on scroll                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Database Decision: QuestDB

### Why QuestDB Over ClickHouse

After analyzing all three architectural plans, **QuestDB is the unanimous recommendation** for this use case. Here's the detailed comparison:

| Criteria | QuestDB | ClickHouse | Winner |
|----------|---------|------------|--------|
| **Ingestion Model** | Streaming-friendly ILP | Batch-oriented (needs 10K+ rows) | **QuestDB** |
| **Operational Setup** | Single binary, zero-config | Complex tuning required | **QuestDB** |
| **Time Aggregation** | Native `SAMPLE BY 5m` | Requires `argMin/argMax` patterns | **QuestDB** |
| **C++ Integration** | Trivial (TCP socket + string) | Requires HTTP client or heavy lib | **QuestDB** |
| **Python Client** | Native DataFrame, 1.8M rows/sec | Multiple options, more setup | **QuestDB** |
| **Resource Footprint** | ~10 MB core | Hundreds of MB, 4+ GB RAM | **QuestDB** |
| **Ingestion Rate** | 4-5M rows/sec | Millions rows/sec | Tie |
| **Compression** | ~5x typical | 5-10x with Gorilla+ZSTD | ClickHouse |
| **Horizontal Scale** | Enterprise only | Built-in clustering | ClickHouse |

### The Ingestion Problem (Critical)

**ClickHouse's LSM Tree Architecture**: Every insert creates a new "part" on disk. Row-by-row inserts (as ticks arrive) create thousands of tiny parts per second, leading to "Too many parts" errors. You'd need Kafka or an in-memory buffer to batch ticks into chunks of 10,000+. This adds complexity and latency.

**QuestDB's Time-Partitioned Append**: Designed for the "firehose" of data. Accepts Influx Line Protocol (ILP) directly over a raw TCP socket. The C++ Feed Handler can write directly—no intermediate queue needed.

### Critical Insight

At **5,000 symbols × 1 candle/minute = 83 rows/second**, both databases are massively overprovisioned. The decision comes down to **ease of use** and **architectural simplicity**, where QuestDB wins decisively.

### Optimal QuestDB Schema

```sql
CREATE TABLE candles_1m (
    timestamp TIMESTAMP,
    symbol SYMBOL CAPACITY 8192 CACHE INDEX,
    exchange SYMBOL CAPACITY 16,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume DOUBLE,
    trade_count INT,
    vwap DOUBLE
) TIMESTAMP(timestamp)
PARTITION BY DAY
WAL
DEDUP UPSERT KEYS(timestamp, symbol, exchange);
```

**Key Design Choices**:
- `SYMBOL` type provides dictionary encoding (~2x compression)
- `WAL` improves ingestion 1.6x
- `DEDUP UPSERT` handles corrected candles automatically
- `INDEX` on symbol for fast filtering

### Building Higher Timeframes with SAMPLE BY

```sql
-- Real-time 5-minute candles from 1-minute data
SELECT
    timestamp_floor('5m', timestamp) as candle_time,
    symbol,
    first(open) as open,
    max(high) as high,
    min(low) as low,
    last(close) as close,
    sum(volume) as volume
FROM candles_1m
WHERE timestamp IN '2025-01-18'
  AND symbol = 'NSE:NIFTY25JANFUT'
SAMPLE BY 5m ALIGN TO CALENDAR;
```

---

## 4. Python vs C++ Responsibility Matrix

### The Industry Pattern

Professional HFT firms (like Hudson River Trading) use approximately **70% Python for R&D and 30% C++ for execution**. The critical insight: **latency requirements determine language choice, not arbitrary optimization**.

### Component Assignment

| Component | Language | Latency Budget | Justification |
|-----------|----------|----------------|---------------|
| **Market Data Feed Handlers** | C++ | <1ms | Binary protocol parsing, kernel bypass potential |
| **Order Execution Engine** | C++ | <1μs | Deterministic, no GC pauses |
| **Order Book Management** | C++ | 50-150ns | Real-time state, lock-free |
| **Pre-trade Risk Checks** | C++ | <100ns | On critical path |
| **JSON Parsing (Fyers)** | C++ (simdjson) | <1ms | 50-depth = massive JSON payloads |
| **SBE Decoding (Binance)** | C++ | <100ns | Zero-copy binary access |
| **Strategy Research** | Python | N/A | Development speed priority |
| **Signal Generation (>100ms)** | Python | 10-100ms | Not alpha-critical at this latency |
| **Backtesting** | Python | N/A | Rich ecosystem (Pandas, NumPy) |
| **Tick-to-Candle Aggregation** | Python* | 1-10ms | *C++ only if sub-second candles needed |
| **ML Model Training** | Python | N/A | PyTorch/TensorFlow with C++ cores |
| **API Server** | Python (FastAPI) | 1-10ms | I/O-bound, async handles it |
| **Database Queries** | Python | 10-100ms | QuestDB Python client is fast |

### When to Escalate to C++

1. **Tick rate exceeds 10,000/second per symbol**
2. **Sub-second candle generation required**
3. **GIL becomes bottleneck** (profile with `py-spy`)
4. **Need for deterministic latency** (no GC pauses)

### Recommended Interop: nanobind

For new HFT projects, **nanobind outperforms pybind11 by 3-10x**:

| Library | Compile Time | Binary Size | Function Call Overhead |
|---------|--------------|-------------|------------------------|
| nanobind | Baseline | Baseline | Baseline |
| pybind11 | 2.7-4.4× slower | 3-5× larger | 3-10× higher |
| Cython | 1.6-4.4× slower | 3-12× larger | Similar to nanobind |

### GC Mitigation for Python Trading Code

```python
import gc

# After initialization (before trading starts)
gc.freeze()

# Tune thresholds to reduce collection frequency
gc.set_threshold(14000, 10, 10)

# Disable automatic GC during trading hours
gc.disable()

# Use __slots__ for data classes to reduce memory allocation
class MarketTick:
    __slots__ = ['timestamp', 'symbol', 'price', 'volume']
    
    def __init__(self, timestamp, symbol, price, volume):
        self.timestamp = timestamp
        self.symbol = symbol
        self.price = price
        self.volume = volume
```

---

## 5. Market Data Ingestion

### 5.1 NSE Feed Handler (Fyers API v3)

**Data Profile**: Fyers provides 50 levels of market depth (50 best bids + 50 best asks). This is significantly larger than typical Level 2 data—100 separate price and quantity fields per update.

**Constraints**:
- 15 symbols max for TBT
- Daily token expiration at 3:00 AM IST (SEBI compliance)
- 1000+ ticks/second during active trading
- JSON/Protobuf over WebSocket

**The Parsing Bottleneck**: Standard JSON parsers (Python's `json` or C++'s `nlohmann/json`) create a full DOM tree, causing heap fragmentation and CPU stalls.

**Solution: simdjson with On-Demand API**

```cpp
#include "simdjson.h"

simdjson::ondemand::parser parser;
simdjson::padded_string json = simdjson::padded_string::load(buffer);
auto doc = parser.iterate(json);

// Efficiently extracting depth without full DOM tree
for (auto bid : doc["market_depth"]["bids"]) {
    double price = bid["price"];
    int64_t qty = bid["qty"];
    // Update internal order book struct
    order_book.update_bid(price, qty);
}
```

**simdjson Performance**: Uses SIMD instructions (AVX2 on Intel/AMD, NEON on ARM) to process JSON at **2.5 GB/s**—treating JSON like a stream rather than building a tree.

### 5.2 Binance Feed Handler

**Protocol Selection**: For HFT, use **Simple Binary Encoding (SBE)** instead of JSON.

| Protocol | Parsing Method | Latency |
|----------|----------------|---------|
| JSON | Scan every byte for delimiters | 10-100μs |
| SBE | Direct memory offset access | <100ns |

**SBE Endpoint**: `wss://stream-sbe.binance.com:9443/ws`

**Constraints**:
- API Key required in connection header (even for public data)
- 1,024 streams per connection
- 24-hour auto-disconnect (implement warm standby)
- 5-15ms typical latency

**SBE Implementation**:

```cpp
// Schema compiled from Binance XML using real-logic/sbe tool
#include "binance_sbe_stubs.hpp"

// Zero-copy access - no parsing, just memory offset
void process_message(const char* buffer, size_t length) {
    sbe::TradeMessage msg;
    msg.wrap(buffer, 0, length);
    
    // Direct memory read - no parsing overhead
    double price = msg.executionPrice();
    double qty = msg.executionQuantity();
    int64_t timestamp = msg.transactionTime();
}
```

**Reconnect Strategy**: Establish a secondary connection 5 minutes before the 24-hour mark. De-duplicate messages based on sequence numbers before switching.

### 5.3 Normalized Internal Message Format

Both feed handlers output a uniform struct:

```cpp
// Cache-line aligned to prevent false sharing
struct alignas(64) MarketTick {
    int64_t timestamp_ns;     // Nanosecond precision
    int32_t symbol_id;        // Mapped integer for O(1) lookup
    double bid_price_L1;
    double ask_price_L1;
    double bid_qty_L1;
    double ask_qty_L1;
    double last_price;
    double last_volume;
    uint8_t exchange;         // 0=NSE, 1=Binance
    uint8_t flags;            // Trade/Quote/Depth indicator
    char padding[6];          // Align to 64 bytes
};
```

---

## 6. Inter-Process Communication (IPC)

### The Hybrid Approach

| Path Type | Technology | Latency | Use Case |
|-----------|------------|---------|----------|
| **Data Plane** | Aeron (shared memory) | <1μs | TBT market data (hot path) |
| **Control Plane** | ZeroMQ PUB/SUB | ~30-50μs | Start/stop signals, config |
| **Intra-process** | LMAX Disruptor pattern | <50ns | Strategy pipeline stages |

### Why Aeron for Market Data

ZeroMQ relies on kernel sockets (`send/recv` syscalls), making it non-deterministic—a busy kernel can delay tick delivery by hundreds of microseconds.

**Aeron bypasses the kernel** for IPC by writing directly to a memory-mapped file that Python reads.

| Feature | ZeroMQ | Aeron |
|---------|--------|-------|
| Transport | OS kernel sockets | Memory-mapped files |
| Latency (IPC) | 30-50μs | <1μs |
| Throughput | ~1M msg/sec | >20M msg/sec |
| Flow Control | Block or Drop (HWM) | Sophisticated back-pressure |
| Complexity | Low | Higher (Media Driver) |

### Aeron Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  C++ Publisher  │     │   Aeron Media   │     │ Python Consumer │
│  (Feed Handler) │────►│     Driver      │────►│ (Strategy)      │
│                 │     │  (manages shm)  │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                      │                       │
         └──────────────────────┼───────────────────────┘
                                │
                         /dev/shm/aeron
                       (shared memory files)
```

### Lock-Free SPSC Ring Buffer (C Implementation)

For intra-process communication or as a fallback:

```c
typedef struct alignas(64) {
    _Atomic uint64_t write_idx;
    char padding1[56];              // Cache line isolation
    _Atomic uint64_t read_idx;
    char padding2[56];
    size_t mask;                    // Power-of-2 for fast modulo
    MarketTick* buffer;
} SPSCRingBuffer;

bool ring_push(SPSCRingBuffer* rb, const MarketTick* tick) {
    uint64_t w = atomic_load_explicit(&rb->write_idx, memory_order_relaxed);
    uint64_t r = atomic_load_explicit(&rb->read_idx, memory_order_acquire);
    
    if (w - r >= rb->mask) return false;  // Full
    
    rb->buffer[w & rb->mask] = *tick;
    atomic_store_explicit(&rb->write_idx, w + 1, memory_order_release);
    return true;
}
```

**Performance**: 8M messages/second with P99 latency of 850ns—20x faster than traditional message queues.

### Memory Sizing

```
NSE Trading Hours: 6.5 hours = 23,400 seconds
Per Symbol (active): 100 ticks/sec avg × 64 bytes = ~150 MB/day
50 Active Symbols: 50 × 150 MB = 7.5 GB ring buffer allocation

Recommended: 16GB RAM dedicated to tick buffers with 2x safety margin
```

---

## 7. Real-Time Processing Pipeline

### Tick-to-Candle Aggregation

```python
class StreamingOHLCV:
    __slots__ = ['timestamp', 'open', 'high', 'low', 'close',
                 'volume', 'vwap_num', 'vwap_den', 'count']
    
    def __init__(self, timestamp: int, price: float):
        self.timestamp = timestamp
        self.open = self.high = self.low = self.close = price
        self.volume = self.vwap_num = self.vwap_den = 0.0
        self.count = 0
    
    def update(self, price: float, volume: float):
        """O(1) update per tick - no memory allocation"""
        self.high = max(self.high, price)
        self.low = min(self.low, price)
        self.close = price
        self.volume += volume
        self.vwap_num += price * volume
        self.vwap_den += volume
        self.count += 1
    
    @property
    def vwap(self) -> float:
        return self.vwap_num / self.vwap_den if self.vwap_den > 0 else 0.0
```

### Multi-Timeframe Generator

```python
class TimeframeManager:
    def __init__(self, intervals: list[int]):
        """intervals in seconds: [1, 5, 60, 300, 3600]"""
        self.aggregators = {
            interval: {} for interval in intervals  # symbol -> StreamingOHLCV
        }
        self.intervals = sorted(intervals)
    
    def process_tick(self, tick: MarketTick) -> list[dict]:
        """Returns list of completed candles"""
        completed = []
        
        for interval in self.intervals:
            bar_time = (tick.timestamp_ns // 10**9 // interval) * interval
            
            agg = self.aggregators[interval].get(tick.symbol_id)
            
            if agg is None:
                # First tick for this symbol/interval
                self.aggregators[interval][tick.symbol_id] = StreamingOHLCV(
                    bar_time, tick.last_price
                )
            elif bar_time > agg.timestamp:
                # New bar started - emit completed bar
                completed.append({
                    'interval': interval,
                    'symbol': tick.symbol_id,
                    'candle': agg
                })
                # Start new bar
                self.aggregators[interval][tick.symbol_id] = StreamingOHLCV(
                    bar_time, tick.last_price
                )
            
            # Update current bar
            self.aggregators[interval][tick.symbol_id].update(
                tick.last_price, tick.last_volume
            )
        
        return completed
```

---

## 8. Visualization Architecture

### The Dual-Source Data Strategy

**Key Pattern**: Ticks stay in memory, candles go to database.

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (Browser)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────┐     ┌─────────────────────────────┐   │
│   │    Historical       │     │      Real-Time              │   │
│   │    Candles          │     │      TBT Updates            │   │
│   │                     │     │                             │   │
│   │  REST: /api/history │     │  WebSocket: /ws/ticks       │   │
│   │  Source: QuestDB    │     │  Source: Memory Ring Buffer │   │
│   │                     │     │                             │   │
│   │  On: Initial load   │     │  On: Every tick             │   │
│   │      Scroll/pan     │     │      Continuous stream      │   │
│   └─────────────────────┘     └─────────────────────────────┘   │
│              │                            │                      │
│              └────────────┬───────────────┘                      │
│                           ▼                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │          TradingView Lightweight Charts                 │   │
│   │                                                         │   │
│   │   series.setData(history)  +  series.update(liveTick)  │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Backend API (Python FastAPI)

```python
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import questdb.ingress as qi

app = FastAPI()

# Historical data endpoint
@app.get("/api/history")
async def get_history(symbol: str, interval: str = "1m", 
                      start: int = None, end: int = None, limit: int = 500):
    """
    Fetch historical candles from QuestDB.
    For intervals > 1m, aggregates from 1m data using SAMPLE BY.
    """
    interval_map = {
        "1m": "1m", "5m": "5m", "15m": "15m", 
        "1h": "1h", "4h": "4h", "1d": "1d"
    }
    
    sample_by = interval_map.get(interval, "1m")
    
    query = f"""
        SELECT 
            timestamp_floor('{sample_by}', timestamp) as time,
            first(open) as open,
            max(high) as high,
            min(low) as low,
            last(close) as close,
            sum(volume) as volume
        FROM candles_1m
        WHERE symbol = '{symbol}'
        {'AND timestamp >= ' + str(start) if start else ''}
        {'AND timestamp <= ' + str(end) if end else ''}
        SAMPLE BY {sample_by} ALIGN TO CALENDAR
        ORDER BY time DESC
        LIMIT {limit}
    """
    
    result = await questdb_client.query(query)
    return JSONResponse(content=result.to_dict('records'))

# Real-time WebSocket endpoint
@app.websocket("/ws/ticks/{symbol}")
async def websocket_ticks(websocket: WebSocket, symbol: str):
    await websocket.accept()
    
    # Subscribe to Aeron channel for this symbol
    subscription = aeron_subscriber.subscribe(symbol)
    
    try:
        while True:
            # Poll for new ticks (non-blocking)
            tick = await subscription.poll()
            
            if tick:
                # Conflation: only send at 60fps max
                await websocket.send_json({
                    "type": "tick",
                    "time": tick.timestamp_ns // 10**9,
                    "price": tick.last_price,
                    "volume": tick.last_volume
                })
    finally:
        subscription.close()
```

### Frontend Implementation (JavaScript)

```javascript
import { createChart } from 'lightweight-charts';

class TradingChart {
    constructor(container, symbol, interval = '1m') {
        this.symbol = symbol;
        this.interval = interval;
        this.resolution = this.getResolutionMs(interval);
        
        // Initialize chart
        this.chart = createChart(container, {
            width: container.clientWidth,
            height: 500,
            timeScale: { timeVisible: true, secondsVisible: true }
        });
        
        this.candleSeries = this.chart.addCandlestickSeries();
        this.tickBuffer = new TickRingBuffer(50000);  // 5 min at 1000 ticks/sec
        
        // Load initial history
        this.loadHistory();
        
        // Connect WebSocket for real-time
        this.connectWebSocket();
        
        // Setup lazy loading on scroll
        this.setupLazyLoading();
    }
    
    getResolutionMs(interval) {
        const map = {
            '1s': 1000, '5s': 5000, '1m': 60000,
            '5m': 300000, '15m': 900000, '1h': 3600000
        };
        return map[interval] || 60000;
    }
    
    async loadHistory(endTime = null) {
        const params = new URLSearchParams({
            symbol: this.symbol,
            interval: this.interval,
            limit: 500
        });
        if (endTime) params.append('end', endTime);
        
        const response = await fetch(`/api/history?${params}`);
        const candles = await response.json();
        
        // Prepend to existing data
        const existingData = this.candleSeries.data();
        const merged = [...candles.reverse(), ...existingData];
        this.candleSeries.setData(merged);
    }
    
    connectWebSocket() {
        this.ws = new WebSocket(`ws://${window.location.host}/ws/ticks/${this.symbol}`);
        
        this.ws.onmessage = (event) => {
            const tick = JSON.parse(event.data);
            this.processTick(tick);
        };
        
        this.ws.onclose = () => {
            // Reconnect after 1 second
            setTimeout(() => this.connectWebSocket(), 1000);
        };
    }
    
    processTick(tick) {
        // Store in ring buffer for tick charts
        this.tickBuffer.enqueue(tick);
        
        // Get current bar time (floor to resolution)
        const barTime = Math.floor(tick.time / (this.resolution / 1000)) 
                        * (this.resolution / 1000);
        
        // Get last bar from chart
        const data = this.candleSeries.data();
        const lastBar = data.length > 0 ? data[data.length - 1] : null;
        
        if (!lastBar || barTime > lastBar.time) {
            // New bar started
            this.candleSeries.update({
                time: barTime,
                open: tick.price,
                high: tick.price,
                low: tick.price,
                close: tick.price
            });
        } else if (barTime === lastBar.time) {
            // Update existing bar
            this.candleSeries.update({
                time: lastBar.time,
                open: lastBar.open,
                high: Math.max(lastBar.high, tick.price),
                low: Math.min(lastBar.low, tick.price),
                close: tick.price
            });
        }
    }
    
    setupLazyLoading() {
        this.chart.timeScale().subscribeVisibleLogicalRangeChange(
            this.debounce((logicalRange) => {
                if (logicalRange?.from < 10 && !this.loading) {
                    this.loading = true;
                    const data = this.candleSeries.data();
                    const oldestTime = data.length > 0 ? data[0].time : null;
                    
                    this.loadHistory(oldestTime).finally(() => {
                        this.loading = false;
                    });
                }
            }, 100)
        );
    }
    
    debounce(fn, delay) {
        let timeout;
        return (...args) => {
            clearTimeout(timeout);
            timeout = setTimeout(() => fn(...args), delay);
        };
    }
}

// Ring buffer for tick storage
class TickRingBuffer {
    constructor(capacity = 50000) {
        this.capacity = capacity;
        this.buffer = new Array(capacity);
        this.head = 0;
        this.tail = 0;
        this.count = 0;
    }
    
    enqueue(tick) {
        if (this.count === this.capacity) {
            this.head = (this.head + 1) % this.capacity;
        } else {
            this.count++;
        }
        this.buffer[this.tail] = tick;
        this.tail = (this.tail + 1) % this.capacity;
    }
    
    getRecent(n) {
        const result = [];
        let idx = (this.tail - 1 + this.capacity) % this.capacity;
        for (let i = 0; i < Math.min(n, this.count); i++) {
            result.unshift(this.buffer[idx]);
            idx = (idx - 1 + this.capacity) % this.capacity;
        }
        return result;
    }
}
```

### Supporting All Timeframes

| Timeframe Type | Data Source | Implementation |
|----------------|-------------|----------------|
| **Tick charts** | Memory ring buffer | Count N ticks → new bar |
| **Second charts** | Memory ring buffer | Floor timestamp to interval |
| **1m, 5m, 15m, 1h** | QuestDB via SAMPLE BY | Server-side aggregation |
| **Range bars** | Memory ring buffer | New bar when range ≥ threshold |
| **Renko** | Memory ring buffer | New brick when price moves brick size |
| **Custom minutes (3m, 7m)** | Client-side from 1m | TimeframeBuilder.aggregate() |

**Graceful Degradation**: When tick buffer expires for historical tick charts, fall back to 1-minute candle approximation with user notification.

---

## 9. Order Execution & Risk Management

### Execution Flow

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   Strategy    │     │  Risk Engine  │     │    Order      │
│   (Python)    │────►│   (C++)       │────►│   Gateway     │
│               │     │               │     │   (C++)       │
│  Generates    │     │  Pre-trade    │     │               │
│  OrderIntent  │     │  validation   │     │  Signs &      │
└───────────────┘     └───────────────┘     │  transmits    │
                                            └───────┬───────┘
                                                    │
                      ┌─────────────────────────────┼─────────────────────────────┐
                      │                             │                             │
                      ▼                             ▼                             ▼
              ┌───────────────┐             ┌───────────────┐             ┌───────────────┐
              │  Fyers REST   │             │  Binance REST │             │  Fyers Order  │
              │  Order API    │             │  Order API    │             │  WebSocket    │
              │  (~50ms RTT)  │             │  (~50ms RTT)  │             │  (confirms)   │
              └───────────────┘             └───────────────┘             └───────────────┘
```

### Pre-Trade Risk Checks (C++)

```cpp
struct RiskLimits {
    double max_order_value;
    double max_position_value;
    double max_loss_per_day;
    double fat_finger_threshold_pct;  // Max deviation from LTP
    int max_orders_per_second;
};

class RiskEngine {
public:
    enum class RiskResult { APPROVED, REJECTED_VALUE, REJECTED_POSITION, 
                           REJECTED_LOSS, REJECTED_PRICE, REJECTED_RATE };
    
    RiskResult validate(const OrderIntent& order, const MarketState& state) {
        // 1. Order value check
        double order_value = order.quantity * order.price;
        if (order_value > limits_.max_order_value) {
            return RiskResult::REJECTED_VALUE;
        }
        
        // 2. Position limit check
        double new_position = state.current_position + 
                              (order.side == Side::BUY ? order.quantity : -order.quantity);
        if (std::abs(new_position * state.last_price) > limits_.max_position_value) {
            return RiskResult::REJECTED_POSITION;
        }
        
        // 3. Daily loss check
        if (state.daily_pnl < -limits_.max_loss_per_day) {
            return RiskResult::REJECTED_LOSS;
        }
        
        // 4. Fat finger check
        double price_deviation = std::abs(order.price - state.last_price) / state.last_price;
        if (price_deviation > limits_.fat_finger_threshold_pct) {
            return RiskResult::REJECTED_PRICE;
        }
        
        // 5. Rate limit check
        if (order_rate_limiter_.check() == false) {
            return RiskResult::REJECTED_RATE;
        }
        
        return RiskResult::APPROVED;
    }
    
private:
    RiskLimits limits_;
    TokenBucketRateLimiter order_rate_limiter_;
};
```

### Latency Considerations

**Fyers**: Order placement via REST/Socket ~50ms round-trip. Python overhead (microseconds) is negligible compared to network latency.

**Binance**: REST API ~50ms round-trip. For latency-sensitive strategies, use WebSocket order entry.

**Bottom Line**: Unless doing sub-100ms latency arbitrage, Python execution is acceptable. The architecture supports C++ execution upgrade path without redesign.

---

## 10. Complete Technology Stack

| Layer | Component | Technology | License |
|-------|-----------|------------|---------|
| **Core Engine** | Framework pattern | NautilusTrader-inspired | LGPL-3.0 |
| **Feed Handler** | NSE Connector | C++17, simdjson, Boost.Beast | Apache/BSD |
| **Feed Handler** | Binance Connector | C++17, SBE, Boost.Beast | Apache/BSD |
| **IPC** | Data Plane | Aeron | Apache 2.0 |
| **IPC** | Control Plane | ZeroMQ | LGPL |
| **Time-Series DB** | Candle Storage | QuestDB | Apache 2.0 |
| **Cache** | Session State | KeyDB (multi-threaded Redis fork) | BSD-3 |
| **API** | REST/WebSocket | FastAPI + uvicorn | MIT |
| **Python WS** | Client Library | websockets | BSD |
| **Charts** | Visualization | TradingView Lightweight Charts v5.1 | Apache 2.0 |
| **Monitoring** | Metrics | Prometheus | Apache 2.0 |
| **Monitoring** | Dashboards | Grafana | AGPL |
| **C++/Python** | Interop | nanobind | BSD |

---

## 11. Performance Benchmarks & Latency Budget

| Component | Expected Latency | How to Achieve |
|-----------|------------------|----------------|
| Fyers WS → Buffer | <10ms | simdjson parsing, dedicated thread |
| Binance WS → Buffer | <15ms | SBE decoding, combined streams |
| Buffer → Aggregator | <1μs | Aeron shared memory |
| OHLCV Update | <100ns | O(1) arithmetic, no allocation |
| ZeroMQ PUB | ~10μs | Pre-allocated buffers |
| Strategy Signal | 10-100μs | Vectorized NumPy operations |
| Risk Check | <100ns | C++ pre-trade validation |
| QuestDB Write | <1ms | Async ILP batch |
| **End-to-end (typical)** | **15-25ms** | Exchange latency dominant |

### Memory Budget

| Component | Allocation | Notes |
|-----------|------------|-------|
| Tick Ring Buffers | 7.5 GB | 50 symbols × 150MB |
| QuestDB | 4 GB | WAL + query cache |
| Python Processes | 2 GB | Strategy + API |
| System Overhead | 2.5 GB | OS, monitoring |
| **Total Recommended** | **16 GB** | With 2x safety margin |

---

## 12. Implementation Roadmap

### Phase 1: Python Prototype (Weeks 1-4)

1. **Basic Data Pipeline**
   - Python WebSocket connections to Fyers and Binance
   - Simple tick aggregation to 1-minute candles
   - QuestDB setup with basic schema

2. **Visualization MVP**
   - FastAPI backend serving historical data
   - TradingView Lightweight Charts integration
   - WebSocket push for live updates

3. **Validation**
   - Verify data correctness against exchange data
   - Measure baseline latencies

### Phase 2: Performance Optimization (Weeks 5-8)

1. **Profile and Identify Bottlenecks**
   - Use `py-spy` for Python profiling
   - Identify GIL contention points

2. **Selective C++ Migration**
   - Replace JSON parsing with simdjson (nanobind wrapper)
   - Implement lock-free ring buffers

3. **IPC Upgrade**
   - Deploy Aeron Media Driver
   - Migrate tick data path to shared memory

### Phase 3: Production Hardening (Weeks 9-12)

1. **Risk Management**
   - C++ pre-trade risk engine
   - Order rate limiting
   - Position tracking

2. **Monitoring & Alerting**
   - Prometheus metrics integration
   - Grafana dashboards
   - Latency histogram tracking

3. **Fault Tolerance**
   - WebSocket reconnection logic
   - Binance 24-hour disconnect handling
   - QuestDB WAL for crash recovery

### Key Principle

> "Start with Python-only prototype using ZeroMQ for IPC. Profile and identify actual bottlenecks before C++ migration. Use nanobind for surgical C++ optimization of hot spots. Deploy QuestDB with WAL enabled from day one."

---

## 13. Conclusion

This architecture prioritizes **operational simplicity over theoretical perfection**:

1. **QuestDB's single-binary deployment** and `SAMPLE BY` syntax eliminate ClickHouse cluster complexity while providing sufficient performance for candle storage.

2. **The Python/C++ split** follows industry best practices: Python accelerates strategy research iteration while C++ ensures deterministic execution latency.

3. **The dual-source data strategy** (ticks in memory, candles in database) solves the fundamental tension between TBT visualization and storage efficiency.

4. **The complete stack remains 100% open source**, avoiding vendor lock-in while matching architectural patterns used by professional trading firms.

The system achieves both capabilities—real-time tick-by-tick visualization AND lightweight historical storage—without storing petabytes of tick data. Start with Python, profile ruthlessly, and optimize surgically with C++ only where measurements demand it.

---

## Appendix A: Quick Start Commands

```bash
# QuestDB
docker run -p 9000:9000 -p 9009:9009 -p 8812:8812 questdb/questdb

# KeyDB (Redis alternative, 5x faster)
docker run -p 6379:6379 eqalpha/keydb

# Aeron Media Driver
java -jar aeron-all-*.jar io.aeron.driver.MediaDriver

# Python environment
pip install fastapi uvicorn questdb websockets numpy pandas aeron-python

# Build C++ feed handler
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

## Appendix B: Key Configuration Files

### QuestDB server.conf
```ini
# /var/lib/questdb/conf/server.conf
line.tcp.enabled=true
line.tcp.port=9009
pg.enabled=true
pg.port=8812
http.enabled=true
http.port=9000
```

### Aeron aeron.properties
```properties
# Media Driver configuration
aeron.dir=/dev/shm/aeron
aeron.term.buffer.length=16777216
aeron.ipc.term.buffer.length=67108864
```
