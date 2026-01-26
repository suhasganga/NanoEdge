"""REST API endpoints for order management.

All market making endpoints are prefixed with /api/mm for easy routing.
"""

import asyncio
from typing import Literal

from fastapi import APIRouter, HTTPException, Query, WebSocket, WebSocketDisconnect
import structlog

from hft.mm.types import OrderSide, GridOrderConfig
from hft.mm.simulator import OrderSimulator
from hft.mm.ws_types import (
    encode_order_update,
    encode_position_update,
    encode_order_fill,
    encode_orders_snapshot,
)

logger = structlog.get_logger(__name__)

router = APIRouter()

# Global state for simulators - keyed by symbol
_simulators: dict[str, OrderSimulator] = {}
_order_subscribers: dict[str, set[asyncio.Queue]] = {}


def get_or_create_simulator(
    symbol: str,
    exchange: str = "binance",
    market: str = "spot",
) -> OrderSimulator:
    """Get existing simulator or create new one for symbol."""
    key = symbol.upper()
    if key not in _simulators:
        simulator = OrderSimulator(
            symbol=key,
            exchange=exchange,
            market=market,
            on_order_update=lambda o: _broadcast_order_update(key, o),
            on_position_update=lambda p: _broadcast_position_update(key, p),
            on_fill=lambda f: _broadcast_fill(key, f),
        )
        _simulators[key] = simulator
        logger.info("simulator_created", symbol=key)
    return _simulators[key]


def get_simulator(symbol: str) -> OrderSimulator | None:
    """Get existing simulator for symbol."""
    return _simulators.get(symbol.upper())


def _broadcast_order_update(symbol: str, order) -> None:
    """Broadcast order update to all subscribers."""
    subscribers = _order_subscribers.get(symbol, set())
    if not subscribers:
        return

    data = encode_order_update(order)
    for queue in list(subscribers):
        try:
            queue.put_nowait(data)
        except asyncio.QueueFull:
            pass  # Drop if client slow


def _broadcast_position_update(symbol: str, position) -> None:
    """Broadcast position update to all subscribers."""
    subscribers = _order_subscribers.get(symbol, set())
    if not subscribers:
        return

    data = encode_position_update(position)
    for queue in list(subscribers):
        try:
            queue.put_nowait(data)
        except asyncio.QueueFull:
            pass


def _broadcast_fill(symbol: str, fill) -> None:
    """Broadcast fill to all subscribers."""
    subscribers = _order_subscribers.get(symbol, set())
    if not subscribers:
        return

    data = encode_order_fill(fill)
    for queue in list(subscribers):
        try:
            queue.put_nowait(data)
        except asyncio.QueueFull:
            pass


# ============================================================================
# REST Endpoints
# ============================================================================


@router.post("/orders")
async def place_order(
    symbol: str = Query(..., description="Trading pair (e.g., BTCUSDT)"),
    side: Literal["buy", "sell"] = Query(..., description="Order side"),
    price: float = Query(..., gt=0, description="Limit price"),
    quantity: float = Query(..., gt=0, description="Order quantity"),
    tag: str = Query("", description="Optional order tag"),
):
    """Place a simulated limit order."""
    simulator = get_or_create_simulator(symbol)
    order_side = OrderSide.BUY if side == "buy" else OrderSide.SELL

    order = await simulator.place_order(order_side, price, quantity, tag)

    return {
        "status": "success",
        "order": order.to_dict(),
    }


@router.delete("/orders/{order_id}")
async def cancel_order(order_id: str):
    """Cancel a specific order by ID."""
    # Search all simulators for the order
    for simulator in _simulators.values():
        if await simulator.cancel_order(order_id):
            return {"status": "success", "order_id": order_id}

    raise HTTPException(status_code=404, detail="Order not found")


@router.delete("/orders")
async def cancel_all_orders(
    symbol: str = Query(None, description="Filter by symbol"),
    side: Literal["buy", "sell"] | None = Query(None, description="Filter by side"),
    tag: str | None = Query(None, description="Filter by tag"),
):
    """Cancel multiple orders with optional filters."""
    total_cancelled = 0

    if symbol:
        # Cancel for specific symbol
        simulator = get_simulator(symbol)
        if simulator:
            order_side = None
            if side:
                order_side = OrderSide.BUY if side == "buy" else OrderSide.SELL
            total_cancelled = await simulator.cancel_all_orders(side=order_side, tag=tag)
    else:
        # Cancel across all symbols
        for simulator in _simulators.values():
            order_side = None
            if side:
                order_side = OrderSide.BUY if side == "buy" else OrderSide.SELL
            total_cancelled += await simulator.cancel_all_orders(side=order_side, tag=tag)

    return {"status": "success", "cancelled": total_cancelled}


@router.get("/orders")
async def get_orders(
    symbol: str = Query(None, description="Filter by symbol"),
):
    """Get all open orders."""
    orders = []

    if symbol:
        simulator = get_simulator(symbol)
        if simulator:
            orders = [o.to_dict() for o in simulator.get_open_orders()]
    else:
        for simulator in _simulators.values():
            orders.extend(o.to_dict() for o in simulator.get_open_orders())

    return {"orders": orders}


