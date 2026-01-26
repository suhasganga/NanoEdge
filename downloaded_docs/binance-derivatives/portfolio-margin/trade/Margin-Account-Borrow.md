On this page

# Margin Account Borrow(MARGIN)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#api-description "Direct link to API Description")

Apply for a margin loan.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#http-request "Direct link to HTTP Request")

POST `/papi/v1/marginLoan`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#request-weightip "Direct link to Request Weight(IP)")

**100**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| amount | DECIMAL | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow#response-example "Direct link to Response Example")

```prism-code
{  
    //transaction id  
    "tranId": 100000001  
}
```