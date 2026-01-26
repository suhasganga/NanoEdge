import { createSignal, createEffect, For, Show, onCleanup } from "solid-js";
import { cn } from "~/lib/utils";
import {
  INDICATOR_TEMPLATES,
  INDICATOR_CATEGORIES,
  formatIndicatorLabel,
  searchTemplates,
  type IndicatorTemplate,
  type IndicatorCategory,
} from "~/lib/indicatorTemplates";
import { IndicatorConfigPanel } from "./IndicatorConfigPanel";
import type { IndicatorConfig } from "~/stores/indicatorStore";

interface IndicatorDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  activeIndicators: IndicatorConfig[];
  onAddIndicator: (config: IndicatorConfig) => void;
  onRemoveIndicator: (id: string) => void;
  onToggleIndicator: (id: string) => void;
}

export function IndicatorDialog(props: IndicatorDialogProps) {
  const [query, setQuery] = createSignal("");
  const [activeCategory, setActiveCategory] = createSignal<IndicatorCategory | "all">("all");
  const [selectedTemplate, setSelectedTemplate] = createSignal<IndicatorTemplate | null>(null);
  const [selectedIndex, setSelectedIndex] = createSignal(0);
  let inputRef: HTMLInputElement | undefined;

  // Filter templates based on search and category
  const filteredTemplates = () => {
    let templates = query()
      ? searchTemplates(query())
      : INDICATOR_TEMPLATES;

    if (activeCategory() !== "all") {
      templates = templates.filter((t) => t.category === activeCategory());
    }

    return templates;
  };

  // Reset state when dialog opens
  createEffect(() => {
    if (props.open) {
      setQuery("");
      setActiveCategory("all");
      setSelectedTemplate(null);
      setSelectedIndex(0);
      // Focus input after a brief delay
      setTimeout(() => inputRef?.focus(), 50);
    }
  });

  // Keyboard navigation
  const handleKeyDown = (e: KeyboardEvent) => {
    if (selectedTemplate()) return; // Don't navigate when config panel is open

    const templates = filteredTemplates();

    switch (e.key) {
      case "Escape":
        props.onOpenChange(false);
        break;
      case "ArrowDown":
        e.preventDefault();
        setSelectedIndex((prev) => Math.min(prev + 1, templates.length - 1));
        break;
      case "ArrowUp":
        e.preventDefault();
        setSelectedIndex((prev) => Math.max(prev - 1, 0));
        break;
      case "Enter":
        e.preventDefault();
        if (templates[selectedIndex()]) {
          setSelectedTemplate(templates[selectedIndex()]);
        }
        break;
    }
  };

  // Global escape handler
  createEffect(() => {
    if (!props.open) return;

    const handleGlobalKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        if (selectedTemplate()) {
          setSelectedTemplate(null);
        } else {
          props.onOpenChange(false);
        }
      }
    };
    document.addEventListener("keydown", handleGlobalKeyDown);
    onCleanup(() => document.removeEventListener("keydown", handleGlobalKeyDown));
  });

  const handleAddIndicator = (config: IndicatorConfig) => {
    props.onAddIndicator(config);
    setSelectedTemplate(null);
  };

  return (
    <Show when={props.open}>
      <div class="fixed inset-0 z-50 flex items-start justify-center pt-[10vh]">
      {/* Backdrop */}
      <div
        class="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={() => props.onOpenChange(false)}
      />

      {/* Dialog */}
      <div class="relative w-full max-w-xl bg-[#1e222d] rounded-lg shadow-2xl overflow-hidden border border-[#363a45] animate-in fade-in zoom-in-95 duration-150">
        <Show
          when={!selectedTemplate()}
          fallback={
            <IndicatorConfigPanel
              template={selectedTemplate()!}
              onAdd={handleAddIndicator}
              onCancel={() => setSelectedTemplate(null)}
            />
          }
        >
          {/* Header */}
          <div class="flex items-center justify-between px-5 py-4 border-b border-[#363a45]">
            <h2 class="text-lg font-semibold text-[#d1d4dc]">Indicators</h2>
            <button
              onClick={() => props.onOpenChange(false)}
              class="p-1.5 rounded-md hover:bg-[#2a2e39] text-[#787b86] hover:text-[#d1d4dc] transition-colors"
            >
              <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                <path
                  d="M4.5 4.5L13.5 13.5M4.5 13.5L13.5 4.5"
                  stroke="currentColor"
                  stroke-width="1.5"
                  stroke-linecap="round"
                />
              </svg>
            </button>
          </div>

          {/* Search Input */}
          <div class="px-5 py-4 border-b border-[#363a45]">
            <div class="relative">
              <div class="absolute left-4 top-1/2 -translate-y-1/2 text-[#787b86]">
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                  <circle cx="8" cy="8" r="5" stroke="currentColor" stroke-width="1.5" />
                  <path d="M12 12L16 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                </svg>
              </div>
              <input
                ref={inputRef}
                type="text"
                placeholder="Search indicators..."
                value={query()}
                onInput={(e) => {
                  setQuery(e.currentTarget.value);
                  setSelectedIndex(0);
                }}
                onKeyDown={handleKeyDown}
                class="w-full h-10 pl-11 pr-4 bg-[#2a2e39] border border-[#363a45] rounded-lg text-[#d1d4dc] text-sm placeholder-[#787b86] focus:outline-none focus:border-[#2962ff] transition-all"
              />
              <Show when={query()}>
                <button
                  onClick={() => {
                    setQuery("");
                    inputRef?.focus();
                  }}
                  class="absolute right-3 top-1/2 -translate-y-1/2 text-[#787b86] hover:text-[#d1d4dc]"
                >
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <path d="M4 4L12 12M4 12L12 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                  </svg>
                </button>
              </Show>
            </div>
          </div>

          {/* Category Tabs */}
          <div class="px-5 py-3 border-b border-[#363a45]">
            <div class="flex gap-2">
              <For each={INDICATOR_CATEGORIES}>
                {(cat) => (
                  <button
                    onClick={() => {
                      setActiveCategory(cat.id);
                      setSelectedIndex(0);
                    }}
                    class={cn(
                      "px-3 py-1.5 rounded-md text-xs font-medium transition-all",
                      activeCategory() === cat.id
                        ? "bg-[#2962ff] text-white"
                        : "bg-[#2a2e39] text-[#787b86] hover:bg-[#363a45] hover:text-[#d1d4dc]"
                    )}
                  >
                    {cat.label}
                  </button>
                )}
              </For>
            </div>
          </div>

          {/* Available Indicators */}
          <div class="max-h-[200px] overflow-y-auto">
            <Show
              when={filteredTemplates().length > 0}
              fallback={
                <div class="flex flex-col items-center justify-center py-8 text-[#787b86]">
                  <p class="text-sm">No indicators found</p>
                </div>
              }
            >
              <div class="py-2">
                <For each={filteredTemplates()}>
                  {(template, index) => (
                    <button
                      onClick={() => setSelectedTemplate(template)}
                      onMouseEnter={() => setSelectedIndex(index())}
                      class={cn(
                        "w-full px-5 py-3 flex items-center gap-4 transition-colors text-left",
                        selectedIndex() === index()
                          ? "bg-[#2a2e39]"
                          : "hover:bg-[#2a2e39]/50"
                      )}
                    >
                      {/* Icon */}
                      <div class="w-8 h-8 rounded-md bg-[#363a45] flex items-center justify-center text-[#d1d4dc]">
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                          <path
                            d="M2 12L5 8L8 10L14 4"
                            stroke="currentColor"
                            stroke-width="1.5"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                          />
                        </svg>
                      </div>

                      {/* Info */}
                      <div class="flex-1 min-w-0">
                        <div class="flex items-center gap-2">
                          <span class="font-medium text-[#d1d4dc]">
                            {template.shortName}
                          </span>
                          <span class="text-xs text-[#787b86]">
                            {template.name}
                          </span>
                        </div>
                        <p class="text-xs text-[#787b86] truncate mt-0.5">
                          {template.description}
                        </p>
                      </div>

                      {/* Arrow */}
                      <svg width="16" height="16" viewBox="0 0 16 16" fill="none" class="text-[#787b86]">
                        <path d="M6 4L10 8L6 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                      </svg>
                    </button>
                  )}
                </For>
              </div>
            </Show>
          </div>

          {/* Active Indicators */}
          <Show when={props.activeIndicators.length > 0}>
            <div class="border-t border-[#363a45]">
              <div class="px-5 py-2 bg-[#1a1d24]">
                <span class="text-xs font-medium text-[#787b86] uppercase tracking-wide">
                  Active ({props.activeIndicators.length})
                </span>
              </div>
              <div class="max-h-[180px] overflow-y-auto">
                <For each={props.activeIndicators}>
                  {(indicator) => (
                    <div class="px-5 py-2.5 flex items-center gap-3 hover:bg-[#2a2e39]/50 transition-colors">
                      {/* Color dot */}
                      <div
                        class="w-3 h-3 rounded-full shrink-0"
                        style={{ "background-color": indicator.color }}
                      />

                      {/* Label */}
                      <span class="flex-1 text-sm text-[#d1d4dc]">
                        {formatIndicatorLabel(
                          indicator.type,
                          indicator.period,
                          indicator.params
                        )}
                      </span>

                      {/* Visibility toggle */}
                      <button
                        onClick={() => props.onToggleIndicator(indicator.id)}
                        class={cn(
                          "p-1.5 rounded hover:bg-[#363a45] transition-colors",
                          indicator.visible
                            ? "text-[#d1d4dc]"
                            : "text-[#787b86]"
                        )}
                        title={indicator.visible ? "Hide" : "Show"}
                      >
                        <Show
                          when={indicator.visible}
                          fallback={
                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                              <path d="M2 2L14 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                              <path d="M6.5 6.5C6.18 6.94 6 7.45 6 8C6 9.1 6.9 10 8 10C8.55 10 9.06 9.82 9.5 9.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                              <path d="M3.5 5.5C2.5 6.5 1.7 7.5 1.2 8C2.5 10.5 5 13 8 13C9 13 10 12.7 10.9 12.2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                              <path d="M8 3C11 3 13.5 5.5 14.8 8C14.5 8.6 14.1 9.2 13.6 9.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                            </svg>
                          }
                        >
                          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                            <circle cx="8" cy="8" r="2" stroke="currentColor" stroke-width="1.5" />
                            <path d="M1.2 8C2.5 5.5 5 3 8 3C11 3 13.5 5.5 14.8 8C13.5 10.5 11 13 8 13C5 13 2.5 10.5 1.2 8Z" stroke="currentColor" stroke-width="1.5" />
                          </svg>
                        </Show>
                      </button>

                      {/* Remove button */}
                      <button
                        onClick={() => props.onRemoveIndicator(indicator.id)}
                        class="p-1.5 rounded hover:bg-[#363a45] text-[#787b86] hover:text-[#ef5350] transition-colors"
                        title="Remove"
                      >
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                          <path d="M4 4L12 12M4 12L12 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        </svg>
                      </button>
                    </div>
                  )}
                </For>
              </div>
            </div>
          </Show>

          {/* Footer */}
          <div class="px-5 py-3 border-t border-[#363a45] flex items-center justify-between text-xs text-[#787b86]">
            <div class="flex items-center gap-4">
              <span class="flex items-center gap-1">
                <kbd class="px-1.5 py-0.5 bg-[#2a2e39] rounded text-[10px] font-mono">↑</kbd>
                <kbd class="px-1.5 py-0.5 bg-[#2a2e39] rounded text-[10px] font-mono">↓</kbd>
                <span class="ml-1">Navigate</span>
              </span>
              <span class="flex items-center gap-1">
                <kbd class="px-1.5 py-0.5 bg-[#2a2e39] rounded text-[10px] font-mono">Enter</kbd>
                <span class="ml-1">Select</span>
              </span>
              <span class="flex items-center gap-1">
                <kbd class="px-1.5 py-0.5 bg-[#2a2e39] rounded text-[10px] font-mono">Esc</kbd>
                <span class="ml-1">Close</span>
              </span>
            </div>
          </div>
        </Show>
      </div>
    </div>
    </Show>
  );
}
