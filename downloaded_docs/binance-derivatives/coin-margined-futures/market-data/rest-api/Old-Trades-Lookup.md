On this page

# Old Trades Lookup(MARKET\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#api-description "Direct link to API Description")

Get older market historical trades.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#http-request "Direct link to HTTP Request")

GET `/dapi/v1/historicalTrades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| limit | INT | NO | Default 100; max 500. |
| fromId | LONG | NO | TradeId to fetch from. Default gets most recent trades. |

> * Market trades means trades filled in the order book. Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "id": 595103,  
    "price": "9642.2",  
    "qty": "1",  
    "baseQty": "0.01037108",  
    "time": 1499865549590,  
    "isBuyerMaker": true,  
  }  
]
```