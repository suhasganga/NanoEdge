On this page

# Partial Book Depth Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#stream-description "Direct link to Stream Description")

Top **<levels>** bids and asks, Valid levels are **<levels>** are 5, 10, 20.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#url-path "Direct link to URL PATH")

`/public`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#stream-name "Direct link to Stream Name")

`<symbol>@depth<level>@100ms` or `<symbol>@depth<level>@500ms`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#update-speed "Direct link to Update Speed")

**100ms** or **500ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Partial-Book-Depth-Streams#response-example "Direct link to Response Example")

```prism-code
{  
    "e": "depthUpdate",            // event type   
    "E": 1762866729459,            // event time  
    "T": 1762866729358,            // transaction time   
    "s": "BTC-251123-126000-C",    // Option symbol    
    "U": 465,                      // First update ID in event  
    "u": 465,                      // Final update ID in event  
    "pu": 464,                     // Final update Id in last stream(ie `u` in last stream)  
    "b": [                         // Buy order     
        [  
            "1100.000",            // Price  
            "0.6000"               // quantity  
        ]          
    ],  
    "a": [                         // Sell order     
        [  
            "1300.000",  
            "0.6000"  
        ]  
    ]  
}
```