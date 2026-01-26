import {
  Component,
  JSX,
  Show,
  ParentComponent,
} from "solid-js";
import { ContextMenu as KContextMenu } from "@kobalte/core/context-menu";
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

// TradingView submenu arrow icon
const ArrowIcon: Component = () => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 16" width="10" height="16">
    <path
      fill="currentColor"
      d="M.6 1.4l1.4-1.4 8 8-8 8-1.4-1.4 6.389-6.532-6.389-6.668z"
    />
  </svg>
);

// Context Menu Root
export const ContextMenuRoot = KContextMenu;

// Context Menu Trigger
interface ContextMenuTriggerProps {
  children: JSX.Element;
  class?: string;
}

export const ContextMenuTrigger: ParentComponent<ContextMenuTriggerProps> = (props) => {
  return (
    <KContextMenu.Trigger class={props.class}>
      {props.children}
    </KContextMenu.Trigger>
  );
};

// Context Menu Content
interface ContextMenuContentProps {
  children: JSX.Element;
  class?: string;
}

export const ContextMenuContent: ParentComponent<ContextMenuContentProps> = (props) => {
  return (
    <KContextMenu.Portal>
      <KContextMenu.Content
        class={cn(
          // TradingView dark theme styling
          "min-w-[200px] py-1 rounded",
          "bg-[#1e222d] border border-[#2a2e39]",
          "shadow-[0_2px_4px_rgba(0,0,0,0.2),0_0_1px_rgba(0,0,0,0.3)]",
          "text-[#d1d4dc] text-[13px]",
          "font-sans",
          // Animation
          "animate-in fade-in-0 zoom-in-95",
          "data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95",
          "origin-[var(--kb-menu-content-transform-origin)]",
          "z-50",
          props.class
        )}
      >
        {props.children}
      </KContextMenu.Content>
    </KContextMenu.Portal>
  );
};

// Context Menu Item
interface ContextMenuItemProps {
  onSelect?: () => void;
  disabled?: boolean;
  children: JSX.Element;
  shortcut?: string;
  class?: string;
}

export const ContextMenuItem: ParentComponent<ContextMenuItemProps> = (props) => {
  return (
    <KContextMenu.Item
      onSelect={props.onSelect}
      disabled={props.disabled}
      class={cn(
        "flex items-center gap-2 px-3 py-2 cursor-pointer select-none outline-none",
        "hover:bg-[#2a2e39] focus:bg-[#2a2e39] transition-colors",
        props.disabled && "opacity-50 cursor-not-allowed",
        props.class
      )}
    >
      <span class="w-6" /> {/* Spacer for icon column */}
      <span class="flex-1">{props.children}</span>
      <Show when={props.shortcut}>
        <span class="text-[12px] text-[#787b86]">{props.shortcut}</span>
      </Show>
    </KContextMenu.Item>
  );
};

// Context Menu Checkbox Item
interface ContextMenuCheckboxItemProps {
  checked?: boolean;
  onChange?: (checked: boolean) => void;
  disabled?: boolean;
  children: JSX.Element;
  shortcut?: string;
  class?: string;
}

export const ContextMenuCheckboxItem: Component<ContextMenuCheckboxItemProps> = (
  props
) => {
  return (
    <KContextMenu.CheckboxItem
      checked={props.checked}
      onChange={props.onChange}
      disabled={props.disabled}
      class={cn(
        "flex items-center gap-2 px-3 py-2 cursor-pointer select-none outline-none",
        "hover:bg-[#2a2e39] focus:bg-[#2a2e39] transition-colors",
        props.disabled && "opacity-50 cursor-not-allowed",
        props.class
      )}
    >
      <span class="w-6 flex items-center justify-center">
        <KContextMenu.ItemIndicator>
          <CheckIcon />
        </KContextMenu.ItemIndicator>
      </span>
      <span class="flex-1">{props.children}</span>
      <Show when={props.shortcut}>
        <span class="text-[12px] text-[#787b86]">{props.shortcut}</span>
      </Show>
    </KContextMenu.CheckboxItem>
  );
};

// Context Menu Radio Group
export const ContextMenuRadioGroup = KContextMenu.RadioGroup;

// Context Menu Radio Item
interface ContextMenuRadioItemProps {
  value: string;
  disabled?: boolean;
  children: JSX.Element;
  shortcut?: string;
  class?: string;
}

