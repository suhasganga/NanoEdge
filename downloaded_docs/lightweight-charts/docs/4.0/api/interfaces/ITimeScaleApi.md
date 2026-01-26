Version: 4.0

On this page

Interface to chart time scale

## Methods[​](#methods "Direct link to Methods")

### scrollPosition()[​](#scrollposition "Direct link to scrollPosition()")

> **scrollPosition**(): `number`

Return the distance from the right edge of the time scale to the lastest bar of the series measured in bars.

#### Returns[​](#returns "Direct link to Returns")

`number`

---

### scrollToPosition()[​](#scrolltoposition "Direct link to scrollToPosition()")

> **scrollToPosition**(`position`, `animated`): `void`

Scrolls the chart to the specified position.

#### Parameters[​](#parameters "Direct link to Parameters")

• **position**: `number`

Target data position

• **animated**: `boolean`

Setting this to true makes the chart scrolling smooth and adds animation

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

---

### scrollToRealTime()[​](#scrolltorealtime "Direct link to scrollToRealTime()")

> **scrollToRealTime**(): `void`

Restores default scroll position of the chart. This process is always animated.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

---

### getVisibleRange()[​](#getvisiblerange "Direct link to getVisibleRange()")

> **getVisibleRange**(): [`TimeRange`](/lightweight-charts/docs/4.0/api/type-aliases/TimeRange)

Returns current visible time range of the chart.

