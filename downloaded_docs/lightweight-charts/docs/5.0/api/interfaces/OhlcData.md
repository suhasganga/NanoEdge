Version: 5.0

On this page

Represents a bar with a [Time](/lightweight-charts/docs/5.0/api/type-aliases/Time) and open, high, low, and close prices.

## Extends[​](#extends "Direct link to Extends")

* [`WhitespaceData`](/lightweight-charts/docs/5.0/api/interfaces/WhitespaceData)<`HorzScaleItem`>

## Extended by[​](#extended-by "Direct link to Extended by")

* [`BarData`](/lightweight-charts/docs/5.0/api/interfaces/BarData)
* [`CandlestickData`](/lightweight-charts/docs/5.0/api/interfaces/CandlestickData)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/5.0/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The bar time.

#### Overrides[​](#overrides "Direct link to Overrides")

[`WhitespaceData`](/lightweight-charts/docs/5.0/api/interfaces/WhitespaceData) . [`time`](/lightweight-charts/docs/5.0/api/interfaces/WhitespaceData#time)

---

### open[​](#open "Direct link to open")

> **open**: `number`

The open price.

---

### high[​](#high "Direct link to high")

> **high**: `number`

The high price.

---

### low[​](#low "Direct link to low")

> **low**: `number`

The low price.

---

### close[​](#close "Direct link to close")

> **close**: `number`

The close price.

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`WhitespaceData`](/lightweight-charts/docs/5.0/api/interfaces/WhitespaceData) . [`customValues`](/lightweight-charts/docs/5.0/api/interfaces/WhitespaceData#customvalues)