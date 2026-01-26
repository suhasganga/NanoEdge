Version: 5.1

On this page

Represents a range of bars and the number of bars outside the range.

## Extends[​](#extends "Direct link to Extends")

* `Partial` <[`IRange`](/lightweight-charts/docs/api/interfaces/IRange)<`HorzScaleItem`>>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](#properties "Direct link to Properties")

### barsBefore[​](#barsbefore "Direct link to barsBefore")

> **barsBefore**: `number`

The number of bars before the start of the range.
Positive value means that there are some bars before (out of logical range from the left) the [IRange.from](/lightweight-charts/docs/api/interfaces/IRange#from) logical index in the series.
Negative value means that the first series' bar is inside the passed logical range, and between the first series' bar and the [IRange.from](/lightweight-charts/docs/api/interfaces/IRange#from) logical index are some bars.

---

### barsAfter[​](#barsafter "Direct link to barsAfter")

> **barsAfter**: `number`

The number of bars after the end of the range.
Positive value in the `barsAfter` field means that there are some bars after (out of logical range from the right) the [IRange.to](/lightweight-charts/docs/api/interfaces/IRange#to) logical index in the series.
Negative value means that the last series' bar is inside the passed logical range, and between the last series' bar and the [IRange.to](/lightweight-charts/docs/api/interfaces/IRange#to) logical index are some bars.

---

### from?[​](#from "Direct link to from?")

> `optional` **from**: `HorzScaleItem`

The from value. The start of the range.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

`Partial.from`

---

### to?[​](#to "Direct link to to?")

> `optional` **to**: `HorzScaleItem`

The to value. The end of the range.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

`Partial.to`