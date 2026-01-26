Version: 5.1

On this page

Represents a marker drawn above or below a data point to indicate a price change update.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T** = [`Time`](/lightweight-charts/docs/api/type-aliases/Time)

The type of the time value, defaults to Time.

## Properties[​](#properties "Direct link to Properties")

### time[​](#time "Direct link to time")

> **time**: `T`

The point on the horizontal scale.

---

### value[​](#value "Direct link to value")

> **value**: `number`

The price value for the data point.

---

### sign[​](#sign "Direct link to sign")

> **sign**: [`MarkerSign`](/lightweight-charts/docs/api/enumerations/MarkerSign)

The direction of the price change.