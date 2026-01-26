On this page

# Transfer LDUSDT/RWUSD for Portfolio Margin(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#api-description "Direct link to API Description")

Transfer LDUSDT/RWUSD as collateral for all types of Portfolio Margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/earn-asset-transfer`

## Request Weight(UID)[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#request-weightuid "Direct link to Request Weight(UID)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES | `LDUSDT` and `RWUSD` |
| transferType | STRING | YES | `EARN_TO_FUTURE` /`FUTURE_TO_EARN` |
| amount | DECIMAL | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin#response-example "Direct link to Response Example")

```prism-code
{  
  "msg":"success"  
}
```