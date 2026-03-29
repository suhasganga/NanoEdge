"""WebSocket message types for order updates.

Pre-compiled msgspec encoders for high-performance serialization.
"""

import msgspec
from nanoedge.mm.types import SimulatedOrder, SimulatedPosition, OrderFill


class OrderUpdateMsg(msgspec.Struct):
    """Real-time order update message."""

    type: str = "order_update"
    order_id: str = ""
    symbol: str = ""
    side: str = ""
    price: float = 0.0
    quantity: float = 0.0
    filled_quantity: float = 0.0
    status: str = ""
    tag: str = ""
    created_at: int = 0
    updated_at: int = 0


class PositionUpdateMsg(msgspec.Struct):
    """Real-time position update message."""

    type: str = "position_update"
    symbol: str = ""
    quantity: float = 0.0
    avg_entry_price: float = 0.0
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    updated_at: int = 0


class OrderFillMsg(msgspec.Struct):
    """Order fill notification for chart markers."""

    type: str = "order_fill"
    order_id: str = ""
    fill_id: str = ""
    symbol: str = ""
    side: str = ""
    price: float = 0.0
    quantity: float = 0.0
    timestamp: int = 0


class OrdersSnapshotMsg(msgspec.Struct):
    """Snapshot of all orders (sent on WebSocket connect)."""

    type: str = "orders_snapshot"
    orders: list = []  # List of OrderUpdateMsg dicts
    position: dict | None = None  # PositionUpdateMsg dict or None


# Pre-compiled encoder for all message types
encoder = msgspec.json.Encoder()


def encode_order_update(order: SimulatedOrder) -> bytes:
    """Encode order to JSON bytes."""
    return encoder.encode(
        OrderUpdateMsg(
            type="order_update",
            order_id=order.order_id,
            symbol=order.symbol,
            side=order.side.value,
            price=order.price,
            quantity=order.quantity,
            filled_quantity=order.filled_quantity,
            status=order.status.value,
            tag=order.tag,
            created_at=order.created_at_ms,
            updated_at=order.updated_at_ms,
        )
    )


def encode_position_update(position: SimulatedPosition) -> bytes:
    """Encode position to JSON bytes."""
    return encoder.encode(
        PositionUpdateMsg(
            type="position_update",
            symbol=position.symbol,
            quantity=position.quantity,
            avg_entry_price=position.avg_entry_price,
            realized_pnl=position.realized_pnl,
            unrealized_pnl=position.unrealized_pnl,
            updated_at=position.updated_at_ms,
        )
    )


def encode_order_fill(fill: OrderFill) -> bytes:
    """Encode fill to JSON bytes."""
    return encoder.encode(
        OrderFillMsg(
            type="order_fill",
            order_id=fill.order_id,
            fill_id=fill.fill_id,
            symbol=fill.symbol,
            side=fill.side.value,
            price=fill.price,
            quantity=fill.quantity,
            timestamp=fill.timestamp_ms,
        )
    )


def encode_orders_snapshot(
    orders: list[SimulatedOrder],
    position: SimulatedPosition | None,
) -> bytes:
    """Encode full snapshot to JSON bytes."""
    order_dicts = [
        {
            "order_id": o.order_id,
            "symbol": o.symbol,
            "side": o.side.value,
            "price": o.price,
            "quantity": o.quantity,
            "filled_quantity": o.filled_quantity,
            "status": o.status.value,
            "tag": o.tag,
            "created_at": o.created_at_ms,
            "updated_at": o.updated_at_ms,
        }
        for o in orders
    ]

    position_dict = None
    if position:
        position_dict = {
            "symbol": position.symbol,
            "quantity": position.quantity,
            "avg_entry_price": position.avg_entry_price,
            "realized_pnl": position.realized_pnl,
            "unrealized_pnl": position.unrealized_pnl,
            "updated_at": position.updated_at_ms,
        }

    return encoder.encode(
        OrdersSnapshotMsg(
            type="orders_snapshot",
            orders=order_dicts,
            position=position_dict,
        )
    )
