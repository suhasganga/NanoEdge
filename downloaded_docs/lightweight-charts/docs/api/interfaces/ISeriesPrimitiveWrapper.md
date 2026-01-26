Version: 5.1

On this page

Interface for a series primitive.

## Extended by[​](#extended-by "Direct link to Extended by")

* [`ISeriesMarkersPluginApi`](/lightweight-charts/docs/api/interfaces/ISeriesMarkersPluginApi)
* [`ISeriesUpDownMarkerPluginApi`](/lightweight-charts/docs/api/interfaces/ISeriesUpDownMarkerPluginApi)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

• **Options** = `unknown`

## Properties[​](#properties "Direct link to Properties")

### detach()[​](#detach "Direct link to detach()")

> **detach**: () => `void`

Detaches the plugin from the series.

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### getSeries()[​](#getseries "Direct link to getSeries()")

> **getSeries**: () => [`ISeriesApi`](/lightweight-charts/docs/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/api/interfaces/SeriesOptionsMap), `T`, [`AreaData`](/lightweight-charts/docs/api/interfaces/AreaData)<`T`> | [`WhitespaceData`](/lightweight-charts/docs/api/interfaces/WhitespaceData)<`T`> | [`BarData`](/lightweight-charts/docs/api/interfaces/BarData)<`T`> | [`CandlestickData`](/lightweight-charts/docs/api/interfaces/CandlestickData)<`T`> | [`BaselineData`](/lightweight-charts/docs/api/interfaces/BaselineData)<`T`> | [`LineData`](/lightweight-charts/docs/api/interfaces/LineData)<`T`> | [`HistogramData`](/lightweight-charts/docs/api/interfaces/HistogramData)<`T`> | [`CustomData`](/lightweight-charts/docs/api/interfaces/CustomData)<`T`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/api/interfaces/CustomSeriesWhitespaceData)<`T`>, [`CustomSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)>>

Returns the current series.

#### Returns[​](#returns-1 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/api/interfaces/SeriesOptionsMap), `T`, [`AreaData`](/lightweight-charts/docs/api/interfaces/AreaData)<`T`> | [`WhitespaceData`](/lightweight-charts/docs/api/interfaces/WhitespaceData)<`T`> | [`BarData`](/lightweight-charts/docs/api/interfaces/BarData)<`T`> | [`CandlestickData`](/lightweight-charts/docs/api/interfaces/CandlestickData)<`T`> | [`BaselineData`](/lightweight-charts/docs/api/interfaces/BaselineData)<`T`> | [`LineData`](/lightweight-charts/docs/api/interfaces/LineData)<`T`> | [`HistogramData`](/lightweight-charts/docs/api/interfaces/HistogramData)<`T`> | [`CustomData`](/lightweight-charts/docs/api/interfaces/CustomData)<`T`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/api/interfaces/CustomSeriesWhitespaceData)<`T`>, [`CustomSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)>>

---

### applyOptions()?[​](#applyoptions "Direct link to applyOptions()?")

> `optional` **applyOptions**: (`options`) => `void`

Applies options to the primitive.

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial)<`Options`>

Options to apply. The options are deeply merged with the current options.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`