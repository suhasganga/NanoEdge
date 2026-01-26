import { Component, splitProps, Show } from "solid-js";
import { Checkbox as KCheckbox } from "@kobalte/core/checkbox";
import { cn } from "~/lib/utils";

// TradingView checkmark icon
const CheckIcon: Component = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" width="16" height="16">
    <path
      fill="currentColor"
      d="M22 9.06 11 20 6 14.7l1.09-1.02 3.94 4.16L20.94 8 22 9.06Z"
    />
  </svg>
);

interface CheckboxProps {
  checked?: boolean;
  onChange?: (checked: boolean) => void;
  label?: string;
  disabled?: boolean;
  class?: string;
}

export const Checkbox: Component<CheckboxProps> = (props) => {
  const [local] = splitProps(props, [
    "checked",
    "onChange",
    "label",
    "disabled",
    "class",
  ]);

  return (
    <KCheckbox
      checked={local.checked}
      onChange={local.onChange}
      disabled={local.disabled}
      class={cn(
        "group flex items-center gap-2 cursor-pointer select-none",
        local.disabled && "opacity-50 cursor-not-allowed",
        local.class
      )}
    >
      <KCheckbox.Input class="sr-only" />
      <KCheckbox.Control
        class={cn(
          "flex h-4 w-4 items-center justify-center rounded border transition-colors",
          "border-[#363a45] bg-transparent",
          "group-hover:border-[#787b86]",
          "data-[checked]:bg-[#2962ff] data-[checked]:border-[#2962ff]"
        )}
      >
        <KCheckbox.Indicator class="text-white">
          <CheckIcon />
        </KCheckbox.Indicator>
      </KCheckbox.Control>
      <Show when={local.label}>
        <KCheckbox.Label class="text-[13px] text-[#d1d4dc]">
          {local.label}
        </KCheckbox.Label>
      </Show>
    </KCheckbox>
  );
};

// Menu-style checkbox item (for context menus)
interface MenuCheckboxItemProps {
  checked?: boolean;
  onChange?: (checked: boolean) => void;
  label: string;
  shortcut?: string;
  disabled?: boolean;
  class?: string;
}

export const MenuCheckboxItem: Component<MenuCheckboxItemProps> = (props) => {
  return (
    <KCheckbox
      checked={props.checked}
      onChange={props.onChange}
      disabled={props.disabled}
      class={cn(
        "group flex items-center gap-2 px-3 py-2 cursor-pointer select-none",
        "hover:bg-[#2a2e39] transition-colors",
        props.disabled && "opacity-50 cursor-not-allowed",
        props.class
      )}
    >
      <KCheckbox.Input class="sr-only" />
      <span class="w-6 flex items-center justify-center">
        <KCheckbox.Indicator class="text-[#d1d4dc]">
          <CheckIcon />
        </KCheckbox.Indicator>
      </span>
      <KCheckbox.Label class="flex-1 text-[13px] text-[#d1d4dc]">
        {props.label}
      </KCheckbox.Label>
      <Show when={props.shortcut}>
        <span class="text-[12px] text-[#787b86]">{props.shortcut}</span>
      </Show>
    </KCheckbox>
  );
};
