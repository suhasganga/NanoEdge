On this page

# Cancel all Option orders on specific symbol (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#api-description "Direct link to API Description")

Cancel all active order on a symbol.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#http-request "Direct link to HTTP Request")

DELETE `/eapi/v1/allOpenOrders`

## Request Weight[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option trading pair, e.g BTC-200730-9000-C |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/trade/Cancel-all-Option-orders-on-specific-symbol#response-example "Direct link to Response Example")

```prism-code
{  
  "code": 0,  
  "msg": "success"  
}
```