Version: 5.1

On this page

A base interface for a data point of single-value series.

## Extends[​](#extends "Direct link to Extends")

* [`WhitespaceData`](/lightweight-charts/docs/api/interfaces/WhitespaceData)<`HorzScaleItem`>

## Extended by[​](#extended-by "Direct link to Extended by")

* [`AreaData`](/lightweight-charts/docs/api/interfaces/AreaData)
* [`BaselineData`](/lightweight-charts/docs/api/interfaces/BaselineData)
* [`HistogramData`](/lightweight-charts/docs/api/interfaces/HistogramData)
* [`LineData`](/lightweight-charts/docs/api/interfaces/LineData)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The time of the data.

#### Overrides[​](#overrides "Direct link to Overrides")

[`WhitespaceData`](/lightweight-charts/docs/api/interfaces/WhitespaceData) . [`time`](/lightweight-charts/docs/api/interfaces/WhitespaceData#time)

---

### value[​](#value "Direct link to value")

> **value**: `number`

Price value of the data.

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`WhitespaceData`](/lightweight-charts/docs/api/interfaces/WhitespaceData) . [`customValues`](/lightweight-charts/docs/api/interfaces/WhitespaceData#customvalues)