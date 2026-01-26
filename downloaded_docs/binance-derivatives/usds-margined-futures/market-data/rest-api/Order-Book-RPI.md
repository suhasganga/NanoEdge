On this page

# RPI Order Book

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#api-description "Direct link to API Description")

Query symbol orderbook with RPI orders

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#http-request "Direct link to HTTP Request")

GET `/fapi/v1/rpiDepth`

**Note**:

> RPI(Retail Price Improvement) orders are included and aggreated in the response message. Crossed price levels are hidden and invisible.

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#request-weight "Direct link to Request Weight")

Adjusted based on the limit:

| Limit | Weight |
| --- | --- |
| 1000 | 20 |

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| limit | INT | NO | Default 1000; Valid limits:[1000] |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI#response-example "Direct link to Response Example")

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