On this page

# Query All CM Orders (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#api-description "Direct link to API Description")

Get all account CM orders; active, canceled, or filled.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/allOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **40** with pair

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| pair | STRING | NO |  |
| orderId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 50; max 100. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Either `symbol` or `pair` must be sent.
> * If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned.
> * These orders will not be found:
>   + order status is `CANCELED` or `EXPIRED`, **AND**
>   + order has NO filled trade, **AND**
>   + created time + 3 days < current time

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "avgPrice": "0.0",  
    "clientOrderId": "abc",  
    "cumBase": "0",  
    "executedQty": "0",  
    "orderId": 1917641,  
    "origQty": "0.40",  
    "origType": "LIMIT",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "status": "NEW",  
    "symbol": "BTCUSD_200925",  
    "pair": "BTCUSD",  
    "time": 1579276756075,              // order time  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1579276756075       // update time  
  }  
]
```