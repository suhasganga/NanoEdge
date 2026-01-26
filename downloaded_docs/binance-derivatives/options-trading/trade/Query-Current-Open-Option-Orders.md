On this page

# Query Current Open Option Orders (USER\_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#api-description "Direct link to API Description")

Query current all open orders, status: ACCEPTED PARTIALLY\_FILLED

## HTTP Request[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#http-request "Direct link to HTTP Request")

GET `/eapi/v1/openOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO | return all orders if don't pass, Option trading pair, e.g BTC-200730-9000-C, |
| orderId | LONG | NO | Returns the orderId and subsequent orders, the most recent order is returned by default |
| startTime | LONG | NO | Start Time |
| endTime | LONG | NO | End Time |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/trade/Query-Current-Open-Option-Orders#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "orderId": 4611875134427365377,     // System order number  
    "symbol": "BTC-200730-9000-C",      // Option trading pair  
    "price": "100",                     // Order Price  
    "quantity": "1",                    // Order Quantity  
    "executedQty": "0",                 // Number of completed trades  
    "side": "BUY",                      // Buy/sell direction  
    "type": "LIMIT",                    // Order type  
    "timeInForce": "GTC",               // Time in force method  
    "reduceOnly": false,                // Order is reduce only Y/N  
    "createTime": 1592465880683,        // Order Time  
    "updateTime": 1592465880683,        // Update Time  
    "status": "NEW",                    // Order status  
    "avgPrice": "0",                    // Average price of completed trade  
    "clientOrderId": "",                 // Client order ID           
    "priceScale": 2,  
    "quantityScale": 2,  
    "optionSide": "CALL",  
    "quoteAsset": "USDT",  
    "mmp": false  
  }  
]
```