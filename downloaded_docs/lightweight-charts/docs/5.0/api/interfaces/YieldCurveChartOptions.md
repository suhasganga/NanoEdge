Version: 5.0

On this page

Extended chart options that include yield curve specific options.
This interface combines the standard chart options with yield curve options.

## Extends[​](#extends "Direct link to Extends")

* [`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl)<`number`>

## Properties[​](#properties "Direct link to Properties")

### width[​](#width "Direct link to width")

> **width**: `number`

Width of the chart in pixels

#### Default Value[​](#default-value "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`width`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#width)

---

### height[​](#height "Direct link to height")

> **height**: `number`

Height of the chart in pixels

#### Default Value[​](#default-value-1 "Direct link to Default Value")

If `0` (default) or none value provided, then a size of the widget will be calculated based its container's size.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`height`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#height)

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

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`autoSize`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#autosize)

---

### layout[​](#layout "Direct link to layout")

> **layout**: [`LayoutOptions`](/lightweight-charts/docs/5.0/api/interfaces/LayoutOptions)

Layout options

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`layout`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#layout)

---

### leftPriceScale[​](#leftpricescale "Direct link to leftPriceScale")

> **leftPriceScale**: [`PriceScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/PriceScaleOptions)

Left price scale options

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`leftPriceScale`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#leftpricescale)

---

### rightPriceScale[​](#rightpricescale "Direct link to rightPriceScale")

> **rightPriceScale**: [`PriceScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/PriceScaleOptions)

Right price scale options

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`rightPriceScale`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#rightpricescale)

---

### overlayPriceScales[​](#overlaypricescales "Direct link to overlayPriceScales")

> **overlayPriceScales**: [`OverlayPriceScaleOptions`](/lightweight-charts/docs/5.0/api/type-aliases/OverlayPriceScaleOptions)

Overlay price scale options

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`overlayPriceScales`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#overlaypricescales)

---

### timeScale[​](#timescale "Direct link to timeScale")

> **timeScale**: [`HorzScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/HorzScaleOptions)

Time scale options

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`timeScale`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#timescale)

---

### crosshair[​](#crosshair "Direct link to crosshair")

> **crosshair**: [`CrosshairOptions`](/lightweight-charts/docs/5.0/api/interfaces/CrosshairOptions)

The crosshair shows the intersection of the price and time scale values at any point on the chart.

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`crosshair`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#crosshair)

---

### grid[​](#grid "Direct link to grid")

> **grid**: [`GridOptions`](/lightweight-charts/docs/5.0/api/interfaces/GridOptions)

A grid is represented in the chart background as a vertical and horizontal lines drawn at the levels of visible marks of price and the time scales.

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`grid`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#grid)

---

### handleScroll[​](#handlescroll "Direct link to handleScroll")

> **handleScroll**: `boolean` | [`HandleScrollOptions`](/lightweight-charts/docs/5.0/api/interfaces/HandleScrollOptions)

Scroll options, or a boolean flag that enables/disables scrolling

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`handleScroll`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#handlescroll)

---

### handleScale[​](#handlescale "Direct link to handleScale")

> **handleScale**: `boolean` | [`HandleScaleOptions`](/lightweight-charts/docs/5.0/api/interfaces/HandleScaleOptions)

Scale options, or a boolean flag that enables/disables scaling

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`handleScale`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#handlescale)

---

### kineticScroll[​](#kineticscroll "Direct link to kineticScroll")

> **kineticScroll**: [`KineticScrollOptions`](/lightweight-charts/docs/5.0/api/interfaces/KineticScrollOptions)

Kinetic scroll options

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`kineticScroll`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#kineticscroll)

---

### trackingMode[​](#trackingmode "Direct link to trackingMode")

> **trackingMode**: [`TrackingModeOptions`](/lightweight-charts/docs/5.0/api/interfaces/TrackingModeOptions)

Represent options for the tracking mode's behavior.

Mobile users will not have the ability to see the values/dates like they do on desktop.
To see it, they should enter the tracking mode. The tracking mode will deactivate the scrolling
and make it possible to check values and dates.

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`trackingMode`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#trackingmode)

---

### addDefaultPane[​](#adddefaultpane "Direct link to addDefaultPane")

> **addDefaultPane**: `boolean`

Whether to add a default pane to the chart
Disable this option when you want to create a chart with no panes and add them manually

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`addDefaultPane`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#adddefaultpane)

---

### localization[​](#localization "Direct link to localization")

> **localization**: [`LocalizationOptions`](/lightweight-charts/docs/5.0/api/interfaces/LocalizationOptions)<`number`>

Localization options.

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[`ChartOptionsImpl`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl) . [`localization`](/lightweight-charts/docs/5.0/api/interfaces/ChartOptionsImpl#localization)

---

### yieldCurve[​](#yieldcurve "Direct link to yieldCurve")

> **yieldCurve**: [`YieldCurveOptions`](/lightweight-charts/docs/5.0/api/interfaces/YieldCurveOptions)

Yield curve specific options.
This object contains all the settings related to how the yield curve is displayed and behaves.