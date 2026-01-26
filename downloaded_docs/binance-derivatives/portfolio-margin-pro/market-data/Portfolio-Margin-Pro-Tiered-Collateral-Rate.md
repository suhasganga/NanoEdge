On this page

# Portfolio Margin Pro Tiered Collateral Rate(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#api-description "Direct link to API Description")

Portfolio Margin PRO Tiered Collateral Rate

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#http-request "Direct link to HTTP Request")

GET `/sapi/v2/portfolio/collateralRate`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#request-weightip "Direct link to Request Weight(IP)")

**50**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "asset": "BNB",  
        "collateralInfo": [  
            {  
            "tierFloor": "0.0000",  
            "tierCap": "1000.0000",  
            "collateralRate": "1.0000",  
            "cum":"0.0000"    //account equity quick addition number  
            },  
            {  
            "tierFloor": "1000.0000",  
            "tierCap": "2000.0000",  
            "collateralRate": "0.9000",  
            "cum":"0.0000"  
            }  
        ]  
    },  
    {  
        "asset": "USDT",  
        "collateralInfo": [  
            {  
                "tierFloor": "0.0000",  
                "tierCap": "1000.0000",  
                "collateralRate": "1.0000",  
                "cum":"0.0000"  
            },  
            {  
                "tierFloor": "1000.0000",  
                "tierCap": "2000.0000",  
                "collateralRate": "0.9999",  
                "cum":"0.0000"  
            }  
        ]  
    }  
]
```