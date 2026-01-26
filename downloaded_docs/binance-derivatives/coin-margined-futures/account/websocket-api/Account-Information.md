On this page

# Account Information(USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/websocket-api/Account-Information#api-description "Direct link to API Description")

Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.

## Method[​](/docs/derivatives/coin-margined-futures/account/websocket-api/Account-Information#method "Direct link to Method")

`account.status`

## Request[​](/docs/derivatives/coin-margined-futures/account/websocket-api/Account-Information#request "Direct link to Request")

```prism-code
{  
  "id": "baaec739-c5cf-4920-b448-c0b9c5431410",  
  "method": "account.status",  
  "params": {  
    "apiKey": "",  
    "timestamp": 1727785087742,  
    "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
   }  
}
```

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/websocket-api/Account-Information#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/websocket-api/Account-Information#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/websocket-api/Account-Information#response-example "Direct link to Response Example")

```prism-code
{  
  "id": "baaec739-c5cf-4920-b448-c0b9c5431410",  
  "status": 200,  
  "result": {  
    "feeTier": 0,  
    "canTrade": true,  
    "canDeposit": true,  
    "canWithdraw": true,  
    "updateTime": 0,  
    "assets": [  
      {  
        "asset": "WLD",  
        "walletBalance": "0.00000000",  
        "unrealizedProfit": "0.00000000",  
        "marginBalance": "0.00000000",  
        "maintMargin": "0.00000000",  
        "initialMargin": "0.00000000",  
        "positionInitialMargin": "0.00000000",  
        "openOrderInitialMargin": "0.00000000",  
        "maxWithdrawAmount": "0.00000000",  
        "crossWalletBalance": "0.00000000",  
        "crossUnPnl": "0.00000000",  
        "availableBalance": "0.00000000",  
        "updateTime": 0  
      },  
      // ... ...  
    ],  
    "positions": [  
      {  
        "symbol": "ETHUSD_220930",  
        "initialMargin": "0",  
        "maintMargin": "0",  
        "unrealizedProfit": "0.00000000",  
        "positionInitialMargin": "0",  
        "openOrderInitialMargin": "0",  
        "leverage": "7",  
        "isolated": false,  
        "positionSide": "BOTH",  
        "entryPrice": "0.00000000",  
        "maxQty": "1000",  
        "notionalValue": "0",  
        "isolatedWallet": "0",  
        "updateTime": 0,  
        "positionAmt": "0",  
        "breakEvenPrice": "0.00000000"  
      },  
      // ... ...  
    ]  
  },  
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