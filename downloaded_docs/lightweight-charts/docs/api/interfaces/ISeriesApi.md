Version: 5.1

On this page

Represents the interface for interacting with series.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **TSeriesType** *extends* [`SeriesType`](/lightweight-charts/docs/api/type-aliases/SeriesType)

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/api/type-aliases/Time)

• **TData** = [`SeriesDataItemTypeMap`](/lightweight-charts/docs/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`TSeriesType`]

• **TOptions** = [`SeriesOptionsMap`](/lightweight-charts/docs/api/interfaces/SeriesOptionsMap)[`TSeriesType`]

• **TPartialOptions** = [`SeriesPartialOptionsMap`](/lightweight-charts/docs/api/interfaces/SeriesPartialOptionsMap)[`TSeriesType`]

## Methods[​](#methods "Direct link to Methods")

### priceFormatter()[​](#priceformatter "Direct link to priceFormatter()")

> **priceFormatter**(): [`IPriceFormatter`](/lightweight-charts/docs/api/interfaces/IPriceFormatter)

Returns current price formatter

#### Returns[​](#returns "Direct link to Returns")

[`IPriceFormatter`](/lightweight-charts/docs/api/interfaces/IPriceFormatter)

Interface to the price formatter object that can be used to format prices in the same way as the chart does

---

### priceToCoordinate()[​](#pricetocoordinate "Direct link to priceToCoordinate()")

