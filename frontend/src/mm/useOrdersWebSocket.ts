/**
 * WebSocket hook for real-time order updates.
 *
 * Connects to /api/mm/ws/orders/{symbol} and maintains order/position state.
 * Follows the same pattern as useWebSocket.ts (connectionId, arraybuffer,
 * no reactive writes inside createEffect).
 */

import { createEffect, onCleanup, Accessor, untrack } from "solid-js";
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
  let ws: WebSocket | null = null;
  let reconnectTimeout: ReturnType<typeof setTimeout> | null = null;
  let reconnectAttempts = 0;
  let connectionId = 0;
  const MAX_RECONNECT_ATTEMPTS = 10;
  const RECONNECT_INTERVAL = 3000;

  const textDecoder = new TextDecoder();

  const handleMessage = (msg: OrderWebSocketMsg) => {
    switch (msg.type) {
      case "orders_snapshot":
        orderStore.syncFromSnapshot({
          orders: msg.orders as unknown as SimulatedOrder[],
          position: msg.position as unknown as SimulatedPosition | null,
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
        break;

      default:
        console.warn("[OrdersWS] Unknown message type:", (msg as any).type);
    }
  };

  const connect = (url: string) => {
    const currentConnectionId = ++connectionId;

    try {
      ws = new WebSocket(url);
      ws.binaryType = "arraybuffer";

      ws.onopen = () => {
        if (currentConnectionId !== connectionId) return;
        console.log(`[OrdersWS] Connected`);
        orderStore.setIsConnected(true);
        reconnectAttempts = 0;
      };

      ws.onmessage = (event) => {
        if (currentConnectionId !== connectionId) return;
        try {
          const text =
            event.data instanceof ArrayBuffer
              ? textDecoder.decode(event.data)
              : event.data;
          const msg: OrderWebSocketMsg = JSON.parse(text);
          handleMessage(msg);
        } catch (e) {
          console.error("[OrdersWS] Failed to parse message:", e);
        }
      };

      ws.onerror = () => {
        if (currentConnectionId !== connectionId) return;
      };

      ws.onclose = (event) => {
        if (currentConnectionId !== connectionId) return;
        orderStore.setIsConnected(false);
        console.log(`[OrdersWS] Closed: ${event.code} ${event.reason}`);

        if (reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
          const delay = Math.min(
            RECONNECT_INTERVAL * Math.pow(2, reconnectAttempts),
            30000
          );
          console.log(
            `[OrdersWS] Reconnecting in ${delay}ms (attempt ${reconnectAttempts + 1})`
          );
          reconnectTimeout = setTimeout(() => {
            reconnectAttempts++;
            connect(url);
          }, delay);
        }
      };
    } catch (e) {
      console.error("[OrdersWS] Connection error:", e);
    }
  };

  const disconnect = () => {
    connectionId++;
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
      reconnectTimeout = null;
    }
    if (ws) {
      ws.close();
      ws = null;
    }
    orderStore.setIsConnected(false);
  };

  // Build URL from symbol - same pattern as useCandleWebSocket etc.
  const getUrl = (sym: string): string => {
    if (!sym) return "";
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const host = window.location.host;
    return `${protocol}//${host}/api/mm/ws/orders/${sym}`;
  };

  // Effect to handle symbol changes - matches useWebSocket.ts exactly
  createEffect(() => {
    const sym = options.symbol();
    // All store writes use untrack to avoid reactive dependency tracking
    disconnect();
    if (sym) {
      untrack(() => orderStore.setSymbol(sym));
      connect(getUrl(sym));
    }
  });

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
