On this page

# Notional Bracket for Symbol(USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#api-description "Direct link to API Description")

Get the symbol's notional bracket list.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#http-request "Direct link to HTTP Request")

GET `/dapi/v2/leverageBracket`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Symbol#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "symbol": "BTCUSD_PERP",  
        "notionalCoef": 1.50,  //user symbol bracket multiplier, only appears when user's symbol bracket is adjusted   
        "brackets": [  
            {  
                "bracket": 1,   // bracket level  
                "initialLeverage": 125,  // the maximum leverage  
                "qtyCap": 50,  // upper edge of base asset quantity  
                "qtylFloor": 0,  // lower edge of base asset quantity  
                "maintMarginRatio": 0.004 // maintenance margin rate  
				"cum": 0.0 // Auxiliary number for quick calculation   
            },  
        ]  
    }  
]
```