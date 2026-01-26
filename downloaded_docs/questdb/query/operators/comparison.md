On this page

This page describes the available operators to assist with comparison
operations.

If `string` or `char` values are used in the input, they are converted to `int`
using the [ASCII Table](https://www.asciitable.com/) for comparison.

## `IN` (list)[​](#in-list "Direct link to in-list")

`X IN (a, b, c)` returns true if X is present in the list.

#### Example[​](#example "Direct link to Example")

```prism-code
SELECT 5 IN (1, 2, 7, 5, 8)
```

| column |
| --- |
| true |

## `=` Equals[​](#-equals "Direct link to -equals")

`(value1) = (value2)` - returns true if the two values are the same.

#### Arguments[​](#arguments "Direct link to Arguments")

* `value1` is any data type.
* `value2` is any data type.

#### Return value[​](#return-value "Direct link to Return value")

Return value type is boolean.

#### Examples[​](#examples "Direct link to Examples")

```prism-code
SELECT '5' = '5';  
-- Returns true  
  
SELECT 5 = 5;  
-- Returns true  
  
SELECT '5' = '3';  
-- Returns false  
  
SELECT 5 = 3;  
-- Returns false
```

## `>` Greater than[​](#-greater-than "Direct link to -greater-than")

* `(value1) > (value2)` - returns true if `value1` is greater than `value2`.

#### Arguments[​](#arguments-1 "Direct link to Arguments")

* `value1` and `value2` are one of the following data types:
  + any numeric data type
  + `char`
  + `date`
  + `timestamp`
  + `symbol`
  + `string`

#### Return value[​](#return-value-1 "Direct link to Return value")

Return value type is boolean.

#### Examples[​](#examples-1 "Direct link to Examples")

```prism-code
SELECT 'abc' > 'def';  
-- Returns false  
  
SELECT '5' > '5';  
-- Returns false  
  
SELECT 'a' > 'b';  
-- Returns false
```

## `>=` Greater than or equal to[​](#-greater-than-or-equal-to "Direct link to -greater-than-or-equal-to")

* `(value1) >= (value2)` - returns true if `value1` is greater than `value2`.

#### Arguments[​](#arguments-2 "Direct link to Arguments")

* `value1` and `value2` are one of the following data types:
  + any numeric data type
  + `char`
  + `date`
  + `timestamp`
  + `symbol`
  + `string`

#### Return value[​](#return-value-2 "Direct link to Return value")

Return value type is boolean.

#### Examples[​](#examples-2 "Direct link to Examples")

```prism-code
SELECT 'abc' >= 'def';  
-- Returns false  
  
SELECT '5' >= '5';  
-- Returns true  
  
SELECT '7' >= '5';  
-- Returns true  
  
SELECT 'a' >= 'b';  
-- Returns false
```

## `<` Lesser than[​](#-lesser-than "Direct link to -lesser-than")

* `(value1) < (value2)` - returns true if `value1` is less than `value2`.

#### Arguments[​](#arguments-3 "Direct link to Arguments")

* `value1` and `value2` are one of the following data types:
  + any numeric data type
  + `char`
  + `date`
  + `timestamp`
  + `symbol`
  + `string`

#### Return value[​](#return-value-3 "Direct link to Return value")

Return value type is boolean.

#### Examples[​](#examples-3 "Direct link to Examples")

```prism-code
SELECT '123' < '456';  
-- Returns true  
  
SELECT 5 < 5;  
-- Returns false  
  
SELECT 5 < 3;  
-- Returns false
```

## `<=` Lesser than or equal to[​](#-lesser-than-or-equal-to "Direct link to -lesser-than-or-equal-to")

* `(value1) <= (value2)` - returns true if `value1` is less than `value2`.

#### Arguments[​](#arguments-4 "Direct link to Arguments")

* `value1` and `value2` are one of the following data types:
  + any numeric data type
  + `char`
  + `date`
  + `timestamp`
  + `symbol`
  + `string`

#### Return value[​](#return-value-4 "Direct link to Return value")

Return value type is boolean.

#### Examples[​](#examples-4 "Direct link to Examples")

```prism-code
SELECT '123' <= '456';  
-- Returns true  
  
SELECT 5 <= 5;  
-- Returns true  
  
SELECT 5 <= 3;  
-- Returns false
```

## `<>` or `!=` Not equals[​](#-or--not-equals "Direct link to -or--not-equals")

`(value1) <> (value2)` - returns true if `value1` is not equal to `value2`.

`!=` is an alias of `<>`.

#### Arguments[​](#arguments-5 "Direct link to Arguments")

* `value1` is any data type.
* `value2` is any data type.

#### Return value[​](#return-value-5 "Direct link to Return value")

Return value type is boolean.

#### Examples[​](#examples-5 "Direct link to Examples")

```prism-code
SELECT '5' <> '5';  
-- Returns false  
  
SELECT 5 <> 5;  
-- Returns false  
  
SELECT 'a' <> 'b';  
-- Returns true  
  
SELECT 5 <> 3;  
-- Returns true
```

## `IN` (value1, value2, ...)[​](#in-value1-value2- "Direct link to in-value1-value2-")

The `IN` operator, when used with more than one argument, behaves as the
standard SQL `IN`. It provides a concise way to represent multiple OR-ed
equality conditions.

#### Arguments[​](#arguments-6 "Direct link to Arguments")

* `value1`, `value2`, ... are string type values representing dates or
  timestamps.

#### Examples[​](#examples-6 "Direct link to Examples")

Consider the following query:

IN list

```prism-code
SELECT * FROM scores  
WHERE ts IN ('2018-01-01', '2018-01-01T12:00', '2018-01-02');
```

This query is equivalent to:

IN list equivalent OR

```prism-code
SELECT * FROM scores  
WHERE ts = '2018-01-01' or ts = '2018-01-01T12:00' or ts = '2018-01-02';
```

| ts | value |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 123.4 |
| 2018-01-01T12:00:00.000000Z | 589.1 |
| 2018-01-02T00:00:00.000000Z | 131.5 |