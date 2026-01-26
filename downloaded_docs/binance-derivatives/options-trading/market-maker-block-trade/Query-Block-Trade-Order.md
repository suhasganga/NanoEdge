On this page

# Query Block Trade Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Order#api-description "Direct link to API Description")

Check block trade order status.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Order#http-request "Direct link to HTTP Request")

GET `/eapi/v1/block/order/orders`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Order#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blockOrderMatchingKey | STRING | NO | If specified, returns the specific block trade associated with the blockOrderMatchingKey |
| endTime | LONG | NO |  |
| startTime | LONG | NO |  |
| underlying | STRING | NO |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Order#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "blockTradeSettlementKey": "7d046e6e-a429-4335-ab9d-6a681febcde5",  
        "expireTime": 1730172115801,  
        "liquidity": "TAKER",  
        "status": "RECEIVED",  
        "createTime": 1730170315803,  
        "legs": [  
            {  
                "symbol": "BNB-241101-700-C",  
                "side": "BUY",  
                "quantity": "1.2",  
                "price": "2.8"  
            }  
        ]  
    },  
    {  
        "blockTradeSettlementKey": "28b96c28-ba05-6906-a47c-703215cfbfe6",  
        "expireTime": 1730171860460,  
        "liquidity": "TAKER",  
        "status": "RECEIVED",  
        "createTime": 1730170060462,  
        "legs": [  
            {  
                "symbol": "BNB-241101-700-C",  
                "side": "BUY",  
                "quantity": "1.66",  
                "price": "20"  
            }  
        ]  
    }  
]  
```