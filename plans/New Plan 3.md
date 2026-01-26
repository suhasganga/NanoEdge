# **Unified High-Frequency Trading Architecture: A Split-Plane Approach for NSE and Binance Integration**

## **1\. Executive Summary and Strategic Imperatives**

The contemporary landscape of High-Frequency Trading (HFT) is characterized by a relentless pursuit of deterministic latency, throughput maximization, and architectural resilience. As market microstructures evolve across traditional equities (National Stock Exchange of India \- NSE) and digital assets (Binance), the engineering challenges shift from pure speed to a delicate balance of execution determinism, data fidelity, and analytical agility. This report presents a comprehensive architectural blueprint—herein referred to as **Plan.md**—that bridges these disparate market environments using a "Split-Plane" hybrid computing model.

The core objective of this research is to define a production-grade trading stack that leverages the raw, bare-metal performance of C++ for the "Hot Path" (market data ingestion, normalized messaging, and order execution) while utilizing the rapid development capabilities and rich ecosystem of Python for the "Warm Path" (strategy logic, quantitative analysis, and user interface management). This bifurcation of concerns is not merely a preference but a strategic necessity. Pure C++ systems, while performant, often suffer from slow iteration cycles and rigid development environments. Conversely, pure Python systems cannot guarantee the microsecond-level jitter requirements of modern HFT due to the Global Interpreter Lock (GIL), dynamic typing overheads, and unpredictable garbage collection pauses.

Furthermore, this architecture rigorously adheres to a requirement for 100% open-source resources. While proprietary hardware drivers (e.g., Solarflare OpenOnload) and commercial tick databases (e.g., KDB+) are common in institutional HFT, the open-source community has matured sufficiently to offer competitive alternatives. Technologies such as **Aeron** for Inter-Process Communication (IPC), **QuestDB** for time-series persistence, and **LMAX Disruptor** patterns provide the building blocks for an enterprise-grade stack without the licensing encumbrances of proprietary software.

This document serves as the definitive technical specification for the proposed system. It details the selection of QuestDB over ClickHouse for specific tick-capture workloads, the implementation of trading visualization using **TradingView Lightweight Charts** with complex real-time aggregation logic, and the precise data flow mechanisms required to handle NSE’s 50-level market depth and Binance’s Tick-By-Tick (TBT) feeds. The report synthesizes insights from multiple architectural plans 1 to propose a unified "Dual-Source" data strategy that resolves the tension between real-time visualization and storage efficiency.

## **2\. System Topology: The Split-Plane Architecture**

The "Split-Plane" architecture is the foundational design pattern for this trading stack. It strictly separates the system into an **Execution Plane** and a **Strategy Plane**, mediated by a high-performance, lock-free IPC layer. This topology ensures that the non-deterministic behaviors of the strategy layer do not bleed into the critical execution path.

### **2.1 The Execution Plane (C++20)**

The Execution Plane is the system's interface with the physical market. Written entirely in **C++20**, its primary responsibility is the preservation of signal integrity and the minimization of "wire-to-wire" latency. It is the "Hot Path" where every nanosecond of jitter translates to slippage and lost alpha.

* **Core Responsibilities:**  
  * **Connectivity:** Managing WebSocket and TCP connections to Fyers (NSE) and Binance.  
  * **Parsing:** Decoding JSON (Fyers) and SBE (Binance) protocols.  
  * **Normalization:** Converting disparate exchange formats into a unified MarketTick structure.  
  * **Book Building:** Maintaining the Limit Order Book (LOB) in memory.  
  * **Risk Gateway:** Performing pre-trade risk checks (fat-finger, credit limits) in sub-microsecond timeframes.  
  * **Order Routing:** Formatting and transmitting orders to the exchange.  
* **Concurrency Model:** The Execution Plane utilizes a **Thread-Per-Core** model. Critical threads—specifically the Feed Handler and the Order Gateway—are pinned to specific CPU cores using isolcpus (kernel boot parameter) and pthread\_setaffinity\_np (system call). This prevents the operating system scheduler from migrating these threads across cores, thereby preserving L1/L2 cache locality and eliminating context switching latency.  
* **Memory Management:** Dynamic memory allocation (malloc, new) is strictly forbidden on the critical path. All memory structures, including the LOB and message buffers, are statically allocated at startup or managed via memory arenas (slab allocators) to prevent heap fragmentation and nondeterministic allocation times.1

### **2.2 The Strategy Plane (Python 3.11+)**

