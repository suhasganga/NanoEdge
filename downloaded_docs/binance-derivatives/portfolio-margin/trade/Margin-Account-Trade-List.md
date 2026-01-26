On this page

# Margin Account Trade List (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#api-description "Direct link to API Description")

Margin Account Trade List

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/myTrades`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#weight "Direct link to Weight")

**5**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#parameters "Direct link to Parameters:")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| fromId | LONG | NO | TradeId to fetch from. Default gets most recent trades. |
| limit | INT | NO | Default 500; max 1000. |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

**Notes:**

* If `fromId` is set, it will get trades >= that `fromId`. Otherwise most recent trades are returned.
* Less than 24 hours between `startTime` and `endTime`.

## Response:[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#response "Direct link to Response:")

```prism-code
[  
    {  
        "commission": "0.00006000",  
        "commissionAsset": "BTC",  
        "id": 34,  
        "isBestMatch": true,  
        "isBuyer": false,  
        "isMaker": false,  
        "orderId": 39324,  
        "price": "0.02000000",  
        "qty": "3.00000000",  
        "symbol": "BNBBTC",  
        "time": 1561973357171  
    }  
]
```