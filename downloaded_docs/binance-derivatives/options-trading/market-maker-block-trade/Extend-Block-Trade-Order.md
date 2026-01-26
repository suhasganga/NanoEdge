On this page

# Extend Block Trade Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Extend-Block-Trade-Order#api-description "Direct link to API Description")

Extends a block trade expire time by 30 mins from the current time.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Extend-Block-Trade-Order#http-request "Direct link to HTTP Request")

PUT `/eapi/v1/block/order/create`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Extend-Block-Trade-Order#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Extend-Block-Trade-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blockOrderMatchingKey | STRING | YES |  |
| recvWindow | INT | NO | The value cannot be greater than 60000 |
| timestamp | INT | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Extend-Block-Trade-Order#response-example "Direct link to Response Example")

```prism-code
{  
    "blockTradeSettlementKey": "3668822b8-1baa-6a2f-adb8-d3de6289b361",  
    "expireTime": 1730172007000,  
    "liquidity": "TAKER",  
    "status": "RECEIVED",  
    "createTime": 1730170088111,  
    "legs": [  
        {  
            "symbol": "BNB-241101-700-C",  
            "side": "BUY",  
            "quantity": "1.2",  
            "price": "2.8"  
        }  
    ]  
}
```