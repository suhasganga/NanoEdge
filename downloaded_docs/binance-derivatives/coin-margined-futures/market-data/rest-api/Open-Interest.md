On this page

# Open Interest

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#api-description "Direct link to API Description")

Get present open interest of a specific symbol.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#http-request "Direct link to HTTP Request")

GET `/dapi/v1/openInterest`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest#response-example "Direct link to Response Example")

```prism-code
{  
	"symbol": "BTCUSD_200626",  
	"pair": "BTCUSD",  
	"openInterest": "15004",  
	"contractType": "CURRENT_QUARTER",  
	"time": 1591261042378  
}
```