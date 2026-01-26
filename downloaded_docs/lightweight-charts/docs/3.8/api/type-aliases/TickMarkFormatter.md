Version: 3.8

On this page

> **TickMarkFormatter**: (`time`, `tickMarkType`, `locale`) => `string`

The `TickMarkFormatter` is used to customize tick mark labels on the time scale.

This function should return `time` as a string formatted according to `tickMarkType` type (year, month, etc) and `locale`.

Note that the returned string should be the shortest possible value and should have no more than 8 characters.
Otherwise, the tick marks will overlap each other.

## Example[​](#example "Direct link to Example")

```prism-code
const customFormatter = (time, tickMarkType, locale) => {  
    // your code here  
};
```

## Parameters[​](#parameters "Direct link to Parameters")

• **time**: [`UTCTimestamp`](/lightweight-charts/docs/3.8/api/type-aliases/UTCTimestamp) | [`BusinessDay`](/lightweight-charts/docs/3.8/api/interfaces/BusinessDay)

• **tickMarkType**: [`TickMarkType`](/lightweight-charts/docs/3.8/api/enumerations/TickMarkType)

• **locale**: `string`

## Returns[​](#returns "Direct link to Returns")

`string`