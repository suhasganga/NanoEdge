On this page

# Trade Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#stream-description "Direct link to Stream Description")

The Trade Streams push raw trade information for specific symbol or underlying asset. E.g.[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#stream-name "Direct link to Stream Name")

`<symbol>@optionTrade` or `<underlying>@optionTrade`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Trade-Streams#response-example "Direct link to Response Example")

```prism-code
{  
    "e": "trade",                  // event type     
    "E": 1762856064204,            // event time     
    "T": 1762856064203,            // trade completed time      
    "s": "BTC-251123-126000-C",    // Option trading symbol      
    "t": 4,                        // trade ID     
    "p": "1300.000",               // price  
    "q": "0.1000",                 // quantity, always positive  
    "X": "MARKET",                 // trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade	  
    "S": "BUY",                    // direction     
    "m": false                     // Is the buyer the market maker?  
}
```