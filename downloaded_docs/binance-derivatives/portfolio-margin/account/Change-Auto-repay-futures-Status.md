On this page

# Change Auto-repay-futures Status(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#api-description "Direct link to API Description")

Change Auto-repay-futures Status

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#http-request "Direct link to HTTP Request")

POST `/papi/v1/repay-futures-switch`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#request-weightip "Direct link to Request Weight(IP)")

**750**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| autoRepay | STRING | YES | Default: `true`; `false` for turn off the auto-repay futures negative balance function |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#response-example "Direct link to Response Example")

```prism-code
{  
    "msg": "success"  
}
```