On this page

Changes the data type of an existing column in a table.

The data type of the column is altered without affecting the data already stored
in the table. However, it's important to note that altering the column type can
result in data loss or errors if the new type cannot accommodate the existing
data. Therefore, it's recommended to review the data and backup the table before
altering the column type.

caution

* Changing the column type may lead to data loss or errors if the new type
  cannot accommodate the existing data.
* The new data type must be compatible with the existing data in the column.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of ALTER TABLE with ALTER COLUMN TYPE keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NzciIGhlaWdodD0iMzciPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iNjIiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSIyMSI+QUxURVI8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjExMyIgeT0iMyIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTExIiB5PSIxIiB3aWR0aD0iNjIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTIxIiB5PSIyMSI+VEFCTEU8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN0YWJsZU5hbWUiIHhsaW5rOnRpdGxlPSJ0YWJsZU5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSIxOTUiIHk9IjMiIHdpZHRoPSI4OCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIxOTMiIHk9IjEiIHdpZHRoPSI4OCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMjAzIiB5PSIyMSI+dGFibGVOYW1lPC90ZXh0PjwvYT48cmVjdCB4PSIzMDMiIHk9IjMiIHdpZHRoPSI2MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjMwMSIgeT0iMSIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjMxMSIgeT0iMjEiPkFMVEVSPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzODUiIHk9IjMiIHdpZHRoPSI3OCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjM4MyIgeT0iMSIgd2lkdGg9Ijc4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5MyIgeT0iMjEiPkNPTFVNTjwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI2NvbHVtbk5hbWUiIHhsaW5rOnRpdGxlPSJjb2x1bW5OYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iNDgzIiB5PSIzIiB3aWR0aD0iMTAyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjQ4MSIgeT0iMSIgd2lkdGg9IjEwMiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNDkxIiB5PSIyMSI+Y29sdW1uTmFtZTwvdGV4dD48L2E+PHJlY3QgeD0iNjA1IiB5PSIzIiB3aWR0aD0iNTQiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI2MDMiIHk9IjEiIHdpZHRoPSI1NCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI2MTMiIHk9IjIxIj5UWVBFPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjdHlwZURlZiIgeGxpbms6dGl0bGU9InR5cGVEZWYiPgogICAgICAgICAgICA8cmVjdCB4PSI2NzkiIHk9IjMiIHdpZHRoPSI3MCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI2NzciIHk9IjEiIHdpZHRoPSI3MCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNjg3IiB5PSIyMSI+dHlwZURlZjwvdGV4dD48L2E+PHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNjIgMCBoMTAgbTAgMCBoMTAgbTYyIDAgaDEwIG0wIDAgaDEwIG04OCAwIGgxMCBtMCAwIGgxMCBtNjIgMCBoMTAgbTAgMCBoMTAgbTc4IDAgaDEwIG0wIDAgaDEwIG0xMDIgMCBoMTAgbTAgMCBoMTAgbTU0IDAgaDEwIG0wIDAgaDEwIG03MCAwIGgxMCBtMyAwIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9Ijc2NyAxNyA3NzUgMTMgNzc1IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNzY3IDE3IDc1OSAxMyA3NTkgMjEiPjwvcG9seWdvbj4KPC9zdmc+)

## Supported Data Types[​](#supported-data-types "Direct link to Supported Data Types")

The `ALTER TABLE COLUMN TYPE` command supports changing the column type to any
compatible data type.

## Examples[​](#examples "Direct link to Examples")

Change the data type of the column `age` in the table `employees` to `INT`:

```prism-code
ALTER TABLE employees ALTER COLUMN age TYPE INT;
```

When changing the column type, ensure that the new type is compatible with the
existing data. For instance, changing a column type from STRING to DOUBLE might
result in data loss or conversion errors if the existing data contains
non-numeric values.

```prism-code
ALTER TABLE tbl ALTER COLUMN col_name TYPE DOUBLE;
```