export const ContextMenuRadioItem: Component<ContextMenuRadioItemProps> = (props) => {
  return (
    <KContextMenu.RadioItem
      value={props.value}
      disabled={props.disabled}
      class={cn(
        "flex items-center gap-2 px-3 py-2 cursor-pointer select-none outline-none",
        "hover:bg-[#2a2e39] focus:bg-[#2a2e39] transition-colors",
        props.disabled && "opacity-50 cursor-not-allowed",
        props.class
      )}
    >
      <span class="w-6 flex items-center justify-center">
        <KContextMenu.ItemIndicator>
          <CheckIcon />
        </KContextMenu.ItemIndicator>
      </span>
      <span class="flex-1">{props.children}</span>
      <Show when={props.shortcut}>
        <span class="text-[12px] text-[#787b86]">{props.shortcut}</span>
      </Show>
    </KContextMenu.RadioItem>
  );
};

// Context Menu Separator
export const ContextMenuSeparator: Component<{ class?: string }> = (props) => {
  return (
    <KContextMenu.Separator
      class={cn("h-px bg-[#2a2e39] my-1", props.class)}
    />
  );
};

// Context Menu Sub (submenu)
export const ContextMenuSub = KContextMenu.Sub;

// Context Menu Sub Trigger
interface ContextMenuSubTriggerProps {
  disabled?: boolean;
  children: JSX.Element;
  class?: string;
}

export const ContextMenuSubTrigger: Component<ContextMenuSubTriggerProps> = (
  props
) => {
  return (
    <KContextMenu.SubTrigger
      disabled={props.disabled}
      class={cn(
        "flex items-center gap-2 px-3 py-2 cursor-pointer select-none outline-none",
        "hover:bg-[#2a2e39] focus:bg-[#2a2e39] transition-colors",
        "data-[expanded]:bg-[#2a2e39]",
        props.disabled && "opacity-50 cursor-not-allowed",
        props.class
      )}
    >
      <span class="w-6" /> {/* Spacer for icon column */}
      <span class="flex-1">{props.children}</span>
      <ArrowIcon />
    </KContextMenu.SubTrigger>
  );
};

// Context Menu Sub Content
interface ContextMenuSubContentProps {
  children: JSX.Element;
  class?: string;
}

export const ContextMenuSubContent: ParentComponent<ContextMenuSubContentProps> = (
  props
) => {
  return (
    <KContextMenu.Portal>
      <KContextMenu.SubContent
        class={cn(
          // TradingView dark theme styling (same as main content)
          "min-w-[180px] py-1 rounded",
          "bg-[#1e222d] border border-[#2a2e39]",
          "shadow-[0_2px_4px_rgba(0,0,0,0.2),0_0_1px_rgba(0,0,0,0.3)]",
          "text-[#d1d4dc] text-[13px]",
          "font-sans",
          // Animation
          "animate-in fade-in-0 zoom-in-95",
          "data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95",
          "origin-[var(--kb-menu-content-transform-origin)]",
          "z-50",
          props.class
        )}
      >
        {props.children}
      </KContextMenu.SubContent>
    </KContextMenu.Portal>
  );
};

// Context Menu Group
export const ContextMenuGroup = KContextMenu.Group;

// Context Menu Group Label
interface ContextMenuGroupLabelProps {
  children: JSX.Element;
  class?: string;
}

export const ContextMenuGroupLabel: Component<ContextMenuGroupLabelProps> = (
  props
) => {
  return (
    <KContextMenu.GroupLabel
      class={cn(
        "px-3 py-1.5 text-[11px] font-medium text-[#787b86] uppercase tracking-wide",
        props.class
      )}
    >
      {props.children}
    </KContextMenu.GroupLabel>
  );
};

// Export all as a namespace for convenience
export const ContextMenu = {
  Root: ContextMenuRoot,
  Trigger: ContextMenuTrigger,
  Content: ContextMenuContent,
  Item: ContextMenuItem,
  CheckboxItem: ContextMenuCheckboxItem,
  RadioGroup: ContextMenuRadioGroup,
  RadioItem: ContextMenuRadioItem,
  Separator: ContextMenuSeparator,
  Sub: ContextMenuSub,
  SubTrigger: ContextMenuSubTrigger,
  SubContent: ContextMenuSubContent,
  Group: ContextMenuGroup,
  GroupLabel: ContextMenuGroupLabel,
};
