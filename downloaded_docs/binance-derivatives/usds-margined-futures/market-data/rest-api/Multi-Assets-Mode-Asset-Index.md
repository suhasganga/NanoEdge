On this page

# Multi-Assets Mode Asset Index

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#api-description "Direct link to API Description")

asset index for Multi-Assets mode

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#http-request "Direct link to HTTP Request")

GET `/fapi/v1/assetIndex`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#request-weight "Direct link to Request Weight")

**1** for a single symbol; **10** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO | Asset pair |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Multi-Assets-Mode-Asset-Index#response-example "Direct link to Response Example")

> **Response:**

```prism-code
{  
	"symbol": "ADAUSD",  
	"time": 1635740268004,  
	"index": "1.92957370",  
	"bidBuffer": "0.10000000",   
	"askBuffer": "0.10000000",   
	"bidRate": "1.73661633",  
	"askRate": "2.12253107",  
	"autoExchangeBidBuffer": "0.05000000",  
	"autoExchangeAskBuffer": "0.05000000",  
	"autoExchangeBidRate": "1.83309501",  
	"autoExchangeAskRate": "2.02605238"  
}
```

> Or(without symbol)

```prism-code
[  
	{  
		"symbol": "ADAUSD",  
		"time": 1635740268004,  
		"index": "1.92957370",  
		"bidBuffer": "0.10000000",   
		"askBuffer": "0.10000000",   
		"bidRate": "1.73661633",  
		"askRate": "2.12253107",  
		"autoExchangeBidBuffer": "0.05000000",  
		"autoExchangeAskBuffer": "0.05000000",  
		"autoExchangeBidRate": "1.83309501",  
		"autoExchangeAskRate": "2.02605238"  
	}  
]
```