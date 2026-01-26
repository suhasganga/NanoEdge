On this page

# Open Interest

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest#api-description "Direct link to API Description")

Get present open interest of a specific symbol.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest#http-request "Direct link to HTTP Request")

GET `/fapi/v1/openInterest`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest#response-example "Direct link to Response Example")

```prism-code
{  
	"openInterest": "10659.509",   
	"symbol": "BTCUSDT",  
	"time": 1589437530011   // Transaction time  
}
```