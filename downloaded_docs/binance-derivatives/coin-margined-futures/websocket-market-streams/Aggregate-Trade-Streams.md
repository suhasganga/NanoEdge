On this page

# Aggregate Trade Streams

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-description "Direct link to Stream Description")

The Aggregate Trade Streams push market trade information that is aggregated for fills with same price and taking side every 100 milliseconds.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#stream-name "Direct link to Stream Name")

`<symbol>@aggTrade`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#update-speed "Direct link to Update Speed")

**100ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams#response-example "Direct link to Response Example")

```prism-code
{  
  "e":"aggTrade",		// Event type  
  "E":1591261134288,	// Event time  
  "a":424951,			// Aggregate trade ID  
  "s":"BTCUSD_200626",	// Symbol  
  "p":"9643.5",			// Price  
  "q":"2",				// Quantity  
  "f":606073,			// First trade ID  
  "l":606073,			// Last trade ID  
  "T":1591261134199,	// Trade time  
  "m":false				// Is the buyer the market maker?  
}
```