On this page

# Reset Market Maker Protection Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#api-description "Direct link to API Description")

Reset MMP, start MMP order again.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#http-request "Direct link to HTTP Request")

POST `/eapi/v1/mmpReset`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | TRUE | underlying, e.g BTCUSDT |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Reset-Market-Maker-Protection-Config#response-example "Direct link to Response Example")

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