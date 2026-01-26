On this page

# Query Portfolio Margin Pro Negative Balance Interest History(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#api-description "Direct link to API Description")

Query interest history of negative balance for portfolio margin.

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/portfolio/interest-history`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#request-weightip "Direct link to Request Weight(IP)")

**50**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| size | LONG | NO | Default:10 Max:100 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#response-example "Direct link to Response Example")

```prism-code
[  
    {  
        "asset": "USDT",      
        "interest": "24.4440",               //interest amount  
        "interestAccruedTime": 1670227200000,  
        "interestRate": "0.0001164",         //daily interest rate  
        "principal": "210000"  
    }   
]
```