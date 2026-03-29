import { createSignal, createEffect, createRoot } from "solid-js";

/**
 * Chart Settings Store
 *
 * Manages all chart configuration with localStorage persistence.
 * Settings are reactive and automatically sync to localStorage.
 */

// Price scale modes (from TradingView Lightweight Charts)
export const PriceScaleMode = {
  Normal: 0,
  Logarithmic: 1,
  Percentage: 2,
  IndexedTo100: 3,
} as const;

export type PriceScaleMode = (typeof PriceScaleMode)[keyof typeof PriceScaleMode];

// Crosshair modes
export const CrosshairMode = {
  Normal: 0,
  Magnet: 1,
} as const;

export type CrosshairMode = (typeof CrosshairMode)[keyof typeof CrosshairMode];

// Full settings interface
export interface ChartSettings {
  // Scale settings
  scaleMode: PriceScaleMode;
  invertScale: boolean;
  autoScale: boolean;
  lockPriceToBarRatio: boolean;
  priceToBarRatio: number;
  priceScalePosition: "left" | "right";

  // Candle colors
  candleUpColor: string;
  candleDownColor: string;
  wickUpColor: string;
  wickDownColor: string;
  borderUpColor: string;
  borderDownColor: string;
  borderVisible: boolean;

  // Grid settings
  gridVerticalVisible: boolean;
  gridHorizontalVisible: boolean;
  gridVerticalColor: string;
  gridHorizontalColor: string;

  // Crosshair settings
  crosshairMode: CrosshairMode;
  crosshairColor: string;
  crosshairLabelBackground: string;

  // Price labels & lines
  showLastPriceLine: boolean;
  showPrevDayClose: boolean;
  prevDayClosePrice: number | null;
  showHighLowLines: boolean;
  highPrice: number | null;
  lowPrice: number | null;
  showBidAskLines: boolean;

  // Time scale
  showBarCountdown: boolean;
  timeVisible: boolean;
  secondsVisible: boolean;
  timezone: string; // IANA timezone ID, "UTC", or "EXCHANGE"

  // Legend/Status line
  showLegend: boolean;
  legendPosition: "top-left" | "top-right" | "bottom-left" | "bottom-right";
}

// Default settings
export const DEFAULT_SETTINGS: ChartSettings = {
  // Scale settings
  scaleMode: PriceScaleMode.Normal,
  invertScale: false,
  autoScale: true,
  lockPriceToBarRatio: false,
  priceToBarRatio: 1,
  priceScalePosition: "right",

  // Candle colors (TradingView defaults)
  candleUpColor: "#26a69a",
  candleDownColor: "#ef5350",
  wickUpColor: "#26a69a",
  wickDownColor: "#ef5350",
  borderUpColor: "#26a69a",
  borderDownColor: "#ef5350",
  borderVisible: false,

  // Grid settings
  gridVerticalVisible: true,
  gridHorizontalVisible: true,
  gridVerticalColor: "#1e222d",
  gridHorizontalColor: "#1e222d",

  // Crosshair settings
  crosshairMode: CrosshairMode.Magnet,
  crosshairColor: "#758696",
  crosshairLabelBackground: "#131722",

  // Price labels & lines
  showLastPriceLine: true,
  showPrevDayClose: false,
  prevDayClosePrice: null,
  showHighLowLines: false,
  highPrice: null,
  lowPrice: null,
  showBidAskLines: false,

  // Time scale
  showBarCountdown: false,
  timeVisible: true,
  secondsVisible: true,
  timezone: "EXCHANGE", // Default to exchange timezone

  // Legend/Status line
  showLegend: true,
  legendPosition: "top-left",
};

const STORAGE_KEY = "nanoedge-chart-settings";

// Load settings from localStorage
function loadSettings(): ChartSettings {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      const parsed = JSON.parse(stored);
      // Merge with defaults to handle new settings added in updates
      return { ...DEFAULT_SETTINGS, ...parsed };
    }
  } catch (e) {
    console.warn("Failed to load chart settings from localStorage:", e);
  }
  return DEFAULT_SETTINGS;
}

// Save settings to localStorage
function saveSettings(settings: ChartSettings): void {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
  } catch (e) {
    console.warn("Failed to save chart settings to localStorage:", e);
  }
}

