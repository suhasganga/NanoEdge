On this page

# Order Book

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#api-description "Direct link to API Description")

Get current order book. Note that this request returns limited market depth.
If you need to continuously monitor order book updates, please consider using Websocket Market Streams:

* `<symbol>@depth<levels>`
* `<symbol>@depth`

You can use `depth` request together with `<symbol>@depth` streams to maintain a local order book.

## Method[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#method "Direct link to Method")

`depth`

**Note**:

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#request "Direct link to Request")

```prism-code
{  
    "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
    "method": "depth",  
    "params": {  
      "symbol": "BTCUSDT"  
    }  
}
```

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#request-weight "Direct link to Request Weight")

Adjusted based on the limit:

| Limit | Weight |
| --- | --- |
| 5, 10, 20, 50 | 2 |
| 100 | 5 |
| 500 | 10 |
| 1000 | 20 |

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| limit | INT | NO | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api#response-example "Direct link to Response Example")

```prism-code
{  
  "id": "51e2affb-0aba-4821-ba75-f2625006eb43",  
  "status": 200,  
  "result": {  
    "lastUpdateId": 1027024,  
    "E": 1589436922972,   // Message output time  
    "T": 1589436922959,   // Transaction time  
    "bids": [  
      [  
        "4.00000000",     // PRICE  
        "431.00000000"    // QTY  
      ]  
    ],  
    "asks": [  
      [  
        "4.00000200",  
        "12.00000000"  
      ]  
    ]  
  },  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 5  
    }  
  ]  
}
```