Version: 3.8

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

## Properties[​](#properties "Direct link to Properties")

### time[​](#time "Direct link to time")

> **time**: [`Time`](/lightweight-charts/docs/3.8/api/type-aliases/Time)

The time of the data.