On this page

# Liquidation Order Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#stream-description "Direct link to Stream Description")

The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol.
For each symbol，only the latest one liquidation order within 1000ms will be pushed as the snapshot. If no liquidation happens in the interval of 1000ms, no stream will be pushed.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#stream-name "Direct link to Stream Name")

`<symbol>@forceOrder`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#update-speed "Direct link to Update Speed")

1000ms

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams#response-example "Direct link to Response Example")

```prism-code
{  
  
	"e":"forceOrder",                   // Event Type  
	"E":1568014460893,                  // Event Time  
	"o":{  
	  
		"s":"BTCUSDT",                   // Symbol  
		"S":"SELL",                      // Side  
		"o":"LIMIT",                     // Order Type  
		"f":"IOC",                       // Time in Force  
		"q":"0.014",                     // Original Quantity  
		"p":"9910",                      // Price  
		"ap":"9910",                     // Average Price  
		"X":"FILLED",                    // Order Status  
		"l":"0.014",                     // Order Last Filled Quantity  
		"z":"0.014",                     // Order Filled Accumulated Quantity  
		"T":1568014460893,          	 // Order Trade Time  
	  
	}  
  
}
```