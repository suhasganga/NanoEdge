Version: Next

On this page

Extends LocalizationOptions for price-based charts.
Includes settings specific to formatting price values on the horizontal scale.

## Extends[​](#extends "Direct link to Extends")

* [`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) <[`HorzScalePriceItem`](/lightweight-charts/docs/next/api/type-aliases/HorzScalePriceItem)>

## Properties[​](#properties "Direct link to Properties")

### timeFormatter?[​](#timeformatter "Direct link to timeFormatter?")

> `optional` **timeFormatter**: [`TimeFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/TimeFormatterFn)<`number`>

Override formatting of the time scale crosshair label.

#### Default Value[​](#default-value "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`timeFormatter`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#timeformatter)

---

### dateFormat[​](#dateformat "Direct link to dateFormat")

> **dateFormat**: `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which will be replaced with corresponding date's value.

Ignored if [timeFormatter](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#timeformatter) has been specified.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`'dd MMM \'yy'`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`dateFormat`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#dateformat)

---

### locale[​](#locale "Direct link to locale")

> **locale**: `string`

Current locale used to format dates. Uses the browser's language settings by default.

#### See[​](#see "Direct link to See")

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation>

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`navigator.language`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`locale`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#locale)

---

### priceFormatter?[​](#priceformatter "Direct link to priceFormatter?")

> `optional` **priceFormatter**: [`PriceFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/PriceFormatterFn)

Override formatting of the price scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in price formats.

#### See[​](#see-1 "Direct link to See")

[PriceFormatCustom](/lightweight-charts/docs/next/api/interfaces/PriceFormatCustom)

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`priceFormatter`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#priceformatter)

---

### tickmarksPriceFormatter?[​](#tickmarkspriceformatter "Direct link to tickmarksPriceFormatter?")

> `optional` **tickmarksPriceFormatter**: [`TickmarksPriceFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/TickmarksPriceFormatterFn)

Overrides the formatting of price scale tick marks. Use this to define formatting rules based on all provided price values.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`tickmarksPriceFormatter`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#tickmarkspriceformatter)

---

### percentageFormatter?[​](#percentageformatter "Direct link to percentageFormatter?")

> `optional` **percentageFormatter**: [`PercentageFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/PercentageFormatterFn)

Overrides the formatting of percentage scale tick marks.

#### Default Value[​](#default-value-5 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`percentageFormatter`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#percentageformatter)

---

### tickmarksPercentageFormatter?[​](#tickmarkspercentageformatter "Direct link to tickmarksPercentageFormatter?")

> `optional` **tickmarksPercentageFormatter**: [`TickmarksPercentageFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/TickmarksPercentageFormatterFn)

Override formatting of the percentage scale tick marks. Can be used if formatting should be adjusted based on all the values being formatted

#### Default Value[​](#default-value-6 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions) . [`tickmarksPercentageFormatter`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions#tickmarkspercentageformatter)

---

### precision[​](#precision "Direct link to precision")

> **precision**: `number`

The number of decimal places to display for price values on the horizontal scale.