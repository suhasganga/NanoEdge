On this page

# Toggle BNB Burn On Futures Trade (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#api-description "Direct link to API Description")

Change user's BNB Fee Discount (Fee Discount On or Fee Discount Off ) on ***EVERY symbol***

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#http-request "Direct link to HTTP Request")

POST `/fapi/v1/feeBurn`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| feeBurn | STRING | YES | "true": Fee Discount On; "false": Fee Discount Off |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Toggle-BNB-Burn-On-Futures-Trade#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,  
	"msg": "success"  
}
```