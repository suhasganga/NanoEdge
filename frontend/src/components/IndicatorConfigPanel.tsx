import { createSignal, For, Show } from "solid-js";
import { cn } from "~/lib/utils";
import type { IndicatorTemplate } from "~/lib/indicatorTemplates";
import { INDICATOR_COLORS } from "~/lib/indicatorTemplates";
import type { IndicatorConfig } from "~/stores/indicatorStore";
import { generateIndicatorId } from "~/stores/indicatorStore";

interface IndicatorConfigPanelProps {
  template: IndicatorTemplate;
  existingConfig?: IndicatorConfig; // For editing
  onAdd: (config: IndicatorConfig) => void;
  onCancel: () => void;
}

export function IndicatorConfigPanel(props: IndicatorConfigPanelProps) {
  const isEditing = () => !!props.existingConfig;

  const [period, setPeriod] = createSignal(
    props.existingConfig?.period ?? props.template.defaultPeriod
  );
  const [color, setColor] = createSignal(
    props.existingConfig?.color ?? props.template.defaultColor
  );
  const [stdDev, setStdDev] = createSignal(
    props.existingConfig?.params?.stdDev ?? props.template.defaultStdDev ?? 2
  );

  const handlePeriodInput = (value: string) => {
    const num = parseInt(value, 10);
    if (!isNaN(num)) {
      const clamped = Math.max(
        props.template.minPeriod,
        Math.min(props.template.maxPeriod, num)
      );
      setPeriod(clamped);
    }
  };

  const handleStdDevInput = (value: string) => {
    const num = parseFloat(value);
    if (!isNaN(num) && num >= 0.1 && num <= 5) {
      setStdDev(Math.round(num * 10) / 10);
    }
  };

  const handleAdd = () => {
    const config: IndicatorConfig = {
      id: props.existingConfig?.id ?? generateIndicatorId(props.template.type, period()),
      type: props.template.type,
      period: period(),
      color: color(),
      visible: true,
      params: props.template.hasStdDev ? { stdDev: stdDev() } : undefined,
    };
    props.onAdd(config);
  };

  return (
    <div class="flex flex-col h-full">
      {/* Header */}
      <div class="flex items-center gap-3 px-5 py-4 border-b border-[#363a45]">
        <button
          onClick={props.onCancel}
          class="p-1.5 rounded-md hover:bg-[#2a2e39] text-[#787b86] hover:text-[#d1d4dc] transition-colors"
          title="Back"
        >
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path
              d="M11 4L6 9L11 14"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>
        <div>
          <h3 class="text-base font-semibold text-[#d1d4dc]">
            {props.template.name}
          </h3>
          <p class="text-xs text-[#787b86]">{props.template.shortName}</p>
        </div>
      </div>

      {/* Configuration */}
      <div class="flex-1 px-5 py-4 space-y-6 overflow-y-auto">
        {/* Period */}
        <div class="space-y-2">
          <label class="text-sm font-medium text-[#d1d4dc]">Period</label>
          <div class="flex items-center gap-3">
            <input
              type="range"
              min={props.template.minPeriod}
              max={Math.min(props.template.maxPeriod, 200)}
              value={period()}
              onInput={(e) => setPeriod(parseInt(e.currentTarget.value, 10))}
              class="flex-1 h-2 bg-[#2a2e39] rounded-lg appearance-none cursor-pointer accent-[#2962ff]"
            />
            <input
              type="number"
              min={props.template.minPeriod}
              max={props.template.maxPeriod}
              value={period()}
              onInput={(e) => handlePeriodInput(e.currentTarget.value)}
              class="w-20 h-9 px-3 bg-[#2a2e39] border border-[#363a45] rounded-md text-[#d1d4dc] text-sm text-center focus:outline-none focus:border-[#2962ff]"
            />
          </div>
          <p class="text-xs text-[#787b86]">
            Range: {props.template.minPeriod} - {props.template.maxPeriod}
          </p>
        </div>

        {/* Standard Deviation (for Bollinger Bands) */}
        <Show when={props.template.hasStdDev}>
          <div class="space-y-2">
            <label class="text-sm font-medium text-[#d1d4dc]">
              Standard Deviation
            </label>
            <div class="flex items-center gap-3">
              <input
                type="range"
                min="0.5"
                max="4"
                step="0.5"
                value={stdDev()}
                onInput={(e) => setStdDev(parseFloat(e.currentTarget.value))}
                class="flex-1 h-2 bg-[#2a2e39] rounded-lg appearance-none cursor-pointer accent-[#2962ff]"
              />
              <input
                type="number"
                min="0.1"
                max="5"
                step="0.1"
                value={stdDev()}
                onInput={(e) => handleStdDevInput(e.currentTarget.value)}
                class="w-20 h-9 px-3 bg-[#2a2e39] border border-[#363a45] rounded-md text-[#d1d4dc] text-sm text-center focus:outline-none focus:border-[#2962ff]"
              />
            </div>
            <p class="text-xs text-[#787b86]">
              Controls the width of the bands
            </p>
          </div>
        </Show>

        {/* Color */}
        <div class="space-y-2">
          <label class="text-sm font-medium text-[#d1d4dc]">Color</label>
          <div class="flex flex-wrap gap-2">
            <For each={INDICATOR_COLORS}>
              {(c) => (
                <button
                  onClick={() => setColor(c)}
                  class={cn(
                    "w-8 h-8 rounded-md transition-all",
                    color() === c
                      ? "ring-2 ring-[#2962ff] ring-offset-2 ring-offset-[#1e222d]"
                      : "hover:scale-110"
                  )}
                  style={{ "background-color": c }}
                  title={c}
                />
              )}
            </For>
          </div>
          <div class="flex items-center gap-2 mt-2">
            <span class="text-xs text-[#787b86]">Custom:</span>
            <input
              type="color"
              value={color()}
              onInput={(e) => setColor(e.currentTarget.value)}
              class="w-8 h-8 rounded cursor-pointer bg-transparent border-0"
            />
            <span class="text-xs text-[#787b86] font-mono">{color()}</span>
          </div>
        </div>

        {/* Preview */}
        <div class="p-3 bg-[#2a2e39] rounded-lg">
          <div class="flex items-center gap-3">
            <div
              class="w-4 h-4 rounded-full"
              style={{ "background-color": color() }}
            />
            <span class="text-sm text-[#d1d4dc]">
              {props.template.shortName} {period()}
              {props.template.hasStdDev && `, ${stdDev()}`}
            </span>
          </div>
        </div>
      </div>

      {/* Footer */}
      <div class="flex items-center justify-end gap-3 px-5 py-4 border-t border-[#363a45]">
        <button
          onClick={props.onCancel}
          class="px-4 py-2 text-sm font-medium text-[#787b86] hover:text-[#d1d4dc] transition-colors"
        >
          Cancel
        </button>
        <button
          onClick={handleAdd}
          class="px-4 py-2 text-sm font-medium bg-[#2962ff] text-white rounded-md hover:bg-[#1e4bd8] transition-colors"
        >
          {isEditing() ? "Update" : "Add to Chart"}
        </button>
      </div>
    </div>
  );
}
