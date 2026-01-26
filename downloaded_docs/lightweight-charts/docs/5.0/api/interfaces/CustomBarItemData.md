Version: 5.0

On this page

Renderer data for an item within the custom series.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/5.0/api/interfaces/CustomData)<`HorzScaleItem`> = [`CustomData`](/lightweight-charts/docs/5.0/api/interfaces/CustomData)<`HorzScaleItem`>

## Properties[​](#properties "Direct link to Properties")

### x[​](#x "Direct link to x")

> **x**: `number`

Horizontal coordinate for the item. Measured from the left edge of the pane in pixels.

---

### time[​](#time "Direct link to time")

> **time**: `number`

Time scale index for the item. This isn't the timestamp but rather the logical index.

---

### originalData[​](#originaldata "Direct link to originalData")

> **originalData**: `TData`

Original data for the item.

---

### barColor[​](#barcolor "Direct link to barColor")

> **barColor**: `string`

Color assigned for the item, typically used for price line and price scale label.