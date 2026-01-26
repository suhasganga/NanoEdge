On this page

# All Market Mini Tickers Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#stream-description "Direct link to Stream Description")

24hr rolling window mini-ticker statistics for all symbols. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before. Note that only tickers that have changed will be present in the array.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#stream-name "Direct link to Stream Name")

`!miniTicker@arr`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream#response-example "Direct link to Response Example")

```prism-code
[    
	{  
	  "e":"24hrMiniTicker",			// Event type  
	  "E":1591267704450,			// Event time  
	  "s":"BTCUSD_200626",			// Symbol  
	  "ps":"BTCUSD",				// Pair  
	  "c":"9561.7",					// Close price  
	  "o":"9580.9",					// Open price  
	  "h":"10000.0",				// High price  
	  "l":"7000.0",					// Low price  
	  "v":"487476",					// Total traded volume  
	  "q":"33264343847.22378500"	// Total traded base asset volume  
	}  
]
```