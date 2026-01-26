On this page

# Query Block Trade Details (USER\_DATA)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#api-description "Direct link to API Description")

Query block trade details; returns block trade details from counterparty's perspective.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#http-request "Direct link to HTTP Request")

GET `/eapi/v1/block/order/execute`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blockOrderMatchingKey | STRING | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#response-example "Direct link to Response Example")

```prism-code
{  
    "blockTradeSettlementKey": "12b96c28-ba05-8906-c89t-703215cfb2e6",  
    "expireTime": 1730171860460,  
    "liquidity": "MAKER",  
    "status": "RECEIVED",  
    "createTime": 1730170060462,  
    "legs": [  
        {  
            "symbol": "BNB-241101-700-C",  
            "side": "SELL",  
            "quantity": "1.66",  
            "price": "20"  
        }  
    ]  
}
```