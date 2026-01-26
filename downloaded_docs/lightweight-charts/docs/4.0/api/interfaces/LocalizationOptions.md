Version: 4.0

On this page

Represents options for formatting dates, times, and prices according to a locale.

## Properties[​](#properties "Direct link to Properties")

### locale[​](#locale "Direct link to locale")

> **locale**: `string`

Current locale used to format dates. Uses the browser's language settings by default.

#### See[​](#see "Direct link to See")

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation>

#### Default Value[​](#default-value "Direct link to Default Value")

`navigator.language`

---

### priceFormatter?[​](#priceformatter "Direct link to priceFormatter?")

> `optional` **priceFormatter**: [`PriceFormatterFn`](/lightweight-charts/docs/4.0/api/type-aliases/PriceFormatterFn)

Override formatting of the price scale crosshair label. Can be used for cases that can't be covered with built-in price formats.

#### See[​](#see-1 "Direct link to See")

[PriceFormatCustom](/lightweight-charts/docs/4.0/api/interfaces/PriceFormatCustom)

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`undefined`

---

### timeFormatter?[​](#timeformatter "Direct link to timeFormatter?")

> `optional` **timeFormatter**: [`TimeFormatterFn`](/lightweight-charts/docs/4.0/api/type-aliases/TimeFormatterFn)

Override formatting of the time scale crosshair label.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`undefined`

---

### dateFormat[​](#dateformat "Direct link to dateFormat")

> **dateFormat**: `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which will be replaced with corresponding date's value.

Ignored if [timeFormatter](/lightweight-charts/docs/4.0/api/interfaces/LocalizationOptions#timeformatter) has been specified.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`'dd MMM \'yy'`