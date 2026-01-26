On this page

# Modify Isolated Position Margin(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#api-description "Direct link to API Description")

Modify Isolated Position Margin

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#http-request "Direct link to HTTP Request")

POST `/fapi/v1/positionMargin`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| positionSide | ENUM | NO | Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent with Hedge Mode. |
| amount | DECIMAL | YES |  |
| type | INT | YES | 1: Add position margin，2: Reduce position margin |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * Only for isolated symbol

## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin#response-example "Direct link to Response Example")

```prism-code
{  
	"amount": 100.0,  
  	"code": 200,  
  	"msg": "Successfully modify position margin.",  
  	"type": 1  
}
```