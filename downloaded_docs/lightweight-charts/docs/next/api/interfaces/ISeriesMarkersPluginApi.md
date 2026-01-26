Version: Next

On this page

Interface for a series markers plugin

## Extends[​](#extends "Direct link to Extends")

* [`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper)<`HorzScaleItem`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](#properties "Direct link to Properties")

### setMarkers()[​](#setmarkers "Direct link to setMarkers()")

> **setMarkers**: (`markers`) => `void`

Set markers to the series.

#### Parameters[​](#parameters "Direct link to Parameters")

• **markers**: [`SeriesMarker`](/lightweight-charts/docs/next/api/type-aliases/SeriesMarker)<`HorzScaleItem`>[]

An array of markers to be displayed on the series.

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### markers()[​](#markers "Direct link to markers()")

> **markers**: () => readonly [`SeriesMarker`](/lightweight-charts/docs/next/api/type-aliases/SeriesMarker)<`HorzScaleItem`>[]

Returns current markers.

#### Returns[​](#returns-1 "Direct link to Returns")

readonly [`SeriesMarker`](/lightweight-charts/docs/next/api/type-aliases/SeriesMarker)<`HorzScaleItem`>[]

---

### detach()[​](#detach "Direct link to detach()")

> **detach**: () => `void`

Detaches the plugin from the series.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

#### Overrides[​](#overrides "Direct link to Overrides")

[`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper) . [`detach`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper#detach)

---

### getSeries()[​](#getseries "Direct link to getSeries()")

> **getSeries**: () => [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

Returns the current series.

#### Returns[​](#returns-3 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper) . [`getSeries`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper#getseries)

---

### applyOptions()?[​](#applyoptions "Direct link to applyOptions()?")

> `optional` **applyOptions**: (`options`) => `void`

Applies options to the primitive.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial)<`unknown`>

Options to apply. The options are deeply merged with the current options.

#### Returns[​](#returns-4 "Direct link to Returns")

`void`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper) . [`applyOptions`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper#applyoptions)