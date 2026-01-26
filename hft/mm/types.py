"""Order and position types for market making simulation.

Designed for future live trading support via OrderExecutor protocol.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Protocol
import time
import uuid


class OrderSide(str, Enum):
    """Order side - buy or sell."""

    BUY = "buy"
    SELL = "sell"


class OrderStatus(str, Enum):
    """Order lifecycle status."""

    PENDING = "pending"  # Created, not yet active
    OPEN = "open"  # Active in order book
    PARTIALLY_FILLED = "partially_filled"  # Some quantity filled
    FILLED = "filled"  # Fully executed
    CANCELLED = "cancelled"  # User cancelled


@dataclass(slots=True)
class SimulatedOrder:
    """A simulated order for paper trading.

    Attributes:
        order_id: Unique identifier (UUID)
        symbol: Trading pair (e.g., BTCUSDT)
        exchange: Exchange name (binance, fyers)
        market: Market type (spot, futures)
        side: Buy or sell
        price: Limit price
        quantity: Original order quantity
        filled_quantity: How much has been filled
        status: Current order status
        created_at_ms: Timestamp when order was created
        updated_at_ms: Timestamp of last update
        tag: User-defined tag for order grouping (e.g., "grid", "att")
    """

    order_id: str
    symbol: str
    exchange: str
    market: str
    side: OrderSide
    price: float
    quantity: float
    filled_quantity: float
    status: OrderStatus
    created_at_ms: int
    updated_at_ms: int
    tag: str = ""

    @classmethod
    def create(
        cls,
        symbol: str,
        side: OrderSide,
        price: float,
        quantity: float,
        exchange: str = "binance",
        market: str = "spot",
        tag: str = "",
    ) -> "SimulatedOrder":
        """Factory method to create a new order."""
        now_ms = int(time.time() * 1000)
        return cls(
            order_id=str(uuid.uuid4()),
            symbol=symbol,
            exchange=exchange,
            market=market,
            side=side,
            price=price,
            quantity=quantity,
            filled_quantity=0.0,
            status=OrderStatus.OPEN,
            created_at_ms=now_ms,
            updated_at_ms=now_ms,
            tag=tag,
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "order_id": self.order_id,
            "symbol": self.symbol,
            "exchange": self.exchange,
            "market": self.market,
            "side": self.side.value,
            "price": self.price,
            "quantity": self.quantity,
            "filled_quantity": self.filled_quantity,
            "status": self.status.value,
            "created_at": self.created_at_ms,
            "updated_at": self.updated_at_ms,
            "tag": self.tag,
        }


@dataclass(slots=True)
class SimulatedPosition:
    """Tracks position state for a symbol.

    Attributes:
        symbol: Trading pair
        exchange: Exchange name
        market: Market type
        quantity: Position size (positive = long, negative = short)
        avg_entry_price: Volume-weighted average entry price
        realized_pnl: Cumulative realized P&L from closed trades
        unrealized_pnl: Current unrealized P&L (calculated from mark price)
        updated_at_ms: Last update timestamp
    """

    symbol: str
    exchange: str
    market: str
    quantity: float
    avg_entry_price: float
    realized_pnl: float
    unrealized_pnl: float
    updated_at_ms: int

    @classmethod
    def create(
        cls,
        symbol: str,
        exchange: str = "binance",
        market: str = "spot",
    ) -> "SimulatedPosition":
        """Factory method to create a new empty position."""
        return cls(
            symbol=symbol,
            exchange=exchange,
            market=market,
            quantity=0.0,
            avg_entry_price=0.0,
            realized_pnl=0.0,
            unrealized_pnl=0.0,
            updated_at_ms=int(time.time() * 1000),
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "symbol": self.symbol,
            "exchange": self.exchange,
            "market": self.market,
            "quantity": self.quantity,
            "avg_entry_price": self.avg_entry_price,
            "realized_pnl": self.realized_pnl,
            "unrealized_pnl": self.unrealized_pnl,
            "updated_at": self.updated_at_ms,
        }


@dataclass(slots=True)
class OrderFill:
    """Represents a fill event when an order is executed.

    Attributes:
        order_id: The order that was filled
        fill_id: Unique identifier for this fill
        symbol: Trading pair
        side: Buy or sell
        price: Execution price
        quantity: Fill quantity
        timestamp_ms: When the fill occurred
    """

    order_id: str
    fill_id: str
    symbol: str
    side: OrderSide
    price: float
    quantity: float
    timestamp_ms: int

    @classmethod
    def create(
        cls,
        order_id: str,
        symbol: str,
        side: OrderSide,
        price: float,
        quantity: float,
    ) -> "OrderFill":
        """Factory method to create a new fill."""
        return cls(
            order_id=order_id,
            fill_id=str(uuid.uuid4()),
            symbol=symbol,
            side=side,
            price=price,
            quantity=quantity,
            timestamp_ms=int(time.time() * 1000),
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "order_id": self.order_id,
            "fill_id": self.fill_id,
            "symbol": self.symbol,
            "side": self.side.value,
            "price": self.price,
            "quantity": self.quantity,
            "timestamp": self.timestamp_ms,
        }


class OrderExecutor(Protocol):
    """Protocol for order execution - implement for simulation or live exchange.

    This allows swapping between paper trading and real exchange connectivity
    without changing the rest of the codebase.
    """

    async def place_order(
        self,
        symbol: str,
        side: OrderSide,
        price: float,
        quantity: float,
        tag: str = "",
    ) -> SimulatedOrder:
        """Place a new order."""
        ...

    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an existing order."""
        ...

    async def cancel_all_orders(
        self,
        symbol: str | None = None,
        side: OrderSide | None = None,
        tag: str | None = None,
    ) -> int:
        """Cancel multiple orders with optional filters."""
        ...

    def get_open_orders(self, symbol: str | None = None) -> list[SimulatedOrder]:
        """Get all open orders."""
        ...

    def get_position(self, symbol: str) -> SimulatedPosition:
        """Get position for a symbol."""
        ...


@dataclass
class GridOrderConfig:
    """Configuration for grid order generation.

    Attributes:
        base_price: Center price for the grid
        spread: Distance between price levels
        levels: Number of levels per side
        base_quantity: Quantity at first level
        quantity_scale: Multiplier per level (1 = flat, 1.5 = pyramid)
        side: "both", "buy", or "sell"
        tag: Tag for all grid orders
    """

    base_price: float
    spread: float
    levels: int = 5
    base_quantity: float = 1.0
    quantity_scale: float = 1.0
    side: str = "both"  # "both", "buy", "sell"
    tag: str = "grid"

    def generate_orders(self) -> list[tuple[OrderSide, float, float]]:
        """Generate order specifications from config.

        Returns:
            List of (side, price, quantity) tuples
        """
        orders: list[tuple[OrderSide, float, float]] = []

        for i in range(1, self.levels + 1):
            qty = self.base_quantity * (self.quantity_scale ** (i - 1))

            if self.side in ("both", "buy"):
                buy_price = self.base_price - (self.spread * i)
                orders.append((OrderSide.BUY, buy_price, qty))

            if self.side in ("both", "sell"):
                sell_price = self.base_price + (self.spread * i)
                orders.append((OrderSide.SELL, sell_price, qty))

        return orders
