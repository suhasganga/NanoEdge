On this page

# Basis

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Basis#api-description "Direct link to API Description")

Query future basis

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Basis#http-request "Direct link to HTTP Request")

GET `/futures/data/basis`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Basis#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Basis#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pair | STRING | YES | BTCUSDT |
| contractType | ENUM | YES | CURRENT\_QUARTER, NEXT\_QUARTER, PERPETUAL |
| period | ENUM | YES | "5m","15m","30m","1h","2h","4h","6h","12h","1d" |
| limit | LONG | YES | Default 30,Max 500 |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |

> * If startTime and endTime are not sent, the most recent data is returned.
> * Only the data of the latest 30 days is available.

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Basis#response-example "Direct link to Response Example")

```prism-code
[    
    {  
        "indexPrice": "34400.15945055",  
        "contractType": "PERPETUAL",  
        "basisRate": "0.0004",  
        "futuresPrice": "34414.10",  
        "annualizedBasisRate": "",  
        "basis": "13.94054945",  
        "pair": "BTCUSDT",  
        "timestamp": 1698742800000  
    }  
]
```