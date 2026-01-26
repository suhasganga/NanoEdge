Version: 4.2

On this page

> **Time**: [`UTCTimestamp`](/lightweight-charts/docs/4.2/api/type-aliases/UTCTimestamp) | [`BusinessDay`](/lightweight-charts/docs/4.2/api/interfaces/BusinessDay) | `string`

The Time type is used to represent the time of data items.

Values can be a [UTCTimestamp](/lightweight-charts/docs/4.2/api/type-aliases/UTCTimestamp), a [BusinessDay](/lightweight-charts/docs/4.2/api/interfaces/BusinessDay), or a business day string in ISO format.

## Example[​](#example "Direct link to Example")

```prism-code
const timestamp = 1529899200; // Literal timestamp representing 2018-06-25T04:00:00.000Z  
const businessDay = { year: 2019, month: 6, day: 1 }; // June 1, 2019  
const businessDayString = '2021-02-03'; // Business day string literal
```