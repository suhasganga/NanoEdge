import { Component, createSignal } from "solid-js";
import { Tabs } from "~/components/ui/Tabs";
import { MarketStatsBar } from "./MarketStatsBar";
import { OrderBook } from "./OrderBook";
import { RecentTrades } from "./RecentTrades";
import { MyOrders } from "~/mm/MyOrders";

interface TradingSidebarProps {
  symbol: string;
}

export const TradingSidebar: Component<TradingSidebarProps> = (props) => {
  const [activeTab, setActiveTab] = createSignal("book");

  return (
    <div class="flex h-full flex-col bg-card">
      {/* Market Stats - Always visible at top */}
      <MarketStatsBar symbol={props.symbol} />

      {/* Tabs */}
      <Tabs.Root
        value={activeTab()}
        onChange={setActiveTab}
        class="flex-1 flex flex-col min-h-0"
      >
        <Tabs.List class="shrink-0 border-b border-border">
          <Tabs.Trigger value="book">Book</Tabs.Trigger>
          <Tabs.Trigger value="trades">Trades</Tabs.Trigger>
          <Tabs.Trigger value="orders">
            My Orders
          </Tabs.Trigger>
        </Tabs.List>

        <Tabs.Content value="book" class="flex-1 min-h-0 overflow-hidden">
          <OrderBook symbol={props.symbol} />
        </Tabs.Content>

        <Tabs.Content value="trades" class="flex-1 min-h-0 overflow-hidden">
          <RecentTrades symbol={props.symbol} />
        </Tabs.Content>

        <Tabs.Content value="orders" class="flex-1 min-h-0 overflow-hidden">
          <MyOrders symbol={props.symbol} />
        </Tabs.Content>
      </Tabs.Root>
    </div>
  );
};
