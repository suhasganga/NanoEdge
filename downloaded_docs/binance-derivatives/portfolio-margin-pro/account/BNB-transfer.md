On this page

# BNB transfer(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#api-description "Direct link to API Description")

BNB transfer can be between Margin Account and USDM Account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/bnb-transfer`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#request-weightip "Direct link to Request Weight(IP)")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| amount | DECIMAL | YES |  |
| transferSide | STRING | YES | "TO\_UM","FROM\_UM" |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * You can only use this function 2 times per 10 minutes in a rolling manner

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/BNB-transfer#response-example "Direct link to Response Example")

```prism-code
{  
     "tranId": 100000001  
}
```