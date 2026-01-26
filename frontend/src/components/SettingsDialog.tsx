import { Component, Show, createSignal } from "solid-js";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  Button,
} from "./ui/Dialog";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "./ui/Tabs";
import { Checkbox } from "./ui/Checkbox";
import {
  settings,
  updateSetting,
  resetToDefaults,
  PriceScaleMode,
  CrosshairMode,
  type ChartSettings,
} from "~/stores/chartSettings";

/**
 * SettingsDialog
 *
 * TradingView-style settings dialog with tabbed navigation.
 * Provides comprehensive chart customization options.
 */

interface SettingsDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

// Tab icons (matching TradingView)
const SymbolIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="20" height="20" fill="currentColor">
    <path fill-rule="evenodd" d="M11 4h-1v3H8.5a.5.5 0 0 0-.5.5v13a.5.5 0 0 0 .5.5H10v3h1v-3h1.5a.5.5 0 0 0 .5-.5v-13a.5.5 0 0 0-.5-.5H11V4ZM9 8v12h3V8H9Zm10-1h-1v3h-1.5a.5.5 0 0 0-.5.5v7a.5.5 0 0 0 .5.5H18v3h1v-3h1.5a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5H19V7Zm-2 10v-6h3v6h-3Z" />
  </svg>
);

const ScalesIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="20" height="20" fill="none">
    <path stroke="currentColor" stroke-width="1.5" d="M10.5 20.5a2 2 0 1 1-2-2m2 2a2 2 0 0 0-2-2m2 2h14m-16-2v-14m16 16L21 17m3.5 3.5L21 24M8.5 4.5 12 8M8.5 4.5 5 8" />
  </svg>
);

const CanvasIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="20" height="20" fill="currentColor">
    <path d="M16.73 6.56a2.5 2.5 0 0 1 3.54 0l1.17 1.17a2.5 2.5 0 0 1 0 3.54l-.59.58-9 9-1 1-.14.15H6v-4.7l.15-.15 1-1 9-9 .58-.59Zm2.83.7a1.5 1.5 0 0 0-2.12 0l-.23.24 3.29 3.3.23-.24a1.5 1.5 0 0 0 0-2.12l-1.17-1.17Zm.23 4.24L16.5 8.2l-8.3 8.3 3.3 3.3 8.3-8.3Zm-9 9L7.5 17.2l-.5.5V21h3.3l.5-.5Z" />
  </svg>
);

const StatusLineIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="20" height="20" fill="currentColor">
    <path fill-rule="evenodd" d="M7 7h14a1 1 0 1 1 0 2H7a1 1 0 0 1 0-2ZM5 8c0-1.1.9-2 2-2h14a2 2 0 1 1 0 4H7a2 2 0 0 1-2-2Zm13 5H6v1h12v-1Zm0 4H6v1h12v-1ZM6 21h12v1H6v-1Z" />
  </svg>
);

// Color picker component
interface ColorPickerProps {
  value: string;
  onChange: (color: string) => void;
  label?: string;
}

const ColorPicker: Component<ColorPickerProps> = (props) => {
  return (
    <div class="flex items-center gap-2">
      <Show when={props.label}>
        <span class="text-[13px] text-[#787b86] min-w-[80px]">{props.label}</span>
      </Show>
      <label class="relative">
        <input
          type="color"
          value={props.value}
          onInput={(e) => props.onChange(e.currentTarget.value)}
          class="absolute inset-0 opacity-0 cursor-pointer w-full h-full"
        />
        <div
          class="w-6 h-6 rounded border border-[#363a45] cursor-pointer"
          style={{ "background-color": props.value }}
        />
      </label>
    </div>
  );
};

// Section component
interface SectionProps {
  title: string;
  children: any;
}

const Section: Component<SectionProps> = (props) => (
  <div class="mb-6">
    <h3 class="text-[13px] font-medium text-[#d1d4dc] mb-3">{props.title}</h3>
    <div class="space-y-3">{props.children}</div>
  </div>
);

// Row component for settings
interface RowProps {
  label: string;
  children: any;
}

const Row: Component<RowProps> = (props) => (
  <div class="flex items-center justify-between">
    <span class="text-[13px] text-[#787b86]">{props.label}</span>
    {props.children}
  </div>
);

