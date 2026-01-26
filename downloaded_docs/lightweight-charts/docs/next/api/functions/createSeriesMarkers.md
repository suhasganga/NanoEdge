Version: Next

On this page

> **createSeriesMarkers**<`HorzScaleItem`>(`series`, `markers`?, `options`?): [`ISeriesMarkersPluginApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesMarkersPluginApi)<`HorzScaleItem`>

A function to create a series markers primitive.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Parameters[​](#parameters "Direct link to Parameters")

• **series**: [`ISeriesApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsMap), `HorzScaleItem`, [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>, [`CustomSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/next/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/next/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/next/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/next/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/next/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/next/api/interfaces/SeriesOptionsCommon)>>

The series to which the primitive will be attached.

• **markers?**: [`SeriesMarker`](/lightweight-charts/docs/next/api/type-aliases/SeriesMarker)<`HorzScaleItem`>[]

An array of markers to be displayed on the series.

• **options?**: [`DeepPartial`](/lightweight-charts/docs/next/api/type-aliases/DeepPartial) <[`SeriesMarkersOptions`](/lightweight-charts/docs/next/api/interfaces/SeriesMarkersOptions)>

Options for the series markers plugin.

## Returns[​](#returns "Direct link to Returns")

[`ISeriesMarkersPluginApi`](/lightweight-charts/docs/next/api/interfaces/ISeriesMarkersPluginApi)<`HorzScaleItem`>

## Example[​](#example "Direct link to Example")

```prism-code
import { createSeriesMarkers } from 'lightweight-charts';  
  
    const seriesMarkers = createSeriesMarkers(  
        series,  
        [  
            {  
                color: 'green',  
                position: 'inBar',  
                shape: 'arrowDown',  
                time: 1556880900,  
            },  
        ]  
    );  
 // and then you can modify the markers  
 // set it to empty array to remove all markers  
 seriesMarkers.setMarkers([]);  
  
 // `seriesMarkers.markers()` returns current markers
```