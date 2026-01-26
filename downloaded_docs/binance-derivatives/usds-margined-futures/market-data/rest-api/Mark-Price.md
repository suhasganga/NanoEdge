On this page

# Mark Price

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#api-description "Direct link to API Description")

Mark Price and Funding Rate

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#http-request "Direct link to HTTP Request")

GET `/fapi/v1/premiumIndex`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#request-weight "Direct link to Request Weight")

**1** with symbol, **10** without symbol

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price#response-example "Direct link to Response Example")

> **Response:**

```prism-code
{  
	"symbol": "BTCUSDT",  
	"markPrice": "11793.63104562",	// mark price  
	"indexPrice": "11781.80495970",	// index price  
	"estimatedSettlePrice": "11781.16138815", // Estimated Settle Price, only useful in the last hour before the settlement starts.  
	"lastFundingRate": "0.00038246",  // This is the Latest funding rate  
	"interestRate": "0.00010000",  
	"nextFundingTime": 1597392000000,  
	"time": 1597370495002  
}
```

> **OR (when symbol not sent)**

```prism-code
[  
	{  
	    "symbol": "BTCUSDT",  
	    "markPrice": "11793.63104562",	// mark price  
	    "indexPrice": "11781.80495970",	// index price  
	    "estimatedSettlePrice": "11781.16138815", // Estimated Settle Price, only useful in the last hour before the settlement starts.  
	    "lastFundingRate": "0.00038246",  // This is the Latest funding rate  
	    "interestRate": "0.00010000",  
	    "nextFundingTime": 1597392000000,  
	    "time": 1597370495002  
	}  
]
```