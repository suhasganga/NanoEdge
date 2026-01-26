On this page

# Get BNB Burn Status (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#api-description "Direct link to API Description")

Get user's BNB Fee Discount (Fee Discount On or Fee Discount Off )

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#http-request "Direct link to HTTP Request")

GET `/fapi/v1/feeBurn`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-BNB-Burn-Status#response-example "Direct link to Response Example")

```prism-code
{  
	"feeBurn": true // "true": Fee Discount On; "false": Fee Discount Off  
}
```