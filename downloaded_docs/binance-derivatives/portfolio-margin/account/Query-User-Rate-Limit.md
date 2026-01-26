On this page

# Query User Rate Limit (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#api-description "Direct link to API Description")

Query User Rate Limit

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#http-request "Direct link to HTTP Request")

GET `/papi/v1/rateLimit/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-User-Rate-Limit#response-example "Direct link to Response Example")

```prism-code
[  
  {  
        "rateLimitType": "ORDERS",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 1200  
    }  
]
```