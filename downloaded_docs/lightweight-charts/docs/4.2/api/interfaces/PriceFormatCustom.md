Version: 4.2

On this page

Represents series value formatting options.

## Properties[​](#properties "Direct link to Properties")

### type[​](#type "Direct link to type")

> **type**: `"custom"`

The custom price format.

---

### formatter[​](#formatter "Direct link to formatter")

> **formatter**: [`PriceFormatterFn`](/lightweight-charts/docs/4.2/api/type-aliases/PriceFormatterFn)

Override price formatting behaviour. Can be used for cases that can't be covered with built-in price formats.

---

### minMove[​](#minmove "Direct link to minMove")

> **minMove**: `number`

The minimum possible step size for price value movement.

#### Default Value[​](#default-value "Direct link to Default Value")

`0.01`