On this page

# Historical Exercise Records

## API Description[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#api-description "Direct link to API Description")

Get historical exercise records.

* REALISTIC\_VALUE\_STRICKEN -> Exercised
* EXTRINSIC\_VALUE\_EXPIRED -> Expired OTM

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#http-request "Direct link to HTTP Request")

GET `/eapi/v1/exerciseHistory`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#request-weight "Direct link to Request Weight")

**3**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | NO | Underlying index like BTCUSDT |
| startTime | LONG | NO | Start Time |
| endTime | LONG | NO | End Time |
| limit | INT | NO | Number of records Default:100 Max:100 |

## Response Example[​](/docs/derivatives/options-trading/market-data/Historical-Exercise-Records#response-example "Direct link to Response Example")

```prism-code
[  
  {   
    "symbol": "BTC-220121-60000-P",            // symbol    
    "strikePrice": "60000",                    // strike price  
    "realStrikePrice": "38844.69652571",       // real strike price  
    "expiryDate": 1642752000000,               // Exercise time  
    "strikeResult": "REALISTIC_VALUE_STRICKEN" // strike result  
  }  
]
```