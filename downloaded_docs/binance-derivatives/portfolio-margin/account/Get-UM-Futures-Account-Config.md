On this page

# UM Futures Account Configuration(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#api-description "Direct link to API Description")

Query UM Futures account configuration

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/accountConfig`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config#response-example "Direct link to Response Example")

```prism-code
{     
    "feeTier": 0,               // account commission tier   
    "canTrade": true,           // if can trade  
    "canDeposit": true,         // if can transfer in asset  
    "canWithdraw": true,        // if can transfer out asset  
    "dualSidePosition": true,  
    "updateTime": 1724416653850,            // reserved property, please ignore   
    "multiAssetsMargin": false,  
    "tradeGroupId": -1  
}
```