On this page

# Query CM Position Information(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#api-description "Direct link to API Description")

Get current CM position information.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/positionRisk`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| marginAsset | STRING | NO |  |
| pair | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If neither `marginAsset` nor `pair` is sent, positions of all symbols with `TRADING` status will be returned.
> * for One-way Mode user, the response will only show the "BOTH" positions
> * for Hedge Mode user, the response will show "LONG", and "SHORT" positions.

**Note**

> * Please use with user data stream `ACCOUNT_UPDATE` to meet your timeliness and accuracy needs.

## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-CM-Position-Information#response-example "Direct link to Response Example")

* For One-way position mode:

```prism-code
[  
    {  
        "symbol": "BTCUSD_201225",  
        "positionAmt": "1",  
        "entryPrice": "11707.70000003",  
        "markPrice": "11788.66626667",  
        "unRealizedProfit": "0.00005866",  
        "liquidationPrice": "6170.20509059",   
        "leverage": "125",  
        "positionSide": "LONG",  
        "updateTime": 1627026881327,  
        "maxQty": "50",  
        "notionalValue": "0.00084827"    
    }  
]
```

> * For Hedge position mode(only return with position):

```prism-code
[  
    {  
        "symbol": "BTCUSD_201225",  
        "positionAmt": "1",  
        "entryPrice": "11707.70000003",  
        "markPrice": "11788.66626667",  
        "unRealizedProfit": "0.00005866",  
        "liquidationPrice": "6170.20509059",   
        "leverage": "125",  
        "positionSide": "LONG",  
        "updateTime": 1627026881327,  
        "maxQty": "50",  
        "notionalValue": "0.00084827"   
    },  
    {  
        "symbol": "BTCUSD_201225",  
        "positionAmt": "1",  
        "entryPrice": "11707.70000003",  
        "markPrice": "11788.66626667",  
        "unRealizedProfit": "0.00005866",  
        "liquidationPrice": "6170.20509059",   
        "leverage": "125",  
        "positionSide": "LONG",  
        "updateTime": 1627026881327,  
        "maxQty": "50",  
        "notionalValue": "0.00084827"   
    }  
]
```