On this page

# Individual Symbol Ticker Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-description "Direct link to Stream Description")

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name "Direct link to Stream Name")

`<symbol>@ticker`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#update-speed "Direct link to Update Speed")

**2000ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#response-example "Direct link to Response Example")

```prism-code
{  
  "e": "24hrTicker",  // Event type  
  "E": 123456789,     // Event time  
  "s": "BTCUSDT",     // Symbol  
  "p": "0.0015",      // Price change  
  "P": "250.00",      // Price change percent  
  "w": "0.0018",      // Weighted average price  
  "c": "0.0025",      // Last price  
  "Q": "10",          // Last quantity  
  "o": "0.0010",      // Open price  
  "h": "0.0025",      // High price  
  "l": "0.0010",      // Low price  
  "v": "10000",       // Total traded base asset volume  
  "q": "18",          // Total traded quote asset volume  
  "O": 0,             // Statistics open time  
  "C": 86400000,      // Statistics close time  
  "F": 0,             // First trade ID  
  "L": 18150,         // Last trade Id  
  "n": 18151          // Total number of trades  
}
```