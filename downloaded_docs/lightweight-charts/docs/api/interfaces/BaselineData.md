Version: 5.1

On this page

Structure describing a single item of data for baseline series

## Extends[​](#extends "Direct link to Extends")

* [`SingleValueData`](/lightweight-charts/docs/api/interfaces/SingleValueData)<`HorzScaleItem`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### topFillColor1?[​](#topfillcolor1 "Direct link to topFillColor1?")

> `optional` **topFillColor1**: `string`

Optional top area top fill color value for certain data item. If missed, color from options is used

---

### topFillColor2?[​](#topfillcolor2 "Direct link to topFillColor2?")

> `optional` **topFillColor2**: `string`

Optional top area bottom fill color value for certain data item. If missed, color from options is used

---

### topLineColor?[​](#toplinecolor "Direct link to topLineColor?")

> `optional` **topLineColor**: `string`

Optional top area line color value for certain data item. If missed, color from options is used

---

### bottomFillColor1?[​](#bottomfillcolor1 "Direct link to bottomFillColor1?")

> `optional` **bottomFillColor1**: `string`

Optional bottom area top fill color value for certain data item. If missed, color from options is used

---

### bottomFillColor2?[​](#bottomfillcolor2 "Direct link to bottomFillColor2?")

> `optional` **bottomFillColor2**: `string`

Optional bottom area bottom fill color value for certain data item. If missed, color from options is used

---

### bottomLineColor?[​](#bottomlinecolor "Direct link to bottomLineColor?")

> `optional` **bottomLineColor**: `string`

Optional bottom area line color value for certain data item. If missed, color from options is used

---

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The time of the data.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`SingleValueData`](/lightweight-charts/docs/api/interfaces/SingleValueData) . [`time`](/lightweight-charts/docs/api/interfaces/SingleValueData#time)

---

### value[​](#value "Direct link to value")

> **value**: `number`

Price value of the data.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`SingleValueData`](/lightweight-charts/docs/api/interfaces/SingleValueData) . [`value`](/lightweight-charts/docs/api/interfaces/SingleValueData#value)

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`SingleValueData`](/lightweight-charts/docs/api/interfaces/SingleValueData) . [`customValues`](/lightweight-charts/docs/api/interfaces/SingleValueData#customvalues)