On this page

# 24hr Ticker Price Change Statistics

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#api-description "Direct link to API Description")

24 hour rolling window price change statistics.  
**Careful** when accessing this with no symbol.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#http-request "Direct link to HTTP Request")

GET `/fapi/v1/ticker/24hr`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-weight "Direct link to Request Weight")

**1** for a single symbol;  
**40** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |

> * If the symbol is not sent, tickers for all symbols will be returned in an array.

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#response-example "Direct link to Response Example")

> **Response:**

```prism-code
{  
  "symbol": "BTCUSDT",  
  "priceChange": "-94.99999800",  
  "priceChangePercent": "-95.960",  
  "weightedAvgPrice": "0.29628482",  
  "lastPrice": "4.00000200",  
  "lastQty": "200.00000000",  
  "openPrice": "99.00000000",  
  "highPrice": "100.00000000",  
  "lowPrice": "0.10000000",  
  "volume": "8913.30000000",  
  "quoteVolume": "15.30000000",  
  "openTime": 1499783499040,  
  "closeTime": 1499869899040,  
  "firstId": 28385,   // First tradeId  
  "lastId": 28460,    // Last tradeId  
  "count": 76         // Trade count  
}
```

> OR

```prism-code
[  
	{  
  		"symbol": "BTCUSDT",  
  		"priceChange": "-94.99999800",  
  		"priceChangePercent": "-95.960",  
  		"weightedAvgPrice": "0.29628482",  
  		"lastPrice": "4.00000200",  
  		"lastQty": "200.00000000",  
  		"openPrice": "99.00000000",  
  		"highPrice": "100.00000000",  
  		"lowPrice": "0.10000000",  
  		"volume": "8913.30000000",  
  		"quoteVolume": "15.30000000",  
  		"openTime": 1499783499040,  
  		"closeTime": 1499869899040,  
  		"firstId": 28385,   // First tradeId  
  		"lastId": 28460,    // Last tradeId  
  		"count": 76         // Trade count  
	}  
]
```