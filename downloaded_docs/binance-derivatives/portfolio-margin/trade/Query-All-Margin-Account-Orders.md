On this page

# Query All Margin Account Orders (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#api-description "Direct link to API Description")

Query All Margin Account Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/allOrders`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#weight "Direct link to Weight")

**100**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#parameters "Direct link to Parameters:")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 500; max 500. |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

**Notes:**

* If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
* For some historical orders cummulativeQuoteQty will be < 0, meaning the data is not available at this time.

## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-All-Margin-Account-Orders#response "Direct link to Response:")

```prism-code
[  
      {  
          "clientOrderId": "D2KDy4DIeS56PvkM13f8cP",  
          "cummulativeQuoteQty": "0.00000000",  
          "executedQty": "0.00000000",  
          "icebergQty": "0.00000000",  
          "isWorking": false,  
          "orderId": 41295,  
          "origQty": "5.31000000",  
          "price": "0.22500000",  
          "side": "SELL",  
          "status": "CANCELED",  
          "stopPrice": "0.18000000",  
          "symbol": "BNBBTC",  
          "time": 1565769338806,  
          "timeInForce": "GTC",  
          "type": "TAKE_PROFIT_LIMIT",  
          "updateTime": 1565769342148，  
          "accountId": 152950866,  
          "selfTradePreventionMode": "EXPIRE_TAKER",  
          "preventedMatchId": null,  
          "preventedQuantity": null  
      }  
]
```