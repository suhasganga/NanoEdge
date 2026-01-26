On this page

# 24-hour TICKER

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#stream-description "Direct link to Stream Description")

24hr ticker info for all symbols. Only symbols whose ticker info changed will be sent.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#stream-name "Direct link to Stream Name")

`<symbol>@optionTicker` or `<underlying>@optionTicker@<expiretionDate>` e.g: btcusdt@optionTicker@251230

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/24-hour-TICKER#response-example "Direct link to Response Example")

```prism-code
{  
    "e": "24hrTicker",          // Event type  
    "E": 1764080707933,         // Event time  
    "s": "ETH-251226-3000-C",   // Symbol  
    "p": "0.0000",              // Price change  
    "P": "0.00",                // Price change percent  
    "w": "200.0000",            // Weighted average price  
    "c": "200.0000",            // Last price  
    "Q": "1.0000",              // Last quantity  
    "o": "200.0000",            // Open price  
    "h": "200.0000",            // High price  
    "l": "200.0000",            // Low price  
    "v": "9.0000",              // Trading volume(in contracts)  
    "q": "1800.0000",           // trade amount(in quote asset)   
    "O": 1764051060000,         // Statistics open time  
    "C": 1764080707933,         // Statistics close time  
    "F": 1,                     // First trade ID  
    "L": 22,                    // Last trade Id  
    "n": 9                      // Total number of trade  
}
```