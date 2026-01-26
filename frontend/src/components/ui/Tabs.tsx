import {
  Component,
  JSX,
  splitProps,
  Show,
  ParentComponent,
  For,
} from "solid-js";
import { Tabs as KTabs } from "@kobalte/core/tabs";
import { cn } from "~/lib/utils";

// Tab definitions
interface TabItem {
  value: string;
  label: string;
  icon?: JSX.Element;
  disabled?: boolean;
}

// Tabs Root
interface TabsRootProps {
  value?: string;
  defaultValue?: string;
  onChange?: (value: string) => void;
  orientation?: "horizontal" | "vertical";
  children: JSX.Element;
  class?: string;
}

export const TabsRoot: ParentComponent<TabsRootProps> = (props) => {
  const [local] = splitProps(props, [
    "value",
    "defaultValue",
    "onChange",
    "orientation",
    "children",
    "class",
  ]);

  return (
    <KTabs
      value={local.value}
      defaultValue={local.defaultValue}
      onChange={local.onChange}
      orientation={local.orientation ?? "horizontal"}
      class={cn(
        "flex",
        local.orientation === "vertical" ? "flex-row" : "flex-col",
        local.class
      )}
    >
      {local.children}
    </KTabs>
  );
};

// Tabs List (container for tab triggers)
interface TabsListProps {
  children: JSX.Element;
  class?: string;
}

export const TabsList: ParentComponent<TabsListProps> = (props) => {
  return (
    <KTabs.List
      class={cn(
        "flex shrink-0",
        // Horizontal tabs
        "data-[orientation=horizontal]:flex-row data-[orientation=horizontal]:border-b data-[orientation=horizontal]:border-[#2a2e39]",
        // Vertical tabs (sidebar style like TradingView settings)
        "data-[orientation=vertical]:flex-col data-[orientation=vertical]:w-[180px] data-[orientation=vertical]:border-r data-[orientation=vertical]:border-[#2a2e39] data-[orientation=vertical]:bg-[#131722]",
        props.class
      )}
    >
      {props.children}
    </KTabs.List>
  );
};

// Tab Trigger
interface TabsTriggerProps {
  value: string;
  disabled?: boolean;
  children: JSX.Element;
  icon?: JSX.Element;
  class?: string;
}

export const TabsTrigger: ParentComponent<TabsTriggerProps> = (props) => {
  return (
    <KTabs.Trigger
      value={props.value}
      disabled={props.disabled}
      class={cn(
        "flex items-center gap-2 px-4 py-3 text-[13px] transition-colors outline-none",
        "text-[#787b86] hover:text-[#d1d4dc]",
        // Horizontal tabs
        "data-[orientation=horizontal]:border-b-2 data-[orientation=horizontal]:border-transparent",
        "data-[orientation=horizontal]:data-[selected]:border-[#2962ff] data-[orientation=horizontal]:data-[selected]:text-[#d1d4dc]",
        // Vertical tabs (sidebar style)
        "data-[orientation=vertical]:w-full data-[orientation=vertical]:justify-start",
        "data-[orientation=vertical]:data-[selected]:bg-[#1e222d] data-[orientation=vertical]:data-[selected]:text-[#d1d4dc]",
        "data-[orientation=vertical]:hover:bg-[#1e222d]/50",
        // Disabled state
        props.disabled && "opacity-50 cursor-not-allowed",
        props.class
      )}
    >
      <Show when={props.icon}>
        <span class="w-5 h-5 flex items-center justify-center text-current">
          {props.icon}
        </span>
      </Show>
      <span>{props.children}</span>
    </KTabs.Trigger>
  );
};

// Tab Content
interface TabsContentProps {
  value: string;
  children: JSX.Element;
  class?: string;
}

export const TabsContent: ParentComponent<TabsContentProps> = (props) => {
  return (
    <KTabs.Content
      value={props.value}
      class={cn(
        "flex-1 outline-none",
        "animate-in fade-in-0",
        "data-[state=inactive]:hidden",
        props.class
      )}
    >
      {props.children}
    </KTabs.Content>
  );
};

// Convenient Tabs component with items array
interface TabsProps {
  items: TabItem[];
  value?: string;
  defaultValue?: string;
  onChange?: (value: string) => void;
  orientation?: "horizontal" | "vertical";
  children: (value: string) => JSX.Element;
  class?: string;
  listClass?: string;
  contentClass?: string;
}

export const SimpleTabs: Component<TabsProps> = (props) => {
  return (
    <TabsRoot
      value={props.value}
      defaultValue={props.defaultValue ?? props.items[0]?.value}
      onChange={props.onChange}
      orientation={props.orientation}
      class={props.class}
    >
      <TabsList class={props.listClass}>
        <For each={props.items}>
          {(item) => (
            <TabsTrigger
              value={item.value}
              disabled={item.disabled}
              icon={item.icon}
            >
              {item.label}
            </TabsTrigger>
          )}
        </For>
      </TabsList>
      <For each={props.items}>
        {(item) => (
          <TabsContent value={item.value} class={props.contentClass}>
            {props.children(item.value)}
          </TabsContent>
        )}
      </For>
    </TabsRoot>
  );
};

// Export all as a namespace for convenience
export const Tabs = {
  Root: TabsRoot,
  List: TabsList,
  Trigger: TabsTrigger,
  Content: TabsContent,
};
