On this page

# Long/Short Ratio

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#api-description "Direct link to API Description")

Query symbol Long/Short Ratio

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#http-request "Direct link to HTTP Request")

GET `/futures/data/globalLongShortAccountRatio`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| period | ENUM | YES | "5m","15m","30m","1h","2h","4h","6h","12h","1d" |
| limit | LONG | NO | default 30, max 500 |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |

> * If startTime and endTime are not sent, the most recent data is returned.
> * Only the data of the latest 30 days is available.
> * IP rate limit 1000 requests/5min

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio#response-example "Direct link to Response Example")

```prism-code
[  
    {   
         "symbol":"BTCUSDT",  // long/short account num ratio of all traders  
	      "longShortRatio":"0.1960",  //long account num ratio of all traders  
	      "longAccount": "0.6622",   // short account num ratio of all traders  
	      "shortAccount":"0.3378",   
	      "timestamp":"1583139600000"  
      
     },  
       
     {  
           
         "symbol":"BTCUSDT",  
	      "longShortRatio":"1.9559",  
	      "longAccount": "0.6617",   
	      "shortAccount":"0.3382", 	                  
	      "timestamp":"1583139900000"  
	                 
        },     
	      
]
```