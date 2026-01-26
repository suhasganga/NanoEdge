On this page

# Notional Bracket for Pair(USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#api-description "Direct link to API Description")

**Not recommended to continue using this v1 endpoint**

Get the pair's default notional bracket list, may return ambiguous values when there have been multiple different `symbol` brackets under the `pair`, suggest using the following `GET /dapi/v2/leverageBracket` query instead to get the specific `symbol` notional bracket list.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#http-request "Direct link to HTTP Request")

GET `/dapi/v1/leverageBracket`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pair | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "pair": "BTCUSD",  
        "brackets": [  
            {  
                "bracket": 1,   // bracket level  
                "initialLeverage": 125,  // the maximum leverage  
                "qtyCap": 50,  // upper edge of base asset quantity  
                "qtylFloor": 0,  // lower edge of base asset quantity  
                "maintMarginRatio": 0.004 // maintenance margin rate  
				"cum": 0.0  // Auxiliary number for quick calculation   
            },  
        ]  
    }  
]
```