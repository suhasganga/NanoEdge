/**
 * Tests for indicator calculations.
 *
 * Since the calculation methods in IndicatorManager are private,
 * we test them by creating standalone pure functions that mirror the logic.
 * We also test the IndicatorManager class with a mocked chart API.
 */

import { describe, it, expect, vi, beforeEach } from "vitest";
import { IndicatorManager } from "./indicators";

// Test data
interface CandleData {
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume?: number;
}

// Pure calculation functions (mirroring the private methods for testing)
function calculateSMA(
  data: CandleData[],
  period: number
): { time: number; value?: number }[] {
  const result: { time: number; value?: number }[] = [];
  for (let i = 0; i < data.length; i++) {
    if (i < period - 1) {
      result.push({ time: data[i].time });
    } else {
      let sum = 0;
      for (let j = i - period + 1; j <= i; j++) {
        sum += data[j].close;
      }
      result.push({ time: data[i].time, value: sum / period });
    }
  }
  return result;
}

function calculateEMA(
  data: CandleData[],
  period: number
): { time: number; value?: number }[] {
  const k = 2 / (period + 1);
  const result: { time: number; value?: number }[] = [];
  let ema: number | null = null;

  for (let i = 0; i < data.length; i++) {
    if (i < period - 1) {
      result.push({ time: data[i].time });
    } else if (i === period - 1) {
      let sum = 0;
      for (let j = 0; j < period; j++) {
        sum += data[j].close;
      }
      ema = sum / period;
      result.push({ time: data[i].time, value: ema });
    } else {
      ema = data[i].close * k + ema! * (1 - k);
      result.push({ time: data[i].time, value: ema });
    }
  }
  return result;
}

function calculateBollingerBands(
  data: CandleData[],
  period: number,
  stdDev: number
): {
  upper: { time: number; value?: number }[];
  middle: { time: number; value?: number }[];
  lower: { time: number; value?: number }[];
} {
  const upper: { time: number; value?: number }[] = [];
  const middle: { time: number; value?: number }[] = [];
  const lower: { time: number; value?: number }[] = [];

  for (let i = 0; i < data.length; i++) {
    if (i < period - 1) {
      upper.push({ time: data[i].time });
      middle.push({ time: data[i].time });
      lower.push({ time: data[i].time });
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

      middle.push({ time: data[i].time, value: sma });
      upper.push({ time: data[i].time, value: sma + stdDev * std });
      lower.push({ time: data[i].time, value: sma - stdDev * std });
    }
  }
  return { upper, middle, lower };
}

// Sample candle data for testing
function createSampleCandles(count: number, basePrice = 100): CandleData[] {
  const candles: CandleData[] = [];
  for (let i = 0; i < count; i++) {
    // Create predictable prices for testing: 100, 102, 104, 106, ...
    const close = basePrice + i * 2;
    candles.push({
      time: 1704067200 + i * 60, // 1 minute apart
      open: close - 1,
      high: close + 1,
      low: close - 2,
      close: close,
      volume: 100,
    });
  }
  return candles;
}

describe("calculateSMA", () => {
  it("returns empty array for empty data", () => {
    const result = calculateSMA([], 20);
    expect(result).toEqual([]);
  });

  it("returns undefined values for insufficient data", () => {
    const candles = createSampleCandles(3);
    const result = calculateSMA(candles, 5);

    // All 3 points should have no value (insufficient data for period 5)
    expect(result).toHaveLength(3);
    expect(result[0].value).toBeUndefined();
    expect(result[1].value).toBeUndefined();
    expect(result[2].value).toBeUndefined();
  });

  it("calculates correct average at period boundary", () => {
    // Create 5 candles with close prices: 100, 102, 104, 106, 108
    const candles = createSampleCandles(5);
    const result = calculateSMA(candles, 5);

    // First 4 should have no value
    expect(result[0].value).toBeUndefined();
    expect(result[1].value).toBeUndefined();
    expect(result[2].value).toBeUndefined();
    expect(result[3].value).toBeUndefined();

    // 5th should have SMA = (100 + 102 + 104 + 106 + 108) / 5 = 104
    expect(result[4].value).toBe(104);
  });

  it("all values defined after period", () => {
    const candles = createSampleCandles(10);
    const result = calculateSMA(candles, 3);

    // First 2 should have no value
    expect(result[0].value).toBeUndefined();
    expect(result[1].value).toBeUndefined();

    // Rest should all have values
    for (let i = 2; i < result.length; i++) {
      expect(result[i].value).toBeDefined();
    }
  });

  it("produces correct rolling average", () => {
    // Candles: 100, 102, 104, 106, 108
    const candles = createSampleCandles(5);
    const result = calculateSMA(candles, 3);

    // SMA at index 2: (100 + 102 + 104) / 3 = 102
    expect(result[2].value).toBe(102);

    // SMA at index 3: (102 + 104 + 106) / 3 = 104
    expect(result[3].value).toBe(104);

    // SMA at index 4: (104 + 106 + 108) / 3 = 106
    expect(result[4].value).toBe(106);
  });

  it("handles period of 1", () => {
    const candles = createSampleCandles(3);
    const result = calculateSMA(candles, 1);

    // SMA with period 1 should equal the close price
    expect(result[0].value).toBe(100);
    expect(result[1].value).toBe(102);
    expect(result[2].value).toBe(104);
  });
});

