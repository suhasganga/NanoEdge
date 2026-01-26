Version: 4.1

On this page

Represents style options for an area series.

## Properties[​](#properties "Direct link to Properties")

### topColor[​](#topcolor "Direct link to topColor")

> **topColor**: `string`

Color of the top part of the area.

#### Default Value[​](#default-value "Direct link to Default Value")

`'rgba( 46, 220, 135, 0.4)'`

---

### bottomColor[​](#bottomcolor "Direct link to bottomColor")

> **bottomColor**: `string`

Color of the bottom part of the area.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`'rgba( 40, 221, 100, 0)'`

---

### invertFilledArea[​](#invertfilledarea "Direct link to invertFilledArea")

> **invertFilledArea**: `boolean`

Invert the filled area. Fills the area above the line if set to true.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`false`

---

### lineColor[​](#linecolor "Direct link to lineColor")

> **lineColor**: `string`

Line color.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`'#33D778'`

---

### lineStyle[​](#linestyle "Direct link to lineStyle")

> **lineStyle**: [`LineStyle`](/lightweight-charts/docs/4.1/api/enumerations/LineStyle)

Line style.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

```prism-code
{@link LineStyle.Solid}
```

---

### lineWidth[​](#linewidth "Direct link to lineWidth")

> **lineWidth**: [`LineWidth`](/lightweight-charts/docs/4.1/api/type-aliases/LineWidth)

Line width in pixels.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`3`

---

### lineType[​](#linetype "Direct link to lineType")

> **lineType**: [`LineType`](/lightweight-charts/docs/4.1/api/enumerations/LineType)

Line type.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

```prism-code
{@link LineType.Simple}
```

---

### lineVisible[​](#linevisible "Direct link to lineVisible")

> **lineVisible**: `boolean`

Show series line.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`true`

---

### pointMarkersVisible[​](#pointmarkersvisible "Direct link to pointMarkersVisible")

> **pointMarkersVisible**: `boolean`

Show circle markers on each point.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`false`

---

### pointMarkersRadius?[​](#pointmarkersradius "Direct link to pointMarkersRadius?")

> `optional` **pointMarkersRadius**: `number`

Circle markers radius in pixels.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`undefined`

---

### crosshairMarkerVisible[​](#crosshairmarkervisible "Direct link to crosshairMarkerVisible")

> **crosshairMarkerVisible**: `boolean`

Show the crosshair marker.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

`true`

---

### crosshairMarkerRadius[​](#crosshairmarkerradius "Direct link to crosshairMarkerRadius")

> **crosshairMarkerRadius**: `number`

Crosshair marker radius in pixels.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`4`

---

### crosshairMarkerBorderColor[​](#crosshairmarkerbordercolor "Direct link to crosshairMarkerBorderColor")

> **crosshairMarkerBorderColor**: `string`

Crosshair marker border color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`''`

---

### crosshairMarkerBackgroundColor[​](#crosshairmarkerbackgroundcolor "Direct link to crosshairMarkerBackgroundColor")

> **crosshairMarkerBackgroundColor**: `string`

The crosshair marker background color. An empty string falls back to the color of the series under the crosshair.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

`''`

---

### crosshairMarkerBorderWidth[​](#crosshairmarkerborderwidth "Direct link to crosshairMarkerBorderWidth")

> **crosshairMarkerBorderWidth**: `number`

Crosshair marker border width in pixels.

#### Default Value[​](#default-value-14 "Direct link to Default Value")

`2`

---

### lastPriceAnimation[​](#lastpriceanimation "Direct link to lastPriceAnimation")

> **lastPriceAnimation**: [`LastPriceAnimationMode`](/lightweight-charts/docs/4.1/api/enumerations/LastPriceAnimationMode)

Last price animation mode.

#### Default Value[​](#default-value-15 "Direct link to Default Value")

```prism-code
{@link LastPriceAnimationMode.Disabled}
```