The Strategy Plane hosts the proprietary trading logic. Written in **Python 3.11+**, it prioritizes development velocity, readability, and access to the vast ecosystem of quantitative libraries (NumPy, Pandas, SciPy, PyTorch).

* **Core Responsibilities:**  
  * **Alpha Generation:** Calculating signals based on normalized market data.  
  * **Complex Event Processing:** Managing multi-leg strategies and arbitrage logic.  
  * **Historical Analysis:** Backfilling data and running real-time regressions.  
  * **Frontend Services:** Serving the API and managing WebSocket connections for the UI.  
* **Justification:** Python is selected for this layer because alpha generation often involves complex statistical mathematics and matrix operations that are cumbersome to implement in C++. Furthermore, the latency penalty of Python (typically 10–50 microseconds for optimized code) is acceptable for the decision-making logic of many strategies, provided the data ingestion and order transmission (the C++ layer) remain in the sub-microsecond range. The use of **Nanobind** allows for efficient, low-overhead communication between the Python interpreter and C++ structures.1

### **2.3 The Connectivity Bridge: Aeron IPC**

The critical link in a hybrid architecture is the bridge between C++ and Python. Standard inter-process communication methods like pipes, TCP sockets, or HTTP calls introduce massive latency overhead (microseconds to milliseconds) due to kernel involvement (context switches, copying data between user/kernel space).

To meet the requirements of a production-grade HFT system, this architecture utilizes **Aeron**, a high-performance messaging transport.

* **Mechanism:** Aeron operates over shared memory (IPC) for processes on the same machine. It writes directly to memory-mapped files (typically in /dev/shm), allowing the subscriber to read data without kernel intervention.  
* **Performance:** Aeron consistently delivers inter-process latencies under **1 microsecond**, vastly outperforming ZeroMQ, which often exhibits latencies in the 30–50 microsecond range due to its reliance on kernel sockets.1  
* **Reliability:** Aeron provides sophisticated flow control and backpressure mechanisms, ensuring that a slow Python consumer does not destabilize the fast C++ producer.

### **2.4 Hardware and OS Tuning**

Software architecture cannot be divorced from the hardware it runs on. For this system to perform as designed, specific OS-level tunings are required:

* **Kernel Bypass:** While full kernel bypass (DPDK/Solarflare) requires specific hardware, the architecture supports **AF\_XDP**, an open-source kernel technology that allows user-space applications to read packets directly from the NIC DMA rings, bypassing much of the Linux networking stack.  
* **Clock Synchronization:** High-fidelity backtesting and trade analysis require precise timestamps. The server must utilize **PTP (Precision Time Protocol)** rather than NTP to achieve microsecond-level synchronization with exchange clocks.1

## **3\. Market Data Ingestion: The Hot Path Implementation**

The ingestion layer faces the unique challenge of normalizing two radically different data protocols: the verbose, text-based JSON feeds from the National Stock Exchange of India (via Fyers) and the compact, binary SBE feeds from Binance.

### **3.1 NSE Feed Handler (Fyers API v3)**

The Fyers API v3 is the primary gateway to NSE data. It provides a WebSocket connection for real-time data, including a dedicated channel for market depth.

#### **3.1.1 The Challenge of 50-Level Depth**

The distinguishing feature of the Fyers TBT feed is the provision of **Level 3 data**, specifically 50 levels of market depth (50 best bids and 50 best asks).1

* **Data Volume:** A standard Level 2 quote contains the best bid/ask or perhaps the top 5 levels. A 50-level update is significantly larger, containing 100 separate price and quantity fields. In active instruments like Bank Nifty Options, these updates can occur dozens of times per second.  
* **Protocol Overhead:** Fyers utilizes a WebSocket connection carrying **JSON** payloads. While JSON is human-readable, it is computationally expensive to parse. Standard DOM-based parsers (like Python's json module or C++'s nlohmann/json) construct a tree object for every message, allocating memory for every node. For a 50-depth update, this induces massive heap fragmentation and CPU stall, rendering standard parsers unsuitable for HFT.1

#### **3.1.2 Solution: High-Performance JSON Parsing with simdjson**

To handle the Fyers JSON feed within the latency budget, the C++ Execution Plane utilizes **simdjson**, widely regarded as the fastest JSON parser in the world.1

