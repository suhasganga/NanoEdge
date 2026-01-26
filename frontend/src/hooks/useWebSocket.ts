import { createSignal, onCleanup, createEffect, Accessor } from "solid-js";

export interface WebSocketOptions<T> {
  url: Accessor<string>;
  onMessage?: (data: T) => void;
  reconnectInterval?: number;
  maxReconnectAttempts?: number;
  /** Minimum interval between state updates in ms (default: 16ms = 60fps) */
  throttleMs?: number;
}

/**
 * Latency chain breakdown for end-to-end timing analysis.
 *
 * Timestamp chain:
 * T0 (exch_ts/timestamp) → T1 (recv_ts) → T3 (api_ts) → T4 (client_ts)
 */
export interface LatencyChain {
  // Individual stage latencies (ms)
  network: number;      // T1 - T0: Exchange → Server receive
  server: number;       // T3 - T1: Server processing (parse + process)
  client: number;       // T4 - T3: Server → Client
  total: number;        // T4 - T0: Total end-to-end

  // Rolling averages (ms) - last 100 samples
  avgNetwork: number;
  avgServer: number;
  avgClient: number;
  avgTotal: number;

  // Sample count
  sampleCount: number;

  // Clock skew flag - when true, network/server are unmeasurable
  hasClockSkew: boolean;
}

export interface WebSocketState<T> {
  data: Accessor<T | null>;
  isConnected: Accessor<boolean>;
  error: Accessor<string | null>;
  send: (message: unknown) => void;
  latency: Accessor<LatencyChain | null>;
}

/**
 * Rolling window for latency samples (fixed size).
 */
class LatencyRollingWindow {
  private samples: number[] = [];
  private maxSize: number;

  constructor(maxSize: number = 100) {
    this.maxSize = maxSize;
  }

  add(value: number): void {
    this.samples.push(value);
    if (this.samples.length > this.maxSize) {
      this.samples.shift();
    }
  }

  average(): number {
    if (this.samples.length === 0) return 0;
    return this.samples.reduce((a, b) => a + b, 0) / this.samples.length;
  }

  count(): number {
    return this.samples.length;
  }

  clear(): void {
    this.samples = [];
  }
}

/**
 * WebSocket hook with RAF batching for HFT performance.
 * Only updates state at 60fps to avoid excessive re-renders.
 */
