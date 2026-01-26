Version: Next

On this page

Base structure describing a single item of data for a custom series.

This type allows for any properties to be defined
within the interface. It is recommended that you extend this interface with
the required data structure.

## Extends[​](#extends "Direct link to Extends")

* [`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData)<`HorzScaleItem`>

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### color?[​](#color "Direct link to color?")

> `optional` **color**: `string`

If defined then this color will be used for the price line and price scale line
for this specific data item of the custom series.

---

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The time of the data.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData) . [`time`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData#time)

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`CustomSeriesWhitespaceData`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData) . [`customValues`](/lightweight-charts/docs/next/api/interfaces/CustomSeriesWhitespaceData#customvalues)