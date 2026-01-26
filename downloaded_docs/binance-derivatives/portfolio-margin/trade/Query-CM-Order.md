On this page

# Query CM Order(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#api-description "Direct link to API Description")

Check an CM order's status.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

Notes:

> * Either `orderId` or `origClientOrderId` must be sent.
> * These orders will not be found:
>   + order status is `CANCELED` or `EXPIRED`, **AND**
>   + order has NO filled trade, **AND**
>   + created time + 3 days < current time

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-CM-Order#response-example "Direct link to Response Example")

```prism-code
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
    "status": "NEW",  
    "symbol": "BTCUSD_200925",  
    "pair": "BTCUSD",  
    "positionSide": "SHORT",  
    "time": 1579276756075,             // order time  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1579276756075        // update time  
}
```