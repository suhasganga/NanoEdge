On this page

# Symbol Order Book Ticker

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#api-description "Direct link to API Description")

Best price/qty on the order book for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#http-request "Direct link to HTTP Request")

GET `/fapi/v1/ticker/bookTicker`

**Note**:

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#request-weight "Direct link to Request Weight")

**2** for a single symbol;  
**5** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |

> * If the symbol is not sent, bookTickers for all symbols will be returned in an array.
> * The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#response-example "Direct link to Response Example")

```prism-code
{  
  "symbol": "BTCUSDT",  
  "bidPrice": "4.00000000",  
  "bidQty": "431.00000000",  
  "askPrice": "4.00000200",  
  "askQty": "9.00000000",  
  "time": 1589437530011   // Transaction time  
}
```

> OR

```prism-code
[  
	{  
  		"symbol": "BTCUSDT",  
  		"bidPrice": "4.00000000",  
  		"bidQty": "431.00000000",  
  		"askPrice": "4.00000200",  
  		"askQty": "9.00000000",  
  		"time": 1589437530011  
	}  
]
```