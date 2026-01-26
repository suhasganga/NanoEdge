On this page

# Exchange Information

## API Description[​](/docs/derivatives/options-trading/market-data/Exchange-Information#api-description "Direct link to API Description")

Current exchange trading rules and symbol information

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Exchange-Information#http-request "Direct link to HTTP Request")

GET `/eapi/v1/exchangeInfo`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Exchange-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Exchange-Information#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/derivatives/options-trading/market-data/Exchange-Information#response-example "Direct link to Response Example")

```prism-code
{  
  "timezone": "UTC",                    // Time zone used by the server  
  "serverTime": 1592387337630,          // Current system time  
  "optionContracts": [                  // Option contract underlying asset info  
    {  
      "baseAsset": "BTC",               // Base currency  
      "quoteAsset": "USDT",             // Quotation asset  
      "underlying": "BTCUSDT",          // Name of the underlying asset of the option contract  
      "settleAsset": "USDT"             // Settlement currency  
    }  
  ],  
  "optionAssets": [                     // Option asset info  
    {  
      "name": "USDT"                    // Asset name  
    }  
  ],  
  "optionSymbols": [                    // Option trading pair info  
    {  
        "expiryDate": 1660521600000,    // expiry time  
        "filters": [  
            {  
                "filterType": "PRICE_FILTER",  
                "minPrice": "0.02",  
                "maxPrice": "80000.01",  
                "tickSize": "0.01"  
            },  
            {  
                "filterType": "LOT_SIZE",  
                "minQty": "0.01",  
                "maxQty": "100",  
                "stepSize": "0.01"  
            }  
        ],  
        "symbol": "BTC-220815-50000-C",   // Trading pair name  
        "side": "CALL",                   // Direction: CALL long, PUT short  
        "strikePrice": "50000",           // Strike price  
        "underlying": "BTCUSDT",          // Underlying asset of the contract  
        "unit": 1,                        // Contract unit, the quantity of the underlying asset represented by a single contract.  
        "liquidationFeeRate": "0.0019000",// liquidation fee rate  
        "minQty": "0.01",                 // Minimum order quantity  
        "maxQty": "100",                  // Maximum order quantity  
        "initialMargin": "0.15",          // Initial Magin Ratio  
        "maintenanceMargin": "0.075",     // Maintenance Margin Ratio  
        "minInitialMargin": "0.1",        // Min Initial Margin Ratio  
        "minMaintenanceMargin": "0.05",   // Min Maintenance Margin Ratio  
        "priceScale": 2,                  // price precision  
        "quantityScale": 2,               // quantity precision  
        "quoteAsset": "USDT",             // Quotation asset  
        "status": "TRADING"               // Trading Status  
    }  
  ],  
  "rateLimits": [  
    {  
        "rateLimitType": "REQUEST_WEIGHT",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 2400  
    },  
    {  
        "rateLimitType": "ORDERS",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 1200  
    },  
    {  
        "rateLimitType": "ORDERS",  
        "interval": "SECOND",  
        "intervalNum": 10,  
        "limit": 300  
    }  
  ]  
}
```