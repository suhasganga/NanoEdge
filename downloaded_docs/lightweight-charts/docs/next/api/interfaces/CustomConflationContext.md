Version: Next

On this page

Context object provided to custom series conflation reducers.
This wraps the internal SeriesPlotRow data while providing a user-friendly interface.

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

• **TData** *extends* [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`> = [`CustomData`](/lightweight-charts/docs/next/api/interfaces/CustomData)<`HorzScaleItem`>

## Properties[​](#properties "Direct link to Properties")

### data[​](#data "Direct link to data")

> `readonly` **data**: `TData`

The original custom data item provided by the user.

---

### index[​](#index "Direct link to index")

> `readonly` **index**: `number`

The time index of the data point in the series.

---

### originalTime[​](#originaltime "Direct link to originalTime")

> `readonly` **originalTime**: `HorzScaleItem`

The original time value provided by the user.

---

### time[​](#time "Direct link to time")

> `readonly` **time**: `unknown`

The internal time point object.

---

### priceValues[​](#pricevalues "Direct link to priceValues")

> `readonly` **priceValues**: [`CustomSeriesPricePlotValues`](/lightweight-charts/docs/next/api/type-aliases/CustomSeriesPricePlotValues)

The computed price values for this data point (as returned by priceValueBuilder).
The last value in this array is used as the current price.