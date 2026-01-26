On this page

# Cancel All Open Orders(TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders#api-description "Direct link to API Description")

Cancel All Open Orders

## HTTP Request[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders#http-request "Direct link to HTTP Request")

DELETE `/dapi/v1/allOpenOrders`

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders#response-example "Direct link to Response Example")

```prism-code
{  
	"code": 200,   
	"msg": "The operation of cancel all open order is done."  
}
```