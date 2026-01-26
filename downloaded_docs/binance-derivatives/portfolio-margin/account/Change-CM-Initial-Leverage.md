On this page

# Change CM Initial Leverage (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#api-description "Direct link to API Description")

Change user's initial leverage of specific symbol in CM.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#http-request "Direct link to HTTP Request")

POST `/papi/v1/cm/leverage`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| leverage | INT | YES | target initial leverage: int from 1 to 125 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#response-example "Direct link to Response Example")

```prism-code
{  
    "leverage": 21,  
    "maxQty": "1000",  
    "symbol": "BTCUSD_200925"  
}
```