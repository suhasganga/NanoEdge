On this page

# Futures Account Configuration(USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config#api-description "Direct link to API Description")

Query account configuration

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config#http-request "Direct link to HTTP Request")

GET `/fapi/v1/accountConfig`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config#response-example "Direct link to Response Example")

```prism-code
{     
    "feeTier": 0,               // account commission tier   
    "canTrade": true,           // if can trade  
    "canDeposit": true,         // if can transfer in asset  
    "canWithdraw": true,        // if can transfer out asset  
    "dualSidePosition": true,  
    "updateTime": 0,            // reserved property, please ignore   
    "multiAssetsMargin": false,  
    "tradeGroupId": -1  
}
```