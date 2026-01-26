On this page

# User Commission Rate (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#api-description "Direct link to API Description")

Query user commission rate

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#http-request "Direct link to HTTP Request")

GET `/dapi/v1/commissionRate`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate#response-example "Direct link to Response Example")

```prism-code
{  
	"symbol": "BTCUSD_PERP",  
  	"makerCommissionRate": "0.00015",  // 0.015%  
  	"takerCommissionRate": "0.00040"   // 0.040%  
}
```