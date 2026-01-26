On this page

# ENUM Definitions

This will apply for both REST API and WebSocket API.

## Symbol status (status)[​](/docs/binance-spot-api-docs/enums#symbol-status-status "Direct link to Symbol status (status)")

* `TRADING`
* `END_OF_DAY`
* `HALT`
* `BREAK`

## Account and Symbol Permissions (permissions)[​](/docs/binance-spot-api-docs/enums#account-and-symbol-permissions-permissions "Direct link to Account and Symbol Permissions (permissions)")

* `SPOT`
* `MARGIN`
* `LEVERAGED`
* `TRD_GRP_002`
* `TRD_GRP_003`
* `TRD_GRP_004`
* `TRD_GRP_005`
* `TRD_GRP_006`
* `TRD_GRP_007`
* `TRD_GRP_008`
* `TRD_GRP_009`
* `TRD_GRP_010`
* `TRD_GRP_011`
* `TRD_GRP_012`
* `TRD_GRP_013`
* `TRD_GRP_014`
* `TRD_GRP_015`
* `TRD_GRP_016`
* `TRD_GRP_017`
* `TRD_GRP_018`
* `TRD_GRP_019`
* `TRD_GRP_020`
* `TRD_GRP_021`
* `TRD_GRP_022`
* `TRD_GRP_023`
* `TRD_GRP_024`
* `TRD_GRP_025`

## Order status (status)[​](/docs/binance-spot-api-docs/enums#order-status-status "Direct link to Order status (status)")

| Status | Description |
| --- | --- |
| `NEW` | The order has been accepted by the engine. |
| `PENDING_NEW` | The order is in a pending phase until the working order of an order list has been fully filled. |
| `PARTIALLY_FILLED` | A part of the order has been filled. |
| `FILLED` | The order has been completed. |
| `CANCELED` | The order has been canceled by the user. |
| `PENDING_CANCEL` | Currently unused |
| `REJECTED` | The order was not accepted by the engine and not processed. |
| `EXPIRED` | The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill)   or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance) |
| `EXPIRED_IN_MATCH` | The order was expired by the exchange due to STP. (e.g. an order with `EXPIRE_TAKER` will match with existing orders on the book with the same account or same `tradeGroupId`) |

## Order List Status (listStatusType)[​](/docs/binance-spot-api-docs/enums#order-list-status-liststatustype "Direct link to Order List Status (listStatusType)")

| Status | Description |
| --- | --- |
| `RESPONSE` | This is used when the ListStatus is responding to a failed action. (E.g. order list placement or cancellation) |
| `EXEC_STARTED` | The order list has been placed or there is an update to the order list status. |
| `UPDATED` | The clientOrderId of an order in the order list has been changed. |
| `ALL_DONE` | The order list has finished executing and thus is no longer active. |

## Order List Order Status (listOrderStatus)[​](/docs/binance-spot-api-docs/enums#order-list-order-status-listorderstatus "Direct link to Order List Order Status (listOrderStatus)")

| Status | Description |
| --- | --- |
| `EXECUTING` | Either an order list has been placed or there is an update to the status of the list. |
| `ALL_DONE` | An order list has completed execution and thus no longer active. |
| `REJECT` | The List Status is responding to a failed action either during order placement or order canceled. |

## ContingencyType[​](/docs/binance-spot-api-docs/enums#contingencytype "Direct link to ContingencyType")

* `OCO`
* `OTO`

## AllocationType[​](/docs/binance-spot-api-docs/enums#allocationtype "Direct link to AllocationType")

* `SOR`

## Order types (orderTypes, type)[​](/docs/binance-spot-api-docs/enums#order-types-ordertypes-type "Direct link to Order types (orderTypes, type)")

* `LIMIT`
* `MARKET`
* `STOP_LOSS`
* `STOP_LOSS_LIMIT`
* `TAKE_PROFIT`
* `TAKE_PROFIT_LIMIT`
* `LIMIT_MAKER`

## Order Response Type (newOrderRespType)[​](/docs/binance-spot-api-docs/enums#order-response-type-neworderresptype "Direct link to Order Response Type (newOrderRespType)")

* `ACK`
* `RESULT`
* `FULL`

## Working Floor[​](/docs/binance-spot-api-docs/enums#working-floor "Direct link to Working Floor")

* `EXCHANGE`
* `SOR`

## Order side (side)[​](/docs/binance-spot-api-docs/enums#order-side-side "Direct link to Order side (side)")

* `BUY`
* `SELL`

## Time in force (timeInForce)[​](/docs/binance-spot-api-docs/enums#time-in-force-timeinforce "Direct link to Time in force (timeInForce)")

This sets how long an order will be active before expiration.

| Status | Description |
| --- | --- |
| `GTC` | Good Til Canceled   An order will be on the book unless the order is canceled. |
| `IOC` | Immediate Or Cancel   An order will try to fill the order as much as it can before the order expires. |
| `FOK` | Fill or Kill   An order will expire if the full order cannot be filled upon execution. |

## Rate limiters (rateLimitType)[​](/docs/binance-spot-api-docs/enums#rate-limiters-ratelimittype "Direct link to Rate limiters (rateLimitType)")

* REQUEST\_WEIGHT

```prism-code
{  
    "rateLimitType": "REQUEST_WEIGHT",  
    "interval": "MINUTE",  
    "intervalNum": 1,  
    "limit": 6000  
}
```

* ORDERS

```prism-code
{  
    "rateLimitType": "ORDERS",  
    "interval": "SECOND",  
    "intervalNum": 1,  
    "limit": 10  
}
```

* RAW\_REQUESTS

```prism-code
{  
    "rateLimitType": "RAW_REQUESTS",  
    "interval": "MINUTE",  
    "intervalNum": 5,  
    "limit": 61000  
}
```

## Rate limit intervals (interval)[​](/docs/binance-spot-api-docs/enums#rate-limit-intervals-interval "Direct link to Rate limit intervals (interval)")

* SECOND
* MINUTE
* DAY

## STP Modes[​](/docs/binance-spot-api-docs/enums#stp-modes "Direct link to STP Modes")

Read [Self Trade Prevention (STP) FAQ](/docs/binance-spot-api-docs/faqs/stp_faq) to learn more.

* `NONE`
* `EXPIRE_MAKER`
* `EXPIRE_TAKER`
* `EXPIRE_BOTH`
* `DECREMENT`
* `TRANSFER`