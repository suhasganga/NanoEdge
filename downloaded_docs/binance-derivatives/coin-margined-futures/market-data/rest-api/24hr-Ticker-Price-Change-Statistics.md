On this page

# 24hr Ticker Price Change Statistics

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#api-description "Direct link to API Description")

24 hour rolling window price change statistics.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#http-request "Direct link to HTTP Request")

GET `/dapi/v1/ticker/24hr`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-weight "Direct link to Request Weight")

**1** for a single symbol, **40** when the symbol parameter is omitted
**Careful** when accessing this with no symbol.

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| pair | STRING | NO |  |

> * Symbol and pair cannot be sent together
> * If a pair is sent,tickers for all symbols of the pair will be returned
> * If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics#response-example "Direct link to Response Example")

```prism-code
[  
	{  
		"symbol": "BTCUSD_200925",  
	  	"pair": "BTCUSD",  
	  	"priceChange": "136.6",  
	  	"priceChangePercent": "1.436",  
	  	"weightedAvgPrice": "9547.3",  
	  	"lastPrice": "9651.6",  
	  	"lastQty": "1",  
	  	"openPrice": "9515.0",  
	  	"highPrice": "9687.0",  
	  	"lowPrice": "9499.5",  
	  	"volume": "494109",  
	  	"baseVolume": "5192.94797687",  
	  	"openTime": 1591170300000,  
	  	"closeTime": 1591256718418,  
	  	"firstId": 600507, // First tradeId  
	  	"lastId": 697803,  // Last tradeId  
	  	"count": 97297    // Trade count  	  
  	}  
]
```