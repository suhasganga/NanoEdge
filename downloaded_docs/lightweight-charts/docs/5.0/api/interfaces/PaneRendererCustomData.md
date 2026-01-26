Version: 5.0

On this page

Data provide to the custom series pane view which can be used within the renderer
for drawing the series data.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/5.0/api/interfaces/CustomData)<`HorzScaleItem`>

## Properties[​](#properties "Direct link to Properties")

### bars[​](#bars "Direct link to bars")

> **bars**: readonly [`CustomBarItemData`](/lightweight-charts/docs/5.0/api/interfaces/CustomBarItemData)<`HorzScaleItem`, `TData`>[]

List of all the series' items and their x coordinates.

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

Spacing between consecutive bars.

---

### visibleRange[​](#visiblerange "Direct link to visibleRange")

> **visibleRange**: [`IRange`](/lightweight-charts/docs/5.0/api/interfaces/IRange)<`number`>

The current visible range of items on the chart.