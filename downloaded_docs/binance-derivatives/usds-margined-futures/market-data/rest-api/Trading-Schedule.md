On this page

# Trading Schedule

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#api-description "Direct link to API Description")

Trading session schedules for the underlying assets of TradFi Perps are provided for a one-week period starting from the day prior to the query time, covering both the U.S. equity and commodity markets. Equity market session types include "PRE\_MARKET", "REGULAR", "AFTER\_MARKET", "OVERNIGHT", and "NO\_TRADING", while commodity market session types include "REGULAR" and "NO\_TRADING".

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#http-request "Direct link to HTTP Request")

GET `/fapi/v1/tradingSchedule`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#response-example "Direct link to Response Example")

```prism-code
{  
  "updateTime": 1761286643918,  
  "marketSchedules": {  
    "EQUITY": {  
      "sessions": [  
        {  
          "startTime": 1761177600000,  
          "endTime": 1761206400000,  
          "type": "OVERNIGHT"  
        },  
        {  
          "startTime": 1761206400000,  
          "endTime": 1761226200000,  
          "type": "PRE_MARKET"  
        }   
      ]  
    },  
    "COMMODITY": {  
      "sessions": [  
        {  
          "startTime": 1761724800000,  
          "endTime": 1761744600000,  
          "type": "NO_TRADING"  
        },  
        {  
          "startTime": 1761744600000,  
          "endTime": 1761768000000,  
          "type": "REGULAR"  
        }  
      ]  
    }  
  }  
}
```