On this page

# Futures Trading Quantitative Rules Indicators (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators#api-description "Direct link to API Description")

Futures trading quantitative rules indicators, for more information on this, please refer to the [Futures Trading Quantitative Rules](https://www.binance.com/en/support/faq/4f462ebe6ff445d4a170be7d9e897272)

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators#http-request "Direct link to HTTP Request")

GET `/fapi/v1/apiTradingStatus`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators#request-weight "Direct link to Request Weight")

* **1** for a single symbol
* **10** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators#response-example "Direct link to Response Example")

> **Response:**

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
        ],  
        "ETHUSDT": [  
            {  
				"isLocked": true,  
			    "plannedRecoverTime": 1545741270000,  
                "indicator": "UFR",  
                "value": 0.05,  
                "triggerValue": 0.995  
            },  
            {  
				"isLocked": true,  
			    "plannedRecoverTime": 1545741270000,  
                "indicator": "IFER",  
                "value": 0.99,  
                "triggerValue": 0.99  
            },  
            {  
				"isLocked": true,  
			    "plannedRecoverTime": 1545741270000,  
                "indicator": "GCR",  
                "value": 0.99,  
                "triggerValue": 0.99  
            }  
            {  
				"isLocked": true,  
			    "plannedRecoverTime": 1545741270000,  
                "indicator": "DR",  
                "value": 0.99,  
                "triggerValue": 0.99  
            }  
        ]  
    },  
    "updateTime": 1545741270000  
}
```

> Or (account violation triggered)

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