// Create the store (singleton pattern with createRoot for SSR safety)
function createChartSettingsStore() {
  const [settings, setSettings] = createSignal<ChartSettings>(loadSettings());

  // Auto-save to localStorage when settings change
  createEffect(() => {
    saveSettings(settings());
  });

  // Update a single setting
  const updateSetting = <K extends keyof ChartSettings>(
    key: K,
    value: ChartSettings[K]
  ) => {
    setSettings((prev) => ({ ...prev, [key]: value }));
  };

  // Update multiple settings at once
  const updateSettings = (partial: Partial<ChartSettings>) => {
    setSettings((prev) => ({ ...prev, ...partial }));
  };

  // Reset all settings to defaults
  const resetToDefaults = () => {
    setSettings(DEFAULT_SETTINGS);
  };

  // Reset a specific category
  const resetCategory = (category: "scale" | "candle" | "grid" | "crosshair" | "lines" | "time" | "legend") => {
    const categoryDefaults: Partial<ChartSettings> = {};

    switch (category) {
      case "scale":
        Object.assign(categoryDefaults, {
          scaleMode: DEFAULT_SETTINGS.scaleMode,
          invertScale: DEFAULT_SETTINGS.invertScale,
          autoScale: DEFAULT_SETTINGS.autoScale,
          lockPriceToBarRatio: DEFAULT_SETTINGS.lockPriceToBarRatio,
          priceToBarRatio: DEFAULT_SETTINGS.priceToBarRatio,
          priceScalePosition: DEFAULT_SETTINGS.priceScalePosition,
        });
        break;
      case "candle":
        Object.assign(categoryDefaults, {
          candleUpColor: DEFAULT_SETTINGS.candleUpColor,
          candleDownColor: DEFAULT_SETTINGS.candleDownColor,
          wickUpColor: DEFAULT_SETTINGS.wickUpColor,
          wickDownColor: DEFAULT_SETTINGS.wickDownColor,
          borderUpColor: DEFAULT_SETTINGS.borderUpColor,
          borderDownColor: DEFAULT_SETTINGS.borderDownColor,
          borderVisible: DEFAULT_SETTINGS.borderVisible,
        });
        break;
      case "grid":
        Object.assign(categoryDefaults, {
          gridVerticalVisible: DEFAULT_SETTINGS.gridVerticalVisible,
          gridHorizontalVisible: DEFAULT_SETTINGS.gridHorizontalVisible,
          gridVerticalColor: DEFAULT_SETTINGS.gridVerticalColor,
          gridHorizontalColor: DEFAULT_SETTINGS.gridHorizontalColor,
        });
        break;
      case "crosshair":
        Object.assign(categoryDefaults, {
          crosshairMode: DEFAULT_SETTINGS.crosshairMode,
          crosshairColor: DEFAULT_SETTINGS.crosshairColor,
          crosshairLabelBackground: DEFAULT_SETTINGS.crosshairLabelBackground,
        });
        break;
      case "lines":
        Object.assign(categoryDefaults, {
          showLastPriceLine: DEFAULT_SETTINGS.showLastPriceLine,
          showPrevDayClose: DEFAULT_SETTINGS.showPrevDayClose,
          showHighLowLines: DEFAULT_SETTINGS.showHighLowLines,
          showBidAskLines: DEFAULT_SETTINGS.showBidAskLines,
        });
        break;
      case "time":
        Object.assign(categoryDefaults, {
          showBarCountdown: DEFAULT_SETTINGS.showBarCountdown,
          timeVisible: DEFAULT_SETTINGS.timeVisible,
          secondsVisible: DEFAULT_SETTINGS.secondsVisible,
          timezone: DEFAULT_SETTINGS.timezone,
        });
        break;
      case "legend":
        Object.assign(categoryDefaults, {
          showLegend: DEFAULT_SETTINGS.showLegend,
          legendPosition: DEFAULT_SETTINGS.legendPosition,
        });
        break;
    }

    setSettings((prev) => ({ ...prev, ...categoryDefaults }));
  };

  return {
    // Reactive getter
    settings,

    // Setters
    updateSetting,
    updateSettings,
    setSettings,

    // Reset functions
    resetToDefaults,
    resetCategory,
  };
}

// Export singleton store
export const chartSettingsStore = createRoot(createChartSettingsStore);

// Convenience exports
export const { settings, updateSetting, updateSettings, resetToDefaults, resetCategory } =
  chartSettingsStore;
