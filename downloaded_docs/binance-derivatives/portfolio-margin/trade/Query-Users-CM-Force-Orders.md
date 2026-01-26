On this page

# Query User's CM Force Orders(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#api-description "Direct link to API Description")

Query User's CM Force Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/forceOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **50** without symbol

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| autoCloseType | ENUM | NO | "LIQUIDATION" for liquidation orders, "ADL" for ADL orders. |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 50; max 100. |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

> * If "autoCloseType" is not sent, orders with both of the types will be returned
> * If "startTime" is not sent, data within 7 days before "endTime" can be queried

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "orderId": 165123080,  
    "symbol": "BTCUSD_200925",  
    "pair": "BTCUSD",  
    "status": "FILLED",  
    "clientOrderId": "autoclose-1596542005017000006",  
    "price": "11326.9",  
    "avgPrice": "11326.9",  
    "origQty": "1",  
    "executedQty": "1",  
    "cumBase": "0.00882854",  
    "timeInForce": "IOC",  
    "type": "LIMIT",  
    "reduceOnly": false,  
    "side": "SELL",  
    "positionSide": "BOTH",  
    "origType": "LIMIT",  
    "time": 1596542005019,  
    "updateTime": 1596542005050  
  }  
]
```