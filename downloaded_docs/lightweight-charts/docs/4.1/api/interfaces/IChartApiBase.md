Version: 4.1

On this page

The main interface of a single chart.

## Extended by[​](#extended-by "Direct link to Extended by")

* [`IChartApi`](/lightweight-charts/docs/4.1/api/interfaces/IChartApi)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/4.1/api/type-aliases/Time)

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

### addCustomSeries()[​](#addcustomseries "Direct link to addCustomSeries()")

> **addCustomSeries**<`TData`, `TOptions`, `TPartialOptions`>(`customPaneView`, `customOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Custom"`, `HorzScaleItem`, `TData` | [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`>, `TOptions`, `TPartialOptions`>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom renderer to
implement chart types which the library doesn't support by default.

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/4.1/api/interfaces/CustomData)<`HorzScaleItem`>

• **TOptions** *extends* [`CustomSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CustomSeriesOptions)

• **TPartialOptions** *extends* [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> = [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **customPaneView**: [`ICustomSeriesPaneView`](/lightweight-charts/docs/4.1/api/interfaces/ICustomSeriesPaneView)<`HorzScaleItem`, `TData`, `TOptions`>

A custom series pane view which implements the custom renderer.

• **customOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

```prism-code
const series = chart.addCustomSeries(myCustomPaneView);
```

#### Returns[​](#returns-2 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Custom"`, `HorzScaleItem`, `TData` | [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`>, `TOptions`, `TPartialOptions`>

---

### addAreaSeries()[​](#addareaseries "Direct link to addAreaSeries()")

> **addAreaSeries**(`areaOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Area"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/4.1/api/interfaces/AreaData)<`HorzScaleItem`>, [`AreaSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/AreaSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

Creates an area series with specified parameters.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **areaOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-3 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Area"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/4.1/api/interfaces/AreaData)<`HorzScaleItem`>, [`AreaSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/AreaSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

An interface of the created series.

#### Example[​](#example "Direct link to Example")

```prism-code
const series = chart.addAreaSeries();
```

---

### addBaselineSeries()[​](#addbaselineseries "Direct link to addBaselineSeries()")

> **addBaselineSeries**(`baselineOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Baseline"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.1/api/interfaces/BaselineData)<`HorzScaleItem`>, [`BaselineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BaselineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

Creates a baseline series with specified parameters.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **baselineOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-4 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Baseline"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.1/api/interfaces/BaselineData)<`HorzScaleItem`>, [`BaselineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BaselineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

An interface of the created series.

#### Example[​](#example-1 "Direct link to Example")

```prism-code
const series = chart.addBaselineSeries();
```

---

### addBarSeries()[​](#addbarseries "Direct link to addBarSeries()")

> **addBarSeries**(`barOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Bar"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.1/api/interfaces/BarData)<`HorzScaleItem`>, [`BarSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BarSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

Creates a bar series with specified parameters.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **barOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-5 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Bar"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.1/api/interfaces/BarData)<`HorzScaleItem`>, [`BarSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BarSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

An interface of the created series.

#### Example[​](#example-2 "Direct link to Example")

```prism-code
const series = chart.addBarSeries();
```

---

### addCandlestickSeries()[​](#addcandlestickseries "Direct link to addCandlestickSeries()")

> **addCandlestickSeries**(`candlestickOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Candlestick"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickData)<`HorzScaleItem`>, [`CandlestickSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CandlestickSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

Creates a candlestick series with specified parameters.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **candlestickOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-6 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Candlestick"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickData)<`HorzScaleItem`>, [`CandlestickSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CandlestickSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

An interface of the created series.

#### Example[​](#example-3 "Direct link to Example")

```prism-code
const series = chart.addCandlestickSeries();
```

---

### addHistogramSeries()[​](#addhistogramseries "Direct link to addHistogramSeries()")

> **addHistogramSeries**(`histogramOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Histogram"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.1/api/interfaces/HistogramData)<`HorzScaleItem`>, [`HistogramSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

Creates a histogram series with specified parameters.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **histogramOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-7 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Histogram"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.1/api/interfaces/HistogramData)<`HorzScaleItem`>, [`HistogramSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

An interface of the created series.

#### Example[​](#example-4 "Direct link to Example")

```prism-code
const series = chart.addHistogramSeries();
```

---

### addLineSeries()[​](#addlineseries "Direct link to addLineSeries()")

> **addLineSeries**(`lineOptions`?): [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Line"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.1/api/interfaces/LineData)<`HorzScaleItem`>, [`LineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/LineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

Creates a line series with specified parameters.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **lineOptions?**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

#### Returns[​](#returns-8 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`"Line"`, `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.1/api/interfaces/LineData)<`HorzScaleItem`>, [`LineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/LineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

An interface of the created series.

#### Example[​](#example-5 "Direct link to Example")

```prism-code
const series = chart.addLineSeries();
```

---

### removeSeries()[​](#removeseries "Direct link to removeSeries()")

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you cannot do anything with the series after removing it.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **seriesApi**: [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`CustomData`](/lightweight-charts/docs/4.1/api/interfaces/CustomData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/4.1/api/interfaces/AreaData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.1/api/interfaces/BaselineData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.1/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.1/api/interfaces/HistogramData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.1/api/interfaces/LineData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/AreaSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BaselineSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CandlestickSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/HistogramSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/LineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

#### Returns[​](#returns-9 "Direct link to Returns")

`void`

#### Example[​](#example-6 "Direct link to Example")

```prism-code
chart.removeSeries(series);
```

---

### subscribeClick()[​](#subscribeclick "Direct link to subscribeClick()")

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.1/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Handler to be called on mouse click.

#### Returns[​](#returns-10 "Direct link to Returns")

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

Unsubscribe a handler that was previously subscribed using [subscribeClick](/lightweight-charts/docs/4.1/api/interfaces/IChartApiBase#subscribeclick).

#### Parameters[​](#parameters-10 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.1/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](#returns-11 "Direct link to Returns")

`void`

#### Example[​](#example-8 "Direct link to Example")

```prism-code
chart.unsubscribeClick(myClickHandler);
```

---

### subscribeDblClick()[​](#subscribedblclick "Direct link to subscribeDblClick()")

> **subscribeDblClick**(`handler`): `void`

Subscribe to the chart double-click event.

#### Parameters[​](#parameters-11 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.1/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Handler to be called on mouse double-click.

#### Returns[​](#returns-12 "Direct link to Returns")

`void`

#### Example[​](#example-9 "Direct link to Example")

```prism-code
function myDblClickHandler(param) {  
    if (!param.point) {  
        return;  
    }  
  
    console.log(`Double Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);  
}  
  
chart.subscribeDblClick(myDblClickHandler);
```

---

### unsubscribeDblClick()[​](#unsubscribedblclick "Direct link to unsubscribeDblClick()")

> **unsubscribeDblClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeDblClick](/lightweight-charts/docs/4.1/api/interfaces/IChartApiBase#subscribedblclick).

#### Parameters[​](#parameters-12 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.1/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](#returns-13 "Direct link to Returns")

`void`

#### Example[​](#example-10 "Direct link to Example")

```prism-code
chart.unsubscribeDblClick(myDblClickHandler);
```

---

### subscribeCrosshairMove()[​](#subscribecrosshairmove "Direct link to subscribeCrosshairMove()")

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](#parameters-13 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.1/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Handler to be called on crosshair move.

#### Returns[​](#returns-14 "Direct link to Returns")

`void`

#### Example[​](#example-11 "Direct link to Example")

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

Unsubscribe a handler that was previously subscribed using [subscribeCrosshairMove](/lightweight-charts/docs/4.1/api/interfaces/IChartApiBase#subscribecrosshairmove).

#### Parameters[​](#parameters-14 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/4.1/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](#returns-15 "Direct link to Returns")

`void`

#### Example[​](#example-12 "Direct link to Example")

```prism-code
chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);
```

---

### priceScale()[​](#pricescale "Direct link to priceScale()")

> **priceScale**(`priceScaleId`): [`IPriceScaleApi`](/lightweight-charts/docs/4.1/api/interfaces/IPriceScaleApi)

Returns API to manipulate a price scale.

#### Parameters[​](#parameters-15 "Direct link to Parameters")

• **priceScaleId**: `string`

ID of the price scale.

#### Returns[​](#returns-16 "Direct link to Returns")

[`IPriceScaleApi`](/lightweight-charts/docs/4.1/api/interfaces/IPriceScaleApi)

Price scale API.

---

### timeScale()[​](#timescale "Direct link to timeScale()")

> **timeScale**(): [`ITimeScaleApi`](/lightweight-charts/docs/4.1/api/interfaces/ITimeScaleApi)<`HorzScaleItem`>

Returns API to manipulate the time scale

#### Returns[​](#returns-17 "Direct link to Returns")

[`ITimeScaleApi`](/lightweight-charts/docs/4.1/api/interfaces/ITimeScaleApi)<`HorzScaleItem`>

Target API

---

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](#parameters-16 "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`ChartOptionsImpl`](/lightweight-charts/docs/4.1/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>>

Any subset of options.

#### Returns[​](#returns-18 "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`ChartOptionsImpl`](/lightweight-charts/docs/4.1/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>>

Returns currently applied options

#### Returns[​](#returns-19 "Direct link to Returns")

`Readonly` <[`ChartOptionsImpl`](/lightweight-charts/docs/4.1/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>>

Full set of currently applied options, including defaults

---

### takeScreenshot()[​](#takescreenshot "Direct link to takeScreenshot()")

> **takeScreenshot**(): `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding crosshair.

#### Returns[​](#returns-20 "Direct link to Returns")

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like `toDataURL()` or `toBlob()` can be used to serialize the result.

---

### autoSizeActive()[​](#autosizeactive "Direct link to autoSizeActive()")

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to check
whether the chart is handling resizing automatically with a `ResizeObserver`.

#### Returns[​](#returns-21 "Direct link to Returns")

`boolean`

Whether the `autoSize` option is enabled and the active.

---

### chartElement()[​](#chartelement "Direct link to chartElement()")

> **chartElement**(): `HTMLDivElement`

Returns the generated div element containing the chart. This can be used for adding your own additional event listeners, or for measuring the
elements dimensions and position within the document.

#### Returns[​](#returns-22 "Direct link to Returns")

`HTMLDivElement`

generated div element containing the chart.

---

### setCrosshairPosition()[​](#setcrosshairposition "Direct link to setCrosshairPosition()")

> **setCrosshairPosition**(`price`, `horizontalPosition`, `seriesApi`): `void`

Set the crosshair position within the chart.

Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly.

For example if you want to synchronise the crosshairs of two separate charts.

#### Parameters[​](#parameters-17 "Direct link to Parameters")

• **price**: `number`

The price (vertical coordinate) of the new crosshair position.

• **horizontalPosition**: `HorzScaleItem`

The horizontal coordinate (time by default) of the new crosshair position.

• **seriesApi**: [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`CustomData`](/lightweight-charts/docs/4.1/api/interfaces/CustomData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/4.1/api/interfaces/AreaData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.1/api/interfaces/BaselineData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.1/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.1/api/interfaces/HistogramData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.1/api/interfaces/LineData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/AreaSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BaselineSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/CandlestickSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/HistogramSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/4.1/api/type-aliases/LineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.1/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/4.1/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsCommon)>>

#### Returns[​](#returns-23 "Direct link to Returns")

`void`

---

### clearCrosshairPosition()[​](#clearcrosshairposition "Direct link to clearCrosshairPosition()")

> **clearCrosshairPosition**(): `void`

Clear the crosshair position within the chart.

#### Returns[​](#returns-24 "Direct link to Returns")

`void`

---

### paneSize()[​](#panesize "Direct link to paneSize()")

> **paneSize**(): [`PaneSize`](/lightweight-charts/docs/4.1/api/interfaces/PaneSize)

Returns the dimensions of the chart pane (the plot surface which excludes time and price scales).
This would typically only be useful for plugin development.

#### Returns[​](#returns-25 "Direct link to Returns")

[`PaneSize`](/lightweight-charts/docs/4.1/api/interfaces/PaneSize)

Dimensions of the chart pane