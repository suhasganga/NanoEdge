On this page

# Order status(USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#api-description "Direct link to API Description")

Query order status by order ID.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#http-request "Direct link to HTTP Request")

GET `/fapi/v1/convert/orderStatus`

## Request Weight[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#request-weight "Direct link to Request Weight")

**50(IP)**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orderId | STRING | NO | Either orderId or quoteId is required |
| quoteId | STRING | NO | Either orderId or quoteId is required |

## Response Example[​](/docs/derivatives/usds-margined-futures/convert/Order-Status#response-example "Direct link to Response Example")

```prism-code
{  
  "orderId":933256278426274426,  
  "orderStatus":"SUCCESS",  
  "fromAsset":"BTC",  
  "fromAmount":"0.00054414",  
  "toAsset":"USDT",  
  "toAmount":"20",  
  "ratio":"36755",  
  "inverseRatio":"0.00002721",  
  "createTime":1623381330472  
}
```