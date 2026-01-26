On this page

Specify the number and position of records returned by a
[SELECT statement](/docs/query/sql/select/).

Other implementations of SQL sometimes use clauses such as `OFFSET` or `ROWNUM`.
Our implementation uses `LIMIT` for both the offset from start and limit.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the LIMIT keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NDciIGhlaWdodD0iODEiPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iNzAiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjcwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSIyMSI+U0VMRUNUPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc29tZVNlbGVjdFN0YXRlbWVudCIgeGxpbms6dGl0bGU9InNvbWVTZWxlY3RTdGF0ZW1lbnQiPgogICAgICAgICAgICA8cmVjdCB4PSIxMjEiIHk9IjMiIHdpZHRoPSIxNjAiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMTE5IiB5PSIxIiB3aWR0aD0iMTYwIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIxMjkiIHk9IjIxIj5zb21lU2VsZWN0U3RhdGVtZW50PC90ZXh0PjwvYT48cmVjdCB4PSIzMDEiIHk9IjMiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI5OSIgeT0iMSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjMwOSIgeT0iMjEiPkxJTUlUPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjbnVtYmVyT2ZSZWNvcmRzIiB4bGluazp0aXRsZT0ibnVtYmVyT2ZSZWNvcmRzIj4KICAgICAgICAgICAgPHJlY3QgeD0iNDAxIiB5PSIzIiB3aWR0aD0iMTMyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjM5OSIgeT0iMSIgd2lkdGg9IjEzMiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNDA5IiB5PSIyMSI+bnVtYmVyT2ZSZWNvcmRzPC90ZXh0PjwvYT48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI2xvd2VyQm91bmQiIHhsaW5rOnRpdGxlPSJsb3dlckJvdW5kIj4KICAgICAgICAgICAgPHJlY3QgeD0iNDAxIiB5PSI0NyIgd2lkdGg9Ijk0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjM5OSIgeT0iNDUiIHdpZHRoPSI5NCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNDA5IiB5PSI2NSI+bG93ZXJCb3VuZDwvdGV4dD48L2E+PHJlY3QgeD0iNTE1IiB5PSI0NyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNTEzIiB5PSI0NSIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjUyMyIgeT0iNjUiPiw8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN1cHBlckJvdW5kIiB4bGluazp0aXRsZT0idXBwZXJCb3VuZCI+CiAgICAgICAgICAgIDxyZWN0IHg9IjU1OSIgeT0iNDciIHdpZHRoPSI5NiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI1NTciIHk9IjQ1IiB3aWR0aD0iOTYiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjU2NyIgeT0iNjUiPnVwcGVyQm91bmQ8L3RleHQ+PC9hPjxyZWN0IHg9IjY5NSIgeT0iMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNjkzIiB5PSIxIiB3aWR0aD0iMjQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNzAzIiB5PSIyMSI+OzwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNzAgMCBoMTAgbTAgMCBoMTAgbTE2MCAwIGgxMCBtMCAwIGgxMCBtNjAgMCBoMTAgbTIwIDAgaDEwIG0xMzIgMCBoMTAgbTAgMCBoMTIyIG0tMjk0IDAgaDIwIG0yNzQgMCBoMjAgbS0zMTQgMCBxMTAgMCAxMCAxMCBtMjk0IDAgcTAgLTEwIDEwIC0xMCBtLTMwNCAxMCB2MjQgbTI5NCAwIHYtMjQgbS0yOTQgMjQgcTAgMTAgMTAgMTAgbTI3NCAwIHExMCAwIDEwIC0xMCBtLTI4NCAxMCBoMTAgbTk0IDAgaDEwIG0wIDAgaDEwIG0yNCAwIGgxMCBtMCAwIGgxMCBtOTYgMCBoMTAgbTIwIC00NCBoMTAgbTI0IDAgaDEwIG0zIDAgaC0zIj48L3BhdGg+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNzM3IDE3IDc0NSAxMyA3NDUgMjEiPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI3MzcgMTcgNzI5IDEzIDcyOSAyMSI+PC9wb2x5Z29uPgo8L3N2Zz4=)

* `numberOfRecords` is the number of records to return.
* `upperBound` and `lowerBound` is the range of records to return.

Here's the exhaustive list of supported combinations of arguments. `m` and `n`
are positive numbers, and negative numbers are explicitly labeled `-m` and `-n`.

* `LIMIT n`: take the first `n` records
* `LIMIT -n`: take the last `n` records
* `LIMIT m, n`: skip the first `m` records, then take up to record number `n`
  (inclusive)
  + result is the range of records `(m, n]` number 1 denoting the first record
  + if `m > n`, implicitly swap the arguments
  + PostgreSQL equivalent: `OFFSET m LIMIT (n-m)`
* `LIMIT -m, -n`: take the last `m` records, then drop the last `n` records from
  that
  + result is the range of records `[-m, -n)`, number -1 denoting the last
    record
  + if `m < n`, implicitly swap them
* `LIMIT m, -n`: drop the first `m` and the last `n` records. This gives you the
  range `(m, -n)`. These arguments will not be swapped.

These are additional edge-case variants:

* `LIMIT n, 0` = `LIMIT 0, n` = `LIMIT n,` = `LIMIT , n` = `LIMIT n`
* `LIMIT -n, 0` = `LIMIT -n,` = `LIMIT -n`

## Examples[​](#examples "Direct link to Examples")

Examples use this schema and dataset:

```prism-code
CREATE TABLE tango (id LONG);  
INSERT INTO tango VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10);
```

First 5 records

```prism-code
SELECT * FROM tango LIMIT 5;  
  
 id  
----  
 1  
 2  
 3  
 4  
 5
```

Last 5 records

```prism-code
SELECT * FROM tango LIMIT -5;  
  
  
 id  
----  
 6  
 7  
 8  
 9  
 10
```

Records 3, 4, and 5

```prism-code
SELECT * FROM tango LIMIT 2, 5;  
  
 id  
----  
 3  
 4  
 5
```

Records -5 and -4

```prism-code
SELECT * FROM tango LIMIT -5, -3;  
  
 id  
----  
 6  
 7
```

Records 3, 4, ..., -3, -2

```prism-code
SELECT * FROM tango LIMIT 2, -1;  
  
 id  
----  
 3  
 4  
 5  
 6  
 7  
 8  
 9
```

Implicit argument swap, records 3, 4, 5

```prism-code
SELECT * FROM tango LIMIT 5, 2;  
  
 id  
----  
 3  
 4  
 5
```

Implicit argument swap, records -5 and -4

```prism-code
SELECT * FROM tango LIMIT -3, -5;  
  
 id  
----  
 6  
 7
```