Note that this method cannot extrapolate time and will use the only currently existent data.
To get complete information about current visible range, please use [getVisibleLogicalRange](/lightweight-charts/docs/4.0/api/interfaces/ITimeScaleApi#getvisiblelogicalrange) and [ISeriesApi.barsInLogicalRange](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi#barsinlogicalrange).

#### Returns[​](#returns-3 "Direct link to Returns")

[`TimeRange`](/lightweight-charts/docs/4.0/api/type-aliases/TimeRange)

Visible range or null if the chart has no data at all.

---

### setVisibleRange()[​](#setvisiblerange "Direct link to setVisibleRange()")

> **setVisibleRange**(`range`): `void`

Sets visible range of data.

Note that this method cannot extrapolate time and will use the only currently existent data.
Thus, for example, if currently a chart doesn't have data prior `2018-01-01` date and you set visible range with `from` date `2016-01-01`, it will be automatically adjusted to `2018-01-01` (and the same for `to` date).

But if you can approximate indexes on your own - you could use [setVisibleLogicalRange](/lightweight-charts/docs/4.0/api/interfaces/ITimeScaleApi#setvisiblelogicalrange) instead.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **range**: [`TimeRange`](/lightweight-charts/docs/4.0/api/type-aliases/TimeRange)

Target visible range of data.

#### Returns[​](#returns-4 "Direct link to Returns")

`void`

#### Example[​](#example "Direct link to Example")

```prism-code
chart.timeScale().setVisibleRange({  
    from: (new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0))).getTime() / 1000,  
    to: (new Date(Date.UTC(2018, 1, 1, 0, 0, 0, 0))).getTime() / 1000,  
});
```

---

### getVisibleLogicalRange()[​](#getvisiblelogicalrange "Direct link to getVisibleLogicalRange()")

> **getVisibleLogicalRange**(): [`LogicalRange`](/lightweight-charts/docs/4.0/api/type-aliases/LogicalRange)

Returns the current visible [logical range](/lightweight-charts/docs/4.0/time-scale#logical-range) of the chart as an object with the first and last time points of the logical range, or returns `null` if the chart has no data.

#### Returns[​](#returns-5 "Direct link to Returns")

[`LogicalRange`](/lightweight-charts/docs/4.0/api/type-aliases/LogicalRange)

Visible range or null if the chart has no data at all.

---

### setVisibleLogicalRange()[​](#setvisiblelogicalrange "Direct link to setVisibleLogicalRange()")

> **setVisibleLogicalRange**(`range`): `void`

Sets visible [logical range](/lightweight-charts/docs/4.0/time-scale#logical-range) of data.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **range**: [`Range`](/lightweight-charts/docs/4.0/api/interfaces/Range)<`number`>

Target visible logical range of data.

#### Returns[​](#returns-6 "Direct link to Returns")

`void`

#### Example[​](#example-1 "Direct link to Example")

```prism-code
chart.timeScale().setVisibleLogicalRange({ from: 0, to: Date.now() / 1000 });
```

---

### resetTimeScale()[​](#resettimescale "Direct link to resetTimeScale()")

> **resetTimeScale**(): `void`

Restores default zoom level and scroll position of the time scale.

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

---

### fitContent()[​](#fitcontent "Direct link to fitContent()")

> **fitContent**(): `void`

Automatically calculates the visible range to fit all data from all series.

#### Returns[​](#returns-8 "Direct link to Returns")

`void`

---

### logicalToCoordinate()[​](#logicaltocoordinate "Direct link to logicalToCoordinate()")

> **logicalToCoordinate**(`logical`): [`Coordinate`](/lightweight-charts/docs/4.0/api/type-aliases/Coordinate)

Converts a logical index to local x coordinate.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **logical**: [`Logical`](/lightweight-charts/docs/4.0/api/type-aliases/Logical)

Logical index needs to be converted

#### Returns[​](#returns-9 "Direct link to Returns")

[`Coordinate`](/lightweight-charts/docs/4.0/api/type-aliases/Coordinate)

x coordinate of that time or `null` if the chart doesn't have data

---

### coordinateToLogical()[​](#coordinatetological "Direct link to coordinateToLogical()")

> **coordinateToLogical**(`x`): [`Logical`](/lightweight-charts/docs/4.0/api/type-aliases/Logical)

Converts a coordinate to logical index.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **x**: `number`

Coordinate needs to be converted

#### Returns[​](#returns-10 "Direct link to Returns")

[`Logical`](/lightweight-charts/docs/4.0/api/type-aliases/Logical)

Logical index that is located on that coordinate or `null` if the chart doesn't have data

---

### timeToCoordinate()[​](#timetocoordinate "Direct link to timeToCoordinate()")

> **timeToCoordinate**(`time`): [`Coordinate`](/lightweight-charts/docs/4.0/api/type-aliases/Coordinate)

Converts a time to local x coordinate.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **time**: [`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)

Time needs to be converted

#### Returns[​](#returns-11 "Direct link to Returns")

[`Coordinate`](/lightweight-charts/docs/4.0/api/type-aliases/Coordinate)

X coordinate of that time or `null` if no time found on time scale

---

### coordinateToTime()[​](#coordinatetotime "Direct link to coordinateToTime()")

> **coordinateToTime**(`x`): [`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)

Converts a coordinate to time.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **x**: `number`

Coordinate needs to be converted.

#### Returns[​](#returns-12 "Direct link to Returns")

[`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)

Time of a bar that is located on that coordinate or `null` if there are no bars found on that coordinate.

---

### width()[​](#width "Direct link to width()")

> **width**(): `number`

Returns a width of the time scale.

#### Returns[​](#returns-13 "Direct link to Returns")

`number`

---

### height()[​](#height "Direct link to height()")

> **height**(): `number`

Returns a height of the time scale.

#### Returns[​](#returns-14 "Direct link to Returns")

`number`

---

### subscribeVisibleTimeRangeChange()[​](#subscribevisibletimerangechange "Direct link to subscribeVisibleTimeRangeChange()")

> **subscribeVisibleTimeRangeChange**(`handler`): `void`

Subscribe to the visible time range change events.

The argument passed to the handler function is an object with `from` and `to` properties of type [Time](/lightweight-charts/docs/4.0/api/type-aliases/Time), or `null` if there is no visible data.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **handler**: [`TimeRangeChangeEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/TimeRangeChangeEventHandler)

Handler (function) to be called when the visible indexes change.

#### Returns[​](#returns-15 "Direct link to Returns")

`void`

#### Example[​](#example-2 "Direct link to Example")

```prism-code
function myVisibleTimeRangeChangeHandler(newVisibleTimeRange) {  
    if (newVisibleTimeRange === null) {  
        // handle null  
    }  
  
    // handle new logical range  
}  
  
chart.timeScale().subscribeVisibleTimeRangeChange(myVisibleTimeRangeChangeHandler);
```

---

### unsubscribeVisibleTimeRangeChange()[​](#unsubscribevisibletimerangechange "Direct link to unsubscribeVisibleTimeRangeChange()")

> **unsubscribeVisibleTimeRangeChange**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeVisibleTimeRangeChange](/lightweight-charts/docs/4.0/api/interfaces/ITimeScaleApi#subscribevisibletimerangechange).

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **handler**: [`TimeRangeChangeEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/TimeRangeChangeEventHandler)

Previously subscribed handler

#### Returns[​](#returns-16 "Direct link to Returns")

`void`

#### Example[​](#example-3 "Direct link to Example")

```prism-code
chart.timeScale().unsubscribeVisibleTimeRangeChange(myVisibleTimeRangeChangeHandler);
```

---

### subscribeVisibleLogicalRangeChange()[​](#subscribevisiblelogicalrangechange "Direct link to subscribeVisibleLogicalRangeChange()")

> **subscribeVisibleLogicalRangeChange**(`handler`): `void`

Subscribe to the visible logical range change events.

The argument passed to the handler function is an object with `from` and `to` properties of type `number`, or `null` if there is no visible data.

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **handler**: [`LogicalRangeChangeEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/LogicalRangeChangeEventHandler)

Handler (function) to be called when the visible indexes change.

#### Returns[​](#returns-17 "Direct link to Returns")

`void`

#### Example[​](#example-4 "Direct link to Example")

```prism-code
function myVisibleLogicalRangeChangeHandler(newVisibleLogicalRange) {  
    if (newVisibleLogicalRange === null) {  
        // handle null  
    }  
  
    // handle new logical range  
}  
  
chart.timeScale().subscribeVisibleLogicalRangeChange(myVisibleLogicalRangeChangeHandler);
```

---

### unsubscribeVisibleLogicalRangeChange()[​](#unsubscribevisiblelogicalrangechange "Direct link to unsubscribeVisibleLogicalRangeChange()")

> **unsubscribeVisibleLogicalRangeChange**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeVisibleLogicalRangeChange](/lightweight-charts/docs/4.0/api/interfaces/ITimeScaleApi#subscribevisiblelogicalrangechange).

#### Parameters[​](#parameters-10 "Direct link to Parameters")

• **handler**: [`LogicalRangeChangeEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/LogicalRangeChangeEventHandler)

Previously subscribed handler

#### Returns[​](#returns-18 "Direct link to Returns")

`void`

#### Example[​](#example-5 "Direct link to Example")

```prism-code
chart.timeScale().unsubscribeVisibleLogicalRangeChange(myVisibleLogicalRangeChangeHandler);
```

---

### subscribeSizeChange()[​](#subscribesizechange "Direct link to subscribeSizeChange()")

> **subscribeSizeChange**(`handler`): `void`

Adds a subscription to time scale size changes

#### Parameters[​](#parameters-11 "Direct link to Parameters")

• **handler**: [`SizeChangeEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/SizeChangeEventHandler)

Handler (function) to be called when the time scale size changes

#### Returns[​](#returns-19 "Direct link to Returns")

`void`

---

### unsubscribeSizeChange()[​](#unsubscribesizechange "Direct link to unsubscribeSizeChange()")

> **unsubscribeSizeChange**(`handler`): `void`

Removes a subscription to time scale size changes

#### Parameters[​](#parameters-12 "Direct link to Parameters")

• **handler**: [`SizeChangeEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/SizeChangeEventHandler)

Previously subscribed handler

#### Returns[​](#returns-20 "Direct link to Returns")

`void`

---

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the time scale.

#### Parameters[​](#parameters-13 "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`TimeScaleOptions`](/lightweight-charts/docs/4.0/api/interfaces/TimeScaleOptions)>

Any subset of options.

#### Returns[​](#returns-21 "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`TimeScaleOptions`](/lightweight-charts/docs/4.0/api/interfaces/TimeScaleOptions)>

Returns current options

#### Returns[​](#returns-22 "Direct link to Returns")

`Readonly` <[`TimeScaleOptions`](/lightweight-charts/docs/4.0/api/interfaces/TimeScaleOptions)>

Currently applied options