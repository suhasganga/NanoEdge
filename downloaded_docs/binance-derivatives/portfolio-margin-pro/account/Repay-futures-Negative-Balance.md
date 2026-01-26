On this page

# Repay futures Negative Balance(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance#api-description "Direct link to API Description")

Repay futures Negative Balance

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/repay-futures-negative-balance`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance#request-weightip "Direct link to Request Weight(IP)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | STRING | NO | SPOT or MARGIN，default SPOT｜ |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance#response-example "Direct link to Response Example")

```prism-code
{  
    "msg": "success"  
}
```