describe("calculateEMA", () => {
  it("returns empty array for empty data", () => {
    const result = calculateEMA([], 20);
    expect(result).toEqual([]);
  });

  it("uses SMA as seed at period boundary", () => {
    // Candles: 100, 102, 104
    const candles = createSampleCandles(3);
    const result = calculateEMA(candles, 3);

    // At period-1 (index 2), EMA should equal SMA = (100 + 102 + 104) / 3 = 102
    expect(result[2].value).toBe(102);
  });

  it("applies correct multiplier k = 2/(period+1)", () => {
    const candles = createSampleCandles(5);
    const result = calculateEMA(candles, 3);

    // k = 2 / (3 + 1) = 0.5
    const k = 0.5;

    // EMA at index 2 (seed): SMA = 102
    expect(result[2].value).toBe(102);

    // EMA at index 3: close=106, prevEMA=102
    // EMA = 106 * 0.5 + 102 * 0.5 = 104
    expect(result[3].value).toBe(104);

    // EMA at index 4: close=108, prevEMA=104
    // EMA = 108 * 0.5 + 104 * 0.5 = 106
    expect(result[4].value).toBe(106);
  });

  it("returns undefined values before period", () => {
    const candles = createSampleCandles(5);
    const result = calculateEMA(candles, 3);

    expect(result[0].value).toBeUndefined();
    expect(result[1].value).toBeUndefined();
  });

  it("converges toward price faster with smaller period", () => {
    // EMA with smaller period reacts faster to price changes
    const candles: CandleData[] = [
      { time: 1, open: 100, high: 101, low: 99, close: 100 },
      { time: 2, open: 100, high: 101, low: 99, close: 100 },
      { time: 3, open: 100, high: 101, low: 99, close: 100 },
      { time: 4, open: 150, high: 151, low: 149, close: 150 }, // Big jump
    ];

    const ema2 = calculateEMA(candles, 2);
    const ema3 = calculateEMA(candles, 3);

    // EMA with period 2 should be closer to 150 than EMA with period 3
    expect(ema2[3].value!).toBeGreaterThan(ema3[3].value!);
  });
});

describe("calculateBollingerBands", () => {
  it("returns empty arrays for empty data", () => {
    const result = calculateBollingerBands([], 20, 2);
    expect(result.upper).toEqual([]);
    expect(result.middle).toEqual([]);
    expect(result.lower).toEqual([]);
  });

  it("middle band equals SMA", () => {
    const candles = createSampleCandles(5);
    const bb = calculateBollingerBands(candles, 5, 2);
    const sma = calculateSMA(candles, 5);

    // Middle band should equal SMA at each point
    for (let i = 0; i < candles.length; i++) {
      expect(bb.middle[i].value).toBe(sma[i].value);
    }
  });

  it("bands are symmetric around middle", () => {
    const candles = createSampleCandles(10);
    const bb = calculateBollingerBands(candles, 5, 2);

    // For points with values, upper and lower should be equidistant from middle
    for (let i = 4; i < candles.length; i++) {
      const upper = bb.upper[i].value!;
      const middle = bb.middle[i].value!;
      const lower = bb.lower[i].value!;

      const upperDiff = upper - middle;
      const lowerDiff = middle - lower;

      expect(upperDiff).toBeCloseTo(lowerDiff, 10);
    }
  });

  it("stdDev parameter scales band width", () => {
    const candles = createSampleCandles(10);
    const bb1 = calculateBollingerBands(candles, 5, 1);
    const bb2 = calculateBollingerBands(candles, 5, 2);

    // At index 4 (first valid point)
    const width1 = bb1.upper[4].value! - bb1.lower[4].value!;
    const width2 = bb2.upper[4].value! - bb2.lower[4].value!;

    // Width with stdDev=2 should be ~2x width with stdDev=1
    expect(width2).toBeCloseTo(width1 * 2, 10);
  });

  it("returns undefined values before period", () => {
    const candles = createSampleCandles(5);
    const bb = calculateBollingerBands(candles, 5, 2);

    // First 4 should have no value
    for (let i = 0; i < 4; i++) {
      expect(bb.upper[i].value).toBeUndefined();
      expect(bb.middle[i].value).toBeUndefined();
      expect(bb.lower[i].value).toBeUndefined();
    }
  });

  it("variance calculation is correct", () => {
    // Create candles with known variance
    // Prices: 100, 100, 100, 100, 100 -> variance = 0
    const flatCandles: CandleData[] = [];
    for (let i = 0; i < 5; i++) {
      flatCandles.push({
        time: 1704067200 + i * 60,
        open: 100,
        high: 101,
        low: 99,
        close: 100,
        volume: 100,
      });
    }

    const bb = calculateBollingerBands(flatCandles, 5, 2);

    // With zero variance, all bands should equal the SMA
    expect(bb.upper[4].value).toBe(100);
    expect(bb.middle[4].value).toBe(100);
    expect(bb.lower[4].value).toBe(100);
  });
});

