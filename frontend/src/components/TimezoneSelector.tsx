import { Component, For, Show, createSignal, createEffect, onCleanup } from "solid-js";
import { Portal } from "solid-js/web";
import { cn } from "~/lib/utils";
import { settings, updateSetting } from "~/stores/chartSettings";
import {
  getCurrentTimeInTimezone,
  getTimezoneOffsetLabel,
  resolveTimezone,
  getTimezonesSortedByOffset,
} from "~/lib/timezone";

interface TimezoneSelectorProps {
  symbol: string;
}

/**
 * TimezoneSelector - TradingView-style timezone picker.
 *
 * Features:
 * - Flat list sorted by UTC offset (no search, no grouping)
 * - Checkmark on left for selected item
 * - Live clock at bottom of dropdown
 * - Clean minimal styling matching TradingView
 */
export const TimezoneSelector: Component<TimezoneSelectorProps> = (props) => {
  const [isOpen, setIsOpen] = createSignal(false);
  const [currentTime, setCurrentTime] = createSignal("");
  const [dropdownPos, setDropdownPos] = createSignal({ top: 0, right: 0 });
  let buttonRef: HTMLButtonElement | undefined;

  // Get the resolved timezone (handles "EXCHANGE" special case)
  const resolvedTz = () => resolveTimezone(settings().timezone, props.symbol);

  // Update clock every second
  createEffect(() => {
    const tz = resolvedTz();
    const updateTime = () => {
      setCurrentTime(getCurrentTimeInTimezone(tz));
    };
    updateTime();
    const interval = setInterval(updateTime, 1000);
    onCleanup(() => clearInterval(interval));
  });

  // Close dropdown on outside click
  createEffect(() => {
    if (!isOpen()) return;

    const handleClickOutside = (e: MouseEvent) => {
      const target = e.target as Node;
      if (buttonRef && !buttonRef.contains(target)) {
        // Check if click is inside the dropdown portal
        const dropdown = document.getElementById("timezone-dropdown");
        if (dropdown && !dropdown.contains(target)) {
          setIsOpen(false);
        }
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    onCleanup(() => document.removeEventListener("mousedown", handleClickOutside));
  });

  // Update dropdown position when opening
  const openDropdown = () => {
    if (buttonRef) {
      const rect = buttonRef.getBoundingClientRect();
      setDropdownPos({
        top: rect.bottom + 4,
        right: window.innerWidth - rect.right,
      });
    }
    setIsOpen(true);
  };

  // Get sorted timezone list
  const sortedTimezones = getTimezonesSortedByOffset();

  // Select timezone
  const selectTimezone = (timezone: string) => {
    updateSetting("timezone", timezone);
    setIsOpen(false);
  };

  // Check if timezone is currently selected
  const isSelected = (timezone: string) => settings().timezone === timezone;

  // Get offset label for dropdown button
  const offsetLabel = () => getTimezoneOffsetLabel(resolvedTz());

  return (
    <>
      {/* Trigger Button - Shows clock and timezone offset */}
      <button
        ref={buttonRef}
        onClick={() => (isOpen() ? setIsOpen(false) : openDropdown())}
        class={cn(
          "h-8 px-2 flex items-center gap-1.5 text-xs font-mono",
          "text-muted-foreground hover:text-foreground transition-colors"
        )}
        title="Timezone"
      >
        <span class="text-foreground">{currentTime()}</span>
        <span>{offsetLabel()}</span>
        <svg
          width="8"
          height="8"
          viewBox="0 0 8 8"
          fill="none"
          stroke="currentColor"
          stroke-width="1.5"
          class={cn("transition-transform", isOpen() && "rotate-180")}
        >
          <path d="M1 3L4 6L7 3" />
        </svg>
      </button>

      {/* Dropdown Menu - Rendered via Portal to escape parent overflow */}
      <Show when={isOpen()}>
        <Portal>
          <div
            id="timezone-dropdown"
            class={cn(
              "fixed z-[9999]",
              "w-48 max-h-[400px] overflow-hidden",
              "bg-[#1e222d] border border-[#363a45] rounded shadow-xl",
              "flex flex-col"
            )}
            style={{
              top: `${dropdownPos().top}px`,
              right: `${dropdownPos().right}px`,
            }}
          >
            {/* Timezone List */}
            <div class="flex-1 overflow-y-auto scrollbar-hide py-1">
              {/* UTC option */}
              <TimezoneRow
                label="UTC"
                offset=""
                selected={isSelected("UTC")}
                onClick={() => selectTimezone("UTC")}
              />

              {/* Exchange option */}
              <TimezoneRow
                label="Exchange"
                offset=""
                selected={isSelected("EXCHANGE")}
                onClick={() => selectTimezone("EXCHANGE")}
              />

              {/* All timezones sorted by offset */}
              <For each={sortedTimezones}>
                {(tz) => (
                  <TimezoneRow
                    label={tz.label}
                    offset={tz.offset.replace("UTC", "")}
                    selected={isSelected(tz.id)}
                    onClick={() => selectTimezone(tz.id)}
                  />
                )}
              </For>
            </div>

            {/* Clock display at bottom */}
            <div class="px-3 py-2 border-t border-[#363a45] text-xs font-mono text-muted-foreground">
              {currentTime()} {offsetLabel()}
            </div>
          </div>
        </Portal>
      </Show>
    </>
  );
};

/** Individual timezone row in dropdown */
const TimezoneRow: Component<{
  label: string;
  offset: string;
  selected: boolean;
  onClick: () => void;
}> = (props) => {
  return (
    <button
      onClick={props.onClick}
      class={cn(
        "w-full px-3 py-1.5 text-left text-[13px] flex items-center gap-2",
        "hover:bg-[#2a2e39] transition-colors",
        props.selected && "text-foreground"
      )}
    >
      {/* Checkmark on left */}
      <span class="w-4 flex-shrink-0">
        <Show when={props.selected}>
          <svg
            width="14"
            height="14"
            viewBox="0 0 14 14"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path d="M2 7L5.5 10.5L12 4" />
          </svg>
        </Show>
      </span>

      {/* Offset and label */}
      <span class="text-muted-foreground">
        <Show when={props.offset} fallback={props.label}>
          ({props.offset}) {props.label}
        </Show>
      </span>
    </button>
  );
};
