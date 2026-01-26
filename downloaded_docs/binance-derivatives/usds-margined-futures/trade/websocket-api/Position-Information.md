On this page

# Position Information (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information#api-description "Direct link to API Description")

Get current position information.

## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information#method "Direct link to Method")

`account.position`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information#request "Direct link to Request")

```prism-code
{  
   	"id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
    "method": "account.position",  
    "params": {  
        "apiKey": "xTaDyrmvA9XT2oBHHjy39zyPzKCvMdtH3b9q4xadkAg2dNSJXQGCxzui26L823W2",  
        "symbol": "BTCUSDT",  
        "timestamp": 1702920680303,  
        "signature": "31ab02a51a3989b66c29d40fcdf78216978a60afc6d8dc1c753ae49fa3164a2a"  
    }  
}
```

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

**Note**

> * Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information#response-example "Direct link to Response Example")

> For One-way position mode:

```prism-code
{  
  "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
  "status": 200,  
  "result": [  
    {  
        "entryPrice": "0.00000",  
        "breakEvenPrice": "0.0",    
        "marginType": "isolated",   
        "isAutoAddMargin": "false",  
        "isolatedMargin": "0.00000000",   
        "leverage": "10",   
        "liquidationPrice": "0",   
        "markPrice": "6679.50671178",     
        "maxNotionalValue": "20000000",   
        "positionAmt": "0.000",  
        "notional": "0",   
        "isolatedWallet": "0",  
        "symbol": "BTCUSDT",   
        "unRealizedProfit": "0.00000000",   
        "positionSide": "BOTH",  
        "updateTime": 0  
    }  
],  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 20  
    }  
  ]  
}
```

> For Hedge position mode:

```prism-code
{  
  "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
  "status": 200,  
  "result": [  
    {  
        "symbol": "BTCUSDT",  
        "positionAmt": "0.001",  
        "entryPrice": "22185.2",  
        "breakEvenPrice": "0.0",    
        "markPrice": "21123.05052574",  
        "unRealizedProfit": "-1.06214947",  
        "liquidationPrice": "19731.45529116",  
        "leverage": "4",  
        "maxNotionalValue": "100000000",  
        "marginType": "cross",  
        "isolatedMargin": "0.00000000",  
        "isAutoAddMargin": "false",  
        "positionSide": "LONG",  
        "notional": "21.12305052",  
        "isolatedWallet": "0",  
        "updateTime": 1655217461579  
    },  
    {  
        "symbol": "BTCUSDT",  
        "positionAmt": "0.000",  
        "entryPrice": "0.0",  
        "breakEvenPrice": "0.0",    
        "markPrice": "21123.05052574",  
        "unRealizedProfit": "0.00000000",  
        "liquidationPrice": "0",  
        "leverage": "4",  
        "maxNotionalValue": "100000000",  
        "marginType": "cross",  
        "isolatedMargin": "0.00000000",  
        "isAutoAddMargin": "false",  
        "positionSide": "SHORT",  
        "notional": "0",  
        "isolatedWallet": "0",  
        "updateTime": 0  
    }  
],  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 20  
    }  
  ]  
}
```