describe("IndicatorManager", () => {
  let mockChart: any;
  let mockSeries: any;

  beforeEach(() => {
    mockSeries = {
      setData: vi.fn(),
      update: vi.fn(),
      applyOptions: vi.fn(),
    };

    mockChart = {
      addSeries: vi.fn(() => mockSeries),
    };
  });

  describe("addSMA", () => {
    it("creates series and returns it", () => {
      const manager = new IndicatorManager(mockChart);
      const series = manager.addSMA(20, "#2962FF");

      expect(mockChart.addSeries).toHaveBeenCalled();
      expect(series).toBe(mockSeries);
    });

    it("stores indicator with correct period", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      expect(manager.isVisible("sma_20")).toBe(true);
    });
  });

  describe("addEMA", () => {
    it("creates series and stores indicator", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addEMA(12, "#00E676");

      expect(mockChart.addSeries).toHaveBeenCalled();
      expect(manager.isVisible("ema_12")).toBe(true);
    });
  });

  describe("addBollingerBands", () => {
    it("creates three series for upper, middle, lower", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addBollingerBands(20, 2);

      // Should create 3 series (upper, middle, lower)
      expect(mockChart.addSeries).toHaveBeenCalledTimes(3);
      expect(manager.isVisible("bollinger")).toBe(true);
    });
  });

  describe("toggle", () => {
    it("returns new visibility state", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      // Initially visible
      expect(manager.isVisible("sma_20")).toBe(true);

      // Toggle off
      const newState1 = manager.toggle("sma_20");
      expect(newState1).toBe(false);
      expect(manager.isVisible("sma_20")).toBe(false);

      // Toggle on
      const newState2 = manager.toggle("sma_20");
      expect(newState2).toBe(true);
      expect(manager.isVisible("sma_20")).toBe(true);
    });

    it("returns false for unknown indicator", () => {
      const manager = new IndicatorManager(mockChart);
      const result = manager.toggle("unknown_indicator");
      expect(result).toBe(false);
    });

    it("calls applyOptions on series", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      manager.toggle("sma_20");

      expect(mockSeries.applyOptions).toHaveBeenCalledWith({ visible: false });
    });
  });

  describe("isVisible", () => {
    it("returns true for visible indicator", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      expect(manager.isVisible("sma_20")).toBe(true);
    });

    it("returns false for unknown indicator", () => {
      const manager = new IndicatorManager(mockChart);

      expect(manager.isVisible("unknown")).toBe(false);
    });
  });

  describe("clear", () => {
    it("clears data from all series", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");
      manager.addEMA(12, "#00E676");

      manager.clear();

      expect(mockSeries.setData).toHaveBeenCalledWith([]);
    });
  });

  describe("update", () => {
    it("calls setData on visible indicators", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      const candles = createSampleCandles(25);
      manager.update(candles);

      expect(mockSeries.setData).toHaveBeenCalled();
    });

    it("does not update hidden indicators", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");
      manager.toggle("sma_20"); // Hide it

      mockSeries.setData.mockClear();

      const candles = createSampleCandles(25);
      manager.update(candles);

      // setData should not be called for hidden indicator
      expect(mockSeries.setData).not.toHaveBeenCalled();
    });
  });

  describe("updateLast", () => {
    it("updates the last candle in data", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      const candles = createSampleCandles(25);
      manager.update(candles);

      mockSeries.update.mockClear();

      // Update with a candle at the same time
      const updatedCandle = { ...candles[24], close: 200 };
      manager.updateLast(updatedCandle);

      expect(mockSeries.update).toHaveBeenCalled();
    });

    it("does nothing when no data exists", () => {
      const manager = new IndicatorManager(mockChart);
      manager.addSMA(20, "#2962FF");

      // Try to update without any existing data
      manager.updateLast({
        time: 1704067200,
        open: 100,
        high: 101,
        low: 99,
        close: 100,
      });

      // Should not throw or call update
      expect(mockSeries.update).not.toHaveBeenCalled();
    });
  });
});
