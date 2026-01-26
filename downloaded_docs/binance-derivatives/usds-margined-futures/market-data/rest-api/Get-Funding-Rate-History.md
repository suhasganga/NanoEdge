On this page

# Get Funding Rate History

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#api-description "Direct link to API Description")

Get Funding Rate History

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#http-request "Direct link to HTTP Request")

GET `/fapi/v1/fundingRate`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#request-weight "Direct link to Request Weight")

share 500/5min/IP rate limit with GET /fapi/v1/fundingInfo

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| startTime | LONG | NO | Timestamp in ms to get funding rate from INCLUSIVE. |
| endTime | LONG | NO | Timestamp in ms to get funding rate until INCLUSIVE. |
| limit | INT | NO | Default 100; max 1000 |

> * If `startTime` and `endTime` are not sent, the most recent 200 records are returned.
> * If the number of data between `startTime` and `endTime` is larger than `limit`, return as `startTime` + `limit`.
> * In ascending order.

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History#response-example "Direct link to Response Example")

```prism-code
[  
	{  
    	"symbol": "BTCUSDT",  
    	"fundingRate": "-0.03750000",  
    	"fundingTime": 1570608000000,  
		"markPrice": "34287.54619963"   // mark price associated with a particular funding fee charge  
	},  
	{  
   		"symbol": "BTCUSDT",  
    	"fundingRate": "0.00010000",  
    	"fundingTime": 1570636800000,  
		"markPrice": "34287.54619963"   
	}  
]
```