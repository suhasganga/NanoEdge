On this page

# Get User Commission Rate for UM(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#api-description "Direct link to API Description")

Get User Commission Rate for UM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/commissionRate`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM#response-example "Direct link to Response Example")

```prism-code
{  
    "symbol": "BTCUSDT",  
    "makerCommissionRate": "0.0002",  // 0.02%  
    "takerCommissionRate": "0.0004"   // 0.04%  
}
```