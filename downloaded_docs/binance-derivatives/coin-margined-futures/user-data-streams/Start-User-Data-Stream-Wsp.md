On this page

# Start User Data Stream (USER\_STREAM)

## API Description[​](/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#api-description "Direct link to API Description")

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

## Method[​](/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#method "Direct link to Method")

`userDataStream.start`

## Request[​](/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#request "Direct link to Request")

```prism-code
{  
  "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
  "method": "userDataStream.start",  
  "params": {  
    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"  
  }  
}
```

## Request Weight[​](/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `apiKey` | STRING | NO | Required if session is not authenticated via session.logon |

## Response Example[​](/docs/derivatives/coin-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#response-example "Direct link to Response Example")

```prism-code
{  
  "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
  "status": 200,  
  "result": {  
    "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"  
  },  
   "rateLimits": [  
	{  
		"rateLimitType": "REQUEST_WEIGHT",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 2400,  
        "count": 8  
    }  
  ]  
}
```