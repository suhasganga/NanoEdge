Version: 5.1

On this page

Represents series value formatting options.
The precision and minMove properties allow wide customization of formatting.

## Examples[​](#examples "Direct link to Examples")

```prism-code
`minMove=0.01`, `precision` is not specified - prices will change like 1.13, 1.14, 1.15 etc.
```

```prism-code
`minMove=0.01`, `precision=3` - prices will change like 1.130, 1.140, 1.150 etc.
```

```prism-code
`minMove=0.05`, `precision` is not specified - prices will change like 1.10, 1.15, 1.20 etc.
```

## Properties[​](#properties "Direct link to Properties")

### type[​](#type "Direct link to type")

> **type**: `"percent"` | `"price"` | `"volume"`

Built-in price formats:

* `'price'` is the most common choice; it allows customization of precision and rounding of prices.
* `'volume'` uses abbreviation for formatting prices like `1.2K` or `12.67M`.
* `'percent'` uses `%` sign at the end of prices.

---

### precision[​](#precision "Direct link to precision")

> **precision**: `number`

Number of digits after the decimal point.
If it is not set, then its value is calculated automatically based on minMove.

#### Default Value[​](#default-value "Direct link to Default Value")

`2` if both [minMove](/lightweight-charts/docs/api/interfaces/PriceFormatBuiltIn#minmove) and [precision](/lightweight-charts/docs/api/interfaces/PriceFormatBuiltIn#precision) are not provided, calculated automatically based on [minMove](/lightweight-charts/docs/api/interfaces/PriceFormatBuiltIn#minmove) otherwise.

---

### minMove[​](#minmove "Direct link to minMove")

> **minMove**: `number`

The minimum possible step size for price value movement. This value shouldn't have more decimal digits than the precision.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`0.01`

---

### base?[​](#base "Direct link to base?")

> `optional` **base**: `number`

The base value for the price format. It should equal to 1 / [minMove](/lightweight-charts/docs/api/interfaces/PriceFormatBuiltIn#minmove).
If this option is specified, we ignore the [minMove](/lightweight-charts/docs/api/interfaces/PriceFormatBuiltIn#minmove) option.
It can be useful for cases with very small price movements like `1e-18` where we can reach limitations of floating point precision.