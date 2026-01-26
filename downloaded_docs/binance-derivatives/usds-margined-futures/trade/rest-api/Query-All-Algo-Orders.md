On this page

# Query All Algo Orders (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#api-description "Direct link to API Description")

Get all algo orders; active, CANCELED, TRIGGERED or FINISHED .

* These orders will not be found:
  + order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  + order create time + 90 days < current time

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#http-request "Direct link to HTTP Request")

GET `/fapi/v1/allAlgoOrders`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| algoId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| page | INT | NO |  |
| limit | INT | NO | Default 500; max 1000. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

**Notes:**

> * If `algoId` is set, it will get orders >= that `algoId`. Otherwise most recent orders are returned.
> * The query time period must be less then 7 days( default as the recent 7 days).

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders#response-example "Direct link to Response Example")

```prism-code
[  
   {  
       "algoId": 2146760,  
       "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
       "algoType": "CONDITIONAL",  
       "orderType": "TAKE_PROFIT",  
       "symbol": "BNBUSDT",  
       "side": "SELL",  
       "positionSide": "BOTH",  
       "timeInForce": "GTC",  
       "quantity": "0.01",  
       "algoStatus": "CANCELED",  
       "actualOrderId": "",  
       "actualPrice": "0.00000",  
       "triggerPrice": "750.000",  
       "price": "750.000",  
       "icebergQuantity": null,  
       "tpTriggerPrice": "0.000",  
       "tpPrice": "0.000",  
       "slTriggerPrice": "0.000",  
       "slPrice": "0.000",  
       "tpOrderType": "",  
       "selfTradePreventionMode": "EXPIRE_MAKER",  
       "workingType": "CONTRACT_PRICE",  
       "priceMatch": "NONE",  
       "closePosition": false,  
       "priceProtect": false,  
       "reduceOnly": false,  
       "createTime": 1750485492076,  
       "updateTime": 1750514545091,  
       "triggerTime": 0,  
       "goodTillDate": 0  
   }  
]
```