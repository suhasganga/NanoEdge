Version: 5.0

On this page

Represents common chart options

## Extended by[​](#extended-by "Direct link to Extended by")

* [`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl)

## Properties[​](#properties "Direct link to Properties")

### width[​](#width "Direct link to width")

> **width**: `number`

Width of the chart in pixels

#### Default Value[​](#default-value "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

---

### height[​](#height "Direct link to height")

> **height**: `number`

Height of the chart in pixels

#### Default Value[​](#default-value-1 "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

---

### autoSize[​](#autosize "Direct link to autoSize")

> **autoSize**: `boolean`

Setting this flag to `true` will make the chart watch the chart container's size and automatically resize the chart to fit its container whenever the size changes.

This feature requires [`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) class to be available in the global scope.
Note that calling code is responsible for providing a polyfill if required. If the global scope does not have `ResizeObserver`, a warning will appear and the flag will be ignored.

Please pay attention that `autoSize` option and explicit sizes options `width` and `height` don't conflict with one another.
If you specify `autoSize` flag, then `width` and `height` options will be ignored unless `ResizeObserver` has failed. If it fails then the values will be used as fallback.

The flag `autoSize` could also be set with and unset with `applyOptions` function.

```prism-code
const chart = LightweightCharts.createChart(document.body, {  
    autoSize: true,  
});
```

---

### layout[​](#layout "Direct link to layout")

> **layout**: [`LayoutOptions`](/lightweight-charts/docs/5.0/api/interfaces/LayoutOptions)

Layout options

---

### leftPriceScale[​](#leftpricescale "Direct link to leftPriceScale")

> **leftPriceScale**: [`PriceScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/PriceScaleOptions)

Left price scale options

---

### rightPriceScale[​](#rightpricescale "Direct link to rightPriceScale")

> **rightPriceScale**: [`PriceScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/PriceScaleOptions)

Right price scale options

---

### overlayPriceScales[​](#overlaypricescales "Direct link to overlayPriceScales")

> **overlayPriceScales**: [`OverlayPriceScaleOptions`](/lightweight-charts/docs/5.0/api/type-aliases/OverlayPriceScaleOptions)

Overlay price scale options

---

### timeScale[​](#timescale "Direct link to timeScale")

> **timeScale**: [`HorzScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/HorzScaleOptions)

Time scale options

---

### crosshair[​](#crosshair "Direct link to crosshair")

> **crosshair**: [`CrosshairOptions`](/lightweight-charts/docs/5.0/api/interfaces/CrosshairOptions)

The crosshair shows the intersection of the price and time scale values at any point on the chart.

---

### grid[​](#grid "Direct link to grid")

> **grid**: [`GridOptions`](/lightweight-charts/docs/5.0/api/interfaces/GridOptions)

A grid is represented in the chart background as a vertical and horizontal lines drawn at the levels of visible marks of price and the time scales.

---

### handleScroll[​](#handlescroll "Direct link to handleScroll")

> **handleScroll**: `boolean` | [`HandleScrollOptions`](/lightweight-charts/docs/5.0/api/interfaces/HandleScrollOptions)

Scroll options, or a boolean flag that enables/disables scrolling

---

### handleScale[​](#handlescale "Direct link to handleScale")

> **handleScale**: `boolean` | [`HandleScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/HandleScaleOptions)

Scale options, or a boolean flag that enables/disables scaling

---

### kineticScroll[​](#kineticscroll "Direct link to kineticScroll")

> **kineticScroll**: [`KineticScrollOptions`](/lightweight-charts/docs/5.0/api/interfaces/KineticScrollOptions)

Kinetic scroll options

---

### trackingMode[​](#trackingmode "Direct link to trackingMode")

> **trackingMode**: [`TrackingModeOptions`](/lightweight-charts/docs/5.0/api/interfaces/TrackingModeOptions)

Represent options for the tracking mode's behavior.

Mobile users will not have the ability to see the values/dates like they do on desktop.
To see it, they should enter the tracking mode. The tracking mode will deactivate the scrolling
and make it possible to check values and dates.

---

### localization[​](#localization "Direct link to localization")

> **localization**: [`LocalizationOptionsBase`](/lightweight-charts/docs/5.0/api/interfaces/LocalizationOptionsBase)

Basic localization options

---

### addDefaultPane[​](#adddefaultpane "Direct link to addDefaultPane")

> **addDefaultPane**: `boolean`

Whether to add a default pane to the chart
Disable this option when you want to create a chart with no panes and add them manually

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`true`