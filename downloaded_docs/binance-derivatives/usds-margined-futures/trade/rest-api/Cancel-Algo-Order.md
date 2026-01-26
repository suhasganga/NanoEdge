On this page

# Cancel Algo Order (TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#api-description "Direct link to API Description")

Cancel an active algo order.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#http-request "Direct link to HTTP Request")

DELETE `/fapi/v1/algoOrder`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algoId | LONG | NO |  |
| clientAlgoId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Either `algoId` or `clientAlgoId` must be sent.

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#response-example "Direct link to Response Example")

```prism-code
{  
   "algoId": 2146760,  
   "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
   "code": "200",  
   "msg": "success"  
}
```