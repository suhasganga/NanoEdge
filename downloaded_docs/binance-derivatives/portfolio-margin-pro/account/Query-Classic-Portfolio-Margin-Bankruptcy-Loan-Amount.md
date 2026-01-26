On this page

# Query Portfolio Margin Pro Bankruptcy Loan Amount(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#api-description "Direct link to API Description")

Query Portfolio Margin Pro Bankruptcy Loan Amount

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/pmLoan`

## Request Weight(UID)[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#request-weightuid "Direct link to Request Weight(UID)")

**500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If there’s no classic portfolio margin bankruptcy loan, the amount would be 0

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#response-example "Direct link to Response Example")

```prism-code
{  
   "asset": "BUSD",     
   "amount":  "579.45", // portfolio margin bankruptcy loan amount in BUSD  
}
```