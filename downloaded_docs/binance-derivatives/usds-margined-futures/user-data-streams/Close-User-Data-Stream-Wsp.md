On this page

# Close User Data Stream (USER\_STREAM)

## API Description[​](/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#api-description "Direct link to API Description")

Close out a user data stream.

## Method[​](/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#method "Direct link to Method")

`userDataStream.stop`

## Request[​](/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#request "Direct link to Request")

```prism-code
{  
  "id": "819e1b1b-8c06-485b-a13e-131326c69599",  
  "method": "userDataStream.stop",  
  "params": {  
    "apiKey": "vmPUZE6mv9SD5VNHk9HlWFsOr9aLE2zvsw0MuIgwCIPy8atIco14y7Ju91duEh8A"  
  }  
}
```

## Request Weight[​](/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#response-example "Direct link to Response Example")

```prism-code
{  
  "id": "819e1b1b-8c06-485b-a13e-131326c69599",  
  "status": 200,  
  "result": {},  
   "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 2  
    }  
  ]  
}
```