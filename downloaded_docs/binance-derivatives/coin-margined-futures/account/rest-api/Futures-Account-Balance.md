On this page

# Futures Account Balance (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#api-description "Direct link to API Description")

Check futures account balance

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#http-request "Direct link to HTTP Request")

GET `/dapi/v1/balance`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance#response-example "Direct link to Response Example")

```prism-code
[  
 	{  
 		"accountAlias": "SgsR",    // unique account code  
 		"asset": "BTC",  
 		"balance": "0.00250000",  
 		"withdrawAvailable": "0.00250000",  
 		"crossWalletBalance": "0.00241969",  
  		"crossUnPnl": "0.00000000",  
  		"availableBalance": "0.00241969",  
 		"updateTime": 1592468353979  
	}  
]
```