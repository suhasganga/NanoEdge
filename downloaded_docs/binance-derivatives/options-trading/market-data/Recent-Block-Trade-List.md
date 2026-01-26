On this page

# Recent Block Trades List

## API Description[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#api-description "Direct link to API Description")

Get recent block trades

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#http-request "Direct link to HTTP Request")

GET `/eapi/v1/blockTrades`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO | Option trading pair, e.g. BTC-200730-9000-C |
| limit | INT | NO | Number of records; Default: 100 and Max: 500 |

## Response Example[​](/docs/derivatives/options-trading/market-data/Recent-Block-Trade-List#response-example "Direct link to Response Example")

```prism-code
[  
	{  
		"id": 1125899906901081078,  
		"tradeId": 389,  
		"symbol": "ETH-250725-1200-P",  
		"price": "342.40",  
		"qty": "-2167.20",  
		"quoteQty": "-4.90",  
		"side": -1,  
		"time": 1733950676483  
	},  
	{  
		"id": 1125899906901080972,  
		"tradeId": 161,  
		"symbol": "XRP-250904-0.086-P",  
		"price": "3.0",  
		"qty": "-6.0",  
		"quoteQty": "-2.02",  
		"side": -1,  
		"time": 1733950488444  
	}  
]
```