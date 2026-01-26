Version: 4.1

On this page

Represents a price line options.

## Properties[​](#properties "Direct link to Properties")

### id?[​](#id "Direct link to id?")

> `optional` **id**: `string`

The optional ID of this price line.

---

### price[​](#price "Direct link to price")

> **price**: `number`

Price line's value.

#### Default Value[​](#default-value "Direct link to Default Value")

`0`

---

### color[​](#color "Direct link to color")

> **color**: `string`

Price line's color.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`''`

---

### lineWidth[​](#linewidth "Direct link to lineWidth")

> **lineWidth**: [`LineWidth`](/lightweight-charts/docs/4.1/api/type-aliases/LineWidth)

Price line's width in pixels.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`1`

---

### lineStyle[​](#linestyle "Direct link to lineStyle")

> **lineStyle**: [`LineStyle`](/lightweight-charts/docs/4.1/api/enumerations/LineStyle)

Price line's style.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

```prism-code
{@link LineStyle.Solid}
```

---

### lineVisible[​](#linevisible "Direct link to lineVisible")

> **lineVisible**: `boolean`

Display line.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`true`

---

### axisLabelVisible[​](#axislabelvisible "Direct link to axisLabelVisible")

> **axisLabelVisible**: `boolean`

Display the current price value in on the price scale.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`true`

---

### title[​](#title "Direct link to title")

> **title**: `string`

Price line's on the chart pane.

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`''`

---

### axisLabelColor[​](#axislabelcolor "Direct link to axisLabelColor")

> **axisLabelColor**: `string`

Background color for the axis label.
Will default to the price line color if unspecified.

#### Default Value[​](#default-value-7 "Direct link to Default Value")

`''`

---

### axisLabelTextColor[​](#axislabeltextcolor "Direct link to axisLabelTextColor")

> **axisLabelTextColor**: `string`

Text color for the axis label.

#### Default Value[​](#default-value-8 "Direct link to Default Value")

`''`