On this page

This page describes the available functions to assist with performing boolean
calculations on numeric and timestamp types.

## isOrdered[​](#isordered "Direct link to isOrdered")

`isOrdered(column)` return a `boolean` indicating whether the column values are
ordered in a table.

**Arguments:**

* `column` is a column name of numeric or timestamp type.

**Return value:**

Return value type is `boolean`.

**Examples:**

Given a table with the following contents:

| numeric\_sequence | ts |
| --- | --- |
| 1 | 2021-05-01T11:00:00.000000Z |
| 2 | 2021-05-01T12:00:00.000000Z |
| 3 | 2021-05-01T13:00:00.000000Z |

```prism-code
SELECT isOrdered(numeric_sequence) is_num_ordered,  
       isOrdered(ts) is_ts_ordered  
FROM my_table
```

| is\_num\_ordered | is\_ts\_ordered |
| --- | --- |
| true | true |

Adding an integer and timestamp rows out-of-order

| numeric\_sequence | ts |
| --- | --- |
| 1 | 2021-05-01T11:00:00.000000Z |
| 2 | 2021-05-01T12:00:00.000000Z |
| 3 | 2021-05-01T13:00:00.000000Z |
| 2 | 2021-05-01T12:00:00.000000Z |

```prism-code
SELECT isOrdered(numeric_sequence) FROM my_table
```

| is\_num\_ordered | is\_ts\_ordered |
| --- | --- |
| false | false |

## SELECT boolean expressions[​](#select-boolean-expressions "Direct link to SELECT boolean expressions")

If you'd like to apply boolean logic in your SELECT expressions, see the
[SELECT reference](/docs/query/sql/select/).