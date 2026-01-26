On this page

# Accept Block Trade Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Accept-Block-Trade-Order#api-description "Direct link to API Description")

Accept a block trade order

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Accept-Block-Trade-Order#http-request "Direct link to HTTP Request")

POST `/eapi/v1/block/order/execute`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Accept-Block-Trade-Order#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Accept-Block-Trade-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blockOrderMatchingKey | STRING | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Accept-Block-Trade-Order#response-example "Direct link to Response Example")

```prism-code
{  
    "blockTradeSettlementKey": "7d046e6e-a429-4335-ab9d-6a681febcde5",  
    "expireTime": 1730172115801,  
    "liquidity": "MAKER",  
    "status": "ACCEPTED",  
    "createTime": 1730170315803,  
    "legs": [  
        {  
            "symbol": "BNB-241101-700-C",  
            "side": "SELL",  
            "quantity": "1.2",  
            "price": "2.8"  
        }  
    ]  
}
```