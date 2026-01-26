On this page

# Index Price Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#stream-description "Direct link to Stream Description")

Underlying(e.g ETHUSDT) index stream.

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#url-path "Direct link to URL PATH")

`/market`

**Stream Name:**  
`!index@arr`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Index-Price-Streams#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "e":"indexPrice",  
        "E":1763092572229,  
        "s":"ETHUSDT",  
        "p":"3224.51976744"  
    },  
    {  
        "e": "indexPrice",     // event type  
        "E": 1763092572229,    // time  
        "s": "BTCUSDT",        // underlying symbol  
        "p": "99102.32326087"  // index price  
    }  
]
```