On this page

# Cancel All UM Open Conditional Orders (TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#api-description "Direct link to API Description")

Cancel All UM Open Conditional Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#http-request "Direct link to HTTP Request")

`DELETE /papi/v1/um/conditional/allOpenOrders`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#request-weightorder "Direct link to Request Weight(Order)")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#response-example "Direct link to Response Example")

```prism-code
{  
    "code": "200",   
    "msg": "The operation of cancel all conditional open order is done."  
}
```