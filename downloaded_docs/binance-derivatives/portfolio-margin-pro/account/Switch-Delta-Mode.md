On this page

# Switch Delta Mode(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#api-description "Direct link to API Description")

Switch the Delta mode for existing PM PRO / PM RETAIL accounts.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/delta-mode`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#request-weightip "Direct link to Request Weight(IP)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deltaEnabled | STRING | YES | `true` to enable Delta mode; `false` to disable Delta mode |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Switch-Delta-Mode#response-example "Direct link to Response Example")

```prism-code
{  
    "msg": "success"  
}
```