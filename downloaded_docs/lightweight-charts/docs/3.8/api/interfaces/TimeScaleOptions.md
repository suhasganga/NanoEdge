Version: 3.8

On this page

Options for the time scale; the horizontal scale at the bottom of the chart that displays the time of data.

## Properties[​](#properties "Direct link to Properties")

### rightOffset[​](#rightoffset "Direct link to rightOffset")

> **rightOffset**: `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](#default-value "Direct link to Default Value")

`0`

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

The space between bars in pixels.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`6`

---

### minBarSpacing[​](#minbarspacing "Direct link to minBarSpacing")

> **minBarSpacing**: `number`

The minimum space between bars in pixels.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`0.5`

---

### fixLeftEdge[​](#fixleftedge "Direct link to fixLeftEdge")

> **fixLeftEdge**: `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`false`

---

### fixRightEdge[​](#fixrightedge "Direct link to fixRightEdge")

> **fixRightEdge**: `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`false`

---

### lockVisibleTimeRangeOnResize[​](#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize")

> **lockVisibleTimeRangeOnResize**: `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`false`

---

### rightBarStaysOnScroll[​](#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll")

> **rightBarStaysOnScroll**: `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`false`

---

### borderVisible[​](#bordervisible "Direct link to borderVisible")

> **borderVisible**: `boolean`

Show the time scale border.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`true`

---

### borderColor[​](#bordercolor "Direct link to borderColor")

> **borderColor**: `string`

The time scale border color.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`'#2B2B43'`

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Show the time scale.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`true`

---

### timeVisible[​](#timevisible "Direct link to timeVisible")

> **timeVisible**: `boolean`

Show the time, not just the date, in the time scale and vertical crosshair label.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

`false`

---

### secondsVisible[​](#secondsvisible "Direct link to secondsVisible")

> **secondsVisible**: `boolean`

Show seconds in the time scale and vertical crosshair label in `hh:mm:ss` format for intraday data.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`true`

---

### shiftVisibleRangeOnNewBar[​](#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar")

> **shiftVisibleRangeOnNewBar**: `boolean`

Shift the visible range to the right (into the future) by the number of new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`true`

---

### tickMarkFormatter?[​](#tickmarkformatter "Direct link to tickMarkFormatter?")

> `optional` **tickMarkFormatter**: [`TickMarkFormatter`](/lightweight-charts/docs/3.8/api/type-aliases/TickMarkFormatter)

Tick marks formatter can be used to customize tick marks labels on the time axis.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

`undefined`