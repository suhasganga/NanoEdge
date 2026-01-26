Version: 4.0

On this page

The main interface of a single chart.

## Methods[​](#methods "Direct link to Methods")

### remove()[​](#remove "Direct link to remove()")

> **remove**(): `void`

Removes the chart object including all DOM elements. This is an irreversible operation, you cannot do anything with the chart after removing it.

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### resize()[​](#resize "Direct link to resize()")

> **resize**(`width`, `height`, `forceRepaint`?): `void`

Sets fixed size of the chart. By default chart takes up 100% of its container.

If chart has the `autoSize` option enabled, and the ResizeObserver is available then
the width and height values will be ignored.

#### Parameters[​](#parameters "Direct link to Parameters")

• **width**: `number`

Target width of the chart.

• **height**: `number`

Target height of the chart.

• **forceRepaint?**: `boolean`

True to initiate resize immediately. One could need this to get screenshot immediately after resize.

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

---

### addAreaSeries()[​](#addareaseries "Direct link to addAreaSeries()")

> **addAreaSeries**(`areaOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Area"`>

Creates an area series with specified parameters.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **areaOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.0/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-2 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Area"`>

An interface of the created series.

#### Example[​](#example "Direct link to Example")

```prism-code
const series = chart.addAreaSeries();
```

---

### addBaselineSeries()[​](#addbaselineseries "Direct link to addBaselineSeries()")

> **addBaselineSeries**(`baselineOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Baseline"`>

Creates a baseline series with specified parameters.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **baselineOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.0/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-3 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Baseline"`>

An interface of the created series.

#### Example[​](#example-1 "Direct link to Example")

```prism-code
const series = chart.addBaselineSeries();
```

---

### addBarSeries()[​](#addbarseries "Direct link to addBarSeries()")

> **addBarSeries**(`barOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Bar"`>

Creates a bar series with specified parameters.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **barOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.0/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-4 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Bar"`>

An interface of the created series.

#### Example[​](#example-2 "Direct link to Example")

```prism-code
const series = chart.addBarSeries();
```

---

### addCandlestickSeries()[​](#addcandlestickseries "Direct link to addCandlestickSeries()")

> **addCandlestickSeries**(`candlestickOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Candlestick"`>

Creates a candlestick series with specified parameters.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **candlestickOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.0/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-5 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Candlestick"`>

An interface of the created series.

#### Example[​](#example-3 "Direct link to Example")

```prism-code
const series = chart.addCandlestickSeries();
```

---

### addHistogramSeries()[​](#addhistogramseries "Direct link to addHistogramSeries()")

> **addHistogramSeries**(`histogramOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Histogram"`>

Creates a histogram series with specified parameters.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **histogramOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.0/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-6 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Histogram"`>

An interface of the created series.

#### Example[​](#example-4 "Direct link to Example")

```prism-code
const series = chart.addHistogramSeries();
```

---

### addLineSeries()[​](#addlineseries "Direct link to addLineSeries()")

> **addLineSeries**(`lineOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Line"`>

Creates a line series with specified parameters.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **lineOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.0/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-7 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<`"Line"`>

An interface of the created series.

#### Example[​](#example-5 "Direct link to Example")

```prism-code
const series = chart.addLineSeries();
```

---

### removeSeries()[​](#removeseries "Direct link to removeSeries()")

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you cannot do anything with the series after removing it.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **seriesApi**: [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsMap)>

#### Returns[​](#returns-8 "Direct link to Returns")

`void`

#### Example[​](#example-6 "Direct link to Example")

```prism-code
chart.removeSeries(series);
```

---

### subscribeClick()[​](#subscribeclick "Direct link to subscribeClick()")

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/MouseEventHandler)

Handler to be called on mouse click.

#### Returns[​](#returns-9 "Direct link to Returns")

`void`

#### Example[​](#example-7 "Direct link to Example")

```prism-code
function myClickHandler(param) {  
    if (!param.point) {  
        return;  
    }  
  
    console.log(`Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
}  
  
chart.subscribeClick(myClickHandler);
```

---

### unsubscribeClick()[​](#unsubscribeclick "Direct link to unsubscribeClick()")

> **unsubscribeClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeClick](/lightweight-charts/docs/4.0/api/interfaces/IChartApi#subscribeclick).

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/MouseEventHandler)

Previously subscribed handler

#### Returns[​](#returns-10 "Direct link to Returns")

`void`

#### Example[​](#example-8 "Direct link to Example")

```prism-code
chart.unsubscribeClick(myClickHandler);
```

---

### subscribeCrosshairMove()[​](#subscribecrosshairmove "Direct link to subscribeCrosshairMove()")

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](#parameters-10 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/MouseEventHandler)

Handler to be called on crosshair move.

#### Returns[​](#returns-11 "Direct link to Returns")

`void`

#### Example[​](#example-9 "Direct link to Example")

```prism-code
function myCrosshairMoveHandler(param) {  
    if (!param.point) {  
        return;  
    }  
  
    console.log(`Crosshair moved to ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
}  
  
chart.subscribeCrosshairMove(myCrosshairMoveHandler);
```

---

### unsubscribeCrosshairMove()[​](#unsubscribecrosshairmove "Direct link to unsubscribeCrosshairMove()")

> **unsubscribeCrosshairMove**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeCrosshairMove](/lightweight-charts/docs/4.0/api/interfaces/IChartApi#subscribecrosshairmove).

#### Parameters[​](#parameters-11 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.0/api/type-aliases/MouseEventHandler)

Previously subscribed handler

#### Returns[​](#returns-12 "Direct link to Returns")

`void`

#### Example[​](#example-10 "Direct link to Example")

```prism-code
chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);
```

---

### priceScale()[​](#pricescale "Direct link to priceScale()")

> **priceScale**(`priceScaleId`): [`IPriceScaleApi`](/lightweight-charts/docs/4.0/api/interfaces/IPriceScaleApi)

Returns API to manipulate a price scale.

#### Parameters[​](#parameters-12 "Direct link to Parameters")

• **priceScaleId**: `string`

ID of the price scale.

#### Returns[​](#returns-13 "Direct link to Returns")

[`IPriceScaleApi`](/lightweight-charts/docs/4.0/api/interfaces/IPriceScaleApi)

Price scale API.

---

### timeScale()[​](#timescale "Direct link to timeScale()")

> **timeScale**(): [`ITimeScaleApi`](/lightweight-charts/docs/4.0/api/interfaces/ITimeScaleApi)

Returns API to manipulate the time scale

#### Returns[​](#returns-14 "Direct link to Returns")

[`ITimeScaleApi`](/lightweight-charts/docs/4.0/api/interfaces/ITimeScaleApi)

Target API

---

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](#parameters-13 "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/4.0/api/type-aliases/DeepPartial) <[`ChartOptions`](/lightweight-charts/docs/4.0/api/interfaces/ChartOptions)>

Any subset of options.

#### Returns[​](#returns-15 "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`ChartOptions`](/lightweight-charts/docs/4.0/api/interfaces/ChartOptions)>

Returns currently applied options

#### Returns[​](#returns-16 "Direct link to Returns")

`Readonly` <[`ChartOptions`](/lightweight-charts/docs/4.0/api/interfaces/ChartOptions)>

Full set of currently applied options, including defaults

---

### takeScreenshot()[​](#takescreenshot "Direct link to takeScreenshot()")

> **takeScreenshot**(): `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding crosshair.

#### Returns[​](#returns-17 "Direct link to Returns")

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like `toDataURL()` or `toBlob()` can be used to serialize the result.

---

### autoSizeActive()[​](#autosizeactive "Direct link to autoSizeActive()")

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to check
whether the chart is handling resizing automatically with a `ResizeObserver`.

#### Returns[​](#returns-18 "Direct link to Returns")

`boolean`

Whether the `autoSize` option is enabled and the active.