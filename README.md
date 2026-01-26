# HFT Platform

Real-time cryptocurrency trading visualization platform with Binance market data integration.

## Quick Start

```bash
uv sync                  # Install dependencies
uv run python main.py    # Start server
```

**Open**: http://localhost:8000

**QuestDB** (optional, for historical data):
```bash
docker run -d --name questdb -p 9000:9000 -p 9009:9009 questdb/questdb
```

## Features

- **Live Candlestick Charts** - TradingView Lightweight Charts v5.1
- **Custom Indicators** - TradingView-style dialog for adding SMA/EMA/Bollinger with any period
- **Volume Histogram** - Real-time volume bars with OHLCV coloring
- **Trading Sidebar** - Tabbed interface (Book/Trades/Orders)
- **Market Stats Bar** - 24h price change, high/low, volume with live indicator
- **50-Level Order Book** - Depth visualization with price grouping, hover states
- **Recent Trades Feed** - Color-coded live trade stream
- **Multiple Timeframes** - 1m, 5m, 15m, 1h, 1D intervals with live updates
- **Infinite Scroll History** - Lazy loading from QuestDB
- **Auto Gap-Fill** - Missing data automatically fetched from Binance REST API
- **Auto-Backfill on Startup** - Server automatically fills gaps for all symbols with data in QuestDB
- **Auto-Backfill on Symbol Switch** - Switching symbols via WebSocket triggers automatic data backfill
- **Live Higher TF Updates** - Frontend aggregates 1m candles into higher timeframes in real-time

## Architecture

```
Binance WebSocket
     │
     ├── @aggTrade stream ──→ Tick Handler ──→ Ring Buffer (session storage)
     │                              │
     │                              ├──→ OHLCV Aggregator ──→ /ws/candles (real-time updates)
     │                              └──→ Trade Handler ────→ /ws/trades (recent trades)
     │
     ├── @kline_1m stream ──→ Kline Handler ──→ QuestDB (only closed candles)
     │                                                │
     │                                                └──→ /ws/candles (candle close events)
     │
     └── @ticker stream ───→ Stats Handler ──→ /ws/stats (24h market stats)
```

**Data Integrity**: Only complete candles from Binance's kline stream (with `is_closed=true`) are written to QuestDB. This ensures clean data even after server restarts, avoiding partial candle artifacts.

## Tech Stack

- **Backend**: Python 3.12+, FastAPI, uvicorn, websockets
- **Database**: QuestDB (time-series)
- **Frontend**: SolidJS + TypeScript + Vite + Tailwind CSS
- **Charts**: TradingView Lightweight Charts v5.1
- **Indicators**: Custom IndicatorManager (SMA, EMA, Bollinger)

## Exchange Connectors

### Binance (Phase 1 - Complete)
- WebSocket streams: `@aggTrade`, `@kline_1m`, `@depth`, `@ticker`
- Local order book with 50-level depth
- REST API for historical data and gap-fill

### Fyers/NSE (Phase 2 - In Progress)
- **TBT 50-Depth** (Complete): Protobuf-based WebSocket for 50-level market depth
  - Connection pool auto-manages up to 3 connections (15 symbols max)
  - Incremental updates via snapshot + diff pattern
  - Rate limits: 3 connections/user, 5 symbols/connection
- **Standard Feed**: WebSocket for market data (5-level depth)
- **REST Client**: Historical candles, quotes, depth snapshots

## Project Structure

