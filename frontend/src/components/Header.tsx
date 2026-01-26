import { Component, For, Show } from "solid-js";
import { cn } from "~/lib/utils";
import { ChartType } from "./Chart";
import { SymbolSearch } from "./SymbolSearch";
import { TimezoneSelector } from "./TimezoneSelector";

const INTERVALS = ["1m", "5m", "15m", "30m", "1h", "4h", "1d"];

const CHART_TYPE_OPTIONS: { type: ChartType; title: string; icon: string }[] = [
  {
    type: "candlestick",
    title: "Candles",
    icon: `<svg width="16" height="16" viewBox="0 0 16 16"><rect x="7" y="1" width="2" height="14" fill="currentColor"/><rect x="5" y="4" width="6" height="8" fill="currentColor"/></svg>`,
  },
  {
    type: "bar",
    title: "Bars",
    icon: `<svg width="16" height="16" viewBox="0 0 16 16"><path d="M4 2v12M4 5H2M4 11H6M10 4v8M10 4H8M10 10H12" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>`,
  },
  {
    type: "line",
    title: "Line",
    icon: `<svg width="16" height="16" viewBox="0 0 16 16"><path d="M1 12L5 6L9 9L15 3" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>`,
  },
  {
    type: "area",
    title: "Area",
    icon: `<svg width="16" height="16" viewBox="0 0 16 16"><path d="M1 12L5 6L9 9L15 3V14H1Z" fill="currentColor" opacity="0.3"/><path d="M1 12L5 6L9 9L15 3" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>`,
  },
  {
    type: "baseline",
    title: "Baseline",
    icon: `<svg width="16" height="16" viewBox="0 0 16 16"><line x1="1" y1="8" x2="15" y2="8" stroke="currentColor" stroke-dasharray="2 2"/><path d="M1 10L5 6L9 9L15 5" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>`,
  },
];

const SCALE_MODES = [
  { value: 0, label: "Normal" },
  { value: 1, label: "Log" },
  { value: 2, label: "%" },
  { value: 3, label: "Index" },
];

interface HeaderProps {
  symbol: string;
  interval: string;
  chartType: ChartType;
  scaleMode: number;
  volumeVisible: boolean;
  activeIndicatorCount: number;
  searchOpen: boolean;
  searchInitialChar?: string;
  onSearchOpenChange: (open: boolean) => void;
  onSymbolChange: (symbol: string) => void;
  onIntervalChange: (interval: string) => void;
  onChartTypeChange: (type: ChartType) => void;
  onScaleModeChange: (mode: number) => void;
  onGoLive: () => void;
  onToggleVolume: () => void;
  onOpenIndicatorDialog: () => void;
  onSymbolSelect?: (exchange: string, market: string, symbol: string) => void;
}

