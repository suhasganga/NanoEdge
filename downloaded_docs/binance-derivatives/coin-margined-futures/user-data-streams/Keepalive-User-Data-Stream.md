On this page

# Keepalive User Data Stream (USER\_STREAM)

## API Description[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream#api-description "Direct link to API Description")

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream#http-request "Direct link to HTTP Request")

PUT `/dapi/v1/listenKey`

## Request Weight[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/derivatives/coin-margined-futures/user-data-streams/Keepalive-User-Data-Stream#response-example "Direct link to Response Example")

```prism-code
{  
    "listenKey": "vmNt6gl1so8bXVsaAY153FG5tf63QaODxUarKUM8V8rY4ElSwEe431DNIYNKOkQp"  
}
```