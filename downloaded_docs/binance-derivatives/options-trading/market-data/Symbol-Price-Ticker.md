On this page

# Index Price

## API Description[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#api-description "Direct link to API Description")

Get spot index price for option underlying.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#http-request "Direct link to HTTP Request")

GET `/eapi/v1/index`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | YES | Spot pair（Option contract underlying asset, e.g BTCUSDT) |

## Response Example[​](/docs/derivatives/options-trading/market-data/Symbol-Price-Ticker#response-example "Direct link to Response Example")

```prism-code
{  
   "time": 1656647305000,  
   "indexPrice": "105917.75" // Current index price  
}
```