Version: 5.1

On this page

Options for the time scale; the horizontal scale at the bottom of the chart that displays the time of data.

## Extended by[​](#extended-by "Direct link to Extended by")

* [`TimeScaleOptions`](/lightweight-charts/docs/api/interfaces/TimeScaleOptions)

## Properties[​](#properties "Direct link to Properties")

### rightOffset[​](#rightoffset "Direct link to rightOffset")

> **rightOffset**: `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](#default-value "Direct link to Default Value")

`0`

---

### rightOffsetPixels?[​](#rightoffsetpixels "Direct link to rightOffsetPixels?")

> `optional` **rightOffsetPixels**: `number`

The margin space in pixels from the right side of the chart.
This option has priority over `rightOffset`.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`undefined`

---

### barSpacing[​](#barspacing "Direct link to barSpacing")

> **barSpacing**: `number`

The space between bars in pixels.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`6`

---

### minBarSpacing[​](#minbarspacing "Direct link to minBarSpacing")

> **minBarSpacing**: `number`

The minimum space between bars in pixels.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`0.5`

---

### maxBarSpacing[​](#maxbarspacing "Direct link to maxBarSpacing")

> **maxBarSpacing**: `number`

The maximum space between bars in pixels.

Has no effect if value is set to `0`.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`0`

---

### fixLeftEdge[​](#fixleftedge "Direct link to fixLeftEdge")

> **fixLeftEdge**: `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`false`

---

### fixRightEdge[​](#fixrightedge "Direct link to fixRightEdge")

> **fixRightEdge**: `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`false`

---

### lockVisibleTimeRangeOnResize[​](#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize")

> **lockVisibleTimeRangeOnResize**: `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`false`

---

### rightBarStaysOnScroll[​](#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll")

> **rightBarStaysOnScroll**: `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`false`

---

### borderVisible[​](#bordervisible "Direct link to borderVisible")

> **borderVisible**: `boolean`

Show the time scale border.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`true`

---

### borderColor[​](#bordercolor "Direct link to borderColor")

> **borderColor**: `string`

The time scale border color.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

`'#2B2B43'`

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Show the time scale.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`true`

---

### timeVisible[​](#timevisible "Direct link to timeVisible")

> **timeVisible**: `boolean`

Show the time, not just the date, in the time scale and vertical crosshair label.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`false`

---

### secondsVisible[​](#secondsvisible "Direct link to secondsVisible")

> **secondsVisible**: `boolean`

Show seconds in the time scale and vertical crosshair label in `hh:mm:ss` format for intraday data.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

`true`

---

### shiftVisibleRangeOnNewBar[​](#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar")

> **shiftVisibleRangeOnNewBar**: `boolean`

Shift the visible range to the right (into the future) by the number of new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](#default-value-14 "Direct link to Default Value")

`true`

---

### allowShiftVisibleRangeOnWhitespaceReplacement[​](#allowshiftvisiblerangeonwhitespacereplacement "Direct link to allowShiftVisibleRangeOnWhitespaceReplacement")

> **allowShiftVisibleRangeOnWhitespaceReplacement**: `boolean`

Allow the visible range to be shifted to the right when a new bar is added which
is replacing an existing whitespace time point on the chart.

Note that this only applies when the last bar is visible & `shiftVisibleRangeOnNewBar` is enabled.

#### Default Value[​](#default-value-15 "Direct link to Default Value")

`false`

---

### ticksVisible[​](#ticksvisible "Direct link to ticksVisible")

> **ticksVisible**: `boolean`

Draw small vertical line on time axis labels.

#### Default Value[​](#default-value-16 "Direct link to Default Value")

`false`

---

### tickMarkMaxCharacterLength?[​](#tickmarkmaxcharacterlength "Direct link to tickMarkMaxCharacterLength?")

> `optional` **tickMarkMaxCharacterLength**: `number`

Maximum tick mark label length. Used to override the default 8 character maximum length.

#### Default Value[​](#default-value-17 "Direct link to Default Value")

`undefined`

---

### uniformDistribution[​](#uniformdistribution "Direct link to uniformDistribution")

> **uniformDistribution**: `boolean`

Changes horizontal scale marks generation.
With this flag equal to `true`, marks of the same weight are either all drawn or none are drawn at all.

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

---

### allowBoldLabels[​](#allowboldlabels "Direct link to allowBoldLabels")

> **allowBoldLabels**: `boolean`

Allow major time scale labels to be rendered in a bolder font weight.

#### Default Value[​](#default-value-19 "Direct link to Default Value")

```prism-code
true
```

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