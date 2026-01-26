/**
 * Order and position types for market making simulation.
 *
 * These types match the backend hft/mm/types.py definitions.
 */

export type OrderSide = "buy" | "sell";

export type OrderStatus =
  | "pending"
  | "open"
  | "partially_filled"
  | "filled"
  | "cancelled";

export interface SimulatedOrder {
  order_id: string;
  symbol: string;
  exchange: string;
  market: string;
  side: OrderSide;
  price: number;
  quantity: number;
  filled_quantity: number;
  status: OrderStatus;
  tag: string;
  created_at: number;
  updated_at: number;
}

export interface SimulatedPosition {
  symbol: string;
  exchange?: string;
  market?: string;
  quantity: number;
  avg_entry_price: number;
  realized_pnl: number;
  unrealized_pnl: number;
  updated_at?: number;
}

export interface OrderFill {
  order_id: string;
  fill_id: string;
  symbol: string;
  side: OrderSide;
  price: number;
  quantity: number;
  timestamp: number;
}

/**
 * WebSocket message types
 */

export interface OrderUpdateMsg {
  type: "order_update";
  order_id: string;
  symbol: string;
  side: OrderSide;
  price: number;
  quantity: number;
  filled_quantity: number;
  status: OrderStatus;
  tag: string;
  created_at: number;
  updated_at: number;
}

export interface PositionUpdateMsg {
  type: "position_update";
  symbol: string;
  quantity: number;
  avg_entry_price: number;
  realized_pnl: number;
  unrealized_pnl: number;
  updated_at: number;
}

export interface OrderFillMsg {
  type: "order_fill";
  order_id: string;
  fill_id: string;
  symbol: string;
  side: OrderSide;
  price: number;
  quantity: number;
  timestamp: number;
}

export interface OrdersSnapshotMsg {
  type: "orders_snapshot";
  orders: OrderUpdateMsg[];
  position: PositionUpdateMsg | null;
}

export interface HeartbeatMsg {
  type: "heartbeat";
}

export type OrderWebSocketMsg =
  | OrderUpdateMsg
  | PositionUpdateMsg
  | OrderFillMsg
  | OrdersSnapshotMsg
  | HeartbeatMsg;

/**
 * Grid order configuration
 */
export interface GridOrderConfig {
  symbol: string;
  base_price: number;
  spread: number;
  levels?: number;
  base_quantity?: number;
  quantity_scale?: number;
  side?: "both" | "buy" | "sell";
  tag?: string;
}

/**
 * API response types
 */

export interface PlaceOrderResponse {
  status: "success";
  order: SimulatedOrder;
}

export interface CancelOrderResponse {
  status: "success";
  order_id?: string;
  cancelled?: number;
}

export interface GetOrdersResponse {
  orders: SimulatedOrder[];
}

export interface GetPositionResponse {
  position: SimulatedPosition;
}

export interface GetFillsResponse {
  fills: OrderFill[];
}

export interface PlaceGridResponse {
  status: "success";
  orders_placed: number;
  orders: SimulatedOrder[];
}