export function useWebSocket<T>(options: WebSocketOptions<T>): WebSocketState<T> {
  const [data, setData] = createSignal<T | null>(null);
  const [isConnected, setIsConnected] = createSignal(false);
  const [error, setError] = createSignal<string | null>(null);
  const [latency, setLatency] = createSignal<LatencyChain | null>(null);

  let ws: WebSocket | null = null;
  let reconnectAttempts = 0;
  let reconnectTimeout: ReturnType<typeof setTimeout> | null = null;
  let throttleTimeout: ReturnType<typeof setTimeout> | null = null;
  let pendingData: T | null = null;
  let connectionId = 0;
  let lastUpdateTime = 0;

  // Rolling windows for latency averages
  const networkWindow = new LatencyRollingWindow(100);
  const serverWindow = new LatencyRollingWindow(100);
  const clientWindow = new LatencyRollingWindow(100);
  const totalWindow = new LatencyRollingWindow(100);

  const {
    reconnectInterval = 3000,
    maxReconnectAttempts = 10,
    onMessage,
    throttleMs = 16, // Default 60fps
  } = options;

  // Throttled update: Only flush data at specified interval
  const scheduleFlush = () => {
    if (throttleTimeout !== null) return; // Already scheduled

    const now = performance.now();
    const elapsed = now - lastUpdateTime;
    const delay = Math.max(0, throttleMs - elapsed);

    throttleTimeout = setTimeout(() => {
      throttleTimeout = null;
      if (pendingData !== null) {
        lastUpdateTime = performance.now();
        const dataToFlush = pendingData;
        pendingData = null;
        setData(() => dataToFlush);
        if (onMessage) {
          onMessage(dataToFlush);
        }
      }
    }, delay);
  };

  const cancelThrottle = () => {
    if (throttleTimeout !== null) {
      clearTimeout(throttleTimeout);
      throttleTimeout = null;
    }
  };

  // TextDecoder for binary message handling (reused for performance)
  const textDecoder = new TextDecoder();

  const connect = (url: string) => {
    // Increment connection ID to invalidate stale handlers
    const currentConnectionId = ++connectionId;

    try {
      ws = new WebSocket(url);
      // Use arraybuffer for faster binary handling (avoids Blob overhead)
      ws.binaryType = "arraybuffer";

      ws.onopen = () => {
        if (currentConnectionId !== connectionId) return;
        setIsConnected(true);
        setError(null);
        reconnectAttempts = 0;
        console.log(`[WS] Connected to ${url}`);
      };

      ws.onmessage = (event) => {
        if (currentConnectionId !== connectionId) return;
        const clientTs = Date.now();  // T4: Client receive timestamp

        try {
          // Handle both binary (ArrayBuffer) and text messages
          const text = event.data instanceof ArrayBuffer
            ? textDecoder.decode(event.data)
            : event.data;
          const parsed = JSON.parse(text) as T;
          // Skip heartbeat messages
          if ((parsed as any).type === "heartbeat") return;

          // Extract timestamps for latency calculation
          // T0: Exchange event time (exch_ts or timestamp field, in ms)
          // T1: Server receive time (recv_ts)
          // T3: API push time (api_ts)
          const msg = parsed as any;
          const exchTs = msg.exch_ts || msg.timestamp;
          const recvTs = msg.recv_ts;
          const apiTs = msg.api_ts;

          // Calculate latency chain if timestamps are present
          // Full chain: exchTs → recvTs → apiTs → clientTs
          // Partial chain: exchTs → apiTs → clientTs (when recv_ts is 0)
          if (exchTs && apiTs && apiTs > 0) {
            const hasFullChain = recvTs && recvTs > 0;
            let total = clientTs - exchTs;    // T4 - T0
            const client = clientTs - apiTs;    // T4 - T3

            let network: number;
            let server: number;

            if (hasFullChain) {
              // Full chain available
              network = recvTs - exchTs;    // T1 - T0
              server = apiTs - recvTs;      // T3 - T1
            } else {
              // Partial chain - estimate network+server combined
              network = apiTs - exchTs;     // T3 - T0 (network + server combined)
              server = 0;                   // Unknown when recv_ts missing
            }

            // Handle clock skew: if exchange clock is ahead of local clock,
            // network latency appears negative. In this case, we can't reliably
            // measure network/server latency, but client latency is still valid.
            const hasClockSkew = network < 0 || total < 0;
            if (hasClockSkew) {
              // When clock skew detected, use client latency as the primary metric
              // Set network/server to 0 (unmeasurable) and use client as total
              network = 0;
              server = 0;
              total = client;  // Best estimate we have
            }

            // Only track positive client latency (basic sanity check)
            if (client >= 0) {
              // Only add to rolling windows if we have reliable data (no clock skew)
              if (!hasClockSkew && hasFullChain && server >= 0) {
                networkWindow.add(network);
                serverWindow.add(server);
                clientWindow.add(client);
                totalWindow.add(total);
              } else if (client >= 0) {
                // With clock skew, still track client latency
                clientWindow.add(client);
                totalWindow.add(client);  // Use client as proxy for total
              }

              setLatency({
                network,
                server,
                client,
                total,
                avgNetwork: networkWindow.average(),
                avgServer: serverWindow.average(),
                avgClient: clientWindow.average(),
                avgTotal: totalWindow.average(),
                sampleCount: totalWindow.count(),
                hasClockSkew,
              });
            }
          }

          // Store pending data and schedule throttled flush
          pendingData = parsed;
          scheduleFlush();
        } catch (e) {
          console.error("[WS] Failed to parse message:", e);
        }
      };

      ws.onerror = (event) => {
        if (currentConnectionId !== connectionId) return;
        console.error("[WS] Error:", event);
        setError("WebSocket error occurred");
      };

      ws.onclose = (event) => {
        if (currentConnectionId !== connectionId) return;
        setIsConnected(false);
        cancelThrottle();
        console.log(`[WS] Closed: ${event.code} ${event.reason}`);

        // Attempt reconnection
        if (reconnectAttempts < maxReconnectAttempts) {
          const delay = Math.min(
            reconnectInterval * Math.pow(2, reconnectAttempts),
            30000
          );
          console.log(`[WS] Reconnecting in ${delay}ms (attempt ${reconnectAttempts + 1})`);
          reconnectTimeout = setTimeout(() => {
            reconnectAttempts++;
            connect(url);
          }, delay);
        } else {
          setError("Max reconnection attempts reached");
        }
      };
    } catch (e) {
      console.error("[WS] Connection error:", e);
      setError(`Failed to connect: ${e}`);
    }
  };

  const disconnect = () => {
    connectionId++; // Invalidate any pending handlers
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
      reconnectTimeout = null;
    }
    cancelThrottle();
    pendingData = null; // Clear any pending data
    if (ws) {
      ws.close();
      ws = null;
    }
    setIsConnected(false);
    setData(null); // Clear data on disconnect to avoid showing stale data from previous symbol
    setLatency(null); // Clear latency on disconnect
    // Clear rolling windows
    networkWindow.clear();
    serverWindow.clear();
    clientWindow.clear();
    totalWindow.clear();
  };

  const send = (message: unknown) => {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(typeof message === "string" ? message : JSON.stringify(message));
    }
  };

  // Effect to handle URL changes
  createEffect(() => {
    const url = options.url();
    disconnect();
    if (url) {
      connect(url);
    }
  });

  // Cleanup on unmount
  onCleanup(() => {
    disconnect();
  });

  return {
    data,
    isConnected,
    error,
    send,
    latency,
  };
}

