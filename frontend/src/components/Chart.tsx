import {
  Component,
  createEffect,
  createSignal,
  onCleanup,
  onMount,
  Show,
} from "solid-js";
import {
  createChart,
  IChartApi,
  ISeriesApi,
  CandlestickData,
  HistogramData,
  Time,
  ColorType,
  CandlestickSeries,
  HistogramSeries,
  BarSeries,
  LineSeries,
  AreaSeries,
  BaselineSeries,
  CrosshairMode as LWCCrosshairMode,
  LastPriceAnimationMode,
  LineStyle,
  SeriesType,
} from "lightweight-charts";
import { useCandleWebSocket, CandleData } from "~/hooks/useWebSocket";
import { IndicatorManager } from "~/lib/indicators";
import { PriceLineManager } from "~/lib/priceLines";
import { cn } from "~/lib/utils";
import { OrderOverlayManager } from "~/mm/orderOverlay";
import { useOrdersWebSocket } from "~/mm/useOrdersWebSocket";
import { orderStore } from "~/mm/orderStore";
import type { OrderFill } from "~/mm/types";
import {
  settings,
  type ChartSettings,
  CrosshairMode,
} from "~/stores/chartSettings";
import {
  timeToTz,
  resolveTimezone,
  getTimezoneOffsetLabel,
} from "~/lib/timezone";

// Interval durations in seconds
const INTERVAL_SECONDS: Record<string, number> = {
  "1m": 60,
  "5m": 300,
  "15m": 900,
  "30m": 1800,
  "1h": 3600,
  "4h": 14400,
  "1d": 86400,
};

// Chart type definitions
export type ChartType = "candlestick" | "bar" | "line" | "area" | "baseline";

interface ChartTypeConfig {
  seriesType: typeof CandlestickSeries | typeof BarSeries | typeof LineSeries | typeof AreaSeries | typeof BaselineSeries;
  usesOHLC: boolean;
  options: Record<string, unknown>;
}

const CHART_TYPES: Record<ChartType, ChartTypeConfig> = {
  candlestick: {
    seriesType: CandlestickSeries,
    usesOHLC: true,
    options: {
      upColor: "#26a69a",
      downColor: "#ef5350",
      borderVisible: false,
      wickUpColor: "#26a69a",
      wickDownColor: "#ef5350",
    },
  },
  bar: {
    seriesType: BarSeries,
    usesOHLC: true,
    options: {
      upColor: "#26a69a",
      downColor: "#ef5350",
    },
  },
  line: {
    seriesType: LineSeries,
    usesOHLC: false,
    options: {
      color: "#2962FF",
      lineWidth: 2,
      crosshairMarkerVisible: true,
      crosshairMarkerRadius: 4,
      lastPriceAnimation: LastPriceAnimationMode.Continuous,
    },
  },
  area: {
    seriesType: AreaSeries,
    usesOHLC: false,
    options: {
      lineColor: "#2962FF",
      topColor: "rgba(41, 98, 255, 0.4)",
      bottomColor: "rgba(41, 98, 255, 0.05)",
      lineWidth: 2,
      crosshairMarkerVisible: true,
    },
  },
  baseline: {
    seriesType: BaselineSeries,
    usesOHLC: false,
    options: {
      baseValue: { type: "price", price: 0 },
      topLineColor: "rgba(38, 166, 154, 1)",
      topFillColor1: "rgba(38, 166, 154, 0.28)",
      topFillColor2: "rgba(38, 166, 154, 0.05)",
      bottomLineColor: "rgba(239, 83, 80, 1)",
      bottomFillColor1: "rgba(239, 83, 80, 0.05)",
      bottomFillColor2: "rgba(239, 83, 80, 0.28)",
      lineWidth: 2,
    },
  },
};

interface ChartProps {
  symbol: string;
  interval: string;
  chartType?: ChartType;
  onReady?: (api: ChartApi) => void;
}

export interface ChartApi {
  scrollToRealtime: () => void;
  fitContent: () => void;
  setChartType: (type: ChartType) => void;
  setScaleMode: (mode: number) => void;
  toggleVolume: () => boolean;
  toggleIndicator: (name: string) => boolean;
  isIndicatorVisible: (name: string) => boolean;
  // Dynamic indicator methods
  addIndicator: (config: import("~/stores/indicatorStore").IndicatorConfig) => void;
  removeIndicator: (id: string) => void;
  setIndicatorVisibility: (id: string, visible: boolean) => void;
  syncIndicators: (configs: import("~/stores/indicatorStore").IndicatorConfig[]) => void;
  // New scale methods
  setInvertScale: (invert: boolean) => void;
  setAutoScale: (auto: boolean) => void;
  setLockPriceToBarRatio: (lock: boolean) => void;
  setPriceScalePosition: (position: "left" | "right") => void;
  // Price line methods
  setCurrentPriceLine: (visible: boolean) => void;
  setPrevDayCloseLine: (visible: boolean, price?: number) => void;
  setHighLowLines: (visible: boolean, high?: number, low?: number) => void;
  setBidAskLines: (visible: boolean, bid?: number, ask?: number) => void;
  updateBidAsk: (bid: number, ask: number) => void;
  // Appearance
  applyCandleColors: (colors: Partial<ChartSettings>) => void;
  applyGridSettings: (settings: Partial<ChartSettings>) => void;
  applyCrosshairSettings: (settings: Partial<ChartSettings>) => void;
  // Full settings
  applySettings: (settings: ChartSettings) => void;
  // Get current price (for bar countdown)
  getCurrentPrice: () => number | null;
  // Get interval seconds
  getIntervalSeconds: () => number;
}

