On this page

# Account Trade List (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and symbol.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/dapi/v1/userTrades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#request-weight "Direct link to Request Weight")

**20** with symbol，**40** with pair

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| pair | STRING | NO |  |
| orderId | STRING | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| fromId | LONG | NO | Trade id to fetch from. Default gets most recent trades. |
| limit | INT | NO | Default 50; max 1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Either symbol or pair must be sent
> * Symbol and pair cannot be sent together
> * Pair and fromId cannot be sent together
> * OrderId can only be sent together with symbol
> * If a pair is sent,tickers for all symbols of the pair will be returned
> * The parameter `fromId` cannot be sent with `startTime` or `endTime`
> * If startTime and endTime are both not sent, then the last 7 days' data will be returned.
> * The time between startTime and endTime cannot be longer than 7 days.

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List#response-example "Direct link to Response Example")

```prism-code
[  
	{  
		'symbol': 'BTCUSD_200626',  
	  	'id': 6,  
	  	'orderId': 28,  
	  	'pair': 'BTCUSD',  
	  	'side': 'SELL',  
	  	'price': '8800',  
	  	'qty': '1',  
	  	'realizedPnl': '0',  
	  	'marginAsset': 'BTC',  
	  	'baseQty': '0.01136364',  
	  	'commission': '0.00000454',  
	  	'commissionAsset': 'BTC',  
	  	'time': 1590743483586,  
	  	'positionSide': 'BOTH',  
	  	'buyer': false,  
	  	'maker': false  
	}  
]
```