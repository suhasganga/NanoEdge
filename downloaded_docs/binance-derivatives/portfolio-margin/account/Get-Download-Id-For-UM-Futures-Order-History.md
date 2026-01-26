On this page

# Get Download Id For UM Futures Order History (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#api-description "Direct link to API Description")

Get download id for UM futures order history

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/order/asyn`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#request-weight "Direct link to Request Weight")

**1500**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startTime | LONG | YES | Timestamp in ms |
| endTime | LONG | YES | Timestamp in ms |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Request Limitation is 10 times per month, shared by front end download page and rest api
> * The time between `startTime` and `endTime` can not be longer than 1 year

## Response Example[​](/docs/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#response-example "Direct link to Response Example")

```prism-code
{  
	"avgCostTimestampOfLast30d":7241837, // Average time taken for data download in the past 30 days  
  	"downloadId":"546975389218332672",  
}
```