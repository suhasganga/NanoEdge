On this page

# BNB transfer (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#api-description "Direct link to API Description")

Transfer BNB in and out of UM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#http-request "Direct link to HTTP Request")

POST `/papi/v1/bnb-transfer`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#request-weightip "Direct link to Request Weight(IP)")

**750**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| amount | DECIMAL | YES |  |
| transferSide | STRING | YES | "TO\_UM","FROM\_UM" |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

> * The endpoint can only be called 10 times per 10 minutes in a rolling manner

## Response Example[​](/docs/derivatives/portfolio-margin/account/BNB-transfer#response-example "Direct link to Response Example")

```prism-code
{  
    "tranId": 100000001       //transaction id  
}  
```