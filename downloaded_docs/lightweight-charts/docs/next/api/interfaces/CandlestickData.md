Version: Next

On this page

Structure describing a single item of data for candlestick series

## Extends[​](#extends "Direct link to Extends")

* [`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData)<`HorzScaleItem`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### color?[​](#color "Direct link to color?")

> `optional` **color**: `string`

Optional color value for certain data item. If missed, color from options is used

---

### borderColor?[​](#bordercolor "Direct link to borderColor?")

> `optional` **borderColor**: `string`

Optional border color value for certain data item. If missed, color from options is used

---

### wickColor?[​](#wickcolor "Direct link to wickColor?")

> `optional` **wickColor**: `string`

Optional wick color value for certain data item. If missed, color from options is used

---

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The bar time.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData) . [`time`](/lightweight-charts/docs/next/api/interfaces/OhlcData#time)

---

### open[​](#open "Direct link to open")

> **open**: `number`

The open price.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData) . [`open`](/lightweight-charts/docs/next/api/interfaces/OhlcData#open)

---

### high[​](#high "Direct link to high")

> **high**: `number`

The high price.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData) . [`high`](/lightweight-charts/docs/next/api/interfaces/OhlcData#high)

---

### low[​](#low "Direct link to low")

> **low**: `number`

The low price.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData) . [`low`](/lightweight-charts/docs/next/api/interfaces/OhlcData#low)

---

### close[​](#close "Direct link to close")

> **close**: `number`

The close price.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData) . [`close`](/lightweight-charts/docs/next/api/interfaces/OhlcData#close)

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData) . [`customValues`](/lightweight-charts/docs/next/api/interfaces/OhlcData#customvalues)