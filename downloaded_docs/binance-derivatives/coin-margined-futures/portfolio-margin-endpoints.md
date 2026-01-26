On this page

# Classic Portfolio Margin Account Information (USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#api-description "Direct link to API Description")

Get Classic Portfolio Margin current account information.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#http-request "Direct link to HTTP Request")

GET `/dapi/v1/pmAccountInfo`

## Request Weight(IP)[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#request-weightip "Direct link to Request Weight(IP)")

**5**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO |  |

> * maxWithdrawAmount is for asset transfer out to the spot wallet.

## Response Example[​](/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints#response-example "Direct link to Response Example")

```prism-code
{  
    "maxWithdrawAmountUSD": "25347.92083245",   // Classic Portfolio margin maximum virtual amount for transfer out in USD  
    "asset": "BTC",            // asset name  
    "maxWithdrawAmount": "1.33663654",        // maximum amount for transfer out  
}
```