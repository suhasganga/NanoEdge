On this page

# Margin Max Borrow(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#api-description "Direct link to API Description")

Query margin max borrow

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/maxBorrowable`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than `60000` |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Margin-Max-Borrow#response-example "Direct link to Response Example")

```prism-code
{  
  "amount": "1.69248805", // account's currently max borrowable amount with sufficient system availability  
  "borrowLimit": "60" // max borrowable amount limited by the account level  
}
```