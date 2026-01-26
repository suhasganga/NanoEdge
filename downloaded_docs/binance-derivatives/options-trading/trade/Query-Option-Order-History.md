On this page

# Query Option Order History (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#api-description "Direct link to API Description")

Query all finished orders within 5 days, finished status: CANCELLED FILLED REJECTED.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#http-request "Direct link to HTTP Request")

GET `/eapi/v1/historyOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#request-weight "Direct link to Request Weight")

**3**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option trading pair |
| orderId | LONG | NO | Returns the orderId and subsequent orders, the most recent order is returned by default |
| startTime | LONG | NO | Start Time, e.g 1593511200000 |
| endTime | LONG | NO | End Time, e.g 1593512200000 |
| limit | INT | NO | Number of result sets returned Default:100 Max:1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/trade/Query-Option-Order-History#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "orderId": 4611922413427359795,  
        "symbol": "BTC-220715-2000-C",  
        "price": "18000.00000000",  
        "quantity": "-0.50000000",  
        "executedQty": "-0.50000000",  
        "side": "SELL",  
        "type": "LIMIT",  
        "timeInForce": "GTC",  
        "reduceOnly": false,  
        "createTime": 1657867694244,  
        "updateTime": 1657867888216,  
        "status": "FILLED",  
        "avgPrice": "18000.00000000",  
        "clientOrderId": "",  
        "priceScale": 2,  
        "quantityScale": 2,  
        "optionSide": "CALL",  
        "quoteAsset": "USDT",  
        "mmp": false  
    }  
]
```