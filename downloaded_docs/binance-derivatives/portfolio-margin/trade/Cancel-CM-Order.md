On this page

# Cancel CM Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order#api-description "Direct link to API Description")

Cancel an active LIMIT order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order#http-request "Direct link to HTTP Request")

DELETE `/papi/v1/cm/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Either `orderId` or `origClientOrderId` must be sent.

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order#response-example "Direct link to Response Example")

```prism-code
{  
    "avgPrice": "0.0",  
    "clientOrderId": "myOrder1",  
    "cumQty": "0",  
    "cumBase": "0",  
    "executedQty": "0",  
    "orderId": 283194212,  
    "origQty": "2",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",    
    "status": "CANCELED",            
    "symbol": "BTCUSD_200925",  
    "pair": "BTCUSD",  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1571110484038,  
}
```