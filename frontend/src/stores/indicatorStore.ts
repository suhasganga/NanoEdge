import { createSignal, createEffect, createRoot } from "solid-js";

/**
 * Indicator Store
 *
 * Manages dynamic indicator configurations with localStorage persistence.
 * Supports multiple instances of the same indicator type with different parameters.
 */

export type IndicatorType = "sma" | "ema" | "bollinger";

export interface IndicatorConfig {
  id: string; // Unique ID: e.g., "sma_29_abc123"
  type: IndicatorType;
  period: number;
  color: string;
  visible: boolean;
  params?: {
    stdDev?: number; // For Bollinger Bands
  };
}

// Preset indicator IDs for quick-toggle buttons
export const PRESET_IDS = {
  SMA_20: "sma_20_preset",
  SMA_50: "sma_50_preset",
  EMA_12: "ema_12_preset",
  EMA_26: "ema_26_preset",
  BOLLINGER: "bollinger_20_preset",
} as const;

const STORAGE_KEY = "nanoedge-indicators";

// Generate unique ID for new indicators
export function generateIndicatorId(type: IndicatorType, period: number): string {
  const random = Math.random().toString(36).substring(2, 8);
  return `${type}_${period}_${random}`;
}

// Default preset indicators (created on first load)
function getDefaultIndicators(): IndicatorConfig[] {
  return [
    {
      id: PRESET_IDS.SMA_20,
      type: "sma",
      period: 20,
      color: "#2962FF",
      visible: false,
    },
    {
      id: PRESET_IDS.SMA_50,
      type: "sma",
      period: 50,
      color: "#FF6D00",
      visible: false,
    },
    {
      id: PRESET_IDS.EMA_12,
      type: "ema",
      period: 12,
      color: "#00E676",
      visible: false,
    },
    {
      id: PRESET_IDS.EMA_26,
      type: "ema",
      period: 26,
      color: "#FF1744",
      visible: false,
    },
    {
      id: PRESET_IDS.BOLLINGER,
      type: "bollinger",
      period: 20,
      color: "#26a69a",
      visible: false,
      params: { stdDev: 2 },
    },
  ];
}

// Load indicators from localStorage
function loadIndicators(): IndicatorConfig[] {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      const parsed = JSON.parse(stored) as IndicatorConfig[];
      // Validate and return
      if (Array.isArray(parsed) && parsed.every((i) => i.id && i.type && i.period)) {
        return parsed;
      }
    }
  } catch (e) {
    console.warn("Failed to load indicators from localStorage:", e);
  }
  return getDefaultIndicators();
}

// Save indicators to localStorage
function saveIndicators(indicators: IndicatorConfig[]): void {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(indicators));
  } catch (e) {
    console.warn("Failed to save indicators to localStorage:", e);
  }
}

// Create the store (singleton pattern with createRoot for SSR safety)
function createIndicatorStore() {
  const [indicators, setIndicators] = createSignal<IndicatorConfig[]>(loadIndicators());

  // Auto-save to localStorage when indicators change
  createEffect(() => {
    saveIndicators(indicators());
  });

  // Add a new indicator
  const addIndicator = (config: Omit<IndicatorConfig, "id"> & { id?: string }): string => {
    const id = config.id || generateIndicatorId(config.type, config.period);
    const newIndicator: IndicatorConfig = {
      ...config,
      id,
      visible: config.visible ?? true,
    };
    setIndicators((prev) => [...prev, newIndicator]);
    return id;
  };

  // Remove an indicator by ID
  const removeIndicator = (id: string): void => {
    setIndicators((prev) => prev.filter((i) => i.id !== id));
  };

  // Toggle indicator visibility
  const toggleIndicator = (id: string): boolean => {
    let newVisible = false;
    setIndicators((prev) =>
      prev.map((i) => {
        if (i.id === id) {
          newVisible = !i.visible;
          return { ...i, visible: newVisible };
        }
        return i;
      })
    );
    return newVisible;
  };

  // Update indicator config
  const updateIndicator = (id: string, partial: Partial<Omit<IndicatorConfig, "id">>): void => {
    setIndicators((prev) =>
      prev.map((i) => (i.id === id ? { ...i, ...partial } : i))
    );
  };

  // Get indicator by ID
  const getIndicator = (id: string): IndicatorConfig | undefined => {
    return indicators().find((i) => i.id === id);
  };

  // Get indicators by type
  const getIndicatorsByType = (type: IndicatorType): IndicatorConfig[] => {
    return indicators().filter((i) => i.type === type);
  };

  // Get visible indicators
  const getVisibleIndicators = (): IndicatorConfig[] => {
    return indicators().filter((i) => i.visible);
  };

  // Check if indicator exists
  const hasIndicator = (id: string): boolean => {
    return indicators().some((i) => i.id === id);
  };

  // Find or create preset indicator (for quick-toggle buttons)
  const findOrCreatePreset = (presetId: string, defaults: Omit<IndicatorConfig, "id">): IndicatorConfig => {
    const existing = getIndicator(presetId);
    if (existing) return existing;

    // Create the preset
    addIndicator({ ...defaults, id: presetId, visible: false });
    return getIndicator(presetId)!;
  };

  // Reset to defaults
  const resetToDefaults = (): void => {
    setIndicators(getDefaultIndicators());
  };

  return {
    // Reactive getter
    indicators,

    // CRUD operations
    addIndicator,
    removeIndicator,
    toggleIndicator,
    updateIndicator,

    // Queries
    getIndicator,
    getIndicatorsByType,
    getVisibleIndicators,
    hasIndicator,
    findOrCreatePreset,

    // Reset
    resetToDefaults,
  };
}

// Export singleton store
export const indicatorStore = createRoot(createIndicatorStore);

// Convenience exports
export const {
  indicators,
  addIndicator,
  removeIndicator,
  toggleIndicator,
  updateIndicator,
  getIndicator,
  getIndicatorsByType,
  getVisibleIndicators,
  hasIndicator,
  findOrCreatePreset,
  resetToDefaults,
} = indicatorStore;
