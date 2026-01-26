On this page

# User Exercise Record (USER\_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#api-description "Direct link to API Description")

Get account exercise records.

## HTTP Request[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#http-request "Direct link to HTTP Request")

GET `/eapi/v1/exerciseRecord`

## Request Weight[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO | Option trading pair, e.g BTC-200730-9000-C |
| startTime | LONG | NO | startTime |
| endTime | LONG | NO | endTime |
| limit | INT | NO | default 1000, max 1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "id": "1125899906842624042",  
        "currency": "USDT",  
        "symbol": "BTC-220721-25000-C",  
        "exercisePrice": "25000.00000000",  
        "quantity": "1.00000000",  
        "amount": "0.00000000",  
        "fee": "0.00000000",  
        "createDate": 1658361600000,  
        "priceScale": 2,  
        "quantityScale": 2,  
        "optionSide": "CALL",  
        "positionSide": "LONG",  
        "quoteAsset": "USDT"  
    }  
]
```