@router.get("/position/{symbol}")
async def get_position(symbol: str):
    """Get position for a symbol."""
    simulator = get_simulator(symbol)
    if not simulator:
        # Return empty position if no simulator exists
        return {
            "position": {
                "symbol": symbol.upper(),
                "quantity": 0.0,
                "avg_entry_price": 0.0,
                "realized_pnl": 0.0,
                "unrealized_pnl": 0.0,
            }
        }

    return {"position": simulator.get_position().to_dict()}


@router.post("/reset/{symbol}")
async def reset_simulator(symbol: str):
    """Reset simulator state for a symbol (clear orders and position)."""
    simulator = get_simulator(symbol)
    if not simulator:
        raise HTTPException(status_code=404, detail="No simulator for symbol")

    simulator.reset()
    return {"status": "success", "symbol": symbol.upper()}


@router.get("/fills/{symbol}")
async def get_fills(
    symbol: str,
    limit: int = Query(100, ge=1, le=1000),
):
    """Get recent fills for a symbol."""
    simulator = get_simulator(symbol)
    if not simulator:
        return {"fills": []}

    fills = [f.to_dict() for f in simulator.get_fills(limit)]
    return {"fills": fills}


# ============================================================================
# Grid Order Endpoints
# ============================================================================


@router.post("/grid")
async def place_grid_orders(
    symbol: str = Query(..., description="Trading pair"),
    base_price: float = Query(..., gt=0, description="Center price for grid"),
    spread: float = Query(..., gt=0, description="Distance between levels"),
    levels: int = Query(5, ge=1, le=20, description="Levels per side"),
    base_quantity: float = Query(1.0, gt=0, description="Quantity at first level"),
    quantity_scale: float = Query(1.0, ge=0.5, le=3.0, description="Quantity multiplier per level"),
    side: Literal["both", "buy", "sell"] = Query("both", description="Order sides to place"),
    tag: str = Query("grid", description="Tag for all grid orders"),
):
    """Place multi-level grid orders around base_price.

    Example: base_price=90000, spread=100, levels=3, base_quantity=0.1, quantity_scale=1.5
    Creates:
      BUY  @ 89900 qty 0.1
      BUY  @ 89800 qty 0.15
      BUY  @ 89700 qty 0.225
      SELL @ 90100 qty 0.1
      SELL @ 90200 qty 0.15
      SELL @ 90300 qty 0.225
    """
    simulator = get_or_create_simulator(symbol)

    config = GridOrderConfig(
        base_price=base_price,
        spread=spread,
        levels=levels,
        base_quantity=base_quantity,
        quantity_scale=quantity_scale,
        side=side,
        tag=tag,
    )

    orders = await simulator.place_grid_orders(config)

    return {
        "status": "success",
        "orders_placed": len(orders),
        "orders": [o.to_dict() for o in orders],
    }


@router.delete("/grid/{symbol}")
async def cancel_grid_orders(
    symbol: str,
    tag: str = Query("grid", description="Grid tag to cancel"),
):
    """Cancel all orders with specified grid tag."""
    simulator = get_simulator(symbol)
    if not simulator:
        return {"status": "success", "cancelled": 0}

    cancelled = await simulator.cancel_all_orders(tag=tag)
    return {"status": "success", "cancelled": cancelled}


# ============================================================================
# WebSocket Endpoint
# ============================================================================


@router.websocket("/ws/orders/{symbol}")
async def ws_orders(websocket: WebSocket, symbol: str):
    """Real-time order and position updates.

    Sends:
    - orders_snapshot on connect (all open orders + position)
    - order_update on each order state change
    - position_update on position change
    - order_fill on each fill
    """
    await websocket.accept()
    symbol = symbol.upper()

    # Get or create simulator
    simulator = get_or_create_simulator(symbol)

    # Send initial snapshot
    snapshot_data = encode_orders_snapshot(
        orders=simulator.get_open_orders(),
        position=simulator.get_position(),
    )
    await websocket.send_bytes(snapshot_data)

    # Subscribe to updates
    queue: asyncio.Queue = asyncio.Queue(maxsize=100)
    _order_subscribers.setdefault(symbol, set()).add(queue)

    logger.info("orders_ws_connected", symbol=symbol)

    try:
        while True:
            try:
                # Wait for updates with timeout for heartbeat
                data = await asyncio.wait_for(queue.get(), timeout=30.0)
                await websocket.send_bytes(data)
            except asyncio.TimeoutError:
                # Send heartbeat
                await websocket.send_text('{"type":"heartbeat"}')
    except WebSocketDisconnect:
        logger.info("orders_ws_disconnected", symbol=symbol)
    except Exception as e:
        logger.error("orders_ws_error", symbol=symbol, error=str(e))
    finally:
        _order_subscribers[symbol].discard(queue)


# ============================================================================
# Integration Hook for Trade Handler
# ============================================================================


def process_trade_for_simulation(trade) -> None:
    """Call this from the main trade handler to check for fills.

    This should be called from hft/api/dependencies.py handle_trade().
    """
    symbol = trade.symbol.upper() if hasattr(trade, "symbol") else str(trade.get("symbol", "")).upper()
    simulator = get_simulator(symbol)
    if simulator:
        # process_trade is synchronous for low latency
        simulator.process_trade(trade)
