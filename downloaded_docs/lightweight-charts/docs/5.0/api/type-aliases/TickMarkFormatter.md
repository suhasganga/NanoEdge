Version: 5.0

On this page

> **TickMarkFormatter**: (`time`, `tickMarkType`, `locale`) => `string` | `null`

The `TickMarkFormatter` is used to customize tick mark labels on the time scale.

This function should return `time` as a string formatted according to `tickMarkType` type (year, month, etc) and `locale`.

Note that the returned string should be the shortest possible value and should have no more than 8 characters.
Otherwise, the tick marks will overlap each other.

If the formatter function returns `null` then the default tick mark formatter will be used as a fallback.

## Example[​](#example "Direct link to Example")

```prism-code
const customFormatter = (time, tickMarkType, locale) => {  
    // your code here  
};
```

## Parameters[​](#parameters "Direct link to Parameters")

• **time**: [`Time`](/lightweight-charts/docs/5.0/api/type-aliases/Time)

• **tickMarkType**: [`TickMarkType`](/lightweight-charts/docs/5.0/api/enumerations/TickMarkType)

• **locale**: `string`

## Returns[​](#returns "Direct link to Returns")

`string` | `null`