On this page

# Query Algo Order (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#api-description "Direct link to API Description")

Check an algo order's status.

* These orders will not be found:
  + order status is `CANCELED` or `EXPIRED` **AND** order has NO filled trade **AND** created time + 3 days < current time
  + order create time + 90 days < current time

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#http-request "Direct link to HTTP Request")

GET `/fapi/v1/algoOrder`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algoId | LONG | NO |  |
| clientAlgoId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

Notes:

> * Either `algoId` or `clientAlgoId` must be sent.
> * `algoId` is self-increment for each specific `symbol`

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order#response-example "Direct link to Response Example")

```prism-code
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
```