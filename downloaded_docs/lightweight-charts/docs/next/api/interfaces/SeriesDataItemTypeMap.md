Version: Next

On this page

Represents the type of data that a series contains.

For example a bar series contains [BarData](/lightweight-charts/docs/next/api/interfaces/BarData) or [WhitespaceData](/lightweight-charts/docs/next/api/interfaces/WhitespaceData).

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### Bar[​](#bar "Direct link to Bar")

> **Bar**: [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/next/api/interfaces/BarData)<`HorzScaleItem`>

The types of bar series data.

---

### Candlestick[​](#candlestick "Direct link to Candlestick")

> **Candlestick**: [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/next/api/interfaces/CandlestickData)<`HorzScaleItem`>

The types of candlestick series data.

---

### Area[​](#area "Direct link to Area")

> **Area**: [`AreaData`](/lightweight-charts/docs/next/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`>

The types of area series data.

---

### Baseline[​](#baseline "Direct link to Baseline")

> **Baseline**: [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/next/api/interfaces/BaselineData)<`HorzScaleItem`>

The types of baseline series data.

---

### Line[​](#line "Direct link to Line")

> **Line**: [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/next/api/interfaces/LineData)<`HorzScaleItem`>

The types of line series data.

---

### Histogram[​](#histogram "Direct link to Histogram")

> **Histogram**: [`WhitespaceData`](/lightweight-charts/docs/next/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/next/api/interfaces/HistogramData)<`HorzScaleItem`>

The types of histogram series data.

---

### Custom[​](#custom "Direct link to Custom")

> **Custom**: [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>

The base types of an custom series data.