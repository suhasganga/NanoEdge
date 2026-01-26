On this page

# Get Market Maker Protection Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints#api-description "Direct link to API Description")

Get config for MMP.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints#http-request "Direct link to HTTP Request")

GET `/eapi/v1/mmp (HMAC SHA256)`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | TRUE | underlying, e.g BTCUSDT |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints#response-example "Direct link to Response Example")

```prism-code
{  
    "underlyingId": 2,  
    "underlying": "BTCUSDT",  
    "windowTimeInMilliseconds": 3000,  
    "frozenTimeInMilliseconds": 300000,  
    "qtyLimit": "2",  
    "deltaLimit": "2.3",  
    "lastTriggerTime": 0  
}
```