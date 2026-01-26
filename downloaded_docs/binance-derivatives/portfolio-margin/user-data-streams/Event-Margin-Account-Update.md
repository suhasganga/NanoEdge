On this page

# Event: Margin Account Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#event-description "Direct link to Event Description")

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.

## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#event-name "Direct link to Event Name")

`outboundAccountPosition`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#response-example "Direct link to Response Example")

```prism-code
{  
  "e": "outboundAccountPosition", //Event type  
  "E": 1564034571105,             //Event Time  
  "u": 1564034571073,             //Time of last account update  
  "U": 1027053479517,             // time updateID  
  "B": [                          //Balances Array  
    {  
      "a": "ETH",                 //Asset  
      "f": "10000.000000",        //Free  
      "l": "0.000000"             //Locked  
    }  
  ]  
}
```