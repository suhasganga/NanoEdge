Version: 4.2

On this page

Represents options for formatting dates, times, and prices according to a locale.

## Extends[​](#extends "Direct link to Extends")

* [`LocalizationOptionsBase`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem**

## Properties[​](#properties "Direct link to Properties")

### timeFormatter?[​](#timeformatter "Direct link to timeFormatter?")

> `optional` **timeFormatter**: [`TimeFormatterFn`](/lightweight-charts/docs/4.2/api/type-aliases/TimeFormatterFn)<`HorzScaleItem`>

Override formatting of the time scale crosshair label.

#### Default Value[​](#default-value "Direct link to Default Value")

`undefined`

---

### dateFormat[​](#dateformat "Direct link to dateFormat")

> **dateFormat**: `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which will be replaced with corresponding date's value.

Ignored if [timeFormatter](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptions#timeformatter) has been specified.

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`'dd MMM \'yy'`

---

### locale[​](#locale "Direct link to locale")

> **locale**: `string`

Current locale used to format dates. Uses the browser's language settings by default.

#### See[​](#see "Direct link to See")

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation>

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`navigator.language`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[`LocalizationOptionsBase`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase) . [`locale`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase#locale)

---

### priceFormatter?[​](#priceformatter "Direct link to priceFormatter?")

> `optional` **priceFormatter**: [`PriceFormatterFn`](/lightweight-charts/docs/4.2/api/type-aliases/PriceFormatterFn)

Override formatting of the price scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in price formats.

#### See[​](#see-1 "Direct link to See")

[PriceFormatCustom](/lightweight-charts/docs/4.2/api/interfaces/PriceFormatCustom)

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[`LocalizationOptionsBase`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase) . [`priceFormatter`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase#priceformatter)

---

### percentageFormatter?[​](#percentageformatter "Direct link to percentageFormatter?")

> `optional` **percentageFormatter**: [`PercentageFormatterFn`](/lightweight-charts/docs/4.2/api/type-aliases/PercentageFormatterFn)

Override formatting of the percentage scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in percentage format.

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`undefined`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[`LocalizationOptionsBase`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase) . [`percentageFormatter`](/lightweight-charts/docs/4.2/api/interfaces/LocalizationOptionsBase#percentageformatter)