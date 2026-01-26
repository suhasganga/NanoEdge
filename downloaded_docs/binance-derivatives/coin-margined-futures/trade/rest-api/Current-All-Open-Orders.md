On this page

# Current All Open Orders (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#api-description "Direct link to API Description")

Get all open orders on a symbol. **Careful** when accessing this with no symbol.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#http-request "Direct link to HTTP Request")

GET `/dapi/v1/openOrders`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#request-weight "Direct link to Request Weight")

**1** for a single symbol, **40** for mutltiple symbols

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| pair | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders#response-example "Direct link to Response Example")

```prism-code
[  
  {  
  	"avgPrice": "0.0",  
  	"clientOrderId": "abc",  
  	"cumBase": "0",  
  	"executedQty": "0",  
  	"orderId": 1917641,  
  	"origQty": "0.40",  
  	"origType": "TRAILING_STOP_MARKET",  
  	"price": "0",  
  	"reduceOnly": false,  
  	"side": "BUY",  
  	"positionSide": "SHORT",  
  	"status": "NEW",  
  	"stopPrice": "9300",				// please ignore when order type is TRAILING_STOP_MARKET  
  	"closePosition": false,   			// if Close-All  
  	"symbol": "BTCUSD_200925",  
  	"time": 1579276756075,				// order time  
  	"timeInForce": "GTC",  
  	"type": "TRAILING_STOP_MARKET",  
  	"activatePrice": "9020",			// activation price, only return with TRAILING_STOP_MARKET order  
  	"priceRate": "0.3",					// callback rate, only return with TRAILING_STOP_MARKET order  
  	"updateTime": 1579276756075,		// update time  
  	"workingType": "CONTRACT_PRICE",  
  	"priceProtect": false,              // if conditional order trigger is protected  
  	"priceMatch": "NONE",               //price match mode  
  	"selfTradePreventionMode": "NONE"   //self trading preventation mode  
  }  
]
```