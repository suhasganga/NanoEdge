On this page

# Cancel All Option Orders By Underlying (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#api-description "Direct link to API Description")

Cancel all active orders on specified underlying.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#http-request "Direct link to HTTP Request")

DELETE `/eapi/v1/allOpenOrdersByUnderlying`

## Request Weight[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | YES | Option underlying, e.g BTCUSDT |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/trade/Cancel-All-Option-Orders-By-Underlying#response-example "Direct link to Response Example")

```prism-code
{  
    "code": 0,  
    "msg": "success",  
}
```