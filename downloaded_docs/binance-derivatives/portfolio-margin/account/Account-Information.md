On this page

# Account Information(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Account-Information#api-description "Direct link to API Description")

Query account information

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Account-Information#http-request "Direct link to HTTP Request")

GET `/papi/v1/account`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Account-Information#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Account-Information#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Account-Information#response-example "Direct link to Response Example")

```prism-code
{  
   "uniMMR": "5167.92171923",        // Portfolio margin account maintenance margin rate  
   "accountEquity": "122607.35137903",   // Account equity, in USD value  
   "actualEquity": "73.47428058",   //Account equity without collateral rate, in USD value  
   "accountInitialMargin": "23.72469206",   
   "accountMaintMargin": "23.72469206", // Portfolio margin account maintenance margin, unit：USD  
   "accountStatus": "NORMAL"   // Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
   "virtualMaxWithdrawAmount": "1627523.32459208"   // Portfolio margin maximum amount for transfer out in USD  
   "totalAvailableBalance":"",  
   "totalMarginOpenLoss":"", // in USD margin open order  
   "updateTime": 1657707212154 // last update time   
}
```