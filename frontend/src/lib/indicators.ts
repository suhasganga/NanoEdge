/**
 * IndicatorManager - Handles technical indicators for TradingView Lightweight Charts.
 *
 * Supports dynamic addition/removal of indicators with unique IDs.
 * Multiple instances of the same indicator type can coexist.
 */

import {
  IChartApi,
  ISeriesApi,
  LineSeries,
  LineStyle,
  Time,
} from "lightweight-charts";
import type { IndicatorConfig } from "~/stores/indicatorStore";

interface CandleData {
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume?: number;
}

interface LinePoint {
  time: Time;
  value?: number;
}

interface SMAIndicator {
  id: string;
  series: ISeriesApi<"Line">;
  period: number;
  type: "sma";
  visible: boolean;
  color: string;
}

interface EMAIndicator {
  id: string;
  series: ISeriesApi<"Line">;
  period: number;
  type: "ema";
  visible: boolean;
  color: string;
}

interface BollingerIndicator {
  id: string;
  upper: ISeriesApi<"Line">;
  middle: ISeriesApi<"Line">;
  lower: ISeriesApi<"Line">;
  period: number;
  stdDev: number;
  type: "bollinger";
  visible: boolean;
  color: string;
}

type Indicator = SMAIndicator | EMAIndicator | BollingerIndicator;

export class IndicatorManager {
  private chart: IChartApi;
  private indicators: Map<string, Indicator> = new Map();
  private candleData: CandleData[] = [];

  constructor(chart: IChartApi) {
    this.chart = chart;
  }

  /**
   * Add a dynamic indicator from config
   */
  addDynamicIndicator(config: IndicatorConfig): string {
    // Remove existing indicator with same ID if exists
    if (this.indicators.has(config.id)) {
      this.removeIndicator(config.id);
    }

    switch (config.type) {
      case "sma":
        this.addSMAWithId(config.id, config.period, config.color, config.visible);
        break;
      case "ema":
        this.addEMAWithId(config.id, config.period, config.color, config.visible);
        break;
      case "bollinger":
        this.addBollingerWithId(
          config.id,
          config.period,
          config.params?.stdDev ?? 2,
          config.color,
          config.visible
        );
        break;
    }

    // Calculate data if we have candles
    if (this.candleData.length > 0 && config.visible) {
      this.updateIndicator(config.id);
    }

    return config.id;
  }

  /**
   * Remove an indicator by ID
   */
  removeIndicator(id: string): void {
    const indicator = this.indicators.get(id);
    if (!indicator) return;

    if (indicator.type === "bollinger") {
      this.chart.removeSeries(indicator.upper);
      this.chart.removeSeries(indicator.middle);
      this.chart.removeSeries(indicator.lower);
    } else {
      this.chart.removeSeries(indicator.series);
    }

    this.indicators.delete(id);
  }

  /**
   * Set indicator visibility
   */
  setIndicatorVisibility(id: string, visible: boolean): void {
    const indicator = this.indicators.get(id);
    if (!indicator) return;

    indicator.visible = visible;

    if (indicator.type === "bollinger") {
      indicator.upper.applyOptions({ visible });
      indicator.middle.applyOptions({ visible });
      indicator.lower.applyOptions({ visible });
    } else {
      indicator.series.applyOptions({ visible });
    }

    // If turning on, recalculate
    if (visible && this.candleData.length > 0) {
      this.updateIndicator(id);
    }
  }

  /**
   * Update indicator color
   */
  updateIndicatorColor(id: string, color: string): void {
    const indicator = this.indicators.get(id);
    if (!indicator) return;

    indicator.color = color;

    if (indicator.type === "bollinger") {
      // For Bollinger, update upper/lower with base color, middle stays white/gray
      indicator.upper.applyOptions({ color: `${color}99` }); // 60% opacity
      indicator.lower.applyOptions({ color: `${color}99` });
    } else {
      indicator.series.applyOptions({ color });
    }
  }

  /**
   * Get indicator by ID
   */
  getIndicator(id: string): Indicator | undefined {
    return this.indicators.get(id);
  }

  /**
   * Check if indicator exists
   */
  hasIndicator(id: string): boolean {
    return this.indicators.has(id);
  }

  /**
   * Get all indicator IDs
   */
  getIndicatorIds(): string[] {
    return Array.from(this.indicators.keys());
  }

  // Legacy methods for backward compatibility
  addSMA(period: number, color: string): ISeriesApi<"Line"> {
    const id = `sma_${period}`;
    return this.addSMAWithId(id, period, color, true);
  }

