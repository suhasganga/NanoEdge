import { createSignal, createResource, For, Show, createEffect, onCleanup } from "solid-js";
import { cn } from "~/lib/utils";

interface SearchResult {
  symbol: string;
  exchange: string;
  market: string;
  description: string;
  type: string;
  base: string;
  quote: string;
}

interface SymbolSearchProps {
  onSelect: (exchange: string, market: string, symbol: string) => void;
  onClose?: () => void;
  initialValue?: string;
}

const FILTER_TABS = [
  { id: "all", label: "All", icon: null },
  { id: "spot", label: "Crypto", icon: "crypto" },
  { id: "futures", label: "Futures", icon: "futures" },
  { id: "equity", label: "Stocks", icon: "stocks" },
  { id: "index_future,index_option_ce,index_option_pe", label: "Indices", icon: "indices" },
  { id: "currency_future,currency_option_ce,currency_option_pe", label: "Forex", icon: "forex" },
  { id: "commodity_future,commodity_option_ce,commodity_option_pe", label: "Commodities", icon: "commodities" },
];

const EXCHANGE_LOGOS: Record<string, { name: string; color: string; abbr: string }> = {
  binance: { name: "Binance", color: "#F0B90B", abbr: "BN" },
  fyers: { name: "NSE", color: "#0052CC", abbr: "NSE" },
};

// Generate avatar colors based on symbol
function getAvatarColor(symbol: string): string {
  const colors = [
    "bg-blue-500", "bg-green-500", "bg-yellow-500", "bg-purple-500",
    "bg-pink-500", "bg-indigo-500", "bg-cyan-500", "bg-orange-500",
  ];
  const hash = symbol.split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);
  return colors[hash % colors.length];
}

