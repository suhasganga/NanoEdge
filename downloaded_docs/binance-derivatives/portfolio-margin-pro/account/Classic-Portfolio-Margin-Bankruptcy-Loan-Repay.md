On this page

# Portfolio Margin Pro Bankruptcy Loan Repay

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#api-description "Direct link to API Description")

Repay Portfolio Margin Pro Bankruptcy Loan

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/repay`

## Request Weight(UID)[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#request-weightuid "Direct link to Request Weight(UID)")

**3000**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | STRING | NO | SPOT or MARGIN，default SPOT |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

* Please note that the API Key has enabled Spot & Margin Trading permissions to access this endpoint.

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay#response-example "Direct link to Response Example")

```prism-code
{  
    "tranId": 58203331886213504  
}
```