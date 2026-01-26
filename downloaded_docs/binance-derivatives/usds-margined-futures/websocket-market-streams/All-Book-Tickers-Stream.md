On this page

# All Book Tickers Stream

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#stream-description "Direct link to Stream Description")

Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#stream-name "Direct link to Stream Name")

`!bookTicker`

**Note**:

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#update-speed "Direct link to Update Speed")

**5s**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream#response-example "Direct link to Response Example")

```prism-code
{  
  "e":"bookTicker",			// event type  
  "u":400900217,     		// order book updateId  
  "E": 1568014460893,  	// event time  
  "T": 1568014460891,  	// transaction time  
  "s":"BNBUSDT",     		// symbol  
  "b":"25.35190000", 		// best bid price  
  "B":"31.21000000", 		// best bid qty  
  "a":"25.36520000", 		// best ask price  
  "A":"40.66000000"  		// best ask qty  
}
```