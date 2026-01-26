On this page

# Get User Commission Rate for CM(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#api-description "Direct link to API Description")

Get User Commission Rate for CM

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/commissionRate`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#response-example "Direct link to Response Example")

```prism-code
{  
    "symbol": "BTCUSD_PERP",  
    "makerCommissionRate": "0.00015",  // 0.015%  
    "takerCommissionRate": "0.00040"   // 0.040%  
}
```