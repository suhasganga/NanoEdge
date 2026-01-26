Version: 4.1

On this page

Extended time scale options for time-based horizontal scale

## Extends[​](#extends "Direct link to Extends")

* [`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions)

## Properties[​](#properties "Direct link to Properties")

### rightOffset[​](#rightoffset "Direct link to rightOffset")

> **rightOffset**: `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](#default-value "Direct link to Default Value")

`0`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`rightOffset`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#rightoffset)

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

The space between bars in pixels.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`6`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`barSpacing`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#barspacing)

---

### minBarSpacing[​](#minbarspacing "Direct link to minBarSpacing")

> **minBarSpacing**: `number`

The minimum space between bars in pixels.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`0.5`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`minBarSpacing`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#minbarspacing)

---

### fixLeftEdge[​](#fixleftedge "Direct link to fixLeftEdge")

> **fixLeftEdge**: `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`fixLeftEdge`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#fixleftedge)

---

### fixRightEdge[​](#fixrightedge "Direct link to fixRightEdge")

> **fixRightEdge**: `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`fixRightEdge`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#fixrightedge)

---

### lockVisibleTimeRangeOnResize[​](#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize")

> **lockVisibleTimeRangeOnResize**: `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`lockVisibleTimeRangeOnResize`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#lockvisibletimerangeonresize)

---

### rightBarStaysOnScroll[​](#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll")

> **rightBarStaysOnScroll**: `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`rightBarStaysOnScroll`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#rightbarstaysonscroll)

---

### borderVisible[​](#bordervisible "Direct link to borderVisible")

> **borderVisible**: `boolean`

Show the time scale border.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`borderVisible`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#bordervisible)

---

### borderColor[​](#bordercolor "Direct link to borderColor")

> **borderColor**: `string`

The time scale border color.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`'#2B2B43'`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`borderColor`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#bordercolor)

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Show the time scale.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`visible`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#visible)

---

### timeVisible[​](#timevisible "Direct link to timeVisible")

> **timeVisible**: `boolean`

Show the time, not just the date, in the time scale and vertical crosshair label.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`timeVisible`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#timevisible)

---

### secondsVisible[​](#secondsvisible "Direct link to secondsVisible")

> **secondsVisible**: `boolean`

Show seconds in the time scale and vertical crosshair label in `hh:mm:ss` format for intraday data.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`secondsVisible`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#secondsvisible)

---

### shiftVisibleRangeOnNewBar[​](#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar")

> **shiftVisibleRangeOnNewBar**: `boolean`

Shift the visible range to the right (into the future) by the number of new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`shiftVisibleRangeOnNewBar`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#shiftvisiblerangeonnewbar)

---

### allowShiftVisibleRangeOnWhitespaceReplacement[​](#allowshiftvisiblerangeonwhitespacereplacement "Direct link to allowShiftVisibleRangeOnWhitespaceReplacement")

> **allowShiftVisibleRangeOnWhitespaceReplacement**: `boolean`

Allow the visible range to be shifted to the right when a new bar is added which
is replacing an existing whitespace time point on the chart.

Note that this only applies when the last bar is visible & `shiftVisibleRangeOnNewBar` is enabled.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`allowShiftVisibleRangeOnWhitespaceReplacement`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#allowshiftvisiblerangeonwhitespacereplacement)

---

### ticksVisible[​](#ticksvisible "Direct link to ticksVisible")

> **ticksVisible**: `boolean`

Draw small vertical line on time axis labels.

#### Default Value[​](#default-value-14 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`ticksVisible`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#ticksvisible)

---

### tickMarkMaxCharacterLength?[​](#tickmarkmaxcharacterlength "Direct link to tickMarkMaxCharacterLength?")

> `optional` **tickMarkMaxCharacterLength**: `number`

Maximum tick mark label length. Used to override the default 8 character maximum length.

#### Default Value[​](#default-value-15 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`tickMarkMaxCharacterLength`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#tickmarkmaxcharacterlength)

---

### uniformDistribution[​](#uniformdistribution "Direct link to uniformDistribution")

> **uniformDistribution**: `boolean`

Changes horizontal scale marks generation.
With this flag equal to `true`, marks of the same weight are either all drawn or none are drawn at all.

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`uniformDistribution`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#uniformdistribution)

---

### minimumHeight[​](#minimumheight "Direct link to minimumHeight")

> **minimumHeight**: `number`

Define a minimum height for the time scale.
Note: This value will be exceeded if the
time scale needs more space to display it's contents.

Setting a minimum height could be useful for ensuring that
multiple charts positioned in a horizontal stack each have
an identical time scale height, or for plugins which
require a bit more space within the time scale pane.

#### Default Value[​](#default-value-16 "Direct link to Default Value")

```prism-code
0
```

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`minimumHeight`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#minimumheight)

---

### allowBoldLabels[​](#allowboldlabels "Direct link to allowBoldLabels")

> **allowBoldLabels**: `boolean`

Allow major time scale labels to be rendered in a bolder font weight.

#### Default Value[​](#default-value-17 "Direct link to Default Value")

```prism-code
true
```

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions) . [`allowBoldLabels`](/lightweight-charts/docs/4.1/api/interfaces/HorzScaleOptions#allowboldlabels)

---

### tickMarkFormatter?[​](#tickmarkformatter "Direct link to tickMarkFormatter?")

> `optional` **tickMarkFormatter**: [`TickMarkFormatter`](/lightweight-charts/docs/4.1/api/type-aliases/TickMarkFormatter)

Tick marks formatter can be used to customize tick marks labels on the time axis.

#### Default Value[​](#default-value-18 "Direct link to Default Value")

`undefined`