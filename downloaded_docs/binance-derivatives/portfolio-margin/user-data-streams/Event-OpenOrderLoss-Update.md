On this page

# Event: OpenOrderLoss Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#event-description "Direct link to Event Description")

Cross margin order margin stream

## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#event-name "Direct link to Event Name")

`openOrderLoss`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#response-example "Direct link to Response Example")

```prism-code
{  
    "e": "openOrderLoss",      //Event Type  
    "E": 1678710578788,        // Event Time  
    "O": [  
        {                    // Update Data  
        "a": "BUSD",  
        "o": "-0.1232313"       // Amount  
        },   
        {  
        "a": "BNB",  
        "o": "-12.1232313"  
        }  
    ]  
}
```