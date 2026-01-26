Version: 3.8

On this page

Represents a mouse event.

## Properties[​](#properties "Direct link to Properties")

### time?[​](#time "Direct link to time?")

> `optional` **time**: [`UTCTimestamp`](/lightweight-charts/docs/3.8/api/type-aliases/UTCTimestamp) | [`BusinessDay`](/lightweight-charts/docs/3.8/api/interfaces/BusinessDay)

Time of the data at the location of the mouse event.

The value will be `undefined` if the location of the event in the chart is outside the range of available data.

---

### point?[​](#point "Direct link to point?")

> `optional` **point**: [`Point`](/lightweight-charts/docs/3.8/api/interfaces/Point)

Location of the event in the chart.

The value will be `undefined` if the event is fired outside the chart, for example a mouse leave event.

---

### seriesPrices[​](#seriesprices "Direct link to seriesPrices")

> **seriesPrices**: `Map` <[`ISeriesApi`](/lightweight-charts/docs/3.8/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/3.8/api/interfaces/SeriesOptionsMap)>, [`BarPrice`](/lightweight-charts/docs/3.8/api/type-aliases/BarPrice) | [`BarPrices`](/lightweight-charts/docs/3.8/api/interfaces/BarPrices)>

Prices of all series at the location of the event in the chart.

Keys of the map are [ISeriesApi](/lightweight-charts/docs/3.8/api/interfaces/ISeriesApi) instances. Values are prices.
Each price is a number for line, area, and histogram series or a OHLC object for candlestick and bar series.

---

### hoveredSeries?[​](#hoveredseries "Direct link to hoveredSeries?")

> `optional` **hoveredSeries**: [`ISeriesApi`](/lightweight-charts/docs/3.8/api/interfaces/ISeriesApi)<keyof [`SeriesOptionsMap`](/lightweight-charts/docs/3.8/api/interfaces/SeriesOptionsMap)>

The [ISeriesApi](/lightweight-charts/docs/3.8/api/interfaces/ISeriesApi) for the series at the point of the mouse event.

---

### hoveredMarkerId?[​](#hoveredmarkerid "Direct link to hoveredMarkerId?")

> `optional` **hoveredMarkerId**: `string`

The ID of the marker at the point of the mouse event.