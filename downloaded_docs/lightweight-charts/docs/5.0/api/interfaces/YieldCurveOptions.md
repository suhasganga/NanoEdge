Version: 5.0

On this page

Options specific to yield curve charts.

## Properties[​](#properties "Direct link to Properties")

### baseResolution[​](#baseresolution "Direct link to baseResolution")

> **baseResolution**: `number`

The smallest time unit for the yield curve, typically representing one month.
This value determines the granularity of the time scale.

#### Default Value[​](#default-value "Direct link to Default Value")

```prism-code
1
```

---

### minimumTimeRange[​](#minimumtimerange "Direct link to minimumTimeRange")

> **minimumTimeRange**: `number`

The minimum time range to be displayed on the chart, in units of baseResolution.
This ensures that the chart always shows at least this much time range, even if there's less data.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

```prism-code
120 (10 years)
```

---

### startTimeRange[​](#starttimerange "Direct link to startTimeRange")

> **startTimeRange**: `number`

The starting time value for the chart, in units of baseResolution.
This determines where the time scale begins.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

```prism-code
0
```

---

### formatTime()?[​](#formattime "Direct link to formatTime()?")

> `optional` **formatTime**: (`months`) => `string`

Optional custom formatter for time values on the horizontal axis.
If not provided, a default formatter will be used.

#### Parameters[​](#parameters "Direct link to Parameters")

• **months**: `number`

The number of months (or baseResolution units) to format

#### Returns[​](#returns "Direct link to Returns")

`string`