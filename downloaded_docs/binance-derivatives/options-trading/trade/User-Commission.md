On this page

# User Commission (USER\_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/User-Commission#api-description "Direct link to API Description")

Get account commission.

## HTTP Request[​](/docs/derivatives/options-trading/trade/User-Commission#http-request "Direct link to HTTP Request")

GET `/eapi/v1/commission`

## Request Weight[​](/docs/derivatives/options-trading/trade/User-Commission#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/User-Commission#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/trade/User-Commission#response-example "Direct link to Response Example")

```prism-code
{  
    "commissions": [  
        {  
            "underlying": "BTCUSDT",  
            "makerFee": "0.000240",  
            "takerFee": "0.000240"  
        },  
        {  
            "underlying": "ETHUSDT",  
            "makerFee": "0.000240",  
            "takerFee": "0.000240"  
        },  
        {  
            "underlying": "BNBUSDT",  
            "makerFee": "0.000240",  
            "takerFee": "0.000240"  
        },  
        {  
            "underlying": "SOLUSDT",  
            "makerFee": "0.000240",  
            "takerFee": "0.000240"  
        },  
        {  
            "underlying": "XRPUSDT",  
            "makerFee": "0.000240",  
            "takerFee": "0.000240"  
        },  
        {  
            "underlying": "DOGEUSDT",  
            "makerFee": "0.000240",  
            "takerFee": "0.000240"  
        }  
    ]  
}
```