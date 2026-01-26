/**
 * OrderOverlayManager - Manages order visualization on TradingView chart.
 *
 * Shows:
 * - Open orders as horizontal price lines (green=buy, red=sell)
 * - Position average entry price line
 * - Fill markers on the chart
 *
 * Following the pattern of frontend/src/lib/priceLines.ts
 */

import type {
  ISeriesApi,
  IPriceLine,
  CreatePriceLineOptions,
  SeriesType,
} from "lightweight-charts";
import type { SimulatedOrder, SimulatedPosition, OrderFill } from "./types";

// Line style constants (matching priceLines.ts)
export const LineStyle = {
  Solid: 0,
  Dotted: 1,
  Dashed: 2,
  LargeDashed: 3,
  SparseDotted: 4,
} as const;

// Color constants
const COLORS = {
  buyOrder: "#26a69a", // Green for buy orders
  sellOrder: "#ef5350", // Red for sell orders
  longPosition: "#2962FF", // Blue for long position
  shortPosition: "#9c27b0", // Purple for short position
  fillBuy: "#26a69a",
  fillSell: "#ef5350",
} as const;

interface OrderLineConfig {
  orderId: string;
  price: number;
  side: "buy" | "sell";
  quantity: number;
  filledQuantity: number;
  status: string;
  tag: string;
}

export class OrderOverlayManager {
  private series: ISeriesApi<SeriesType>;

  // Price lines for open orders (order_id -> IPriceLine)
  private orderLines: Map<string, IPriceLine> = new Map();

  // Position average entry line
  private positionLine: IPriceLine | null = null;

  // Track current position state for updates
  private currentPositionQty: number = 0;

  constructor(series: ISeriesApi<SeriesType>) {
    this.series = series;
  }

  /**
   * Set or update an order line on the chart
   */
  setOrderLine(order: OrderLineConfig): void {
    // Remove existing line for this order
    this.removeOrderLine(order.orderId);

    // Only show open or partially filled orders
    if (order.status !== "open" && order.status !== "partially_filled") {
      return;
    }

    const color = order.side === "buy" ? COLORS.buyOrder : COLORS.sellOrder;

    // Calculate fill percentage for title
    const fillPct =
      order.quantity > 0
        ? ((order.filledQuantity / order.quantity) * 100).toFixed(0)
        : "0";

    // Format quantity for display
    const qtyDisplay =
      order.quantity >= 1
        ? order.quantity.toFixed(2)
        : order.quantity.toPrecision(4);

    // Build title: "BUY 0.1 [grid]" or "SELL 0.1 (50%)"
    let title = `${order.side.toUpperCase()} ${qtyDisplay}`;
    if (order.tag) {
      title += ` [${order.tag}]`;
    }
    if (order.filledQuantity > 0) {
      title += ` (${fillPct}%)`;
    }

    const lineOptions: CreatePriceLineOptions = {
      price: order.price,
      color: color,
      lineWidth: 1,
      lineStyle: LineStyle.Dashed,
      axisLabelVisible: true,
      title: title,
    };

    try {
      const line = this.series.createPriceLine(lineOptions);
      this.orderLines.set(order.orderId, line);
    } catch (e) {
      console.error("[OrderOverlay] Failed to create order line:", e);
    }
  }

  /**
   * Remove an order line from the chart
   */
  removeOrderLine(orderId: string): void {
    const line = this.orderLines.get(orderId);
    if (line) {
      try {
        this.series.removePriceLine(line);
      } catch (e) {
        // Line may already be removed
      }
      this.orderLines.delete(orderId);
    }
  }

  /**
   * Update an existing order line's price (for efficiency)
   */
  updateOrderLinePrice(orderId: string, price: number): void {
    const line = this.orderLines.get(orderId);
    if (line) {
      line.applyOptions({ price });
    }
  }

