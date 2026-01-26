On this page

# Get Portfolio Margin Asset Leverage(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#api-description "Direct link to API Description")

Get Portfolio Margin Asset Leverage

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/margin-asset-leverage`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#request-weightip "Direct link to Request Weight(IP)")

**50**

## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#response-example "Direct link to Response Example")

```prism-code
[  
   {  
       "asset": "USDC",  
       "leverage": 10  
   },  
   {  
       "asset": "USDT",  
       "leverage": 10  
   }  
]
```