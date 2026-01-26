On this page

# Get Funding Rate Info

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#api-description "Direct link to API Description")

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#http-request "Direct link to HTTP Request")

GET `/dapi/v1/fundingInfo`

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "symbol": "BTCUSD_PERP",  
        "adjustedFundingRateCap": "0.02500000",  
        "adjustedFundingRateFloor": "-0.02500000",  
        "fundingIntervalHours": 8,  
        "disclaimer": false   // ignore  
    }  
]
```