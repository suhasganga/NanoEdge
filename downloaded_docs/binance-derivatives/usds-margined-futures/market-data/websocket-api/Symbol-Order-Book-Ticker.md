On this page

# Symbol Order Book Ticker

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#api-description "Direct link to API Description")

Best price/qty on the order book for a symbol or symbols.

## Method[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#method "Direct link to Method")

`ticker.book`

**Note**:

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#request "Direct link to Request")

```prism-code
{  
    "id": "9d32157c-a556-4d27-9866-66760a174b57",  
    "method": "ticker.book",  
    "params": {  
        "symbol": "BTCUSDT"  
    }  
}
```

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#request-weight "Direct link to Request Weight")

**2** for a single symbol;  
**5** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |

> * If the symbol is not sent, bookTickers for all symbols will be returned in an array.
> * The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#response-example "Direct link to Response Example")

```prism-code
{  
  "id": "9d32157c-a556-4d27-9866-66760a174b57",  
  "status": 200,  
  "result": {  
    "lastUpdateId": 1027024,  
    "symbol": "BTCUSDT",  
    "bidPrice": "4.00000000",  
    "bidQty": "431.00000000",  
    "askPrice": "4.00000200",  
    "askQty": "9.00000000",  
    "time": 1589437530011   // Transaction time  
  },  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 2  
    }  
  ]  
}
```

> OR

```prism-code
{  
  "id": "9d32157c-a556-4d27-9866-66760a174b57",  
  "status": 200,  
  "result": [  
    {  
      "lastUpdateId": 1027024,  
      "symbol": "BTCUSDT",  
      "bidPrice": "4.00000000",  
      "bidQty": "431.00000000",  
      "askPrice": "4.00000200",  
      "askQty": "9.00000000",  
      "time": 1589437530011  
    }  
  ],  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 2  
    }  
  ]  
}
```