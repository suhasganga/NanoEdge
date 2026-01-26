import { Component } from "solid-js";

export const MyOrders: Component = () => {
  return (
    <div class="flex h-full flex-col items-center justify-center p-4 text-center">
      <svg
        class="w-12 h-12 text-muted-foreground mb-4"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.5"
      >
        <path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
      </svg>
      <h3 class="text-sm font-semibold mb-1">Authentication Required</h3>
      <p class="text-xs text-muted-foreground">
        Connect your API keys to view and manage orders
      </p>
      <p class="text-xs text-muted-foreground/60 mt-4">Coming soon</p>
    </div>
  );
};
