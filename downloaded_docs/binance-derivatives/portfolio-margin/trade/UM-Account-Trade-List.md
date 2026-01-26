On this page

# UM Account Trade List(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and UM symbol.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/userTrades`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| fromId | LONG | NO | Trade id to fetch from. Default gets most recent trades. |
| limit | INT | NO | Default 500; max 1000. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If `startTime` and `endTime` are both not sent, then the last '7 days' data will be returned.
> * The time between `startTime` and `endTime` cannot be longer than 7 days.
> * The parameter `fromId` cannot be sent with `startTime` or `endTime`.

## Response Example[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "symbol": "BTCUSDT",  
        "id": 67880589,  
        "orderId": 270093109,  
        "side": "SELL",  
        "price": "28511.00",  
        "qty": "0.010",  
        "realizedPnl": "2.58500000",  
        "quoteQty": "285.11000",  
        "commission": "-0.11404400",  
        "commissionAsset": "USDT",  
        "time": 1680688557875,  
        "buyer": false,  
        "maker": false,  
        "positionSide": "BOTH"  
    }  
]
```