import { createEffect, onCleanup } from "solid-js";
import {
  updateSetting,
  settings,
  PriceScaleMode,
} from "~/stores/chartSettings";

/**
 * Keyboard Shortcuts Hook
 *
 * Provides TradingView-style keyboard shortcuts for chart operations.
 *
 * Shortcuts:
 * - Alt + I: Toggle invert scale
 * - Alt + L: Toggle logarithmic scale
 * - Alt + P: Toggle percentage scale
 * - Alt + A: Toggle auto-scale
 * - Escape: Close menus/dialogs (handled by Kobalte)
 */

export interface KeyboardShortcutHandlers {
  onOpenSettings?: () => void;
  onCloseSettings?: () => void;
}

export function useKeyboardShortcuts(_handlers: KeyboardShortcutHandlers = {}) {
  createEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      // Only handle Alt + key combinations
      if (!event.altKey) return;

      // Ignore if user is typing in an input
      const target = event.target as HTMLElement;
      if (
        target.tagName === "INPUT" ||
        target.tagName === "TEXTAREA" ||
        target.isContentEditable
      ) {
        return;
      }

      const key = event.key.toLowerCase();
      const currentSettings = settings();

      switch (key) {
        case "i":
          // Toggle invert scale
          event.preventDefault();
          updateSetting("invertScale", !currentSettings.invertScale);
          break;

        case "l":
          // Toggle logarithmic scale
          event.preventDefault();
          if (currentSettings.scaleMode === PriceScaleMode.Logarithmic) {
            updateSetting("scaleMode", PriceScaleMode.Normal);
          } else {
            updateSetting("scaleMode", PriceScaleMode.Logarithmic);
          }
          break;

        case "p":
          // Toggle percentage scale
          event.preventDefault();
          if (currentSettings.scaleMode === PriceScaleMode.Percentage) {
            updateSetting("scaleMode", PriceScaleMode.Normal);
          } else {
            updateSetting("scaleMode", PriceScaleMode.Percentage);
          }
          break;

        case "a":
          // Toggle auto-scale
          event.preventDefault();
          updateSetting("autoScale", !currentSettings.autoScale);
          break;
      }
    };

    window.addEventListener("keydown", handleKeyDown);

    onCleanup(() => {
      window.removeEventListener("keydown", handleKeyDown);
    });
  });
}

/**
 * Hook to handle escape key for closing dialogs
 */
export function useEscapeKey(onEscape: () => void, enabled: () => boolean) {
  createEffect(() => {
    if (!enabled()) return;

    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        onEscape();
      }
    };

    window.addEventListener("keydown", handleKeyDown);

    onCleanup(() => {
      window.removeEventListener("keydown", handleKeyDown);
    });
  });
}
