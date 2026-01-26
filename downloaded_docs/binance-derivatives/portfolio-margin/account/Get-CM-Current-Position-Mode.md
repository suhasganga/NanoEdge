On this page

# Get CM Current Position Mode(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode#api-description "Direct link to API Description")

Get user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/positionSide/dual`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode#response-example "Direct link to Response Example")

```prism-code
{  
  "dualSidePosition": true // "true": Hedge Mode; "false": One-way Mode  
}
```