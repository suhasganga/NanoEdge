Version: 4.0

On this page

Represents the interface for interacting with series.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **TSeriesType** *extends* [`SeriesType`](/lightweight-charts/docs/4.0/api/type-aliases/SeriesType)

## Methods[​](#methods "Direct link to Methods")

### priceFormatter()[​](#priceformatter "Direct link to priceFormatter()")

> **priceFormatter**(): [`IPriceFormatter`](/lightweight-charts/docs/4.0/api/interfaces/IPriceFormatter)

Returns current price formatter

#### Returns[​](#returns "Direct link to Returns")

[`IPriceFormatter`](/lightweight-charts/docs/4.0/api/interfaces/IPriceFormatter)

Interface to the price formatter object that can be used to format prices in the same way as the chart does

---

### priceToCoordinate()[​](#pricetocoordinate "Direct link to priceToCoordinate()")

> **priceToCoordinate**(`price`): [`Coordinate`](/lightweight-charts/docs/4.0/api/type-aliases/Coordinate)

Converts specified series price to pixel coordinate according to the series price scale

#### Parameters[​](#parameters "Direct link to Parameters")

• **price**: `number`

Input price to be converted

#### Returns[​](#returns-1 "Direct link to Returns")

[`Coordinate`](/lightweight-charts/docs/4.0/api/type-aliases/Coordinate)

Pixel coordinate of the price level on the chart

---

### coordinateToPrice()[​](#coordinatetoprice "Direct link to coordinateToPrice()")

> **coordinateToPrice**(`coordinate`): [`BarPrice`](/lightweight-charts/docs/4.0/api/type-aliases/BarPrice)

Converts specified coordinate to price value according to the series price scale

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **coordinate**: `number`

Input coordinate to be converted

#### Returns[​](#returns-2 "Direct link to Returns")

[`BarPrice`](/lightweight-charts/docs/4.0/api/type-aliases/BarPrice)

Price value of the coordinate on the chart

---

### barsInLogicalRange()[​](#barsinlogicalrange "Direct link to barsInLogicalRange()")

> **barsInLogicalRange**(`range`): [`BarsInfo`](/lightweight-charts/docs/4.0/api/interfaces/BarsInfo)