/**
 * Specialized hook for candle WebSocket
 */
export interface CandleData {
  type: string;
  symbol: string;
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
  is_closed?: boolean;
}

export function useCandleWebSocket(symbol: Accessor<string>) {
  const url = () => {
    const s = symbol();
    if (!s) return "";
    // Use relative URL which will be proxied by Vite in dev
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const host = window.location.host;
    return `${protocol}//${host}/ws/candles/${s}`;
  };

  return useWebSocket<CandleData>({ url });
}

/**
 * Specialized hook for depth/orderbook WebSocket
 */
export interface DepthData {
  type: string;
  symbol: string;
  bids: [string, string][];
  asks: [string, string][];
  spread?: number;
}

export function useDepthWebSocket(symbol: Accessor<string>) {
  const url = () => {
    const s = symbol();
    if (!s) return "";
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const host = window.location.host;
    return `${protocol}//${host}/ws/depth/${s}`;
  };

  // Throttle depth updates to 10fps (100ms) - balance between perf and latency
  return useWebSocket<DepthData>({ url, throttleMs: 100 });
}

/**
 * Specialized hook for recent trades WebSocket
 */
export interface TradeData {
  type: string;
  symbol: string;
  price: number;
  quantity: number;
  is_buyer_maker: boolean;
  timestamp: number;
  trade_id: number;
}

export function useTradesWebSocket(symbol: Accessor<string>) {
  const url = () => {
    const s = symbol();
    if (!s) return "";
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const host = window.location.host;
    return `${protocol}//${host}/ws/trades/${s}`;
  };

  // Throttle trade updates to 20fps (50ms) - trades should feel responsive
  return useWebSocket<TradeData>({ url, throttleMs: 50 });
}

/**
 * Specialized hook for 24h market stats WebSocket
 */
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

export function useStatsWebSocket(symbol: Accessor<string>) {
  const url = () => {
    const s = symbol();
    if (!s) return "";
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const host = window.location.host;
    return `${protocol}//${host}/ws/stats/${s}`;
  };

  // Throttle stats updates to 5fps (200ms) - price/change should update quickly
  return useWebSocket<StatsData>({ url, throttleMs: 200 });
}
