Version: 4.0

On this page

Structure describing a crosshair line (vertical or horizontal)

## Properties[​](#properties "Direct link to Properties")

### color[​](#color "Direct link to color")

> **color**: `string`

Crosshair line color.

#### Default Value[​](#default-value "Direct link to Default Value")

`'#758696'`

---

### width[​](#width "Direct link to width")

> **width**: [`LineWidth`](/lightweight-charts/docs/4.0/api/type-aliases/LineWidth)

Crosshair line width.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`1`

---

### style[​](#style "Direct link to style")

> **style**: [`LineStyle`](/lightweight-charts/docs/4.0/api/enumerations/LineStyle)

Crosshair line style.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

```prism-code
{@link LineStyle.LargeDashed}
```

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Display the crosshair line.

Note that disabling crosshair lines does not disable crosshair marker on Line and Area series.
It can be disabled by using `crosshairMarkerVisible` option of a relevant series.

#### See[​](#see "Direct link to See")

* [LineStyleOptions.crosshairMarkerVisible](/lightweight-charts/docs/4.0/api/interfaces/LineStyleOptions#crosshairmarkervisible)
* [AreaStyleOptions.crosshairMarkerVisible](/lightweight-charts/docs/4.0/api/interfaces/AreaStyleOptions#crosshairmarkervisible)
* [BaselineStyleOptions.crosshairMarkerVisible](/lightweight-charts/docs/4.0/api/interfaces/BaselineStyleOptions#crosshairmarkervisible)

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`true`

---

### labelVisible[​](#labelvisible "Direct link to labelVisible")

> **labelVisible**: `boolean`

Display the crosshair label on the relevant scale.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`true`

---

### labelBackgroundColor[​](#labelbackgroundcolor "Direct link to labelBackgroundColor")

> **labelBackgroundColor**: `string`

Crosshair label background color.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`'#4c525e'`