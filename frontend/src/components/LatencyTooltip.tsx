import { Component, For, Show } from "solid-js";
import { LatencyChain } from "~/hooks/useWebSocket";
import { useLatencyMetrics, HistogramStats } from "~/hooks/useLatencyMetrics";

interface LatencyTooltipProps {
  latency: LatencyChain | null;
  symbol: string;
}

/**
 * Format latency value for display.
 */
function formatMs(ms: number): string {
  if (ms < 1) return "<1ms";
  if (ms < 1000) return `${Math.round(ms)}ms`;
  return `${(ms / 1000).toFixed(1)}s`;
}

/**
 * Format microseconds to readable string.
 */
function formatUs(us: number): string {
  if (us < 1000) return `${Math.round(us)}us`;
  return `${(us / 1000).toFixed(1)}ms`;
}

/**
 * Render a single histogram stat row.
 */
const HistogramRow: Component<{ label: string; stats: HistogramStats }> = (props) => (
  <div class="flex justify-between gap-4 text-xs">
    <span class="text-muted-foreground">{props.label}:</span>
    <span class="font-mono">
      p50={formatUs(props.stats.p50_us)} p95={formatUs(props.stats.p95_us)}
    </span>
  </div>
);

/**
 * LatencyTooltip shows detailed latency chain breakdown on hover.
 * Also fetches and displays server-side percentile metrics.
 */
