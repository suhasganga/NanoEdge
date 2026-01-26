On this page

## Overview[​](#overview "Direct link to Overview")

`UNION`, `EXCEPT`, and `INTERSECT` perform set operations.

`UNION` is used to combine the results of two or more queries.

`EXCEPT` and `INTERSECT` return distinct rows by comparing the results of two
queries.

To work properly, all of the following must be true:

* Each query statement should return the same number of column.
* Each column to be combined should have data types that are either the same, or
  supported by `implicit cast`. For example, IPv4 columns can be combined with VARCHAR/STRING
  columns as they will be automatically cast. See [CAST](/docs/query/sql/cast/) for more
  information.

  + Example:

    ```prism-code
    select '1'::varchar as col from long_sequence(1)  
    union all  
    select '127.0.0.1'::ipv4 from long_sequence(1);
    ```
* Columns in each query statement should be in the same order.

## Syntax[​](#syntax "Direct link to Syntax")

### UNION[​](#union "Direct link to UNION")

![Flow chart showing the syntax of the UNION, EXCEPT &amp; INTERSECT keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0ODMiIGhlaWdodD0iMTI1Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDE3IDEgMTMgMSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDE3IDkgMTMgOSAyMSI+PC9wb2x5Z29uPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjcXVlcnlfMSIgeGxpbms6dGl0bGU9InF1ZXJ5XzEiPgogICAgICAgICAgICA8cmVjdCB4PSIzMSIgeT0iMyIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjI5IiB5PSIxIiB3aWR0aD0iNzIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjM5IiB5PSIyMSI+cXVlcnlfMTwvdGV4dD48L2E+PHJlY3QgeD0iMTQzIiB5PSIzIiB3aWR0aD0iNjYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxNDEiIHk9IjEiIHdpZHRoPSI2NiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxNTEiIHk9IjIxIj5VTklPTjwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTQzIiB5PSI0NyIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTQxIiB5PSI0NSIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE1MSIgeT0iNjUiPkVYQ0VQVDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTQzIiB5PSI5MSIgd2lkdGg9Ijk2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTQxIiB5PSI4OSIgd2lkdGg9Ijk2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE1MSIgeT0iMTA5Ij5JTlRFUlNFQ1Q8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjI5OSIgeT0iMzUiIHdpZHRoPSI0NCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI5NyIgeT0iMzMiIHdpZHRoPSI0NCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzMDciIHk9IjUzIj5BTEw8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNxdWVyeV8yIiB4bGluazp0aXRsZT0icXVlcnlfMiI+CiAgICAgICAgICAgIDxyZWN0IHg9IjM4MyIgeT0iMyIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjM4MSIgeT0iMSIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzOTEiIHk9IjIxIj5xdWVyeV8yPC90ZXh0PjwvYT48cGF0aCBjbGFzcz0ibGluZSIgZD0ibTE3IDE3IGgyIG0wIDAgaDEwIG03MiAwIGgxMCBtMjAgMCBoMTAgbTY2IDAgaDEwIG0wIDAgaDMwIG0tMTM2IDAgaDIwIG0xMTYgMCBoMjAgbS0xNTYgMCBxMTAgMCAxMCAxMCBtMTM2IDAgcTAgLTEwIDEwIC0xMCBtLTE0NiAxMCB2MjQgbTEzNiAwIHYtMjQgbS0xMzYgMjQgcTAgMTAgMTAgMTAgbTExNiAwIHExMCAwIDEwIC0xMCBtLTEyNiAxMCBoMTAgbTcyIDAgaDEwIG0wIDAgaDI0IG0tMTI2IC0xMCB2MjAgbTEzNiAwIHYtMjAgbS0xMzYgMjAgdjI0IG0xMzYgMCB2LTI0IG0tMTM2IDI0IHEwIDEwIDEwIDEwIG0xMTYgMCBxMTAgMCAxMCAtMTAgbS0xMjYgMTAgaDEwIG05NiAwIGgxMCBtNDAgLTg4IGgxMCBtMCAwIGg1NCBtLTg0IDAgaDIwIG02NCAwIGgyMCBtLTEwNCAwIHExMCAwIDEwIDEwIG04NCAwIHEwIC0xMCAxMCAtMTAgbS05NCAxMCB2MTIgbTg0IDAgdi0xMiBtLTg0IDEyIHEwIDEwIDEwIDEwIG02NCAwIHExMCAwIDEwIC0xMCBtLTc0IDEwIGgxMCBtNDQgMCBoMTAgbTIwIC0zMiBoMTAgbTcyIDAgaDEwIG0zIDAgaC0zIj48L3BhdGg+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNDczIDE3IDQ4MSAxMyA0ODEgMjEiPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI0NzMgMTcgNDY1IDEzIDQ2NSAyMSI+PC9wb2x5Z29uPgo8L3N2Zz4=)

