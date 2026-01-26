Version: 5.1

On this page

> **createUpDownMarkers**<`T`>(`series`, `options`?): [`ISeriesUpDownMarkerPluginApi`](/lightweight-charts/docs/api/interfaces/ISeriesUpDownMarkerPluginApi)<`T`>

Creates and attaches the Series Up Down Markers Plugin.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](#parameters "Direct link to Parameters")

• **series**: [`ISeriesApi`](/lightweight-charts/docs/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/api/interfaces/SeriesOptionsMap), `T`, [`AreaData`](/lightweight-charts/docs/api/interfaces/AreaData)<`T`> | [`WhitespaceData`](/lightweight-charts/docs/api/interfaces/WhitespaceData)<`T`> | [`BarData`](/lightweight-charts/docs/api/interfaces/BarData)<`T`> | [`CandlestickData`](/lightweight-charts/docs/api/interfaces/CandlestickData)<`T`> | [`BaselineData`](/lightweight-charts/docs/api/interfaces/BaselineData)<`T`> | [`LineData`](/lightweight-charts/docs/api/interfaces/LineData)<`T`> | [`HistogramData`](/lightweight-charts/docs/api/interfaces/HistogramData)<`T`> | [`CustomData`](/lightweight-charts/docs/api/interfaces/CustomData)<`T`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/api/interfaces/CustomSeriesWhitespaceData)<`T`>, [`CustomSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/api/interfaces/SeriesOptionsCommon)>>

Series to which attach the Up Down Markers Plugin

• **options?**: `Partial` <[`UpDownMarkersPluginOptions`](/lightweight-charts/docs/api/interfaces/UpDownMarkersPluginOptions)>

options for the Up Down Markers Plugin

## Returns[​](#returns "Direct link to Returns")

[`ISeriesUpDownMarkerPluginApi`](/lightweight-charts/docs/api/interfaces/ISeriesUpDownMarkerPluginApi)<`T`>

Api for Series Up Down Marker Plugin. [ISeriesUpDownMarkerPluginApi](/lightweight-charts/docs/api/interfaces/ISeriesUpDownMarkerPluginApi)

## Example[​](#example "Direct link to Example")

```prism-code
import { createUpDownMarkers, createChart, LineSeries } from 'lightweight-charts';  
  
const chart = createChart('container');  
const lineSeries = chart.addSeries(LineSeries);  
const upDownMarkers = createUpDownMarkers(lineSeries, {  
    positiveColor: '#22AB94',  
    negativeColor: '#F7525F',  
    updateVisibilityDuration: 5000,  
});  
// to add some data  
upDownMarkers.setData(  
    [  
        { time: '2020-02-02', value: 12.34 },  
        //... more line series data  
    ]  
);  
// ... Update some values  
upDownMarkers.update({ time: '2020-02-02', value: 13.54 }, true);  
// to remove plugin from the series  
upDownMarkers.detach();
```