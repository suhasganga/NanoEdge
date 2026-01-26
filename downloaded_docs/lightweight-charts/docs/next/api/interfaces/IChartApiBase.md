Version: Next

On this page

The main interface of a single chart.

## Extended by[​](#extended-by "Direct link to Extended by")

* [`IChartApi`](/lightweight-charts/docs/next/api/interfaces/IChartApi)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

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

> **addCustomSeries**<`TData`, `TOptions`, `TPartialOptions`>(`customPaneView`, `customOptions`?, `paneIndex`?): [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`"Custom"`, `HorzScaleItem`, `TData` | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`>, `TOptions`, `TPartialOptions`>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom renderer to
implement chart types which the library doesn't support by default.

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`>

• **TOptions** *extends* [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions)

• **TPartialOptions** *extends* [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> = [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **customPaneView**: [`ICustomSeriesPaneView`](/lightweight-charts/docs/next/api/interfaces/ICustomSeriesPaneView)<`HorzScaleItem`, `TData`, `TOptions`>

A custom series pane view which implements the custom renderer.

• **customOptions?**: [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`TOptions` & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>

Customization parameters of the series being created.

```prism-code
const series = chart.addCustomSeries(myCustomPaneView);
```

• **paneIndex?**: `number`

#### Returns[​](#returns-2 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`"Custom"`, `HorzScaleItem`, `TData` | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`>, `TOptions`, `TPartialOptions`>

---

### addSeries()[​](#addseries "Direct link to addSeries()")

> **addSeries**<`T`>(`definition`, `options`?, `paneIndex`?): [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`T`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](/lightweight-charts/docs/next/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`T`], [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap)[`T`], [`SeriesPartialOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesPartialOptionsMap)[`T`]>

Creates a series with specified parameters.

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

• **T** *extends* keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap)

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **definition**: [`SeriesDefinition`](/lightweight-charts/docs/next/api/interfaces/SeriesDefinition)<`T`>

A series definition.

• **options?**: [`SeriesPartialOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesPartialOptionsMap)[`T`]

Customization parameters of the series being created.

• **paneIndex?**: `number`

An index of the pane where the series should be created.

```prism-code
const series = chart.addSeries(LineSeries, { lineWidth: 2 });
```

#### Returns[​](#returns-3 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<`T`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](/lightweight-charts/docs/next/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`T`], [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap)[`T`], [`SeriesPartialOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesPartialOptionsMap)[`T`]>

---

### removeSeries()[​](#removeseries "Direct link to removeSeries()")

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you cannot do anything with the series after removing it.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **seriesApi**: [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

#### Returns[​](#returns-4 "Direct link to Returns")

`void`

#### Example[​](#example "Direct link to Example")

```prism-code
chart.removeSeries(series);
```

---

### subscribeClick()[​](#subscribeclick "Direct link to subscribeClick()")

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/next/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Handler to be called on mouse click.

#### Returns[​](#returns-5 "Direct link to Returns")

`void`

#### Example[​](#example-1 "Direct link to Example")

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

Unsubscribe a handler that was previously subscribed using [subscribeClick](/lightweight-charts/docs/next/api/interfaces/IChartApiBase#subscribeclick).

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/next/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](#returns-6 "Direct link to Returns")

`void`

#### Example[​](#example-2 "Direct link to Example")

```prism-code
chart.unsubscribeClick(myClickHandler);
```

---

### subscribeDblClick()[​](#subscribedblclick "Direct link to subscribeDblClick()")

> **subscribeDblClick**(`handler`): `void`

Subscribe to the chart double-click event.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/next/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Handler to be called on mouse double-click.

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

#### Example[​](#example-3 "Direct link to Example")

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

Unsubscribe a handler that was previously subscribed using [subscribeDblClick](/lightweight-charts/docs/next/api/interfaces/IChartApiBase#subscribedblclick).

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/next/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](#returns-8 "Direct link to Returns")

`void`

#### Example[​](#example-4 "Direct link to Example")

```prism-code
chart.unsubscribeDblClick(myDblClickHandler);
```

---

### subscribeCrosshairMove()[​](#subscribecrosshairmove "Direct link to subscribeCrosshairMove()")

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/next/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Handler to be called on crosshair move.

#### Returns[​](#returns-9 "Direct link to Returns")

`void`

#### Example[​](#example-5 "Direct link to Example")

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

Unsubscribe a handler that was previously subscribed using [subscribeCrosshairMove](/lightweight-charts/docs/next/api/interfaces/IChartApiBase#subscribecrosshairmove).

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **handler**: [`MouseEventHandler`](/lightweight-charts/docs/next/api/type-aliases/MouseEventHandler)<`HorzScaleItem`>

Previously subscribed handler

#### Returns[​](#returns-10 "Direct link to Returns")

`void`

#### Example[​](#example-6 "Direct link to Example")

```prism-code
chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);
```

---

### priceScale()[​](#pricescale "Direct link to priceScale()")

> **priceScale**(`priceScaleId`, `paneIndex`?): [`IPriceScaleApi`](/lightweight-charts/docs/next/api/interfaces/IPriceScaleApi)

Returns API to manipulate a price scale.

#### Parameters[​](#parameters-10 "Direct link to Parameters")

• **priceScaleId**: `string`

ID of the price scale.

• **paneIndex?**: `number`

Index of the pane (default: 0)

#### Returns[​](#returns-11 "Direct link to Returns")

[`IPriceScaleApi`](/lightweight-charts/docs/next/api/interfaces/IPriceScaleApi)

Price scale API.

---

### timeScale()[​](#timescale "Direct link to timeScale()")

> **timeScale**(): [`ITimeScaleApi`](/lightweight-charts/docs/next/api/interfaces/ITimeScaleApi)<`HorzScaleItem`>

Returns API to manipulate the time scale

#### Returns[​](#returns-12 "Direct link to Returns")

[`ITimeScaleApi`](/lightweight-charts/docs/next/api/interfaces/ITimeScaleApi)<`HorzScaleItem`>

Target API

---

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](#parameters-11 "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`ChartOptionsImpl`](/lightweight-charts/docs/next/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>>

Any subset of options.

#### Returns[​](#returns-13 "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`ChartOptionsImpl`](/lightweight-charts/docs/next/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>>

Returns currently applied options

#### Returns[​](#returns-14 "Direct link to Returns")

`Readonly` <[`ChartOptionsImpl`](/lightweight-charts/docs/next/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>>

Full set of currently applied options, including defaults

---

### takeScreenshot()[​](#takescreenshot "Direct link to takeScreenshot()")

> **takeScreenshot**(`addTopLayer`?, `includeCrosshair`?): `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding crosshair.

#### Parameters[​](#parameters-12 "Direct link to Parameters")

• **addTopLayer?**: `boolean`

if true, the top layer and primitives will be included in the screenshot (default: false)

• **includeCrosshair?**: `boolean`

works only if addTopLayer is enabled. If true, the crosshair will be included in the screenshot (default: false)

#### Returns[​](#returns-15 "Direct link to Returns")

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like `toDataURL()` or `toBlob()` can be used to serialize the result.

---

### addPane()[​](#addpane "Direct link to addPane()")

> **addPane**(`preserveEmptyPane`?): [`IPaneApi`](/lightweight-charts/docs/next/api/interfaces/IPaneApi)<`HorzScaleItem`>

Add a pane to the chart

#### Parameters[​](#parameters-13 "Direct link to Parameters")

• **preserveEmptyPane?**: `boolean`

Whether to preserve the empty pane

#### Returns[​](#returns-16 "Direct link to Returns")

[`IPaneApi`](/lightweight-charts/docs/next/api/interfaces/IPaneApi)<`HorzScaleItem`>

The pane API

---

### panes()[​](#panes "Direct link to panes()")

> **panes**(): [`IPaneApi`](/lightweight-charts/docs/next/api/interfaces/IPaneApi)<`HorzScaleItem`>[]

Returns array of panes' API

#### Returns[​](#returns-17 "Direct link to Returns")

[`IPaneApi`](/lightweight-charts/docs/next/api/interfaces/IPaneApi)<`HorzScaleItem`>[]

array of pane's Api

---

### removePane()[​](#removepane "Direct link to removePane()")

> **removePane**(`index`): `void`

Removes a pane with index

#### Parameters[​](#parameters-14 "Direct link to Parameters")

• **index**: `number`

the pane to be removed

#### Returns[​](#returns-18 "Direct link to Returns")

`void`

---

### swapPanes()[​](#swappanes "Direct link to swapPanes()")

> **swapPanes**(`first`, `second`): `void`

swap the position of two panes.

#### Parameters[​](#parameters-15 "Direct link to Parameters")

• **first**: `number`

the first index

• **second**: `number`

the second index

#### Returns[​](#returns-19 "Direct link to Returns")

`void`

---

### autoSizeActive()[​](#autosizeactive "Direct link to autoSizeActive()")

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to check
whether the chart is handling resizing automatically with a `ResizeObserver`.

#### Returns[​](#returns-20 "Direct link to Returns")

`boolean`

Whether the `autoSize` option is enabled and the active.

---

### chartElement()[​](#chartelement "Direct link to chartElement()")

> **chartElement**(): `HTMLDivElement`

Returns the generated div element containing the chart. This can be used for adding your own additional event listeners, or for measuring the
elements dimensions and position within the document.

#### Returns[​](#returns-21 "Direct link to Returns")

`HTMLDivElement`

generated div element containing the chart.

---

### setCrosshairPosition()[​](#setcrosshairposition "Direct link to setCrosshairPosition()")

> **setCrosshairPosition**(`price`, `horizontalPosition`, `seriesApi`): `void`

Set the crosshair position within the chart.

Usually the crosshair position is set automatically by the user's actions. However in some cases you may want to set it explicitly.

For example if you want to synchronise the crosshairs of two separate charts.

#### Parameters[​](#parameters-16 "Direct link to Parameters")

• **price**: `number`

The price (vertical coordinate) of the new crosshair position.

• **horizontalPosition**: `HorzScaleItem`

The horizontal coordinate (time by default) of the new crosshair position.

• **seriesApi**: [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

#### Returns[​](#returns-22 "Direct link to Returns")

`void`

---

### clearCrosshairPosition()[​](#clearcrosshairposition "Direct link to clearCrosshairPosition()")

> **clearCrosshairPosition**(): `void`

Clear the crosshair position within the chart.

#### Returns[​](#returns-23 "Direct link to Returns")

`void`

---

### paneSize()[​](#panesize "Direct link to paneSize()")

> **paneSize**(`paneIndex`?): [`PaneSize`](/lightweight-charts/docs/next/api/interfaces/PaneSize)

Returns the dimensions of the chart pane (the plot surface which excludes time and price scales).
This would typically only be useful for plugin development.

#### Parameters[​](#parameters-17 "Direct link to Parameters")

• **paneIndex?**: `number`

The index of the pane

#### Returns[​](#returns-24 "Direct link to Returns")

[`PaneSize`](/lightweight-charts/docs/next/api/interfaces/PaneSize)

Dimensions of the chart pane

#### Default Value[​](#default-value "Direct link to Default Value")

`0`

---

### horzBehaviour()[​](#horzbehaviour "Direct link to horzBehaviour()")

> **horzBehaviour**(): [`IHorzScaleBehavior`](/lightweight-charts/docs/next/api/interfaces/IHorzScaleBehavior)<`HorzScaleItem`>

Returns the horizontal scale behaviour.

#### Returns[​](#returns-25 "Direct link to Returns")

[`IHorzScaleBehavior`](/lightweight-charts/docs/next/api/interfaces/IHorzScaleBehavior)<`HorzScaleItem`>