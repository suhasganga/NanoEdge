import { Component, For, Show, createSignal, createEffect, createMemo, on } from "solid-js";
import { useTradesWebSocket } from "~/hooks/useWebSocket";
import { cn } from "~/lib/utils";
import { settings } from "~/stores/chartSettings";
import { resolveTimezone } from "~/lib/timezone";

interface RecentTradesProps {
  symbol: string;
  maxTrades?: number;
}

interface TradeItem {
  id: number;
  price: number;
  quantity: number;
  isBuy: boolean; // !is_buyer_maker
  timestamp: number;
}

// Minimum valid timestamp: Jan 1, 2020 00:00:00 UTC in milliseconds
const MIN_VALID_TIMESTAMP_MS = 1577836800000;

function isNseMarketOpen(): boolean {
  const now = new Date();
  const utcHour = now.getUTCHours();
  const utcMinute = now.getUTCMinutes();
  const utcDay = now.getUTCDay();

  if (utcDay === 0 || utcDay === 6) return false;

  const utcMinutes = utcHour * 60 + utcMinute;
  const marketOpen = 3 * 60 + 45;
  const marketClose = 10 * 60;

  return utcMinutes >= marketOpen && utcMinutes < marketClose;
}

function isIndianSymbol(symbol: string): boolean {
  const upper = symbol.toUpperCase();
  return upper.startsWith("NSE:") || upper.startsWith("BSE:") || upper.startsWith("MCX:");
}

export const RecentTrades: Component<RecentTradesProps> = (props) => {
  const maxTrades = () => props.maxTrades ?? 50;
  const [trades, setTrades] = createSignal<TradeItem[]>([]);

  const { data: tradeData, isConnected } = useTradesWebSocket(() => props.symbol);

  // Status info when no trades
  const statusInfo = createMemo(() => {
    const connected = isConnected();
    const isIndian = isIndianSymbol(props.symbol);
    const marketOpen = isNseMarketOpen();

    if (!connected) {
      return { message: "Disconnected", color: "text-ask" };
    }

    if (isIndian && !marketOpen) {
      return { message: "Market Closed", color: "text-yellow-500" };
    }

    return { message: "Waiting for trades...", color: "text-muted-foreground" };
  });

  // Add new trade to list when received
  createEffect(() => {
    const trade = tradeData();
    if (!trade) return;

    // Validate timestamp to prevent 1970 dates from bad data
    if (trade.timestamp < MIN_VALID_TIMESTAMP_MS) {
      console.warn("Invalid trade timestamp:", trade.timestamp);
      return;
    }

    setTrades((prev) => {
      const newTrade: TradeItem = {
        id: trade.trade_id,
        price: trade.price,
        quantity: trade.quantity,
        isBuy: !trade.is_buyer_maker,
        timestamp: trade.timestamp,
      };

      // Optimize: avoid spread when at max capacity
      // Use slice to create new array reference for reactivity
      const max = maxTrades();
      if (prev.length >= max) {
        // At capacity: create new array with new trade at front, drop last
        const result = [newTrade, ...prev.slice(0, max - 1)];
        return result;
      }
      // Under capacity: simple prepend
      return [newTrade, ...prev];
    });
  });

  // Reset trades when symbol changes (explicit dependency tracking)
  createEffect(
    on(
      () => props.symbol,
      () => setTrades([]),
      { defer: true }
    )
  );

  // Get resolved timezone for display
  const getTimezone = () => resolveTimezone(settings().timezone, props.symbol);

  const formatTime = (ts: number): string => {
    const d = new Date(ts);
    return d.toLocaleTimeString("en-US", {
      hour12: false,
      timeZone: getTimezone(),
    });
  };

  const formatPrice = (price: number): string => {
    if (price >= 1000) return price.toFixed(2);
    if (price >= 1) return price.toFixed(4);
    return price.toFixed(6);
  };

  const formatQty = (qty: number): string => {
    if (qty >= 1) return qty.toFixed(4);
    return qty.toFixed(6);
  };

  return (
    <div class="flex h-full flex-col contain-content">
      {/* Header */}
      <div class="border-b border-border px-3 py-2">
        <h3 class="text-sm font-semibold">Recent Trades</h3>
      </div>

      {/* Column headers */}
      <div class="flex border-b border-border px-3 py-1 text-xs text-muted-foreground">
        <div class="flex-1">Price</div>
        <div class="flex-1 text-right">Size</div>
        <div class="w-16 text-right">Time</div>
      </div>

      {/* Trade list */}
      <div class="flex-1 overflow-y-auto scrollbar-hide">
        <Show
          when={trades().length > 0}
          fallback={
            <div class="flex h-full items-center justify-center">
              <span class={cn("text-sm", statusInfo().color)}>
                {statusInfo().message}
              </span>
            </div>
          }
        >
          <For each={trades()}>
            {(trade, index) => (
              <div
                class={cn(
                  "flex px-3 py-0.5 text-xs font-mono transition-colors hover:bg-muted/30",
                  index() === 0 && "trade-flash"
                )}
              >
                <div class={cn("flex-1", trade.isBuy ? "text-bid" : "text-ask")}>
                  {formatPrice(trade.price)}
                </div>
                <div class="flex-1 text-right">{formatQty(trade.quantity)}</div>
                <div class="w-16 text-right text-muted-foreground">
                  {formatTime(trade.timestamp)}
                </div>
              </div>
            )}
          </For>
        </Show>
      </div>
    </div>
  );
};
