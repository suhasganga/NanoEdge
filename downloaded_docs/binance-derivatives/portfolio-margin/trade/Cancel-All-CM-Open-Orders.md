On this page

# Cancel All CM Open Orders(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders#api-description "Direct link to API Description")

Cancel all active LIMIT orders on specific symbol

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders#http-request "Direct link to HTTP Request")

DELETE `/papi/v1/cm/allOpenOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders#response-example "Direct link to Response Example")

```prism-code
{  
    "code": 200,   
    "msg": "The operation of cancel all open order is done."  
}
```