Version: Next

On this page

Interface to be implemented by the object in order to be used as a price formatter

## Methods[​](#methods "Direct link to Methods")

### format()[​](#format "Direct link to format()")

> **format**(`price`): `string`

Formatting function

#### Parameters[​](#parameters "Direct link to Parameters")

• **price**: `number`

Original price to be formatted

#### Returns[​](#returns "Direct link to Returns")

`string`

Formatted price

---

### formatTickmarks()[​](#formattickmarks "Direct link to formatTickmarks()")

> **formatTickmarks**(`prices`): `string`[]

A formatting function for price scale tick marks. Use this function to define formatting rules based on all provided price values.

#### Parameters[​](#parameters-1 "Direct link to Parameters")

• **prices**: readonly `number`[]

Prices to be formatted

#### Returns[​](#returns-1 "Direct link to Returns")

`string`[]

Formatted prices