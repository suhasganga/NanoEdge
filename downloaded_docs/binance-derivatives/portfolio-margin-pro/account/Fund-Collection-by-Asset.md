On this page

# Fund Collection by Asset(USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#api-description "Direct link to API Description")

Transfers specific asset from Futures Account to Margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#http-request "Direct link to HTTP Request")

POST `/sapi/v1/portfolio/asset-collection`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#request-weightip "Direct link to Request Weight(IP)")

**60**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * The BNB transfer is not be supported

## Response Example[​](/docs/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#response-example "Direct link to Response Example")

```prism-code
{  
    "msg": "success"  
}
```