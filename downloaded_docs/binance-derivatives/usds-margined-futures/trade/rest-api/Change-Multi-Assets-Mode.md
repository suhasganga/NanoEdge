On this page

# Change Multi-Assets Mode (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#api-description "Direct link to API Description")

Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on ***Every symbol***

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#http-request "Direct link to HTTP Request")

POST `/fapi/v1/multiAssetsMargin`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| multiAssetsMargin | STRING | YES | "true": Multi-Assets Mode; "false": Single-Asset Mode |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,  
	"msg": "success"  
}
```