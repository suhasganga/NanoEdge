On this page

# Query All Current CM Open Orders(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders#api-description "Direct link to API Description")

Get all open orders on a symbol.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders#http-request "Direct link to HTTP Request")

`GET /papi/v1/cm/openOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted
**Careful** when accessing this with no symbol.

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| pair | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If the symbol is not sent, orders for all symbols will be returned in an array.

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders#response-example "Direct link to Response Example")

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
    "pair":"BTCUSD",  
    "time": 1579276756075,              // order time  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1579276756075        // update time  
  }  
]
```