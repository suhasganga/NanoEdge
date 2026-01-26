Version: Next

On this page

Represents basic localization options

## Extended by[​](#extended-by "Direct link to Extended by")

* [`LocalizationOptions`](/lightweight-charts/docs/next/api/interfaces/LocalizationOptions)

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

> `optional` **priceFormatter**: [`PriceFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/PriceFormatterFn)

Override formatting of the price scale tick marks, labels and crosshair labels. Can be used for cases that can't be covered with built-in price formats.

#### See[​](#see-1 "Direct link to See")

[PriceFormatCustom](/lightweight-charts/docs/next/api/interfaces/PriceFormatCustom)

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`undefined`

---

### tickmarksPriceFormatter?[​](#tickmarkspriceformatter "Direct link to tickmarksPriceFormatter?")

> `optional` **tickmarksPriceFormatter**: [`TickmarksPriceFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/TickmarksPriceFormatterFn)

Overrides the formatting of price scale tick marks. Use this to define formatting rules based on all provided price values.

#### Default Value[​](#default-value-2 "Direct link to Default Value")

`undefined`

---

### percentageFormatter?[​](#percentageformatter "Direct link to percentageFormatter?")

> `optional` **percentageFormatter**: [`PercentageFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/PercentageFormatterFn)

Overrides the formatting of percentage scale tick marks.

#### Default Value[​](#default-value-3 "Direct link to Default Value")

`undefined`

---

### tickmarksPercentageFormatter?[​](#tickmarkspercentageformatter "Direct link to tickmarksPercentageFormatter?")

> `optional` **tickmarksPercentageFormatter**: [`TickmarksPercentageFormatterFn`](/lightweight-charts/docs/next/api/type-aliases/TickmarksPercentageFormatterFn)

Override formatting of the percentage scale tick marks. Can be used if formatting should be adjusted based on all the values being formatted

#### Default Value[​](#default-value-4 "Direct link to Default Value")

`undefined`