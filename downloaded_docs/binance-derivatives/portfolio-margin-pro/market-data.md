On this page

# Query Portfolio Margin Asset Index Price (MARKET\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data#api-description "Direct link to API Description")

Query Portfolio Margin Asset Index Price

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/asset-index-price`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data#request-weightip "Direct link to Request Weight(IP)")

**1** if send asset or **50** if not send asset

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/market-data#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | NO |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data#response-example "Direct link to Response Example")

```prism-code
[  
   {  
       "asset": "BTC",  
       "assetIndexPrice": "28251.9136906",  // in USD  
       "time": 1683518338121  
   }  
]
```