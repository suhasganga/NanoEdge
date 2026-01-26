On this page

# Change Margin Type (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#api-description "Direct link to API Description")

Change user's margin type in the specific symbol market.For Hedge Mode, LONG and SHORT positions of one symbol use the same margin type.  
With ISOLATED margin type, margins of the LONG and SHORT positions are isolated from each other.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#http-request "Direct link to HTTP Request")

POST `/dapi/v1/marginType`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| marginType | ENUM | YES | ISOLATED, CROSSED |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,  
	"msg": "success"  
}
```