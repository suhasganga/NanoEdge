import { createSignal, createEffect, onCleanup, Accessor } from "solid-js";

/**
 * Types for dynamic WebSocket data - reuse types from useWebSocket.ts
 */
export interface CandleData {
  type: string;
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
  closed?: boolean;
}

export interface DepthData {
  type: string;
  symbol: string;
  bids: [number, number][];
  asks: [number, number][];
  lastUpdateId: number;
}

export interface TradeData {
  type: string;
  symbol: string;
  price: number;
  quantity: number;
  is_buyer_maker: boolean;
  timestamp: number;
  trade_id: number;
}

export interface StatsData {
  type: string;
  symbol: string;
  price_change: number;
  price_change_percent: number;
  high_24h: number;
  low_24h: number;
  volume_24h: number;
  quote_volume_24h: number;
  trade_count_24h: number;
  last_price: number;
  open_price: number;
}

export interface DynamicSubscriptionState {
  candle: Accessor<CandleData | null>;
  depth: Accessor<DepthData | null>;
  trades: Accessor<TradeData[]>;
  stats: Accessor<StatsData | null>;
  isConnected: Accessor<boolean>;
  currentSymbol: Accessor<string | null>;
  subscribe: (exchange: string, market: string, symbol: string) => void;
}

/**
 * Dynamic WebSocket subscription hook.
 *
 * Provides a single WebSocket connection to /ws/subscribe that can switch
 * between different symbols dynamically. Unlike the separate hooks for
 * candles/depth/trades/stats, this uses one unified connection.
 *
 * Usage:
 * ```tsx
 * const { candle, depth, trades, stats, isConnected, subscribe } = useDynamicSubscription();
 *
 * // Subscribe to a symbol
 * subscribe("binance", "spot", "SOLUSDT");
 *
 * // Data is automatically updated via signals
 * console.log(candle()?.close);
 * ```
 */
export function useDynamicSubscription(): DynamicSubscriptionState {
  const [candle, setCandle] = createSignal<CandleData | null>(null);
  const [depth, setDepth] = createSignal<DepthData | null>(null);
  const [trades, setTrades] = createSignal<TradeData[]>([]);
  const [stats, setStats] = createSignal<StatsData | null>(null);
  const [isConnected, setIsConnected] = createSignal(false);
  const [currentSymbol, setCurrentSymbol] = createSignal<string | null>(null);

  let ws: WebSocket | null = null;
  let reconnectTimeout: ReturnType<typeof setTimeout> | null = null;
  let reconnectAttempts = 0;
  let pendingSubscribe: { exchange: string; market: string; symbol: string } | null = null;

  const maxReconnectAttempts = 10;
  const reconnectInterval = 1000;

  // TextDecoder for binary message handling (reused for performance)
  const textDecoder = new TextDecoder();

  const connect = () => {
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const url = `${protocol}//${window.location.host}/ws/subscribe`;

    try {
      ws = new WebSocket(url);
      // Use arraybuffer for faster binary handling (avoids Blob overhead)
      ws.binaryType = "arraybuffer";

      ws.onopen = () => {
        console.log("[WS Dynamic] Connected to /ws/subscribe");
        setIsConnected(true);
        reconnectAttempts = 0;

        // Send pending subscription if any
        if (pendingSubscribe) {
          ws?.send(JSON.stringify({ action: "subscribe", ...pendingSubscribe }));
          setCurrentSymbol(pendingSubscribe.symbol);
          pendingSubscribe = null;
        }
      };

      ws.onmessage = (event) => {
        try {
          // Handle both binary (ArrayBuffer) and text messages
          const text = event.data instanceof ArrayBuffer
            ? textDecoder.decode(event.data)
            : event.data;
          const msg = JSON.parse(text);

          // Skip heartbeat messages
          if (msg.type === "heartbeat") return;

          switch (msg.type) {
            case "candle":
              setCandle(msg);
              break;
            case "depth":
              setDepth(msg);
              break;
            case "trade":
              // Keep last 100 trades
              setTrades((prev) => [msg, ...prev.slice(0, 99)]);
              break;
            case "stats":
              setStats(msg);
              break;
            case "subscribed":
              console.log(`[WS Dynamic] Subscribed to ${msg.exchange}:${msg.market}:${msg.symbol}`);
              // Data already cleared in subscribe(), just confirm the symbol
              setCurrentSymbol(msg.symbol);
              break;
            case "unsubscribed":
              console.log("[WS Dynamic] Unsubscribed");
              setCurrentSymbol(null);
              break;
          }
        } catch (e) {
          console.error("[WS Dynamic] Failed to parse message:", e);
        }
      };

      ws.onerror = (event) => {
        console.error("[WS Dynamic] Error:", event);
      };

      ws.onclose = (event) => {
        console.log(`[WS Dynamic] Closed: ${event.code} ${event.reason}`);
        setIsConnected(false);
        ws = null;

        // Attempt reconnection with exponential backoff
        if (reconnectAttempts < maxReconnectAttempts) {
          const delay = Math.min(
            reconnectInterval * Math.pow(2, reconnectAttempts),
            30000
          );
          console.log(`[WS Dynamic] Reconnecting in ${delay}ms (attempt ${reconnectAttempts + 1})`);
          reconnectTimeout = setTimeout(() => {
            reconnectAttempts++;
            // Preserve the current subscription for reconnection
            if (currentSymbol() && !pendingSubscribe) {
              pendingSubscribe = {
                exchange: "binance", // Default, could be stored
                market: "spot",
                symbol: currentSymbol()!,
              };
            }
            connect();
          }, delay);
        }
      };
    } catch (e) {
      console.error("[WS Dynamic] Connection error:", e);
    }
  };

  const disconnect = () => {
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
      reconnectTimeout = null;
    }
    if (ws) {
      ws.close();
      ws = null;
    }
    setIsConnected(false);
  };

  const subscribe = (exchange: string, market: string, symbol: string) => {
    console.log(`[WS Dynamic] Subscribe request: ${exchange}:${market}:${symbol}`);

    // Clear all data immediately on subscribe to avoid showing stale data from previous symbol
    // This ensures users see empty/loading state until new data arrives
    setCandle(null);
    setDepth(null);
    setTrades([]);
    setStats(null);
    setCurrentSymbol(symbol);

    if (ws?.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ action: "subscribe", exchange, market, symbol }));
    } else {
      // Store for when connection opens
      pendingSubscribe = { exchange, market, symbol };

      // If not connected, try to connect
      if (!ws || ws.readyState === WebSocket.CLOSED) {
        connect();
      }
    }
  };

  // Connect on mount
  createEffect(() => {
    connect();
  });

  // Cleanup on unmount
  onCleanup(() => {
    disconnect();
  });

  return {
    candle,
    depth,
    trades,
    stats,
    isConnected,
    currentSymbol,
    subscribe,
  };
}
