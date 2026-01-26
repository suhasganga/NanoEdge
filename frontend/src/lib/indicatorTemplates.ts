/**
 * Indicator Templates
 *
 * Defines available indicator types, their defaults, and configuration options.
 * Used by the IndicatorDialog for displaying and configuring indicators.
 */

import type { IndicatorType } from "~/stores/indicatorStore";

export type IndicatorCategory = "trend" | "momentum" | "volatility" | "volume";

export interface IndicatorTemplate {
  type: IndicatorType;
  name: string;
  shortName: string;
  description: string;
  defaultPeriod: number;
  defaultColor: string;
  minPeriod: number;
  maxPeriod: number;
  category: IndicatorCategory;
  hasStdDev?: boolean;
  defaultStdDev?: number;
  icon?: string; // SVG path or component name
}

/**
 * Available indicator templates
 */
export const INDICATOR_TEMPLATES: IndicatorTemplate[] = [
  // Trend Indicators
  {
    type: "sma",
    name: "Simple Moving Average",
    shortName: "SMA",
    description: "Calculates the arithmetic mean of prices over a specified period",
    defaultPeriod: 20,
    defaultColor: "#2962FF",
    minPeriod: 1,
    maxPeriod: 500,
    category: "trend",
  },
  {
    type: "ema",
    name: "Exponential Moving Average",
    shortName: "EMA",
    description: "Weighted moving average giving more importance to recent prices",
    defaultPeriod: 20,
    defaultColor: "#FF6D00",
    minPeriod: 1,
    maxPeriod: 500,
    category: "trend",
  },

  // Volatility Indicators
  {
    type: "bollinger",
    name: "Bollinger Bands",
    shortName: "BB",
    description: "Volatility bands placed above and below a moving average",
    defaultPeriod: 20,
    defaultColor: "#26a69a",
    minPeriod: 2,
    maxPeriod: 200,
    category: "volatility",
    hasStdDev: true,
    defaultStdDev: 2,
  },
];

/**
 * Color palette for indicators (TradingView-inspired)
 */
export const INDICATOR_COLORS = [
  "#2962FF", // Blue
  "#FF6D00", // Orange
  "#00E676", // Green
  "#FF1744", // Red
  "#7B1FA2", // Purple
  "#00BCD4", // Cyan
  "#FFEB3B", // Yellow
  "#E91E63", // Pink
  "#009688", // Teal
  "#795548", // Brown
  "#607D8B", // Blue Grey
  "#9C27B0", // Deep Purple
] as const;

/**
 * Get a unique color for a new indicator (cycles through palette)
 */
export function getNextIndicatorColor(existingColors: string[]): string {
  for (const color of INDICATOR_COLORS) {
    if (!existingColors.includes(color)) {
      return color;
    }
  }
  // If all colors used, return a random one
  return INDICATOR_COLORS[Math.floor(Math.random() * INDICATOR_COLORS.length)];
}

/**
 * Get template by type
 */
export function getIndicatorTemplate(type: IndicatorType): IndicatorTemplate | undefined {
  return INDICATOR_TEMPLATES.find((t) => t.type === type);
}

/**
 * Get templates by category
 */
export function getTemplatesByCategory(category: IndicatorCategory): IndicatorTemplate[] {
  return INDICATOR_TEMPLATES.filter((t) => t.category === category);
}

/**
 * Search templates by name/description
 */
export function searchTemplates(query: string): IndicatorTemplate[] {
  const lowerQuery = query.toLowerCase();
  return INDICATOR_TEMPLATES.filter(
    (t) =>
      t.name.toLowerCase().includes(lowerQuery) ||
      t.shortName.toLowerCase().includes(lowerQuery) ||
      t.description.toLowerCase().includes(lowerQuery)
  );
}

/**
 * Format indicator label for display (e.g., "SMA 20", "BB 20, 2")
 */
export function formatIndicatorLabel(
  type: IndicatorType,
  period: number,
  params?: { stdDev?: number }
): string {
  const template = getIndicatorTemplate(type);
  if (!template) return `${type.toUpperCase()} ${period}`;

  if (type === "bollinger" && params?.stdDev) {
    return `${template.shortName} ${period}, ${params.stdDev}`;
  }
  return `${template.shortName} ${period}`;
}

/**
 * Category metadata for filtering UI
 */
export const INDICATOR_CATEGORIES: {
  id: IndicatorCategory | "all";
  label: string;
}[] = [
  { id: "all", label: "All" },
  { id: "trend", label: "Trend" },
  { id: "volatility", label: "Volatility" },
  // Future categories
  // { id: "momentum", label: "Momentum" },
  // { id: "volume", label: "Volume" },
];
