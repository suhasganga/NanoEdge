On this page

# Order Book

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book#api-description "Direct link to API Description")

Query symbol orderbook

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book#http-request "Direct link to HTTP Request")

GET `/fapi/v1/depth`

**Note**:

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book#request-weight "Direct link to Request Weight")

Adjusted based on the limit:

| Limit | Weight |
| --- | --- |
| 5, 10, 20, 50 | 2 |
| 100 | 5 |
| 500 | 10 |
| 1000 | 20 |

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| limit | INT | NO | Default 500; Valid limits:[5, 10, 20, 50, 100, 500, 1000] |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book#response-example "Direct link to Response Example")

```prism-code
{  
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
}
```