Returns bars information for the series in the provided [logical range](/lightweight-charts/docs/4.0/time-scale#logical-range) or `null`, if no series data has been found in the requested range.
This method can be used, for instance, to implement downloading historical data while scrolling to prevent a user from seeing empty space.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **range**: [`Range`](/lightweight-charts/docs/4.0/api/interfaces/Range)<`number`>

The [logical range](/lightweight-charts/docs/4.0/time-scale#logical-range) to retrieve info for.

#### Returns[​](#returns-3 "Direct link to Returns")

[`BarsInfo`](/lightweight-charts/docs/4.0/api/interfaces/BarsInfo)

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

• **options**: [`SeriesPartialOptionsMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesPartialOptionsMap)[`TSeriesType`]

Any subset of options.

#### Returns[​](#returns-4 "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`SeriesOptionsMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsMap)[`TSeriesType`]>

Returns currently applied options

#### Returns[​](#returns-5 "Direct link to Returns")

`Readonly` <[`SeriesOptionsMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsMap)[`TSeriesType`]>

Full set of currently applied options, including defaults

---

### priceScale()[​](#pricescale "Direct link to priceScale()")

> **priceScale**(): [`IPriceScaleApi`](/lightweight-charts/docs/4.0/api/interfaces/IPriceScaleApi)

Returns interface of the price scale the series is currently attached

#### Returns[​](#returns-6 "Direct link to Returns")

[`IPriceScaleApi`](/lightweight-charts/docs/4.0/api/interfaces/IPriceScaleApi)

IPriceScaleApi object to control the price scale

---

### setData()[​](#setdata "Direct link to setData()")

> **setData**(`data`): `void`

Sets or replaces series data.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **data**: [`SeriesDataItemTypeMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesDataItemTypeMap)[`TSeriesType`][]

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

> **update**(`bar`): `void`

Adds new data item to the existing set (or updates the latest item if times of the passed/latest items are equal).

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **bar**: [`SeriesDataItemTypeMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesDataItemTypeMap)[`TSeriesType`]

A single data item to be added. Time of the new item must be greater or equal to the latest existing time point.
If the new item's time is equal to the last existing item's time, then the existing item is replaced with the new one.

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

### dataByIndex()[​](#databyindex "Direct link to dataByIndex()")

> **dataByIndex**(`logicalIndex`, `mismatchDirection`?): [`SeriesDataItemTypeMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesDataItemTypeMap)[`TSeriesType`]

Returns a bar data by provided logical index.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **logicalIndex**: `number`

Logical index

• **mismatchDirection?**: [`MismatchDirection`](/lightweight-charts/docs/4.0/api/enumerations/MismatchDirection)

Search direction if no data found at provided logical index.

#### Returns[​](#returns-9 "Direct link to Returns")

[`SeriesDataItemTypeMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesDataItemTypeMap)[`TSeriesType`]

Original data item provided via setData or update methods.

#### Example[​](#example "Direct link to Example")

```prism-code
const originalData = series.dataByIndex(10, LightweightCharts.MismatchDirection.NearestLeft);
```

---

### setMarkers()[​](#setmarkers "Direct link to setMarkers()")

> **setMarkers**(`data`): `void`

Allows to set/replace all existing series markers with new ones.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **data**: [`SeriesMarker`](/lightweight-charts/docs/4.0/api/interfaces/SeriesMarker) <[`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)>[]

An array of series markers. This array should be sorted by time. Several markers with same time are allowed.

#### Returns[​](#returns-10 "Direct link to Returns")

`void`

#### Example[​](#example-1 "Direct link to Example")

```prism-code
series.setMarkers([  
    {  
        time: '2019-04-09',  
        position: 'aboveBar',  
        color: 'black',  
        shape: 'arrowDown',  
    },  
    {  
        time: '2019-05-31',  
        position: 'belowBar',  
        color: 'red',  
        shape: 'arrowUp',  
        id: 'id3',  
    },  
    {  
        time: '2019-05-31',  
        position: 'belowBar',  
        color: 'orange',  
        shape: 'arrowUp',  
        id: 'id4',  
        text: 'example',  
        size: 2,  
    },  
]);  
  
chart.subscribeCrosshairMove(param => {  
    console.log(param.hoveredObjectId);  
});  
  
chart.subscribeClick(param => {  
    console.log(param.hoveredObjectId);  
});
```

---

### markers()[​](#markers "Direct link to markers()")

> **markers**(): [`SeriesMarker`](/lightweight-charts/docs/4.0/api/interfaces/SeriesMarker) <[`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)>[]

Returns an array of series markers.

#### Returns[​](#returns-11 "Direct link to Returns")

[`SeriesMarker`](/lightweight-charts/docs/4.0/api/interfaces/SeriesMarker) <[`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)>[]

---

### createPriceLine()[​](#createpriceline "Direct link to createPriceLine()")

> **createPriceLine**(`options`): [`IPriceLine`](/lightweight-charts/docs/4.0/api/interfaces/IPriceLine)

Creates a new price line

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **options**: [`CreatePriceLineOptions`](/lightweight-charts/docs/4.0/api/type-aliases/CreatePriceLineOptions)

Any subset of options, however `price` is required.

#### Returns[​](#returns-12 "Direct link to Returns")

[`IPriceLine`](/lightweight-charts/docs/4.0/api/interfaces/IPriceLine)

#### Example[​](#example-2 "Direct link to Example")

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

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **line**: [`IPriceLine`](/lightweight-charts/docs/4.0/api/interfaces/IPriceLine)

A line to remove.

#### Returns[​](#returns-13 "Direct link to Returns")

`void`

#### Example[​](#example-3 "Direct link to Example")

```prism-code
const priceLine = series.createPriceLine({ price: 80.0 });  
series.removePriceLine(priceLine);
```

---

### seriesType()[​](#seriestype "Direct link to seriesType()")

> **seriesType**(): `TSeriesType`

Return current series type.

#### Returns[​](#returns-14 "Direct link to Returns")

`TSeriesType`

Type of the series.

#### Example[​](#example-4 "Direct link to Example")

```prism-code
const lineSeries = chart.addLineSeries();  
console.log(lineSeries.seriesType()); // "Line"  
  
const candlestickSeries = chart.addCandlestickSeries();  
console.log(candlestickSeries.seriesType()); // "Candlestick"
```