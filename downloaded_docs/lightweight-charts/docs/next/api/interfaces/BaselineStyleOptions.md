Version: Next

On this page

Represents style options for a baseline series.

## Properties[​](#properties "Direct link to Properties")

### baseValue[​](#basevalue "Direct link to baseValue")

> **baseValue**: [`BaseValuePrice`](/lightweight-charts/docs/next/api/interfaces/BaseValuePrice)

Base value of the series.

#### Default Value[​](#default-value "Direct link to Default Value")

`{ type: 'price', price: 0 }`

---

### relativeGradient[​](#relativegradient "Direct link to relativeGradient")

> **relativeGradient**: `boolean`

Gradient is relative to the base value and the currently visible range.
If it is false, the gradient is relative to the top and bottom of the chart.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`false`

---

### topFillColor1[​](#topfillcolor1 "Direct link to topFillColor1")

> **topFillColor1**: `string`

The first color of the top area.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`'rgba(38, 166, 154, 0.28)'`

---

### topFillColor2[​](#topfillcolor2 "Direct link to topFillColor2")

> **topFillColor2**: `string`

The second color of the top area.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`'rgba(38, 166, 154, 0.05)'`

---

### topLineColor[​](#toplinecolor "Direct link to topLineColor")

> **topLineColor**: `string`

The line color of the top area.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`'rgba(38, 166, 154, 1)'`

---

### bottomFillColor1[​](#bottomfillcolor1 "Direct link to bottomFillColor1")

> **bottomFillColor1**: `string`

The first color of the bottom area.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`'rgba(239, 83, 80, 0.05)'`

---

### bottomFillColor2[​](#bottomfillcolor2 "Direct link to bottomFillColor2")

> **bottomFillColor2**: `string`

The second color of the bottom area.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`'rgba(239, 83, 80, 0.28)'`

---

### bottomLineColor[​](#bottomlinecolor "Direct link to bottomLineColor")

> **bottomLineColor**: `string`

The line color of the bottom area.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`'rgba(239, 83, 80, 1)'`

---

### lineWidth[​](#linewidth "Direct link to lineWidth")

> **lineWidth**: [`LineWidth`](/lightweight-charts/docs/next/api/type-aliases/LineWidth)

Line width.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`3`

---

### lineStyle[​](#linestyle "Direct link to lineStyle")

> **lineStyle**: [`LineStyle`](/lightweight-charts/docs/next/api/enumerations/LineStyle)

Line style.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

```prism-code
{@link LineStyle.Solid}
```

---

### lineType[​](#linetype "Direct link to lineType")

> **lineType**: [`LineType`](/lightweight-charts/docs/next/api/enumerations/LineType)

Line type.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

```prism-code
{@link LineType.Simple}
```

---

### lineVisible[​](#linevisible "Direct link to lineVisible")

> **lineVisible**: `boolean`

Show series line.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`true`

---

### pointMarkersVisible[​](#pointmarkersvisible "Direct link to pointMarkersVisible")

> **pointMarkersVisible**: `boolean`

Show circle markers on each point.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`false`

---

### pointMarkersRadius?[​](#pointmarkersradius "Direct link to pointMarkersRadius?")

> `optional` **pointMarkersRadius**: `number`

Circle markers radius in pixels.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

`undefined`

---

### crosshairMarkerVisible[​](#crosshairmarkervisible "Direct link to crosshairMarkerVisible")

> **crosshairMarkerVisible**: `boolean`

Show the crosshair marker.

#### Default Value[​](#default-value-14 "Direct link to Default Value")

`true`

---

### crosshairMarkerRadius[​](#crosshairmarkerradius "Direct link to crosshairMarkerRadius")

> **crosshairMarkerRadius**: `number`

Crosshair marker radius in pixels.

#### Default Value[​](#default-value-15 "Direct link to Default Value")

`4`

---

### crosshairMarkerBorderColor[​](#crosshairmarkerbordercolor "Direct link to crosshairMarkerBorderColor")

> **crosshairMarkerBorderColor**: `string`

Crosshair marker border color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](#default-value-16 "Direct link to Default Value")

`''`

---

### crosshairMarkerBackgroundColor[​](#crosshairmarkerbackgroundcolor "Direct link to crosshairMarkerBackgroundColor")

> **crosshairMarkerBackgroundColor**: `string`

The crosshair marker background color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](#default-value-17 "Direct link to Default Value")

`''`

---

### crosshairMarkerBorderWidth[​](#crosshairmarkerborderwidth "Direct link to crosshairMarkerBorderWidth")

> **crosshairMarkerBorderWidth**: `number`

Crosshair marker border width in pixels.

#### Default Value[​](#default-value-18 "Direct link to Default Value")

`2`

---

### lastPriceAnimation[​](#lastpriceanimation "Direct link to lastPriceAnimation")

> **lastPriceAnimation**: [`LastPriceAnimationMode`](/lightweight-charts/docs/next/api/enumerations/LastPriceAnimationMode)

Last price animation mode.

#### Default Value[​](#default-value-19 "Direct link to Default Value")

```prism-code
{@link LastPriceAnimationMode.Disabled}
```