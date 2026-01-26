On this page

# Event: Greek Update

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#event-description "Direct link to Event Description")

`GREEK_UPDATE` will be triggered when a position changes or periodically every 10 seconds when having position.

## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#event-name "Direct link to Event Name")

`GREEK_UPDATE`

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#response-example "Direct link to Response Example")

```prism-code
{  
        "e": "GREEK_UPDATE",  
        "E": 1762917544216,  
        "T": 1762917544216,  
        "G": [  
            {  
                "u": "BTCUSDT",   
                "d": "-0.01304097",   //delta  
                "g": "-0.00000124",   //gamma  
                "t": "16.11648100",   //theta   
                "v": "-3.83444011"    //vega  
            }  
        ]  
}
```