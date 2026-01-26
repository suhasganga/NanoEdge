Version: 5.1

On this page

> **createYieldCurveChart**(`container`, `options`?): [`IYieldCurveChartApi`](/lightweight-charts/docs/api/interfaces/IYieldCurveChartApi)

Creates a yield curve chart with the specified options.

A yield curve chart differs from the default chart type
in the following ways:

* Horizontal scale is linearly spaced, and defined in monthly
  time duration units
* Whitespace is ignored for the crosshair and grid lines

## Parameters[​](#parameters "Direct link to Parameters")

• **container**: `string` | `HTMLElement`

ID of HTML element or element itself

• **options?**: [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`YieldCurveChartOptions`](/lightweight-charts/docs/api/interfaces/YieldCurveChartOptions)>

The yield chart options.

## Returns[​](#returns "Direct link to Returns")

[`IYieldCurveChartApi`](/lightweight-charts/docs/api/interfaces/IYieldCurveChartApi)

An interface to the created chart