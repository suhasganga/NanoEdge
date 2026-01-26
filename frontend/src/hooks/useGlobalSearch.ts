import { onMount, onCleanup, Accessor } from "solid-js";

interface UseGlobalSearchOptions {
  isOpen: Accessor<boolean>;
  onOpen: (initialChar?: string) => void;
}

// Keys that should NOT trigger search
const IGNORED_KEYS = new Set([
  // Modifier keys
  "Control", "Alt", "Shift", "Meta", "CapsLock", "NumLock", "ScrollLock",
  // Action keys
  "Escape", "Enter", "Tab", "Backspace", "Delete", "Insert",
  // Navigation keys
  "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight",
  "Home", "End", "PageUp", "PageDown",
  // Function keys
  "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
  // Other special keys
  "PrintScreen", "Pause", "ContextMenu", " ",
]);

/**
 * Global keyboard listener for TradingView-style search.
 * Opens search modal when user types alphanumeric characters anywhere on page.
 *
 * Does NOT trigger on:
 * - Modifier keys alone (Ctrl, Alt, Shift, Meta)
 * - Keyboard shortcuts (Ctrl+C, Ctrl+V, etc.)
 * - Navigation keys (arrows, Tab, Enter, Escape)
 * - Function keys (F1-F12)
 * - When focused on INPUT/TEXTAREA/contentEditable
 * - When search modal is already open
 */
export function useGlobalSearch(options: UseGlobalSearchOptions) {
  let debounceTimer: number | undefined;

  const handleKeyDown = (e: KeyboardEvent) => {
    // Skip if search already open
    if (options.isOpen()) return;

    // Skip if any modifier held (except Shift for capitals)
    if (e.ctrlKey || e.altKey || e.metaKey) return;

    // Skip ignored keys
    if (IGNORED_KEYS.has(e.key)) return;

    // Skip if focused on input element
    const target = e.target as HTMLElement;
    if (
      target.tagName === "INPUT" ||
      target.tagName === "TEXTAREA" ||
      target.tagName === "SELECT" ||
      target.isContentEditable
    ) return;

    // Only trigger on printable characters (length 1)
    if (e.key.length !== 1) return;

    // Prevent the character from being typed elsewhere
    e.preventDefault();

    // Debounce to handle fat-fingering (50ms)
    clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(() => {
      options.onOpen(e.key);
    }, 50);
  };

  onMount(() => {
    document.addEventListener("keydown", handleKeyDown);
  });

  onCleanup(() => {
    document.removeEventListener("keydown", handleKeyDown);
    clearTimeout(debounceTimer);
  });
}