> **priceToCoordinate**(`price`): [`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

Converts specified series price to pixel coordinate according to the series price scale

#### Parameters[​](#parameters "Direct link to Parameters")

• **price**: `number`

Input price to be converted

#### Returns[​](#returns-1 "Direct link to Returns")

[`Coordinate`](/lightweight-charts/docs/api/type-aliases/Coordinate)

Pixel coordinate of the price level on the chart

---

### coordinateToPrice()[​](#coordinatetoprice "Direct link to coordinateToPrice()")

> **coordinateToPrice**(`coordinate`): [`BarPrice`](/lightweight-charts/docs/api/type-aliases/BarPrice)

Converts specified coordinate to price value according to the series price scale

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **coordinate**: `number`

Input coordinate to be converted

#### Returns[​](#returns-2 "Direct link to Returns")

[`BarPrice`](/lightweight-charts/docs/api/type-aliases/BarPrice)

Price value of the coordinate on the chart

---

### barsInLogicalRange()[​](#barsinlogicalrange "Direct link to barsInLogicalRange()")

> **barsInLogicalRange**(`range`): [`BarsInfo`](/lightweight-charts/docs/api/interfaces/BarsInfo)<`HorzScaleItem`>

Returns bars information for the series in the provided [logical range](/lightweight-charts/docs/time-scale#logical-range) or `null`, if no series data has been found in the requested range.
This method can be used, for instance, to implement downloading historical data while scrolling to prevent a user from seeing empty space.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **range**: [`IRange`](/lightweight-charts/docs/api/interfaces/IRange)<`number`>

The [logical range](/lightweight-charts/docs/time-scale#logical-range) to retrieve info for.

#### Returns[​](#returns-3 "Direct link to Returns")

[`BarsInfo`](/lightweight-charts/docs/api/interfaces/BarsInfo)<`HorzScaleItem`>

The bars info for the given logical range.

#### Examples[​](#examples "Direct link to Examples")

```prism-code
const barsInfo = series.barsInLogicalRange(chart.timeScale().getVisibleLogicalRange());  
console.log(barsInfo);
```

```prism-code
function onVisibleLogicalRangeChanged(newVisibleLogicalRange) {  
    const barsInfo = series.barsInLogicalRange(newVisibleLogicalRange);  
    // if there less than 50 bars to the left of the visible area  
    if (barsInfo !== null && barsInfo.barsBefore < 50) {  
        // try to load additional historical data and prepend it to the series data  
    }  
}  
  
chart.timeScale().subscribeVisibleLogicalRangeChange(onVisibleLogicalRangeChanged);
```

---

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the existing series
You can set options initially when you create series or use the `applyOptions` method of the series to change the existing options.
Note that you can only pass options you want to change.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **options**: `TPartialOptions`

Any subset of options.

#### Returns[​](#returns-4 "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly`<`TOptions`>

Returns currently applied options

#### Returns[​](#returns-5 "Direct link to Returns")

`Readonly`<`TOptions`>

Full set of currently applied options, including defaults

---

### priceScale()[​](#pricescale "Direct link to priceScale()")

> **priceScale**(): [`IPriceScaleApi`](/lightweight-charts/docs/api/interfaces/IPriceScaleApi)

Returns the API interface for controlling the price scale that this series is currently attached to.

#### Returns[​](#returns-6 "Direct link to Returns")

[`IPriceScaleApi`](/lightweight-charts/docs/api/interfaces/IPriceScaleApi)

IPriceScaleApi An interface for controlling the price scale (axis component) currently used by this series

#### Remarks[​](#remarks "Direct link to Remarks")

Important: The returned PriceScaleApi is bound to the specific price scale (by ID and pane) that the series
is using at the time this method is called. If you later move the series to a different pane or attach it
to a different price scale (e.g., from 'right' to 'left'), the previously returned PriceScaleApi will NOT
follow the series. It will continue to control the original price scale it was created for.

To control the new price scale after moving a series, you must call this method again to get a fresh
PriceScaleApi instance for the current price scale.

---

### setData()[​](#setdata "Direct link to setData()")

> **setData**(`data`): `void`

Sets or replaces series data.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **data**: `TData`[]

Ordered (earlier time point goes first) array of data items. Old data is fully replaced with the new one.

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

#### Examples[​](#examples-1 "Direct link to Examples")

```prism-code
lineSeries.setData([  
    { time: '2018-12-12', value: 24.11 },  
    { time: '2018-12-13', value: 31.74 },  
]);
```

```prism-code
barSeries.setData([  
    { time: '2018-12-19', open: 141.77, high: 170.39, low: 120.25, close: 145.72 },  
    { time: '2018-12-20', open: 145.72, high: 147.99, low: 100.11, close: 108.19 },  
]);
```

---

### update()[​](#update "Direct link to update()")

> **update**(`bar`, `historicalUpdate`?): `void`

Adds new data item to the existing set (or updates the latest item if times of the passed/latest items are equal).

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **bar**: `TData`

A single data item to be added. Time of the new item must be greater or equal to the latest existing time point.
If the new item's time is equal to the last existing item's time, then the existing item is replaced with the new one.

• **historicalUpdate?**: `boolean`

If true, allows updating an existing data point that is not the latest bar. Default is false.
Updating older data using `historicalUpdate` will be slower than updating the most recent data point.

#### Returns[​](#returns-8 "Direct link to Returns")

`void`

#### Examples[​](#examples-2 "Direct link to Examples")

```prism-code
lineSeries.update({  
    time: '2018-12-12',  
    value: 24.11,  
});
```

```prism-code
barSeries.update({  
    time: '2018-12-19',  
    open: 141.77,  
    high: 170.39,  
    low: 120.25,  
    close: 145.72,  
});
```

---

### pop()[​](#pop "Direct link to pop()")

> **pop**(`count`): `TData`[]

Removes one or more data items from the end of the series.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **count**: `number`

The number of data items to remove.

#### Returns[​](#returns-9 "Direct link to Returns")

`TData`[]

The removed data items.

#### Example[​](#example "Direct link to Example")

```prism-code
const removedData = lineSeries.pop(1);  
console.log(removedData);
```

---

### dataByIndex()[​](#databyindex "Direct link to dataByIndex()")

> **dataByIndex**(`logicalIndex`, `mismatchDirection`?): `TData`

Returns a bar data by provided logical index.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **logicalIndex**: `number`

Logical index

• **mismatchDirection?**: [`MismatchDirection`](/lightweight-charts/docs/api/enumerations/MismatchDirection)

Search direction if no data found at provided logical index.

#### Returns[​](#returns-10 "Direct link to Returns")

`TData`

Original data item provided via setData or update methods.

#### Example[​](#example-1 "Direct link to Example")

```prism-code
const originalData = series.dataByIndex(10, LightweightCharts.MismatchDirection.NearestLeft);
```

---

### data()[​](#data "Direct link to data()")

> **data**(): readonly `TData`[]

Returns all the bar data for the series.

#### Returns[​](#returns-11 "Direct link to Returns")

readonly `TData`[]

Original data items provided via setData or update methods.

#### Example[​](#example-2 "Direct link to Example")

```prism-code
const originalData = series.data();
```

---

### subscribeDataChanged()[​](#subscribedatachanged "Direct link to subscribeDataChanged()")

> **subscribeDataChanged**(`handler`): `void`

Subscribe to the data changed event. This event is fired whenever the `update` or `setData` method is evoked
on the series.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **handler**: [`DataChangedHandler`](/lightweight-charts/docs/api/type-aliases/DataChangedHandler)

Handler to be called on a data changed event.

#### Returns[​](#returns-12 "Direct link to Returns")

`void`

#### Example[​](#example-3 "Direct link to Example")

```prism-code
function myHandler() {  
    const data = series.data();  
    console.log(`The data has changed. New Data length: ${data.length}`);  
}  
  
series.subscribeDataChanged(myHandler);
```

---

### unsubscribeDataChanged()[​](#unsubscribedatachanged "Direct link to unsubscribeDataChanged()")

> **unsubscribeDataChanged**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using [subscribeDataChanged](/lightweight-charts/docs/api/interfaces/ISeriesApi#subscribedatachanged).

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **handler**: [`DataChangedHandler`](/lightweight-charts/docs/api/type-aliases/DataChangedHandler)

Previously subscribed handler

#### Returns[​](#returns-13 "Direct link to Returns")

`void`

#### Example[​](#example-4 "Direct link to Example")

```prism-code
chart.unsubscribeDataChanged(myHandler);
```

---

### createPriceLine()[​](#createpriceline "Direct link to createPriceLine()")

> **createPriceLine**(`options`): [`IPriceLine`](/lightweight-charts/docs/api/interfaces/IPriceLine)

Creates a new price line

#### Parameters[​](#parameters-10 "Direct link to Parameters")

• **options**: [`CreatePriceLineOptions`](/lightweight-charts/docs/api/type-aliases/CreatePriceLineOptions)

Any subset of options, however `price` is required.

#### Returns[​](#returns-14 "Direct link to Returns")

[`IPriceLine`](/lightweight-charts/docs/api/interfaces/IPriceLine)

#### Example[​](#example-5 "Direct link to Example")

```prism-code
const priceLine = series.createPriceLine({  
    price: 80.0,  
    color: 'green',  
    lineWidth: 2,  
    lineStyle: LightweightCharts.LineStyle.Dotted,  
    axisLabelVisible: true,  
    title: 'P/L 500',  
});
```

---

### removePriceLine()[​](#removepriceline "Direct link to removePriceLine()")

> **removePriceLine**(`line`): `void`

Removes the price line that was created before.

#### Parameters[​](#parameters-11 "Direct link to Parameters")

• **line**: [`IPriceLine`](/lightweight-charts/docs/api/interfaces/IPriceLine)

A line to remove.

#### Returns[​](#returns-15 "Direct link to Returns")

`void`

#### Example[​](#example-6 "Direct link to Example")

```prism-code
const priceLine = series.createPriceLine({ price: 80.0 });  
series.removePriceLine(priceLine);
```

---

### priceLines()[​](#pricelines "Direct link to priceLines()")

> **priceLines**(): [`IPriceLine`](/lightweight-charts/docs/api/interfaces/IPriceLine)[]

Returns an array of price lines.

#### Returns[​](#returns-16 "Direct link to Returns")

[`IPriceLine`](/lightweight-charts/docs/api/interfaces/IPriceLine)[]

---

### seriesType()[​](#seriestype "Direct link to seriesType()")

> **seriesType**(): `TSeriesType`

Return current series type.

#### Returns[​](#returns-17 "Direct link to Returns")

`TSeriesType`

Type of the series.

#### Example[​](#example-7 "Direct link to Example")

```prism-code
const lineSeries = chart.addSeries(LineSeries);  
console.log(lineSeries.seriesType()); // "Line"  
  
const candlestickSeries = chart.addCandlestickSeries();  
console.log(candlestickSeries.seriesType()); // "Candlestick"
```

---

### lastValueData()[​](#lastvaluedata "Direct link to lastValueData()")

> **lastValueData**(`globalLast`): [`LastValueDataResult`](/lightweight-charts/docs/api/type-aliases/LastValueDataResult)

Return the last value data of the series.

#### Parameters[​](#parameters-12 "Direct link to Parameters")

• **globalLast**: `boolean`

If false, get the last value in the current visible range. Otherwise, fetch the absolute last value

#### Returns[​](#returns-18 "Direct link to Returns")

[`LastValueDataResult`](/lightweight-charts/docs/api/type-aliases/LastValueDataResult)

The last value data of the series.

#### Example[​](#example-8 "Direct link to Example")

```prism-code
const lineSeries = chart.addSeries(LineSeries);  
console.log(lineSeries.lastValueData(true)); // { noData: false, price: 24.11, color: '#000000' }  
  
const candlestickSeries = chart.addCandlestickSeries();  
console.log(candlestickSeries.lastValueData(false)); // { noData: false, price: 145.72, color: '#000000' }
```

---

### attachPrimitive()[​](#attachprimitive "Direct link to attachPrimitive()")

> **attachPrimitive**(`primitive`): `void`

Attaches additional drawing primitive to the series

#### Parameters[​](#parameters-13 "Direct link to Parameters")

• **primitive**: [`ISeriesPrimitive`](/lightweight-charts/docs/api/type-aliases/ISeriesPrimitive)<`HorzScaleItem`>

any implementation of ISeriesPrimitive interface

#### Returns[​](#returns-19 "Direct link to Returns")

`void`

---

### detachPrimitive()[​](#detachprimitive "Direct link to detachPrimitive()")

> **detachPrimitive**(`primitive`): `void`

Detaches additional drawing primitive from the series

#### Parameters[​](#parameters-14 "Direct link to Parameters")

• **primitive**: [`ISeriesPrimitive`](/lightweight-charts/docs/api/type-aliases/ISeriesPrimitive)<`HorzScaleItem`>

implementation of ISeriesPrimitive interface attached before
Does nothing if specified primitive was not attached

#### Returns[​](#returns-20 "Direct link to Returns")

`void`

---

### moveToPane()[​](#movetopane "Direct link to moveToPane()")

> **moveToPane**(`paneIndex`): `void`

Move the series to another pane.

If the pane with the specified index does not exist, the pane will be created.

#### Parameters[​](#parameters-15 "Direct link to Parameters")

• **paneIndex**: `number`

The index of the pane. Should be a number between 0 and the total number of panes.

#### Returns[​](#returns-21 "Direct link to Returns")

`void`

---

### seriesOrder()[​](#seriesorder "Direct link to seriesOrder()")

> **seriesOrder**(): `number`

Gets the zero-based index of this series within the list of all series on the current pane.

#### Returns[​](#returns-22 "Direct link to Returns")

`number`

The current index of the series in the pane's series collection.

---

### setSeriesOrder()[​](#setseriesorder "Direct link to setSeriesOrder()")

> **setSeriesOrder**(`order`): `void`

Sets the zero-based index of this series within the pane's series collection, thereby adjusting its rendering order.

Note:

* The chart may automatically recalculate this index after operations such as removing other series or moving this series to a different pane.
* If the provided index is less than 0, equal to, or greater than the number of series, it will be clamped to a valid range.
* Price scales derive their formatters from the series with the lowest index; changing the order may affect the price scale's formatting

#### Parameters[​](#parameters-16 "Direct link to Parameters")

• **order**: `number`

The desired zero-based index to set for this series within the pane.

#### Returns[​](#returns-23 "Direct link to Returns")

`void`

---

### getPane()[​](#getpane "Direct link to getPane()")

> **getPane**(): [`IPaneApi`](/lightweight-charts/docs/api/interfaces/IPaneApi)<`HorzScaleItem`>

Returns the pane to which the series is currently attached.

#### Returns[​](#returns-24 "Direct link to Returns")

[`IPaneApi`](/lightweight-charts/docs/api/interfaces/IPaneApi)<`HorzScaleItem`>

Pane API object to control the pane