On this page

# New Symbol Info

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#stream-description "Direct link to Stream Description")

New symbol listing stream.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#url-path "Direct link to URL PATH")

`/market`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#stream-name "Direct link to Stream Name")

`!optionSymbol`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/New-Symbol-Info#response-example "Direct link to Response Example")

```prism-code
{  
    "e":"optionSymbol",             // Event Type  
    "E":1669356423908,              // Event Time  
    "s":"BTC-250926-140000-C",      // Symbol  
    "ps":"BTCUSDT",                 // Underlying index of the contract  
    "qa":"USDT",                    // Quotation asset  
    "d":"CALL",                     // Option type  
    "sp":"21000",                   // Strike price  
    "dt":4133404800000,             // Delivery date time  
    "u":1,                          // unit, the quantity of the underlying asset represented by a single contract.  
    "ot":1569398400000,             // onboard date time  
    "cs":"TRADING"                  // Contract status   
}
```