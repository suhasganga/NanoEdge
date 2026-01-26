Version: 3.8

On this page

Structure that describes price scale options

## Properties[​](#properties "Direct link to Properties")

### autoScale[​](#autoscale "Direct link to autoScale")

> **autoScale**: `boolean`

Autoscaling is a feature that automatically adjusts a price scale to fit the visible range of data.
Note that overlay price scales are always auto-scaled.

#### Default Value[​](#default-value "Direct link to Default Value")

`true`

---

### mode[​](#mode "Direct link to mode")

> **mode**: [`PriceScaleMode`](/lightweight-charts/docs/3.8/api/enumerations/PriceScaleMode)

Price scale mode.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

```prism-code
{@link PriceScaleMode.Normal}
```

---

### invertScale[​](#invertscale "Direct link to invertScale")

> **invertScale**: `boolean`

Invert the price scale, so that a upwards trend is shown as a downwards trend and vice versa.
Affects both the price scale and the data on the chart.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`false`

---

### alignLabels[​](#alignlabels "Direct link to alignLabels")

> **alignLabels**: `boolean`

Align price scale labels to prevent them from overlapping.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`true`

---

### scaleMargins[​](#scalemargins "Direct link to scaleMargins")

> **scaleMargins**: [`PriceScaleMargins`](/lightweight-charts/docs/3.8/api/interfaces/PriceScaleMargins)

Price scale margins.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`{ bottom: 0.1, top: 0.2 }`

#### Example[​](#example "Direct link to Example")

```prism-code
chart.priceScale('right').applyOptions({  
    scaleMargins: {  
        top: 0.8,  
        bottom: 0,  
    },  
});
```

---

### borderVisible[​](#bordervisible "Direct link to borderVisible")

> **borderVisible**: `boolean`

Set true to draw a border between the price scale and the chart area.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`true`

---

### borderColor[​](#bordercolor "Direct link to borderColor")

> **borderColor**: `string`

Price scale border color.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`'#2B2B43'`

---

### entireTextOnly[​](#entiretextonly "Direct link to entireTextOnly")

> **entireTextOnly**: `boolean`

Show top and bottom corner labels only if entire text is visible.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`false`

---

### visible[​](#visible "Direct link to visible")

> **visible**: `boolean`

Indicates if this price scale visible. Ignored by overlay price scales.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`true` for the right price scale and `false` for the left

---

### drawTicks[​](#drawticks "Direct link to drawTicks")

> **drawTicks**: `boolean`

Draw small horizontal line on price axis labels.

#### Default Value[​](#default-value-9 "Direct link to Default Value")

`true`