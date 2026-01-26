import {
  Component,
  createMemo,
  createSignal,
  For,
  Show,
} from "solid-js";
import { useDepthWebSocket } from "~/hooks/useWebSocket";
import { cn } from "~/lib/utils";

interface OrderBookProps {
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
  const utcDay = now.getUTCDay();

  if (utcDay === 0 || utcDay === 6) return false;

  const utcMinutes = utcHour * 60 + utcMinute;
  const marketOpen = 3 * 60 + 45; // 03:45 UTC
  const marketClose = 10 * 60; // 10:00 UTC

  return utcMinutes >= marketOpen && utcMinutes < marketClose;
}

function isIndianSymbol(symbol: string): boolean {
  const upper = symbol.toUpperCase();
  return upper.startsWith("NSE:") || upper.startsWith("BSE:") || upper.startsWith("MCX:");
}

interface OrderLevel {
  price: number;
  size: number;
  total: number;
  percentage: number;
}

// Price grouping options
const GROUPING_OPTIONS = [
  { value: 0, label: "None" },
  { value: 0.01, label: "0.01" },
  { value: 0.1, label: "0.1" },
  { value: 1, label: "1" },
  { value: 10, label: "10" },
  { value: 100, label: "100" },
];

// Maximum depth levels to render (prevents DOM explosion on large orderbooks)
// Backend sends 50 levels, matching that for optimal performance
const MAX_DEPTH_LEVELS = 50;

