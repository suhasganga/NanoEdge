Version: Next

On this page

Represents series value formatting options.

## Properties[​](#properties "Direct link to Properties")

### type[​](#type "Direct link to type")

> **type**: `"custom"`

The custom price format.

---

### formatter[​](#formatter "Direct link to formatter")

> **formatter**: [`PriceFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/PriceFormatterFn)

Override price formatting behaviour. Can be used for cases that can't be covered with built-in price formats.

---

### tickmarksFormatter?[​](#tickmarksformatter "Direct link to tickmarksFormatter?")

> `optional` **tickmarksFormatter**: [`TickmarksPriceFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/TickmarksPriceFormatterFn)

Override price formatting for multiple prices. Can be used if formatter should be adjusted based of all values being formatted.

---

### minMove[​](#minmove "Direct link to minMove")

> **minMove**: `number`

The minimum possible step size for price value movement.

#### Default Value[​](#default-value "Direct link to Default Value")

`0.01`

---

### base?[​](#base "Direct link to base?")

> `optional` **base**: `number`

The base value for the price format. It should equal to 1 / [minMove](/lightweight-charts/docs/next/api/interfaces/PriceFormatCustom#minmove).
If this option is specified, we ignore the [minMove](/lightweight-charts/docs/next/api/interfaces/PriceFormatCustom#minmove) option.
It can be useful for cases with very small price movements like `1e-18` where we can reach limitations of floating point precision.