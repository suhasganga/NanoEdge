On this page

# Get Current Position Mode(USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode#api-description "Direct link to API Description")

Get user's position mode (Hedge Mode or One-way Mode ) on ***EVERY symbol***

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode#http-request "Direct link to HTTP Request")

GET `/dapi/v1/positionSide/dual`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode#response-example "Direct link to Response Example")

```prism-code
{  
	"dualSidePosition": true // "true": Hedge Mode; "false": One-way Mode  
}
```