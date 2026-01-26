Version: 5.1

On this page

Interface to control chart's price scale

## Methods[​](#methods "Direct link to Methods")

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the price scale

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/api/type-aliases/DeepPartial) <[`PriceScaleOptions`](/lightweight-charts/docs/api/interfaces/PriceScaleOptions)>

Any subset of options.

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`PriceScaleOptions`](/lightweight-charts/docs/api/interfaces/PriceScaleOptions)>

Returns currently applied options of the price scale

#### Returns[​](#returns-1 "Direct link to Returns")

`Readonly` <[`PriceScaleOptions`](/lightweight-charts/docs/api/interfaces/PriceScaleOptions)>

Full set of currently applied options, including defaults

---

### width()[​](#width "Direct link to width()")

> **width**(): `number`

Returns a width of the price scale if it's visible or 0 if invisible.

#### Returns[​](#returns-2 "Direct link to Returns")

`number`

---

### setVisibleRange()[​](#setvisiblerange "Direct link to setVisibleRange()")

> **setVisibleRange**(`range`): `void`

Sets the visible range of the price scale.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **range**: [`IRange`](/lightweight-charts/docs/api/interfaces/IRange)<`number`>

The visible range to set, with `from` and `to` properties.

#### Returns[​](#returns-3 "Direct link to Returns")

`void`

---

### getVisibleRange()[​](#getvisiblerange "Direct link to getVisibleRange()")

> **getVisibleRange**(): [`IRange`](/lightweight-charts/docs/api/interfaces/IRange)<`number`>

Returns the visible range of the price scale.

#### Returns[​](#returns-4 "Direct link to Returns")

[`IRange`](/lightweight-charts/docs/api/interfaces/IRange)<`number`>

The visible range of the price scale, or null if the range is not set.

---

### setAutoScale()[​](#setautoscale "Direct link to setAutoScale()")

> **setAutoScale**(`on`): `void`

Sets the auto scale mode of the price scale.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

• **on**: `boolean`

If true, enables auto scaling; if false, disables it.

#### Returns[​](#returns-5 "Direct link to Returns")

`void`