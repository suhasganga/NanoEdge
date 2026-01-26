On this page

# Change Margin Type(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#api-description "Direct link to API Description")

Change symbol level margin type

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#http-request "Direct link to HTTP Request")

POST `/fapi/v1/marginType`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| marginType | ENUM | YES | ISOLATED, CROSSED |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,  
	"msg": "success"  
}
```