* `UNION` returns distinct results.
* `UNION ALL` returns all `UNION` results including duplicates.
* `EXCEPT` returns distinct rows from the left input query that are not returned
  by the right input query.
* `EXCEPT ALL` returns all `EXCEPT` results including duplicates.
* `INTERSECT` returns distinct rows that are returned by both input queries.
* `INTERSECT ALL` returns all `INTERSECT` results including duplicates.

## Examples[​](#examples "Direct link to Examples")

The examples for the set operations use the following tables:

sensor\_1:

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | New York |
| 2 | United Automation | Miami |
| 3 | Omron | Miami |
| 4 | Honeywell | San Francisco |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |
| 1 | Honeywell | New York |

Notice that the last row in the sensor\_1 table is a duplicate.

sensor\_2:

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | San Francisco |
| 2 | United Automation | Boston |
| 3 | Eberle | New York |
| 4 | Honeywell | Boston |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |

### UNION[​](#union-1 "Direct link to UNION")

```prism-code
sensor_1 UNION sensor_2;
```

returns

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | New York |
| 2 | United Automation | Miami |
| 3 | Omron | Miami |
| 4 | Honeywell | San Francisco |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |
| 1 | Honeywell | San Francisco |
| 2 | United Automation | Boston |
| 3 | Eberle | New York |
| 4 | Honeywell | Boston |

`UNION` eliminates duplication even when one of the queries returns nothing.

For instance:

```prism-code
sensor_1  
UNION  
sensor_2 WHERE ID > 10;
```

returns:

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | New York |
| 2 | United Automation | Miami |
| 3 | Omron | Miami |
| 4 | Honeywell | San Francisco |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |

The duplicate row in `sensor_1` is not returned as a result.

```prism-code
sensor_1 UNION ALL sensor_2;
```

returns

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | New York |
| 2 | United Automation | Miami |
| 3 | Omron | Miami |
| 4 | Honeywell | San Francisco |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |
| 1 | Honeywell | San Francisco |
| 2 | United Automation | Boston |
| 3 | Eberle | New York |
| 4 | Honeywell | Boston |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |

### EXCEPT[​](#except "Direct link to EXCEPT")

```prism-code
sensor_1 EXCEPT sensor_2;
```

returns

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | New York |
| 2 | United Automation | Miami |
| 3 | Omron | Miami |
| 4 | Honeywell | San Francisco |

Notice that `EXCEPT` eliminates duplicates. Let's run `EXCEPT ALL` to change
that.

```prism-code
sensor_1 EXCEPT ALL sensor_2;
```

| ID | make | city |
| --- | --- | --- |
| 1 | Honeywell | New York |
| 2 | United Automation | Miami |
| 3 | Omron | Miami |
| 4 | Honeywell | San Francisco |
| 1 | Honeywell | New York |

### INTERSECT[​](#intersect "Direct link to INTERSECT")

```prism-code
sensor_1 INTERSECT sensor_2;
```

returns

| ID | make | city |
| --- | --- | --- |
| 5 | Omron | Boston |
| 6 | RS Pro | Boston |

In this example we have no duplicates, but if there were any, we could use
`INTERSECT ALL` to have them.

## Keyword execution priority[​](#keyword-execution-priority "Direct link to Keyword execution priority")

The QuestDB's engine processes the keywords from left to right, unless the
priority is defined by parenthesis.

For example:

```prism-code
query_1 UNION query_2 EXCEPT query_3;
```

is executed as:

```prism-code
(query_1 UNION query_2) EXCEPT query_3;
```

Similarly, the following syntax:

```prism-code
query_1 UNION query_2 INTERSECT query_3;
```

is executed as:

```prism-code
(query_1 UNION query_2) INTERSECT query_3;
```

## Clauses[​](#clauses "Direct link to Clauses")

The set operations can be used with clauses such as `LIMIT`, `ORDER BY`, and
`WHERE`. However, when the clause keywords are added after the set operations,
the execution order for different clauses varies.

For `LIMIT` and `ORDER BY`, the clauses are applied after the set operations.

For example:

```prism-code
query_1 UNION query_2  
LIMIT 3;
```

is executed as:

```prism-code
(query_1 UNION query_2)  
LIMIT 3;
```

For `WHERE`, the clause is applied first to the query immediate prior to it.

```prism-code
query_1 UNION query_2  
WHERE value = 1;
```

is executed as:

```prism-code
query_1 UNION (query_2 WHERE value = 1);
```

note

* QuestDB applies `GROUP BY` implicitly. See
  [GROUP BY reference](/docs/query/sql/group-by/) for more information.
* Quest does not support the clause `HAVING` yet.

## Alias[​](#alias "Direct link to Alias")

When different aliases are used with set operations, the execution follows a
left-right order and the output uses the first alias.

For example:

```prism-code
SELECT alias_1 FROM table_1  
UNION  
SELECT alias_2 FROM table_2;
```

The output shows `alias_1`.