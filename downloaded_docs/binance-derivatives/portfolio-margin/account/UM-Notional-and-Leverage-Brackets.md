On this page

# UM Notional and Leverage Brackets (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#api-description "Direct link to API Description")

Query UM notional and leverage brackets

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#http-request "Direct link to HTTP Request")

`GET /papi/v1/um/leverageBracket`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "symbol": "ETHUSDT",  
        "notionalCoef": "4.0",  
        "brackets": [  
            {  
                "bracket": 1,   // Notional bracket  
                "initialLeverage": 75,  // Max initial leverage for this bracket  
                "notionalCap": 10000,  // Cap notional of this bracket  
                "notionalFloor": 0,  // Notional threshold of this bracket   
                "maintMarginRatio": 0.0065, // Maintenance ratio for this bracket  
                "cum":0 // Auxiliary number for quick calculation   
            },  
        ]  
    }  
]
```