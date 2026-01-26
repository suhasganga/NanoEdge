On this page

# Account Trade List (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and symbol.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/fapi/v1/userTrades`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO | This can only be used in combination with `symbol` |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| fromId | LONG | NO | Trade id to fetch from. Default gets most recent trades. |
| limit | INT | NO | Default 500; max 1000. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If `startTime` and `endTime` are both not sent, then the last 7 days' data will be returned.
> * The time between `startTime` and `endTime` cannot be longer than 7 days.
> * The parameter `fromId` cannot be sent with `startTime` or `endTime`.
> * Only support querying trade in the past 6 months

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#response-example "Direct link to Response Example")

```prism-code
[  
  {  
  	"buyer": false,  
  	"commission": "-0.07819010",  
  	"commissionAsset": "USDT",  
  	"id": 698759,  
  	"maker": false,  
  	"orderId": 25851813,  
  	"price": "7819.01",  
  	"qty": "0.002",  
  	"quoteQty": "15.63802",  
  	"realizedPnl": "-0.91539999",  
  	"side": "SELL",  
  	"positionSide": "SHORT",  
  	"symbol": "BTCUSDT",  
  	"time": 1569514978020  
  }  
]
```