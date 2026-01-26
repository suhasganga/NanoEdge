On this page

# Change Initial Leverage(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#api-description "Direct link to API Description")

Change user's initial leverage of specific symbol market.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#http-request "Direct link to HTTP Request")

POST `/fapi/v1/leverage`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| leverage | INT | YES | target initial leverage: int from 1 to 125 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#response-example "Direct link to Response Example")

```prism-code
{  
 	"leverage": 21,  
 	"maxNotionalValue": "1000000",  
 	"symbol": "BTCUSDT"  
}
```