interface AggregatedCandle {
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
}

interface LegendData {
  symbol: string;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
  change: number;
  changePercent: number;
}

interface TooltipData extends LegendData {
  time: number;
  x: number;
  y: number;
}

export const Chart: Component<ChartProps> = (props) => {
  let chartContainer: HTMLDivElement | undefined;
  let chart: IChartApi | undefined;
  let mainSeries: ISeriesApi<SeriesType> | undefined;
  let volumeSeries: ISeriesApi<"Histogram"> | undefined;
  let indicatorManager: IndicatorManager | undefined;
  let priceLineManager: PriceLineManager | undefined;
  let orderOverlayManager: OrderOverlayManager | undefined;
  let abortController: AbortController | undefined;
  let chartApiRef: ChartApi | undefined;

  // Orders WebSocket connection
  const { isConnected: ordersConnected } = useOrdersWebSocket({
    symbol: () => props.symbol,
  });

  const [isLoading, setIsLoading] = createSignal(true);
  const [error, setError] = createSignal<string | null>(null);
  const [chartType, setChartTypeState] = createSignal<ChartType>(props.chartType ?? "candlestick");
  const [legendData, setLegendData] = createSignal<LegendData | null>(null);
  const [tooltipData, setTooltipData] = createSignal<TooltipData | null>(null);
  const [fillFlash, setFillFlash] = createSignal<OrderFill | null>(null);

  // Dynamic price precision based on price magnitude (replicates TradingView behavior)
  let pricePrecision = 2;
  let priceMinMove = 0.01;

  /**
   * Derive decimal precision from a representative price.
   * Matches how TradingView adapts the price scale for different assets:
   * - BTCUSDT (~90000) → 2 decimals
   * - ETHUSDT (~3000)  → 2 decimals
   * - DOGEUSDT (~0.12) → 5 decimals
   * - SHIBUSDT (~0.00001) → 8 decimals
   */
  const updatePricePrecision = (price: number) => {
    if (price <= 0) return;
    if (price >= 1000) {
      pricePrecision = 2;
    } else if (price >= 100) {
      pricePrecision = 3;
    } else if (price >= 1) {
      pricePrecision = 4;
    } else if (price >= 0.01) {
      pricePrecision = 5;
    } else if (price >= 0.0001) {
      pricePrecision = 6;
    } else {
      pricePrecision = 8;
    }
    priceMinMove = Math.pow(10, -pricePrecision);
  };

  /** Format a price value using the current precision */
  const fmtPrice = (price: number): string => price.toFixed(pricePrecision);

  /** Apply current price format to the main series and overlay */
  const applyPriceFormat = () => {
    if (mainSeries) {
      mainSeries.applyOptions({
        priceFormat: {
          type: "price",
          precision: pricePrecision,
          minMove: priceMinMove,
        },
      });
    }
    orderOverlayManager?.setPricePrecision(pricePrecision);
  };

  // Track previous fill count for detecting new fills
  let prevFillCount = 0;

  // WebSocket for real-time updates
  const { data: wsData } = useCandleWebSocket(() => props.symbol);

  // State for higher timeframe aggregation
  let currentPeriodCandle: AggregatedCandle | null = null;
  let wsMinuteVolumes = new Map<number, number>();
  let candleData: AggregatedCandle[] = [];
  let isLoadingMore = false;

  // Floor timestamp to interval boundary
  const floorTimestamp = (timestamp: number, interval: string): number => {
    const intervalSec = INTERVAL_SECONDS[interval] || 60;
    return Math.floor(timestamp / intervalSec) * intervalSec;
  };

  // Aggregate incoming 1m candle into current period
  const aggregateCandle = (incoming: CandleData): AggregatedCandle => {
    const periodTime = floorTimestamp(incoming.time, props.interval);

    if (!currentPeriodCandle || currentPeriodCandle.time !== periodTime) {
      wsMinuteVolumes.clear();
      currentPeriodCandle = {
        time: periodTime,
        open: incoming.open,
        high: incoming.high,
        low: incoming.low,
        close: incoming.close,
        volume: incoming.volume,
      };
      wsMinuteVolumes.set(incoming.time, incoming.volume);
    } else {
      currentPeriodCandle.high = Math.max(currentPeriodCandle.high, incoming.high);
      currentPeriodCandle.low = Math.min(currentPeriodCandle.low, incoming.low);
      currentPeriodCandle.close = incoming.close;
      wsMinuteVolumes.set(incoming.time, incoming.volume);
      currentPeriodCandle.volume = Array.from(wsMinuteVolumes.values()).reduce(
        (a, b) => a + b,
        0
      );
    }

    return { ...currentPeriodCandle };
  };

  // Get resolved timezone based on current settings and symbol
  const getResolvedTimezone = () => resolveTimezone(settings().timezone, props.symbol);

  // Transform candle time to target timezone
  const transformTime = (utcTime: number): number => {
    const tz = getResolvedTimezone();
    return timeToTz(utcTime, tz);
  };

  // Convert OHLC to single-value format with timezone transformation
  const toSingleValue = (data: AggregatedCandle[]): { time: Time; value: number }[] => {
    return data.map((d) => ({ time: transformTime(d.time) as Time, value: d.close }));
  };

  // Get data formatted for current chart type with timezone transformation
  // Accepts optional type parameter to avoid signal timing issues during rapid switching
  const getFormattedData = (type?: ChartType): CandlestickData<Time>[] | { time: Time; value: number }[] => {
    const actualType = type ?? chartType();
    const config = CHART_TYPES[actualType];
    if (config.usesOHLC) {
      return candleData.map((d) => ({
        time: transformTime(d.time) as Time,
        open: d.open,
        high: d.high,
        low: d.low,
        close: d.close,
      }));
    }
    return toSingleValue(candleData);
  };

  // Format price using dynamic precision
  const formatPrice = (price: number): string => fmtPrice(price);

  // Format volume
  const formatVolume = (value: number): string => {
    if (value >= 1e9) return (value / 1e9).toFixed(2) + "B";
    if (value >= 1e6) return (value / 1e6).toFixed(2) + "M";
    if (value >= 1e3) return (value / 1e3).toFixed(2) + "K";
    return value.toFixed(2);
  };

  // Create main series based on chart type
  // Accepts optional type parameter to avoid signal timing issues during rapid switching
  const createMainSeries = (type?: ChartType) => {
    if (!chart) return;

    const actualType = type ?? chartType();
    const config = CHART_TYPES[actualType];
    const options = { ...config.options };

    // For baseline, set base value from first candle
    if (actualType === "baseline" && candleData.length > 0) {
      (options as any).baseValue = { type: "price", price: candleData[0].open };
    }

    mainSeries = chart.addSeries(config.seriesType as any, options as any);
  };

  // Update volume data with timezone transformation
  const updateVolumeData = () => {
    if (!volumeSeries) return;
    const volumeDataArr: HistogramData<Time>[] = candleData.map((d) => ({
      time: transformTime(d.time) as Time,
      value: d.volume || 0,
      color: d.close >= d.open ? "rgba(38, 166, 154, 0.5)" : "rgba(239, 83, 80, 0.5)",
    }));
    volumeSeries.setData(volumeDataArr);
  };

  // Fetch historical data
  const fetchHistoryData = async (limit: number = 500, endTime?: number) => {
    if (abortController) {
      abortController.abort();
    }
    abortController = new AbortController();

    let url = `/api/history?symbol=${props.symbol}&interval=${props.interval}&limit=${limit}`;
    if (endTime) {
      url += `&end_time=${endTime}`;
    }

    const response = await fetch(url, { signal: abortController.signal });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  };

  // Load more history when scrolling left
  const loadMoreHistory = async () => {
    if (isLoadingMore || candleData.length === 0) return;
    isLoadingMore = true;

    try {
      const oldestTime = candleData[0].time;
      const moreData = await fetchHistoryData(500, oldestTime - 1);

      if (moreData.length > 0 && mainSeries) {
        candleData = [...moreData, ...candleData];
        mainSeries.setData(getFormattedData() as any);
        updateVolumeData();
        indicatorManager?.update(candleData);
      }
    } catch (e) {
      if ((e as Error).name !== "AbortError") {
        console.error("Failed to load more history:", e);
      }
    } finally {
      isLoadingMore = false;
    }
  };

  // Handle crosshair move for legend/tooltip
  const onCrosshairMove = (param: any) => {
    if (!param.point || !param.time || param.point.x < 0 || param.point.y < 0) {
      setTooltipData(null);
      return;
    }

    const seriesData = param.seriesData.get(mainSeries);
    const volumeValue = param.seriesData.get(volumeSeries);

    if (!seriesData) {
      setTooltipData(null);
      return;
    }

    // Get OHLC data
    let ohlc: AggregatedCandle | undefined;
    const config = CHART_TYPES[chartType()];

    if (config.usesOHLC) {
      ohlc = seriesData as AggregatedCandle;
    } else {
      // Find OHLC by transformed time (chart uses transformed times)
      ohlc = candleData.find((c) => transformTime(c.time) === param.time);
    }

    if (!ohlc) return;

    const change = ohlc.close - ohlc.open;
    const changePercent = (change / ohlc.open) * 100;

    const data: LegendData = {
      symbol: props.symbol,
      open: ohlc.open,
      high: ohlc.high,
      low: ohlc.low,
      close: ohlc.close,
      volume: volumeValue?.value ?? ohlc.volume ?? 0,
      change,
      changePercent,
    };

    setLegendData(data);
    setTooltipData({
      ...data,
      time: param.time,
      x: param.point.x,
      y: param.point.y,
    });
  };

  // Load data
  const loadData = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const data = await fetchHistoryData(500);

      if (mainSeries && volumeSeries && Array.isArray(data)) {
        candleData = data;

        // Derive price precision from first candle close price
        if (data.length > 0) {
          updatePricePrecision(data[data.length - 1].close);
          applyPriceFormat();
        }

        mainSeries.setData(getFormattedData() as any);
        updateVolumeData();
        indicatorManager?.update(candleData);

        // Reset aggregation state
        currentPeriodCandle = null;
        wsMinuteVolumes.clear();

        // Initialize current period from last candle
        if (data.length > 0 && props.interval !== "1m") {
          const last = data[data.length - 1];
          currentPeriodCandle = { ...last };
        }

        // Update legend with latest
        if (data.length > 0) {
          const last = data[data.length - 1];
          const change = last.close - last.open;
          setLegendData({
            symbol: props.symbol,
            open: last.open,
            high: last.high,
            low: last.low,
            close: last.close,
            volume: last.volume,
            change,
            changePercent: (change / last.open) * 100,
          });
        }

        chart?.timeScale().fitContent();
      }
    } catch (e) {
      if ((e as Error).name !== "AbortError") {
        console.error("Failed to fetch history:", e);
        setError(e instanceof Error ? e.message : "Failed to fetch data");
      }
    } finally {
      setIsLoading(false);
    }
  };

  // Initialize chart
  onMount(() => {
    if (!chartContainer) return;

    chart = createChart(chartContainer, {
      layout: {
        background: { type: ColorType.Solid, color: "transparent" },
        textColor: "#d1d4dc",
        fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      },
      grid: {
        vertLines: { color: "#1e222d" },
        horzLines: { color: "#1e222d" },
      },
      crosshair: {
        mode: CrosshairMode.Normal,
        vertLine: {
          color: "#758696",
          width: 1,
          style: LineStyle.Dashed,
          labelBackgroundColor: "#2a2e39",
        },
        horzLine: {
          color: "#758696",
          width: 1,
          style: LineStyle.Dashed,
          labelBackgroundColor: "#2a2e39",
        },
      },
      rightPriceScale: {
        borderColor: "#2a2e39",
        scaleMargins: {
          top: 0.05,
          bottom: 0.25,
        },
      },
      timeScale: {
        borderColor: "#2a2e39",
        timeVisible: true,
        secondsVisible: false,
        rightOffset: 5,
        barSpacing: 6,
      },
      handleScroll: {
        mouseWheel: true,
        pressedMouseMove: true,
        horzTouchDrag: true,
        vertTouchDrag: false,
      },
      handleScale: {
        axisPressedMouseMove: true,
        mouseWheel: true,
        pinch: true,
      },
    });

    // Create main series
    createMainSeries();

    // Volume series
    volumeSeries = chart.addSeries(HistogramSeries, {
      priceFormat: { type: "volume" },
      priceScaleId: "volume",
    });

    volumeSeries.priceScale().applyOptions({
      scaleMargins: {
        top: 0.85,
        bottom: 0,
      },
    });

    // Initialize indicator manager
    // Indicators are now managed through the indicatorStore
    // The parent component will call syncIndicators() after onReady
    indicatorManager = new IndicatorManager(chart);

    // Initialize price line manager
    if (mainSeries) {
      priceLineManager = new PriceLineManager(mainSeries);

      // Initialize order overlay manager for MM visualization
      orderOverlayManager = new OrderOverlayManager(mainSeries);
      orderOverlayManager.setTimeTransform(transformTime);
    }

    // Subscribe to crosshair move
    chart.subscribeCrosshairMove(onCrosshairMove);

    // Subscribe to visible range changes for lazy loading
    chart.timeScale().subscribeVisibleLogicalRangeChange((logicalRange) => {
      if (!logicalRange || !mainSeries) return;
      const barsInfo = mainSeries.barsInLogicalRange(logicalRange);
      if (barsInfo && barsInfo.barsBefore !== null && barsInfo.barsBefore < 10) {
        loadMoreHistory();
      }
    });

    // Handle resize
    const resizeObserver = new ResizeObserver((entries) => {
      if (chart && entries[0]) {
        const { width, height } = entries[0].contentRect;
        chart.applyOptions({ width, height });
      }
    });

    resizeObserver.observe(chartContainer);

    // Helper to get current price scale ID
    const getPriceScaleId = () => {
      const s = settings();
      return s.priceScalePosition === "left" ? "left" : "right";
    };

    // Expose API to parent
    chartApiRef = {
      scrollToRealtime: () => chart?.timeScale().scrollToRealTime(),
      fitContent: () => chart?.timeScale().fitContent(),
      setChartType: (type: ChartType) => {
        if (type === chartType() || !chart) return;

        // Save state
        const visibleRange = chart.timeScale().getVisibleLogicalRange();

        // Remove old series if it exists
        if (mainSeries) {
          chart.removeSeries(mainSeries);
          mainSeries = undefined; // Clear reference immediately to prevent stale access
        }

        // Update state and create new series
        // Pass type directly to avoid signal timing issues during rapid switching
        setChartTypeState(type);
        createMainSeries(type);
        applyPriceFormat();

        // Re-initialize price line manager with new series
        // mainSeries is reassigned by createMainSeries - use type assertion
        if (mainSeries !== undefined) {
          const series = mainSeries as ISeriesApi<SeriesType>;
          priceLineManager = new PriceLineManager(series);

          // Update order overlay manager with new series
          if (orderOverlayManager) {
            orderOverlayManager.updateSeries(series);
          }

          // Restore data - pass type directly
          if (candleData.length > 0) {
            series.setData(getFormattedData(type) as any);
          }
        }

        // Restore range
        if (visibleRange) {
          chart.timeScale().setVisibleLogicalRange(visibleRange);
        }
      },
      setScaleMode: (mode: number) => {
        const scaleId = getPriceScaleId();
        chart?.priceScale(scaleId).applyOptions({ mode });
      },
      toggleVolume: () => {
        if (!volumeSeries) return false;
        const visible = volumeSeries.options().visible !== false;
        volumeSeries.applyOptions({ visible: !visible });
        return !visible;
      },
      toggleIndicator: (name: string) => {
        return indicatorManager?.toggle(name) ?? false;
      },
      isIndicatorVisible: (name: string) => {
        return indicatorManager?.isVisible(name) ?? false;
      },
      addIndicator: (config) => {
        indicatorManager?.addDynamicIndicator(config);
      },
      removeIndicator: (id: string) => {
        indicatorManager?.removeIndicator(id);
      },
      setIndicatorVisibility: (id: string, visible: boolean) => {
        indicatorManager?.setIndicatorVisibility(id, visible);
      },
      syncIndicators: (configs) => {
        if (!indicatorManager) return;
        // Get current indicator IDs
        const currentIds = new Set(indicatorManager.getIndicatorIds());
        const newIds = new Set(configs.map((c) => c.id));

        // Remove indicators that are no longer in configs
        for (const id of currentIds) {
          if (!newIds.has(id)) {
            indicatorManager.removeIndicator(id);
          }
        }

        // Add or update indicators from configs
        for (const config of configs) {
          if (!indicatorManager.hasIndicator(config.id)) {
            indicatorManager.addDynamicIndicator(config);
          } else {
            indicatorManager.setIndicatorVisibility(config.id, config.visible);
          }
        }
      },
      // New scale methods
      setInvertScale: (invert: boolean) => {
        const scaleId = getPriceScaleId();
        chart?.priceScale(scaleId).applyOptions({ invertScale: invert });
      },
      setAutoScale: (auto: boolean) => {
        const scaleId = getPriceScaleId();
        chart?.priceScale(scaleId).applyOptions({ autoScale: auto });
      },
      setLockPriceToBarRatio: (lock: boolean) => {
        const scaleId = getPriceScaleId();
        chart?.priceScale(scaleId).applyOptions({
          scaleMargins: lock
            ? { top: 0.1, bottom: 0.3 } // Fixed margins when locked
            : { top: 0.05, bottom: 0.25 },
        });
      },
      setPriceScalePosition: (position: "left" | "right") => {
        if (!chart || !mainSeries) return;
        chart.applyOptions({
          rightPriceScale: { visible: position === "right" },
          leftPriceScale: { visible: position === "left" },
        });
        mainSeries.applyOptions({ priceScaleId: position });
      },
      // Price line methods
      setCurrentPriceLine: (visible: boolean) => {
        if (!priceLineManager) return;
        const price = candleData.length > 0 ? candleData[candleData.length - 1].close : undefined;
        priceLineManager.setCurrentPriceLine(visible, price);
      },
      setPrevDayCloseLine: (visible: boolean, price?: number) => {
        priceLineManager?.setPrevDayCloseLine(visible, price);
      },
      setHighLowLines: (visible: boolean, high?: number, low?: number) => {
        priceLineManager?.setHighLowLines(visible, high, low);
      },
      setBidAskLines: (visible: boolean, bid?: number, ask?: number) => {
        priceLineManager?.setBidAskLines(visible, bid, ask);
      },
      updateBidAsk: (bid: number, ask: number) => {
        priceLineManager?.updateBidAsk(bid, ask);
      },
      // Appearance
      applyCandleColors: (colors: Partial<ChartSettings>) => {
        if (!mainSeries) return;
        const config = CHART_TYPES[chartType()];
        if (config.usesOHLC) {
          mainSeries.applyOptions({
            upColor: colors.candleUpColor,
            downColor: colors.candleDownColor,
            wickUpColor: colors.wickUpColor,
            wickDownColor: colors.wickDownColor,
            borderUpColor: colors.borderUpColor,
            borderDownColor: colors.borderDownColor,
            borderVisible: colors.borderVisible,
          } as any);
        }
      },
      applyGridSettings: (s: Partial<ChartSettings>) => {
        chart?.applyOptions({
          grid: {
            vertLines: {
              visible: s.gridVerticalVisible,
              color: s.gridVerticalColor,
            },
            horzLines: {
              visible: s.gridHorizontalVisible,
              color: s.gridHorizontalColor,
            },
          },
        });
      },
      applyCrosshairSettings: (s: Partial<ChartSettings>) => {
        chart?.applyOptions({
          crosshair: {
            mode: s.crosshairMode === CrosshairMode.Magnet
              ? LWCCrosshairMode.Magnet
              : LWCCrosshairMode.Normal,
            vertLine: {
              color: s.crosshairColor,
              labelBackgroundColor: s.crosshairLabelBackground,
            },
            horzLine: {
              color: s.crosshairColor,
              labelBackgroundColor: s.crosshairLabelBackground,
            },
          },
        });
      },
      // Full settings
      applySettings: (s: ChartSettings) => {
        if (!chart) return;

        // Scale settings
        chartApiRef?.setScaleMode(s.scaleMode);
        chartApiRef?.setInvertScale(s.invertScale);
        chartApiRef?.setAutoScale(s.autoScale);
        chartApiRef?.setPriceScalePosition(s.priceScalePosition);

        // Candle colors
        chartApiRef?.applyCandleColors(s);

        // Grid
        chartApiRef?.applyGridSettings(s);

        // Crosshair
        chartApiRef?.applyCrosshairSettings(s);

        // Time scale
        chart.timeScale().applyOptions({
          timeVisible: s.timeVisible,
          secondsVisible: s.secondsVisible,
        });

        // Price lines
        chartApiRef?.setCurrentPriceLine(s.showLastPriceLine);
        if (s.showPrevDayClose && s.prevDayClosePrice !== null) {
          chartApiRef?.setPrevDayCloseLine(true, s.prevDayClosePrice);
        } else {
          chartApiRef?.setPrevDayCloseLine(false);
        }
        if (s.showHighLowLines && s.highPrice !== null && s.lowPrice !== null) {
          chartApiRef?.setHighLowLines(true, s.highPrice, s.lowPrice);
        } else {
          chartApiRef?.setHighLowLines(false);
        }
        chartApiRef?.setBidAskLines(s.showBidAskLines);
      },
      // Get current price (for bar countdown)
      getCurrentPrice: () => {
        if (candleData.length === 0) return null;
        return candleData[candleData.length - 1].close;
      },
      // Get interval seconds
      getIntervalSeconds: () => {
        return INTERVAL_SECONDS[props.interval] || 60;
      },
    };

    if (props.onReady) {
      props.onReady(chartApiRef);
    }

    onCleanup(() => {
      resizeObserver.disconnect();
      orderOverlayManager?.clear();
      chart?.remove();
    });

    // Initial data fetch
    loadData();
  });

  // Re-fetch when symbol or interval changes
  createEffect(() => {
    // Track these reactive values to trigger effect on change
    void (props.symbol + props.interval);
    if (chart && mainSeries) {
      // Reset state
      candleData = [];
      currentPeriodCandle = null;
      wsMinuteVolumes.clear();
      mainSeries?.setData([]);
      volumeSeries?.setData([]);
      indicatorManager?.clear();
      orderOverlayManager?.clear();
      loadData();
    }
  });

  // Handle WebSocket updates
  createEffect(() => {
    const incoming = wsData();
    if (!incoming || !mainSeries || !volumeSeries) return;

    // Validate timestamp
    if (incoming.time < 1577836800) {
      console.warn("Invalid candle timestamp:", incoming.time);
      return;
    }

    // Aggregate to current interval
    const candle =
      props.interval === "1m"
        ? {
            time: incoming.time,
            open: incoming.open,
            high: incoming.high,
            low: incoming.low,
            close: incoming.close,
            volume: incoming.volume,
          }
        : aggregateCandle(incoming);

    // Update series with transformed time for display
    const displayTime = transformTime(candle.time);
    const config = CHART_TYPES[chartType()];
    if (config.usesOHLC) {
      mainSeries.update({
        time: displayTime as Time,
        open: candle.open,
        high: candle.high,
        low: candle.low,
        close: candle.close,
      } as any);
    } else {
      mainSeries.update({ time: displayTime as Time, value: candle.close } as any);
    }

    // Update local data (keep original UTC times for internal operations)
    if (candleData.length > 0) {
      const lastIdx = candleData.length - 1;
      if (candleData[lastIdx].time === candle.time) {
        candleData[lastIdx] = candle;
      } else {
        candleData.push(candle);
      }
    }

    // Update volume with transformed time
    volumeSeries.update({
      time: displayTime as Time,
      value: candle.volume,
      color: candle.close >= candle.open ? "rgba(38, 166, 154, 0.5)" : "rgba(239, 83, 80, 0.5)",
    });

    // Update indicators
    indicatorManager?.updateLast(candle);

    // Update current price line
    if (priceLineManager && settings().showLastPriceLine) {
      priceLineManager.updateCurrentPrice(candle.close);
    }

    // Update legend
    const change = candle.close - candle.open;
    setLegendData({
      symbol: props.symbol,
      open: candle.open,
      high: candle.high,
      low: candle.low,
      close: candle.close,
      volume: candle.volume,
      change,
      changePercent: (change / candle.open) * 100,
    });
  });

  // Apply settings reactively when they change
  createEffect(() => {
    const currentSettings = settings();
    if (chartApiRef) {
      chartApiRef.applySettings(currentSettings);
    }
  });

  // Re-render chart when timezone changes
  createEffect(() => {
    // Track timezone setting to trigger effect
    void settings().timezone;
    if (chart && mainSeries && volumeSeries && candleData.length > 0) {
      // Re-apply data with new timezone transformation
      mainSeries.setData(getFormattedData() as any);
      updateVolumeData();
      indicatorManager?.update(candleData);
    }
  });

  // Sync order overlay with orderStore
  createEffect(() => {
    const orders = orderStore.orders();
    if (orderOverlayManager) {
      orderOverlayManager.syncOrders(orders);
    }
  });

  // Sync position overlay
  createEffect(() => {
    const position = orderStore.position();
    if (orderOverlayManager) {
      orderOverlayManager.syncPosition(position);
    }
  });

  // Sync fill markers and show flash notification for new fills
  createEffect(() => {
    const fills = orderStore.fills();
    if (orderOverlayManager) {
      orderOverlayManager.syncFills(fills);
    }

    // Show flash notification for new fills
    if (fills.length > prevFillCount) {
      const newFills = fills.slice(prevFillCount);
      // Show the most recent fill
      const latestFill = newFills[newFills.length - 1];
      if (latestFill) {
        setFillFlash(latestFill);
        setTimeout(() => setFillFlash(null), 2500);
      }
    }
    prevFillCount = fills.length;
  });

  // Format P&L value
  const formatPnL = (n: number) => {
    const sign = n >= 0 ? "+" : "";
    return `${sign}${n.toFixed(2)}`;
  };

  const formatQty = (n: number) => {
    if (Math.abs(n) >= 1) return Math.abs(n).toFixed(4);
    return Math.abs(n).toPrecision(4);
  };

  return (
    <div class="relative h-full w-full bg-[#131722]">
      {/* Loading overlay */}
      <Show when={isLoading()}>
        <div class="absolute inset-0 z-10 flex items-center justify-center bg-[#131722]/80">
          <div class="text-muted-foreground">Loading...</div>
        </div>
      </Show>

      {/* Error overlay */}
      <Show when={error()}>
        <div class="absolute inset-0 z-10 flex items-center justify-center bg-[#131722]/80">
          <div class="text-destructive">{error()}</div>
        </div>
      </Show>

      {/* Legend */}
      <Show when={legendData()}>
        {(data) => (
          <div class="absolute left-3 top-3 z-10 rounded bg-[#1e222d]/90 px-3 py-2 text-xs pointer-events-none">
            <div class="text-sm font-semibold text-foreground mb-1">{data().symbol}</div>
            <div class="flex gap-3 text-muted-foreground font-mono">
              <span>
                <span class="text-muted-foreground/70">O</span>{" "}
                <span class="text-foreground">{formatPrice(data().open)}</span>
              </span>
              <span>
                <span class="text-muted-foreground/70">H</span>{" "}
                <span class="text-foreground">{formatPrice(data().high)}</span>
              </span>
              <span>
                <span class="text-muted-foreground/70">L</span>{" "}
                <span class="text-foreground">{formatPrice(data().low)}</span>
              </span>
              <span>
                <span class="text-muted-foreground/70">C</span>{" "}
                <span class="text-foreground">{formatPrice(data().close)}</span>
              </span>
              <span class={cn(data().change >= 0 ? "text-bid" : "text-ask")}>
                {data().change >= 0 ? "+" : ""}
                {formatPrice(data().change)} ({data().changePercent >= 0 ? "+" : ""}
                {data().changePercent.toFixed(2)}%)
              </span>
            </div>
            <div class="text-muted-foreground mt-1">
              Vol: {formatVolume(data().volume)}
            </div>
          </div>
        )}
      </Show>

      {/* Tooltip */}
      <Show when={tooltipData()}>
        {(data) => {
          // Create reactive position calculation
          const tooltipStyle = () => {
            const d = data();
            const containerWidth = chartContainer?.clientWidth ?? 800;
            const containerHeight = chartContainer?.clientHeight ?? 600;
            const tooltipWidth = 140;
            const tooltipHeight = 140;

            let left = d.x + 15;
            let top = d.y + 15;

            if (left + tooltipWidth > containerWidth) {
              left = d.x - tooltipWidth - 10;
            }
            if (top + tooltipHeight > containerHeight) {
              top = d.y - tooltipHeight - 10;
            }

            return { left: `${left}px`, top: `${top}px` };
          };

          // Tooltip displays the transformed time (which appears as local when read as UTC)
          // The chart stores transformed times, so we display them directly with UTC interpretation
          const dateStr = () => {
            const date = new Date(data().time * 1000);
            return date.toLocaleDateString("en-GB", { timeZone: "UTC" });
          };

          const timeStr = () => {
            const date = new Date(data().time * 1000);
            return date.toLocaleTimeString("en-GB", { timeZone: "UTC" });
          };

          // Show timezone indicator
          const tzLabel = () => getTimezoneOffsetLabel(getResolvedTimezone());

          return (
            <div
              class="absolute z-20 rounded border border-border bg-[#1e222d]/95 px-3 py-2 text-xs pointer-events-none shadow-lg"
              style={tooltipStyle()}
            >
              <div class="text-muted-foreground text-[10px] mb-2">
                {dateStr()} {timeStr()} <span class="text-primary/60">{tzLabel()}</span>
              </div>
              <div class="space-y-1 font-mono">
                <div class="flex justify-between gap-4">
                  <span class="text-muted-foreground">O:</span>
                  <span>{formatPrice(data().open)}</span>
                </div>
                <div class="flex justify-between gap-4">
                  <span class="text-muted-foreground">H:</span>
                  <span>{formatPrice(data().high)}</span>
                </div>
                <div class="flex justify-between gap-4">
                  <span class="text-muted-foreground">L:</span>
                  <span>{formatPrice(data().low)}</span>
                </div>
                <div class="flex justify-between gap-4">
                  <span class="text-muted-foreground">C:</span>
                  <span>{formatPrice(data().close)}</span>
                </div>
                <div class={cn("flex justify-between gap-4", data().change >= 0 ? "text-bid" : "text-ask")}>
                  <span>Chg:</span>
                  <span>
                    {data().changePercent >= 0 ? "+" : ""}
                    {data().changePercent.toFixed(2)}%
                  </span>
                </div>
                <div class="flex justify-between gap-4 text-muted-foreground border-t border-border pt-1 mt-1">
                  <span>Vol:</span>
                  <span>{formatVolume(data().volume)}</span>
                </div>
              </div>
            </div>
          );
        }}
      </Show>

      {/* P&L Overlay for Market Making */}
      <Show when={orderStore.position()}>
        {(pos) => {
          const position = pos();
          if (!position || position.quantity === 0) return null;
          return (
            <div class="absolute top-3 right-3 z-10 rounded bg-[#1e222d]/95 px-3 py-2 text-xs font-mono shadow-lg border border-border">
              <div class="flex items-center gap-3 mb-1">
                <span
                  class={cn(
                    "font-semibold",
                    position.quantity > 0 ? "text-green-500" : "text-red-500"
                  )}
                >
                  {position.quantity > 0 ? "LONG" : "SHORT"} {formatQty(position.quantity)}
                </span>
                <span class="text-muted-foreground">@</span>
                <span class="text-foreground">{fmtPrice(position.avg_entry_price)}</span>
                <span
                  class={cn(
                    "h-2 w-2 rounded-full",
                    ordersConnected() ? "bg-green-500" : "bg-red-500"
                  )}
                  title={ordersConnected() ? "Orders WS connected" : "Orders WS disconnected"}
                />
              </div>
              <div class="flex gap-3 text-[11px]">
                <span class="text-muted-foreground">Real:</span>
                <span class={position.realized_pnl >= 0 ? "text-green-500" : "text-red-500"}>
                  {formatPnL(position.realized_pnl)}
                </span>
                <span class="text-muted-foreground">Unreal:</span>
                <span class={position.unrealized_pnl >= 0 ? "text-green-500" : "text-red-500"}>
                  {formatPnL(position.unrealized_pnl)}
                </span>
                <span class="text-muted-foreground font-medium">Total:</span>
                <span
                  class={cn(
                    "font-bold",
                    position.realized_pnl + position.unrealized_pnl >= 0
                      ? "text-green-500"
                      : "text-red-500"
                  )}
                >
                  {formatPnL(position.realized_pnl + position.unrealized_pnl)}
                </span>
              </div>
            </div>
          );
        }}
      </Show>

      {/* Fill Flash Notification */}
      <Show when={fillFlash()}>
        {(fill) => (
          <div
            class={cn(
              "absolute top-16 right-3 z-20 px-4 py-2 rounded-lg shadow-lg",
              "border-2 text-sm font-mono animate-pulse",
              fill().side === "buy"
                ? "bg-green-900/90 border-green-500 text-green-100"
                : "bg-red-900/90 border-red-500 text-red-100"
            )}
          >
            <div class="font-bold">{fill().side.toUpperCase()} FILLED</div>
            <div>{fill().quantity.toFixed(4)} @ {fmtPrice(fill().price)}</div>
          </div>
        )}
      </Show>

      {/* Chart container */}
      <div ref={chartContainer} class="h-full w-full" />
    </div>
  );
};
