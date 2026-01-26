import { createSignal, createEffect, onCleanup, Accessor } from "solid-js";

/**
 * Server-side latency histogram stats from /api/metrics.
 */
export interface HistogramStats {
  name: string;
  count: number;
  current_samples: number;
  p50_us: number;
  p95_us: number;
  p99_us: number;
  mean_us: number;
  min_us: number;
  max_us: number;
}

export interface ExchangeClockInfo {
  offset_ms: number;  // Local - Exchange (positive = local ahead)
  rtt_ms: number;     // Round-trip time to exchange
}

export interface ClockSyncInfo {
  [exchange: string]: ExchangeClockInfo;  // Per-exchange clock offsets
}

export interface ServerMetrics {
  ws_network: HistogramStats;
  parse_json: HistogramStats;
  parse_protobuf: HistogramStats;
  normalize: HistogramStats;
  agg_update: HistogramStats;
  api_ws_push: HistogramStats;
  db_write: HistogramStats;
  orderbook_update: HistogramStats;
  clock_sync?: ClockSyncInfo;
}

export interface UseLatencyMetricsResult {
  metrics: Accessor<ServerMetrics | null>;
  error: Accessor<string | null>;
  loading: Accessor<boolean>;
  refresh: () => Promise<void>;
}

/**
 * Hook to fetch server-side latency metrics from /api/metrics.
 * Fetches every `intervalMs` milliseconds when `enabled` is true.
 *
 * @param enabled - Accessor that controls whether polling is active
 * @param intervalMs - Polling interval in milliseconds (default: 5000)
 */
export function useLatencyMetrics(
  enabled: Accessor<boolean>,
  intervalMs: number = 5000
): UseLatencyMetricsResult {
  const [metrics, setMetrics] = createSignal<ServerMetrics | null>(null);
  const [error, setError] = createSignal<string | null>(null);
  const [loading, setLoading] = createSignal(false);

  let intervalId: ReturnType<typeof setInterval> | null = null;

  const fetchMetrics = async () => {
    if (!enabled()) return;

    setLoading(true);
    try {
      const response = await fetch("/api/metrics");
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      const data = await response.json();
      setMetrics(data);
      setError(null);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to fetch metrics");
    } finally {
      setLoading(false);
    }
  };

  // Effect to manage polling based on enabled state
  createEffect(() => {
    if (enabled()) {
      // Initial fetch
      fetchMetrics();

      // Start polling
      intervalId = setInterval(fetchMetrics, intervalMs);
    } else {
      // Stop polling when disabled
      if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
      }
    }
  });

  // Cleanup on unmount
  onCleanup(() => {
    if (intervalId) {
      clearInterval(intervalId);
    }
  });

  return {
    metrics,
    error,
    loading,
    refresh: fetchMetrics,
  };
}