It is possible to specify all the additional column type parameters, like
`CAPACITY` & `CACHE`:

```prism-code
ALTER TABLE tbl ALTER COLUMN department TYPE SYMBOL CAPACITY 10000 CACHE;
```

## Available Conversions[​](#available-conversions "Direct link to Available Conversions")

QuestDB supports a wide range of conversions. However, certain type conversions
may lead to data precision loss (e.g., converting a `FLOAT` type to an `INT`) or
range overflow (e.g., converting a `LONG` type to an `INT`). The matrices below
depict fully compatible conversions marked with `X` and conversions that may
result in data loss marked with `L`.

Numeric types support a wide range of conversions, but many of them can result
in the data / precision loss.

| From \ To | boolean | byte | short | int | float | long | double | date | timestamp | timestamp\_ns | decimal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| boolean |  | X | X | X | X | X | X | X | X | X |  |
| byte | L |  | X | X | X | X | X | X | X | X | X |
| short | L | L |  | X | X | X | X | X | X | X | X |
| int | L | L | L |  | L | X | X | X | X | X | X |
| float | L | L | L | L |  | L | X | L | L | L | L |
| long | L | L | L | L | L |  | L | X | X | X | X |
| double | L | L | L | L | X | L |  | L | L | L | L |

Conversions between `TIMESTAMP`, `TIMESTAMP_NS`, and `DATE` types and numeric types are fully
supported. Timestamp values are represented in microseconds since the EPOCH, Timestamp\_ns values
are represented in nanoseconds since the EPOCH,
while Date values are represented in milliseconds since the EPOCH. The EPOCH is
defined as `1970-01-01T00:00:00.000000Z`.

Additionally, when converting from `BOOLEAN` values to numerics, `false` is
represented as `0`, and `true` is represented as `1`. On the way back `0` and
`NULL` are converted to `false` and all other values converted to `true`.

| From \ To | boolean | byte | short | int | float | long | double | date | timestamp | timestamp\_ns | decimal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| date | L | L | L | L | L | X | X |  | X | X |  |
| timestamp | L | L | L | L | L | X | X | L |  |  |  |
| timestamp\_ns | L | L | L | L | L | X | X | L | L |  |  |

Conversions to `SYMBOL`, `STRING` and `VARCHAR` are supported from most of the
data types.

| From \ To | symbol | string | varchar |
| --- | --- | --- | --- |
| boolean | X | X | X |
| byte | X | X | X |
| short | X | X | X |
| int | X | X | X |
| float | X | X | X |
| long | X | X | X |
| date | X | X | X |
| timestamp | X | X | X |
| timestamp\_ns | X | X | X |
| double | X | X | X |
| decimal |  | X | X |
| ipv4 | X | X | X |
| char | X | X | X |
| uuid | X | X | X |
| symbol |  | X | X |
| string | X |  | X |
| varchar | X | X |  |

However conversion from `SYMBOL`, `STRING` and `VARCHAR` to other types can
result in `NULL` values for inconvertable string values.

| From \ To | boolean | byte | short | char | int | float | long | date | timestamp | timestamp\_ns | double | uuid | decimal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| string | L | L | L | L | L | L | L | L | L | L | L | L | L |
| varchar | L | L | L | L | L | L | L | L | L | L | L | L | L |
| symbol | L | L | L | L | L | L | L | L | L | L | L | L |  |

When column type change results into range overflow or precision loss, the same
rules as explicit [CAST](/docs/query/sql/cast/) apply.

## Unsupported Conversions[​](#unsupported-conversions "Direct link to Unsupported Conversions")

Converting from the type to itself is not supported.

If the column `department` is of type `SYMBOL`, then the following query will
result in error, even if the capacity parameter changes:

```prism-code
ALTER TABLE employees ALTER COLUMN department TYPE SYMBOL CAPACITY 4096;
```