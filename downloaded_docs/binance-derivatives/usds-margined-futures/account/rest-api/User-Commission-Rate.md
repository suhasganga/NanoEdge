On this page

# User Commission Rate (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#api-description "Direct link to API Description")

Get User Commission Rate

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#http-request "Direct link to HTTP Request")

GET `/fapi/v1/commissionRate`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#response-example "Direct link to Response Example")

```prism-code
{  
	"symbol": "BTCUSDT",  
  	"makerCommissionRate": "0.0002",  // 0.02%  
  	"takerCommissionRate": "0.0004",  // 0.04%  
    "rpiCommissionRate": "0.00005"   // 0.005%  
}
```