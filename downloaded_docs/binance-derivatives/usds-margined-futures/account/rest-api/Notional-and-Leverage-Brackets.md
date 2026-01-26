On this page

# Notional and Leverage Brackets (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#api-description "Direct link to API Description")

Query user notional and leverage bracket on speicfic symbol

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#http-request "Direct link to HTTP Request")

GET `/fapi/v1/leverageBracket`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#response-example "Direct link to Response Example")

> **Response:**

```prism-code
[  
    {  
        "symbol": "ETHUSDT",  
	    "notionalCoef": 1.50,  //user symbol bracket multiplier, only appears when user's symbol bracket is adjusted   
        "brackets": [  
            {  
                "bracket": 1,   // Notional bracket  
                "initialLeverage": 75,  // Max initial leverage for this bracket  
                "notionalCap": 10000,  // Cap notional of this bracket  
                "notionalFloor": 0,  // Notional threshold of this bracket   
                "maintMarginRatio": 0.0065, // Maintenance ratio for this bracket  
                "cum": 0.0 // Auxiliary number for quick calculation   
                 
            },  
        ]  
    }  
]
```

> **OR** (if symbol sent)

```prism-code
{  
    "symbol": "ETHUSDT",  
    "notionalCoef": 1.50,  
    "brackets": [  
        {  
            "bracket": 1,  
            "initialLeverage": 75,  
            "notionalCap": 10000,  
            "notionalFloor": 0,  
            "maintMarginRatio": 0.0065,  
            "cum":0  
        },  
    ]  
}
```