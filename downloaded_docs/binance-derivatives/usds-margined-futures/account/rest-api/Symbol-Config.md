On this page

# Symbol Configuration(USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#api-description "Direct link to API Description")

Get current account symbol configuration.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#http-request "Direct link to HTTP Request")

GET `/fapi/v1/symbolConfig`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config#response-example "Direct link to Response Example")

```prism-code
[  
  {  
  "symbol": "BTCUSDT",   
  "marginType": "CROSSED",  
  "isAutoAddMargin": false,  
  "leverage": 21,  
  "maxNotionalValue": "1000000",  
  }  
]
```