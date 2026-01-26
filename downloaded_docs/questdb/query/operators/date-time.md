On this page

This page describes the available operators to assist with performing time-based
calculations.

note

If an operator's first argument is a table's timestamp, QuestDB may use an
[Interval Scan](/docs/concepts/deep-dive/interval-scan/) for optimization.

## `BETWEEN` value1 `AND` value2[​](#between-value1-and-value2 "Direct link to between-value1-and-value2")

The `BETWEEN` operator allows you to specify a non-standard range. It includes
both upper and lower bounds, similar to standard SQL. The order of these bounds
is interchangeable, meaning `BETWEEN X AND Y` is equivalent to
`BETWEEN Y AND X`.

#### Arguments[​](#arguments "Direct link to Arguments")

* `value1` and `value2` can be of `date`, `timestamp`, or `string` type.

#### Examples[​](#examples "Direct link to Examples")

Explicit range

```prism-code
SELECT * FROM trades  
WHERE timestamp BETWEEN '2022-01-01T00:00:23.000000Z' AND '2023-01-01T00:00:23.500000Z';
```

This query returns all records within the specified timestamp range:

| ts | value |
| --- | --- |
| 2018-01-01T00:00:23.000000Z | 123.4 |
| ... | ... |
| 2018-01-01T00:00:23.500000Z | 131.5 |

The `BETWEEN` operator can also accept non-constant bounds. For instance, the
following query returns all records older than one year from the current date:

One year before current date[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20trades%0AWHERE%20timestamp%20BETWEEN%20to_str(now()%2C%20'yyyy-MM-dd')%0AAND%20dateadd('y'%2C%20-1%2C%20to_str(now()%2C%20'yyyy-MM-dd'))%3B&executeQuery=true)

```prism-code
SELECT * FROM trades  
WHERE timestamp BETWEEN to_str(now(), 'yyyy-MM-dd')  
AND dateadd('y', -1, to_str(now(), 'yyyy-MM-dd'));
```

The result set for this query would be:

| ts | score |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 123.4 |
| ... | ... |
| 2018-12-31T23:59:59.999999Z | 115.8 |

Results between two specific timestamps

```prism-code
SELECT * FROM trades WHERE ts BETWEEN '2022-05-23T12:15:00.000000Z' AND '2023-05-23T12:16:00.000000Z';
```

This query returns all records from the 15th minute of 12 PM on May 23, 2018:

| ts | score |
| --- | --- |
| 2018-05-23T12:15:00.000000Z | 123.4 |
| ... | ... |
| 2018-05-23T12:15:59.999999Z | 115.8 |

## `IN` (timeRange)[​](#in-timerange "Direct link to in-timerange")

Returns results within a defined range of time.

#### Arguments[​](#arguments-1 "Direct link to Arguments")

* `timeRange` is a `string` type representing the desired time range.

#### Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the WHERE clause with a partial timestamp comparison](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1NzciIGhlaWdodD0iMjU3Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDE3IDEgMTMgMSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDE3IDkgMTMgOSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMSIgeT0iMyIgd2lkdGg9IjcwIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjkiIHk9IjEiIHdpZHRoPSI3MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzOSIgeT0iMjEiPldIRVJFPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjdGltZXN0YW1wQ29sdW1uIiB4bGluazp0aXRsZT0idGltZXN0YW1wQ29sdW1uIj4KICAgICAgICAgICAgPHJlY3QgeD0iMTIxIiB5PSIzIiB3aWR0aD0iMTM0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjExOSIgeT0iMSIgd2lkdGg9IjEzNCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMTI5IiB5PSIyMSI+dGltZXN0YW1wQ29sdW1uPC90ZXh0PjwvYT48cmVjdCB4PSIyNzUiIHk9IjMiIHdpZHRoPSIzNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI3MyIgeT0iMSIgd2lkdGg9IjM2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjI4MyIgeT0iMjEiPklOPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzNTEiIHk9IjMiIHdpZHRoPSI1MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjM0OSIgeT0iMSIgd2lkdGg9IjUyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM1OSIgeT0iMjEiPnl5eXk8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjM1MSIgeT0iNDciIHdpZHRoPSI4MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjM0OSIgeT0iNDUiIHdpZHRoPSI4MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzNTkiIHk9IjY1Ij55eXl5LU1NPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzNTEiIHk9IjkxIiB3aWR0aD0iMTA2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzQ5IiB5PSI4OSIgd2lkdGg9IjEwNiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzNTkiIHk9IjEwOSI+WVlZWS1NTS1kZDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMzUxIiB5PSIxMzUiIHdpZHRoPSIxMjgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNDkiIHk9IjEzMyIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzNTkiIHk9IjE1MyI+eXl5eS1NTS1kZFRoaDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMzUxIiB5PSIxNzkiIHdpZHRoPSIxNTgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNDkiIHk9IjE3NyIgd2lkdGg9IjE1OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzNTkiIHk9IjE5NyI+eXl5eS1NTS1kZFRoaDptbTwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMzUxIiB5PSIyMjMiIHdpZHRoPSIxNzgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNDkiIHk9IjIyMSIgd2lkdGg9IjE3OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzNTkiIHk9IjI0MSI+eXl5eS1NTS1kZFRoaDptbTpzczwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNzAgMCBoMTAgbTAgMCBoMTAgbTEzNCAwIGgxMCBtMCAwIGgxMCBtMzYgMCBoMTAgbTIwIDAgaDEwIG01MiAwIGgxMCBtMCAwIGgxMjYgbS0yMTggMCBoMjAgbTE5OCAwIGgyMCBtLTIzOCAwIHExMCAwIDEwIDEwIG0yMTggMCBxMCAtMTAgMTAgLTEwIG0tMjI4IDEwIHYyNCBtMjE4IDAgdi0yNCBtLTIxOCAyNCBxMCAxMCAxMCAxMCBtMTk4IDAgcTEwIDAgMTAgLTEwIG0tMjA4IDEwIGgxMCBtODAgMCBoMTAgbTAgMCBoOTggbS0yMDggLTEwIHYyMCBtMjE4IDAgdi0yMCBtLTIxOCAyMCB2MjQgbTIxOCAwIHYtMjQgbS0yMTggMjQgcTAgMTAgMTAgMTAgbTE5OCAwIHExMCAwIDEwIC0xMCBtLTIwOCAxMCBoMTAgbTEwNiAwIGgxMCBtMCAwIGg3MiBtLTIwOCAtMTAgdjIwIG0yMTggMCB2LTIwIG0tMjE4IDIwIHYyNCBtMjE4IDAgdi0yNCBtLTIxOCAyNCBxMCAxMCAxMCAxMCBtMTk4IDAgcTEwIDAgMTAgLTEwIG0tMjA4IDEwIGgxMCBtMTI4IDAgaDEwIG0wIDAgaDUwIG0tMjA4IC0xMCB2MjAgbTIxOCAwIHYtMjAgbS0yMTggMjAgdjI0IG0yMTggMCB2LTI0IG0tMjE4IDI0IHEwIDEwIDEwIDEwIG0xOTggMCBxMTAgMCAxMCAtMTAgbS0yMDggMTAgaDEwIG0xNTggMCBoMTAgbTAgMCBoMjAgbS0yMDggLTEwIHYyMCBtMjE4IDAgdi0yMCBtLTIxOCAyMCB2MjQgbTIxOCAwIHYtMjQgbS0yMTggMjQgcTAgMTAgMTAgMTAgbTE5OCAwIHExMCAwIDEwIC0xMCBtLTIwOCAxMCBoMTAgbTE3OCAwIGgxMCBtMjMgLTIyMCBoLTMiPjwvcGF0aD4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI1NjcgMTcgNTc1IDEzIDU3NSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjU2NyAxNyA1NTkgMTMgNTU5IDIxIj48L3BvbHlnb24+Cjwvc3ZnPg==)

#### Examples[​](#examples-1 "Direct link to Examples")

Results in a given year

```prism-code
SELECT * FROM scores WHERE ts IN '2018';
```

This query returns all records from the year 2018:

| ts | score |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 123.4 |
| ... | ... |
| 2018-12-31T23:59:59.999999Z | 115.8 |

Results in a given minute

```prism-code
SELECT * FROM scores WHERE ts IN '2018-05-23T12:15';
```

This query returns all records from the 15th minute of 12 PM on May 23, 2018:

| ts | score |
| --- | --- |
| 2018-05-23T12:15:00.000000Z | 123.4 |
| ... | ... |
| 2018-05-23T12:15:59.999999Z | 115.8 |

