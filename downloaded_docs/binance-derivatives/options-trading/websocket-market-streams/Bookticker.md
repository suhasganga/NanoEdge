On this page

# Individual Symbol Book Ticker Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#stream-description "Direct link to Stream Description")

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#stream-name "Direct link to Stream Name")

`<symbol>@bookTicker`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#update-speed "Direct link to Update Speed")

**Real-Time**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Bookticker#response-example "Direct link to Response Example")

```prism-code
{  
        "e": "bookTicker",             // event type  
        "u": 2472,                     // order book updateId  
        "s": "BTC-251226-110000-C",    // symbol  
        "b": "5000.000",               // best bid price  
        "B": "0.2000",                 // bid bid quantity  
        "a": "5100.000",               // best ask price  
        "A": "0.1000",                 // best ask quantity  
        "T": 1763041762942,            // transaction time  
        "E": 1763041762942             // event time  
}
```