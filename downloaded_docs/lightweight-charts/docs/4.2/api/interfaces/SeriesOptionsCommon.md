Version: 4.2

On this page

Represents options common for all types of series

## Properties[​](#properties "Direct link to Properties")

### lastValueVisible[​](#lastvaluevisible "Direct link to lastValueVisible")

> **lastValueVisible**: `boolean`

Visibility of the label with the latest visible price on the price scale.

#### Default Value[​](#default-value "Direct link to Default Value")

`true`

---

### title[​](#title "Direct link to title")

> **title**: `string`

You can name series when adding it to a chart. This name will be displayed on the label next to the last value label.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`''`

---

### priceScaleId?[​](#pricescaleid "Direct link to priceScaleId?")

> `optional` **priceScaleId**: `string`

Target price scale to bind new series to.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`'right'` if right scale is visible and `'left'` otherwise

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Visibility of the series.
If the series is hidden, everything including price lines, baseline, price labels and markers, will also be hidden.
Please note that hiding a series is not equivalent to deleting it, since hiding does not affect the timeline at all, unlike deleting where the timeline can be changed (some points can be deleted).

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`true`

---

### priceLineVisible[​](#pricelinevisible "Direct link to priceLineVisible")

> **priceLineVisible**: `boolean`

Show the price line. Price line is a horizontal line indicating the last price of the series.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`true`

---

### priceLineSource[​](#pricelinesource "Direct link to priceLineSource")

> **priceLineSource**: [`PriceLineSource`](/lightweight-charts/docs/4.2/api/enumerations/PriceLineSource)

The source to use for the value of the price line.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

```prism-code
{@link PriceLineSource.LastBar}
```

---

### priceLineWidth[​](#pricelinewidth "Direct link to priceLineWidth")

> **priceLineWidth**: [`LineWidth`](/lightweight-charts/docs/4.2/api/type-aliases/LineWidth)

Width of the price line.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`1`

---

### priceLineColor[​](#pricelinecolor "Direct link to priceLineColor")

> **priceLineColor**: `string`

Color of the price line.
By default, its color is set by the last bar color (or by line color on Line and Area charts).

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`''`

---

### priceLineStyle[​](#pricelinestyle "Direct link to priceLineStyle")

> **priceLineStyle**: [`LineStyle`](/lightweight-charts/docs/4.2/api/enumerations/LineStyle)

Price line style.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

```prism-code
{@link LineStyle.Dashed}
```

---

### priceFormat[​](#priceformat "Direct link to priceFormat")

> **priceFormat**: [`PriceFormat`](/lightweight-charts/docs/4.2/api/type-aliases/PriceFormat)

Price format.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`{ type: 'price', precision: 2, minMove: 0.01 }`

---

### baseLineVisible[​](#baselinevisible "Direct link to baseLineVisible")

> **baseLineVisible**: `boolean`

Visibility of base line. Suitable for percentage and `IndexedTo100` scales.

#### Default Value[​](#default-value-10 "Direct link to Default Value")

`true`

---

### baseLineColor[​](#baselinecolor "Direct link to baseLineColor")

> **baseLineColor**: `string`

Color of the base line in `IndexedTo100` mode.

#### Default Value[​](#default-value-11 "Direct link to Default Value")

`'#B2B5BE'`

---

### baseLineWidth[​](#baselinewidth "Direct link to baseLineWidth")

> **baseLineWidth**: [`LineWidth`](/lightweight-charts/docs/4.2/api/type-aliases/LineWidth)

Base line width. Suitable for percentage and `IndexedTo10` scales.

#### Default Value[​](#default-value-12 "Direct link to Default Value")

`1`

---

### baseLineStyle[​](#baselinestyle "Direct link to baseLineStyle")

> **baseLineStyle**: [`LineStyle`](/lightweight-charts/docs/4.2/api/enumerations/LineStyle)

Base line style. Suitable for percentage and indexedTo100 scales.

#### Default Value[​](#default-value-13 "Direct link to Default Value")

```prism-code
{@link LineStyle.Solid}
```

---

### autoscaleInfoProvider?[​](#autoscaleinfoprovider "Direct link to autoscaleInfoProvider?")

> `optional` **autoscaleInfoProvider**: [`AutoscaleInfoProvider`](/lightweight-charts/docs/4.2/api/type-aliases/AutoscaleInfoProvider)

Override the default [AutoscaleInfo](/lightweight-charts/docs/4.2/api/interfaces/AutoscaleInfo) provider.
By default, the chart scales data automatically based on visible data range.
However, for some reasons one could require overriding this behavior.

#### Default Value[​](#default-value-14 "Direct link to Default Value")

`undefined`

#### Examples[​](#examples "Direct link to Examples")

```prism-code
const firstSeries = chart.addLineSeries({  
    autoscaleInfoProvider: () => ({  
        priceRange: {  
            minValue: 0,  
            maxValue: 100,  
        },  
    }),  
});
```

```prism-code
const firstSeries = chart.addLineSeries({  
    autoscaleInfoProvider: () => ({  
        priceRange: {  
            minValue: 0,  
            maxValue: 100,  
        },  
        margins: {  
            above: 10,  
            below: 10,  
        },  
    }),  
});
```

```prism-code
const firstSeries = chart.addLineSeries({  
    autoscaleInfoProvider: original => {  
        const res = original();  
        if (res !== null) {  
            res.priceRange.minValue -= 10;  
            res.priceRange.maxValue += 10;  
        }  
        return res;  
    },  
});
```