Version: Next

On this page

UpDownMarkersPrimitive Plugin for showing the direction of price changes on the chart.
This plugin can only be used with Line and Area series types.

1. Manual control:

* Use the `setMarkers` method to manually add markers to the chart.
  This will replace any existing markers.
* Use `clearMarkers` to remove all markers.

2. Automatic updates:

Use `setData` and `update` from this primitive instead of the those on the series to let the
primitive handle the creation of price change markers automatically.

* Use `setData` to initialize or replace all data points.
* Use `update` to modify individual data points. This will automatically
  create markers for price changes on existing data points.
* The `updateVisibilityDuration` option controls how long markers remain visible.

## Extends[​](#extends "Direct link to Extends")

* [`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper)<`HorzScaleItem`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

• **TData** *extends* [`SeriesDataItemTypeMap`](/lightweight-charts/docs/next/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[[`UpDownMarkersSupportedSeriesTypes`](/lightweight-charts/docs/next/api/type-aliases/UpDownMarkersSupportedSeriesTypes)] = [`SeriesDataItemTypeMap`](/lightweight-charts/docs/next/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`"Line"`]

## Properties[​](#properties "Direct link to Properties")

### detach()[​](#detach "Direct link to detach()")

> **detach**: () => `void`

Detaches the plugin from the series.

#### Returns[​](#returns "Direct link to Returns")

`void`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper) . [`detach`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper#detach)

---

### getSeries()[​](#getseries "Direct link to getSeries()")

> **getSeries**: () => [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

Returns the current series.

#### Returns[​](#returns-1 "Direct link to Returns")

[`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper) . [`getSeries`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper#getseries)

---

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**: (`options`) => `void`

Applies new options to the plugin.

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: `Partial` <[`UpDownMarkersPluginOptions`](/lightweight-charts/docs/next/api/interfaces/UpDownMarkersPluginOptions)>

Partial options to apply.

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

#### Overrides[​](#overrides "Direct link to Overrides")

[`ISeriesPrimitiveWrapper`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper) . [`applyOptions`](/lightweight-charts/docs/next/api/interfaces/ISeriesPrimitiveWrapper#applyoptions)

---

### setData()[​](#setdata "Direct link to setData()")

> **setData**: (`data`) => `void`

Sets the data for the series and manages data points for marker updates.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **data**: `TData`[]

Array of data points to set.

#### Returns[​](#returns-3 "Direct link to Returns")

`void`

---

### update()[​](#update "Direct link to update()")

> **update**: (`data`, `historicalUpdate`?) => `void`

Updates a single data point and manages marker updates for existing data points.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **data**: `TData`

The data point to update.

• **historicalUpdate?**: `boolean`

Optional flag for historical updates.

#### Returns[​](#returns-4 "Direct link to Returns")

`void`

---

### markers()[​](#markers "Direct link to markers()")

> **markers**: () => readonly [`SeriesUpDownMarker`](/lightweight-charts/docs/next/api/interfaces/SeriesUpDownMarker)<`HorzScaleItem`>[]

Retrieves the current markers on the chart.

#### Returns[​](#returns-5 "Direct link to Returns")

readonly [`SeriesUpDownMarker`](/lightweight-charts/docs/next/api/interfaces/SeriesUpDownMarker)<`HorzScaleItem`>[]

---

### setMarkers()[​](#setmarkers "Direct link to setMarkers()")

> **setMarkers**: (`markers`) => `void`

Manually sets markers on the chart.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **markers**: [`SeriesUpDownMarker`](/lightweight-charts/docs/next/api/interfaces/SeriesUpDownMarker)<`HorzScaleItem`>[]

Array of SeriesUpDownMarker to set.

#### Returns[​](#returns-6 "Direct link to Returns")

`void`

---

### clearMarkers()[​](#clearmarkers "Direct link to clearMarkers()")

> **clearMarkers**: () => `void`

Clears all markers from the chart.

#### Returns[​](#returns-7 "Direct link to Returns")

`void`