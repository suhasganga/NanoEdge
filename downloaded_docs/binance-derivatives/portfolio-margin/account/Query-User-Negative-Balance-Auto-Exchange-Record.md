On this page

# Query User Negative Balance Auto Exchange Record (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#api-description "Direct link to API Description")

Query user negative balance auto exchange record

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#http-request "Direct link to HTTP Request")

GET `/papi/v1/portfolio/negative-balance-exchange-record`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#request-weight "Direct link to Request Weight")

**100**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startTime | LONG | YES |  |
| endTime | LONG | YES |  |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

**Note**

> * Response in descending order
> * The max interval between `startTime` and `endTime` is 3 months.

## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#response-example "Direct link to Response Example")

```prism-code
{  
  "total": 2,  
  "rows": [  
    {  
      "startTime": 1736263046841,  
      "endTime": 1736263248179,  
      "details": [  
        {  
          "asset": "ETH",  
          "negativeBalance": 18,  //negative balance amount  
          "negativeMaxThreshold": 5  //the max negative balance threshold  
        }  
      ]  
    },  
    {  
      "startTime": 1736184913252,  
      "endTime": 1736184965474,  
      "details": [  
        {  
          "asset": "BNB",  
          "negativeBalance": 1.10264488,  
          "negativeMaxThreshold": 0  
        }  
      ]  
    }  
  ]  
}
```