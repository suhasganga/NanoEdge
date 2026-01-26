On this page

# Mark Price

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Mark-Price#stream-description "Direct link to Stream Description")

The mark price for all option symbols on specific underlying asset. E.g.[btcusdt@optionMarkPrice](wss://fstream.binance.com/market/stream?streams=btcusdt@optionMarkPrice)

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Mark-Price#url-path "Direct link to URL PATH")

`/market`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Mark-Price#stream-name "Direct link to Stream Name")

`<underlying>@optionMarkPrice`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Mark-Price#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Mark-Price#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "s": "BTC-251120-126000-C",    // Symbol  
        "mp": "770.543",               // Mark price  
        "E": 1762867543321,            // Event time  
        "e": "markPrice",              // Event type  
        "i": "104334.60217391",        // Index price  
        "P": "0.000",                  // Estimated Settle Price, only useful in the 0.5 hour before the settlement starts  
        "bo": "0.000",                 // The best buy price  
        "ao": "900.000",               // The best sell price  
        "bq": "0.0000",                // The best buy quantity  
        "aq": "0.2000",                // The best sell quantity  
        "b": "-1.0",                   // BuyImplied volatility  
        "a": "0.98161161",             // SellImplied volatility   
        "hl": "924.652",               // Buy Maximum price   
        "ll": "616.435",               // Sell Minimum price  
        "vo": "0.9408058",             // volatility  
        "rf": "0.0",                   // risk free rate  
        "d": "0.11111964",             // delta  
        "t": "-164.26702615",          // theta  
        "g": "0.00001245",             // gamma  
        "v": "30.63855919"             // vega  
    },  
    {  
        "s": "BTC-251123-126000-C",  
        "mp": "1249.61",  
        "E": 1762867543321,  
        "e": "markPrice",  
        "i": "104334.60217391",  
        "P": "0.000",  
        "bo": "1200.000",  
        "ao": "1300.000",  
        "bq": "0.3000",  
        "aq": "0.6000",  
        "b": "0.92159033",  
        "a": "0.94461441",  
        "hl": "1499.533",  
        "ll": "999.688",  
        "vo": "0.93310237",  
        "rf": "0.0",  
        "d": "0.14869196",  
        "t": "-172.12148811",  
        "g": "0.00001326",  
        "v": "43.43627792"  
    }  
]
```