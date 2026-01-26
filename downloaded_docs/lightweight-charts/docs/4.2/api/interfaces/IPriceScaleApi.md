Version: 4.2

On this page

Interface to control chart's price scale

## Methods[​](#methods "Direct link to Methods")

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Applies new options to the price scale

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: [`DeepPartial`](/lightweight-charts/docs/4.2/api/type-aliases/DeepPartial) <[`PriceScaleOptions`](/lightweight-charts/docs/4.2/api/interfaces/PriceScaleOptions)>

Any subset of options.

#### Returns[​](#returns "Direct link to Returns")

`void`

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`PriceScaleOptions`](/lightweight-charts/docs/4.2/api/interfaces/PriceScaleOptions)>

Returns currently applied options of the price scale

#### Returns[​](#returns-1 "Direct link to Returns")

`Readonly` <[`PriceScaleOptions`](/lightweight-charts/docs/4.2/api/interfaces/PriceScaleOptions)>

Full set of currently applied options, including defaults

---

### width()[​](#width "Direct link to width()")

> **width**(): `number`

Returns a width of the price scale if it's visible or 0 if invisible.

#### Returns[​](#returns-2 "Direct link to Returns")

`number`