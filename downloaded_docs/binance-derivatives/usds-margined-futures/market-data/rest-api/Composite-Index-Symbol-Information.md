On this page

# Composite Index Symbol Information

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#api-description "Direct link to API Description")

Query composite index symbol information

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#http-request "Direct link to HTTP Request")

GET `/fapi/v1/indexInfo`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |

> * Only for composite index symbols

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Composite-Index-Symbol-Information#response-example "Direct link to Response Example")

```prism-code
[  
	{   
		"symbol": "DEFIUSDT",  
		"time": 1589437530011,    // Current time  
		"component": "baseAsset", //Component asset  
		"baseAssetList":[  
			{  
				"baseAsset":"BAL",  
				"quoteAsset": "USDT",  
				"weightInQuantity":"1.04406228",  
				"weightInPercentage":"0.02783900"  
			},  
			{  
				"baseAsset":"BAND",  
				"quoteAsset": "USDT",  
				"weightInQuantity":"3.53782729",  
				"weightInPercentage":"0.03935200"  
			}  
		]  
	}  
]
```