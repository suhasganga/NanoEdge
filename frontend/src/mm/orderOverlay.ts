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

import {
  createSeriesMarkers,
  type ISeriesApi,
  type IPriceLine,
  type CreatePriceLineOptions,
  type SeriesType,
  type SeriesMarker,
  type Time,
  type UTCTimestamp,
  type ISeriesMarkersPluginApi,
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

// Color constants - Brighter colors for better visibility
const COLORS = {
  buyOrder: "#00C853", // Bright green for buy orders (was #26a69a)
  sellOrder: "#FF5252", // Bright red for sell orders (was #ef5350)
  longPosition: "#2979FF", // Bright blue for long position
  shortPosition: "#E040FB", // Bright purple for short position
  fillBuy: "#00E676", // Even brighter green for fill markers
  fillSell: "#FF1744", // Even brighter red for fill markers
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

  // Fill markers on chart (v5.x uses plugin system)
  private fillMarkers: SeriesMarker<Time>[] = [];
  private markersPlugin: ISeriesMarkersPluginApi<Time> | null = null;

  // Optional time transform function (for timezone support)
  private timeTransform: ((utcTime: number) => number) | null = null;

  // Dynamic price precision (set from chart based on asset price magnitude)
  private pricePrecision: number = 2;

  constructor(series: ISeriesApi<SeriesType>) {
    this.series = series;
    // Initialize markers plugin (v5.x API)
    this.markersPlugin = createSeriesMarkers(series, []);
  }

  /**
   * Set price precision for formatting labels (called by Chart.tsx when data loads)
   */
  setPricePrecision(precision: number): void {
    this.pricePrecision = precision;
  }

  /** Format a price using current precision */
  private fmtPrice(price: number): string {
    return price.toFixed(this.pricePrecision);
  }

  /**
   * Set time transform function (for timezone conversion)
   */
  setTimeTransform(transform: (utcTime: number) => number): void {
    this.timeTransform = transform;
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
      lineWidth: 2, // Thicker for visibility (was 1)
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
      return;
    }

    const color = quantity > 0 ? COLORS.longPosition : COLORS.shortPosition;
    const side = quantity > 0 ? "LONG" : "SHORT";
    const absQty = Math.abs(quantity);
    const qtyDisplay =
      absQty >= 1 ? absQty.toFixed(2) : absQty.toPrecision(4);

    const lineOptions: CreatePriceLineOptions = {
      price: avgPrice,
      color: color,
      lineWidth: 3, // Even thicker for position (was 2)
      lineStyle: LineStyle.Solid, // Solid line for position (was Dotted)
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
   * Sync fill markers on chart
   * Shows buy/sell arrows where orders were filled
   */
  syncFills(fills: OrderFill[]): void {
    // Keep last 50 markers to avoid clutter
    const recentFills = fills.slice(-50);

    // Sort by timestamp ascending (REQUIRED by TradingView Lightweight Charts)
    const sortedFills = [...recentFills].sort((a, b) => a.timestamp - b.timestamp);

    this.fillMarkers = sortedFills.map((fill) => {
      // Convert fill timestamp to chart time
      // Backend sends timestamp in ms, convert to seconds for chart
      let time = fill.timestamp > 1e12 ? Math.floor(fill.timestamp / 1000) : fill.timestamp;

      // Floor to 1-minute candle period for proper alignment with chart bars
      time = Math.floor(time / 60) * 60;

      // Apply time transform if set (for timezone support)
      if (this.timeTransform) {
        time = this.timeTransform(time);
      }

      return {
        time: time as UTCTimestamp,
        position: fill.side === "buy" ? "belowBar" : "aboveBar",
        color: fill.side === "buy" ? COLORS.fillBuy : COLORS.fillSell,
        shape: fill.side === "buy" ? "arrowUp" : "arrowDown",
        text: `${fill.side.toUpperCase()} ${fill.quantity.toFixed(4)} @ ${this.fmtPrice(fill.price)}`,
        size: 2, // Larger markers for visibility
      } as SeriesMarker<Time>;
    });

    try {
      // Use markers plugin API (v5.x)
      if (this.markersPlugin) {
        this.markersPlugin.setMarkers(this.fillMarkers);
      }
    } catch (e) {
      console.error("[OrderOverlay] Failed to set fill markers:", e);
    }
  }

  /**
   * Add a single fill marker
   */
  addFillMarker(fill: OrderFill): void {
    let time = fill.timestamp > 1e12 ? Math.floor(fill.timestamp / 1000) : fill.timestamp;

    // Floor to 1-minute candle period for proper alignment
    time = Math.floor(time / 60) * 60;

    if (this.timeTransform) {
      time = this.timeTransform(time);
    }

    this.fillMarkers.push({
      time: time as UTCTimestamp,
      position: fill.side === "buy" ? "belowBar" : "aboveBar",
      color: fill.side === "buy" ? COLORS.fillBuy : COLORS.fillSell,
      shape: fill.side === "buy" ? "arrowUp" : "arrowDown",
      text: `${fill.side.toUpperCase()} ${fill.quantity.toFixed(4)} @ ${this.fmtPrice(fill.price)}`,
      size: 2, // Larger markers for visibility
    } as SeriesMarker<Time>);

    // Keep only last 50 markers
    if (this.fillMarkers.length > 50) {
      this.fillMarkers = this.fillMarkers.slice(-50);
    }

    // Sort markers by time (required by TradingView)
    this.fillMarkers.sort((a, b) => (a.time as number) - (b.time as number));

    try {
      if (this.markersPlugin) {
        this.markersPlugin.setMarkers(this.fillMarkers);
      }
    } catch (e) {
      console.error("[OrderOverlay] Failed to add fill marker:", e);
    }
  }

  /**
   * Clear fill markers
   */
  clearFillMarkers(): void {
    this.fillMarkers = [];
    try {
      if (this.markersPlugin) {
        this.markersPlugin.setMarkers([]);
      }
    } catch (e) {
      // Series may be removed
    }
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

    // Clear fill markers
    this.clearFillMarkers();
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

    // Store fill markers
    const savedMarkers = [...this.fillMarkers];

    // Clear from old series (but keep markers in memory)
    for (const orderId of this.orderLines.keys()) {
      this.removeOrderLine(orderId);
    }
    this.setPositionLine(null, 0);

    // Detach old markers plugin
    if (this.markersPlugin) {
      try {
        this.markersPlugin.detach();
      } catch (e) {
        // Plugin may already be detached
      }
      this.markersPlugin = null;
    }

    // Update series reference
    this.series = series;

    // Create new markers plugin for new series
    this.markersPlugin = createSeriesMarkers(series, []);

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

    // Restore fill markers on new series
    this.fillMarkers = savedMarkers;
    if (this.fillMarkers.length > 0 && this.markersPlugin) {
      try {
        this.markersPlugin.setMarkers(this.fillMarkers);
      } catch (e) {
        console.error("[OrderOverlay] Failed to restore fill markers:", e);
      }
    }
  }
}