  addEMA(period: number, color: string): ISeriesApi<"Line"> {
    const id = `ema_${period}`;
    return this.addEMAWithId(id, period, color, true);
  }

  addBollingerBands(period: number = 20, stdDev: number = 2): void {
    this.addBollingerWithId("bollinger", period, stdDev, "#26a69a", true);
  }

  // Internal methods with ID support
  private addSMAWithId(
    id: string,
    period: number,
    color: string,
    visible: boolean
  ): ISeriesApi<"Line"> {
    const series = this.chart.addSeries(LineSeries, {
      color: color,
      lineWidth: 1,
      priceScaleId: "right",
      lastValueVisible: false,
      priceLineVisible: false,
      visible: visible,
    });
    this.indicators.set(id, {
      id,
      series,
      period,
      type: "sma",
      visible,
      color,
    });
    return series;
  }

  private addEMAWithId(
    id: string,
    period: number,
    color: string,
    visible: boolean
  ): ISeriesApi<"Line"> {
    const series = this.chart.addSeries(LineSeries, {
      color: color,
      lineWidth: 1,
      priceScaleId: "right",
      lastValueVisible: false,
      priceLineVisible: false,
      visible: visible,
    });
    this.indicators.set(id, {
      id,
      series,
      period,
      type: "ema",
      visible,
      color,
    });
    return series;
  }

  private addBollingerWithId(
    id: string,
    period: number,
    stdDev: number,
    color: string,
    visible: boolean
  ): void {
    const upper = this.chart.addSeries(LineSeries, {
      color: `${color}99`, // 60% opacity
      lineWidth: 1,
      priceScaleId: "right",
      lastValueVisible: false,
      priceLineVisible: false,
      visible: visible,
    });
    const middle = this.chart.addSeries(LineSeries, {
      color: "rgba(255, 255, 255, 0.4)",
      lineWidth: 1,
      lineStyle: LineStyle.Dashed,
      priceScaleId: "right",
      lastValueVisible: false,
      priceLineVisible: false,
      visible: visible,
    });
    const lower = this.chart.addSeries(LineSeries, {
      color: `${color}99`, // 60% opacity
      lineWidth: 1,
      priceScaleId: "right",
      lastValueVisible: false,
      priceLineVisible: false,
      visible: visible,
    });
    this.indicators.set(id, {
      id,
      upper,
      middle,
      lower,
      period,
      stdDev,
      type: "bollinger",
      visible,
      color,
    });
  }

  /**
   * Update a single indicator's data
   */
  private updateIndicator(id: string): void {
    const indicator = this.indicators.get(id);
    if (!indicator || !indicator.visible) return;

    if (indicator.type === "sma") {
      indicator.series.setData(this.calculateSMA(this.candleData, indicator.period));
    } else if (indicator.type === "ema") {
      indicator.series.setData(this.calculateEMA(this.candleData, indicator.period));
    } else if (indicator.type === "bollinger") {
      const bb = this.calculateBollingerBands(
        this.candleData,
        indicator.period,
        indicator.stdDev
      );
      indicator.upper.setData(bb.upper);
      indicator.middle.setData(bb.middle);
      indicator.lower.setData(bb.lower);
    }
  }

  update(candleData: CandleData[]): void {
    this.candleData = candleData;
    for (const [, indicator] of this.indicators) {
      if (!indicator.visible) continue;

      if (indicator.type === "sma") {
        indicator.series.setData(this.calculateSMA(candleData, indicator.period));
      } else if (indicator.type === "ema") {
        indicator.series.setData(this.calculateEMA(candleData, indicator.period));
      } else if (indicator.type === "bollinger") {
        const bb = this.calculateBollingerBands(
          candleData,
          indicator.period,
          indicator.stdDev
        );
        indicator.upper.setData(bb.upper);
        indicator.middle.setData(bb.middle);
        indicator.lower.setData(bb.lower);
      }
    }
  }

