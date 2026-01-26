On this page

# Open Interest

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#stream-description "Direct link to Stream Description")

Option open interest for specific underlying asset on specific expiration date. E.g.[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#url-path "Direct link to URL PATH")

`/market`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#stream-name "Direct link to Stream Name")

`underlying@optionOpenInterest@<expirationDate>`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#update-speed "Direct link to Update Speed")

**60s**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#response-example "Direct link to Response Example")

```prism-code
[  
    {  
      "e":"openInterest",         // Event type  
      "E":1668759300045,          // Event time  
      "s":"ETH-221125-2700-C",    // option symbol  
      "o":"1580.87",              // Open interest in contracts  
      "h":"1912992.178168204"     // Open interest in USDT  
    }  
]
```