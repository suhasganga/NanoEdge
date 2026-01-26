Version: 4.0

On this page

Represents a mouse event.

## Properties[​](#properties "Direct link to Properties")

### time?[​](#time "Direct link to time?")

> `optional` **time**: [`Time`](/lightweight-charts/docs/4.0/api/type-aliases/Time)

Time of the data at the location of the mouse event.

The value will be `undefined` if the location of the event in the chart is outside the range of available data.

---

### logical?[​](#logical "Direct link to logical?")

> `optional` **logical**: [`Logical`](/lightweight-charts/docs/4.0/api/type-aliases/Logical)

Logical index

---

### point?[​](#point "Direct link to point?")

> `optional` **point**: [`Point`](/lightweight-charts/docs/4.0/api/interfaces/Point)

Location of the event in the chart.

The value will be `undefined` if the event is fired outside the chart, for example a mouse leave event.

---

### seriesData[​](#seriesdata "Direct link to seriesData")

> **seriesData**: `Map` <[`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsMap)>, [`BarData`](/lightweight-charts/docs/4.0/api/interfaces/BarData) | [`HistogramData`](/lightweight-charts/docs/4.0/api/interfaces/HistogramData) | [`LineData`](/lightweight-charts/docs/4.0/api/interfaces/LineData)>

Data of all series at the location of the event in the chart.

Keys of the map are [ISeriesApi](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi) instances. Values are prices.
Values of the map are original data items

---

### hoveredSeries?[​](#hoveredseries "Direct link to hoveredSeries?")

> `optional` **hoveredSeries**: [`ISeriesApi`](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/4.0/api/interfaces/SeriesOptionsMap)>

The [ISeriesApi](/lightweight-charts/docs/4.0/api/interfaces/ISeriesApi) for the series at the point of the mouse event.

---

### hoveredObjectId?[​](#hoveredobjectid "Direct link to hoveredObjectId?")

> `optional` **hoveredObjectId**: `unknown`

The ID of the object at the point of the mouse event.

---

### sourceEvent?[​](#sourceevent "Direct link to sourceEvent?")

> `optional` **sourceEvent**: [`TouchMouseEventData`](/lightweight-charts/docs/4.0/api/interfaces/TouchMouseEventData)

The underlying source mouse or touch event data, if available