On this page

# Accept the offered quote (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/convert/Accept-Quote#api-description "Direct link to API Description")

Accept the offered quote by quote ID.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/convert/Accept-Quote#http-request "Direct link to HTTP Request")

POST `/fapi/v1/convert/acceptQuote`

## Request Weight[​](/docs/derivatives/usds-margined-futures/convert/Accept-Quote#request-weight "Direct link to Request Weight")

**200(IP)**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/convert/Accept-Quote#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| quoteId | STRING | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/convert/Accept-Quote#response-example "Direct link to Response Example")

```prism-code
{  
  "orderId":"933256278426274426",  
  "createTime":1623381330472,  
  "orderStatus":"PROCESS" //PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL  
}
```