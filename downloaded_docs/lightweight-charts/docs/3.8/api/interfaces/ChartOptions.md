Version: 3.8

On this page

Structure describing options of the chart. Series options are to be set separately

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

### watermark[​](#watermark "Direct link to watermark")

> **watermark**: [`WatermarkOptions`](/lightweight-charts/docs/3.8/api/interfaces/WatermarkOptions)

Watermark options.

A watermark is a background label that includes a brief description of the drawn data. Any text can be added to it.

Please make sure you enable it and set an appropriate font color and size to make your watermark visible in the background of the chart.
We recommend a semi-transparent color and a large font. Also note that watermark position can be aligned vertically and horizontally.

---

### layout[​](#layout "Direct link to layout")

> **layout**: [`LayoutOptions`](/lightweight-charts/docs/3.8/api/interfaces/LayoutOptions)

Layout options

---

### leftPriceScale[​](#leftpricescale "Direct link to leftPriceScale")

> **leftPriceScale**: [`PriceScaleOptions`](/lightweight-charts/docs/3.8/api/interfaces/PriceScaleOptions)

Left price scale options

---

### rightPriceScale[​](#rightpricescale "Direct link to rightPriceScale")

> **rightPriceScale**: [`PriceScaleOptions`](/lightweight-charts/docs/3.8/api/interfaces/PriceScaleOptions)

Right price scale options

---

### overlayPriceScales[​](#overlaypricescales "Direct link to overlayPriceScales")

> **overlayPriceScales**: [`OverlayPriceScaleOptions`](/lightweight-charts/docs/3.8/api/type-aliases/OverlayPriceScaleOptions)

Overlay price scale options

---

### timeScale[​](#timescale "Direct link to timeScale")

> **timeScale**: [`TimeScaleOptions`](/lightweight-charts/docs/3.8/api/interfaces/TimeScaleOptions)

Time scale options

---

### crosshair[​](#crosshair "Direct link to crosshair")

> **crosshair**: [`CrosshairOptions`](/lightweight-charts/docs/3.8/api/interfaces/CrosshairOptions)

The crosshair shows the intersection of the price and time scale values at any point on the chart.

---

### grid[​](#grid "Direct link to grid")

> **grid**: [`GridOptions`](/lightweight-charts/docs/3.8/api/interfaces/GridOptions)

A grid is represented in the chart background as a vertical and horizontal lines drawn at the levels of visible marks of price and the time scales.

---

### localization[​](#localization "Direct link to localization")

> **localization**: [`LocalizationOptions`](/lightweight-charts/docs/3.8/api/interfaces/LocalizationOptions)

Localization options.

---

### handleScroll[​](#handlescroll "Direct link to handleScroll")

> **handleScroll**: `boolean` | [`HandleScrollOptions`](/lightweight-charts/docs/3.8/api/interfaces/HandleScrollOptions)

Scroll options, or a boolean flag that enables/disables scrolling

---

### handleScale[​](#handlescale "Direct link to handleScale")

> **handleScale**: `boolean` | [`HandleScaleOptions`](/lightweight-charts/docs/3.8/api/interfaces/HandleScaleOptions)

Scale options, or a boolean flag that enables/disables scaling

---

### kineticScroll[​](#kineticscroll "Direct link to kineticScroll")

> **kineticScroll**: [`KineticScrollOptions`](/lightweight-charts/docs/3.8/api/interfaces/KineticScrollOptions)

Kinetic scroll options

---

### trackingMode[​](#trackingmode "Direct link to trackingMode")

> **trackingMode**: [`TrackingModeOptions`](/lightweight-charts/docs/3.8/api/interfaces/TrackingModeOptions)

Represent options for the tracking mode's behavior.

Mobile users will not have the ability to see the values/dates like they do on desktop.
To see it, they should enter the tracking mode. The tracking mode will deactivate the scrolling
and make it possible to check values and dates.