export const SettingsDialog: Component<SettingsDialogProps> = (props) => {
  const [activeTab, setActiveTab] = createSignal("symbol");
  const currentSettings = settings;

  const handleClose = () => {
    props.onOpenChange(false);
  };

  const handleReset = () => {
    resetToDefaults();
  };

  return (
    <Dialog.Root open={props.open} onOpenChange={props.onOpenChange}>
      <DialogContent class="max-w-[700px] h-[600px] flex flex-col">
        <DialogHeader>
          <DialogTitle>Settings</DialogTitle>
        </DialogHeader>

        <div class="flex flex-1 overflow-hidden">
          {/* Sidebar tabs */}
          <Tabs.Root
            value={activeTab()}
            onChange={setActiveTab}
            orientation="vertical"
            class="flex flex-1"
          >
            <TabsList class="w-[180px] bg-[#131722] border-r border-[#2a2e39]">
              <TabsTrigger value="symbol" icon={<SymbolIcon />}>
                Symbol
              </TabsTrigger>
              <TabsTrigger value="scales" icon={<ScalesIcon />}>
                Scales & Lines
              </TabsTrigger>
              <TabsTrigger value="canvas" icon={<CanvasIcon />}>
                Canvas
              </TabsTrigger>
              <TabsTrigger value="status" icon={<StatusLineIcon />}>
                Status Line
              </TabsTrigger>
            </TabsList>

            {/* Symbol Tab */}
            <TabsContent value="symbol" class="flex-1 p-4 overflow-y-auto">
              <Section title="Candle Body">
                <Row label="Up color">
                  <ColorPicker
                    value={currentSettings().candleUpColor}
                    onChange={(c) => updateSetting("candleUpColor", c)}
                  />
                </Row>
                <Row label="Down color">
                  <ColorPicker
                    value={currentSettings().candleDownColor}
                    onChange={(c) => updateSetting("candleDownColor", c)}
                  />
                </Row>
              </Section>

              <Section title="Candle Wick">
                <Row label="Up color">
                  <ColorPicker
                    value={currentSettings().wickUpColor}
                    onChange={(c) => updateSetting("wickUpColor", c)}
                  />
                </Row>
                <Row label="Down color">
                  <ColorPicker
                    value={currentSettings().wickDownColor}
                    onChange={(c) => updateSetting("wickDownColor", c)}
                  />
                </Row>
              </Section>

              <Section title="Candle Border">
                <Checkbox
                  checked={currentSettings().borderVisible}
                  onChange={(c) => updateSetting("borderVisible", c)}
                  label="Show border"
                />
                <Show when={currentSettings().borderVisible}>
                  <Row label="Up color">
                    <ColorPicker
                      value={currentSettings().borderUpColor}
                      onChange={(c) => updateSetting("borderUpColor", c)}
                    />
                  </Row>
                  <Row label="Down color">
                    <ColorPicker
                      value={currentSettings().borderDownColor}
                      onChange={(c) => updateSetting("borderDownColor", c)}
                    />
                  </Row>
                </Show>
              </Section>
            </TabsContent>

            {/* Scales & Lines Tab */}
            <TabsContent value="scales" class="flex-1 p-4 overflow-y-auto">
              <Section title="Price Scale">
                <Row label="Position">
                  <select
                    value={currentSettings().priceScalePosition}
                    onChange={(e) =>
                      updateSetting(
                        "priceScalePosition",
                        e.currentTarget.value as "left" | "right"
                      )
                    }
                    class="bg-[#2a2e39] text-[#d1d4dc] text-[13px] px-2 py-1 rounded border border-[#363a45] outline-none"
                  >
                    <option value="right">Right</option>
                    <option value="left">Left</option>
                  </select>
                </Row>
                <Row label="Scale mode">
                  <select
                    value={String(currentSettings().scaleMode)}
                    onChange={(e) =>
                      updateSetting("scaleMode", parseInt(e.currentTarget.value) as PriceScaleMode)
                    }
                    class="bg-[#2a2e39] text-[#d1d4dc] text-[13px] px-2 py-1 rounded border border-[#363a45] outline-none"
                  >
                    <option value="0">Regular</option>
                    <option value="1">Logarithmic</option>
                    <option value="2">Percentage</option>
                    <option value="3">Indexed to 100</option>
                  </select>
                </Row>
                <Checkbox
                  checked={currentSettings().autoScale}
                  onChange={(c) => updateSetting("autoScale", c)}
                  label="Auto scale"
                />
                <Checkbox
                  checked={currentSettings().invertScale}
                  onChange={(c) => updateSetting("invertScale", c)}
                  label="Invert scale"
                />
                <Checkbox
                  checked={currentSettings().lockPriceToBarRatio}
                  onChange={(c) => updateSetting("lockPriceToBarRatio", c)}
                  label="Lock price to bar ratio"
                />
              </Section>

              <Section title="Price Labels & Lines">
                <Checkbox
                  checked={currentSettings().showLastPriceLine}
                  onChange={(c) => updateSetting("showLastPriceLine", c)}
                  label="Symbol value"
                />
                <Checkbox
                  checked={currentSettings().showPrevDayClose}
                  onChange={(c) => updateSetting("showPrevDayClose", c)}
                  label="Previous day close"
                />
                <Checkbox
                  checked={currentSettings().showHighLowLines}
                  onChange={(c) => updateSetting("showHighLowLines", c)}
                  label="High/Low"
                />
                <Checkbox
                  checked={currentSettings().showBidAskLines}
                  onChange={(c) => updateSetting("showBidAskLines", c)}
                  label="Bid/Ask"
                />
              </Section>

              <Section title="Time Scale">
                <Checkbox
                  checked={currentSettings().timeVisible}
                  onChange={(c) => updateSetting("timeVisible", c)}
                  label="Show time"
                />
                <Checkbox
                  checked={currentSettings().secondsVisible}
                  onChange={(c) => updateSetting("secondsVisible", c)}
                  label="Show seconds"
                />
                <Checkbox
                  checked={currentSettings().showBarCountdown}
                  onChange={(c) => updateSetting("showBarCountdown", c)}
                  label="Countdown to bar close"
                />
              </Section>
            </TabsContent>

            {/* Canvas Tab */}
            <TabsContent value="canvas" class="flex-1 p-4 overflow-y-auto">
              <Section title="Grid">
                <Checkbox
                  checked={currentSettings().gridVerticalVisible}
                  onChange={(c) => updateSetting("gridVerticalVisible", c)}
                  label="Vertical lines"
                />
                <Show when={currentSettings().gridVerticalVisible}>
                  <Row label="Color">
                    <ColorPicker
                      value={currentSettings().gridVerticalColor}
                      onChange={(c) => updateSetting("gridVerticalColor", c)}
                    />
                  </Row>
                </Show>
                <Checkbox
                  checked={currentSettings().gridHorizontalVisible}
                  onChange={(c) => updateSetting("gridHorizontalVisible", c)}
                  label="Horizontal lines"
                />
                <Show when={currentSettings().gridHorizontalVisible}>
                  <Row label="Color">
                    <ColorPicker
                      value={currentSettings().gridHorizontalColor}
                      onChange={(c) => updateSetting("gridHorizontalColor", c)}
                    />
                  </Row>
                </Show>
              </Section>

              <Section title="Crosshair">
                <Row label="Mode">
                  <select
                    value={String(currentSettings().crosshairMode)}
                    onChange={(e) =>
                      updateSetting("crosshairMode", parseInt(e.currentTarget.value) as CrosshairMode)
                    }
                    class="bg-[#2a2e39] text-[#d1d4dc] text-[13px] px-2 py-1 rounded border border-[#363a45] outline-none"
                  >
                    <option value="0">Normal</option>
                    <option value="1">Magnet</option>
                  </select>
                </Row>
                <Row label="Color">
                  <ColorPicker
                    value={currentSettings().crosshairColor}
                    onChange={(c) => updateSetting("crosshairColor", c)}
                  />
                </Row>
                <Row label="Label background">
                  <ColorPicker
                    value={currentSettings().crosshairLabelBackground}
                    onChange={(c) => updateSetting("crosshairLabelBackground", c)}
                  />
                </Row>
              </Section>
            </TabsContent>

            {/* Status Line Tab */}
            <TabsContent value="status" class="flex-1 p-4 overflow-y-auto">
              <Section title="Legend">
                <Checkbox
                  checked={currentSettings().showLegend}
                  onChange={(c) => updateSetting("showLegend", c)}
                  label="Show legend"
                />
                <Show when={currentSettings().showLegend}>
                  <Row label="Position">
                    <select
                      value={currentSettings().legendPosition}
                      onChange={(e) =>
                        updateSetting(
                          "legendPosition",
                          e.currentTarget.value as ChartSettings["legendPosition"]
                        )
                      }
                      class="bg-[#2a2e39] text-[#d1d4dc] text-[13px] px-2 py-1 rounded border border-[#363a45] outline-none"
                    >
                      <option value="top-left">Top Left</option>
                      <option value="top-right">Top Right</option>
                      <option value="bottom-left">Bottom Left</option>
                      <option value="bottom-right">Bottom Right</option>
                    </select>
                  </Row>
                </Show>
              </Section>
            </TabsContent>
          </Tabs.Root>
        </div>

        <DialogFooter class="justify-between">
          <Button variant="secondary" onClick={handleReset}>
            Reset to defaults
          </Button>
          <div class="flex gap-2">
            <Button variant="secondary" onClick={handleClose}>
              Cancel
            </Button>
            <Button variant="primary" onClick={handleClose}>
              Ok
            </Button>
          </div>
        </DialogFooter>
      </DialogContent>
    </Dialog.Root>
  );
};