```
hft/
├── api/              # FastAPI server
│   ├── main.py       # App setup, routes
│   ├── websocket.py  # Real-time candle/depth/trades/stats streams
│   └── history.py    # Historical data REST endpoints
├── connectors/
│   ├── binance/
│   │   ├── ws_client.py  # WebSocket client with 23h reconnection
│   │   ├── feed.py       # Trade/kline/ticker stream handler
│   │   └── orderbook.py  # Local order book manager
│   └── fyers/
│       ├── tbt_feed.py   # TBT 50-depth WebSocket handler
│       ├── tbt_pool.py   # TBT connection pool (auto-scales to 15 symbols)
│       ├── feed.py       # Standard market data WebSocket
│       ├── rest_client.py # Historical data REST client
│       ├── auth.py       # OAuth2 authentication
│       ├── aggregator.py # Tick-to-candle for Fyers
│       ├── types.py      # TBT types (TBTDepth50, TBTQuote, etc.)
│       └── proto/        # Compiled protobuf for TBT messages
├── core/
│   ├── types.py      # MarketTick, OHLCV, Trade, MarketStats structs
│   └── aggregator.py # Tick-to-candle aggregation
└── storage/
    ├── questdb.py    # QuestDB ILP writer
    └── gap_fill.py   # Auto-backfill from exchange REST APIs

frontend/                    # SolidJS + TypeScript + Vite
├── src/
│   ├── App.tsx              # Root component, state management
│   ├── components/
│   │   ├── Chart.tsx            # TradingView chart with all features
│   │   ├── Header.tsx           # Toolbar with controls
│   │   ├── TradingSidebar.tsx   # Tabbed sidebar (Book/Trades/Orders)
│   │   ├── MarketStatsBar.tsx   # 24h stats with live indicator
│   │   ├── OrderBook.tsx        # Order book with price grouping
│   │   ├── RecentTrades.tsx     # Live trade feed
│   │   ├── MyOrders.tsx         # Placeholder for auth
│   │   ├── IndicatorDialog.tsx  # TradingView-style indicator picker
│   │   └── IndicatorConfigPanel.tsx # Indicator period/color config
│   ├── hooks/
│   │   └── useWebSocket.ts  # WebSocket hooks (candles/depth/trades/stats)
│   ├── stores/
│   │   └── indicatorStore.ts    # Dynamic indicator state with localStorage
│   └── lib/
│       ├── indicators.ts        # IndicatorManager (SMA, EMA, BB)
│       └── indicatorTemplates.ts # Indicator definitions and colors
├── dist/                    # Production build output
└── package.json
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/history` | Historical OHLCV candles (auto-backfills gaps from Binance) |
| `POST /api/backfill` | Manually fetch historical data from Binance |
| `GET /api/symbols` | All tradable symbols (194k+ from Binance + NSE) with filters |
| `GET /api/symbols/search?q=BTC` | Prefix search with autocomplete |
| `GET /api/symbols/stats` | Symbol counts by exchange |
| `GET /api/active-symbols` | Currently subscribed symbols with live feeds |
| `GET /api/status` | System status |
| `WS /ws/candles/{symbol}` | Real-time candle updates (500ms + on close) |
| `WS /ws/depth/{symbol}` | Real-time order book (50 levels) |
| `WS /ws/trades/{symbol}` | Real-time trade stream |
| `WS /ws/stats/{symbol}` | 24h market statistics (~1s updates) |

### Auto Gap-Fill

When panning the chart or loading history, missing candles are automatically fetched from Binance. **All timeframes backfill 1m candles**, which QuestDB then aggregates via `SAMPLE BY`.

**Auto-Backfill on Startup**: When the server starts, it automatically queries QuestDB for all symbols with data in the last 30 days, detects gaps > 1 hour, and backfills from Binance REST API. This runs in the background and doesn't block server startup.

**Auto-Backfill on Symbol Switch**: When a user subscribes to a symbol via `/ws/subscribe`, if the symbol has a gap > 30 minutes, the system automatically backfills missing candles.

```bash
# History with auto-backfill (default)
GET /api/history?symbol=BTCUSDT&limit=500

# Higher timeframe - fetches 1m candles, displays 1h aggregated
GET /api/history?symbol=BTCUSDT&interval=1h&limit=24

# 1D chart - fetches all required 1m candles for the period
GET /api/history?symbol=BTCUSDT&interval=1d&limit=30

# Disable auto-backfill
GET /api/history?symbol=BTCUSDT&limit=500&backfill=false

# Manual backfill (fetch last 24 hours of 1m data)
POST /api/backfill?symbol=BTCUSDT&hours=24
```

### Live Updates for Higher Timeframes

The frontend aggregates incoming 1m candles into higher timeframes in real-time:

- **1m interval**: Updates directly from WebSocket
- **5m/15m/1h/1D**: Frontend floors timestamps and aggregates OHLCV values

```
WebSocket (1m candles) → Frontend Aggregation → Chart Update
                              │
                              └── Floor timestamp to interval boundary
                              └── Update high/low/close/volume
```

## Frontend Controls

- **Symbol Selector**: 194k+ symbols (Binance spot/futures/options + NSE equity/F&O)
- **Interval Selector**: 1m, 5m, 15m, 1h, 1D
- **Chart Type Selector**: Candlestick, Bar, Line, Area, Baseline
- **Go Live Button**: Scroll to latest candle
- **Indicators Button**: Opens TradingView-style dialog for custom indicators (any period)
- **Vol Button**: Toggle volume histogram
- **Scale Mode**: Normal, Log, %, Index

## Trading Sidebar

- **Market Stats Bar**: 24h price change (value + %), high/low, volume
- **Tabs**: Book | Trades | Orders
- **Order Book**: Price grouping, gradient depth bars, hover states
- **Recent Trades**: Color-coded by side, flash animation on new trades

## Development Status

| Phase | Status | Description |
|-------|--------|-------------|
| **Phase 1** | Complete | Binance market data + visualization |
| **Phase 2** | In Progress | Fyers/NSE connector (TBT 50-depth complete) |
| **Phase 3** | Planned | Performance optimization |
| **Phase 4** | Planned | C++ hot path (optional) |
| **Phase 5** | Planned | Order execution |

See [plans/master_plan.md](plans/master_plan.md) for full implementation details.
