Version: 5.0

On this page

Represents a series marker.

## Extends[​](#extends "Direct link to Extends")

* [`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase)<`TimeType`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **TimeType**

## Properties[​](#properties "Direct link to Properties")

### time[​](#time "Direct link to time")

> **time**: `TimeType`

The time of the marker.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`time`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#time)

---

### shape[​](#shape "Direct link to shape")

> **shape**: [`SeriesMarkerShape`](/lightweight-charts/docs/5.0/api/type-aliases/SeriesMarkerShape)

The shape of the marker.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`shape`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#shape)

---

### color[​](#color "Direct link to color")

> **color**: `string`

The color of the marker.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`color`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#color)

---

### id?[​](#id "Direct link to id?")

> `optional` **id**: `string`

The ID of the marker.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`id`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#id)

---

### text?[​](#text "Direct link to text?")

> `optional` **text**: `string`

The optional text of the marker.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`text`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#text)

---

### size?[​](#size "Direct link to size?")

> `optional` **size**: `number`

The optional size of the marker.

#### Default Value[​](#default-value "Direct link to Default Value")

`1`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`size`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#size)

---

### position[​](#position "Direct link to position")

> **position**: [`SeriesMarkerPricePosition`](/lightweight-charts/docs/5.0/api/type-aliases/SeriesMarkerPricePosition)

The position of the marker.

#### Overrides[​](#overrides "Direct link to Overrides")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`position`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#position)

---

### price[​](#price "Direct link to price")

> **price**: `number`

The price value for exact Y-axis positioning.

Required when using [SeriesMarkerPricePosition](/lightweight-charts/docs/5.0/api/type-aliases/SeriesMarkerPricePosition) position type.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[`SeriesMarkerBase`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase) . [`price`](/lightweight-charts/docs/5.0/api/interfaces/SeriesMarkerBase#price)