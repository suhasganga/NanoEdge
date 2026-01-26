Version: 5.0

On this page

> **createOptionsChart**(`container`, `options`?): [`IChartApiBase`](/lightweight-charts/docs/5.0/api/interfaces/IChartApiBase)<`number`>

Creates an 'options' chart with price values on the horizontal scale.

This function is used to create a specialized chart type where the horizontal scale
represents price values instead of time. It's particularly useful for visualizing
option chains, price distributions, or any data where price is the primary x-axis metric.

## Parameters[​](#parameters "Direct link to Parameters")

• **container**: `string` | `HTMLElement`

The DOM element or its id where the chart will be rendered.

• **options?**: [`DeepPartial`](/lightweight-charts/docs/5.0/api/type-aliases/DeepPartial) <[`PriceChartOptions`](/lightweight-charts/docs/5.0/api/interfaces/PriceChartOptions)>

Optional configuration options for the price chart.

## Returns[​](#returns "Direct link to Returns")

[`IChartApiBase`](/lightweight-charts/docs/5.0/api/interfaces/IChartApiBase)<`number`>

An instance of IChartApiBase configured for price-based horizontal scaling.