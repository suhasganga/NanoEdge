On this page

# Query Portfolio Margin Pro Bankruptcy Loan Repay History(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#api-description "Direct link to API Description")

Query repay history of pmloan for portfolio margin pro.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/pmloan-history`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#request-weightip "Direct link to Request Weight(IP)")

**500**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| current | LONG | NO | Currently querying page. Start from 1. Default:1 |
| size | LONG | NO | Default:10 Max:100 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

* `startTime` and `endTime` cannot be longer than 360 days
* If `startTime` and `endTime` not sent, return records of the last 30 days by default.
* If `startTime`is sent and `endTime` is not sent, return records of [startTime, startTime+30d].
* If `startTime` is not sent and `endTime` is sent, return records of [endTime-30d, endTime].

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Query-Portfolio-Margin-Pro-Bankruptcy-Loan-Repay-History#response-example "Direct link to Response Example")

```prism-code
{  
  "total": 3,  
  "rows": [  
    {  
      "asset": "USDT",  
      "amount": "404.80294503",  
      "repayTime": 1731336427804  
    },  
    {  
      "asset": "USDT",  
      "amount": "4620.41204574",  
      "repayTime": 1726125090016  
    }  
  ]  
}
```