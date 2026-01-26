On this page

# RPI Diff. Book Depth Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#stream-description "Direct link to Stream Description")

Bids and asks including RPI orders, pushed every 500 milliseconds

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#stream-name "Direct link to Stream Name")

`<symbol>@rpiDepth@500ms`

**Note**:

> RPI(Retail Price Improvement) orders are included and aggreated in the response message. When the quantity of a price level to be updated is equal to 0, it means either all quotations for this price have been filled/canceled, or the quantity of crossed RPI orders for this price are hidden

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#update-speed "Direct link to Update Speed")

**500ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI#response-example "Direct link to Response Example")

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