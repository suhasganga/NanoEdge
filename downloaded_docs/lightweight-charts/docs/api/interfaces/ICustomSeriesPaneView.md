Version: 5.1

On this page

This interface represents the view for the custom series

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/api/type-aliases/Time)

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/api/interfaces/CustomData)<`HorzScaleItem`> = [`CustomData`](/lightweight-charts/docs/api/interfaces/CustomData)<`HorzScaleItem`>

• **TSeriesOptions** *extends* [`CustomSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CustomSeriesOptions) = [`CustomSeriesOptions`](/lightweight-charts/docs/api/type-aliases/CustomSeriesOptions)

## Methods[​](#methods "Direct link to Methods")

### renderer()[​](#renderer "Direct link to renderer()")

> **renderer**(): [`ICustomSeriesPaneRenderer`](/lightweight-charts/docs/api/interfaces/ICustomSeriesPaneRenderer)

This method returns a renderer - special object to draw data for the series
on the main chart pane.

#### Returns[​](#returns "Direct link to Returns")

[`ICustomSeriesPaneRenderer`](/lightweight-charts/docs/api/interfaces/ICustomSeriesPaneRenderer)

an renderer object to be used for drawing.

---

### update()[​](#update "Direct link to update()")

> **update**(`data`, `seriesOptions`): `void`

This method will be called with the latest data for the renderer to use
during the next paint.

#### Parameters[​](#parameters "Direct link to Parameters")

• **data**: [`PaneRendererCustomData`](/lightweight-charts/docs/api/interfaces/PaneRendererCustomData)<`HorzScaleItem`, `TData`>

• **seriesOptions**: `TSeriesOptions`

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

---

### priceValueBuilder()[​](#pricevaluebuilder "Direct link to priceValueBuilder()")

> **priceValueBuilder**(`plotRow`): [`CustomSeriesPricePlotValues`](/lightweight-charts/docs/api/type-aliases/CustomSeriesPricePlotValues)

A function for interpreting the custom series data and returning an array of numbers
representing the price values for the item. These price values are used
by the chart to determine the auto-scaling (to ensure the items are in view) and the crosshair
and price line positions. The last value in the array will be used as the current value. You shouldn't need to
have more than 3 values in this array since the library only needs a largest, smallest, and current value.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **plotRow**: `TData`

#### Returns[​](#returns-2 "Direct link to Returns")

[`CustomSeriesPricePlotValues`](/lightweight-charts/docs/api/type-aliases/CustomSeriesPricePlotValues)

---

### isWhitespace()[​](#iswhitespace "Direct link to isWhitespace()")

> **isWhitespace**(`data`): `data is CustomSeriesWhitespaceData<HorzScaleItem>`

A function for testing whether a data point should be considered fully specified, or if it should
be considered as whitespace. Should return `true` if is whitespace.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **data**: `TData` | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>

data point to be tested

#### Returns[​](#returns-3 "Direct link to Returns")

`data is CustomSeriesWhitespaceData<HorzScaleItem>`

---

### defaultOptions()[​](#defaultoptions "Direct link to defaultOptions()")

> **defaultOptions**(): `TSeriesOptions`

Default options

#### Returns[​](#returns-4 "Direct link to Returns")

`TSeriesOptions`

---

### destroy()?[​](#destroy "Direct link to destroy()?")

> `optional` **destroy**(): `void`

This method will be evoked when the series has been removed from the chart. This method should be used to
clean up any objects, references, and other items that could potentially cause memory leaks.

This method should contain all the necessary code to clean up the object before it is removed from memory.
This includes removing any event listeners or timers that are attached to the object, removing any references
to other objects, and resetting any values or properties that were modified during the lifetime of the object.

#### Returns[​](#returns-5 "Direct link to Returns")

`void`

---

### conflationReducer()?[​](#conflationreducer "Direct link to conflationReducer()?")

> `optional` **conflationReducer**(`item1`, `item2`): `TData`

Optional reducer used for conflation of custom data points.
Given exactly 2 custom data contexts, should return a single aggregated item.
Each context provides access to the original data plus metadata needed for conflation.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **item1**: [`CustomConflationContext`](/lightweight-charts/docs/api/interfaces/CustomConflationContext)<`HorzScaleItem`, `TData`>

• **item2**: [`CustomConflationContext`](/lightweight-charts/docs/api/interfaces/CustomConflationContext)<`HorzScaleItem`, `TData`>

#### Returns[​](#returns-6 "Direct link to Returns")

`TData`