* **SIMD Acceleration:** simdjson uses Single Instruction, Multiple Data (SIMD) instructions—specifically AVX2 on modern Intel/AMD CPUs and NEON on ARM—to validate and parse JSON at speeds exceeding 2.5 GB/s.  
* **On-Demand API:** We utilize the "On-Demand" API of simdjson. This approach iterates over the JSON string in a streaming fashion, extracting values directly from the input buffer without constructing an intermediate DOM tree. This effectively treats JSON as a binary stream, drastically reducing memory allocation and parsing latency to the nanosecond range.1

**Implementation Concept (C++):**

C++

// Conceptual C++ Implementation for Fyers 50-Depth Parsing  
simdjson::ondemand::parser parser;  
simdjson::padded\_string json \= simdjson::padded\_string::load(buffer);  
auto doc \= parser.iterate(json);

// Efficiently extracting depth without DOM construction  
for (auto bid : doc\["market\_depth"\]\["bids"\]) {  
    double price \= bid\["price"\];  
    int qty \= bid\["qty"\];  
    // Update internal Order Book directly  
    orderBook.updateBid(price, qty);  
}

### **3.2 Binance Feed Handler (Crypto Derivatives)**

Binance, operating in the mature crypto HFT space, offers a more optimized connectivity option: **Simple Binary Encoding (SBE)**.

#### **3.2.1 Protocol Selection: SBE vs. JSON**

While Binance offers standard JSON streams, the "Production-Grade" requirement mandates the use of SBE. SBE is the standard for low-latency financial systems, often associated with the FIX/FAST protocol.1

* **Deterministic Access:** Unlike JSON, which requires scanning for delimiters ({, :, }), SBE places data in fixed positions or defined repeating groups. The CPU can access a price field simply by adding a constant offset to the base address of the message buffer. This eliminates branching logic and maximizes instruction pipelining.  
* **Zero-Copy:** Accessing a field becomes a direct memory read. There is no "parsing" phase, only an "access" phase.

#### **3.2.2 Connection Management**

