Version: Next

On this page

Data provide to the custom series pane view which can be used within the renderer
for drawing the series data.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`>

## Properties[​](#properties "Direct link to Properties")

### bars[​](#bars "Direct link to bars")

> **bars**: readonly [`CustomBarItemData`](/lightweight-charts/docs/next/api/interfaces/CustomBarItemData)<`HorzScaleItem`, `TData`>[]

List of all the series' items and their x coordinates.

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

Spacing between consecutive bars.

---

### visibleRange[​](#visiblerange "Direct link to visibleRange")

> **visibleRange**: [`IRange`](/lightweight-charts/docs/next/api/interfaces/IRange)<`number`>

The current visible range of items on the chart.

---

### conflationFactor[​](#conflationfactor "Direct link to conflationFactor")

> **conflationFactor**: `number`

Current conflation factor. The value represents how many data points have been combined
to form this conflated data point. This can be used to calculate the effective bar spacing
until the next data point. `effectiveBarSpacing = conflationFactor * barSpacing`. If you
are rendering a non-continuous series (like a Candlestick instead of Line) then you likely
would want to use the effectiveBarSpacing value for your width calculations.