  updateLast(candle: CandleData): void {
    if (this.candleData.length === 0) return;

    // Update or append the last candle
    const lastIdx = this.candleData.length - 1;
    if (this.candleData[lastIdx].time === candle.time) {
      this.candleData[lastIdx] = candle;
    } else {
      this.candleData.push(candle);
    }

    // Recalculate the last few points for each indicator
    for (const [, indicator] of this.indicators) {
      if (!indicator.visible) continue;

      if (indicator.type === "sma") {
        const smaData = this.calculateSMA(this.candleData, indicator.period);
        if (smaData.length > 0) {
          const last = smaData[smaData.length - 1];
          if (last.value !== undefined) {
            indicator.series.update(last);
          }
        }
      } else if (indicator.type === "ema") {
        const emaData = this.calculateEMA(this.candleData, indicator.period);
        if (emaData.length > 0) {
          const last = emaData[emaData.length - 1];
          if (last.value !== undefined) {
            indicator.series.update(last);
          }
        }
      } else if (indicator.type === "bollinger") {
        const bb = this.calculateBollingerBands(
          this.candleData,
          indicator.period,
          indicator.stdDev
        );
        if (bb.upper.length > 0) {
          const lastUpper = bb.upper[bb.upper.length - 1];
          const lastMiddle = bb.middle[bb.middle.length - 1];
          const lastLower = bb.lower[bb.lower.length - 1];
          if (lastUpper.value !== undefined) {
            indicator.upper.update(lastUpper);
            indicator.middle.update(lastMiddle);
            indicator.lower.update(lastLower);
          }
        }
      }
    }
  }

  toggle(name: string): boolean {
    const indicator = this.indicators.get(name);
    if (!indicator) return false;

    indicator.visible = !indicator.visible;

    if (indicator.type === "bollinger") {
      indicator.upper.applyOptions({ visible: indicator.visible });
      indicator.middle.applyOptions({ visible: indicator.visible });
      indicator.lower.applyOptions({ visible: indicator.visible });
    } else {
      indicator.series.applyOptions({ visible: indicator.visible });
    }

    // If turning on, recalculate
    if (indicator.visible && this.candleData.length > 0) {
      this.update(this.candleData);
    }

    return indicator.visible;
  }

  isVisible(name: string): boolean {
    const indicator = this.indicators.get(name);
    return indicator ? indicator.visible : false;
  }

  clear(): void {
    for (const [, indicator] of this.indicators) {
      if (indicator.type === "bollinger") {
        indicator.upper.setData([]);
        indicator.middle.setData([]);
        indicator.lower.setData([]);
      } else {
        indicator.series.setData([]);
      }
    }
    this.candleData = [];
  }

  /**
   * Clear all indicators and remove series from chart
   */
  destroy(): void {
    for (const id of this.indicators.keys()) {
      this.removeIndicator(id);
    }
    this.candleData = [];
  }

  private calculateSMA(data: CandleData[], period: number): LinePoint[] {
    const result: LinePoint[] = [];
    for (let i = 0; i < data.length; i++) {
      if (i < period - 1) {
        result.push({ time: data[i].time as Time });
      } else {
        let sum = 0;
        for (let j = i - period + 1; j <= i; j++) {
          sum += data[j].close;
        }
        result.push({ time: data[i].time as Time, value: sum / period });
      }
    }
    return result;
  }

  private calculateEMA(data: CandleData[], period: number): LinePoint[] {
    const k = 2 / (period + 1);
    const result: LinePoint[] = [];
    let ema: number | null = null;

    for (let i = 0; i < data.length; i++) {
      if (i < period - 1) {
        result.push({ time: data[i].time as Time });
      } else if (i === period - 1) {
        let sum = 0;
        for (let j = 0; j < period; j++) {
          sum += data[j].close;
        }
        ema = sum / period;
        result.push({ time: data[i].time as Time, value: ema });
      } else {
        ema = data[i].close * k + ema! * (1 - k);
        result.push({ time: data[i].time as Time, value: ema });
      }
    }
    return result;
  }

  private calculateBollingerBands(
    data: CandleData[],
    period: number,
    stdDev: number
  ): { upper: LinePoint[]; middle: LinePoint[]; lower: LinePoint[] } {
    const upper: LinePoint[] = [];
    const middle: LinePoint[] = [];
    const lower: LinePoint[] = [];

    for (let i = 0; i < data.length; i++) {
      if (i < period - 1) {
        upper.push({ time: data[i].time as Time });
        middle.push({ time: data[i].time as Time });
        lower.push({ time: data[i].time as Time });
      } else {
        let sum = 0;
        for (let j = i - period + 1; j <= i; j++) {
          sum += data[j].close;
        }
        const sma = sum / period;

        let variance = 0;
        for (let j = i - period + 1; j <= i; j++) {
          variance += Math.pow(data[j].close - sma, 2);
        }
        variance /= period;
        const std = Math.sqrt(variance);

        middle.push({ time: data[i].time as Time, value: sma });
        upper.push({ time: data[i].time as Time, value: sma + stdDev * std });
        lower.push({ time: data[i].time as Time, value: sma - stdDev * std });
      }
    }
    return { upper, middle, lower };
  }
}
