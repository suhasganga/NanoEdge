On this page

# Change CM Position Mode(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/Change-CM-Position-Mode#api-description "Direct link to API Description")

Change user's position mode (Hedge Mode or One-way Mode ) on EVERY symbol in CM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Change-CM-Position-Mode#http-request "Direct link to HTTP Request")

POST `/papi/v1/cm/positionSide/dual`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Change-CM-Position-Mode#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Change-CM-Position-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dualSidePosition | STRING | YES | "true": Hedge Mode; "false": One-way Mode |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Change-CM-Position-Mode#response-example "Direct link to Response Example")

```prism-code
{  
    "code": 200,  
    "msg": "success"  
}
```