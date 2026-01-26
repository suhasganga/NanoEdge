On this page

# Query Current CM Open Conditional Order(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order#api-description "Direct link to API Description")

Query Current CM Open Conditional Order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/conditional/openOrder`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| strategyId | LONG | NO |  |
| newClientStrategyId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

Notes:

> * Either `strategyId` or `newClientStrategyId` must be sent.
> * If the queried order has been triggered, cancelled or expired, the error message "Order does not exist" will be returned.

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order#response-example "Direct link to Response Example")

```prism-code
{              
    "newClientStrategyId": "abc",   
    "strategyId":123445,  
    "strategyStatus":"NEW",  
    "strategyType": "TRAILING_STOP_MARKET",                                  
    "origQty": "0.40",                        
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "stopPrice": "9300",                // please ignore when order type is TRAILING_STOP_MARKET  
    "symbol": "BTCUSD",  
    "bookTime": 1566818724710,              // order time   
    "updateTime": 1566818724722,  
    "timeInForce": "GTC",  
    "activatePrice": "9020",            // activation price, only return with TRAILING_STOP_MARKET order  
    "priceRate": "0.3"                 // callback rate, only return with TRAILING_STOP_MARKET order                   
}
```