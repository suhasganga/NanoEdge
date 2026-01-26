On this page

# Basis

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#api-description "Direct link to API Description")

Query basis

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#http-request "Direct link to HTTP Request")

GET `/futures/data/basis`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pair | STRING | YES | BTCUSD |
| contractType | ENUM | YES | CURRENT\_QUARTER, NEXT\_QUARTER, PERPETUAL |
| period | ENUM | YES | "5m","15m","30m","1h","2h","4h","6h","12h","1d" |
| limit | LONG | NO | Default 30,Max 500 |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |

> * If startTime and endTime are not sent, the most recent data is returned.
> * Only the data of the latest 30 days is available.

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Basis#response-example "Direct link to Response Example")

```prism-code
[    
   {  
        "indexPrice": "29269.93972727",  
        "contractType": "CURRENT_QUARTER",  
        "basisRate": "0.0024",  
        "futuresPrice": "29341.3",  
        "annualizedBasisRate": "0.0283",  
        "basis": "71.36027273",  
        "pair": "BTCUSD",  
        "timestamp": 1653381600000  
   }  
]
```