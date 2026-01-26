Version: 4.2

On this page

Represents a mouse event.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/4.2/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### time?[​](#time "Direct link to time?")

> `optional` **time**: `HorzScaleItem`

Time of the data at the location of the mouse event.

The value will be `undefined` if the location of the event in the chart is outside the range of available data.

---

### logical?[​](#logical "Direct link to logical?")

> `optional` **logical**: [`Logical`](/lightweight-charts/docs/4.2/api/type-aliases/Logical)

Logical index

---

### point?[​](#point "Direct link to point?")

> `optional` **point**: [`Point`](/lightweight-charts/docs/4.2/api/interfaces/Point)

Location of the event in the chart.

The value will be `undefined` if the event is fired outside the chart, for example a mouse leave event.

---

### seriesData[​](#seriesdata "Direct link to seriesData")

> **seriesData**: `Map` <[`ISeriesApi`](/lightweight-charts/docs/4.2/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/4.2/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/4.2/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.2/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.2/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.2/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.2/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.2/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/4.2/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/4.2/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/AreaSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/BaselineSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/CandlestickSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/HistogramSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/LineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)>>, [`BarData`](/lightweight-charts/docs/4.2/api/interfaces/BarData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.2/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.2/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/4.2/api/interfaces/CustomData)<`HorzScaleItem`>>

Data of all series at the location of the event in the chart.

Keys of the map are [ISeriesApi](/lightweight-charts/docs/4.2/api/interfaces/ISeriesApi) instances. Values are prices.
Values of the map are original data items

---

### hoveredSeries?[​](#hoveredseries "Direct link to hoveredSeries?")

> `optional` **hoveredSeries**: [`ISeriesApi`](/lightweight-charts/docs/4.2/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/4.2/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/4.2/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.2/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.2/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.2/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.2/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.2/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/4.2/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/4.2/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/AreaSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/BaselineSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/CandlestickSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/HistogramSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/4.2/api/type-aliases/LineSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/4.2/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/4.2/api/interfaces/SeriesOptionsCommon)>>

The [ISeriesApi](/lightweight-charts/docs/4.2/api/interfaces/ISeriesApi) for the series at the point of the mouse event.

---

### hoveredObjectId?[​](#hoveredobjectid "Direct link to hoveredObjectId?")

> `optional` **hoveredObjectId**: `unknown`

The ID of the object at the point of the mouse event.

---

### sourceEvent?[​](#sourceevent "Direct link to sourceEvent?")

> `optional` **sourceEvent**: [`TouchMouseEventData`](/lightweight-charts/docs/4.2/api/interfaces/TouchMouseEventData)

The underlying source mouse or touch event data, if available