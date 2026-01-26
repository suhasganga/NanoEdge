On this page

# Trading Session Stream

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#stream-description "Direct link to Stream Description")

Trading session information for the underlying assets of TradFi Perpetual contracts—covering the U.S. equity market and the commodity market—is updated every second. Trading session information for different underlying markets is pushed in separate messages. Session types for the equity market include "PRE\_MARKET", "REGULAR", "AFTER\_MARKET", "OVERNIGHT", and "NO\_TRADING". Session types for the commodity market include "REGULAR" and "NO\_TRADING".

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#stream-name "Direct link to Stream Name")

`tradingSession`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#update-speed "Direct link to Update Speed")

**1s**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Trading-Session-Stream#response-example "Direct link to Response Example")

```prism-code
  {  
    "e": "EquityUpdate",  	// Event type, can also be CommodityUpdate  
    "E": 1765244143062,     // Event time  
    "t": 1765242000000,   	// Session start time  
    "T": 1765270800000,		  // Session end time  
    "S": "OVERNIGHT"        // Session type  
  }
```