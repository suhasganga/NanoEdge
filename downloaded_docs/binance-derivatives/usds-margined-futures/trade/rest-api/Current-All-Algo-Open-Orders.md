On this page

# Current All Algo Open Orders (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#api-description "Direct link to API Description")

Get all algo open orders on a symbol.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#http-request "Direct link to HTTP Request")

GET `/fapi/v1/openAlgoOrders`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol; **40** when the symbol parameter is omitted

**Careful** when accessing this with no symbol.

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algoType | STRING | NO |  |
| symbol | STRING | NO |  |
| algoId | LONG | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If the symbol is not sent, orders for all symbols will be returned in an array.

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#response-example "Direct link to Response Example")

```prism-code
[  
   {  
       "algoId": 2148627,  
       "clientAlgoId": "MRumok0dkhrP4kCm12AHaB",  
       "algoType": "CONDITIONAL",  
       "orderType": "TAKE_PROFIT",  
       "symbol": "BNBUSDT",  
       "side": "SELL",  
       "positionSide": "BOTH",  
       "timeInForce": "GTC",  
       "quantity": "0.01",  
       "algoStatus": "NEW",  
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
       "createTime": 1750514941540,  
       "updateTime": 1750514941540,  
       "triggerTime": 0,  
       "goodTillDate": 0  
   }  
]
```