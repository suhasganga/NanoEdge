"""Market Making module - Order simulation and visualization.

This module provides order simulation capabilities for testing market making strategies.
All code is isolated here for easy removal if needed.

Usage:
    from hft.mm import OrderSimulator, mm_router

    # Register the router in main.py
    app.include_router(mm_router, prefix="/api/mm", tags=["market-making"])
"""

from hft.mm.types import (
    OrderSide,
    OrderStatus,
    SimulatedOrder,
    SimulatedPosition,
    OrderFill,
)
from hft.mm.simulator import OrderSimulator
from hft.mm.routes import router as mm_router

__all__ = [
    "OrderSide",
    "OrderStatus",
    "SimulatedOrder",
    "SimulatedPosition",
    "OrderFill",
    "OrderSimulator",
    "mm_router",
]
