On this page

# Query Margin Max Withdraw(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#api-description "Direct link to API Description")

Query Margin Max Withdraw

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/maxWithdraw`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than `60000` |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw#response-example "Direct link to Response Example")

```prism-code
{   
  "amount": "60"  
}
```