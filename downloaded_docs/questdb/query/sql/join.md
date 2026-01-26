On this page

QuestDB supports the type of joins you can frequently find in
[relational databases](https://questdb.com/glossary/relational-database/): `INNER`, `LEFT (OUTER)`,
`CROSS`. Additionally, it implements joins which are particularly useful for
time-series analytics: `ASOF`, `LT`, `SPLICE`, and `WINDOW`. `FULL` joins are
not yet implemented and are on our roadmap.

All supported join types can be combined in a single SQL statement; QuestDB
SQL's optimizer determines the best execution order and algorithms.

There are no known limitations on the size of tables or sub-queries used in
joins and there are no limitations on the number of joins, either.

## Syntax[​](#syntax "Direct link to Syntax")

High-level overview:

![Flow chart showing the syntax of the high-level syntax of the JOIN keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1NDEiIGhlaWdodD0iNjkiPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNzZWxlY3RDbGF1c2UiIHhsaW5rOnRpdGxlPSJzZWxlY3RDbGF1c2UiPgogICAgICAgICAgICA8cmVjdCB4PSIzMSIgeT0iMyIgd2lkdGg9IjEwMCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjEwMCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMzkiIHk9IjIxIj5zZWxlY3RDbGF1c2U8L3RleHQ+PC9hPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjam9pblN0YXRlbWVudCIgeGxpbms6dGl0bGU9ImpvaW5TdGF0ZW1lbnQiPgogICAgICAgICAgICA8cmVjdCB4PSIxNTEiIHk9IjMiIHdpZHRoPSIxMTAiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMTQ5IiB5PSIxIiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIxNTkiIHk9IjIxIj5qb2luU3RhdGVtZW50PC90ZXh0PjwvYT48cmVjdCB4PSIzMDEiIHk9IjM1IiB3aWR0aD0iNzAiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOTkiIHk9IjMzIiB3aWR0aD0iNzAiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzA5IiB5PSI1MyI+V0hFUkU8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN3aGVyZUNsYXVzZSIgeGxpbms6dGl0bGU9IndoZXJlQ2xhdXNlIj4KICAgICAgICAgICAgPHJlY3QgeD0iMzkxIiB5PSIzNSIgd2lkdGg9IjEwMiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIzODkiIHk9IjMzIiB3aWR0aD0iMTAyIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzOTkiIHk9IjUzIj53aGVyZUNsYXVzZTwvdGV4dD48L2E+PHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtMTAwIDAgaDEwIG0wIDAgaDEwIG0xMTAgMCBoMTAgbTIwIDAgaDEwIG0wIDAgaDIwMiBtLTIzMiAwIGgyMCBtMjEyIDAgaDIwIG0tMjUyIDAgcTEwIDAgMTAgMTAgbTIzMiAwIHEwIC0xMCAxMCAtMTAgbS0yNDIgMTAgdjEyIG0yMzIgMCB2LTEyIG0tMjMyIDEyIHEwIDEwIDEwIDEwIG0yMTIgMCBxMTAgMCAxMCAtMTAgbS0yMjIgMTAgaDEwIG03MCAwIGgxMCBtMCAwIGgxMCBtMTAyIDAgaDEwIG0yMyAtMzIgaC0zIj48L3BhdGg+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNTMxIDE3IDUzOSAxMyA1MzkgMjEiPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI1MzEgMTcgNTIzIDEzIDUyMyAyMSI+PC9wb2x5Z29uPgo8L3N2Zz4=)

* `selectClause` - see [SELECT](/docs/query/sql/select/) for more
  information.
* `whereClause` - see [WHERE](/docs/query/sql/where/) for more information.
* The specific syntax for `joinClause` depends on the type of `JOIN`:

  + `INNER` and `LEFT` `JOIN` has a mandatory `ON` clause allowing arbitrary
    `JOIN` predicates, `operator`:

  ![Flow chart showing the syntax of the INNER, LEFT JOIN keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5NjkiIGhlaWdodD0iMTg1Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDYxIDEgNTcgMSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDYxIDkgNTcgOSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSI1MSIgeT0iNzkiIHdpZHRoPSI2NCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQ5IiB5PSI3NyIgd2lkdGg9IjY0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjU5IiB5PSI5NyI+SU5ORVI8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjUxIiB5PSIxMjMiIHdpZHRoPSI1MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQ5IiB5PSIxMjEiIHdpZHRoPSI1MiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI1OSIgeT0iMTQxIj5MRUZUPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxNTUiIHk9IjQ3IiB3aWR0aD0iNTQiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxNTMiIHk9IjQ1IiB3aWR0aD0iNTQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTYzIiB5PSI2NSI+Sk9JTjwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3RhYmxlIiB4bGluazp0aXRsZT0idGFibGUiPgogICAgICAgICAgICA8cmVjdCB4PSIyNDkiIHk9IjQ3IiB3aWR0aD0iNTIiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMjQ3IiB5PSI0NSIgd2lkdGg9IjUyIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIyNTciIHk9IjY1Ij50YWJsZTwvdGV4dD48L2E+PHJlY3QgeD0iMjQ5IiB5PSI5MSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjQ3IiB5PSI4OSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjI1NyIgeT0iMTA5Ij4oPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc3ViLXF1ZXJ5IiB4bGluazp0aXRsZT0ic3ViLXF1ZXJ5Ij4KICAgICAgICAgICAgPHJlY3QgeD0iMjk1IiB5PSI5MSIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjI5MyIgeT0iODkiIHdpZHRoPSI4NCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMzAzIiB5PSIxMDkiPnN1Yi1xdWVyeTwvdGV4dD48L2E+PHJlY3QgeD0iMzk5IiB5PSI5MSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzk3IiB5PSI4OSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjQwNyIgeT0iMTA5Ij4pPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI0ODUiIHk9IjQ3IiB3aWR0aD0iNDAiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI0ODMiIHk9IjQ1IiB3aWR0aD0iNDAiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDkzIiB5PSI2NSI+T048L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNjb2x1bW4iIHhsaW5rOnRpdGxlPSJjb2x1bW4iPgogICAgICAgICAgICA8cmVjdCB4PSI1ODUiIHk9IjQ3IiB3aWR0aD0iNjQiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iNTgzIiB5PSI0NSIgd2lkdGg9IjY0IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSI1OTMiIHk9IjY1Ij5jb2x1bW48L3RleHQ+PC9hPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjb3BlcmF0b3IiIHhsaW5rOnRpdGxlPSJvcGVyYXRvciI+CiAgICAgICAgICAgIDxyZWN0IHg9IjY2OSIgeT0iNDciIHdpZHRoPSI3NCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI2NjciIHk9IjQ1IiB3aWR0aD0iNzQiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjY3NyIgeT0iNjUiPm9wZXJhdG9yPC90ZXh0PjwvYT48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI2Fub3RoZXJDb2x1bW4iIHhsaW5rOnRpdGxlPSJhbm90aGVyQ29sdW1uIj4KICAgICAgICAgICAgPHJlY3QgeD0iNzYzIiB5PSI0NyIgd2lkdGg9IjExOCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI3NjEiIHk9IjQ1IiB3aWR0aD0iMTE4IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSI3NzEiIHk9IjY1Ij5hbm90aGVyQ29sdW1uPC90ZXh0PjwvYT48cmVjdCB4PSI1ODUiIHk9IjMiIHdpZHRoPSI0OCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjU4MyIgeT0iMSIgd2lkdGg9IjQ4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjU5MyIgeT0iMjEiPkFORDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNTY1IiB5PSIxMzUiIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjU2MyIgeT0iMTMzIiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNTczIiB5PSIxNTMiPig8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNjb2x1bW4iIHhsaW5rOnRpdGxlPSJjb2x1bW4iPgogICAgICAgICAgICA8cmVjdCB4PSI2MzEiIHk9IjEzNSIgd2lkdGg9IjY0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjYyOSIgeT0iMTMzIiB3aWR0aD0iNjQiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjYzOSIgeT0iMTUzIj5jb2x1bW48L3RleHQ+PC9hPjxyZWN0IHg9IjYzMSIgeT0iOTEiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjYyOSIgeT0iODkiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI2MzkiIHk9IjEwOSI+LDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNzM1IiB5PSIxMzUiIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjczMyIgeT0iMTMzIiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNzQzIiB5PSIxNTMiPik8L3RleHQ+CiAgICAgICAgIDxwYXRoIGNsYXNzPSJsaW5lIiBkPSJtMTcgNjEgaDIgbTIwIDAgaDEwIG0wIDAgaDc0IG0tMTA0IDAgaDIwIG04NCAwIGgyMCBtLTEyNCAwIHExMCAwIDEwIDEwIG0xMDQgMCBxMCAtMTAgMTAgLTEwIG0tMTE0IDEwIHYxMiBtMTA0IDAgdi0xMiBtLTEwNCAxMiBxMCAxMCAxMCAxMCBtODQgMCBxMTAgMCAxMCAtMTAgbS05NCAxMCBoMTAgbTY0IDAgaDEwIG0tOTQgLTEwIHYyMCBtMTA0IDAgdi0yMCBtLTEwNCAyMCB2MjQgbTEwNCAwIHYtMjQgbS0xMDQgMjQgcTAgMTAgMTAgMTAgbTg0IDAgcTEwIDAgMTAgLTEwIG0tOTQgMTAgaDEwIG01MiAwIGgxMCBtMCAwIGgxMiBtMjAgLTc2IGgxMCBtNTQgMCBoMTAgbTIwIDAgaDEwIG01MiAwIGgxMCBtMCAwIGgxMjQgbS0yMTYgMCBoMjAgbTE5NiAwIGgyMCBtLTIzNiAwIHExMCAwIDEwIDEwIG0yMTYgMCBxMCAtMTAgMTAgLTEwIG0tMjI2IDEwIHYyNCBtMjE2IDAgdi0yNCBtLTIxNiAyNCBxMCAxMCAxMCAxMCBtMTk2IDAgcTEwIDAgMTAgLTEwIG0tMjA2IDEwIGgxMCBtMjYgMCBoMTAgbTAgMCBoMTAgbTg0IDAgaDEwIG0wIDAgaDEwIG0yNiAwIGgxMCBtNDAgLTQ0IGgxMCBtNDAgMCBoMTAgbTQwIDAgaDEwIG02NCAwIGgxMCBtMCAwIGgxMCBtNzQgMCBoMTAgbTAgMCBoMTAgbTExOCAwIGgxMCBtLTMzNiAwIGwyMCAwIG0tMSAwIHEtOSAwIC05IC0xMCBsMCAtMjQgcTAgLTEwIDEwIC0xMCBtMzE2IDQ0IGwyMCAwIG0tMjAgMCBxMTAgMCAxMCAtMTAgbDAgLTI0IHEwIC0xMCAtMTAgLTEwIG0tMzE2IDAgaDEwIG00OCAwIGgxMCBtMCAwIGgyNDggbS0zNTYgNDQgaDIwIG0zNTYgMCBoMjAgbS0zOTYgMCBxMTAgMCAxMCAxMCBtMzc2IDAgcTAgLTEwIDEwIC0xMCBtLTM4NiAxMCB2NjggbTM3NiAwIHYtNjggbS0zNzYgNjggcTAgMTAgMTAgMTAgbTM1NiAwIHExMCAwIDEwIC0xMCBtLTM2NiAxMCBoMTAgbTI2IDAgaDEwIG0yMCAwIGgxMCBtNjQgMCBoMTAgbS0xMDQgMCBsMjAgMCBtLTEgMCBxLTkgMCAtOSAtMTAgbDAgLTI0IHEwIC0xMCAxMCAtMTAgbTg0IDQ0IGwyMCAwIG0tMjAgMCBxMTAgMCAxMCAtMTAgbDAgLTI0IHEwIC0xMCAtMTAgLTEwIG0tODQgMCBoMTAgbTI0IDAgaDEwIG0wIDAgaDQwIG0yMCA0NCBoMTAgbTI2IDAgaDEwIG0wIDAgaDE0MCBtLTQ1NiAtODggaDIwIG00NTYgMCBoMjAgbS00OTYgMCBxMTAgMCAxMCAxMCBtNDc2IDAgcTAgLTEwIDEwIC0xMCBtLTQ4NiAxMCB2MTAyIG00NzYgMCB2LTEwMiBtLTQ3NiAxMDIgcTAgMTAgMTAgMTAgbTQ1NiAwIHExMCAwIDEwIC0xMCBtLTQ2NiAxMCBoMTAgbTAgMCBoNDQ2IG0yMyAtMTIyIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9Ijk1OSA2MSA5NjcgNTcgOTY3IDY1Ij48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iOTU5IDYxIDk1MSA1NyA5NTEgNjUiPjwvcG9seWdvbj4KPC9zdmc+)

  + `ASOF`, `LT`, and `SPLICE` `JOIN` has optional `ON` clause allowing only the
    `=` predicate.
  + `ASOF` and `LT` join additionally allows an optional `TOLERANCE` clause:

  ![Flow chart showing the syntax of the ASOF, LT, and SPLICE JOIN keyword](/docs/assets/images/AsofLtSpliceJoin-32152487b836394cc6715722ef5693c4.svg)

  + `CROSS JOIN` does not allow any `ON` clause:

  ![Flow chart showing the syntax of the CROSS JOIN keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MzUiIGhlaWdodD0iODEiPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iNjYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjY2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSIyMSI+Q1JPU1M8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjExNyIgeT0iMyIgd2lkdGg9IjU0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTE1IiB5PSIxIiB3aWR0aD0iNTQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTI1IiB5PSIyMSI+Sk9JTjwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3RhYmxlIiB4bGluazp0aXRsZT0idGFibGUiPgogICAgICAgICAgICA8cmVjdCB4PSIyMTEiIHk9IjMiIHdpZHRoPSI1MiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIyMDkiIHk9IjEiIHdpZHRoPSI1MiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMjE5IiB5PSIyMSI+dGFibGU8L3RleHQ+PC9hPjxyZWN0IHg9IjIxMSIgeT0iNDciIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjIwOSIgeT0iNDUiIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyMTkiIHk9IjY1Ij4oPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc3ViLXF1ZXJ5IiB4bGluazp0aXRsZT0ic3ViLXF1ZXJ5Ij4KICAgICAgICAgICAgPHJlY3QgeD0iMjU3IiB5PSI0NyIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjI1NSIgeT0iNDUiIHdpZHRoPSI4NCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMjY1IiB5PSI2NSI+c3ViLXF1ZXJ5PC90ZXh0PjwvYT48cmVjdCB4PSIzNjEiIHk9IjQ3IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNTkiIHk9IjQ1IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzY5IiB5PSI2NSI+KTwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNjYgMCBoMTAgbTAgMCBoMTAgbTU0IDAgaDEwIG0yMCAwIGgxMCBtNTIgMCBoMTAgbTAgMCBoMTI0IG0tMjE2IDAgaDIwIG0xOTYgMCBoMjAgbS0yMzYgMCBxMTAgMCAxMCAxMCBtMjE2IDAgcTAgLTEwIDEwIC0xMCBtLTIyNiAxMCB2MjQgbTIxNiAwIHYtMjQgbS0yMTYgMjQgcTAgMTAgMTAgMTAgbTE5NiAwIHExMCAwIDEwIC0xMCBtLTIwNiAxMCBoMTAgbTI2IDAgaDEwIG0wIDAgaDEwIG04NCAwIGgxMCBtMCAwIGgxMCBtMjYgMCBoMTAgbTIzIC00NCBoLTMiPjwvcGF0aD4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI0MjUgMTcgNDMzIDEzIDQzMyAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjQyNSAxNyA0MTcgMTMgNDE3IDIxIj48L3BvbHlnb24+Cjwvc3ZnPg==)

Columns from joined tables are combined in a single row. Columns with the same
name originating from different tables will be automatically aliased to create a
unique column namespace of the resulting set.

Though it is usually preferable to explicitly specify join conditions, QuestDB
will analyze `WHERE` clauses for implicit join conditions and will derive
transient join conditions where necessary.

## Execution order[​](#execution-order "Direct link to Execution order")

Join operations are performed in order of their appearance in a SQL query. The
following query performs a join on a table with a very small table (just one row
in this example) and a bigger table with 10 million rows:

```prism-code
WITH  
  Manytrades AS  
    (SELECT * FROM trades limit 10000000),  
  Lookup AS  
    (SELECT  'BTC-USD' AS Symbol, 'Bitcoin/USD Pair' AS Description)  
SELECT *  
FROM Lookup  
INNER JOIN ManyTrades  
  ON Lookup.symbol = Manytrades.symbol;
```

The performance of this query can be improved by rewriting the query as follows:

```prism-code
WITH  
  Manytrades AS  
    (SELECT * FROM trades limit 10000000),  
  Lookup AS  
    (SELECT  'BTC-USD' AS Symbol, 'Bitcoin/USD Pair' AS Description)  
SELECT *  
FROM ManyTrades  
INNER JOIN Lookup  
  ON Lookup.symbol = Manytrades.symbol;
```

As a general rule, whenever you have a table significantly larger than the
other, try to use the large one first. If you use `EXPLAIN` with the queries
above, you should see the first version needs to Hash over 10 million rows,
while the second version needs to Hash only over 1 row.

## Implicit joins[​](#implicit-joins "Direct link to Implicit joins")

It is possible to join two tables using the following syntax:

```prism-code
SELECT *  
FROM a, b  
WHERE a.id = b.id;
```

The type of join as well as the column are inferred from the `WHERE` clause, and
may be either an `INNER` or `CROSS` join. For the example above, the equivalent
explicit statement would be:

```prism-code
SELECT *  
FROM a  
JOIN b ON (id);
```

## Using the `ON` clause for the `JOIN` predicate[​](#using-the-on-clause-for-the-join-predicate "Direct link to using-the-on-clause-for-the-join-predicate")

When tables are joined on a column that has the same name in both tables you can
use the `ON (column)` shorthand.

When the `ON` clause is permitted (all except `CROSS JOIN`), it is possible to
join multiple columns.

For example, the following two tables contain identical column names `symbol`
and `side`:

`mayTrades`:

| symbol | side | total |
| --- | --- | --- |
| ADA-BTC | buy | 8079 |
| ADA-BTC | sell | 7678 |
| ADA-USD | buy | 308271 |
| ADA-USD | sell | 279624 |

`juneTrades`:

| symbol | side | total |
| --- | --- | --- |
| ADA-BTC | buy | 10253 |
| ADA-BTC | sell | 17460 |
| ADA-USD | buy | 312359 |
| ADA-USD | sell | 245066 |

It is possible to add multiple JOIN ON condition:

```prism-code
WITH  
  mayTrades AS (  
    SELECT symbol, side, COUNT(*) as total  
    FROM trades  
    WHERE timestamp in '2024-05'  
    ORDER BY Symbol  
    LIMIT 4  
  ),  
  juneTrades AS (  
    SELECT symbol, side, COUNT(*) as total  
    FROM trades  
    WHERE timestamp in '2024-06'  
    ORDER BY Symbol  
    LIMIT 4  
  )  
SELECT *  
FROM mayTrades  
JOIN JuneTrades  
  ON mayTrades.symbol = juneTrades.symbol  
    AND mayTrades.side = juneTrades.side;
```

The query can be simplified further since the column names are identical:

```prism-code
WITH  
  mayTrades AS (  
    SELECT symbol, side, COUNT(*) as total  
    FROM trades  
    WHERE timestamp in '2024-05'  
    ORDER BY Symbol  
    LIMIT 4  
  ),  
  juneTrades AS (  
    SELECT symbol, side, COUNT(*) as total  
    FROM trades  
    WHERE timestamp in '2024-06'  
    ORDER BY Symbol  
    LIMIT 4  
  )  
SELECT *  
FROM mayTrades  
JOIN JuneTrades ON (symbol, side);
```

The result of both queries is the following:

| symbol | symbol1 | side | side1 | total | total1 |
| --- | --- | --- | --- | --- | --- |
| ADA-BTC | ADA-BTC | buy | buy | 8079 | 10253 |
| ADA-BTC | ADA-BTC | sell | sell | 7678 | 17460 |
| ADA-USD | ADA-USD | buy | buy | 308271 | 312359 |
| ADA-USD | ADA-USD | sell | sell | 279624 | 245066 |

## ASOF JOIN[​](#asof-join "Direct link to ASOF JOIN")

ASOF JOIN is a powerful time-series join extension.

It has its own page, [ASOF JOIN](/docs/query/sql/asof-join/).

## WINDOW JOIN[​](#window-join "Direct link to WINDOW JOIN")

WINDOW JOIN aggregates data from a related table within a time-based window
around each row. It is useful for calculating rolling statistics, moving
averages, or aggregating readings within time windows.

It has its own page, [WINDOW JOIN](/docs/query/sql/window-join/).

## (INNER) JOIN[​](#inner-join "Direct link to (INNER) JOIN")

`(INNER) JOIN` returns rows from two tables where the records on the compared
column have matching values in both tables. `JOIN` is interpreted as
`INNER JOIN` by default, making the `INNER` keyword implicit.

The query we just saw above is an example. It returns the `symbol`, `side` and
`total` from the `mayTrades` subquery, and adds the `symbol`, `side`, and
`total` from the `juneTrades` subquery. Both tables are matched based on the
`symbol` and `side`, as specified on the `ON` condition.

## LEFT (OUTER) JOIN[​](#left-outer-join "Direct link to LEFT (OUTER) JOIN")

`LEFT OUTER JOIN` or simply `LEFT JOIN` returns **all** records from the left
table, and if matched, the records of the right table. When there is no match
for the right table, it returns `NULL` values in right table fields.

The general syntax is as follows:

LEFT JOIN ON

```prism-code
WITH  
  Manytrades AS  
    (SELECT * FROM trades limit 100),  
  Lookup AS  
    (SELECT  'BTC-USD' AS Symbol, 'Bitcoin/USD Pair' AS Description)  
SELECT *  
FROM ManyTrades  
LEFT OUTER JOIN Lookup  
  ON Lookup.symbol = Manytrades.symbol;
```

In this example, the result will have 100 rows, one for each row on the
`ManyTrades` subquery. When there is no match with the `Lookup` subquery, the
columns `Symbol1` and `Description` will be `null`.

```prism-code
-- Omitting 'OUTER' makes no difference:  
WITH  
  Manytrades AS  
    (SELECT * FROM trades limit 100),  
  Lookup AS  
    (SELECT  'BTC-USD' AS Symbol, 'Bitcoin/USD Pair' AS Description)  
SELECT *  
FROM ManyTrades  
LEFT JOIN Lookup  
  ON Lookup.symbol = Manytrades.symbol;
```

A `LEFT OUTER JOIN` query can also be used to select all rows in the left table
that do not exist in the right table.

```prism-code
WITH  
  Manytrades AS  
    (SELECT * FROM trades limit 100),  
  Lookup AS  
    (SELECT  'BTC-USD' AS Symbol, 'Bitcoin/USD Pair' AS Description)  
SELECT *  
FROM ManyTrades  
LEFT OUTER JOIN Lookup  
  ON Lookup.symbol = Manytrades.symbol  
WHERE Lookup.Symbol = NULL;
```

In this case, the result has 71 rows out of the 100 in the larger table, and the
columns corresponding to the `Lookup` table are all `NULL`.

## CROSS JOIN[​](#cross-join "Direct link to CROSS JOIN")

`CROSS JOIN` returns the Cartesian product of the two tables being joined and
can be used to create a table with all possible combinations of columns.

The following query is joining a table (a subquery in this case) with itself, to
compare row by row if we have any rows with exactly the same values for all the
columns except the timestamp, and if the timestamps are within 10 seconds from
each other:

```prism-code
-- detect potential duplicates, with same values  
-- and within a 10 seconds range  
  
WITH t AS (  
  SELECT * FROM trades WHERE timestamp IN '2024-06-01'  
)  
SELECT * from t CROSS JOIN t AS t2  
WHERE t.timestamp < t2.timestamp  
  AND datediff('s', t.timestamp , t2.timestamp ) < 10  
  AND t.symbol = t2.symbol  
  AND t.side = t2.side  
  AND t.price = t2.price  
  AND t.amount = t2.amount;
```

note

`CROSS JOIN` does not have an `ON` clause.

## LT JOIN[​](#lt-join "Direct link to LT JOIN")

Similar to [`ASOF JOIN`](/docs/query/sql/asof-join/), `LT JOIN` joins two different time-series measured. For
each row in the first time-series, the `LT JOIN` takes from the second
time-series a timestamp that meets both of the following criteria:

* The timestamp is the closest to the first timestamp.
* The timestamp is **strictly prior to** the first timestamp.

In other words: `LT JOIN` won't join records with equal timestamps.

### Example[​](#example "Direct link to Example")

Consider the following tables:

Table `tradesA`:

| timestamp | price |
| --- | --- |
| 2022-03-08T18:03:57.710419Z | 39269.98 |
| 2022-03-08T18:03:58.357448Z | 39265.31 |
| 2022-03-08T18:03:58.357448Z | 39265.31 |

Table `tradesB`:

| timestamp | price |
| --- | --- |
| 2022-03-08T18:03:57.710419Z | 39269.98 |
| 2022-03-08T18:03:58.357448Z | 39265.31 |
| 2022-03-08T18:03:58.357448Z | 39265.31 |

An `LT JOIN` can be built using the following query:

```prism-code
WITH miniTrades AS (  
  SELECT timestamp, price  
  FROM TRADES  
  WHERE symbol = 'BTC-USD'  
  LIMIT 3  
)  
SELECT tradesA.timestamp, tradesB.timestamp, tradesA.price  
FROM miniTrades tradesA  
LT JOIN miniTrades tradesB;
```

The query above returns the following results:

| timestamp | timestamp1 | price |
| --- | --- | --- |
| 2022-03-08T18:03:57.710419Z | NULL | 39269.98 |
| 2022-03-08T18:03:58.357448Z | 2022-03-08T18:03:57.710419Z | 39265.31 |
| 2022-03-08T18:03:58.357448Z | 2022-03-08T18:03:57.710419Z | 39265.31 |

Notice how the first record in the `tradesA` table is not joined with any record
in the `tradesB` table. This is because there is no record in the `tradesB`
table with a timestamp prior to the timestamp of the first record in the
`tradesA` table.

Similarly, the second record in the `tradesB` table is joined with the first
record in the `tradesA` table because the timestamp of the first record in the
`tradesB` table is prior to the timestamp of the second record in the `tradesA`
table.

note

As seen on this example, `LT` join is often useful to join a table to itself in
order to get preceding values for every row.

The `ON` clause can also be used in combination with `LT JOIN` to join both by
timestamp and column values.

### TOLERANCE clause[​](#tolerance-clause "Direct link to TOLERANCE clause")

The `TOLERANCE` clause enhances LT JOIN by limiting how far back in time the join should look for a match in the right
table. The `TOLERANCE` parameter accepts a time interval value (e.g., 2s, 100ms, 1d).

When specified, a record from the left table t1 at t1.ts will only be joined with a record from the right table t2 at
t2.ts if both conditions are met: `t2.ts < t1.ts` and `t1.ts - t2.ts <= tolerance_value`

This ensures that the matched record from the right table is not only the latest one on or before t1.ts, but also within
the specified time window.

LT JOIN with a TOLERANCE parameter

```prism-code
SELECT ...  
FROM table1  
LT JOIN table2 TOLERANCE 10s  
[WHERE ...]
```

The interval\_literal must be a valid QuestDB interval string, like '5s' (5 seconds), '100ms' (100 milliseconds),
'2m' ( 2 minutes), '3h' (3 hours), or '1d' (1 day).

#### Supported Units for interval\_literal[​](#supported-units-for-interval_literal "Direct link to Supported Units for interval_literal")

The `TOLERANCE` interval literal supports the following time unit qualifiers:

* n: Nanoseconds
* U: Microseconds
* T: Milliseconds
* s: Seconds
* m: Minutes
* h: Hours
* d: Days
* w: Weeks

For example, '100U' is 100 microseconds, '50T' is 50 milliseconds, '2s' is 2 seconds, '30m' is 30 minutes,
'1h' is 1 hour, '7d' is 7 days, and '2w' is 2 weeks. Please note that months (M) and years (Y) are not supported as
units for the `TOLERANCE` clause.

The effective precision of the `TOLERANCE` clause depends on the
[designated timestamp resolution](/docs/concepts/designated-timestamp/#resolution)
of the tables involved. For example, if a table uses microsecond resolution, specifying nanosecond
tolerance (e.g., `500n`) will not provide nanosecond-level matching precision.

See [`ASOF JOIN documentation`](/docs/query/sql/asof-join/#tolerance-clause) for more examples with the `TOLERANCE` clause.

## SPLICE JOIN[​](#splice-join "Direct link to SPLICE JOIN")

`SPLICE JOIN` is a full `ASOF JOIN`. It will return all the records from both
tables. For each record from left table splice join will find prevailing record
from right table and for each record from right table - prevailing record from
left table.

Considering the following tables:

Table `buy` (the left table):

| timestamp | price |
| --- | --- |
| 2024-06-22T00:00:00.039906Z | 0.092014 |
| 2024-06-22T00:00:00.343909Z | 9.805 |

The `sell` table (the right table):

| timestamp | price |
| --- | --- |
| 2024-06-22T00:00:00.222534Z | 64120.28 |
| 2024-06-22T00:00:00.222534Z | 64120.28 |

A `SPLICE JOIN` can be built as follows:

```prism-code
WITH  
buy AS (  -- select the first 5 buys in June 22  
  SELECT timestamp, price FROM trades  
  WHERE timestamp IN '2024-06-22' AND side = 'buy' LIMIT 2  
),  
sell AS ( -- select the first 5 sells in June 22  
  SELECT timestamp, price FROM trades  
  WHERE timestamp IN '2024-06-22' AND side = 'sell' LIMIT 2  
)  
SELECT  
  buy.timestamp, sell.timestamp, buy.price, sell.price  
FROM buy  
SPLICE JOIN sell;
```

This query returns the following results:

| timestamp | timestamp1 | price | price1 |
| --- | --- | --- | --- |
| 2024-06-22T00:00:00.039906Z | NULL | 0.092014 | NULL |
| 2024-06-22T00:00:00.039906Z | 2024-06-22T00:00:00.222534Z | 0.092014 | 64120.28 |
| 2024-06-22T00:00:00.039906Z | 2024-06-22T00:00:00.222534Z | 0.092014 | 64120.28 |
| 2024-06-22T00:00:00.343909Z | 2024-06-22T00:00:00.222534Z | 9.805 | 64120.28 |

Note that the above query does not use the optional `ON` clause. In case you
need additional filtering on the two tables, the `ON` clause can also be used.