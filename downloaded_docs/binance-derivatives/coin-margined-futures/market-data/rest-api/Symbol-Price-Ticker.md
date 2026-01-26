On this page

# Symbol Price Ticker

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#api-description "Direct link to API Description")

Latest price for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#http-request "Direct link to HTTP Request")

GET `/dapi/v1/ticker/price`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#request-weight "Direct link to Request Weight")

**1** for a single symbol, **2** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| pair | STRING | NO |  |

> * Symbol and pair cannot be sent together
> * If a pair is sent,tickers for all symbols of the pair will be returned
> * If either a pair or symbol is sent, tickers for all symbols of all pairs will be returned

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker#response-example "Direct link to Response Example")

```prism-code
[  
	{  
  		"symbol": "BTCUSD_200626",	  
  		"ps": "9647.8",  			// pair   
  		"price": "9647.8",		  
  		"time": 1591257246176    
	}  
]
```