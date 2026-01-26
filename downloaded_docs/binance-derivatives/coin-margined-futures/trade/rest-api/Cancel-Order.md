On this page

# Cancel Order (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Order#api-description "Direct link to API Description")

Cancel an active order.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Order#http-request "Direct link to HTTP Request")

DELETE `/dapi/v1/order`

**Weight:**
**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Either `orderId` or `origClientOrderId` must be sent.

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Order#response-example "Direct link to Response Example")

```prism-code
{  
 	"avgPrice": "0.0",  
 	"clientOrderId": "myOrder1",  
 	"cumQty": "0",  
 	"cumBase": "0",  
 	"executedQty": "0",  
 	"orderId": 283194212,  
 	"origQty": "11",  
 	"origType": "TRAILING_STOP_MARKET",  
  	"price": "0",  
  	"reduceOnly": false,  
  	"side": "BUY",  
  	"positionSide": "SHORT", 			  
  	"status": "CANCELED",  
  	"stopPrice": "9300",				// please ignore when order type is TRAILING_STOP_MARKET  
  	"closePosition": false,   			// if Close-All  
  	"symbol": "BTCUSD_200925",  
  	"pair": "BTCUSD",  
  	"timeInForce": "GTC",  
  	"type": "TRAILING_STOP_MARKET",  
  	"activatePrice": "9020",			// activation price, only return with TRAILING_STOP_MARKET order  
  	"priceRate": "0.3",					// callback rate, only return with TRAILING_STOP_MARKET order  
 	"updateTime": 1571110484038,  
 	"workingType": "CONTRACT_PRICE",  
 	"priceProtect": false,              // if conditional order trigger is protected  
 	"priceMatch": "NONE",               //price match mode  
 	"selfTradePreventionMode": "NONE"   //self trading preventation mode  
}
```