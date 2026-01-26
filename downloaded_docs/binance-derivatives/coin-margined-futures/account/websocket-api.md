On this page

# Futures Account Balance(USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/websocket-api#api-description "Direct link to API Description")

Query account balance info

## Method[​](/docs/derivatives/coin-margined-futures/account/websocket-api#method "Direct link to Method")

`account.balance`

## Request[​](/docs/derivatives/coin-margined-futures/account/websocket-api#request "Direct link to Request")

```prism-code
{  
  "id": "9328e612-1560-4108-979e-283bf85b5acb",  
  "method": "account.balance",  
  "params": {  
    "apiKey": "",  
    "timestamp": 1727810404936,  
    "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
   }  
}
```

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/websocket-api#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/websocket-api#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/websocket-api#response-example "Direct link to Response Example")

```prism-code
{  
  "id": "9328e612-1560-4108-979e-283bf85b5acb",  
  "status": 200,  
  "result": [  
    {  
      "accountAlias": "fWAuTiuXoCuXmY",  
      "asset": "WLD",  
      "balance": "0.00000000",  
      "withdrawAvailable": "0.00000000",  
      "crossWalletBalance": "0.00000000",  
      "crossUnPnl": "0.00000000",  
      "availableBalance": "0.00000000",  
      "updateTime": 0  
    },  
    // ... ...  
  ],  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 10  
    }  
  ]  
}
```