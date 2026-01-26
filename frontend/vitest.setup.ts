import { vi } from "vitest";
import { WebSocket } from "mock-socket";

// Make mock WebSocket available globally
global.WebSocket = WebSocket as unknown as typeof globalThis.WebSocket;

// Mock requestAnimationFrame for throttling tests
global.requestAnimationFrame = vi.fn((cb) => {
  setTimeout(cb, 16);
  return 0;
});

global.cancelAnimationFrame = vi.fn();
