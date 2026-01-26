Version: 4.2

On this page

Represents the interface for interacting with price lines.

## Methods[​](#methods "Direct link to Methods")

### applyOptions()[​](#applyoptions "Direct link to applyOptions()")

> **applyOptions**(`options`): `void`

Apply options to the price line.

#### Parameters[​](#parameters "Direct link to Parameters")

• **options**: `Partial` <[`PriceLineOptions`](/lightweight-charts/docs/4.2/api/interfaces/PriceLineOptions)>

Any subset of options.

#### Returns[​](#returns "Direct link to Returns")

`void`

#### Example[​](#example "Direct link to Example")

```prism-code
priceLine.applyOptions({  
    price: 90.0,  
    color: 'red',  
    lineWidth: 3,  
    lineStyle: LightweightCharts.LineStyle.Dashed,  
    axisLabelVisible: false,  
    title: 'P/L 600',  
});
```

---

### options()[​](#options "Direct link to options()")

> **options**(): `Readonly` <[`PriceLineOptions`](/lightweight-charts/docs/4.2/api/interfaces/PriceLineOptions)>

Get the currently applied options.

#### Returns[​](#returns-1 "Direct link to Returns")

`Readonly` <[`PriceLineOptions`](/lightweight-charts/docs/4.2/api/interfaces/PriceLineOptions)>