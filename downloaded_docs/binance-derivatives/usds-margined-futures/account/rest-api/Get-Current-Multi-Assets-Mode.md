On this page

# Get Current Multi-Assets Mode (USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#api-description "Direct link to API Description")

Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on ***Every symbol***

## HTTP Request[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#http-request "Direct link to HTTP Request")

GET `/fapi/v1/multiAssetsMargin`

## Request Weight[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#request-weight "Direct link to Request Weight")

**30**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#response-example "Direct link to Response Example")

```prism-code
{  
	"multiAssetsMargin": true // "true": Multi-Assets Mode; "false": Single-Asset Mode  
}
```