  /**
   * Set position average entry price line
   */
  setPositionLine(avgPrice: number | null, quantity: number): void {
    // Remove existing position line
    if (this.positionLine) {
      try {
        this.series.removePriceLine(this.positionLine);
      } catch (e) {
        // Line may already be removed
      }
      this.positionLine = null;
    }

    // Don't show line if no position or zero quantity
    if (avgPrice === null || avgPrice === 0 || quantity === 0) {
      this.currentPositionQty = 0;
      return;
    }

    this.currentPositionQty = quantity;

    const color = quantity > 0 ? COLORS.longPosition : COLORS.shortPosition;
    const side = quantity > 0 ? "LONG" : "SHORT";
    const absQty = Math.abs(quantity);
    const qtyDisplay =
      absQty >= 1 ? absQty.toFixed(2) : absQty.toPrecision(4);

    const lineOptions: CreatePriceLineOptions = {
      price: avgPrice,
      color: color,
      lineWidth: 2,
      lineStyle: LineStyle.Dotted,
      axisLabelVisible: true,
      title: `${side} ${qtyDisplay}`,
    };

    try {
      this.positionLine = this.series.createPriceLine(lineOptions);
    } catch (e) {
      console.error("[OrderOverlay] Failed to create position line:", e);
    }
  }

  /**
   * Update position line price (for real-time P&L tracking)
   */
  updatePositionLinePrice(avgPrice: number): void {
    if (this.positionLine && avgPrice > 0) {
      this.positionLine.applyOptions({ price: avgPrice });
    }
  }

  /**
   * Sync all orders at once (bulk update)
   * More efficient than individual updates for large order sets
   */
  syncOrders(orders: SimulatedOrder[]): void {
    // Get IDs of orders that should be displayed
    const activeIds = new Set(
      orders
        .filter((o) => o.status === "open" || o.status === "partially_filled")
        .map((o) => o.order_id)
    );

    // Remove lines for orders no longer active
    for (const orderId of this.orderLines.keys()) {
      if (!activeIds.has(orderId)) {
        this.removeOrderLine(orderId);
      }
    }

    // Add/update lines for active orders
    for (const order of orders) {
      if (order.status === "open" || order.status === "partially_filled") {
        this.setOrderLine({
          orderId: order.order_id,
          price: order.price,
          side: order.side,
          quantity: order.quantity,
          filledQuantity: order.filled_quantity,
          status: order.status,
          tag: order.tag,
        });
      }
    }
  }

  /**
   * Sync position from position update
   */
  syncPosition(position: SimulatedPosition | null): void {
    if (!position || position.quantity === 0) {
      this.setPositionLine(null, 0);
    } else {
      this.setPositionLine(position.avg_entry_price, position.quantity);
    }
  }

  /**
   * Get count of displayed order lines
   */
  getOrderLineCount(): number {
    return this.orderLines.size;
  }

  /**
   * Check if position line is displayed
   */
  hasPositionLine(): boolean {
    return this.positionLine !== null;
  }

  /**
   * Clear all overlays
   */
  clear(): void {
    // Remove all order lines
    for (const orderId of this.orderLines.keys()) {
      this.removeOrderLine(orderId);
    }

    // Remove position line
    this.setPositionLine(null, 0);
  }

  /**
   * Update series reference (when chart type changes)
   * Recreates all lines on new series
   */
  updateSeries(series: ISeriesApi<SeriesType>): void {
    // Store current state
    const currentOrders: Array<{
      id: string;
      options: CreatePriceLineOptions;
    }> = [];

    for (const [id, line] of this.orderLines) {
      try {
        currentOrders.push({
          id,
          options: line.options() as CreatePriceLineOptions,
        });
      } catch (e) {
        // Line may be invalid
      }
    }

    const hadPositionLine = this.positionLine !== null;
    let positionOptions: CreatePriceLineOptions | null = null;
    if (this.positionLine) {
      try {
        positionOptions = this.positionLine.options() as CreatePriceLineOptions;
      } catch (e) {
        // Line may be invalid
      }
    }

    // Clear from old series
    this.clear();

    // Update series reference
    this.series = series;

    // Recreate order lines on new series
    for (const { id, options } of currentOrders) {
      try {
        const line = this.series.createPriceLine(options);
        this.orderLines.set(id, line);
      } catch (e) {
        console.error("[OrderOverlay] Failed to recreate order line:", e);
      }
    }

    // Recreate position line on new series
    if (hadPositionLine && positionOptions) {
      try {
        this.positionLine = this.series.createPriceLine(positionOptions);
      } catch (e) {
        console.error("[OrderOverlay] Failed to recreate position line:", e);
      }
    }
  }
}
