On this page

# Index Price Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#stream-description "Direct link to Stream Description")

Index Price Stream

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#stream-name "Direct link to Stream Name")

`<pair>@indexPrice` OR `<pair>@indexPrice@1s`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#update-speed "Direct link to Update Speed")

**3000ms** OR **1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Index-Price-Stream#response-example "Direct link to Response Example")

```prism-code
  {  
    "e": "indexPriceUpdate",  // Event type  
    "E": 1591261236000,       // Event time  
    "i": "BTCUSD",            // Pair  
    "p": "9636.57860000",     // Index Price  
  }
```