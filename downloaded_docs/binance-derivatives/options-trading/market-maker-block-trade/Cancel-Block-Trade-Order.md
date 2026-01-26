On this page

# Cancel Block Trade Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#api-description "Direct link to API Description")

Cancel a block trade order.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#http-request "Direct link to HTTP Request")

DELETE `eapi/v1/block/order/create`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#request-parameters "Direct link to Request Parameters")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blockOrderMatchingKey | STRING | YES |  |
| recvWindow | INT | NO | The value cannot be greater than 60000 |
| timestamp | INT | YES |  |

## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#response-example "Direct link to Response Example")

```prism-code
{}
```