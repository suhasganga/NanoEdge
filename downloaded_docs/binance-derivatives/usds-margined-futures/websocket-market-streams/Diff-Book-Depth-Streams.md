On this page

# Diff. Book Depth Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Bids and asks, pushed every 250 milliseconds, 500 milliseconds, 100 milliseconds (if existing)

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth` OR `<symbol>@depth@500ms` OR `<symbol>@depth@100ms`

**Note**:

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**250ms**, **500ms**, **100ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams#response-example "Direct link to Response Example")

```prism-code
{  
  "e": "depthUpdate", // Event type  
  "E": 123456789,     // Event time  
  "T": 123456788,     // Transaction time   
  "s": "BTCUSDT",     // Symbol  
  "U": 157,           // First update ID in event  
  "u": 160,           // Final update ID in event  
  "pu": 149,          // Final update Id in last stream(ie `u` in last stream)  
  "b": [              // Bids to be updated  
    [  
      "0.0024",       // Price level to be updated  
      "10"            // Quantity  
    ]  
  ],  
  "a": [              // Asks to be updated  
    [  
      "0.0026",       // Price level to be updated  
      "100"          // Quantity  
    ]  
  ]  
}
```