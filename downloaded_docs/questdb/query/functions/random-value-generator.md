On this page

The following functions have been created to help with our test suite. They are
also useful for users testing QuestDB on specific workloads in order to quickly
generate large test datasets that mimic the structure of their actual data.

Values can be generated either:

* Pseudo randomly
* [Deterministically](/docs/query/functions/row-generator/#long_sequence)
  when specifying a `seed`

QuestDB supports the following random generation functions:

* [rnd\_boolean](#rnd_boolean)
* [rnd\_byte](#rnd_byte)
* [rnd\_short](#rnd_short)
* [rnd\_int](#rnd_int)
* [rnd\_long](#rnd_long)
* [rnd\_long256](#rnd_long256)
* [rnd\_float](#rnd_float)
* [rnd\_double](#rnd_double)
* [rnd\_date](#rnd_date)
* [rnd\_timestamp](#rnd_timestamp)
* [rnd\_char](#rnd_char)
* [rnd\_symbol](#rnd_symbol)
* [rnd\_varchar](#rnd_varchar)
* [rnd\_str](#rnd_str)
* [rnd\_bin](#rnd_bin)
* [rnd\_uuid4](#rnd_uuid4)
* [rnd\_ipv4](#rnd_ipv4)
* [rnd\_double\_array](#rnd_double_array)
* [rnd\_decimal](#rnd_decimal)

## Usage[​](#usage "Direct link to Usage")

Random functions should be used for populating test tables only. They do not
hold values in memory and calculations should not be performed at the same time
as the random numbers are generated.

For example, running
`SELECT round(a,2), a FROM (SELECT rnd_double() a FROM long_sequence(10));` is
bad practice and will return inconsistent results.

A better approach would be to populate a table and then run the query. So for
example

1. **create** - `CREATE TABLE test(val double);`
2. **populate** -
   `INSERT INTO test SELECT * FROM (SELECT rnd_double() FROM long_sequence(10));`
3. **query** - `SELECT round(val,2) FROM test;`

## Generating sequences[​](#generating-sequences "Direct link to Generating sequences")

This page describes the functions to generate values. To generate sequences of
values, please refer the page about
[row generators](/docs/query/functions/row-generator/).

## rnd\_boolean[​](#rnd_boolean "Direct link to rnd_boolean")

`rnd_boolean()` - generates a random `boolean` value, either `true` or `false`,
both having equal probability.

**Return value:**

Return value type is `boolean`.

**Examples:**

Random boolean

```prism-code
SELECT  
    value a,  
    count() b  
FROM (SELECT rnd_boolean() value FROM long_sequence(100));
```

| a | b |
| --- | --- |
| true | 47 |
| false | 53 |

## rnd\_byte[​](#rnd_byte "Direct link to rnd_byte")

* `rnd_byte()` - returns a random integer which can take any value between `0`
  and `127`.
* `rnd_byte(min, max)` - generates byte values in a specific range (for example
  only positive, or between 1 and 10).

**Arguments:**

* `min`: is a `byte` representing the lowest possible generated value
  (inclusive).
* `max`: is a `byte` representing the highest possible generated value
  (inclusive).

**Return value:**

Return value type is `byte`.

**Examples:**

Random byte

```prism-code
SELECT rnd_byte() FROM long_sequence(5);  
SELECT rnd_byte(-1,1) FROM long_sequence(5);
```

```prism-code
122,34,17,83,24  
0,1,-1,-1,0
```

## rnd\_short[​](#rnd_short "Direct link to rnd_short")

* `rnd_short()` - returns a random integer which can take any value between
  `-32768` and `32767`.
* `rnd_short(min, max)` - returns short values in a specific range (for example
  only positive, or between 1 and 10). Supplying `min` above `max` will result
  in an `invalid range` error.

**Arguments:**

* `min`: is a `short` representing the lowest possible generated value
  (inclusive).
* `max`: is a `short` representing the highest possible generated value
  (inclusive).

**Return value:**

Return value type is `short`.

**Examples:**

Random short

```prism-code
SELECT rnd_short() FROM long_sequence(5);  
SELECT rnd_short(-1,1) FROM long_sequence(5);
```

```prism-code
-27434,234,-12977,8843,24  
0,1,-1,-1,0
```

## rnd\_int[​](#rnd_int "Direct link to rnd_int")

* `rnd_int()` is used to return a random integer which can take any value
  between `-2147483648` and `2147483647`.
* `rnd_int(min, max, nanRate)` is used to generate int values in a specific
  range (for example only positive, or between 1 and 10), or to get occasional
  `NaN` values along with int values.

**Arguments:**

* `min`: is an `int` representing the lowest possible generated value
  (inclusive).
* `max`: is an `int` representing the highest possible generated value
  (inclusive).
* `nanRate` is an `int` defining the frequency of occurrence of `NaN` values:
  + `0`: No `NaN` will be returned.
  + `1`: Will only return `NaN`.
  + `N > 1`: On average, one in N generated values will be NaN.

**Return value:**

Return value type is `int`.

**Examples:**

Random int

```prism-code
SELECT rnd_int() FROM long_sequence(5)  
SELECT rnd_int(1,4,0) FROM long_sequence(5);  
SELECT rnd_int(1,4,1) FROM long_sequence(5);  
SELECT rnd_int(1,4,2) FROM long_sequence(5);
```

```prism-code
1822685476, 1173192835, -2808202361, 78121757821, 44934191  
1,4,3,1,2  
null,null,null,null,null  
1,null,4,null,2
```

## rnd\_long[​](#rnd_long "Direct link to rnd_long")

* `rnd_long()` is used to return a random signed integer between
  `0x8000000000000000L` and `0x7fffffffffffffffL`.
* `rnd_long(min, max, nanRate)` is used to generate long values in a specific
  range (for example only positive, or between 1 and 10), or to get occasional
  `NaN` values along with int values.

**Arguments:**

* `min`: is a `long` representing the lowest possible generated value
  (inclusive).
* `max`: is a `long` representing the highest possible generated value
  (inclusive).
* `nanRate` is an `int` defining the frequency of occurrence of `NaN` values:
  + `0`: No `NaN` will be returned.
  + `1`: Will only return `NaN`.
  + `N > 1`: On average, one in N generated values will be `NaN`.

**Return value:**

Return value type is `long`.

**Examples:**

Random long

```prism-code
SELECT rnd_long() FROM long_sequence(5);  
SELECT rnd_long(1,4,0) FROM long_sequence(5);  
SELECT rnd_long(1,4,1) FROM long_sequence(5);  
SELECT rnd_long(-10000000,10000000,2) FROM long_sequence(5);
```

```prism-code
1,4,3,1,2  
null,null,null,null,null  
-164567594, -323331140, 26846334, -892982893, -351053301  
300291810703592700, 2787990010234796000, 4305203476273459700, -8518907563589124000, 8443756723558216000
```

## rnd\_long256[​](#rnd_long256 "Direct link to rnd_long256")

* `rnd_long256()` - generates a random `long256` value between 0 and 2^256.

**Return value:**

Return value type is `long256`.

**Examples:**

Random long256

```prism-code
SELECT rnd_long256() FROM long_sequence(5);
```

```prism-code
0x5dd94b8492b4be20632d0236ddb8f47c91efc2568b4d452847b4a645dbe4871a,  
0x55f256188b3474aca83ccc82c597668bb84f36d3f5b25afd9e194c1867625918,  
0x630c6f02c1c2e0c2aa4ac80ab684aa36d91dd5233cc185bb7097400fa12e7de0,  
0xa9eeaa5268f911f4bcac2e89b621bd28bba90582077fc9fb9f14a53fcf6368b7,  
0x7c80546eea2ec093a5244e39efad3f39c5489d2337007fd0b61d8b141058724d
```

## rnd\_float[​](#rnd_float "Direct link to rnd_float")

* `rnd_float()` - generates a random **positive** `float` between 0 and 1.
* `rnd_float(nanRate)` - generates a random **positive** `float` between 0 and 1
  which will be `NaN` at a frequency defined by `nanRate`.

**Arguments:**

* `nanRate` is an `int` defining the frequency of occurrence of `NaN` values:
* `0`: No `NaN` will be returned.
* `1`: Will only return `NaN`.
* `N > 1`: On average, one in N generated values will be `NaN`.

**Return value:**

Return value type is `float`.

**Examples:**

Random float

```prism-code
SELECT rnd_float() FROM long_sequence(5);  
SELECT rnd_float(2) FROM long_sequence(6);
```

```prism-code
0.3821478, 0.5162148, 0.22929084, 0.03736937, 0.39675003  
0.08108246, 0.7082644, null, 0.6784522, null, 0.5711276
```

## rnd\_double[​](#rnd_double "Direct link to rnd_double")

* `rnd_double()` - generates a random **positive** `double` between 0 and 1.
* `rnd_double(nanRate)` - generates a random **positive** `double` between 0 and
  1 which will be `NaN` at a frequency defined by `nanRate`.

**Arguments:**

* `nanRate` is an `int` defining the frequency of occurrence of `NaN` values:
* `0`: No `NaN` will be returned.
* `1`: Will only return `NaN`.
* `N > 1`: On average, one in N generated values will be `NaN`.

**Return value:**

Return value type is `double`.

**Examples:**

Random double

```prism-code
SELECT rnd_double() FROM long_sequence(5);  
SELECT rnd_double(2) FROM long_sequence(5);
```

```prism-code
0.99115364871, 0.31011470271, 0.10776479191, 0.53938281731, 0.89820403511  
0.99115364871, null, null, 0.53938281731, 0.89820403511
```

## rnd\_date()[​](#rnd_date "Direct link to rnd_date()")

* `rnd_date()` generates a random date between `start` and `end` dates (both
  inclusive). IT will also generate `NaN` values at a frequency defined by
  `nanRate`. When `start` or `end` are invalid dates, or when `start` is
  superior to `end`, it will return `invalid range` error. When `nanRate` is
  inferior to 0, it will return `invalid NAN rate` error.

**Arguments:**

* `start` is a `date` defining the minimum possible generated date (inclusive)
* `end` is a `date` defining the maximum possible generated date (inclusive)
* `nanRate` defines the frequency of occurrence of `NaN` values:
  + `0`: No `NaN` will be returned.
  + `1`: Will only return `NaN`.
  + `N > 1`: On average, one in N generated values will be NaN.

**Return value:**

Return value type is `date`.

**Examples:**

Random date

```prism-code
SELECT rnd_date(  
    to_date('2015', 'yyyy'),  
    to_date('2016', 'yyyy'),  
    0)  
FROM long_sequence(5);
```

```prism-code
2015-01-29T18:00:17.402Z, 2015-11-15T20:22:14.112Z,  
2015-12-08T09:26:04.483Z, 2015-05-28T02:22:47.022Z,  
2015-10-13T19:16:37.034Z
```

## rnd\_timestamp()[​](#rnd_timestamp "Direct link to rnd_timestamp()")

* `rnd_timestamp(start, end, nanRate)` generates a random timestamp between
  `start` and `end` timestamps (both inclusive). It will also generate `NaN`
  values at a frequency defined by `nanRate`. When `start` or `end` are invalid
  timestamps, or when `start` is superior to `end`, it will return
  `invalid range` error. When `nanRate` is inferior to 0, it will return
  `invalid NAN rate` error.

**Arguments:**

* `start` is a `timestamp` defining the minimum possible generated timestamp
  (inclusive)
* `end` is a `timestamp` defining the maximum possible generated timestamp
  (inclusive)
* `nanRate` defines the frequency of occurrence of `NaN` values:
  + `0`: No `NaN` will be returned.
  + `1`: Will only return `NaN`.
  + `N > 1`: On average, one in N generated values will be NaN.

**Return value:**

Return value type is `timestamp`.

**Examples:**

Random timestamp

```prism-code
SELECT rnd_timestamp(  
    to_timestamp('2015', 'yyyy'),  
    to_timestamp('2016', 'yyyy'),  
    0)  
FROM long_sequence(5);
```

```prism-code
2015-01-29T18:00:17.402762Z, 2015-11-15T20:22:14.112744Z,  
2015-12-08T09:26:04.483039Z, 2015-05-28T02:22:47.022680Z,  
2015-10-13T19:16:37.034203Z
```

#### Sequences[​](#sequences "Direct link to Sequences")

To generate increasing timestamps, please refer the page about
[row generators](/docs/query/functions/row-generator/).

## rnd\_char[​](#rnd_char "Direct link to rnd_char")

* `rnd_char()` is used to generate a random `char` which will be an uppercase
  character from the 26-letter A to Z alphabet. Letters from A to Z will be
  generated with equal probability.

**Return value:**

Return value type is `char`.

**Examples:**

Random char

```prism-code
SELECT rnd_char() FROM long_sequence(5);
```

```prism-code
G, P, E, W, K
```

## rnd\_symbol[​](#rnd_symbol "Direct link to rnd_symbol")

* `rnd_symbol(symbolList)` is used to choose a random `symbol` from a list
  defined by the user. It is useful when looking to generate specific symbols
  from a finite list (e.g `BUY, SELL` or `AUTUMN, WINTER, SPRING, SUMMER`.
  Symbols are randomly chosen from the list with equal probability. When only
  one symbol is provided in the list, this symbol will be chosen with 100%
  probability, in which case it is more efficient to use
  `cast('your_symbol' as symbol`
* `rnd_symbol(list_size, minLength, maxLength, nullRate)` generated a finite
  list of distinct random symbols and chooses one symbol from the list at
  random. The finite list is of size `list_size`. The generated symbols length
  is between `minLength` and `maxLength` (both inclusive). The function will
  also generate `null` values at a rate defined by `nullRate`.

**Arguments:**

* `symbolList` is a variable-length list of possible `symbol` values expressed
  as a comma-separated list of strings. For example,
  `'a', 'bcd', 'efg123', '行'`
* `list_size` is the number of distinct `symbol` values to generated
* `minLength` is an `int` defining the minimum length for of a generated symbol
  (inclusive)
* `maxLength` is an `int` defining the maximum length for of a generated symbol
  (inclusive)
* `nullRate` is an `int` defining the frequency of occurrence of `null` values:
  + `0`: No `null` will be returned.
  + `1`: Will only return `null`.
  + `N > 1`: On average, one in N generated values will be `null`.

**Return value:**

Return value type is `symbol`.

**Examples:**

Random symbol from a list

```prism-code
SELECT rnd_symbol('ABC','def', '123')  
FROM long_sequence(5);
```

```prism-code
'ABC', '123', 'def', '123', 'ABC'
```

Random symbol, randomly generated

```prism-code
SELECT rnd_symbol(2, 3, 4, 0)  
FROM long_sequence(5);
```

```prism-code
'ABC', 'DEFG', 'ABC', 'DEFG', 'DEFG'
```

## rnd\_varchar[​](#rnd_varchar "Direct link to rnd_varchar")

* `rnd_varchar(stringList)` chooses a random `varchar` string from a list
  defined by the user. It is useful when looking to generate specific strings
  from a finite list (e.g `BUY, SELL` or `AUTUMN, WINTER, SPRING, SUMMER`.
  Strings are randomly chosen from the list with equal probability. When only
  one string is provided in the list, this string will be chosen with 100%
  probability.
* `rnd_varchar(minLength, maxLength, nullRate)` generates strings of a length
  between between `minLength` and `maxLength` (both inclusive). The function
  will also generate `null` values at a rate defined by `nullRate`.

**Arguments:**

* `strList` is a variable-length list of possible `string` values expressed as a
  comma-separated list of strings. For example, `'a', 'bcd', 'efg123', '行'`
* `minLength` is an `int` defining the minimum length for of a generated string
  (inclusive)
* `maxLength` is an `int` defining the maximum length for of a generated string
  (inclusive)
* `nullRate` is an `int` defining the frequency of occurrence of `null` values:
  + `0`: No `null` will be returned.
  + `1`: Will only return `null`.
  + `N > 1`: On average, one in N generated values will be `null`.

**Return value:**

Return value type is `varchar`.

**Examples:**

Random string from a list

```prism-code
SELECT rnd_varchar('ABC','def', '123')  
FROM long_sequence(5);
```

```prism-code
'ABC', '123', 'def', '123', 'ABC'
```

Random strings, including null, between min and max length.

```prism-code
SELECT rnd_varchar(2, 2, 4)  
FROM long_sequence(4);
```

```prism-code
'潃', 'Ԓ㠗', '콻薓', '8>'
```

## rnd\_str[​](#rnd_str "Direct link to rnd_str")

* `rnd_str(stringList)` is used to choose a random `string` from a list defined
  by the user. It is useful when looking to generate specific strings from a
  finite list (e.g `BUY, SELL` or `AUTUMN, WINTER, SPRING, SUMMER`. Strings are
  randomly chosen from the list with equal probability. When only one string is
  provided in the list, this string will be chosen with 100% probability.
* `rnd_str(minLength, maxLength, nullRate)` generates strings of a length
  between between `minLength` and `maxLength` (both inclusive). The function
  will also generate `null` values at a rate defined by `nullRate`.
* `rnd_str(list_size, minLength, maxLength, nullRate)` generates a finite list
  of distinct random string and chooses one string from the list at random. The
  finite list is of size `list_size`, which is optional.

**Arguments:**

* `strList` is a variable-length list of possible `string` values expressed as a
  comma-separated list of strings. For example, `'a', 'bcd', 'efg123', '行'`
* `list_size` is an optional field declaring the number of distinct `string`
  values to generate.
* `minLength` is an `int` defining the minimum length for of a generated string
  (inclusive)
* `maxLength` is an `int` defining the maximum length for of a generated string
  (inclusive)
* `nullRate` is an `int` defining the frequency of occurrence of `null` values:
  + `0`: No `null` will be returned.
  + `1`: Will only return `null`.
  + `N > 1`: On average, one in N generated values will be `null`.

**Return value:**

Return value type is `string`.

**Examples:**

Random string from a list

```prism-code
SELECT rnd_str('ABC','def', '123')  
FROM long_sequence(5);
```

```prism-code
'ABC', '123', 'def', '123', 'ABC'
```

Random strings, including null, between min and max length.

```prism-code
SELECT rnd_str(2, 2, 4)  
FROM long_sequence(8);
```

```prism-code
'AB', 'CD', null, 'EF', 'CD', 'EF', null, 'AB'
```

5 strings from a set of 3 distinct strings, each 2 characters long, no nulls.

```prism-code
SELECT rnd_str(3, 2, 2, 0) FROM long_sequence(5);
```

```prism-code
'DS', 'GG', 'XS', 'GG', 'XS'
```

## rnd\_bin[​](#rnd_bin "Direct link to rnd_bin")

* `rnd_bin()` generates random binary data of a size up to `32` bytes.
* `rnd_bin(minBytes, maxBytes, nullRate)` generates random binary data of a size
  between `minBytes` and `maxBytes` and returns `null` at a rate defined by
  `nullRate`.

**Arguments:**

* `minBytes` is a `long` defining the minimum size in bytes for of a generated
  binary (inclusive)
* `maxBytes` is a `long` defining the maximum size in bytes for of a generated
  binary (inclusive)
* `nullRate` is an `int` defining the frequency of occurrence of `null` values:
  + `0`: No `null` will be returned.
  + `1`: Will only return `null`.
  + `N > 1`: On average, one in N generated values will be `null`.

**Return value:**

Return value type is `binary`.

**Examples:**

Random binary

```prism-code
SELECT rnd_bin() FROM long_sequence(5);  
SELECT rnd_bin(2, 5, 2) FROM long_sequence(5);
```

## rnd\_uuid4[​](#rnd_uuid4 "Direct link to rnd_uuid4")

* `rnd_uuid4()` is used to generate a random
  [UUID](/docs/query/datatypes/overview/#the-uuid-type).
* The generated UUIDs are
  [version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random))
  as per the [RFC 4122](https://tools.ietf.org/html/rfc4122#section-4.4)
  specification.
* Generated UUIDs do not use a cryptographically strong random generator and
  should not be used for security purposes.

**Return value:**

Return value type is `uuid`.

**Examples:**

Random char

```prism-code
SELECT rnd_uuid4() FROM long_sequence(3);
```

```prism-code
deca0b0b-b14b-4d39-b891-9e1e786a48e7  
2f113ebb-d36e-4e58-b804-6ece2263abe4  
6eddd24a-8889-4345-8001-822cc2d41951
```

## rnd\_ipv4()[​](#rnd_ipv4 "Direct link to rnd_ipv4()")

Random address generator for a single address.

Returns a single IPv4 address.

Useful for testing.

**Examples:**

```prism-code
rnd_ipv4()  
/* Return address between 0.0.0.1 - 255.255.255.255 */  
97.29.14.22
```

## rnd\_ipv4(string, int)[​](#rnd_ipv4string-int "Direct link to rnd_ipv4(string, int)")

Generates a random ip address within the bounds of a given subnet.

The integer argument dictates how many null values will be generated.

Returns an IPv4 address within specified range.

**Examples:**

```prism-code
rnd_ipv4('22.43.200.9/16', 0)  
/* Return address between 22.43.0.0 - 22.43.255.25 */  
22.43.200.12
```

## rnd\_double\_array()[​](#rnd_double_array "Direct link to rnd_double_array()")

Generates a `DOUBLE` array with random elements. There are two main forms:

1. `rnd_double_array(nDims, [ nanRate, [ maxDimLength ] ])` — generates an array
   with the specified dimensionality and random dimension lengths, as well as
   random elements. `nanRate` and `maxDimLength` are optional parameters. The
   default `nanRate` is zero and the default `maxDimLength` is 16.
2. `rnd_double_array(nDims, nanRate, 0, dim1Len, dim2Len, dim3Len, ...)` —
   generates an array of fixed size with random elements. Note the dummy
   argument 0, its is needed to disambiguate from other forms.

**Examples:**

Generate a 2-dimensional array with 50% NaNs and max dimension length 2:

```prism-code
SELECT rnd_double_array(2, 2, 2);
```

```prism-code
[  
  [NaN, 0.45738551710910846],  
  [0.7702337472360304, NaN]  
]
```

Generate a random 2x5 array with no NaNs:

```prism-code
SELECT rnd_double_array(2, 0, 0, 2, 5);
```

```prism-code
[  
  [0.316129098879942,  0.8662158040337894, 0.8642568676265672,  0.6470407728977403, 0.4740048603478647],  
  [0.2928431722534959, 0.4269209916086062, 0.08520276767101154, 0.5371988206397026, 0.5786689751730609]  
]
```

## rnd\_decimal[​](#rnd_decimal "Direct link to rnd_decimal")

* `rnd_decimal(precision, scale, nanRate)` - generates a random **positive**
  `decimal` between 0 and the maximum value representable by the given precision
  and scale.

**Arguments:**

* `nanRate` is an `int` defining the frequency of occurrence of `NaN` values:
* `0`: No `NaN` will be returned.
* `1`: Will only return `NaN`.
* `N > 1`: On average, one in N generated values will be `NaN`.

**Return value:**

Return value type is `decimal`.

**Examples:**

Random decimal

```prism-code
SELECT rnd_decimal(8, 2, 0) FROM long_sequence(5);  
SELECT rnd_decimal(8, 2, 4) FROM long_sequence(5);
```

```prism-code
6618.97 5037.02 7118.16 9024.15 537.05  
null 734.74 787.93 null 789.92
```