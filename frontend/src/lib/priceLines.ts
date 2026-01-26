import type {
  ISeriesApi,
  IPriceLine,
  CreatePriceLineOptions,
  SeriesType,
} from "lightweight-charts";

/**
 * PriceLineManager
 *
 * Manages price lines on a TradingView Lightweight Charts series.
 * Provides methods for creating, updating, and removing price lines
 * for various purposes (current price, prev day close, high/low, bid/ask).
 *
 * Reference: downloaded_docs/lightweight-charts/tutorials/how_to/price-line.md
 */

// Line style constants (from LWC docs)
export const LineStyle = {
  Solid: 0,
  Dotted: 1,
  Dashed: 2,
  LargeDashed: 3,
  SparseDotted: 4,
} as const;

export type LineStyle = (typeof LineStyle)[keyof typeof LineStyle];

// Price line configurations matching TradingView style
export const PRICE_LINE_CONFIGS = {
  currentPrice: {
    color: "#2962FF", // TradingView blue
    lineWidth: 1,
    lineStyle: LineStyle.Solid,
    axisLabelVisible: true,
    title: "",
  },
  prevDayClose: {
    color: "#787B86", // TradingView gray
    lineWidth: 1,
    lineStyle: LineStyle.Dashed,
    axisLabelVisible: true,
    title: "Prev Close",
  },
  high: {
    color: "#26a69a", // Green
    lineWidth: 1,
    lineStyle: LineStyle.Dotted,
    axisLabelVisible: true,
    title: "High",
  },
  low: {
    color: "#ef5350", // Red
    lineWidth: 1,
    lineStyle: LineStyle.Dotted,
    axisLabelVisible: true,
    title: "Low",
  },
  bid: {
    color: "#3fb950", // Bid green
    lineWidth: 1,
    lineStyle: LineStyle.Solid,
    axisLabelVisible: true,
    title: "Bid",
  },
  ask: {
    color: "#f85149", // Ask red
    lineWidth: 1,
    lineStyle: LineStyle.Solid,
    axisLabelVisible: true,
    title: "Ask",
  },
} as const;

export type PriceLineType = keyof typeof PRICE_LINE_CONFIGS;

export class PriceLineManager {
  private series: ISeriesApi<SeriesType>;
  private lines: Map<string, IPriceLine> = new Map();

  constructor(series: ISeriesApi<SeriesType>) {
    this.series = series;
  }

  /**
   * Set or update a price line
   *
   * @param id - Unique identifier for the line
   * @param options - Price line options
   */
  setLine(id: string, options: CreatePriceLineOptions): void {
    // Remove existing line if present
    this.removeLine(id);

    // Create new line
    const line = this.series.createPriceLine(options);
    this.lines.set(id, line);
  }

  /**
   * Remove a price line by ID
   *
   * @param id - Unique identifier for the line
   */
  removeLine(id: string): void {
    const existing = this.lines.get(id);
    if (existing) {
      this.series.removePriceLine(existing);
      this.lines.delete(id);
    }
  }

  /**
   * Update a line's price (for real-time updates)
   *
   * @param id - Unique identifier for the line
   * @param price - New price value
   */
  updateLinePrice(id: string, price: number): void {
    const line = this.lines.get(id);
    if (line) {
      line.applyOptions({ price });
    }
  }

  /**
   * Check if a line exists
   *
   * @param id - Unique identifier for the line
   */
  hasLine(id: string): boolean {
    return this.lines.has(id);
  }

  /**
   * Set current price line (tracks last traded price)
   */
  setCurrentPriceLine(visible: boolean, price?: number): void {
    if (!visible) {
      this.removeLine("currentPrice");
      return;
    }

    if (price !== undefined) {
      this.setLine("currentPrice", {
        price,
        ...PRICE_LINE_CONFIGS.currentPrice,
      });
    }
  }

  /**
   * Update current price (called on each tick)
   */
  updateCurrentPrice(price: number): void {
    if (this.hasLine("currentPrice")) {
      this.updateLinePrice("currentPrice", price);
    }
  }

  /**
   * Set previous day close line
   */
  setPrevDayCloseLine(visible: boolean, price?: number): void {
    if (!visible) {
      this.removeLine("prevDayClose");
      return;
    }

    if (price !== undefined) {
      this.setLine("prevDayClose", {
        price,
        ...PRICE_LINE_CONFIGS.prevDayClose,
      });
    }
  }

  /**
   * Set high/low lines for the day
   */
  setHighLowLines(visible: boolean, high?: number, low?: number): void {
    if (!visible) {
      this.removeLine("high");
      this.removeLine("low");
      return;
    }

    if (high !== undefined) {
      this.setLine("high", {
        price: high,
        ...PRICE_LINE_CONFIGS.high,
      });
    }

    if (low !== undefined) {
      this.setLine("low", {
        price: low,
        ...PRICE_LINE_CONFIGS.low,
      });
    }
  }

  /**
   * Update high/low values
   */
  updateHighLow(high: number, low: number): void {
    if (this.hasLine("high")) {
      this.updateLinePrice("high", high);
    }
    if (this.hasLine("low")) {
      this.updateLinePrice("low", low);
    }
  }

  /**
   * Set bid/ask lines (from order book)
   */
  setBidAskLines(visible: boolean, bid?: number, ask?: number): void {
    if (!visible) {
      this.removeLine("bid");
      this.removeLine("ask");
      return;
    }

    if (bid !== undefined) {
      this.setLine("bid", {
        price: bid,
        ...PRICE_LINE_CONFIGS.bid,
      });
    }

    if (ask !== undefined) {
      this.setLine("ask", {
        price: ask,
        ...PRICE_LINE_CONFIGS.ask,
      });
    }
  }

  /**
   * Update bid/ask prices (called frequently from order book updates)
   */
  updateBidAsk(bid: number, ask: number): void {
    if (this.hasLine("bid")) {
      this.updateLinePrice("bid", bid);
    }
    if (this.hasLine("ask")) {
      this.updateLinePrice("ask", ask);
    }
  }

  /**
   * Create a custom price line
   */
  createCustomLine(
    id: string,
    price: number,
    options: Partial<CreatePriceLineOptions> = {}
  ): void {
    this.setLine(id, {
      price,
      color: "#787B86",
      lineWidth: 1,
      lineStyle: LineStyle.Dashed,
      axisLabelVisible: true,
      title: "",
      ...options,
    });
  }

  /**
   * Remove all price lines
   */
  removeAll(): void {
    for (const [id] of this.lines) {
      this.removeLine(id);
    }
  }

  /**
   * Get all line IDs
   */
  getLineIds(): string[] {
    return Array.from(this.lines.keys());
  }

  /**
   * Update the series reference (needed when chart type changes)
   */
  updateSeries(series: ISeriesApi<SeriesType>): void {
    // Store current line configurations
    const lineConfigs: Array<{ id: string; options: CreatePriceLineOptions }> = [];

    for (const [id, line] of this.lines) {
      // Get options from existing line (approximation - we don't have direct access)
      // This is a limitation - in practice, we'd need to track options separately
      lineConfigs.push({
        id,
        options: line.options() as CreatePriceLineOptions,
      });
    }

    // Clear all lines from old series
    this.removeAll();

    // Update series reference
    this.series = series;

    // Recreate lines on new series
    for (const { id, options } of lineConfigs) {
      this.setLine(id, options);
    }
  }
}
