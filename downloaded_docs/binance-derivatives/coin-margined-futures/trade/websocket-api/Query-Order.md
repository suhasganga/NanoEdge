On this page

# Query Order (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#api-description "Direct link to API Description")

Check an order's status.

* These orders will not be found:
  + order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  + order create time + 90 days < current time

## Method[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#method "Direct link to Method")

`order.status`

## Request[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#request "Direct link to Request")

```prism-code
{  
    "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
    "method": "order.status",  
    "params": {  
        "apiKey": "HMOchcfii9ZRZnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGPHQj1lGdTjR",  
        "orderId": 328999071,  
        "symbol": "BTCUSD_PERP",  
        "timestamp": 1703441060152,  
        "signature": "ba48184fc38a71d03d2b5435bd67c1206e3191e989fe99bda1bc643a880dfdbf"  
    }  
}
```

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

Notes:

> * Either `orderId` or `origClientOrderId` must be sent.
> * `orderId` is self-increment for each specific `symbol`

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order#response-example "Direct link to Response Example")

```prism-code
{  
    "id": "0ce5d070-a5e5-4ff2-b57f-1556741a4204",  
    "status": 200,  
    "result": {  
        "orderId": 328999071,  
        "symbol": "BTCUSD_PERP",  
        "pair": "BTCUSD",  
        "status": "NEW",  
        "clientOrderId": "ArY8Ng1rln0s9x3fclmAHy",  
        "price": "58000",  
        "avgPrice": "0.00",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumBase": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "closePosition": false,  
        "side": "BUY",  
        "positionSide": "LONG",  
        "stopPrice": "0",  
        "workingType": "CONTRACT_PRICE",  
        "priceProtect": false,  
        "origType": "LIMIT",  
        "selfTradePreventionMode": "EXPIRE_TAKER",  
        "time": 1733740063619,  
        "updateTime": 1733740063619,  
        "priceMatch": "NONE"  
    },  
    "rateLimits": [  
        {  
            "rateLimitType": "REQUEST_WEIGHT",  
            "interval": "MINUTE",  
            "intervalNum": 1,  
            "limit": 2400,  
            "count": 6  
        }  
    ]  
}
```