## `IN` (timeRangeWithModifier)[​](#in-timerangewithmodifier "Direct link to in-timerangewithmodifier")

You can apply a modifier to further customize the range. The modifier extends
the upper bound of the original timestamp based on the modifier parameter. An
optional interval with occurrence can be set, to apply the search in the given
time range repeatedly, for a set number of times.

#### Arguments[​](#arguments-2 "Direct link to Arguments")

* `timeRangeWithModifier` is a string in the format
  `'timeRange;modifier;interval;repetition'`.

#### Syntax[​](#syntax-1 "Direct link to Syntax")

![Flow chart showing the syntax of the WHERE clause with a timestamp/modifier comparison](/docs/assets/images/whereTimestampIntervalSearch-e80975394b0c0924c3f3334a6efc0f40.svg)

* `timestamp` is the original time range for the query.
* `modifier` is a signed integer modifying the upper bound applying to the
  `timestamp`:

  + A `positive` value extends the selected period.
  + A `negative` value reduces the selected period.
* `interval` is an unsigned integer indicating the desired interval period for
  the time range.
* `repetition` is an unsigned integer indicating the number of times the
  interval should be applied.

#### Examples[​](#examples-2 "Direct link to Examples")

Modifying the range:

Results in a given year and the first month of the next year

```prism-code
SELECT * FROM scores WHERE ts IN '2018;1M';
```

In this example, the range is the year 2018. The modifier `1M` extends the upper
bound (originally 31 Dec 2018) by one month.

| ts | score |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 123.4 |
| ... | ... |
| 2019-01-31T23:59:59.999999Z | 115.8 |

Results in a given month excluding the last 3 days

```prism-code
SELECT * FROM scores WHERE ts IN '2018-01;-3d';
```

In this example, the range is January 2018. The modifier `-3d` reduces the upper
bound (originally 31 Jan 2018) by 3 days.

| ts | score |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 123.4 |
| ... | ... |
| 2018-01-28T23:59:59.999999Z | 113.8 |

Modifying the interval:

Results on a given date with an interval

```prism-code
SELECT * FROM scores WHERE ts IN '2018-01-01;1d;1y;2';
```

In this example, the range is extended by one day from Jan 1 2018, with a
one-year interval, repeated twice. This means that the query searches for
results on Jan 1-2 in 2018 and in 2019:

| ts | score |
| --- | --- |
| 2018-01-01T00:00:00.000000Z | 123.4 |
| ... | ... |
| 2018-01-02T23:59:59.999999Z | 110.3 |
| 2019-01-01T00:00:00.000000Z | 128.7 |
| ... | ... |
| 2019-01-02T23:59:59.999999Z | 103.8 |

## `IN` (interval)[​](#in-interval "Direct link to in-interval")

Returns results within a defined range of time, as specified by an `interval` value.

#### Arguments[​](#arguments-3 "Direct link to Arguments")

* `interval` is an `interval` type representing the desired time range.

#### Examples[​](#examples-3 "Direct link to Examples")

Check if timestamp is in interval success[Demo this query](https://demo.questdb.io/?query=SELECT%20true%20as%20is_in_interval%20FROM%20trades%0AWHERE%20'2018-05-17T00%3A00%3A00Z'%3A%3Atimestamp%20IN%20interval('2018'%2C%20'2019')%0ALIMIT%20-1&executeQuery=true)

```prism-code
SELECT true as is_in_interval FROM trades  
WHERE '2018-05-17T00:00:00Z'::timestamp IN interval('2018', '2019')  
LIMIT -1
```

| is\_in\_interval |
| --- |
| true |

If we adjust the interval to be not in range, we get no result:

Check if timestamp is in interval failure[Demo this query](https://demo.questdb.io/?query=SELECT%20true%20as%20is_in_interval%20FROM%20trades%0AWHERE%20'2018-05-17T00%3A00%3A00Z'%3A%3Atimestamp%20IN%20interval('2022'%2C%20'2023')%0ALIMIT%20-1%3B&executeQuery=true)

```prism-code
SELECT true as is_in_interval FROM trades  
WHERE '2018-05-17T00:00:00Z'::timestamp IN interval('2022', '2023')  
LIMIT -1;
```

| is\_in\_interval |
| --- |