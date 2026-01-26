/**
 * WebSocket hook for real-time order updates.
 *
 * Connects to /ws/orders/{symbol} and maintains order/position state.
 */

import { createEffect, onCleanup, Accessor } from "solid-js";
import { orderStore } from "./orderStore";
import type {
  OrderWebSocketMsg,
  SimulatedOrder,
  SimulatedPosition,
  OrderFill,
} from "./types";

interface UseOrdersWebSocketOptions {
  /** Function returning the current symbol */
  symbol: Accessor<string>;
  /** API host override (defaults to window.location.host) */
  host?: string;
}

interface UseOrdersWebSocketReturn {
  /** Whether WebSocket is connected */
  isConnected: Accessor<boolean>;
  /** Current orders (reactive) */
  orders: Accessor<SimulatedOrder[]>;
  /** Current position (reactive) */
  position: Accessor<SimulatedPosition | null>;
  /** Recent fills (reactive) */
  fills: Accessor<OrderFill[]>;
}

export function useOrdersWebSocket(
  options: UseOrdersWebSocketOptions
): UseOrdersWebSocketReturn {
  const { symbol, host } = options;

  let ws: WebSocket | null = null;
  let reconnectTimeout: ReturnType<typeof setTimeout> | null = null;
  let reconnectAttempts = 0;
  const MAX_RECONNECT_ATTEMPTS = 10;
  const BASE_RECONNECT_DELAY = 1000;

  const getWsUrl = (sym: string): string => {
    const wsHost = host || window.location.host;
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    return `${protocol}//${wsHost}/api/mm/ws/orders/${sym}`;
  };

  const connect = (sym: string) => {
    if (!sym) return;

    // Close existing connection
    if (ws) {
      ws.close();
      ws = null;
    }

    // Clear any pending reconnect
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
      reconnectTimeout = null;
    }

    orderStore.setSymbol(sym);

    const url = getWsUrl(sym);
    console.log(`[OrdersWS] Connecting to ${url}`);

    try {
      ws = new WebSocket(url);
    } catch (e) {
      console.error("[OrdersWS] Failed to create WebSocket:", e);
      scheduleReconnect(sym);
      return;
    }

    ws.onopen = () => {
      console.log(`[OrdersWS] Connected to ${sym}`);
      orderStore.setIsConnected(true);
      reconnectAttempts = 0;
    };

    ws.onclose = (event) => {
      console.log(`[OrdersWS] Disconnected from ${sym}:`, event.code);
      orderStore.setIsConnected(false);

      // Reconnect if not intentionally closed
      if (event.code !== 1000 && symbol() === sym) {
        scheduleReconnect(sym);
      }
    };

    ws.onerror = (error) => {
      console.error("[OrdersWS] Error:", error);
    };

    ws.onmessage = (event) => {
      try {
        const msg: OrderWebSocketMsg = JSON.parse(event.data);
        handleMessage(msg);
      } catch (e) {
        console.error("[OrdersWS] Failed to parse message:", e);
      }
    };
  };

  const handleMessage = (msg: OrderWebSocketMsg) => {
    switch (msg.type) {
      case "orders_snapshot":
        orderStore.syncFromSnapshot({
          orders: msg.orders as SimulatedOrder[],
          position: msg.position as SimulatedPosition | null,
        });
        break;

      case "order_update":
        orderStore.handleOrderUpdate(msg as unknown as SimulatedOrder);
        break;

      case "position_update":
        orderStore.setPosition(msg as unknown as SimulatedPosition);
        break;

      case "order_fill":
        orderStore.addFill(msg as unknown as OrderFill);
        break;

      case "heartbeat":
        // Ignore heartbeat
        break;

      default:
        console.warn("[OrdersWS] Unknown message type:", (msg as any).type);
    }
  };

  const scheduleReconnect = (sym: string) => {
    if (reconnectAttempts >= MAX_RECONNECT_ATTEMPTS) {
      console.error("[OrdersWS] Max reconnect attempts reached");
      return;
    }

    const delay = Math.min(
      BASE_RECONNECT_DELAY * Math.pow(2, reconnectAttempts),
      30000
    );
    reconnectAttempts++;

    console.log(
      `[OrdersWS] Reconnecting in ${delay}ms (attempt ${reconnectAttempts})`
    );

    reconnectTimeout = setTimeout(() => {
      if (symbol() === sym) {
        connect(sym);
      }
    }, delay);
  };

  const disconnect = () => {
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
      reconnectTimeout = null;
    }

    if (ws) {
      ws.close(1000);
      ws = null;
    }

    orderStore.setIsConnected(false);
  };

  // Effect to manage connection on symbol change
  createEffect(() => {
    const sym = symbol();
    if (sym) {
      connect(sym);
    } else {
      disconnect();
    }
  });

  // Cleanup on unmount
  onCleanup(() => {
    disconnect();
  });

  return {
    isConnected: orderStore.isConnected,
    orders: orderStore.orders,
    position: orderStore.position,
    fills: orderStore.fills,
  };
}
