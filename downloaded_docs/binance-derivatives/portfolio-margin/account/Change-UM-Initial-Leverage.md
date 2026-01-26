On this page

# Change UM Initial Leverage(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#api-description "Direct link to API Description")

Change user's initial leverage of specific symbol in UM.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#http-request "Direct link to HTTP Request")

POST `/papi/v1/um/leverage`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| leverage | INT | YES | target initial leverage: int from 1 to 125 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage#response-example "Direct link to Response Example")

```prism-code
{  
    "leverage": 21,  
    "maxNotionalValue": "1000000",  
    "symbol": "BTCUSDT"  
}
```