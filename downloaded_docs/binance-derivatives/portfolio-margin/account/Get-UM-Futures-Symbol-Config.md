On this page

# UM Futures Symbol Configuration(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#api-description "Direct link to API Description")

Get current UM account symbol configuration.

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/symbolConfig`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#response-example "Direct link to Response Example")

```prism-code
[  
  {  
  "symbol": "BTCUSDT",   
  "marginType": "CROSSED",  
  "isAutoAddMargin": "false",  
  "leverage": 21,  
  "maxNotionalValue": "1000000",  
  }  
]
```