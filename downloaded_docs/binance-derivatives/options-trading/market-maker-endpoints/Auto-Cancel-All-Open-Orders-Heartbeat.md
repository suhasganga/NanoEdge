On this page

# Auto-Cancel All Open Orders (Kill-Switch) Heartbeat (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#api-description "Direct link to API Description")

This endpoint resets the time from which the countdown will begin to the time this messaged is received. It should be called repeatedly as heartbeats. Multiple heartbeats can be updated at once by specifying the underlying symbols as a list (ex. BTCUSDT,ETHUSDT) in the underlyings parameter.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#http-request "Direct link to HTTP Request")

POST `/eapi/v1/countdownCancelAllHeartBeat`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#request-weight "Direct link to Request Weight")

10

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlyings | STRING | YES | Option Underlying Symbols, e.g BTCUSDT,ETHUSDT |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * The response will only include underlying symbols where the heartbeat has been successfully updated.

## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat#response-example "Direct link to Response Example")

```prism-code
{  
 "underlyings":["BTCUSDT","ETHUSDT"]  
}
```