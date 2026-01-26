On this page

# Get Delta Mode Status(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#api-description "Direct link to API Description")

Query the Delta mode status of current account.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/delta-mode`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#request-weightip "Direct link to Request Weight(IP)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Get-Delta-Mode-Status#response-example "Direct link to Response Example")

```prism-code
{  
    "deltaEnabled": false  
}
```