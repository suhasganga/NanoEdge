Version: 5.0

On this page

> **createUpDownMarkers**<`T`>(`series`, `options`?): [`ISeriesUpDownMarkerPluginApi`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesUpDownMarkerPluginApi)<`T`>

Creates and attaches the Series Up Down Markers Plugin.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **T**

## Parameters[​](#parameters "Direct link to Parameters")

• **series**: [`ISeriesApi`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsMap), `T`, [`AreaData`](/lightweight-charts/docs/5.0/api/interfaces/AreaData)<`T`> | [`WhitespaceData`](/lightweight-charts/docs/5.0/api/interfaces/WhitespaceData)<`T`> | [`BarData`](/lightweight-charts/docs/5.0/api/interfaces/BarData)<`T`> | [`CandlestickData`](/lightweight-charts/docs/5.0/api/interfaces/CandlestickData)<`T`> | [`BaselineData`](/lightweight-charts/docs/5.0/api/interfaces/BaselineData)<`T`> | [`LineData`](/lightweight-charts/docs/5.0/api/interfaces/LineData)<`T`> | [`HistogramData`](/lightweight-charts/docs/5.0/api/interfaces/HistogramData)<`T`> | [`CustomData`](/lightweight-charts/docs/5.0/api/interfaces/CustomData)<`T`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/5.0/api/interfaces/CustomSeriesWhitespaceData)<`T`>, [`CustomSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/CustomSeriesOptions) | [`AreaSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/AreaSeriesOptions) | [`BarSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/BarSeriesOptions) | [`CandlestickSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/CandlestickSeriesOptions) | [`BaselineSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/BaselineSeriesOptions) | [`LineSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/LineSeriesOptions) | [`HistogramSeriesOptions`](/lightweight-charts/docs/5.0/api/type-aliases/HistogramSeriesOptions), [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`AreaStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/AreaStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`BarStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/BarStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`CandlestickStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/CandlestickStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`BaselineStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/BaselineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`LineStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/LineStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`HistogramStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/HistogramStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)> | [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`CustomStyleOptions`](/lightweight-charts/docs/5.0/api/interfaces/CustomStyleOptions) & [`SeriesOptionsCommon`](/lightweight-charts/docs/5.0/api/interfaces/SeriesOptionsCommon)>>

Series to which attach the Up Down Markers Plugin

• **options?**: `Partial` <[`UpDownMarkersPluginOptions`](/lightweight-charts/docs/5.0/api/interfaces/UpDownMarkersPluginOptions)>

options for the Up Down Markers Plugin

## Returns[​](#returns "Direct link to Returns")

[`ISeriesUpDownMarkerPluginApi`](/lightweight-charts/docs/5.0/api/interfaces/ISeriesUpDownMarkerPluginApi)<`T`>

Api for Series Up Down Marker Plugin. [ISeriesUpDownMarkerPluginApi](/lightweight-charts/docs/5.0/api/interfaces/ISeriesUpDownMarkerPluginApi)

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