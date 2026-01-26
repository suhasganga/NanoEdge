/**
 * MyOrders - Order management panel for market making.
 *
 * Features:
 * - Order entry form (side, price, quantity)
 * - Position display with P&L
 * - Open orders list with cancel buttons
 * - Grid order placement
 */

import { Component, createSignal, For, Show } from "solid-js";
import { orderStore } from "./orderStore";
import { useOrdersWebSocket } from "./useOrdersWebSocket";
import type { SimulatedOrder, GridOrderConfig } from "./types";

// API client for order operations
const API_BASE = "/api/mm";

async function placeOrder(
  symbol: string,
  side: "buy" | "sell",
  price: number,
  quantity: number,
  tag: string = ""
) {
  const params = new URLSearchParams({
    symbol,
    side,
    price: price.toString(),
    quantity: quantity.toString(),
    tag,
  });

  const response = await fetch(`${API_BASE}/orders?${params}`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error(`Failed to place order: ${response.statusText}`);
  }

  return response.json();
}

async function cancelOrder(orderId: string) {
  const response = await fetch(`${API_BASE}/orders/${orderId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error(`Failed to cancel order: ${response.statusText}`);
  }

  return response.json();
}

async function cancelAllOrders(symbol?: string, side?: "buy" | "sell", tag?: string) {
  const params = new URLSearchParams();
  if (symbol) params.set("symbol", symbol);
  if (side) params.set("side", side);
  if (tag) params.set("tag", tag);

  const response = await fetch(`${API_BASE}/orders?${params}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error(`Failed to cancel orders: ${response.statusText}`);
  }

  return response.json();
}

async function placeGridOrders(config: GridOrderConfig) {
  const params = new URLSearchParams({
    symbol: config.symbol,
    base_price: config.base_price.toString(),
    spread: config.spread.toString(),
    levels: (config.levels ?? 5).toString(),
    base_quantity: (config.base_quantity ?? 1).toString(),
    quantity_scale: (config.quantity_scale ?? 1).toString(),
    side: config.side ?? "both",
    tag: config.tag ?? "grid",
  });

  const response = await fetch(`${API_BASE}/grid?${params}`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error(`Failed to place grid orders: ${response.statusText}`);
  }

  return response.json();
}

async function resetSimulator(symbol: string) {
  const response = await fetch(`${API_BASE}/reset/${symbol}`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error(`Failed to reset simulator: ${response.statusText}`);
  }

  return response.json();
}

// Utility for class names
const cn = (...classes: (string | boolean | undefined)[]) =>
  classes.filter(Boolean).join(" ");

interface MyOrdersProps {
  symbol: string;
}

