Version: 4.1

On this page

Structure describing a single item of data for area series

## Extends[​](#extends "Direct link to Extends")

* [`SingleValueData`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData)<`HorzScaleItem`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/4.1/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### lineColor?[​](#linecolor "Direct link to lineColor?")

> `optional` **lineColor**: `string`

Optional line color value for certain data item. If missed, color from options is used

---

### topColor?[​](#topcolor "Direct link to topColor?")

> `optional` **topColor**: `string`

Optional top color value for certain data item. If missed, color from options is used

---

### bottomColor?[​](#bottomcolor "Direct link to bottomColor?")

> `optional` **bottomColor**: `string`

Optional bottom color value for certain data item. If missed, color from options is used

---

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The time of the data.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`SingleValueData`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData) . [`time`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData#time)

---

### value[​](#value "Direct link to value")

> **value**: `number`

Price value of the data.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`SingleValueData`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData) . [`value`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData#value)

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`SingleValueData`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData) . [`customValues`](/lightweight-charts/docs/4.1/api/interfaces/SingleValueData#customvalues)