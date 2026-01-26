Version: 5.1

On this page

Extended time scale options for time-based horizontal scale

## Extends[​](#extends "Direct link to Extends")

* [`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions)

## Properties[​](#properties "Direct link to Properties")

### rightOffset[​](#rightoffset "Direct link to rightOffset")

> **rightOffset**: `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](#default-value "Direct link to Default Value")

`0`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`rightOffset`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#rightoffset)

---

### rightOffsetPixels?[​](#rightoffsetpixels "Direct link to rightOffsetPixels?")

> `optional` **rightOffsetPixels**: `number`

The margin space in pixels from the right side of the chart.
This option has priority over `rightOffset`.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`rightOffsetPixels`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#rightoffsetpixels)

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

The space between bars in pixels.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`6`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`barSpacing`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#barspacing)

---

### minBarSpacing[​](#minbarspacing "Direct link to minBarSpacing")

> **minBarSpacing**: `number`

The minimum space between bars in pixels.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`0.5`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`minBarSpacing`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#minbarspacing)

---

### maxBarSpacing[​](#maxbarspacing "Direct link to maxBarSpacing")

> **maxBarSpacing**: `number`

The maximum space between bars in pixels.

Has no effect if value is set to `0`.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`0`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`maxBarSpacing`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#maxbarspacing)

---

### fixLeftEdge[​](#fixleftedge "Direct link to fixLeftEdge")

> **fixLeftEdge**: `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`fixLeftEdge`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#fixleftedge)

---

### fixRightEdge[​](#fixrightedge "Direct link to fixRightEdge")

> **fixRightEdge**: `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`fixRightEdge`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#fixrightedge)

---

### lockVisibleTimeRangeOnResize[​](#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize")

> **lockVisibleTimeRangeOnResize**: `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`lockVisibleTimeRangeOnResize`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#lockvisibletimerangeonresize)

---

### rightBarStaysOnScroll[​](#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll")

> **rightBarStaysOnScroll**: `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`rightBarStaysOnScroll`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#rightbarstaysonscroll)

---

### borderVisible[​](#bordervisible "Direct link to borderVisible")

> **borderVisible**: `boolean`

Show the time scale border.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`borderVisible`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#bordervisible)

---

### borderColor[​](#bordercolor "Direct link to borderColor")

> **borderColor**: `string`

The time scale border color.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

`'#2B2B43'`

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`borderColor`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#bordercolor)

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Show the time scale.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`visible`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#visible)

---

### timeVisible[​](#timevisible "Direct link to timeVisible")

> **timeVisible**: `boolean`

Show the time, not just the date, in the time scale and vertical crosshair label.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`timeVisible`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#timevisible)

---

### secondsVisible[​](#secondsvisible "Direct link to secondsVisible")

> **secondsVisible**: `boolean`

Show seconds in the time scale and vertical crosshair label in `hh:mm:ss` format for intraday data.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`secondsVisible`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#secondsvisible)

---

### shiftVisibleRangeOnNewBar[​](#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar")

> **shiftVisibleRangeOnNewBar**: `boolean`

Shift the visible range to the right (into the future) by the number of new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](#default-value-14 "Direct link to Default Value")

`true`

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`shiftVisibleRangeOnNewBar`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#shiftvisiblerangeonnewbar)

---

### allowShiftVisibleRangeOnWhitespaceReplacement[​](#allowshiftvisiblerangeonwhitespacereplacement "Direct link to allowShiftVisibleRangeOnWhitespaceReplacement")

> **allowShiftVisibleRangeOnWhitespaceReplacement**: `boolean`

Allow the visible range to be shifted to the right when a new bar is added which
is replacing an existing whitespace time point on the chart.

Note that this only applies when the last bar is visible & `shiftVisibleRangeOnNewBar` is enabled.

#### Default Value[​](#default-value-15 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`allowShiftVisibleRangeOnWhitespaceReplacement`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#allowshiftvisiblerangeonwhitespacereplacement)

---

### ticksVisible[​](#ticksvisible "Direct link to ticksVisible")

> **ticksVisible**: `boolean`

Draw small vertical line on time axis labels.

#### Default Value[​](#default-value-16 "Direct link to Default Value")

`false`

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`ticksVisible`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#ticksvisible)

---

### tickMarkMaxCharacterLength?[​](#tickmarkmaxcharacterlength "Direct link to tickMarkMaxCharacterLength?")

> `optional` **tickMarkMaxCharacterLength**: `number`

Maximum tick mark label length. Used to override the default 8 character maximum length.

#### Default Value[​](#default-value-17 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`tickMarkMaxCharacterLength`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#tickmarkmaxcharacterlength)

---

### uniformDistribution[​](#uniformdistribution "Direct link to uniformDistribution")

> **uniformDistribution**: `boolean`

Changes horizontal scale marks generation.
With this flag equal to `true`, marks of the same weight are either all drawn or none are drawn at all.

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`uniformDistribution`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#uniformdistribution)

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

#### Default Value[​](#default-value-18 "Direct link to Default Value")

```prism-code
0
```

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`minimumHeight`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#minimumheight)

---

### allowBoldLabels[​](#allowboldlabels "Direct link to allowBoldLabels")

> **allowBoldLabels**: `boolean`

Allow major time scale labels to be rendered in a bolder font weight.

#### Default Value[​](#default-value-19 "Direct link to Default Value")

```prism-code
true
```

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`allowBoldLabels`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#allowboldlabels)

---

### ignoreWhitespaceIndices[​](#ignorewhitespaceindices "Direct link to ignoreWhitespaceIndices")

> **ignoreWhitespaceIndices**: `boolean`

Ignore time scale points containing only whitespace (for all series) when
drawing grid lines, tick marks, and snapping the crosshair to time scale points.

For the yield curve chart type it defaults to `true`.

#### Default Value[​](#default-value-20 "Direct link to Default Value")

```prism-code
false
```

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`ignoreWhitespaceIndices`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#ignorewhitespaceindices)

---

### enableConflation[​](#enableconflation "Direct link to enableConflation")

> **enableConflation**: `boolean`

Enable data conflation for performance optimization when bar spacing is very small.
When enabled, multiple data points are automatically combined into single points
when they would be rendered in less than 0.5 pixels of screen space.
This significantly improves rendering performance for large datasets when zoomed out.

#### Default Value[​](#default-value-21 "Direct link to Default Value")

```prism-code
false
```

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`enableConflation`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#enableconflation)

---

### conflationThresholdFactor?[​](#conflationthresholdfactor "Direct link to conflationThresholdFactor?")

> `optional` **conflationThresholdFactor**: `number`

Smoothing factor for conflation thresholds. Controls how aggressively conflation is applied.
This can be used to create smoother-looking charts, especially useful for sparklines and small charts.

* 1.0 = conflate only when display can't show detail (default, performance-focused)
* 2.0 = conflate at 2x the display threshold (moderate smoothing)
* 4.0 = conflate at 4x the display threshold (strong smoothing)
* 8.0+ = very aggressive smoothing for very small charts

Higher values result in fewer data points being displayed, creating smoother but less detailed charts.
This is particularly useful for sparklines and small charts where smooth appearance is prioritized over showing every data point.

Note: Should be used with continuous series types (line, area, baseline) for best visual results.
Candlestick and bar series may look less natural with high smoothing factors.

#### Default Value[​](#default-value-22 "Direct link to Default Value")

```prism-code
1.0
```

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`conflationThresholdFactor`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#conflationthresholdfactor)

---

### precomputeConflationOnInit[​](#precomputeconflationoninit "Direct link to precomputeConflationOnInit")

> **precomputeConflationOnInit**: `boolean`

Precompute conflation chunks for common levels right after data load.
When enabled, the system will precompute conflation data in the background,
which improves performance when zooming out but increases initial load time
and memory usage.

Performance impact:

* Initial load: +100-500ms depending on dataset size
* Memory usage: +20-50% of original dataset size
* Zoom performance: Significant improvement (10-100x faster)

Recommended for: Large datasets (>10K points) on machines with sufficient memory

#### Default Value[​](#default-value-23 "Direct link to Default Value")

```prism-code
false
```

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`precomputeConflationOnInit`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#precomputeconflationoninit)

---

### precomputeConflationPriority[​](#precomputeconflationpriority "Direct link to precomputeConflationPriority")

> **precomputeConflationPriority**: `"background"` | `"user-visible"` | `"user-blocking"`

Priority used for background precompute tasks when the Prioritized Task Scheduling API is available.

Options:

* 'background': Lowest priority, tasks run only when the browser is idle
* 'user-visible': Medium priority, tasks run when they might affect visible content
* 'user-blocking': Highest priority, tasks run immediately and may block user interaction

Recommendation: Use 'background' for most cases to avoid impacting user experience.
Only use higher priorities if conflation is critical for your application's functionality.

#### Default Value[​](#default-value-24 "Direct link to Default Value")

```prism-code
'background'
```

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[`HorzScaleOptions`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions) . [`precomputeConflationPriority`](/lightweight-charts/docs/api/interfaces/HorzScaleOptions#precomputeconflationpriority)

---

### tickMarkFormatter?[​](#tickmarkformatter "Direct link to tickMarkFormatter?")

> `optional` **tickMarkFormatter**: [`TickMarkFormatter`](/lightweight-charts/docs/api/type-aliases/TickMarkFormatter)

Tick marks formatter can be used to customize tick marks labels on the time axis.

#### Default Value[​](#default-value-25 "Direct link to Default Value")

`undefined`