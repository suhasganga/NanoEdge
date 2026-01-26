On this page

# Start User Data Stream(USER\_STREAM)

## API Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#api-description "Direct link to API Description")

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

## HTTP Request[​](/docs/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#http-request "Direct link to HTTP Request")

POST `/papi/v1/listenKey`

## Request Weight[​](/docs/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#request-parameters "Direct link to Request Parameters")

**None**

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#response-example "Direct link to Response Example")

```prism-code
{  
  "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"  
}
```