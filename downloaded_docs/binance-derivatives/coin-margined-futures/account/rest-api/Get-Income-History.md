On this page

# Get Income History(USER\_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#api-description "Direct link to API Description")

Get income history

## HTTP Request[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#http-request "Direct link to HTTP Request")

GET `/dapi/v1/income`

## Request Weight[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| incomeType | STRING | NO | "TRANSFER","WELCOME\_BONUS", "FUNDING\_FEE", "REALIZED\_PNL", "COMMISSION", "INSURANCE\_CLEAR", and "DELIVERED\_SETTELMENT" |
| startTime | LONG | NO | Timestamp in ms to get funding from INCLUSIVE. |
| endTime | LONG | NO | Timestamp in ms to get funding until INCLUSIVE. |
| page | INT | NO |  |
| limit | INT | NO | Default 100; max 1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * If `incomeType`  is not sent, all kinds of flow will be returned
> * "trandId" is unique in the same "incomeType" for a user
> * The time between `startTime` and `endTime` can not be longer than 1 year

## Response Example[​](/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History#response-example "Direct link to Response Example")

```prism-code
[  
	{  
    	"symbol": "",				// trade symbol, if existing  
    	"incomeType": "TRANSFER",	// income type  
    	"income": "-0.37500000",	// income amount  
    	"asset": "BTC",				// income asset  
    	"info":"WITHDRAW",			// extra information  
    	"time": 1570608000000,  
    	"tranId":"9689322392",		// transaction id  
    	"tradeId":""				// trade id, if existing  
	},  
	{  
   		"symbol": "BTCUSD_200925",  
    	"incomeType": "COMMISSION",   
    	"income": "-0.01000000",  
    	"asset": "BTC",  
    	"info":"",  
    	"time": 1570636800000,  
    	"tranId":"9689322392",  
    	"tradeId":"2059192"  
	}  
]
```