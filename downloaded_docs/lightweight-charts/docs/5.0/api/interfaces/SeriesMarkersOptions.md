Version: 5.0

On this page

Configuration options for the series markers plugin.
These options affect all markers managed by the plugin.

## Properties[​](#properties "Direct link to Properties")

### autoScale[​](#autoscale "Direct link to autoScale")

> **autoScale**: `boolean`

Specifies whether the auto-scaling calculation should expand to include the size of markers.

When `true`, the auto-scale feature will adjust the price scale's range to ensure
series markers are fully visible and not cropped by the chart's edges.

When `false`, the scale will only fit the series data points, which may cause
markers to be partially hidden.

Note: This option only has an effect when auto-scaling is enabled for the price scale.

#### Default Value[​](#default-value "Direct link to Default Value")

`true`

---

### zOrder[​](#zorder "Direct link to zOrder")

> **zOrder**: [`SeriesMarkerZOrder`](/lightweight-charts/docs/5.0/api/type-aliases/SeriesMarkerZOrder)

Defines the stacking order of the markers relative to the series and other primitives.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`normal`