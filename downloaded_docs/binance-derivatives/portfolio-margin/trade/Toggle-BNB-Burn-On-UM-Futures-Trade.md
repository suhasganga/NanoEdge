On this page

# Toggle BNB Burn On UM Futures Trade (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#api-description "Direct link to API Description")

Change user's BNB Fee Discount for UM Futures (Fee Discount On or Fee Discount Off ) on ***EVERY symbol***

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#http-request "Direct link to HTTP Request")

POST `/papi/v1/um/feeBurn`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| feeBurn | STRING | YES | "true": Fee Discount On; "false": Fee Discount Off |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

* The BNB would not be collected from UM-PM account to the Portfolio Margin account.

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,  
	"msg": "success"  
}
```