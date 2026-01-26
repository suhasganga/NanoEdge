Version: 4.1

On this page

Object containing references to the chart and series instances, and a requestUpdate method for triggering
a refresh of the chart.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/4.1/api/type-aliases/Time)

• **TSeriesType** *extends* [`SeriesType`](/lightweight-charts/docs/4.1/api/type-aliases/SeriesType) = keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsMap)

## Properties[​](#properties "Direct link to Properties")

### chart[​](#chart "Direct link to chart")

> **chart**: [`IChartApiBase`](/lightweight-charts/docs/4.1/api/interfaces/IChartApiBase)<`HorzScaleItem`>

Chart instance.

---

### series[​](#series "Direct link to series")

> **series**: [`ISeriesApi`](/lightweight-charts/docs/4.1/api/interfaces/ISeriesApi)<`TSeriesType`, `HorzScaleItem`, [`SeriesDataItemTypeMap`](/lightweight-charts/docs/4.1/api/interfaces/SeriesDataItemTypeMap)<`HorzScaleItem`>[`TSeriesType`], [`SeriesOptionsMap`](/lightweight-charts/docs/4.1/api/interfaces/SeriesOptionsMap)[`TSeriesType`], [`SeriesPartialOptionsMap`](/lightweight-charts/docs/4.1/api/interfaces/SeriesPartialOptionsMap)[`TSeriesType`]>

Series to which the Primitive is attached.

---

### requestUpdate()[​](#requestupdate "Direct link to requestUpdate()")

> **requestUpdate**: () => `void`

Request an update (redraw the chart)

#### Returns[​](#returns "Direct link to Returns")

`void`