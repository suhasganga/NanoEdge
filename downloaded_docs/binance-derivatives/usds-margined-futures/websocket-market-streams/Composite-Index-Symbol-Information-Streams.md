On this page

# Composite Index Symbol Information Streams

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#stream-description "Direct link to Stream Description")

Composite index information for index symbols pushed every second.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#stream-name "Direct link to Stream Name")

`<symbol>@compositeIndex`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Composite-Index-Symbol-Information-Streams#response-example "Direct link to Response Example")

```prism-code
{  
  "e":"compositeIndex",		// Event type  
  "E":1602310596000,		// Event time  
  "s":"DEFIUSDT",			// Symbol  
  "p":"554.41604065",		// Price  
  "C":"baseAsset",  
  "c":[      				// Composition  
  	{  
  		"b":"BAL",			// Base asset  
  		"q":"USDT",         // Quote asset  
  		"w":"1.04884844",	// Weight in quantity  
  		"W":"0.01457800",   // Weight in percentage  
  		"i":"24.33521021"   // Index price  
  	},  
  	{  
  		"b":"BAND",  
  		"q":"USDT" ,  
  		"w":"3.53782729",  
  		"W":"0.03935200",  
  		"i":"7.26420084"  
    }  
  ]  
}
```