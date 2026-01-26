On this page

## generate\_series[​](#generate_series "Direct link to generate_series")

Use `generate_series` to generate a pseudo-table with an arithmetic series in a
single column. You can call it in isolation (`generate_series(...)`), or as part of
a SELECT statement (`SELECT * FROM generate_series(...)`).

This function can generate a `LONG` or `DOUBLE` series. There is also a
[variant](/docs/query/functions/timestamp-generator/#generate_series)
that generates a `TIMESTAMP` series.

The `start` and `end` values are interchangeable, and you can use a negative
`step` value to obtain a descending arithmetic series.

The series is inclusive on both ends.

The step argument is optional, and defaults to 1.

**Arguments:**

`generate_series(start_long, end_long, step_long)` - generates a series of
longs.

`generate_series(start_double, end_double, step_double)` - generates a series of
doubles.

**Return value:**

The column type of the pseudo-table is either `LONG` or `DOUBLE`, according to
the type of the arguments.

**Examples:**

Ascending LONG series[Demo this query](https://demo.questdb.io/?query=generate_series(-3%2C%203%2C%201)%3B%0A--%20or%0Agenerate_series(-3%2C%203)%3B&executeQuery=true)

```prism-code
generate_series(-3, 3, 1);  
-- or  
generate_series(-3, 3);
```

| generate\_series |
| --- |
| -3 |
| -2 |
| -1 |
| 0 |
| 1 |
| 2 |
| 3 |

Descending LONG series[Demo this query](https://demo.questdb.io/?query=generate_series(3%2C%20-3%2C%20-1)%3B&executeQuery=true)

```prism-code
generate_series(3, -3, -1);
```

| generate\_series |
| --- |
| 3 |
| 2 |
| 1 |
| 0 |
| -1 |
| -2 |
| -3 |

Ascending DOUBLE series[Demo this query](https://demo.questdb.io/?query=generate_series(-3d%2C%203d%2C%201d)%3B%0A--%20or%0Agenerate_series(-3d%2C%203d)%3B&executeQuery=true)

```prism-code
generate_series(-3d, 3d, 1d);  
-- or  
generate_series(-3d, 3d);
```

| generate\_series |
| --- |
| -3.0 |
| -2.0 |
| -1.0 |
| 0.0 |
| 1.0 |
| 2.0 |
| 3.0 |

Descending DOUBLE series[Demo this query](https://demo.questdb.io/?query=generate_series(-3d%2C%203d%2C%20-1d)%3B&executeQuery=true)

```prism-code
generate_series(-3d, 3d, -1d);
```

| generate\_series |
| --- |
| 3.0 |
| 2.0 |
| 1.0 |
| 0.0 |
| -1.0 |
| -2.0 |
| -3.0 |

## long\_sequence[​](#long_sequence "Direct link to long_sequence")

Use `long_sequence()` as a row generator to create table data for testing. The
function deals with two concerns:

* generates a pseudo-table with an ascending series of LONG numbers starting at
  1
* serves as the provider of pseudo-randomness to all the
  [random value functions](/docs/query/functions/random-value-generator/)

Basic usage of this function involves providing the number of rows to generate.
You can achieve deterministic pseudo-random behavior by providing the random
seed values.

* `long_sequence(num_rows)` — generates rows with a random seed
* `long_sequence(num_rows, seed1, seed2)` — generates rows deterministically

tip

Deterministic procedural generation makes it easy to test on vast amounts of
data without moving large files across machines. Using the same seed on any
machine at any time will consistently produce the same results for all random
functions.

**Arguments:**

* `num_rows` — `long` representing the number of rows to generate
* `seed1` and `seed2` — `long` numbers that combine into a `long128` seed

**Examples:**

Generate multiple rows

```prism-code
SELECT x, rnd_double()  
FROM long_sequence(5);
```

| x | rnd\_double |
| --- | --- |
| 1 | 0.3279246687 |
| 2 | 0.8341038236 |
| 3 | 0.1023834675 |
| 4 | 0.9130602021 |
| 5 | 0.718276777 |

Access row\_number using the x column

```prism-code
SELECT x, x*x  
FROM long_sequence(5);
```

| x | x\*x |
| --- | --- |
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |

Use with a fixed random seed

```prism-code
SELECT rnd_double()  
FROM long_sequence(2,128349234,4327897);
```

note

The results below will be the same on any machine at any time as long as they
use the same seed in `long_sequence`.

| rnd\_double |
| --- |
| 0.8251337821991485 |
| 0.2714941145110299 |