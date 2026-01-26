On this page

# Option Margin Account Information (USER\_DATA)

## API Description[​](/docs/derivatives/options-trading/account#api-description "Direct link to API Description")

Get current account information.

## HTTP Request[​](/docs/derivatives/options-trading/account#http-request "Direct link to HTTP Request")

GET `/eapi/v1/marginAccount`

## Request Weight[​](/docs/derivatives/options-trading/account#request-weight "Direct link to Request Weight")

**3**

## Request Parameters[​](/docs/derivatives/options-trading/account#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/account#response-example "Direct link to Response Example")

```prism-code
{  
    "asset": [  
        {  
            "asset": "USDT",                     // Asset type  
            "marginBalance": "99998.87365244",   // Account balance  
            "equity": "99998.87365244",          // Account equity  
            "available": "96883.72734374",       // Available funds  
            "initialMargin": "3115.14630870",    // Initial margin  
            "maintMargin": "0.00000000",         // Maintenance margin  
            "unrealizedPNL": "0.00000000",       // Unrealized profit/loss  
            "adjustedEquity": "99998.87365244"   // margin balance + qualified Long Position Value  
        }  
    ],  
    "greek": [  
        {  
            "underlying": "BTCUSDT",    // Option Underlying  
            "delta": "0",               // Account delta  
            "theta": "0",               // Account theta  
            "gamma": "0",               // Account gamma  
            "vega": "0"                 // Account vega    
        }  
    ],  
    "time": 1762843368098,  
    "canTrade": true,  
    "canDeposit": true,  
    "canWithdraw": true,  
    "reduceOnly": false  
}   
```