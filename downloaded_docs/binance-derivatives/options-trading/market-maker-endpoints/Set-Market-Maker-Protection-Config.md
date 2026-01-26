On this page

# Set Market Maker Protection Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#api-description "Direct link to API Description")

Set config for MMP.
Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this mechanism is able to prevent mass trading in short period time. Once market maker's account branches the threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate market and modify order price.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#http-request "Direct link to HTTP Request")

POST `/eapi/v1/mmpSet`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | TRUE | underlying, e.g BTCUSDT |
| windowTimeInMilliseconds | LONG | TRUE | MMP Interval in milliseconds; Range (0,5000] |
| frozenTimeInMilliseconds | LONG | TRUE | MMP frozen time in milliseconds, if set to 0 manual reset is required |
| qtyLimit | DECIMAL | TRUE | quantity limit |
| deltaLimit | DECIMAL | TRUE | net delta limit |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#response-example "Direct link to Response Example")

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