export const OrderBook: Component<OrderBookProps> = (props) => {
  // Price grouping state
  const [priceGrouping, setPriceGrouping] = createSignal(0);
  const [hoveredRow, setHoveredRow] = createSignal<{
    side: "bid" | "ask";
    index: number;
  } | null>(null);

  // WebSocket for depth updates
  const { data: depthData, isConnected } = useDepthWebSocket(() => props.symbol);

  // Group price levels by grouping factor
  const groupLevels = (
    levels: OrderLevel[],
    groupSize: number,
    isBid: boolean
  ): OrderLevel[] => {
    if (groupSize === 0) return levels;

    const grouped = new Map<number, OrderLevel>();
    for (const level of levels) {
      const groupedPrice = isBid
        ? Math.floor(level.price / groupSize) * groupSize
        : Math.ceil(level.price / groupSize) * groupSize;

      const existing = grouped.get(groupedPrice);
      if (existing) {
        existing.size += level.size;
      } else {
        grouped.set(groupedPrice, { ...level, price: groupedPrice });
      }
    }

    return Array.from(grouped.values()).sort((a, b) =>
      isBid ? b.price - a.price : a.price - b.price
    );
  };

  // Process bids and asks - show ALL levels (no slice)
  const processedData = createMemo(() => {
    const depth = depthData();
    if (!depth) {
      return { bids: [], asks: [], spread: 0, midPrice: 0 };
    }

    // Parse, sort, and limit bids (highest first)
    // Slice to MAX_DEPTH_LEVELS to prevent DOM explosion while allowing scroll
    let bids: OrderLevel[] = depth.bids
      .map(([price, size]) => ({
        price: parseFloat(price),
        size: parseFloat(size),
        total: 0,
        percentage: 0,
      }))
      .sort((a, b) => b.price - a.price)
      .slice(0, MAX_DEPTH_LEVELS);

    // Parse, sort, and limit asks (lowest first)
    let asks: OrderLevel[] = depth.asks
      .map(([price, size]) => ({
        price: parseFloat(price),
        size: parseFloat(size),
        total: 0,
        percentage: 0,
      }))
      .sort((a, b) => a.price - b.price)
      .slice(0, MAX_DEPTH_LEVELS);

    // Apply price grouping if set
    const groupSize = priceGrouping();
    if (groupSize > 0) {
      bids = groupLevels(bids, groupSize, true);
      asks = groupLevels(asks, groupSize, false);
    }

    // Calculate cumulative totals
    let bidTotal = 0;
    for (const bid of bids) {
      bidTotal += bid.size;
      bid.total = bidTotal;
    }

    let askTotal = 0;
    for (const ask of asks) {
      askTotal += ask.size;
      ask.total = askTotal;
    }

    // Calculate percentages for depth visualization
    const maxTotal = Math.max(bidTotal, askTotal);
    for (const bid of bids) {
      bid.percentage = maxTotal > 0 ? (bid.total / maxTotal) * 100 : 0;
    }
    for (const ask of asks) {
      ask.percentage = maxTotal > 0 ? (ask.total / maxTotal) * 100 : 0;
    }

    // Calculate spread
    const bestBid = bids[0]?.price ?? 0;
    const bestAsk = asks[0]?.price ?? 0;
    const spread = bestAsk > 0 && bestBid > 0 ? bestAsk - bestBid : 0;
    const midPrice =
      bestBid > 0 && bestAsk > 0 ? (bestBid + bestAsk) / 2 : 0;

    return { bids, asks, spread, midPrice };
  });

  // Format price with appropriate decimals
  const formatPrice = (price: number): string => {
    if (price >= 1000) return price.toFixed(2);
    if (price >= 1) return price.toFixed(4);
    return price.toFixed(6);
  };

  // Format size with appropriate decimals
  const formatSize = (size: number): string => {
    if (size >= 1000) return size.toFixed(2);
    if (size >= 1) return size.toFixed(4);
    return size.toFixed(6);
  };

  // Status info when no data
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

    return { message: "Waiting for data...", color: "text-muted-foreground" };
  });

  // Check if we have any data
  const hasData = createMemo(() => {
    const data = processedData();
    return data.bids.length > 0 || data.asks.length > 0;
  });

  return (
    <div class="flex h-full flex-col bg-card contain-content">
      {/* Header with grouping control */}
      <div class="flex items-center justify-between border-b border-border px-3 py-2">
        <h2 class="text-sm font-semibold">Order Book</h2>
        <select
          class="bg-muted/50 text-xs px-2 py-1 rounded border border-border outline-none"
          value={priceGrouping()}
          onChange={(e) => {
            const val = parseFloat(e.target.value);
            setPriceGrouping(Number.isNaN(val) ? 0 : val);
          }}
        >
          <For each={GROUPING_OPTIONS}>
            {(opt) => <option value={opt.value}>{opt.label}</option>}
          </For>
        </select>
      </div>

      {/* Column headers */}
      <div class="flex border-b border-border px-3 py-1 text-xs text-muted-foreground">
        <div class="flex-1 text-left">Price</div>
        <div class="flex-1 text-right">Size</div>
        <div class="flex-1 text-right">Total</div>
      </div>

      {/* Empty state when no data */}
      <Show when={!hasData()}>
        <div class="flex-1 flex items-center justify-center">
          <span class={cn("text-sm", statusInfo().color)}>
            {statusInfo().message}
          </span>
        </div>
      </Show>

      {/* Asks (sell orders) - reversed so lowest is at bottom */}
      <Show when={hasData()}>
      <div class="flex-1 overflow-hidden">
        <div class="flex h-[calc(50%-16px)] flex-col-reverse overflow-y-auto scrollbar-hide">
          <For each={processedData().asks}>
            {(ask, index) => (
              <div
                class={cn(
                  "relative flex px-3 py-0.5 text-xs font-mono cursor-pointer transition-colors",
                  index() === 0 && "bg-ask/10",
                  hoveredRow()?.side === "ask" &&
                    hoveredRow()?.index === index() &&
                    "bg-muted/50"
                )}
                onMouseEnter={() => setHoveredRow({ side: "ask", index: index() })}
                onMouseLeave={() => setHoveredRow(null)}
              >
                {/* Depth bar with gradient */}
                <div
                  class="absolute inset-y-0 right-0 bg-gradient-to-l from-ask/30 to-ask/10 transition-all duration-200"
                  style={{ width: `${ask.percentage}%` }}
                />
                {/* Content */}
                <div class="relative flex w-full">
                  <div class="flex-1 text-left text-ask">
                    {formatPrice(ask.price)}
                  </div>
                  <div class="flex-1 text-right">{formatSize(ask.size)}</div>
                  <div class="flex-1 text-right text-muted-foreground">
                    {formatSize(ask.total)}
                  </div>
                </div>
              </div>
            )}
          </For>
        </div>

        {/* Compact spread indicator */}
        <div class="flex items-center justify-center border-y border-border bg-muted/20 py-1">
          <Show when={processedData().spread > 0}>
            <span class="text-xs text-muted-foreground font-mono">
              Spread: {formatPrice(processedData().spread)}
            </span>
          </Show>
          <Show when={processedData().spread === 0}>
            <span class="text-xs text-muted-foreground">--</span>
          </Show>
        </div>

        {/* Bids (buy orders) */}
        <div class="flex h-[calc(50%-16px)] flex-col overflow-y-auto scrollbar-hide">
          <For each={processedData().bids}>
            {(bid, index) => (
              <div
                class={cn(
                  "relative flex px-3 py-0.5 text-xs font-mono cursor-pointer transition-colors",
                  index() === 0 && "bg-bid/10",
                  hoveredRow()?.side === "bid" &&
                    hoveredRow()?.index === index() &&
                    "bg-muted/50"
                )}
                onMouseEnter={() => setHoveredRow({ side: "bid", index: index() })}
                onMouseLeave={() => setHoveredRow(null)}
              >
                {/* Depth bar with gradient */}
                <div
                  class="absolute inset-y-0 right-0 bg-gradient-to-l from-bid/30 to-bid/10 transition-all duration-200"
                  style={{ width: `${bid.percentage}%` }}
                />
                {/* Content */}
                <div class="relative flex w-full">
                  <div class="flex-1 text-left text-bid">
                    {formatPrice(bid.price)}
                  </div>
                  <div class="flex-1 text-right">{formatSize(bid.size)}</div>
                  <div class="flex-1 text-right text-muted-foreground">
                    {formatSize(bid.total)}
                  </div>
                </div>
              </div>
            )}
          </For>
        </div>
      </div>
      </Show>
    </div>
  );
};
