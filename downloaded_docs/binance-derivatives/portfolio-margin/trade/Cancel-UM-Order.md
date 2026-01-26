On this page

# Cancel UM Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#api-description "Direct link to API Description")

Cancel an active UM LIMIT order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#http-request "Direct link to HTTP Request")

DELETE `/papi/v1/um/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Either `orderId` or `origClientOrderId` must be sent.

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order#response-example "Direct link to Response Example")

```prism-code
{  
    "avgPrice": "0.00000",  
    "clientOrderId": "myOrder1",  
    "cumQty": "0",  
    "cumQuote": "0",  
    "executedQty": "0",  
    "orderId": 4611875134427365377,  
    "origQty": "0.40",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "status": "CANCELED",  
    "symbol": "BTCUSDT",  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1571110484038,  
    "selfTradePreventionMode": "NONE",   
    "goodTillDate": 0,  
    "priceMatch": "NONE"    
}
```