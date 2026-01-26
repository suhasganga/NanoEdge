On this page

# Send Quote Request(USER\_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#api-description "Direct link to API Description")

Request a quote for the requested token pairs

## HTTP Request[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#http-request "Direct link to HTTP Request")

POST `/fapi/v1/convert/getQuote`

## Request Weight[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#request-weight "Direct link to Request Weight")

**50(IP)**

**360/hour，500/day**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fromAsset | STRING | YES |  |
| toAsset | STRING | YES |  |
| fromAmount | DECIMAL | EITHER | When specified, it is the amount you will be debited after the conversion |
| toAmount | DECIMAL | EITHER | When specified, it is the amount you will be credited after the conversion |
| validTime | ENUM | NO | 10s, default 10s |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

* Either fromAmount or toAmount should be sent
* `quoteId` will be returned only if you have enough funds to convert

## Response Example[​](/docs/derivatives/usds-margined-futures/convert/Send-quote-request#response-example "Direct link to Response Example")

```prism-code
{  
   "quoteId":"12415572564",  
   "ratio":"38163.7",  
   "inverseRatio":"0.0000262",  
   "validTimestamp":1623319461670,  
   "toAmount":"3816.37",  
   "fromAmount":"0.1"  
}
```