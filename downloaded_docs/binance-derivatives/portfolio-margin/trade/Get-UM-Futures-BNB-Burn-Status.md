On this page

# Get UM Futures BNB Burn Status (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#api-description "Direct link to API Description")

Get user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off )

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/feeBurn`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#response-example "Direct link to Response Example")

```prism-code
{  
	"feeBurn": true // "true": Fee Discount On; "false": Fee Discount Off  
}
```