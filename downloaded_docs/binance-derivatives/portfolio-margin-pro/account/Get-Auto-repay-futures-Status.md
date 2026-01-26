On this page

# Get Auto-repay-futures Status(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status#api-description "Direct link to API Description")

Query Auto-repay-futures Status

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/repay-futures-switch`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status#request-weightip "Direct link to Request Weight(IP)")

**30**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status#response-example "Direct link to Response Example")

```prism-code
{  
    "autoRepay": true  //  "true" for turn on the auto-repay futures; "false" for turn off the auto-repay futures   
}
```