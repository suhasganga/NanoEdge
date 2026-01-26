On this page

# CM Notional and Leverage Brackets(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#api-description "Direct link to API Description")

Query CM notional and leverage brackets

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/leverageBracket`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "symbol": "BTCUSD_PERP",  
        "brackets": [  
            {  
                "bracket": 1,   // bracket level  
                "initialLeverage": 125,  // the maximum leverage  
                "qtyCap": 50,  // upper edge of base asset quantity  
                "qtyFloor": 0,  // lower edge of base asset quantity  
                "maintMarginRatio": 0.004, // maintenance margin rate  
                "cum": 0.0 // Auxiliary number for quick calculation   
            },  
        ]  
    }  
]
```