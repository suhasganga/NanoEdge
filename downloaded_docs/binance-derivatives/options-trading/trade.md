On this page

# New Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade#api-description "Direct link to API Description")

Send a new order.

## HTTP Request[​](/docs/derivatives/options-trading/trade#http-request "Direct link to HTTP Request")

POST `/eapi/v1/order`

## Request Parameters[​](/docs/derivatives/options-trading/trade#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option trading pair, e.g BTC-200730-9000-C |
| side | ENUM | YES | Buy/sell direction: SELL, BUY |
| type | ENUM | YES | Order Type: LIMIT(only support limit) |
| quantity | DECIMAL | YES | Order Quantity |
| price | DECIMAL | NO | Order Price |
| timeInForce | ENUM | NO | Time in force method（Default GTC） |
| reduceOnly | BOOLEAN | NO | Reduce Only（Default false） |
| postOnly | BOOLEAN | NO | Post Only（Default false） |
| newOrderRespType | ENUM | NO | "ACK", "RESULT", Default "ACK" |
| clientOrderId | STRING | NO | User-defined order ID cannot be repeated in pending orders |
| isMmp | BOOLEAN | NO | is market maker protection order, true/false |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

Some parameters are mandatory depending on the order type as follows:

| Type | Mandatory parameters |
| --- | --- |
| LIMIT | timeInForce, quantity, price |

## Response Example[​](/docs/derivatives/options-trading/trade#response-example "Direct link to Response Example")

```prism-code
{  
  "orderId": 4611875134427365377,     // System order number  
  "symbol": "BTC-200730-9000-C",      // Option trading pair  
  "price": "100",                     // Order Price  
  "quantity": "1",                    // Order Quantity  
  "executedQty": "0",                 // Number of executed quantity  
  "side": "BUY",                      // Buy/sell direction  
  "type": "LIMIT",                    // Order type  
  "timeInForce": "GTC",               // Time in force method  
  "reduceOnly": false,                // Order is reduce only Y/N  
  "createTime": 1592465880683,        // Order Time  
  "updateTime": 1566818724722,        // Update time  
  "status": "NEW",                    // Order status  
  "avgPrice": "0",                    // Average price of completed trade  
  "source": "API",  
  "clientOrderId": "",                 // Client order ID  
  "priceScale": 2,  
  "quantityScale": 2,  
  "optionSide": "CALL",  
  "quoteAsset": "USDT",  
  "mmp": false  
}
```