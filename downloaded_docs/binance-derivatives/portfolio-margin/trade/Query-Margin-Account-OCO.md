On this page

# Query Margin Account's OCO (USER\_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#api-description "Direct link to API Description")

Retrieves a specific OCO based on provided optional parameters

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/orderList`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#weight "Direct link to Weight")

**5**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#parameters "Direct link to Parameters:")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orderListId | LONG | NO | Either orderListId or origClientOrderId must be provided |
| origClientOrderId | STRING | NO | Either orderListId or origClientOrderId must be provided |
| recvWindow | LONG | NO | The value cannot be greater than 60000 |
| timestamp | LONG | YES |  |

## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#response "Direct link to Response:")

```prism-code
{  
  "orderListId": 27,  
  "contingencyType": "OCO",  
  "listStatusType": "EXEC_STARTED",  
  "listOrderStatus": "EXECUTING",  
  "listClientOrderId": "h2USkA5YQpaXHPIrkd96xE",  
  "transactionTime": 1565245656253,  
  "symbol": "LTCBTC",  
  "orders": [  
    {  
      "symbol": "LTCBTC",  
      "orderId": 4,  
      "clientOrderId": "qD1gy3kc3Gx0rihm9Y3xwS"  
    },  
    {  
      "symbol": "LTCBTC",  
      "orderId": 5,  
      "clientOrderId": "ARzZ9I00CPM8i3NhmU9Ega"  
    }  
  ]  
}
```