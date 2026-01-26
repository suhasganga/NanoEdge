import { createSignal, createEffect, onMount } from "solid-js";
import { Header } from "./components/Header";
import { Chart, ChartApi, ChartType } from "./components/Chart";
import { TradingSidebar } from "./components/TradingSidebar";
import { ChartContextMenu } from "./components/ChartContextMenu";
import { SettingsDialog } from "./components/SettingsDialog";
import { BarCountdown } from "./components/BarCountdown";
import { IndicatorDialog } from "./components/IndicatorDialog";
import { useKeyboardShortcuts } from "./hooks/useKeyboardShortcuts";
import { useGlobalSearch } from "./hooks/useGlobalSearch";
import { settings, updateSetting } from "./stores/chartSettings";
import { useDynamicSubscription } from "./hooks/useDynamicWebSocket";
import {
  indicators,
  addIndicator,
  removeIndicator,
  toggleIndicator,
  getVisibleIndicators,
  type IndicatorConfig,
} from "./stores/indicatorStore";

export default function App() {
  const [symbol, setSymbol] = createSignal("BTCUSDT");
  const [exchange, setExchange] = createSignal("binance");
  const [market, setMarket] = createSignal("spot");
  const [interval, setInterval] = createSignal("1m");
  const [chartType, setChartType] = createSignal<ChartType>("candlestick");
  const [volumeVisible, setVolumeVisible] = createSignal(true);
  const [settingsOpen, setSettingsOpen] = createSignal(false);
  const [searchOpen, setSearchOpen] = createSignal(false);
  const [searchInitialChar, setSearchInitialChar] = createSignal<string | undefined>();
  const [indicatorDialogOpen, setIndicatorDialogOpen] = createSignal(false);

  // Count visible indicators
  const activeIndicatorCount = () => getVisibleIndicators().length;

  let chartApi: ChartApi | undefined;

  // Dynamic subscription for multi-exchange support
  // This ensures infrastructure is set up for new symbols
  const { subscribe: subscribeToSymbol } = useDynamicSubscription();

  // Subscribe to default symbol on mount (only once, not on every signal change)
  onMount(() => {
    subscribeToSymbol(exchange(), market(), symbol());
  });

  // Use keyboard shortcuts
  useKeyboardShortcuts({
    onOpenSettings: () => setSettingsOpen(true),
    onCloseSettings: () => setSettingsOpen(false),
  });

  // Global keyboard search - TradingView-style
  useGlobalSearch({
    isOpen: searchOpen,
    onOpen: (char) => {
      setSearchInitialChar(char);
      setSearchOpen(true);
    },
  });

  // Sync scale mode from settings store
  const scaleMode = () => settings().scaleMode;

  const handleChartReady = (api: ChartApi) => {
    chartApi = api;
    // Sync indicators from store to chart
    api.syncIndicators(indicators());
  };

  // Sync indicators to chart when store changes
  createEffect(() => {
    const inds = indicators();
    chartApi?.syncIndicators(inds);
  });

  const handleChartTypeChange = (type: ChartType) => {
    setChartType(type);
    chartApi?.setChartType(type);
  };

  const handleScaleModeChange = (mode: number) => {
    updateSetting("scaleMode", mode as 0 | 1 | 2 | 3);
    // Chart will update via settings effect
  };

  const handleOpenSettings = () => {
    setSettingsOpen(true);
  };

  const handleGoLive = () => {
    chartApi?.scrollToRealtime();
  };

  const handleToggleVolume = () => {
    const newVisible = chartApi?.toggleVolume() ?? !volumeVisible();
    setVolumeVisible(newVisible);
  };

  // Indicator dialog handlers
  const handleAddIndicator = (config: IndicatorConfig) => {
    addIndicator(config);
  };

  const handleRemoveIndicator = (id: string) => {
    removeIndicator(id);
  };

  const handleToggleIndicatorVisibility = (id: string) => {
    toggleIndicator(id);
  };

  // Handle symbol selection from search (multi-exchange)
  const handleSymbolSelect = (ex: string, mkt: string, sym: string) => {
    setExchange(ex);
    setMarket(mkt);
    setSymbol(sym);
    // Subscribe triggers infrastructure setup on backend
    subscribeToSymbol(ex, mkt, sym);
  };

  // Handle symbol change from dropdown
  const handleSymbolChange = (sym: string) => {
    setSymbol(sym);
    // Detect exchange from symbol format:
    // - NSE:*-EQ, NSE:*-INDEX, MCX:* → Fyers
    // - Everything else → Binance spot
    if (sym.startsWith("NSE:") || sym.startsWith("MCX:") || sym.startsWith("BSE:")) {
      const mkt = sym.includes("-EQ")
        ? "equity"
        : sym.includes("-INDEX")
          ? "index"
          : sym.startsWith("MCX:")
            ? "commodity"
            : "futures";
      setExchange("fyers");
      setMarket(mkt);
      subscribeToSymbol("fyers", mkt, sym);
    } else {
      setExchange("binance");
      setMarket("spot");
      subscribeToSymbol("binance", "spot", sym);
    }
  };

  return (
    <div class="flex h-screen flex-col bg-background text-foreground">
      {/* Header */}
      <Header
        symbol={symbol()}
        interval={interval()}
        chartType={chartType()}
        scaleMode={scaleMode()}
        volumeVisible={volumeVisible()}
        activeIndicatorCount={activeIndicatorCount()}
        searchOpen={searchOpen()}
        searchInitialChar={searchInitialChar()}
        onSearchOpenChange={setSearchOpen}
        onSymbolChange={handleSymbolChange}
        onIntervalChange={setInterval}
        onChartTypeChange={handleChartTypeChange}
        onScaleModeChange={handleScaleModeChange}
        onGoLive={handleGoLive}
        onToggleVolume={handleToggleVolume}
        onOpenIndicatorDialog={() => setIndicatorDialogOpen(true)}
        onSymbolSelect={handleSymbolSelect}
      />

      {/* Main content */}
      <div class="flex flex-1 overflow-hidden">
        {/* Chart with context menu */}
        <div class="flex-1 min-w-0 relative">
          <ChartContextMenu onOpenSettings={handleOpenSettings}>
            <Chart
              symbol={symbol()}
              interval={interval()}
              chartType={chartType()}
              onReady={handleChartReady}
            />
          </ChartContextMenu>

          {/* Bar countdown timer */}
          <BarCountdown
            interval={interval()}
            visible={settings().showBarCountdown}
          />
        </div>

        {/* Trading Sidebar - hidden on mobile */}
        <div class="hidden lg:block w-80 border-l border-border">
          <TradingSidebar symbol={symbol()} />
        </div>
      </div>

      {/* Settings Dialog */}
      <SettingsDialog
        open={settingsOpen()}
        onOpenChange={setSettingsOpen}
      />

      {/* Indicator Dialog */}
      <IndicatorDialog
        open={indicatorDialogOpen()}
        onOpenChange={setIndicatorDialogOpen}
        activeIndicators={indicators()}
        onAddIndicator={handleAddIndicator}
        onRemoveIndicator={handleRemoveIndicator}
        onToggleIndicator={handleToggleIndicatorVisibility}
      />
    </div>
  );
}
