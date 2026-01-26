On this page

# Recent Trades List

## API Description[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#api-description "Direct link to API Description")

Get recent market trades

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#http-request "Direct link to HTTP Request")

GET `/eapi/v1/trades`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option trading pair, e.g BTC-200730-9000-C |
| limit | INT | NO | Number of records Default:100 Max:500 |

## Response Example[​](/docs/derivatives/options-trading/market-data/Recent-Trades-List#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "id": 2323857420768529130,  
        "tradeId": 1,                    // TradeId  
        "symbol": "BTC-251123-126000-C", // Completed trade price  
        "price": "1300",                 // Completed trade quantity  
        "qty": "0.1",                    // Completed trade quantity  
        "quoteQty": "130",               // Completed trade amount  
        "side": -1,                      // Completed trade direction（-1 Sell，1 Buy）  
        "time": 1762780453623            // Time   
    }  
]
```