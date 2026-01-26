On this page

# Margin Account Repay(MARGIN)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#api-description "Direct link to API Description")

Repay for a margin loan.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#http-request "Direct link to HTTP Request")

POST `/papi/v1/repayLoan`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#request-weight "Direct link to Request Weight")

**100**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| amount | DECIMAL | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay#response-example "Direct link to Response Example")

```prism-code
{  
    //transaction id  
    "tranId": 100000001  
}
```