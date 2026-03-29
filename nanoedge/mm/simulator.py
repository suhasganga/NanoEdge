"""Order simulator for market making strategy testing.

Matches simulated orders against live market data using instant fill on price cross.
"""

import asyncio
import time
import structlog
from collections.abc import Callable

from nanoedge.core.types import Trade
from nanoedge.mm.types import (
    OrderSide,
    OrderStatus,
    SimulatedOrder,
    SimulatedPosition,
    OrderFill,
    GridOrderConfig,
)

logger = structlog.get_logger(__name__)


class OrderSimulator:
    """Simulates order execution against live market data.

    Implements instant fill on price cross:
    - BUY orders fill when market price <= order price
    - SELL orders fill when market price >= order price

    Thread-safe via asyncio.Lock for order operations.
    """

    __slots__ = (
        "symbol",
        "exchange",
        "market",
        "_orders",
        "_position",
        "_fills",
        "_lock",
        "on_order_update",
        "on_position_update",
        "on_fill",
        "_last_price",
    )

    def __init__(
        self,
        symbol: str,
        exchange: str = "binance",
        market: str = "spot",
        on_order_update: Callable[[SimulatedOrder], None] | None = None,
        on_position_update: Callable[[SimulatedPosition], None] | None = None,
        on_fill: Callable[[OrderFill], None] | None = None,
    ):
        """Initialize simulator for a symbol.

        Args:
            symbol: Trading pair (e.g., BTCUSDT)
            exchange: Exchange name
            market: Market type (spot, futures)
            on_order_update: Callback when order state changes
            on_position_update: Callback when position changes
            on_fill: Callback when order is filled
        """
        self.symbol = symbol
        self.exchange = exchange
        self.market = market

        self._orders: dict[str, SimulatedOrder] = {}
        self._position = SimulatedPosition.create(symbol, exchange, market)
        self._fills: list[OrderFill] = []
        self._lock = asyncio.Lock()
        self._last_price: float = 0.0

        self.on_order_update = on_order_update
        self.on_position_update = on_position_update
        self.on_fill = on_fill

    async def place_order(
        self,
        side: OrderSide,
        price: float,
        quantity: float,
        tag: str = "",
    ) -> SimulatedOrder:
        """Place a new limit order.

        Args:
            side: Buy or sell
            price: Limit price
            quantity: Order quantity
            tag: Optional tag for order grouping

        Returns:
            The created order
        """
        async with self._lock:
            order = SimulatedOrder.create(
                symbol=self.symbol,
                side=side,
                price=price,
                quantity=quantity,
                exchange=self.exchange,
                market=self.market,
                tag=tag,
            )
            self._orders[order.order_id] = order

            logger.info(
                "order_placed",
                order_id=order.order_id,
                symbol=self.symbol,
                side=side.value,
                price=price,
                quantity=quantity,
                tag=tag,
            )

            if self.on_order_update:
                self.on_order_update(order)

            return order

    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an open order.

        Args:
            order_id: ID of order to cancel

        Returns:
            True if cancelled, False if not found or already filled
        """
        async with self._lock:
            order = self._orders.get(order_id)
            if not order:
                return False

            if order.status not in (OrderStatus.OPEN, OrderStatus.PARTIALLY_FILLED):
                return False

            order.status = OrderStatus.CANCELLED
            order.updated_at_ms = int(time.time() * 1000)

            logger.info(
                "order_cancelled",
                order_id=order_id,
                symbol=self.symbol,
            )

            if self.on_order_update:
                self.on_order_update(order)

            # Remove from active orders
            del self._orders[order_id]
            return True

    async def cancel_all_orders(
        self,
        side: OrderSide | None = None,
        tag: str | None = None,
    ) -> int:
        """Cancel multiple orders with optional filters.

        Args:
            side: Only cancel orders of this side
            tag: Only cancel orders with this tag

        Returns:
            Number of orders cancelled
        """
        async with self._lock:
            to_cancel = []
            for order in self._orders.values():
                if order.status not in (OrderStatus.OPEN, OrderStatus.PARTIALLY_FILLED):
                    continue
                if side is not None and order.side != side:
                    continue
                if tag is not None and order.tag != tag:
                    continue
                to_cancel.append(order.order_id)

        # Cancel outside lock to avoid holding it too long
        count = 0
        for order_id in to_cancel:
            if await self.cancel_order(order_id):
                count += 1

        logger.info(
            "orders_cancelled",
            count=count,
            symbol=self.symbol,
            side=side.value if side else None,
            tag=tag,
        )

        return count

    async def place_grid_orders(self, config: GridOrderConfig) -> list[SimulatedOrder]:
        """Place multiple grid orders from configuration.

        Args:
            config: Grid order configuration

        Returns:
            List of created orders
        """
        orders = []
        for side, price, quantity in config.generate_orders():
            order = await self.place_order(side, price, quantity, tag=config.tag)
            orders.append(order)

        logger.info(
            "grid_orders_placed",
            symbol=self.symbol,
            count=len(orders),
            base_price=config.base_price,
            spread=config.spread,
            levels=config.levels,
        )

        return orders

    def process_trade(self, trade: Trade) -> list[OrderFill]:
        """Process incoming trade to check for fills.

        This is called synchronously from the trade handler for low latency.

        Matching logic (instant fill on price cross):
        - BUY orders fill when trade.price <= order.price
        - SELL orders fill when trade.price >= order.price

        Args:
            trade: Incoming trade from market data

        Returns:
            List of fills that occurred
        """
        if trade.symbol != self.symbol:
            return []

        self._last_price = trade.price
        fills: list[OrderFill] = []

        # Check each open order for fill conditions
        orders_to_remove = []
        for order in self._orders.values():
            if order.status != OrderStatus.OPEN:
                continue

            should_fill = False
            if order.side == OrderSide.BUY and trade.price <= order.price:
                should_fill = True
            elif order.side == OrderSide.SELL and trade.price >= order.price:
                should_fill = True

            if should_fill:
                fill = self._execute_fill(order, trade.price)
                fills.append(fill)
                orders_to_remove.append(order.order_id)

        # Remove filled orders
        for order_id in orders_to_remove:
            del self._orders[order_id]

        # Update unrealized P&L with latest price
        if self._position.quantity != 0:
            self._update_unrealized_pnl(trade.price)

        return fills

    def _execute_fill(self, order: SimulatedOrder, fill_price: float) -> OrderFill:
        """Execute a fill on an order.

        Args:
            order: Order being filled
            fill_price: Price at which fill occurs

        Returns:
            The fill event
        """
        # Create fill event
        fill_qty = order.quantity - order.filled_quantity
        fill = OrderFill.create(
            order_id=order.order_id,
            symbol=self.symbol,
            side=order.side,
            price=fill_price,
            quantity=fill_qty,
        )
        self._fills.append(fill)

        # Update order state
        order.filled_quantity = order.quantity
        order.status = OrderStatus.FILLED
        order.updated_at_ms = fill.timestamp_ms

        logger.info(
            "order_filled",
            order_id=order.order_id,
            symbol=self.symbol,
            side=order.side.value,
            price=fill_price,
            quantity=fill_qty,
        )

        # Update position
        self._apply_fill(fill)

        # Fire callbacks
        if self.on_order_update:
            self.on_order_update(order)
        if self.on_fill:
            self.on_fill(fill)

        return fill

    def _apply_fill(self, fill: OrderFill) -> None:
        """Update position state after a fill.

        Handles:
        - Opening new position
        - Adding to existing position (same side)
        - Reducing/closing position (opposite side)
        - Calculating realized P&L
        """
        pos = self._position
        now_ms = int(time.time() * 1000)

        if fill.side == OrderSide.BUY:
            if pos.quantity >= 0:
                # Adding to long or opening long
                new_qty = pos.quantity + fill.quantity
                if new_qty != 0:
                    # Weighted average price
                    pos.avg_entry_price = (
                        (pos.avg_entry_price * pos.quantity) + (fill.price * fill.quantity)
                    ) / new_qty
                pos.quantity = new_qty
            else:
                # Covering short position
                cover_qty = min(fill.quantity, abs(pos.quantity))
                realized = (pos.avg_entry_price - fill.price) * cover_qty
                pos.realized_pnl += realized
                pos.quantity += fill.quantity

                if pos.quantity == 0:
                    pos.avg_entry_price = 0.0
                elif pos.quantity > 0:
                    # Flipped to long
                    pos.avg_entry_price = fill.price
        else:  # SELL
            if pos.quantity <= 0:
                # Adding to short or opening short
                prev_qty = abs(pos.quantity)
                new_qty = pos.quantity - fill.quantity
                if new_qty != 0:
                    pos.avg_entry_price = (
                        (pos.avg_entry_price * prev_qty) + (fill.price * fill.quantity)
                    ) / abs(new_qty)
                pos.quantity = new_qty
            else:
                # Closing long position
                close_qty = min(fill.quantity, pos.quantity)
                realized = (fill.price - pos.avg_entry_price) * close_qty
                pos.realized_pnl += realized
                pos.quantity -= fill.quantity

                if pos.quantity == 0:
                    pos.avg_entry_price = 0.0
                elif pos.quantity < 0:
                    # Flipped to short
                    pos.avg_entry_price = fill.price

        pos.updated_at_ms = now_ms

        if self.on_position_update:
            self.on_position_update(pos)

    def _update_unrealized_pnl(self, current_price: float) -> None:
        """Update unrealized P&L based on current market price."""
        pos = self._position
        if pos.quantity > 0:
            pos.unrealized_pnl = (current_price - pos.avg_entry_price) * pos.quantity
        elif pos.quantity < 0:
            pos.unrealized_pnl = (pos.avg_entry_price - current_price) * abs(pos.quantity)
        else:
            pos.unrealized_pnl = 0.0

    def get_open_orders(self) -> list[SimulatedOrder]:
        """Get all open orders."""
        return [
            o for o in self._orders.values()
            if o.status in (OrderStatus.OPEN, OrderStatus.PARTIALLY_FILLED)
        ]

    def get_position(self) -> SimulatedPosition:
        """Get current position."""
        return self._position

    def get_fills(self, limit: int = 100) -> list[OrderFill]:
        """Get recent fills."""
        return self._fills[-limit:]

    def get_last_price(self) -> float:
        """Get last processed market price."""
        return self._last_price

    def reset(self) -> None:
        """Reset all state (orders, position, fills)."""
        self._orders.clear()
        self._position = SimulatedPosition.create(self.symbol, self.exchange, self.market)
        self._fills.clear()
        self._last_price = 0.0

        logger.info("simulator_reset", symbol=self.symbol)

        if self.on_position_update:
            self.on_position_update(self._position)
