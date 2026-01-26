On this page

# Change Position Mode(TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#api-description "Direct link to API Description")

Change user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#http-request "Direct link to HTTP Request")

POST `/dapi/v1/positionSide/dual`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dualSidePosition | STRING | YES | "true": Hedge Mode; "false": One-way Mode |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,  
	"msg": "success"  
}
```