On this page

# Get Futures Transaction History Download Link by Id (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id#api-description "Direct link to API Description")

Get futures transaction history download link by Id

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id#http-request "Direct link to HTTP Request")

GET `/dapi/v1/income/asyn/id`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| downloadId | STRING | YES | get by download id api |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Download link expiration: 24h

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id#response-example "Direct link to Response Example")

> **Response:**

```prism-code
{  
	"downloadId":"545923594199212032",  
  	"status":"completed",     // Enum：completed，processing  
  	"url":"www.binance.com",  // The link is mapped to download id  
  	"notified":true,          // ignore  
  	"expirationTimestamp":1645009771000,  // The link would expire after this timestamp  
  	"isExpired":null,  
}
```

> **OR** (Response when server is processing)

```prism-code
{  
	"downloadId":"545923594199212032",  
  	"status":"processing",  
  	"url":"",   
  	"notified":false,  
  	"expirationTimestamp":-1  
  	"isExpired":null,  
  	  
}
```