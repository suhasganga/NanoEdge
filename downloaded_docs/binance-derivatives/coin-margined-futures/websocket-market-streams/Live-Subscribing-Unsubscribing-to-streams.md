On this page

# Live Subscribing/Unsubscribing to streams

* The following data can be sent through the websocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
* The `id` used in the JSON payloads is an unsigned INT used as an identifier to uniquely identify the messages going back and forth.

## Subscribe to a stream[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#subscribe-to-a-stream "Direct link to Subscribe to a stream")

> **Response**

```prism-code
{  
  "result": null,  
  "id": 1  
}
```

* **Request**

  {  
  "method": "SUBSCRIBE",  
  "params":  
  [  
  "btcusd\_200925@aggTrade",  
  "btcusd\_200925@depth"  
  ],  
  "id": 1  
  }

## Unsubscribe to a stream[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#unsubscribe-to-a-stream "Direct link to Unsubscribe to a stream")

> **Response**

```prism-code
{  
  "result": null,  
  "id": 312  
}
```

* **Request**

  {  
  "method": "UNSUBSCRIBE",  
  "params":  
  [  
  "btcusd\_200925@depth"  
  ],  
  "id": 312  
  }

## Listing Subscriptions[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#listing-subscriptions "Direct link to Listing Subscriptions")

> **Response**

```prism-code
{  
  "result": [  
    "btcusd_200925@aggTrade"  
  ],  
  "id": 3  
}
```

* **Request**

  {  
  "method": "LIST\_SUBSCRIPTIONS",  
  "id": 3  
  }

## Setting Properties[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#setting-properties "Direct link to Setting Properties")

Currently, the only property can be set is to set whether `combined` stream payloads are enabled are not.
The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true` when connecting using `/stream/`.

> **Response**

```prism-code
{  
  "result": null,  
  "id": 5  
}
```

* **Request**

  {  
  "method": "SET\_PROPERTY",  
  "params":  
  [  
  "combined",  
  true  
  ],  
  "id": 5  
  }

## Retrieving Properties[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams#retrieving-properties "Direct link to Retrieving Properties")

> **Response**

```prism-code
{  
  "result": true, // Indicates that combined is set to true.  
  "id": 2  
}
```

* **Request**

  {  
  "method": "GET\_PROPERTY",  
  "params":  
  [  
  "combined"  
  ],  
  "id": 2  
  }