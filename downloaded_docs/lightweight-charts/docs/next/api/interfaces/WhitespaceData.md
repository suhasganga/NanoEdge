Version: Next

On this page

Represents a whitespace data item, which is a data point without a value.

## Example[​](#example "Direct link to Example")

```prism-code
const data = [  
    { time: '2018-12-03', value: 27.02 },  
    { time: '2018-12-04' }, // whitespace  
    { time: '2018-12-05' }, // whitespace  
    { time: '2018-12-06' }, // whitespace  
    { time: '2018-12-07' }, // whitespace  
    { time: '2018-12-08', value: 23.92 },  
    { time: '2018-12-13', value: 30.74 },  
];
```

## Extended by[​](#extended-by "Direct link to Extended by")

* [`OhlcData`](/lightweight-charts/docs/next/api/interfaces/OhlcData)
* [`SingleValueData`](/lightweight-charts/docs/next/api/interfaces/SingleValueData)

## Type parameters[​](#type-parameters "Direct link to Type parameters")

• **HorzScaleItem** = [`Time`](/lightweight-charts/docs/next/api/type-aliases/Time)

## Properties[​](#properties "Direct link to Properties")

### time[​](#time "Direct link to time")

> **time**: `HorzScaleItem`

The time of the data.

---

### customValues?[​](#customvalues "Direct link to customValues?")

> `optional` **customValues**: `Record`<`string`, `unknown`>

Additional custom values which will be ignored by the library, but
could be used by plugins.