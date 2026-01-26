import { Component, For, splitProps, Show } from "solid-js";
import { RadioGroup as KRadioGroup } from "@kobalte/core/radio-group";
import { cn } from "~/lib/utils";

// TradingView checkmark icon (used for selected radio in menus)
const CheckIcon: Component = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="16" height="16">
    <path
      fill="currentColor"
      d="M22 9.06 11 20 6 14.7l1.09-1.02 3.94 4.16L20.94 8 22 9.06Z"
    />
  </svg>
);

interface RadioOption {
  value: string;
  label: string;
  shortcut?: string;
  disabled?: boolean;
}

interface RadioGroupProps {
  value?: string;
  onChange?: (value: string) => void;
  options: RadioOption[];
  orientation?: "horizontal" | "vertical";
  class?: string;
}

// Standard radio group (with radio button indicators)
export const RadioGroup: Component<RadioGroupProps> = (props) => {
  const [local] = splitProps(props, [
    "value",
    "onChange",
    "options",
    "orientation",
    "class",
  ]);

  return (
    <KRadioGroup
      value={local.value}
      onChange={local.onChange}
      orientation={local.orientation ?? "vertical"}
      class={cn(
        "flex",
        local.orientation === "horizontal" ? "flex-row gap-4" : "flex-col gap-1",
        local.class
      )}
    >
      <For each={local.options}>
        {(option) => (
          <KRadioGroup.Item
            value={option.value}
            disabled={option.disabled}
            class={cn(
              "group flex items-center gap-2 cursor-pointer select-none",
              option.disabled && "opacity-50 cursor-not-allowed"
            )}
          >
            <KRadioGroup.ItemInput class="sr-only" />
            <KRadioGroup.ItemControl
              class={cn(
                "flex h-4 w-4 items-center justify-center rounded-full border transition-colors",
                "border-[#363a45] bg-transparent",
                "group-hover:border-[#787b86]",
                "data-[checked]:border-[#2962ff]"
              )}
            >
              <KRadioGroup.ItemIndicator class="h-2 w-2 rounded-full bg-[#2962ff]" />
            </KRadioGroup.ItemControl>
            <KRadioGroup.ItemLabel class="text-[13px] text-[#d1d4dc]">
              {option.label}
            </KRadioGroup.ItemLabel>
          </KRadioGroup.Item>
        )}
      </For>
    </KRadioGroup>
  );
};

// Menu-style radio group (for context menus with checkmark indicator)
interface MenuRadioGroupProps {
  value?: string;
  onChange?: (value: string) => void;
  options: RadioOption[];
  class?: string;
}

export const MenuRadioGroup: Component<MenuRadioGroupProps> = (props) => {
  return (
    <KRadioGroup
      value={props.value}
      onChange={props.onChange}
      orientation="vertical"
      class={cn("flex flex-col", props.class)}
    >
      <For each={props.options}>
        {(option) => (
          <KRadioGroup.Item
            value={option.value}
            disabled={option.disabled}
            class={cn(
              "group flex items-center gap-2 px-3 py-2 cursor-pointer select-none",
              "hover:bg-[#2a2e39] transition-colors",
              option.disabled && "opacity-50 cursor-not-allowed"
            )}
          >
            <KRadioGroup.ItemInput class="sr-only" />
            <span class="w-6 flex items-center justify-center">
              <KRadioGroup.ItemIndicator class="text-[#d1d4dc]">
                <CheckIcon />
              </KRadioGroup.ItemIndicator>
            </span>
            <KRadioGroup.ItemLabel class="flex-1 text-[13px] text-[#d1d4dc]">
              {option.label}
            </KRadioGroup.ItemLabel>
            <Show when={option.shortcut}>
              <span class="text-[12px] text-[#787b86]">{option.shortcut}</span>
            </Show>
          </KRadioGroup.Item>
        )}
      </For>
    </KRadioGroup>
  );
};
