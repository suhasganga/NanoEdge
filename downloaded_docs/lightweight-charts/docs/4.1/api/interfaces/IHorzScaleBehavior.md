Version: 4.1

On this page

Class interface for Horizontal scale behavior

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Methods[​](#methods "Direct link to Methods")

### options()[​](#options "Direct link to options()")

> **options**(): [`ChartOptionsImpl`](/lightweight-charts/docs/4.1/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>

Structure describing options of the chart.

#### Returns[​](#returns "Direct link to Returns")

[`ChartOptionsImpl`](/lightweight-charts/docs/4.1/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>

ChartOptionsBase

---

### setOptions()[​](#setoptions "Direct link to setOptions()")

> **setOptions**(`options`): `void`

Set the chart options. Note that this is different to `applyOptions` since the provided options will overwrite the current options
instead of merging with the current options.

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: [`ChartOptionsImpl`](/lightweight-charts/docs/4.1/api/interfaces/ChartOptionsImpl)<`HorzScaleItem`>

Chart options to be set

#### Returns[​](#returns-1 "Direct link to Returns")

`void`

void

---

### preprocessData()[​](#preprocessdata "Direct link to preprocessData()")

> **preprocessData**(`data`): `void`

Method to preprocess the data.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **data**: [`DataItem`](/lightweight-charts/docs/4.1/api/type-aliases/DataItem)<`HorzScaleItem`> | [`DataItem`](/lightweight-charts/docs/4.1/api/type-aliases/DataItem)<`HorzScaleItem`>[]

Data items for the series

#### Returns[​](#returns-2 "Direct link to Returns")

`void`

void

---

### convertHorzItemToInternal()[​](#converthorzitemtointernal "Direct link to convertHorzItemToInternal()")

> **convertHorzItemToInternal**(`item`): `object`

Convert horizontal scale item into an internal horizontal scale item.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **item**: `HorzScaleItem`

item to be converted

#### Returns[​](#returns-3 "Direct link to Returns")

`object`

InternalHorzScaleItem

##### [species][​](#species "Direct link to [species]")

> **[species]**: `"InternalHorzScaleItem"`

The 'name' or species of the nominal.

---

### createConverterToInternalObj()[​](#createconvertertointernalobj "Direct link to createConverterToInternalObj()")

> **createConverterToInternalObj**(`data`): [`HorzScaleItemConverterToInternalObj`](/lightweight-charts/docs/4.1/api/type-aliases/HorzScaleItemConverterToInternalObj)<`HorzScaleItem`>

Creates and returns a converter for changing series data into internal horizontal scale items.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

• **data**: ([`AreaData`](/lightweight-charts/docs/4.1/api/interfaces/AreaData)<`HorzScaleItem`> | [`WhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/WhitespaceData)<`HorzScaleItem`> | [`BarData`](/lightweight-charts/docs/4.1/api/interfaces/BarData)<`HorzScaleItem`> | [`CandlestickData`](/lightweight-charts/docs/4.1/api/interfaces/CandlestickData)<`HorzScaleItem`> | [`BaselineData`](/lightweight-charts/docs/4.1/api/interfaces/BaselineData)<`HorzScaleItem`> | [`LineData`](/lightweight-charts/docs/4.1/api/interfaces/LineData)<`HorzScaleItem`> | [`HistogramData`](/lightweight-charts/docs/4.1/api/interfaces/HistogramData)<`HorzScaleItem`> | [`CustomData`](/lightweight-charts/docs/4.1/api/interfaces/CustomData)<`HorzScaleItem`> | [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/4.1/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>)[]

series data

#### Returns[​](#returns-4 "Direct link to Returns")

[`HorzScaleItemConverterToInternalObj`](/lightweight-charts/docs/4.1/api/type-aliases/HorzScaleItemConverterToInternalObj)<`HorzScaleItem`>

HorzScaleItemConverterToInternalObj

---

### key()[​](#key "Direct link to key()")

> **key**(`internalItem`): [`InternalHorzScaleItemKey`](/lightweight-charts/docs/4.1/api/type-aliases/InternalHorzScaleItemKey)

Returns the key for the specified horizontal scale item.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

• **internalItem**: `HorzScaleItem` | `object`

horizontal scale item for which the key should be returned

#### Returns[​](#returns-5 "Direct link to Returns")

[`InternalHorzScaleItemKey`](/lightweight-charts/docs/4.1/api/type-aliases/InternalHorzScaleItemKey)

InternalHorzScaleItemKey

---

### cacheKey()[​](#cachekey "Direct link to cacheKey()")

> **cacheKey**(`internalItem`): `number`

Returns the cache key for the specified horizontal scale item.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

• **internalItem**

horizontal scale item for which the cache key should be returned

• **internalItem.[species]**: `"InternalHorzScaleItem"`

The 'name' or species of the nominal.

#### Returns[​](#returns-6 "Direct link to Returns")

`number`

number

---

### updateFormatter()[​](#updateformatter "Direct link to updateFormatter()")

> **updateFormatter**(`options`): `void`

Update the formatter with the localization options.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

• **options**: [`LocalizationOptions`](/lightweight-charts/docs/4.1/api/interfaces/LocalizationOptions)<`HorzScaleItem`>

Localization options

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

void

---

### formatHorzItem()[​](#formathorzitem "Direct link to formatHorzItem()")

> **formatHorzItem**(`item`): `string`

Format the horizontal scale item into a display string.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

• **item**

horizontal scale item to be formatted as a string

• **item.[species]**: `"InternalHorzScaleItem"`

The 'name' or species of the nominal.

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

string

---

### formatTickmark()[​](#formattickmark "Direct link to formatTickmark()")

> **formatTickmark**(`item`, `localizationOptions`): `string`

Format the horizontal scale tickmark into a display string.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

• **item**: [`TickMark`](/lightweight-charts/docs/4.1/api/interfaces/TickMark)

tickmark item

• **localizationOptions**: [`LocalizationOptions`](/lightweight-charts/docs/4.1/api/interfaces/LocalizationOptions)<`HorzScaleItem`>

Localization options

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

string

---

### maxTickMarkWeight()[​](#maxtickmarkweight "Direct link to maxTickMarkWeight()")

> **maxTickMarkWeight**(`marks`): [`TickMarkWeightValue`](/lightweight-charts/docs/4.1/api/type-aliases/TickMarkWeightValue)

Returns the maximum tickmark weight value for the specified tickmarks on the time scale.

#### Parameters[​](#parameters-9 "Direct link to Parameters")

• **marks**: [`TimeMark`](/lightweight-charts/docs/4.1/api/interfaces/TimeMark)[]

Timescale tick marks

#### Returns[​](#returns-10 "Direct link to Returns")

[`TickMarkWeightValue`](/lightweight-charts/docs/4.1/api/type-aliases/TickMarkWeightValue)

TickMarkWeightValue

---

### fillWeightsForPoints()[​](#fillweightsforpoints "Direct link to fillWeightsForPoints()")

> **fillWeightsForPoints**(`sortedTimePoints`, `startIndex`): `void`

Fill the weights for the sorted time scale points.

#### Parameters[​](#parameters-10 "Direct link to Parameters")

• **sortedTimePoints**: readonly [`Mutable`](/lightweight-charts/docs/4.1/api/type-aliases/Mutable) <[`TimeScalePoint`](/lightweight-charts/docs/4.1/api/interfaces/TimeScalePoint)>[]

sorted time scale points

• **startIndex**: `number`

starting index

#### Returns[​](#returns-11 "Direct link to Returns")

`void`

void

---

### shouldResetTickmarkLabels()?[​](#shouldresettickmarklabels "Direct link to shouldResetTickmarkLabels()?")

> `optional` **shouldResetTickmarkLabels**(`tickMarks`): `boolean`

If returns true, then the tick mark formatter will be called for all the visible
tick marks even if the formatter has previously been called for a specific tick mark.
This allows you to change the formatting on all the tick marks.

#### Parameters[​](#parameters-11 "Direct link to Parameters")

• **tickMarks**: readonly [`TickMark`](/lightweight-charts/docs/4.1/api/interfaces/TickMark)[]

array of tick marks

#### Returns[​](#returns-12 "Direct link to Returns")

`boolean`

boolean