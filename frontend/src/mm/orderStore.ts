/**
 * Reactive order store for market making simulation.
 *
 * Manages order state, position tracking, and fill history using Solid.js signals.
 */

import { createSignal, createRoot } from "solid-js";
import type {
  SimulatedOrder,
  SimulatedPosition,
  OrderFill,
} from "./types";

function createOrderStore() {
  // Core state
  const [orders, setOrders] = createSignal<SimulatedOrder[]>([]);
  const [position, setPosition] = createSignal<SimulatedPosition | null>(null);
  const [fills, setFills] = createSignal<OrderFill[]>([]);

  // Connection state
  const [isConnected, setIsConnected] = createSignal(false);
  const [currentSymbol, setCurrentSymbol] = createSignal<string | null>(null);

  /**
   * Update or add a single order
   */
  const updateOrder = (order: SimulatedOrder) => {
    setOrders((prev) => {
      const idx = prev.findIndex((o) => o.order_id === order.order_id);
      if (idx >= 0) {
        const updated = [...prev];
        updated[idx] = order;
        return updated;
      }
      return [...prev, order];
    });
  };

  /**
   * Remove an order by ID
   */
  const removeOrder = (orderId: string) => {
    setOrders((prev) => prev.filter((o) => o.order_id !== orderId));
  };

  /**
   * Add a fill to history
   */
  const addFill = (fill: OrderFill) => {
    setFills((prev) => {
      // Keep only last 100 fills
      const updated = [...prev, fill];
      if (updated.length > 100) {
        return updated.slice(-100);
      }
      return updated;
    });
  };

  /**
   * Sync state from WebSocket snapshot
   */
  const syncFromSnapshot = (snapshot: {
    orders: SimulatedOrder[];
    position: SimulatedPosition | null;
  }) => {
    // Filter to only open orders
    const openOrders = snapshot.orders.filter(
      (o) => o.status === "open" || o.status === "partially_filled"
    );
    setOrders(openOrders);
    setPosition(snapshot.position);
  };

  /**
   * Handle order update - update state or remove if filled/cancelled
   */
  const handleOrderUpdate = (order: SimulatedOrder) => {
    if (order.status === "filled" || order.status === "cancelled") {
      removeOrder(order.order_id);
    } else {
      updateOrder(order);
    }
  };

  /**
   * Get orders filtered by side
   */
  const getBuyOrders = () =>
    orders().filter((o) => o.side === "buy" && o.status === "open");
  const getSellOrders = () =>
    orders().filter((o) => o.side === "sell" && o.status === "open");

  /**
   * Get orders filtered by tag
   */
  const getOrdersByTag = (tag: string) =>
    orders().filter((o) => o.tag === tag && o.status === "open");

  /**
   * Get total P&L (realized + unrealized)
   */
  const getTotalPnL = () => {
    const pos = position();
    if (!pos) return 0;
    return pos.realized_pnl + pos.unrealized_pnl;
  };

  /**
   * Clear all state
   */
  const clear = () => {
    setOrders([]);
    setPosition(null);
    setFills([]);
  };

  /**
   * Clear on symbol change
   */
  const setSymbol = (symbol: string | null) => {
    if (symbol !== currentSymbol()) {
      clear();
      setCurrentSymbol(symbol);
    }
  };

  return {
    // State signals
    orders,
    position,
    fills,
    isConnected,
    currentSymbol,

    // State setters (for WebSocket integration)
    setPosition,
    setIsConnected,
    setSymbol,

    // Order operations
    updateOrder,
    removeOrder,
    handleOrderUpdate,
    addFill,
    syncFromSnapshot,

    // Queries
    getBuyOrders,
    getSellOrders,
    getOrdersByTag,
    getTotalPnL,

    // Utilities
    clear,
  };
}

// Create singleton store
export const orderStore = createRoot(createOrderStore);
