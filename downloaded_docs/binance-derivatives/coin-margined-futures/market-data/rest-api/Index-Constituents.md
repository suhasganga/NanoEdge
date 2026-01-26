On this page

# Query Index Price Constituents

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#api-description "Direct link to API Description")

Query index price constituents

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#http-request "Direct link to HTTP Request")

GET `/dapi/v1/constituents`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Constituents#response-example "Direct link to Response Example")

```prism-code
{  
    "symbol": "BTCUSD",  
    "time": 1697422647853,  
    "constituents": [  
        {  
            "exchange": "bitstamp",  
            "symbol": "btcusd"  
        },  
        {  
            "exchange": "coinbase",  
            "symbol": "BTC-USD"  
        },  
        {  
            "exchange": "kraken",  
            "symbol": "XBT/USD"  
        },  
        {  
            "exchange": "binance_cross",  
            "symbol": "BTCUSDC*index(USDCUSD)"  
        }  
    ]  
}
```