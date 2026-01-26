Version: 4.2

On this page

Data provide to the custom series pane view which can be used within the renderer
for drawing the series data.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/4.2/api/interfaces/CustomData)<`HorzScaleItem`>

## Properties[​](#properties "Direct link to Properties")

### bars[​](#bars "Direct link to bars")

> **bars**: readonly [`CustomBarItemData`](/lightweight-charts/docs/4.2/api/interfaces/CustomBarItemData)<`HorzScaleItem`, `TData`>[]

List of all the series' items and their x coordinates.

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

Spacing between consecutive bars.

---

### visibleRange[​](#visiblerange "Direct link to visibleRange")

> **visibleRange**: [`Range`](/lightweight-charts/docs/4.2/api/interfaces/Range)<`number`>

The current visible range of items on the chart.