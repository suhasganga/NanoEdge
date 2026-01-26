On this page

Gracefully stops the execution of a running query.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the CANCEL QUERY keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMDciIGhlaWdodD0iMzciPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iNzQiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9Ijc0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSIyMSI+Q0FOQ0VMPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxMjUiIHk9IjMiIHdpZHRoPSI2NiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjEyMyIgeT0iMSIgd2lkdGg9IjY2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjEzMyIgeT0iMjEiPlFVRVJZPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjcXVlcnlJZCIgeGxpbms6dGl0bGU9InF1ZXJ5SWQiPgogICAgICAgICAgICA8cmVjdCB4PSIyMTEiIHk9IjMiIHdpZHRoPSI2OCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIyMDkiIHk9IjEiIHdpZHRoPSI2OCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMjE5IiB5PSIyMSI+cXVlcnlJZDwvdGV4dD48L2E+PHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNzQgMCBoMTAgbTAgMCBoMTAgbTY2IDAgaDEwIG0wIDAgaDEwIG02OCAwIGgxMCBtMyAwIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjI5NyAxNyAzMDUgMTMgMzA1IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMjk3IDE3IDI4OSAxMyAyODkgMjEiPjwvcG9seWdvbj4KPC9zdmc+)

## Description[​](#description "Direct link to Description")

The `CANCEL QUERY` command sets a flag that is periodically checked by the
running target query. Cancelling depends on how often the flag is checked. It
may not be immediate.

The `query_id` is the unique non-negative identification number of a running
query in query registry.

`CANCEL QUERY` returns an error if:

1. The given `query_id` is negative
2. The query can't be found in registry

A `query_id` is found via the
[`query_activity()`](/docs/query/functions/meta/#query_activity)
meta-function.

## Examples[​](#examples "Direct link to Examples")

Consider we have two open tabs of the QuestDB [Web Console](/docs/getting-started/web-console/overview/).

If we execute the following command in the first tab:

```prism-code
CREATE TABLE test AS (SELECT x FROM long_sequence(1000000000));
```

We can then check that the query is running in the second tab with the
[`query_activity()`](/docs/query/functions/meta/#query_activity)
meta-function:

```prism-code
SELECT * FROM query_activity();
```

| query\_id | worker\_id | worker\_pool | username | query\_start | state\_change | state | query |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 29 | 1 | shared | joe | 2024-01-09T10:51:05.878627Z | 2024-01-09T10:51:05.878627Z | active | CREATE TABLE test\_tab AS (SELECT x FROM long\_sequence(10000000000)); |
| 30 | 21 | shared | joe | 2024-01-09T10:51:10.661032Z | 2024-01-09T10:51:10.661032Z | active | SELECT \* FROM query\_activity(); |

We see that the two latest queries have `query_id`'s of 29 and 30, respectively.

Want to cancel it?

There are two methods:

```prism-code
CANCEL QUERY 29;
```

Or:

```prism-code
SELECT cancel_query(29)
```

After execution, the query then gets interrupted and returns a
`cancelled by user` error in the first tab where the query was launched.

The `cancel_query()` function may cancel multiple queries at the same time or
cancel without the need to lookup a specific `query_id`. You can do so by
chaining with a [`LIKE`](/docs/query/functions/pattern-matching/#likeilike)
operator:

```prism-code
SELECT cancel_query(query_id)  
FROM query_activity()  
WHERE query LIKE 'CREATE TABLE test_tab%'
```

This expression returns `true` if query was found in the registry and if the
cancellation was set. Otherwise, it returns `false`.