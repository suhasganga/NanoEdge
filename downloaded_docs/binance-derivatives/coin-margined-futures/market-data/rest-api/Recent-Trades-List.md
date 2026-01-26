On this page

# Recent Trades List

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#api-description "Direct link to API Description")

Get recent market trades

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#http-request "Direct link to HTTP Request")

GET `/dapi/v1/trades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#request-weight "Direct link to Request Weight")

5

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| limit | INT | NO | Default 500; max 1000. |

* Market trades means trades filled in the order book. Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "id": 28457,  
    "price": "9635.0",  
    "qty": "1",  
    "baseQty": "0.01037883",  
    "time": 1591250192508,  
    "isBuyerMaker": true,  
  }  
]
```