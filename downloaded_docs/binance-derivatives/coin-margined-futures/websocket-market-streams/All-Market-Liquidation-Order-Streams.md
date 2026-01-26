On this page

# All Market Liquidation Order Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#stream-description "Direct link to Stream Description")

The All Liquidation Order Snapshot Streams push force liquidation order information for all symbols in the market.
For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#stream-name "Direct link to Stream Name")

`!forceOrder@arr`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams#response-example "Direct link to Response Example")

```prism-code
{  
	"e":"forceOrder",                   // Event Type  
	"E": 1591154240950,					// Event Time  
	"o":{  
		"s":"BTCUSD_200925", 		// Symbol  
		"ps": "BTCUSD",					// Pair  
		"S":"SELL",						// Side  
		"o":"LIMIT",					// Order Type  
		"f":"IOC",						// Time in Force  
		"q":"1",						// Original Quantity  
		"p":"9425.5",					// Price  
		"ap":"9496.5",					// Average Price  
		"X":"FILLED",					// Order Status  
		"l":"1",						// Order Last Filled Quantity  
		"z":"1",						// Order Filled Accumulated Quantity  
		"T": 1591154240949,				// Order Trade Time  
	  
	}  
}
```