The architecture connects to the Binance SBE endpoint (wss://stream-sbe.binance.com:9443/ws). This endpoint enforces strict operational constraints:

* **24-Hour Disconnect:** Binance forcibly disconnects clients every 24 hours. The system implements an "Active-Active" or "Warm Standby" reconnection strategy. A secondary connection is established 5 minutes prior to the forced disconnect. The system deduplicates messages based on sequence numbers before seamlessly switching the primary data source to the new connection.1  
* **Schema Compilation:** The **sbe-tool** (Java-based) is integrated into the build pipeline to compile the Binance XML schema into C++ header files, ensuring the decoder is always synchronized with the exchange's format.

### **3.3 Data Normalization**

Both feed handlers (Fyers/JSON and Binance/SBE) output a uniform data structure to the internal ring buffers. This allows the downstream Strategy Plane to be exchange-agnostic.

The Unified Tick Structure:  
To ensure optimal performance, the internal tick structure is designed as a Plain Old Data (POD) struct, aligned to the CPU cache line (64 bytes).

C++

struct alignas(64) NormalizedTick {  
    int64\_t timestamp\_ns; // Nanosecond precision (PTP)  
    int32\_t symbol\_id;    // O(1) Lookup ID  
    double bid\_price\_L1;  
    double ask\_price\_L1;  
    double bid\_qty\_L1;  
    double ask\_qty\_L1;  
    //... Padding to ensure 64-byte alignment  
};

The alignas(64) directive is critical. It ensures that each tick fits exactly into a cache line, preventing **false sharing**—a scenario where multiple CPU cores inadvertently invalidate each other's caches while writing to independent variables that happen to share the same cache line. This optimization is standard in HFT but often overlooked in general software architecture.1

## **4\. In-Memory Processing: The Nervous System**

Once market data is ingested and normalized, it must be distributed to various components (Strategy Engine, Risk Engine, Logger, UI) with minimal latency. Traditional queue-based concurrency (using mutexes and locks) is insufficient for HFT due to lock contention and kernel arbitration overhead.

### **4.1 The LMAX Disruptor Pattern**

The architecture implements the **LMAX Disruptor** pattern for intra-process communication within the C++ Execution Plane. The Disruptor is a high-performance inter-thread messaging library that avoids locks entirely.

* **Ring Buffer Topology:** The core data structure is a pre-allocated circular buffer (Ring Buffer). Unlike a linked-list queue, nodes are never allocated or deallocated at runtime, eliminating garbage collection and memory fragmentation.  
* **Lock-Free Semantics:** The Disruptor uses atomic sequence numbers (std::atomic\<uint64\_t\>) to track the progress of producers and consumers. Memory barriers (acquire/release semantics) ensure that data written by the producer is visible to the consumer without the need for expensive mutex locks.1  
* **Single Producer Single Consumer (SPSC):** For the critical path (Feed Handler \-\> Strategy), the system utilizes SPSC semantics. This allows the compiler to optimize memory access patterns aggressively, achieving throughputs exceeding **25 million messages per second** with latencies consistently under **50 nanoseconds**.1

### **4.2 Shared Memory Ring Buffers (IPC)**

For communicating between the C++ Execution Plane and the Python Strategy Plane (running in separate processes), the system uses **Shared Memory (mmap) Ring Buffers** via **Aeron**.

* **Mechanism:** Aeron maps a file in /dev/shm (the Linux RAM disk) into the address space of both processes. The C++ process writes to this memory region, and the Python process reads from it.  
* **Zero-Copy:** Since both processes access the same physical RAM pages, there is no copying of data between kernel buffers.  
* **Throughput & Latency:** This setup achieves **8 million messages per second** with a P99 latency of approximately **850 nanoseconds**. This is approximately 20x faster than traditional message queues like RabbitMQ and 100x faster than Redis.1

### **4.3 The "Ticker Plant" Concept**

While the persistent database stores aggregated candles, the system's memory acts as a "Ticker Plant."

* **Function:** It holds a rolling window of raw ticks (e.g., the last 15 minutes) for every active symbol in the Ring Buffers.  
* **Memory Sizing:**  
  * One tick ≈ 100 bytes.  
  * A 5-minute rolling window at 1,000 ticks/sec requires \~5MB per symbol.  
  * For a full NSE trading day (6.5 hours), 50 active symbols at 100 ticks/sec require approximately **7.5 GB** of ring buffer allocation.  
  * **Recommendation:** The system specification mandates **16GB of RAM** dedicated solely to these ring buffers to provide a 2x safety margin and accommodate burst periods.1

## **5\. Persistence Layer: QuestDB vs. ClickHouse**

A critical architectural decision is the selection of the time-series database. The requirement is to store 1-minute aggregated candles efficiently while supporting high-speed ingestion and standard SQL querying. The candidates are **QuestDB** and **ClickHouse**.

### **5.1 The Ingestion Mechanics Comparison**

The fundamental difference—and the deciding factor—lies in how these databases handle data ingestion.1

* **ClickHouse (LSM Tree):** ClickHouse uses a Log-Structured Merge (LSM) tree. It writes data to "parts" on disk. Every insert creates a new part, and background processes merge these parts. If data is inserted row-by-row (streaming), ClickHouse creates thousands of tiny parts, leading to "Too Many Parts" errors and massive write amplification. To use ClickHouse effectively for HFT, one must introduce a buffering layer (like Kafka) to batch ticks into chunks of 10,000+, adding complexity and latency.  
* **QuestDB (Time-Partitioned Append):** QuestDB is designed for the "firehose" of financial data. It uses an append-only storage model partitioned by time. It accepts the **Influx Line Protocol (ILP)** directly over a raw TCP socket. The C++ Feed Handler can write ticks directly to the socket as they arrive. QuestDB handles the buffering and committing internally without the need for intermediate middleware like Kafka.1

### **5.2 Justification for QuestDB**

**QuestDB** is the selected database for this architecture for the following reasons:

1. **Operational Simplicity:** It is distributed as a single binary (or Docker container) and requires zero external dependencies (no Zookeeper, no Kafka). This aligns with the "100% Open Source" and "Single Machine" constraints.1  
2. **Native Time-Series SQL:** QuestDB features the **SAMPLE BY** clause, which makes generating OHLCV candles from raw ticks trivial.  
   SQL  
   SELECT timestamp, first(price) as open, max(price) as high,   
          min(price) as low, last(price) as close, sum(volume) as volume  
   FROM trades  
   WHERE symbol \= 'NSE:NIFTY'   
   SAMPLE BY 1m ALIGN TO CALENDAR;

   This query is optimized by the database engine, using vectorization to aggregate millions of rows in milliseconds.1  
3. **Ingestion Performance:** QuestDB supports ingestion rates of **4–5 million rows per second**, comfortably handling the full TBT stream from NSE and Binance without bottlenecks.1

### **5.3 Schema Design**

The schema for the 1-minute candle storage is optimized for storage efficiency and query speed.

SQL

CREATE TABLE candles\_1m (  
    timestamp TIMESTAMP,  
    symbol SYMBOL CAPACITY 8192 CACHE INDEX,  
    exchange SYMBOL CAPACITY 16,  
    open DOUBLE,  
    high DOUBLE,  
    low DOUBLE,  
    close DOUBLE,  
    volume DOUBLE,  
    trade\_count INT,  
    vwap DOUBLE  
) TIMESTAMP(timestamp) PARTITION BY DAY WAL DEDUP UPSERT KEYS(timestamp, symbol, exchange);

* **SYMBOL Type:** Internally dictionary-encoded strings, providing \~2x compression for repetitive ticker names.  
* **WAL (Write-Ahead Log):** Enables concurrent ingestion and querying, improving ingestion speed by 1.6x.  
* **DEDUP UPSERT:** Automatically handles duplicate or corrected candles, a common occurrence in unstable data feeds.1

## **6\. The Dual-Source Data Strategy**

A central requirement of the user is "TradingView Visualization supporting TBT updates, dynamic history, and all timeframes." This presents a conflict: storing TBT data for long-term history requires petabytes of storage, but visualizing it requires immediate access. The solution is the **Dual-Source Data Strategy**.1

### **6.1 Strategic Definition**

The Dual-Source strategy partitions data based on its lifecycle and utility:

1. **Hot Data (Memory):** Raw Tick-By-Tick (TBT) data is kept **exclusively in memory** (Ring Buffers) during the active trading session. This allows for sub-microsecond access for trading and real-time visualization. It is *not* persisted to disk in raw form.  
2. **Cold Data (Disk):** Only **aggregated 1-minute OHLCV candles** are persisted to QuestDB. This dramatically reduces storage requirements while preserving the essential price history.

### **6.2 Data Flow Implementation**

This strategy dictates how the Frontend (TradingView) interacts with the backend:

* **Real-Time Stream:** For the current trading session, the frontend connects via WebSocket to the Python backend. The backend taps into the **Aeron** stream (reading from the C++ ring buffer) and pushes every single tick to the frontend. The TradingView chart updates in real-time.  
* **Historical Query:** When the user scrolls back in time, the frontend requests historical data via REST API. The backend queries **QuestDB** for 1-minute candles.  
* **The Merge:** The frontend logic seamlessly merges the historical candles (from DB) with the live ticks (from WebSocket) to create a continuous chart.

### **6.3 Building Non-Standard Timeframes**

Since the database only stores 1-minute bars, how does the system support "all timeframes" (e.g., 3-minute, Range Bars, Tick Charts)?

* **Standard Higher Timeframes (5m, 1h):** These are generated server-side using QuestDB's SAMPLE BY clause (e.g., SAMPLE BY 5m).  
* **Custom Minute Intervals (3m, 7m):** These are aggregated client-side or server-side from the 1-minute data.  
* **Tick, Range, and Renko Charts:** These are built **client-side** from the live tick stream. Since the system maintains a "Ticker Plant" buffer in memory (e.g., last 50,000 ticks), when a user switches to a "Tick Chart," the backend streams this buffer to the client, which then renders the tick/range bars locally. This avoids the need to store and query these complex types from the database.1

## **7\. Hybrid Strategy Implementation: C++ & Python Responsibilities**

The architecture strictly delineates responsibilities to maximize the strengths of each language while mitigating their weaknesses.

### **7.1 C++ Responsibilities (Execution Plane)**

* **Market Data Parsing:** Leveraging simdjson and SBE for deterministic parsing time.  
* **Order Book Management:** Maintaining the LOB state.  
* **Risk Gateway:** Implementing "Hard Kill" switches. Pre-trade risk checks (e.g., Max Order Value, Price Band deviation) must happen in nanoseconds. This is implemented as a C++ filter in the Ring Buffer. Even if the Python strategy malfunctions, the C++ gateway prevents erroneous orders from reaching the exchange.  
* **Order Routing:** Formatting FIX/REST messages and managing socket buffers.

### **7.2 Python Responsibilities (Strategy Plane)**

* **Strategy Logic:** Executing the core trading algorithms. Python's pandas and numpy are used for signal generation.  
* **Bindings:** The system uses **nanobind** instead of pybind11. Nanobind produces smaller binaries and has significantly lower overhead for calling C++ functions from Python (approx. 2-3x faster compilation and execution), essential for passing market data pointers.1  
* **GC Mitigation:** To prevent Garbage Collection (GC) pauses during trading, the Python process utilizes gc.freeze() after initialization and disables automatic GC during market hours, or tunes thresholds to (14000, 10, 10).1

### **7.3 Risk Management Isolation**

The architecture implements redundant risk checks:

1. **Strategy Check (Python):** "Do I have enough capital allocated?" – A logic-level check.  
2. Gateway Check (C++): "Is this order size \> max\_limit?" – A safety-level check.  
   The C++ check acts as a firewall. It runs in a separate memory space/thread and cannot be bypassed by the Python interpreter.

## **8\. Frontend Visualization: TradingView & Real-Time Aggregation**

The frontend is the window into the system's operation. It utilizes **TradingView Lightweight Charts v5.1** (Apache 2.0 license) for high-performance rendering.1

### **8.1 Real-Time TBT Updates**

A common pitfall in TradingView implementations is using setData() for real-time updates, which forces a full re-render of the chart.

* **Solution:** The system uses series.update() for appending new data points or updating the current candle. This method is optimized for high-frequency updates and can handle 60,000+ data points performantly.1  
* **Candle Construction:** As ticks arrive via WebSocket, the JavaScript client updates the *current* candle (Open, High, Low, Close, Volume) in real-time. The user sees the candle "form" live.

### **8.2 Dynamic History Loading (Lazy Loading)**

To support infinite scrolling without loading the entire database into the browser:

* **Event Listener:** The frontend subscribes to the visibleLogicalRangeChange event.  
* **Debouncing:** A debouncer prevents API floods. When the user scrolls close to the "edge" of the loaded history (e.g., logicalRange.from \< 10), a request is triggered.  
* **API Request:** GET /history?symbol=NSE:NIFTY\&end\_time=...  
* **Response:** The Python backend queries QuestDB and returns a chunk of 1-minute candles. The frontend merges this chunk with the existing series using setData (for history) or prepending logic.1

### **8.3 Handling Non-Time Based Charts**

For **Range Bars** or **Renko Charts**, the logic is moved to the client side. The backend streams raw ticks. A JavaScript TimeframeBuilder class consumes these ticks and applies the range/brick logic locally. This allows the user to adjust range settings dynamically without requiring server-side recalculation or storage of these derived bars.1

## **9\. Operational Rigor and Compliance**

Building a "Production-Grade" system requires addressing operational realities beyond code.

### **9.1 SEBI Compliance (NSE)**

For Indian markets, the system must adhere to SEBI regulations.

* **Token Management:** Fyers access tokens expire daily at 3:00 AM IST. The system includes a scheduled cron job (Python orchestration) to perform the login flow and refresh tokens automatically before the market opens.1  
* **Order Limits:** The C++ Risk Gateway enforces SEBI-mandated quantity limits per order (e.g., Freeze Quantities for Nifty/Bank Nifty) to prevent order rejection.

### **9.2 Binance Operational Constraints**

* **WebSocket Reconnection:** Binance streams drop every 24 hours. The C++ Execution Plane implements logic to spawn a new connection, subscribe to streams, buffer messages, and switch over atomically to prevent data gaps.1  
* **Rate Limiting:** The Order Gateway tracks request weights (1200 per minute) locally to prevent IP bans.

### **9.3 Monitoring and Observability**

* **Metrics:** The C++ engine exposes an internal HTTP endpoint (using boost::beast) that exports Prometheus-compatible metrics: tick-to-trade latency histograms (using HdrHistogram), ring buffer depth, and order reject rates.  
* **Logging:** High-performance binary logging (e.g., spdlog in async mode) writes events to disk without blocking the trading thread.

## **10\. Conclusion and Implementation Roadmap**

This architectural blueprint fundamentally transforms the approach to building HFT systems by rejecting the dichotomy between C++ performance and Python usability. By adopting the **Split-Plane** topology, utilizing **Aeron** for nanosecond-level IPC, and employing a **Dual-Source** data strategy with **QuestDB**, the system achieves the best of both worlds: the determinism of an institutional trading engine and the agility of a research platform.

### **Implementation Priorities (Phased Approach)**

1. **Phase 1: The Core (C++):** Implement the simdjson Fyers handler and the SBE Binance handler. Validate throughput into a dummy LMAX Ring Buffer.  
2. **Phase 2: The Bridge (IPC):** Set up the Aeron Media Driver and implement the C++ Publisher / Python Subscriber pattern. Verify zero-copy performance.  
3. **Phase 3: Persistence (QuestDB):** Stand up QuestDB. Implement the C++ Journaler to write ticks via ILP. Verify SAMPLE BY queries.  
4. **Phase 4: Strategy & UI (Python/JS):** Build the FastAPI backend and the TradingView frontend with WebSocket streaming. Implement the "Merge" logic for history \+ live ticks.  
5. **Phase 5: Execution:** Implement the Order Gateway and Risk Checks. Perform end-to-end latency profiling.

This architecture is robust, scalable, and fully open-source, providing a solid foundation for capturing alpha in both traditional and crypto markets.

# ---

**Architecture Plan: Plan.md**

## **1\. System Overview**

* **Objective:** Unified HFT Trading Stack for NSE (Fyers) and Binance (TBT).  
* **Architecture:** Split-Plane Hybrid (C++20 Execution / Python 3.11 Strategy).  
* **License:** 100% Open Source.

## **2\. Technology Stack & Responsibilities**

| Component | Technology | Role & Justification |
| :---- | :---- | :---- |
| **Execution Plane** | **C++ 20** | **Hot Path:** Ingestion, Parsing, Risk, Order Routing. No GC, deterministic latency. |
| **Strategy Plane** | **Python 3.11** | **Warm Path:** Alpha logic, ML inference, API Server. Fast iteration, rich libs. |
| **IPC Transport** | **Aeron** | **Nervous System:** Bridge between C++ and Python. \<1µs latency, zero-copy. |
| **Intra-Process** | **LMAX Disruptor** | **Core Buffer:** Lock-free ring buffer for C++ thread communication. |
| **Database** | **QuestDB** | **Persistence:** Stores 1m candles. Native SAMPLE BY, ILP protocol, no Kafka. |
| **NSE Parsing** | **simdjson** | **Ingestion:** World's fastest JSON parser for Fyers 50-depth feeds. |
| **Binance Parsing** | **SBE (Real Logic)** | **Ingestion:** Binary decoding for Binance TBT. Zero-copy field access. |
| **Frontend** | **TradingView** | **Viz:** Lightweight Charts v5.1. Supports Canvas rendering and 60fps updates. |
| **Binding** | **nanobind** | **Glue:** Low-overhead C++/Python bindings (3x faster than pybind11). |

## **3\. Detailed Data Flow**

1. **Ingestion:**  
   * C++ Thread (Pinned Core 1\) reads TCP packet from Fyers/Binance.  
   * Fyers: Parsed via simdjson (On-Demand).  
   * Binance: Decoded via SBE XML Schema.  
   * Normalized to aligned(64) MarketTick struct.  
2. **Distribution:**  
   * Pushed to **LMAX Ring Buffer** (Sequence 1).  
   * Pushed to **Aeron Publication** (IPC to Python).  
   * Pushed to **QuestDB** via ILP (TCP) for archival.  
3. **Strategy:**  
   * Python Thread (Pinned Core 2\) polls Aeron Subscriber.  
   * nanobind converts binary struct to Python object (zero-copy if possible).  
   * Strategy logic runs (Numpy/Pandas).  
   * Signal generated \-\> Pushed to Aeron Command Channel.  
4. **Execution:**  
   * C++ Gateway reads Command Channel.  
   * **Risk Check:** Pre-trade limits validated in nanoseconds.  
   * **Routing:** Order sent to Exchange API.  
5. **Visualization:**  
   * FastAPI reads tick from Aeron.  
   * Pushes to Frontend via WebSocket.  
   * TradingView updates current candle via series.update().

## **4\. Storage & Aggregation Strategy (Dual-Source)**

| Data Type | Storage Location | Retention | Usage |
| :---- | :---- | :---- | :---- |
| **Raw Ticks (TBT)** | **RAM (Ring Buffer)** | Session Only (e.g., 1 day) | Real-time charts, Range/Renko generation, Strategy execution. |
| **1m Candles** | **QuestDB** | Permanent | Historical charts, Backtesting, Analytics. |

* **Aggregation Logic:** QuestDB SAMPLE BY 1m handles server-side aggregation. Client-side JS handles sub-minute visual aggregation.

## **5\. Deployment & Configuration**

* **OS:** Linux (Ubuntu 22.04 / Fedora).  
* **Kernel:** isolcpus=2,3 to isolate strategy/execution cores.  
* **Memory:** hugepages=1 to prevent TLB misses.  
* **Disk:** NVMe SSD for QuestDB partition writes.  
* **Clock:** PTP daemon enabled for microsecond accuracy.

This plan delivers a state-of-the-art, high-frequency trading platform that is robust, scalable, and completely free of proprietary licensing costs.

#### **Works cited**

1. Plan 1.pdf  
2. Why another binding library? \- nanobind documentation, accessed January 18, 2026, [https://nanobind.readthedocs.io/en/latest/why.html](https://nanobind.readthedocs.io/en/latest/why.html)  
3. Aeron: The Future of Ultra-Low Latency Messaging in Finance and Tech \- Medium, accessed January 18, 2026, [https://medium.com/@s.g.manikandan/aeron-the-future-of-ultra-low-latency-messaging-in-finance-and-tech-3e6aff0f5517](https://medium.com/@s.g.manikandan/aeron-the-future-of-ultra-low-latency-messaging-in-finance-and-tech-3e6aff0f5517)  
4. Materialized views \- QuestDB, accessed January 18, 2026, [https://questdb.com/docs/concepts/materialized-views/](https://questdb.com/docs/concepts/materialized-views/)  
5. How do I use the Market Depth API to get market depth data for a specific symbol?, accessed January 18, 2026, [https://support.fyers.in/portal/en/kb/articles/how-do-i-use-the-market-depth-api-to-get-market-depth-data-for-a-specific-symbol](https://support.fyers.in/portal/en/kb/articles/how-do-i-use-the-market-depth-api-to-get-market-depth-data-for-a-specific-symbol)  
6. The simdjson library, accessed January 18, 2026, [https://simdjson.org/](https://simdjson.org/)  
7. Paper: Parsing Gigabytes of JSON per Second \- Branch Free, accessed January 18, 2026, [https://branchfree.org/2019/02/25/paper-parsing-gigabytes-of-json-per-second/](https://branchfree.org/2019/02/25/paper-parsing-gigabytes-of-json-per-second/)  
8. SBE Market Data Streams \- Binance Developer center, accessed January 18, 2026, [https://developers.binance.com/docs/binance-spot-api-docs/sbe-market-data-streams](https://developers.binance.com/docs/binance-spot-api-docs/sbe-market-data-streams)  
9. low-latency inter-thread communication library inspired by LMAX Disruptor. : r/rust \- Reddit, accessed January 18, 2026, [https://www.reddit.com/r/rust/comments/1e3elbx/disruptorrs\_lowlatency\_interthread\_communication/](https://www.reddit.com/r/rust/comments/1e3elbx/disruptorrs_lowlatency_interthread_communication/)  
10. Fast communication between C++ and python using shared memory \- Stack Overflow, accessed January 18, 2026, [https://stackoverflow.com/questions/69091769/fast-communication-between-c-and-python-using-shared-memory](https://stackoverflow.com/questions/69091769/fast-communication-between-c-and-python-using-shared-memory)  
11. QuestDB Peak time-series performance | by Vinodbokare | Nov, 2025 \- Medium, accessed January 18, 2026, [https://medium.com/@vinodbokare0588/questdb-peak-time-series-performance-309b4a01e607](https://medium.com/@vinodbokare0588/questdb-peak-time-series-performance-309b4a01e607)  
12. SAMPLE BY keyword \- QuestDB, accessed January 18, 2026, [https://questdb.com/docs/query/sql/sample-by/](https://questdb.com/docs/query/sql/sample-by/)  
13. Benchmarks \- nanobind documentation, accessed January 18, 2026, [https://nanobind.readthedocs.io/en/latest/benchmark.html](https://nanobind.readthedocs.io/en/latest/benchmark.html)  
14. How can developers incorporate real-time stock data into their applications? \- FYERS \- Support Portal, accessed January 18, 2026, [https://support.fyers.in/portal/en/kb/articles/how-can-developers-incorporate-real-time-stock-data-into-their-applications](https://support.fyers.in/portal/en/kb/articles/how-can-developers-incorporate-real-time-stock-data-into-their-applications)  
15. Realtime updates | Lightweight Charts \- GitHub Pages, accessed January 18, 2026, [https://tradingview.github.io/lightweight-charts/tutorials/demos/realtime-updates](https://tradingview.github.io/lightweight-charts/tutorials/demos/realtime-updates)  
16. Infinite history | Lightweight Charts \- GitHub Pages, accessed January 18, 2026, [https://tradingview.github.io/lightweight-charts/tutorials/demos/infinite-history](https://tradingview.github.io/lightweight-charts/tutorials/demos/infinite-history)