import { Component, Show, createSignal, createMemo } from "solid-js";
import { LatencyChain } from "~/hooks/useWebSocket";
import { LatencyTooltip } from "./LatencyTooltip";
import { cn } from "~/lib/utils";

interface LatencyIndicatorProps {
  isConnected: boolean;
  latency: LatencyChain | null;
  symbol: string;
  compact?: boolean;
}

/**
 * Health status based on total E2E latency.
 */
type HealthStatus = "excellent" | "good" | "fair" | "poor" | "disconnected";

function getHealthStatus(totalMs: number | null, isConnected: boolean): HealthStatus {
  if (!isConnected) return "disconnected";
  if (totalMs === null) return "disconnected";
  if (totalMs < 100) return "excellent";
  if (totalMs < 500) return "good";
  if (totalMs < 2000) return "fair";
  return "poor";
}

function getHealthColor(status: HealthStatus): string {
  switch (status) {
    case "excellent":
      return "bg-bid";
    case "good":
      return "bg-bid/70";
    case "fair":
      return "bg-yellow-500";
    case "poor":
      return "bg-orange-500";
    case "disconnected":
      return "bg-ask";
  }
}

function getHealthTextColor(status: HealthStatus): string {
  switch (status) {
    case "excellent":
      return "text-bid";
    case "good":
      return "text-bid/70";
    case "fair":
      return "text-yellow-500";
    case "poor":
      return "text-orange-500";
    case "disconnected":
      return "text-ask";
  }
}

/**
 * LatencyIndicator component shows total E2E latency below the live indicator.
 * Displays both current value and rolling average.
 * Shows detailed tooltip on hover with full chain breakdown.
 */
export const LatencyIndicator: Component<LatencyIndicatorProps> = (props) => {
  const [showTooltip, setShowTooltip] = createSignal(false);

  const healthStatus = createMemo(() =>
    getHealthStatus(props.latency?.total ?? null, props.isConnected)
  );

  const dotColor = createMemo(() => getHealthColor(healthStatus()));
  const textColor = createMemo(() => getHealthTextColor(healthStatus()));

  const formatLatency = (ms: number): string => {
    if (ms < 1) return "<1ms";
    if (ms < 1000) return `${Math.round(ms)}ms`;
    return `${(ms / 1000).toFixed(1)}s`;
  };

  const statusLabel = createMemo(() => {
    if (!props.isConnected) return "Disconnected";
    if (!props.latency) return "Connected";
    return "Live";
  });

  return (
    <div
      class="relative flex items-center gap-1.5"
      onMouseEnter={() => setShowTooltip(true)}
      onMouseLeave={() => setShowTooltip(false)}
    >
      {/* Status dot */}
      <div
        class={cn("h-2 w-2 rounded-full", dotColor())}
        title={statusLabel()}
      />

      {/* Latency text */}
      <Show when={props.latency && props.isConnected}>
        <div class={cn("text-xs font-mono", textColor())}>
          {formatLatency(props.latency!.total)}
          <Show when={!props.compact && props.latency!.sampleCount > 0}>
            <span class="text-muted-foreground ml-1">
              (avg: {formatLatency(props.latency!.avgTotal)})
            </span>
          </Show>
        </div>
      </Show>

      {/* Status label when no latency data */}
      <Show when={!props.latency || !props.isConnected}>
        <div class={cn("text-xs", textColor())}>{statusLabel()}</div>
      </Show>

      {/* Tooltip */}
      <Show when={showTooltip() && props.isConnected}>
        <LatencyTooltip latency={props.latency} symbol={props.symbol} />
      </Show>
    </div>
  );
};
