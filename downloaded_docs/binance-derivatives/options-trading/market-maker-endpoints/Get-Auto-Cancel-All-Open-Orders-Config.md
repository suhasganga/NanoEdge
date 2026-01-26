On this page

# Get Auto-Cancel All Open Orders (Kill-Switch) Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#api-description "Direct link to API Description")

This endpoint returns the auto-cancel parameters for each underlying symbol. Note only active auto-cancel parameters will be returned, if countdownTime is set to 0 (ie. countdownTime has been turned off), the underlying symbol and corresponding countdownTime parameter will not be returned in the response.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#http-request "Direct link to HTTP Request")

GET `/eapi/v1/countdownCancelAll`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#request-weight "Direct link to Request Weight")

1

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | NO | Option underlying, e.g BTCUSDT |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * countdownTime = 0 means the function is disabled.

## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config#response-example "Direct link to Response Example")

```prism-code
{  
  "underlying": "ETHUSDT",  
  "countdownTime": 100000  
}
```