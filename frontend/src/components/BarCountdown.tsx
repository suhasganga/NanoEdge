import { Component, createSignal, createEffect, onCleanup, Show } from "solid-js";
import { cn } from "~/lib/utils";

/**
 * BarCountdown
 *
 * Displays a countdown timer showing time remaining until the current candle closes.
 * Updates every second and resets when a new candle starts.
 */

// Interval durations in seconds
const INTERVAL_SECONDS: Record<string, number> = {
  "1m": 60,
  "5m": 300,
  "15m": 900,
  "30m": 1800,
  "1h": 3600,
  "4h": 14400,
  "1d": 86400,
};

interface BarCountdownProps {
  interval: string;
  visible: boolean;
  class?: string;
}

/**
 * Format seconds into MM:SS or HH:MM:SS
 */
function formatCountdown(seconds: number): string {
  if (seconds < 0) seconds = 0;

  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  if (hours > 0) {
    return `${hours}:${String(minutes).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  }

  return `${minutes}:${String(secs).padStart(2, "0")}`;
}

/**
 * Calculate seconds remaining until next candle close
 */
function getSecondsRemaining(intervalSeconds: number): number {
  const now = Math.floor(Date.now() / 1000);
  const elapsed = now % intervalSeconds;
  return intervalSeconds - elapsed;
}

export const BarCountdown: Component<BarCountdownProps> = (props) => {
  const [countdown, setCountdown] = createSignal("");

  createEffect(() => {
    if (!props.visible) return;

    const intervalSeconds = INTERVAL_SECONDS[props.interval] || 60;

    // Update immediately
    setCountdown(formatCountdown(getSecondsRemaining(intervalSeconds)));

    // Update every second
    const timer = setInterval(() => {
      setCountdown(formatCountdown(getSecondsRemaining(intervalSeconds)));
    }, 1000);

    onCleanup(() => clearInterval(timer));
  });

  return (
    <Show when={props.visible}>
      <div
        class={cn(
          "absolute bottom-1 right-20 z-10",
          "px-2 py-0.5 rounded",
          "bg-[#131722]/80 border border-[#2a2e39]",
          "text-[11px] font-mono text-[#787b86]",
          "select-none pointer-events-none",
          props.class
        )}
      >
        {countdown()}
      </div>
    </Show>
  );
};
