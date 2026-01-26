On this page

# Account Funding Flow (USER\_DATA)

## API Description[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#api-description "Direct link to API Description")

Query account funding flows.

## HTTP Request[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#http-request "Direct link to HTTP Request")

GET `/eapi/v1/bill`

## Request Weight[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| currency | STRING | YES | Asset type, only support USDT as of now |
| recordId | LONG | NO | Return the recordId and subsequent data, the latest data is returned by default, e.g 100000 |
| startTime | LONG | NO | Start Time, e.g 1593511200000 |
| endTime | LONG | NO | End Time, e.g 1593512200000 |
| limit | INT | NO | Number of result sets returned Default:100 Max:1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#response-example "Direct link to Response Example")

```prism-code
[  
  {  
    "id": 1125899906842624000,  
    "asset": "USDT",              // Asset type  
    "amount": "-0.552",           // Amount (positive numbers represent inflow, negative numbers represent outflow)  
    "type": "FEE",                // type (fees)  
    "createDate": 1592449456000,  // Time  
  },  
  {  
    "id": 1125899906842624000,  
    "asset": "USDT",              // Asset type  
    "amount": "100",              // Amount (positive numbers represent inflow, negative numbers represent outflow)  
    "type": "CONTRACT",           // type (buy/sell contracts)  
    "createDate": 1592449456000,  // Time  
  },  
  {  
    "id": 1125899906842624000,  
    "asset": "USDT",              // Asset type  
    "amount": "10000",            // Amount (positive numbers represent inflow, negative numbers represent outflow)  
    "type": "TRANSFER",           // type（Funds transfer）  
    "createDate": 1592448410000,  // Time  
  }  
]
```