export const MyOrders: Component<MyOrdersProps> = (props) => {
  // WebSocket connection
  const { isConnected } = useOrdersWebSocket({
    symbol: () => props.symbol,
  });

  // Order entry state
  const [side, setSide] = createSignal<"buy" | "sell">("buy");
  const [price, setPrice] = createSignal("");
  const [quantity, setQuantity] = createSignal("");
  const [tag, setTag] = createSignal("");
  const [isSubmitting, setIsSubmitting] = createSignal(false);
  const [error, setError] = createSignal<string | null>(null);

  // Grid order state
  const [showGrid, setShowGrid] = createSignal(false);
  const [gridSpread, setGridSpread] = createSignal("100");
  const [gridLevels, setGridLevels] = createSignal("5");
  const [gridQty, setGridQty] = createSignal("0.1");
  const [gridScale, setGridScale] = createSignal("1");

  const handleSubmitOrder = async (e: Event) => {
    e.preventDefault();
    setError(null);

    const priceVal = parseFloat(price());
    const qtyVal = parseFloat(quantity());

    if (isNaN(priceVal) || priceVal <= 0) {
      setError("Invalid price");
      return;
    }
    if (isNaN(qtyVal) || qtyVal <= 0) {
      setError("Invalid quantity");
      return;
    }

    setIsSubmitting(true);
    try {
      await placeOrder(props.symbol, side(), priceVal, qtyVal, tag());
      // Clear form on success
      setPrice("");
      setQuantity("");
      setTag("");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to place order");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleCancelOrder = async (orderId: string) => {
    try {
      await cancelOrder(orderId);
    } catch (err) {
      console.error("Failed to cancel order:", err);
    }
  };

  const handleCancelAll = async () => {
    try {
      await cancelAllOrders(props.symbol);
    } catch (err) {
      console.error("Failed to cancel all orders:", err);
    }
  };

  const handlePlaceGrid = async () => {
    const pos = orderStore.position();
    const lastPrice = pos?.avg_entry_price || 0;

    // Use last price or a default
    const basePrice = lastPrice > 0 ? lastPrice : parseFloat(price()) || 0;
    if (basePrice <= 0) {
      setError("Enter a price first or have a position");
      return;
    }

    setIsSubmitting(true);
    try {
      await placeGridOrders({
        symbol: props.symbol,
        base_price: basePrice,
        spread: parseFloat(gridSpread()) || 100,
        levels: parseInt(gridLevels()) || 5,
        base_quantity: parseFloat(gridQty()) || 0.1,
        quantity_scale: parseFloat(gridScale()) || 1,
        side: "both",
        tag: "grid",
      });
      setShowGrid(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to place grid");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleReset = async () => {
    try {
      await resetSimulator(props.symbol);
    } catch (err) {
      console.error("Failed to reset simulator:", err);
    }
  };

  // Format number for display
  const formatNum = (n: number, decimals = 2) => {
    if (Math.abs(n) >= 1) return n.toFixed(decimals);
    return n.toPrecision(4);
  };

  const formatPnL = (n: number) => {
    const sign = n >= 0 ? "+" : "";
    return `${sign}${formatNum(n)}`;
  };

  return (
    <div class="flex h-full flex-col text-sm">
      {/* Connection status */}
      <div class="flex items-center justify-between border-b border-border px-3 py-2">
        <span class="text-xs text-muted-foreground">
          {props.symbol} Orders
        </span>
        <div class="flex items-center gap-2">
          <span
            class={cn(
              "h-2 w-2 rounded-full",
              isConnected() ? "bg-green-500" : "bg-red-500"
            )}
          />
          <span class="text-xs text-muted-foreground">
            {isConnected() ? "Connected" : "Disconnected"}
          </span>
        </div>
      </div>

      {/* Order Entry Form */}
      <form onSubmit={handleSubmitOrder} class="border-b border-border p-3">
        {/* Side toggle */}
        <div class="mb-2 flex gap-1">
          <button
            type="button"
            class={cn(
              "flex-1 rounded py-1 text-xs font-medium transition-colors",
              side() === "buy"
                ? "bg-green-600 text-white"
                : "bg-muted text-muted-foreground hover:bg-muted/80"
            )}
            onClick={() => setSide("buy")}
          >
            Buy
          </button>
          <button
            type="button"
            class={cn(
              "flex-1 rounded py-1 text-xs font-medium transition-colors",
              side() === "sell"
                ? "bg-red-600 text-white"
                : "bg-muted text-muted-foreground hover:bg-muted/80"
            )}
            onClick={() => setSide("sell")}
          >
            Sell
          </button>
        </div>

        {/* Price & Quantity */}
        <div class="mb-2 grid grid-cols-2 gap-2">
          <input
            type="text"
            placeholder="Price"
            value={price()}
            onInput={(e) => setPrice(e.currentTarget.value)}
            class="rounded border border-border bg-background px-2 py-1 text-xs focus:border-primary focus:outline-none"
          />
          <input
            type="text"
            placeholder="Quantity"
            value={quantity()}
            onInput={(e) => setQuantity(e.currentTarget.value)}
            class="rounded border border-border bg-background px-2 py-1 text-xs focus:border-primary focus:outline-none"
          />
        </div>

        {/* Tag (optional) */}
        <input
          type="text"
          placeholder="Tag (optional)"
          value={tag()}
          onInput={(e) => setTag(e.currentTarget.value)}
          class="mb-2 w-full rounded border border-border bg-background px-2 py-1 text-xs focus:border-primary focus:outline-none"
        />

        {/* Error message */}
        <Show when={error()}>
          <div class="mb-2 text-xs text-red-500">{error()}</div>
        </Show>

        {/* Submit button */}
        <button
          type="submit"
          disabled={isSubmitting()}
          class={cn(
            "w-full rounded py-1.5 text-xs font-medium text-white transition-colors",
            side() === "buy"
              ? "bg-green-600 hover:bg-green-700"
              : "bg-red-600 hover:bg-red-700",
            isSubmitting() && "opacity-50 cursor-not-allowed"
          )}
        >
          {isSubmitting() ? "Placing..." : `Place ${side().toUpperCase()} Order`}
        </button>

        {/* Grid & Cancel buttons */}
        <div class="mt-2 flex gap-1">
          <button
            type="button"
            onClick={() => setShowGrid(!showGrid())}
            class="flex-1 rounded bg-muted py-1 text-xs text-muted-foreground hover:bg-muted/80"
          >
            {showGrid() ? "Hide Grid" : "Grid Orders"}
          </button>
          <button
            type="button"
            onClick={handleCancelAll}
            class="flex-1 rounded bg-muted py-1 text-xs text-muted-foreground hover:bg-muted/80"
          >
            Cancel All
          </button>
          <button
            type="button"
            onClick={handleReset}
            class="rounded bg-muted px-2 py-1 text-xs text-muted-foreground hover:bg-muted/80"
            title="Reset simulator"
          >
            Reset
          </button>
        </div>

        {/* Grid order form */}
        <Show when={showGrid()}>
          <div class="mt-2 rounded border border-border p-2">
            <div class="mb-1 text-xs font-medium">Grid Orders</div>
            <div class="grid grid-cols-2 gap-1">
              <input
                type="text"
                placeholder="Spread"
                value={gridSpread()}
                onInput={(e) => setGridSpread(e.currentTarget.value)}
                class="rounded border border-border bg-background px-1.5 py-0.5 text-xs"
              />
              <input
                type="text"
                placeholder="Levels"
                value={gridLevels()}
                onInput={(e) => setGridLevels(e.currentTarget.value)}
                class="rounded border border-border bg-background px-1.5 py-0.5 text-xs"
              />
              <input
                type="text"
                placeholder="Quantity"
                value={gridQty()}
                onInput={(e) => setGridQty(e.currentTarget.value)}
                class="rounded border border-border bg-background px-1.5 py-0.5 text-xs"
              />
              <input
                type="text"
                placeholder="Scale"
                value={gridScale()}
                onInput={(e) => setGridScale(e.currentTarget.value)}
                class="rounded border border-border bg-background px-1.5 py-0.5 text-xs"
              />
            </div>
            <button
              type="button"
              onClick={handlePlaceGrid}
              disabled={isSubmitting()}
              class="mt-1 w-full rounded bg-blue-600 py-1 text-xs text-white hover:bg-blue-700"
            >
              Place Grid
            </button>
          </div>
        </Show>
      </form>

      {/* Position Display */}
      <Show when={orderStore.position()}>
        {(pos) => (
          <div class="border-b border-border p-3">
            <div class="mb-1 text-xs font-medium text-muted-foreground">
              Position
            </div>
            <div class="flex items-center justify-between">
              <span
                class={cn(
                  "text-sm font-medium",
                  pos().quantity > 0
                    ? "text-green-500"
                    : pos().quantity < 0
                    ? "text-red-500"
                    : "text-muted-foreground"
                )}
              >
                {pos().quantity > 0 ? "LONG" : pos().quantity < 0 ? "SHORT" : "FLAT"}{" "}
                {formatNum(Math.abs(pos().quantity))}
              </span>
              <span class="text-xs text-muted-foreground">
                @ {formatNum(pos().avg_entry_price)}
              </span>
            </div>
            <div class="mt-1 grid grid-cols-3 gap-2 text-xs">
              <div>
                <span class="text-muted-foreground">Realized:</span>
                <span
                  class={cn(
                    "ml-1",
                    pos().realized_pnl >= 0 ? "text-green-500" : "text-red-500"
                  )}
                >
                  {formatPnL(pos().realized_pnl)}
                </span>
              </div>
              <div>
                <span class="text-muted-foreground">Unrealized:</span>
                <span
                  class={cn(
                    "ml-1",
                    pos().unrealized_pnl >= 0 ? "text-green-500" : "text-red-500"
                  )}
                >
                  {formatPnL(pos().unrealized_pnl)}
                </span>
              </div>
              <div>
                <span class="text-muted-foreground">Total:</span>
                <span
                  class={cn(
                    "ml-1 font-medium",
                    orderStore.getTotalPnL() >= 0
                      ? "text-green-500"
                      : "text-red-500"
                  )}
                >
                  {formatPnL(orderStore.getTotalPnL())}
                </span>
              </div>
            </div>
          </div>
        )}
      </Show>

      {/* Open Orders List */}
      <div class="flex-1 overflow-y-auto">
        <div class="sticky top-0 border-b border-border bg-background px-3 py-1">
          <span class="text-xs font-medium text-muted-foreground">
            Open Orders ({orderStore.orders().length})
          </span>
        </div>

        <Show
          when={orderStore.orders().length > 0}
          fallback={
            <div class="p-3 text-center text-xs text-muted-foreground">
              No open orders
            </div>
          }
        >
          <For each={orderStore.orders()}>
            {(order) => (
              <div class="flex items-center justify-between border-b border-border px-3 py-2 hover:bg-muted/50">
                <div class="flex-1">
                  <div class="flex items-center gap-2">
                    <span
                      class={cn(
                        "text-xs font-medium",
                        order.side === "buy" ? "text-green-500" : "text-red-500"
                      )}
                    >
                      {order.side.toUpperCase()}
                    </span>
                    <span class="text-xs">{formatNum(order.quantity)}</span>
                    <span class="text-xs text-muted-foreground">@</span>
                    <span class="text-xs">{formatNum(order.price)}</span>
                    <Show when={order.tag}>
                      <span class="rounded bg-muted px-1 text-[10px] text-muted-foreground">
                        {order.tag}
                      </span>
                    </Show>
                  </div>
                  <Show when={order.filled_quantity > 0}>
                    <div class="text-[10px] text-muted-foreground">
                      Filled: {formatNum(order.filled_quantity)} /{" "}
                      {formatNum(order.quantity)}
                    </div>
                  </Show>
                </div>
                <button
                  onClick={() => handleCancelOrder(order.order_id)}
                  class="rounded px-2 py-0.5 text-xs text-muted-foreground hover:bg-red-500/20 hover:text-red-500"
                >
                  Cancel
                </button>
              </div>
            )}
          </For>
        </Show>
      </div>
    </div>
  );
};

export default MyOrders;
