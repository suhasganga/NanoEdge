import { Component, Show, createMemo } from "solid-js";
import { useStatsWebSocket } from "~/hooks/useWebSocket";
import { cn } from "~/lib/utils";
import { LatencyIndicator } from "./LatencyIndicator";

interface MarketStatsBarProps {
  symbol: string;
}

/**
 * Check if NSE/Fyers market is currently open.
 * NSE trading hours: 9:15 AM - 3:30 PM IST (Monday-Friday)
 * IST = UTC + 5:30, so in UTC: 03:45 - 10:00
 */
function isNseMarketOpen(): boolean {
  const now = new Date();
  const utcHour = now.getUTCHours();
  const utcMinute = now.getUTCMinutes();
  const utcDay = now.getUTCDay(); // 0 = Sunday, 6 = Saturday

  // Weekend check
  if (utcDay === 0 || utcDay === 6) return false;

  // Convert to minutes since midnight UTC
  const utcMinutes = utcHour * 60 + utcMinute;

  // NSE opens at 03:45 UTC (9:15 IST) and closes at 10:00 UTC (15:30 IST)
  const marketOpen = 3 * 60 + 45; // 03:45 UTC
  const marketClose = 10 * 60; // 10:00 UTC

  return utcMinutes >= marketOpen && utcMinutes < marketClose;
}

/**
 * Check if symbol is from Indian exchanges (NSE/BSE/MCX)
 */
function isIndianSymbol(symbol: string): boolean {
  const upper = symbol.toUpperCase();
  return upper.startsWith("NSE:") || upper.startsWith("BSE:") || upper.startsWith("MCX:");
}

export const MarketStatsBar: Component<MarketStatsBarProps> = (props) => {
  const { data: stats, isConnected, latency } = useStatsWebSocket(() => props.symbol);

  const formatPrice = (price: number): string => {
    if (price >= 1000) {
      return price.toLocaleString(undefined, {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      });
    }
    return price.toFixed(4);
  };

  const formatChange = (change: number): string => {
    const abs = Math.abs(change);
    const sign = change >= 0 ? "+" : "";
    if (abs >= 100) return `${sign}${change.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    if (abs >= 1) return `${sign}${change.toFixed(4)}`;
    return `${sign}${change.toFixed(6)}`;
  };

  const formatPercent = (pct: number): string => {
    return `${pct >= 0 ? "+" : ""}${pct.toFixed(2)}%`;
  };

  const formatVolume = (vol: number): string => {
    if (vol >= 1_000_000) return `${(vol / 1_000_000).toFixed(2)}M`;
    if (vol >= 1_000) return `${(vol / 1_000).toFixed(2)}K`;
    return vol.toFixed(2);
  };

  // Determine status message and color when no data
  const statusInfo = createMemo(() => {
    const connected = isConnected();
    const isIndian = isIndianSymbol(props.symbol);
    const marketOpen = isNseMarketOpen();

    if (!connected) {
      return { message: "Disconnected", color: "bg-ask", textColor: "text-ask" };
    }

    if (isIndian && !marketOpen) {
      return { message: "Market Closed", color: "bg-yellow-500", textColor: "text-yellow-500" };
    }

    return { message: "Waiting for data...", color: "bg-yellow-500", textColor: "text-muted-foreground" };
  });

  return (
    <div class="border-b border-border px-3 py-2.5 bg-muted/10">
      <Show
        when={stats()}
        fallback={
          <div class="flex items-center justify-between">
            <div class={cn("text-xs", statusInfo().textColor)}>
              {statusInfo().message}
            </div>
            <LatencyIndicator
              isConnected={isConnected()}
              latency={latency()}
              symbol={props.symbol}
              compact
            />
          </div>
        }
      >
        {(s) => (
          <>
            {/* Row 1: Price + Latency */}
            <div class="flex items-center justify-between">
              <span class="text-xl font-semibold font-mono">
                {formatPrice(s().last_price)}
              </span>
              <LatencyIndicator
                isConnected={isConnected()}
                latency={latency()}
                symbol={props.symbol}
                compact
              />
            </div>

            {/* Row 2: Change + Market Status */}
            <div class="flex items-center gap-2 mt-0.5">
              <span
                class={cn(
                  "text-sm font-mono",
                  s().price_change >= 0 ? "text-bid" : "text-ask"
                )}
              >
                {formatChange(s().price_change)} ({formatPercent(s().price_change_percent)})
              </span>
              <Show when={isIndianSymbol(props.symbol) && !isNseMarketOpen()}>
                <span class="text-xs text-yellow-500 bg-yellow-500/10 px-1.5 py-0.5 rounded">
                  Closed
                </span>
              </Show>
            </div>

            {/* Row 3: 24h Stats - horizontal compact */}
            <div class="flex items-center gap-4 mt-2 text-xs">
              <div>
                <span class="text-muted-foreground">H </span>
                <span class="font-mono text-bid">{formatPrice(s().high_24h)}</span>
              </div>
              <div>
                <span class="text-muted-foreground">L </span>
                <span class="font-mono text-ask">{formatPrice(s().low_24h)}</span>
              </div>
              <div>
                <span class="text-muted-foreground">V </span>
                <span class="font-mono">{formatVolume(s().volume_24h)}</span>
              </div>
            </div>
          </>
        )}
      </Show>
    </div>
  );
};
