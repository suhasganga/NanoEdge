On this page

Type conversion. Can be either:

* [Explicit](#explicit-conversion) via `cast()`
* [Implicit](#implicit-conversion), in which case it will be automatically
  performed when required by the context.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the CAST keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NDMiIGhlaWdodD0iMzciPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iNTYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjU2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSIyMSI+Q0FTVDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTA3IiB5PSIzIiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxMDUiIHk9IjEiIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxMTUiIHk9IjIxIj4oPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjZXhwcmVzc2lvbiIgeGxpbms6dGl0bGU9ImV4cHJlc3Npb24iPgogICAgICAgICAgICA8cmVjdCB4PSIxNTMiIHk9IjMiIHdpZHRoPSI5MCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIxNTEiIHk9IjEiIHdpZHRoPSI5MCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMTYxIiB5PSIyMSI+ZXhwcmVzc2lvbjwvdGV4dD48L2E+PHJlY3QgeD0iMjYzIiB5PSIzIiB3aWR0aD0iMzgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyNjEiIHk9IjEiIHdpZHRoPSIzOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyNzEiIHk9IjIxIj5BUzwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3R5cGUiIHhsaW5rOnRpdGxlPSJ0eXBlIj4KICAgICAgICAgICAgPHJlY3QgeD0iMzIxIiB5PSIzIiB3aWR0aD0iNDgiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMzE5IiB5PSIxIiB3aWR0aD0iNDgiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjMyOSIgeT0iMjEiPnR5cGU8L3RleHQ+PC9hPjxyZWN0IHg9IjM4OSIgeT0iMyIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzg3IiB5PSIxIiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzk3IiB5PSIyMSI+KTwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNTYgMCBoMTAgbTAgMCBoMTAgbTI2IDAgaDEwIG0wIDAgaDEwIG05MCAwIGgxMCBtMCAwIGgxMCBtMzggMCBoMTAgbTAgMCBoMTAgbTQ4IDAgaDEwIG0wIDAgaDEwIG0yNiAwIGgxMCBtMyAwIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjQzMyAxNyA0NDEgMTMgNDQxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNDMzIDE3IDQyNSAxMyA0MjUgMjEiPjwvcG9seWdvbj4KPC9zdmc+)

where:

* `expression` can be a constant, a column, or an expression that evaluates to a
  value.
* `type` refers to the desired [data type](/docs/query/datatypes/overview/).

`cast` can be used a part of arithmetic expression as normal

## Explicit conversion[​](#explicit-conversion "Direct link to Explicit conversion")

Types can be converted from one to another using the `cast()` function.

## Examples[​](#examples "Direct link to Examples")

Queries

```prism-code
SELECT  
cast(3L + 2L AS INT) cast1,  
cast(1578506142000000 AS TIMESTAMP) cast2,  
cast(1578506142000000 AS TIMESTAMP_NS) cast3,  
cast('10.2' AS DOUBLE) cast4,  
cast('1' AS INT) cast5;
```

| cast1 | cast2 | cast3 | cast4 | cast5 |
| --- | --- | --- | --- | --- |
| 5 | 2020-01-08T17:55:42.000000Z | 1970-01-19T06:28:26.142000000Z | 10.2 | 1 |

Explicit casting of an expression to a smaller
[data type](/docs/query/datatypes/overview/) may result in loss of data when the
output data type is smaller than the expression.

* Casting a decimal number type (`float` or `double`) to an integer number type
  (`long`, `int`, `short`) will result in decimals drop.
* If the integer part being cast is larger than the resulting data type, it will
  be resized by truncating bits.
* Conversions from `char` to a number type will return the corresponding
  `unicode` number and vice versa.

### Precision loss examples[​](#precision-loss-examples "Direct link to Precision loss examples")

Queries

```prism-code
SELECT  
cast(3.5 + 2 AS INT),  
cast(7234623 AS SHORT),  
cast(2334444.323 AS SHORT);
```

| cast | cast1 | cast2 |
| --- | --- | --- |
| 5 | 25663 | -24852 |

When casting numbers into a smaller data type, QuestDB will truncate the higher
bits of this number.

## Implicit conversion[​](#implicit-conversion "Direct link to Implicit conversion")

Type casting may be necessary in certain context such as

* Operations involving various different types
* Inserting values where the originating type is different from the destination
  column type.

QuestDB will attempt to convert to the data type required by the context. This
is called `implicit cast` and does not require using the `cast()` function.

Implicit casts are only performed when they would **NOT**:

1. Reduce overall precision
2. Truncate potential results

Implicit casting also prevents data loss.

When an operation involves multiple types, the resulting type will be the
smallest possible type so that no data is lost.

## Casting table[​](#casting-table "Direct link to Casting table")

The below chart illustrates the explicit and implicit cast available in QuestDB:

![Table showing the different possibilities the cast function supports, those are defined by an input and output types](/docs/assets/images/castmap-66992e88a17812313b70f327009d8e54.jpg)

Queries

```prism-code
SELECT  
1234L + 567,  
1234L + 0.567,  
to_timestamp('2019-10-17T00:00:00', 'yyyy-MM-ddTHH:mm:ss') + 323,  
to_timestamp('2019-10-17T00:00:00', 'yyyy-MM-ddTHH:mm:ss') + 0.323;
```

| column | column1 | column2 | column3 |
| --- | --- | --- | --- |
| 1801 | 1234.567 | 2019-10-17T00:00:00.000323Z | 1571270400000000 |

## Alternate syntax[​](#alternate-syntax "Direct link to Alternate syntax")

There is a shorthand cast syntax.

Using the above example:

Queries, long form

```prism-code
SELECT  
cast(3.5 + 2 AS INT),  
cast(7234623 AS SHORT),  
cast(2334444.323 AS SHORT);
```

We can use the `::` syntax to shorten things up:

Queries, short hand

```prism-code
SELECT  
    (3.5 + 2)::INT,  
    7234623::SHORT,  
    2334444.323::SHORT;
```

Which to choose?

It's all preference, however many consider the short hand to be more readable.