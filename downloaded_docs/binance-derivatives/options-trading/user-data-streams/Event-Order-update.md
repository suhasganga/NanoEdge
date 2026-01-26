On this page

# Event: Order update

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#event-description "Direct link to Event Description")

When new order created, order status changed will push such event. event type is `ORDER_TRADE_UPDATE`.

**Side**

* BUY
* SELL

**Order Type**

* LIMIT

**Execution Type**

* NEW
* CANCELED
* EXPIRED
* TRADE

**Order Status**

* NEW
* PARTIALLY\_FILLED
* FILLED
* CANCELED
* EXPIRED

**Time in force**

* GTC
* IOC
* FOK
* GTX

## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#event-name "Direct link to Event Name")

`ORDER_TRADE_UPDATE`

## Update Speed[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Order-update#response-example "Direct link to Response Example")

```prism-code
{  
  "e":"ORDER_TRADE_UPDATE",             // Event Type  
  "E":1568879465651,                    // Event Time  
  "T":1568879465650,                    // Transaction Time  
  "o":{                                  
    "s":"BTCUSDT",                      // Symbol  
    "c":"TEST",                         // Client Order Id  
      // special client order id:  
      // starts with "autoclose-": liquidation order  
      // "adl_autoclose": ADL auto close order  
    "S":"SELL",                          // Side  
    "o":"TRAILING_STOP_MARKET",          // Order Type  
    "f":"GTC",                           // Time in Force  
    "q":"0.001",                         // Original Quantity  
    "p":"0",                             // Original Price  
    "ap":"0",                            // Average Price  
    "x":"NEW",                           // Execution Type  
    "X":"NEW",                           // Order Status  
    "i":8886774,                         // Order Id  
    "l":"0",                             // Order Last Filled Quantity  
    "z":"0",                             // Order Filled Accumulated Quantity  
    "L":"0",                             // Last Filled Price  
    "N":"USDT",                          // Commission Asset  
    "n":"0",                             // Commission, negative means fee charge  
    "T":1568879465650,                   // Order Trade Time  
    "t":0,                               // Trade Id  
    "b":"0",                             // Bids qty  
    "a":"9.91",                          // Ask qty  
    "m":false,                           // Is this trade the maker side?  
    "R":false,                           // Is this reduce only  
    "ot":"TRAILING_STOP_MARKET",         // Original Order Type  
    "rp":"0",                            // Realized Profit of the trade  
  }  
}
```