export const Header: Component<HeaderProps> = (props) => {
  const handleSymbolSelect = (exchange: string, market: string, symbol: string) => {
    props.onSearchOpenChange(false);
    // For now, just pass the symbol (existing WebSocket endpoints use symbol only)
    props.onSymbolChange(symbol);
    // If multi-exchange callback is provided, call it
    props.onSymbolSelect?.(exchange, market, symbol);
  };

  return (
    <header class="flex h-14 items-center justify-between border-b border-border bg-card px-4 gap-4 overflow-x-auto">
      {/* Logo / Title */}
      <div class="flex items-center gap-4 shrink-0">
        <h1 class="text-lg font-semibold">HFT Platform</h1>
      </div>

      {/* Controls */}
      <div class="flex items-center gap-2 flex-wrap">
        {/* Symbol Display with Search */}
        <div class="relative flex items-center gap-1">
          {/* Current Symbol Display */}
          <button
            onClick={() => props.onSearchOpenChange(true)}
            class={cn(
              "h-8 px-3 rounded-md border border-input bg-background",
              "hover:bg-muted transition-colors",
              "font-mono text-sm font-medium",
              "flex items-center gap-2"
            )}
            title="Search Symbols (just start typing)"
          >
            <span>{props.symbol}</span>
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" class="opacity-50">
              <circle cx="7" cy="7" r="4" />
              <path d="M10 10L14 14" />
            </svg>
          </button>

          {/* Symbol Search Modal */}
          <Show when={props.searchOpen}>
            <SymbolSearch
              onSelect={handleSymbolSelect}
              onClose={() => props.onSearchOpenChange(false)}
              initialValue={props.searchInitialChar}
            />
          </Show>
        </div>

        {/* Interval Selector */}
        <div class="flex items-center gap-0.5 rounded-md border border-input bg-background p-0.5">
          <For each={INTERVALS}>
            {(int) => (
              <button
                onClick={() => props.onIntervalChange(int)}
                class={cn(
                  "px-2 py-1 text-xs font-medium rounded transition-colors",
                  props.interval === int
                    ? "bg-primary text-primary-foreground"
                    : "hover:bg-muted text-muted-foreground"
                )}
              >
                {int}
              </button>
            )}
          </For>
        </div>

        {/* Go Live Button */}
        <button
          onClick={props.onGoLive}
          class={cn(
            "h-8 px-3 text-xs font-medium rounded-md border border-input",
            "bg-background hover:bg-muted transition-colors"
          )}
        >
          Go Live
        </button>

        {/* Separator */}
        <div class="w-px h-6 bg-border mx-1" />

        {/* Chart Type Buttons */}
        <div class="flex items-center gap-0.5 rounded-md border border-input bg-background p-0.5">
          <For each={CHART_TYPE_OPTIONS}>
            {(opt) => (
              <button
                onClick={() => props.onChartTypeChange(opt.type)}
                title={opt.title}
                class={cn(
                  "p-1.5 rounded transition-colors",
                  props.chartType === opt.type
                    ? "bg-primary text-primary-foreground"
                    : "hover:bg-muted text-muted-foreground"
                )}
                innerHTML={opt.icon}
              />
            )}
          </For>
        </div>

        {/* Separator */}
        <div class="w-px h-6 bg-border mx-1" />

        {/* Indicators Button */}
        <button
          onClick={props.onOpenIndicatorDialog}
          class={cn(
            "h-8 px-3 text-xs font-medium rounded-md border transition-colors",
            "bg-background border-input hover:bg-muted text-muted-foreground",
            "flex items-center gap-1.5"
          )}
          title="Indicators"
        >
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M2 12L5 6L9 9L14 4" stroke-linecap="round" stroke-linejoin="round" />
            <circle cx="5" cy="6" r="1.5" fill="currentColor" stroke="none" />
            <circle cx="9" cy="9" r="1.5" fill="currentColor" stroke="none" />
            <circle cx="14" cy="4" r="1.5" fill="currentColor" stroke="none" />
          </svg>
          Indicators
          <Show when={props.activeIndicatorCount > 0}>
            <span class="ml-0.5 px-1.5 py-0.5 text-[10px] font-semibold bg-primary text-primary-foreground rounded-full">
              {props.activeIndicatorCount}
            </span>
          </Show>
        </button>

        {/* Quick Toggle Indicator Buttons */}
        <button
          onClick={props.onToggleVolume}
          class={cn(
            "h-8 px-2 text-xs font-medium rounded-md border transition-colors",
            props.volumeVisible
              ? "bg-primary text-primary-foreground border-primary"
              : "bg-background border-input hover:bg-muted text-muted-foreground"
          )}
          title="Volume"
        >
          Vol
        </button>

        {/* Separator */}
        <div class="w-px h-6 bg-border mx-1" />

        {/* Scale Mode */}
        <select
          value={props.scaleMode}
          onChange={(e) => props.onScaleModeChange(parseInt(e.currentTarget.value))}
          class={cn(
            "h-8 rounded-md border border-input bg-background px-2 py-1 text-xs",
            "focus:outline-none focus:ring-1 focus:ring-ring"
          )}
          title="Price Scale Mode"
        >
          <For each={SCALE_MODES}>
            {(mode) => (
              <option value={mode.value} selected={mode.value === props.scaleMode}>
                {mode.label}
              </option>
            )}
          </For>
        </select>

        {/* Separator */}
        <div class="w-px h-6 bg-border mx-1" />

        {/* Timezone Selector */}
        <TimezoneSelector symbol={props.symbol} />
      </div>
    </header>
  );
};
