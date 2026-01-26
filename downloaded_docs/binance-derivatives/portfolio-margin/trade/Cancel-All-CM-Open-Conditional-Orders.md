On this page

# Cancel All CM Open Conditional Orders(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders#api-description "Direct link to API Description")

Cancel All CM Open Conditional Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders#http-request "Direct link to HTTP Request")

DELETE `/papi/v1/cm/conditional/allOpenOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders#response-example "Direct link to Response Example")

```prism-code
{  
    "code": "200",   
    "msg": "The operation of cancel all conditional open order is done."  
}
```