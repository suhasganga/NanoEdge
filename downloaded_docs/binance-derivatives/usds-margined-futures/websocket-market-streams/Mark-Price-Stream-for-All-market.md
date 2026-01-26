On this page

# Mark Price Stream for All market

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#stream-description "Direct link to Stream Description")

Mark price and funding rate for all symbols pushed every 3 seconds or every second.

**Note**:

> TradFi symbols will be pushed through a seperate message.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#stream-name "Direct link to Stream Name")

`!markPrice@arr` or `!markPrice@arr@1s`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#update-speed "Direct link to Update Speed")

**3000ms** or **1000ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market#response-example "Direct link to Response Example")

```prism-code
[   
  {  
    "e": "markPriceUpdate",  	// Event type  
    "E": 1562305380000,      	// Event time  
    "s": "BTCUSDT",          	// Symbol  
    "p": "11185.87786614",   	// Mark price  
    "i": "11784.62659091"		// Index price  
    "P": "11784.25641265",		// Estimated Settle Price, only useful in the last hour before the settlement starts  
    "r": "0.00030000",       	// Funding rate  
    "T": 1562306400000       	// Next funding time  
  }  
]
```