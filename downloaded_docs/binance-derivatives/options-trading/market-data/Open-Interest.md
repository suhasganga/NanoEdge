On this page

# Open Interest

## API Description[​](/docs/derivatives/options-trading/market-data/Open-Interest#api-description "Direct link to API Description")

Get open interest for specific underlying asset on specific expiration date.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Open-Interest#http-request "Direct link to HTTP Request")

GET `/eapi/v1/openInterest`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Open-Interest#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Open-Interest#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlyingAsset | STRING | YES | underlying asset, e.g ETH/BTC |
| expiration | STRING | YES | expiration date, e.g 221225 |

## Response Example[​](/docs/derivatives/options-trading/market-data/Open-Interest#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "symbol": "ETH-221119-1175-P",  
        "sumOpenInterest": "4.01",  
        "sumOpenInterestUsd": "4880.2985615624",  
        "timestamp": "1668754020000"  
    }  
]
```