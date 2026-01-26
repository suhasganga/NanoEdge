On this page

# Query User Rate Limit (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit#api-description "Direct link to API Description")

Query User Rate Limit

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit#http-request "Direct link to HTTP Request")

GET `/fapi/v1/rateLimit/order`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "rateLimitType": "ORDERS",  
    "interval": "SECOND",  
    "intervalNum": 10,  
    "limit": 10000,  
  },  
  {  
    "rateLimitType": "ORDERS",  
    "interval": "MINUTE",  
    "intervalNum": 1,  
    "limit": 20000,  
  }  
]
```