export function SymbolSearch(props: SymbolSearchProps) {
  // Initialize query with the character that triggered the search
  const [query, setQuery] = createSignal(props.initialValue || "");
  const [activeFilter, setActiveFilter] = createSignal("all");
  const [selectedIndex, setSelectedIndex] = createSignal(0);
  const [isLoading, setIsLoading] = createSignal(false);
  let inputRef: HTMLInputElement | undefined;
  let resultsRef: HTMLDivElement | undefined;

  // Debounced search - also initialize with initial value
  const [debouncedQuery, setDebouncedQuery] = createSignal(props.initialValue || "");
  let debounceTimer: ReturnType<typeof setTimeout>;

  createEffect(() => {
    const q = query();
    clearTimeout(debounceTimer);
    if (q.length >= 1) {
      debounceTimer = setTimeout(() => {
        setDebouncedQuery(q);
        setSelectedIndex(0);
      }, 150);
    } else {
      setDebouncedQuery("");
    }
  });

  // Fetch search results - depends on both query and filter
  const fetchResults = async (source: { query: string; filter: string }): Promise<SearchResult[]> => {
    const { query: q, filter } = source;
    if (!q || q.length < 1) return [];

    setIsLoading(true);
    try {
      const params = new URLSearchParams({ q, limit: "100" });

      if (filter && filter !== "all") {
        params.set("types", filter);
      }

      const resp = await fetch(`/api/symbols/search?${params}`);
      if (!resp.ok) throw new Error("Search failed");

      const data = await resp.json();
      return data.results || [];
    } catch (err) {
      console.error("Symbol search error:", err);
      return [];
    } finally {
      setIsLoading(false);
    }
  };

  // Resource depends on BOTH query AND filter - re-fetches when either changes
  const [results] = createResource(
    () => ({ query: debouncedQuery(), filter: activeFilter() }),
    fetchResults
  );

  // Focus input on mount and position cursor at end
  createEffect(() => {
    if (inputRef) {
      inputRef.focus();
      // Position cursor at end of initial text
      const len = inputRef.value.length;
      inputRef.setSelectionRange(len, len);
    }
  });

  // Keyboard navigation
  const handleKeyDown = (e: KeyboardEvent) => {
    const resultsList = results() || [];

    switch (e.key) {
      case "Escape":
        props.onClose?.();
        break;
      case "ArrowDown":
        e.preventDefault();
        setSelectedIndex((prev) => Math.min(prev + 1, resultsList.length - 1));
        scrollToSelected();
        break;
      case "ArrowUp":
        e.preventDefault();
        setSelectedIndex((prev) => Math.max(prev - 1, 0));
        scrollToSelected();
        break;
      case "Enter":
        e.preventDefault();
        if (resultsList[selectedIndex()]) {
          handleSelect(resultsList[selectedIndex()]);
        }
        break;
    }
  };

  const scrollToSelected = () => {
    setTimeout(() => {
      const selected = resultsRef?.querySelector(`[data-index="${selectedIndex()}"]`);
      selected?.scrollIntoView({ block: "nearest" });
    }, 0);
  };

  const handleSelect = (result: SearchResult) => {
    props.onSelect(result.exchange, result.market, result.symbol);
    props.onClose?.();
  };

  const clearSearch = () => {
    setQuery("");
    inputRef?.focus();
  };

  // Global escape handler
  createEffect(() => {
    const handleGlobalKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        props.onClose?.();
      }
    };
    document.addEventListener("keydown", handleGlobalKeyDown);
    onCleanup(() => document.removeEventListener("keydown", handleGlobalKeyDown));
  });

  return (
    <div class="fixed inset-0 z-50 flex items-start justify-center pt-[10vh]">
      {/* Backdrop */}
      <div
        class="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={() => props.onClose?.()}
      />

      {/* Dialog */}
      <div class="relative w-full max-w-2xl bg-[#1e222d] rounded-lg shadow-2xl overflow-hidden border border-[#363a45] animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div class="flex items-center justify-between px-5 py-4 border-b border-[#363a45]">
          <h2 class="text-lg font-semibold text-[#d1d4dc]">Symbol Search</h2>
          <button
            onClick={() => props.onClose?.()}
            class="p-1.5 rounded-md hover:bg-[#2a2e39] text-[#787b86] hover:text-[#d1d4dc] transition-colors"
          >
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
              <path d="M4.5 4.5L13.5 13.5M4.5 13.5L13.5 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
            </svg>
          </button>
        </div>

        {/* Search Input */}
        <div class="px-5 py-4 border-b border-[#363a45]">
          <div class="relative">
            <div class="absolute left-4 top-1/2 -translate-y-1/2 text-[#787b86]">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <circle cx="9" cy="9" r="6" stroke="currentColor" stroke-width="1.5" />
                <path d="M13.5 13.5L17 17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
              </svg>
            </div>
            <input
              ref={inputRef}
              type="text"
              placeholder="Search"
              value={query()}
              onInput={(e) => setQuery(e.currentTarget.value)}
              onKeyDown={handleKeyDown}
              class="w-full h-12 pl-12 pr-12 bg-[#2a2e39] border border-[#363a45] rounded-lg text-[#d1d4dc] text-base placeholder-[#787b86] focus:outline-none focus:border-[#2962ff] focus:ring-1 focus:ring-[#2962ff] transition-all"
            />
            <Show when={query()}>
              <button
                onClick={clearSearch}
                class="absolute right-4 top-1/2 -translate-y-1/2 text-[#787b86] hover:text-[#d1d4dc] transition-colors"
              >
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                  <circle cx="9" cy="9" r="8" stroke="currentColor" stroke-width="1.5" />
                  <path d="M6 6L12 12M6 12L12 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                </svg>
              </button>
            </Show>
          </div>
        </div>

        {/* Filter Tabs */}
        <div class="px-5 py-3 border-b border-[#363a45] overflow-x-auto scrollbar-hide">
          <div class="flex gap-2">
            <For each={FILTER_TABS}>
              {(tab) => (
                <button
                  onClick={() => {
                    setActiveFilter(tab.id);
                    setSelectedIndex(0);
                  }}
                  class={cn(
                    "flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium whitespace-nowrap transition-all",
                    activeFilter() === tab.id
                      ? "bg-[#2962ff] text-white"
                      : "bg-[#2a2e39] text-[#787b86] hover:bg-[#363a45] hover:text-[#d1d4dc]"
                  )}
                >
                  {tab.label}
                </button>
              )}
            </For>
          </div>
        </div>

        {/* Results List */}
        <div
          ref={resultsRef}
          class="max-h-[400px] overflow-y-auto scrollbar-hide"
        >
          <Show when={isLoading()}>
            <div class="flex items-center justify-center py-12">
              <div class="flex items-center gap-3 text-[#787b86]">
                <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" opacity="0.25" />
                  <path d="M12 2C6.48 2 2 6.48 2 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                </svg>
                <span>Searching...</span>
              </div>
            </div>
          </Show>

          <Show when={!isLoading() && debouncedQuery() && results()?.length === 0}>
            <div class="flex flex-col items-center justify-center py-12 text-[#787b86]">
              <svg width="48" height="48" viewBox="0 0 48 48" fill="none" class="mb-3 opacity-50">
                <circle cx="22" cy="22" r="14" stroke="currentColor" stroke-width="2" />
                <path d="M32 32L42 42" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                <path d="M16 22H28" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
              </svg>
              <p class="text-sm">No symbols found for "{debouncedQuery()}"</p>
              <p class="text-xs mt-1 opacity-70">Try a different search term</p>
            </div>
          </Show>

          <Show when={!isLoading() && !debouncedQuery()}>
            <div class="flex flex-col items-center justify-center py-12 text-[#787b86]">
              <svg width="48" height="48" viewBox="0 0 48 48" fill="none" class="mb-3 opacity-50">
                <circle cx="22" cy="22" r="14" stroke="currentColor" stroke-width="2" />
                <path d="M32 32L42 42" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
              </svg>
              <p class="text-sm">Search for symbols</p>
              <p class="text-xs mt-1 opacity-70">e.g., BTC, ETH, NIFTY, RELIANCE</p>
            </div>
          </Show>

          <Show when={!isLoading() && results() && results()!.length > 0}>
            <div class="py-2">
              <For each={results()}>
                {(result, index) => {
                  const exchangeInfo = EXCHANGE_LOGOS[result.exchange] || {
                    name: result.exchange.toUpperCase(),
                    color: "#787b86",
                    abbr: result.exchange.substring(0, 3).toUpperCase(),
                  };

                  return (
                    <button
                      data-index={index()}
                      onClick={() => handleSelect(result)}
                      onMouseEnter={() => setSelectedIndex(index())}
                      class={cn(
                        "w-full px-5 py-3 flex items-center gap-4 transition-colors",
                        selectedIndex() === index()
                          ? "bg-[#2a2e39]"
                          : "hover:bg-[#2a2e39]/50"
                      )}
                    >
                      {/* Symbol Avatar */}
                      <div
                        class={cn(
                          "w-10 h-10 rounded-full flex items-center justify-center text-white font-bold text-sm shrink-0",
                          getAvatarColor(result.base || result.symbol)
                        )}
                      >
                        {(result.base || result.symbol).substring(0, 2)}
                      </div>

                      {/* Symbol Info */}
                      <div class="flex-1 min-w-0 text-left">
                        <div class="flex items-center gap-2">
                          <span class="font-semibold text-[#d1d4dc]">
                            {result.symbol}
                          </span>
                          <span class="px-1.5 py-0.5 text-[10px] font-medium rounded bg-[#363a45] text-[#787b86] uppercase">
                            {result.type.replace(/_/g, " ")}
                          </span>
                        </div>
                        <p class="text-sm text-[#787b86] truncate mt-0.5">
                          {result.description || `${result.base} / ${result.quote}`}
                        </p>
                      </div>

                      {/* Exchange Badge */}
                      <div class="flex items-center gap-2 shrink-0">
                        <div
                          class="px-2 py-1 rounded text-xs font-semibold"
                          style={{
                            "background-color": `${exchangeInfo.color}20`,
                            color: exchangeInfo.color,
                          }}
                        >
                          {exchangeInfo.name}
                        </div>
                      </div>
                    </button>
                  );
                }}
              </For>
            </div>
          </Show>
        </div>

        {/* Footer */}
        <div class="px-5 py-3 border-t border-[#363a45] bg-[#1e222d] flex items-center justify-between text-xs text-[#787b86]">
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
          <Show when={results()}>
            <span>{results()!.length} results</span>
          </Show>
        </div>
      </div>
    </div>
  );
}
