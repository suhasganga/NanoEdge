On this page

# ADL Risk

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#api-description "Direct link to API Description")

Query the symbol-level ADL risk rating.
The ADL risk rating measures the likelihood of ADL during liquidation, and the rating takes into account the insurance fund balance, position concentration on the symbol, order book depth, price volatility, average leverage, unrealized PnL, and margin utilization at the symbol level.
The rating can be high, medium and low, and is updated every 30 minutes.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#http-request "Direct link to HTTP Request")

GET `/fapi/v1/symbolAdlRisk`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk#response-example "Direct link to Response Example")

> **Response:**

```prism-code
{  
	"symbol": "BTCUSDT",  
	"adlRisk": "low",  // ADL Risk rating  
	"updateTime": 1597370495002  
}
```

> **OR (when symbol not sent)**

```prism-code
[  
	{  
	    "symbol": "BTCUSDT",  
	    "adlRisk": "low",  // ADL Risk rating  
	    "updateTime": 1597370495002  
	},  
	{  
	    "symbol": "ETHUSDT",  
	    "adlRisk": "high", // ADL Risk rating  
	    "updateTime": 1597370495004  
	}  
]
```