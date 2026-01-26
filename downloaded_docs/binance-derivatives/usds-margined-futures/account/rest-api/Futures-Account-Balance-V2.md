On this page

# Futures Account Balance V2 (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#api-description "Direct link to API Description")

Query account balance info

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#http-request "Direct link to HTTP Request")

GET `/fapi/v2/balance`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#response-example "Direct link to Response Example")

```prism-code
[  
 	{  
 		"accountAlias": "SgsR",    // unique account code  
 		"asset": "USDT",  	// asset name  
 		"balance": "122607.35137903", // wallet balance  
 		"crossWalletBalance": "23.72469206", // crossed wallet balance  
  		"crossUnPnl": "0.00000000",  // unrealized profit of crossed positions  
  		"availableBalance": "23.72469206",       // available balance  
  		"maxWithdrawAmount": "23.72469206",     // maximum amount for transfer out  
  		"marginAvailable": true,    // whether the asset can be used as margin in Multi-Assets mode  
  		"updateTime": 1617939110373  
	}  
]
```