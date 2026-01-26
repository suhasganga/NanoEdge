On this page

# Portfolio Margin UM Trading Quantitative Rules Indicators(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#api-description "Direct link to API Description")

Portfolio Margin UM Trading Quantitative Rules Indicators

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/apiTradingStatus`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#request-weight "Direct link to Request Weight")

**1** for a single symbol
**10** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#response-example "Direct link to Response Example")

```prism-code
{  
    "indicators": { // indicator: quantitative rules indicators, value: user's indicators value, triggerValue: trigger indicator value threshold of quantitative rules.   
        "BTCUSDT": [  
            {  
                "isLocked": true,  
                "plannedRecoverTime": 1545741270000,  
                "indicator": "UFR",  // Unfilled Ratio (UFR)  
                "value": 0.05,  // Current value  
                "triggerValue": 0.995  // Trigger value  
            },  
            {  
                "isLocked": true,  
                "plannedRecoverTime": 1545741270000,  
                "indicator": "IFER",  // IOC/FOK Expiration Ratio (IFER)  
                "value": 0.99,  // Current value  
                "triggerValue": 0.99  // Trigger value  
            },  
            {  
                "isLocked": true,  
                "plannedRecoverTime": 1545741270000,  
                "indicator": "GCR",  // GTC Cancellation Ratio (GCR)  
                "value": 0.99,  // Current value  
                "triggerValue": 0.99  // Trigger value  
            },  
            {  
                "isLocked": true,  
                "plannedRecoverTime": 1545741270000,  
                "indicator": "DR",  // Dust Ratio (DR)  
                "value": 0.99,  // Current value  
                "triggerValue": 0.99  // Trigger value  
            }  
        ]  
    },  
    "updateTime": 1545741270000  
}
```

Or (account violation triggered)

```prism-code
{  
    "indicators":{  
        "ACCOUNT":[  
            {  
                "indicator":"TMV",  //  Too many violations under multiple symbols trigger account violation  
                "value":10,  
                "triggerValue":1,  
                "plannedRecoverTime":1644919865000,  
                "isLocked":true  
            }  
        ]  
    },  
    "updateTime":1644913304748  
}
```