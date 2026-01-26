On this page

# Query User's UM Force Orders (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#api-description "Direct link to API Description")

Query User's UM Force Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/forceOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **50** without symbol

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| autoCloseType | ENUM | NO | `LIQUIDATION` for liquidation orders, `ADL` for ADL orders. |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 50; max 100. |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

> * If `autoCloseType` is not sent, orders with both of the types will be returned
> * If `startTime` is not sent, data within 7 days before `endTime` can be queried

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "orderId": 6071832819,   
    "symbol": "BTCUSDT",   
    "status": "FILLED",   
    "clientOrderId": "autoclose-1596107620040000020",   
    "price": "10871.09",   
    "avgPrice": "10913.21000",   
    "origQty": "0.001",   
    "executedQty": "0.001",   
    "cumQuote": "10.91321",   
    "timeInForce": "IOC",   
    "type": "LIMIT",   
    "reduceOnly": false,   
    "side": "SELL",   
    "positionSide": "BOTH",   
    "origType": "LIMIT",   
    "time": 1596107620044,   
    "updateTime": 1596107620087  
  }  
]
```