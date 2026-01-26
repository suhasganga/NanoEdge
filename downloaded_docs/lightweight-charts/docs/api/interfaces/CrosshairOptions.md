Version: 5.1

On this page

Structure describing crosshair options

## Properties[​](#properties "Direct link to Properties")

### mode[​](#mode "Direct link to mode")

> **mode**: [`CrosshairMode`](/lightweight-charts/docs/api/enumerations/CrosshairMode)

Crosshair mode

#### Default Value[​](#default-value "Direct link to Default Value")

```prism-code
{@link CrosshairMode.Magnet}
```

---

### vertLine[​](#vertline "Direct link to vertLine")

> **vertLine**: [`CrosshairLineOptions`](/lightweight-charts/docs/api/interfaces/CrosshairLineOptions)

Vertical line options.

---

### horzLine[​](#horzline "Direct link to horzLine")

> **horzLine**: [`CrosshairLineOptions`](/lightweight-charts/docs/api/interfaces/CrosshairLineOptions)

Horizontal line options.

---

### doNotSnapToHiddenSeriesIndices[​](#donotsnaptohiddenseriesindices "Direct link to doNotSnapToHiddenSeriesIndices")

> **doNotSnapToHiddenSeriesIndices**: `boolean`

If set to `true`, the crosshair will not snap to the data points of hidden series.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`false`