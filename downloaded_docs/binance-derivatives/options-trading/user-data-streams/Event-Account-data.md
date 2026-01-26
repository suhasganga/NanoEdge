On this page

# Event: Account data

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#event-description "Direct link to Event Description")

* Update under the following conditions:
  + Account deposit or withdrawal
  + Position info change
  + Periodic update every 10s when having position

## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#event-name "Direct link to Event Name")

`ACCOUNT_UPDATE`

## Update Speed[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#response-example "Direct link to Response Example")

```prism-code
{  
    "stream": "89ljxuL6jFTN3Ej85aYOqH2BYXQ7eeuNYcGm7ktV",  
    "data": {  
        "e": "ACCOUNT_UPDATE",        // Event type  
        "E": 1762914568643,           // Event time  
        "T": 1762914568619,           // Transaction Time  
        "eq": "10000371.61462086",    // account equity in USDT  
        "aeq": "10000475.51032086",   // account adjusted equity in USDT  
        "b": "10000475.51032086",     // account wallet balance in USDT  
        "m": "-103.89570000",         // position value  
        "u": "16.10430000",           // unrealized pnl  
        "i": "32354.38562539",        // initial margin in USDT  
        "M": "6089.28766956"          // maintenance margin in USDT  
    }  
}
```