export const LatencyTooltip: Component<LatencyTooltipProps> = (props) => {
  // Always fetch metrics when tooltip is shown
  const { metrics, loading, error } = useLatencyMetrics(() => true, 5000);

  return (
    <div class="absolute right-0 top-full mt-2 z-50 bg-background border border-border rounded-md shadow-lg p-3 min-w-[280px]">
      {/* Header */}
      <div class="text-sm font-medium mb-2 border-b border-border pb-2">
        Latency Chain - {props.symbol}
      </div>

      {/* E2E Breakdown */}
      <Show when={props.latency}>
        <div class="space-y-1 mb-3">
          <div class="text-xs text-muted-foreground mb-1">
            End-to-End Breakdown
            {props.latency!.hasClockSkew && (
              <span class="text-yellow-500 ml-1">(clock skew)</span>
            )}
            {!props.latency!.hasClockSkew && props.latency!.server === 0 && props.latency!.sampleCount === 0 && (
              <span class="text-yellow-500 ml-1">(partial)</span>
            )}
          </div>

          {/* Clock skew detected - show limited data */}
          <Show when={props.latency!.hasClockSkew}>
            <div class="flex justify-between text-xs">
              <span class="text-muted-foreground">Network+Server</span>
              <span class="font-mono text-yellow-500">
                N/A (clock skew)
              </span>
            </div>
          </Show>

          {/* Full chain available (no clock skew) */}
          <Show when={!props.latency!.hasClockSkew && (props.latency!.server > 0 || props.latency!.sampleCount > 0)}>
            {/* Network latency */}
            <div class="flex justify-between text-xs">
              <span class="text-muted-foreground">Network (Exch→Server)</span>
              <span class="font-mono">
                {formatMs(props.latency!.network)}
                <span class="text-muted-foreground ml-2">
                  avg: {formatMs(props.latency!.avgNetwork)}
                </span>
              </span>
            </div>

            {/* Server processing */}
            <div class="flex justify-between text-xs">
              <span class="text-muted-foreground">Server Processing</span>
              <span class="font-mono">
                {formatMs(props.latency!.server)}
                <span class="text-muted-foreground ml-2">
                  avg: {formatMs(props.latency!.avgServer)}
                </span>
              </span>
            </div>
          </Show>

          {/* Partial chain - combined network+server (no clock skew) */}
          <Show when={!props.latency!.hasClockSkew && props.latency!.server === 0 && props.latency!.sampleCount === 0}>
            <div class="flex justify-between text-xs">
              <span class="text-muted-foreground">Network+Server</span>
              <span class="font-mono text-yellow-500">
                {formatMs(props.latency!.network)}
              </span>
            </div>
          </Show>

          {/* Client latency */}
          <div class="flex justify-between text-xs">
            <span class="text-muted-foreground">Client (Server→Browser)</span>
            <span class="font-mono">
              {formatMs(props.latency!.client)}
              <span class="text-muted-foreground ml-2">
                avg: {formatMs(props.latency!.avgClient)}
              </span>
            </span>
          </div>

          {/* Divider */}
          <div class="border-t border-border my-2" />

          {/* Total E2E */}
          <div class="flex justify-between text-xs font-medium">
            <span>Total E2E{props.latency!.hasClockSkew && " (client only)"}</span>
            <span class="font-mono">
              {formatMs(props.latency!.total)}
              <span class="text-muted-foreground ml-2">
                avg: {formatMs(props.latency!.avgTotal)}
              </span>
            </span>
          </div>

          {/* Sample count */}
          <div class="text-xs text-muted-foreground mt-2">
            Samples: {props.latency!.sampleCount.toLocaleString()}
          </div>

          {/* Clock skew explanation */}
          <Show when={props.latency!.hasClockSkew}>
            <div class="text-xs text-yellow-500/80 mt-1">
              Exchange clock ahead of server - using client latency
            </div>
          </Show>
        </div>
      </Show>

      {/* No latency data */}
      <Show when={!props.latency}>
        <div class="text-xs text-muted-foreground mb-3">
          Waiting for latency data...
        </div>
      </Show>

      {/* Server-Side Metrics */}
      <div class="border-t border-border pt-2">
        <div class="text-xs text-muted-foreground mb-1">
          Server-Side Percentiles
        </div>

        <Show when={loading()}>
          <div class="text-xs text-muted-foreground">Loading metrics...</div>
        </Show>

        <Show when={error()}>
          <div class="text-xs text-ask">Error: {error()}</div>
        </Show>

        <Show when={metrics() && !loading()}>
          <div class="space-y-0.5">
            <Show when={metrics()!.parse_json.count > 0}>
              <HistogramRow label="Parse JSON" stats={metrics()!.parse_json} />
            </Show>
            <Show when={metrics()!.api_ws_push.count > 0}>
              <HistogramRow label="WS Push" stats={metrics()!.api_ws_push} />
            </Show>
            <Show when={metrics()!.orderbook_update.count > 0}>
              <HistogramRow label="Order Book" stats={metrics()!.orderbook_update} />
            </Show>
            <Show when={metrics()!.agg_update.count > 0}>
              <HistogramRow label="Aggregator" stats={metrics()!.agg_update} />
            </Show>
          </div>

          {/* Per-Exchange Clock Sync Info */}
          <Show when={metrics()!.clock_sync && Object.keys(metrics()!.clock_sync!).length > 0}>
            <div class="mt-2 pt-2 border-t border-border/50 space-y-1">
              <div class="text-xs text-muted-foreground mb-1">Clock Offsets:</div>
              <For each={Object.entries(metrics()!.clock_sync!)}>
                {([exchange, info]) => (
                  <div class="flex justify-between gap-4 text-xs">
                    <span class="text-muted-foreground capitalize">{exchange}:</span>
                    <span class="font-mono">
                      {info.offset_ms > 0 ? "+" : ""}
                      {info.offset_ms.toFixed(0)}ms
                      <span class="text-muted-foreground ml-1">
                        (RTT: {info.rtt_ms.toFixed(0)}ms)
                      </span>
                    </span>
                  </div>
                )}
              </For>
            </div>
          </Show>
        </Show>
      </div>

      {/* Legend */}
      <div class="border-t border-border pt-2 mt-2 text-xs text-muted-foreground">
        T0=Exchange T1=Recv T3=Push T4=Client
      </div>
    </div>
  );
};
