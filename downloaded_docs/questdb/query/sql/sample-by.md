On this page

`SAMPLE BY` is used on [time-series data](https://questdb.com/blog/what-is-time-series-data/) to summarize large datasets into
aggregates of homogeneous time chunks as part of a
[SELECT statement](/docs/query/sql/select/).

To use `SAMPLE BY`, a table column needs to be specified as a
[designated timestamp](/docs/concepts/designated-timestamp/).

Users performing `SAMPLE BY` queries on datasets **with missing data** may make
use of the [FILL](#fill-options) keyword to specify a fill behavior.

## Syntax[​](#syntax "Direct link to Syntax")

### SAMPLE BY keywords[​](#sample-by-keywords "Direct link to SAMPLE BY keywords")

![Flow chart showing the syntax of the SAMPLE BY keywords](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MjMiIGhlaWdodD0iMjg5Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDE3IDEgMTMgMSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDE3IDkgMTMgOSAyMSI+PC9wb2x5Z29uPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc29tZVNlbGVjdFN0YXRlbWVudC4uLiIgeGxpbms6dGl0bGU9InNvbWVTZWxlY3RTdGF0ZW1lbnQuLi4iPgogICAgICAgICAgICA8cmVjdCB4PSIzMSIgeT0iMyIgd2lkdGg9IjE3MiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjE3MiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMzkiIHk9IjIxIj5zb21lU2VsZWN0U3RhdGVtZW50Li4uPC90ZXh0PjwvYT48cmVjdCB4PSIyMjMiIHk9IjMiIHdpZHRoPSI3NCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjIyMSIgeT0iMSIgd2lkdGg9Ijc0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjIzMSIgeT0iMjEiPlNBTVBMRTwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMzE3IiB5PSIzIiB3aWR0aD0iMzgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzMTUiIHk9IjEiIHdpZHRoPSIzOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzMjUiIHk9IjIxIj5CWTwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI24iIHhsaW5rOnRpdGxlPSJuIj4KICAgICAgICAgICAgPHJlY3QgeD0iMzc1IiB5PSIzIiB3aWR0aD0iMjgiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMzczIiB5PSIxIiB3aWR0aD0iMjgiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjM4MyIgeT0iMjEiPm48L3RleHQ+PC9hPjxyZWN0IHg9IjQ0MyIgeT0iMzUiIHdpZHRoPSIyOCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQ0MSIgeT0iMzMiIHdpZHRoPSIyOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI0NTEiIHk9IjUzIj5UPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI0NDMiIHk9Ijc5IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI0NDEiIHk9Ijc3IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDUxIiB5PSI5NyI+czwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNDQzIiB5PSIxMjMiIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQ0MSIgeT0iMTIxIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDUxIiB5PSIxNDEiPm08L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjQ0MyIgeT0iMTY3IiB3aWR0aD0iMjgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI0NDEiIHk9IjE2NSIgd2lkdGg9IjI4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjQ1MSIgeT0iMTg1Ij5oPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI0NDMiIHk9IjIxMSIgd2lkdGg9IjI4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNDQxIiB5PSIyMDkiIHdpZHRoPSIyOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI0NTEiIHk9IjIyOSI+ZDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNDQzIiB5PSIyNTUiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQ0MSIgeT0iMjUzIiB3aWR0aD0iMzAiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDUxIiB5PSIyNzMiPk08L3RleHQ+CiAgICAgICAgIDxwYXRoIGNsYXNzPSJsaW5lIiBkPSJtMTcgMTcgaDIgbTAgMCBoMTAgbTE3MiAwIGgxMCBtMCAwIGgxMCBtNzQgMCBoMTAgbTAgMCBoMTAgbTM4IDAgaDEwIG0wIDAgaDEwIG0yOCAwIGgxMCBtMjAgMCBoMTAgbTAgMCBoNDIgbS03MiAwIGgyMCBtNTIgMCBoMjAgbS05MiAwIHExMCAwIDEwIDEwIG03MiAwIHEwIC0xMCAxMCAtMTAgbS04MiAxMCB2MTIgbTcyIDAgdi0xMiBtLTcyIDEyIHEwIDEwIDEwIDEwIG01MiAwIHExMCAwIDEwIC0xMCBtLTYyIDEwIGgxMCBtMjggMCBoMTAgbTAgMCBoNCBtLTYyIC0xMCB2MjAgbTcyIDAgdi0yMCBtLTcyIDIwIHYyNCBtNzIgMCB2LTI0IG0tNzIgMjQgcTAgMTAgMTAgMTAgbTUyIDAgcTEwIDAgMTAgLTEwIG0tNjIgMTAgaDEwIG0yNiAwIGgxMCBtMCAwIGg2IG0tNjIgLTEwIHYyMCBtNzIgMCB2LTIwIG0tNzIgMjAgdjI0IG03MiAwIHYtMjQgbS03MiAyNCBxMCAxMCAxMCAxMCBtNTIgMCBxMTAgMCAxMCAtMTAgbS02MiAxMCBoMTAgbTMyIDAgaDEwIG0tNjIgLTEwIHYyMCBtNzIgMCB2LTIwIG0tNzIgMjAgdjI0IG03MiAwIHYtMjQgbS03MiAyNCBxMCAxMCAxMCAxMCBtNTIgMCBxMTAgMCAxMCAtMTAgbS02MiAxMCBoMTAgbTI4IDAgaDEwIG0wIDAgaDQgbS02MiAtMTAgdjIwIG03MiAwIHYtMjAgbS03MiAyMCB2MjQgbTcyIDAgdi0yNCBtLTcyIDI0IHEwIDEwIDEwIDEwIG01MiAwIHExMCAwIDEwIC0xMCBtLTYyIDEwIGgxMCBtMjggMCBoMTAgbTAgMCBoNCBtLTYyIC0xMCB2MjAgbTcyIDAgdi0yMCBtLTcyIDIwIHYyNCBtNzIgMCB2LTI0IG0tNzIgMjQgcTAgMTAgMTAgMTAgbTUyIDAgcTEwIDAgMTAgLTEwIG0tNjIgMTAgaDEwIG0zMCAwIGgxMCBtMCAwIGgyIG0yMyAtMjUyIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjUxMyAxNyA1MjEgMTMgNTIxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNTEzIDE3IDUwNSAxMyA1MDUgMjEiPjwvcG9seWdvbj4KPC9zdmc+)

### FROM-TO keywords[​](#from-to-keywords "Direct link to FROM-TO keywords")

![Flow chart showing the syntax of the FROM-TO keywords](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3MTMiIGhlaWdodD0iMTEzIj4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDE3IDEgMTMgMSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDE3IDkgMTMgOSAyMSI+PC9wb2x5Z29uPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc29tZVNhbXBsZUJ5U2VsZWN0UXVlcnkuLi4iIHhsaW5rOnRpdGxlPSJzb21lU2FtcGxlQnlTZWxlY3RRdWVyeS4uLiI+CiAgICAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iMjA2IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjI5IiB5PSIxIiB3aWR0aD0iMjA2IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzOSIgeT0iMjEiPnNvbWVTYW1wbGVCeVNlbGVjdFF1ZXJ5Li4uPC90ZXh0PjwvYT48cmVjdCB4PSIyNzciIHk9IjMiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI3NSIgeT0iMSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjI4NSIgeT0iMjEiPkZST008L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNsb3dlckJvdW5kIiB4bGluazp0aXRsZT0ibG93ZXJCb3VuZCI+CiAgICAgICAgICAgIDxyZWN0IHg9IjM1NyIgeT0iMyIgd2lkdGg9Ijk0IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjM1NSIgeT0iMSIgd2lkdGg9Ijk0IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzNjUiIHk9IjIxIj5sb3dlckJvdW5kPC90ZXh0PjwvYT48cmVjdCB4PSI0OTEiIHk9IjM1IiB3aWR0aD0iMzgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI0ODkiIHk9IjMzIiB3aWR0aD0iMzgiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDk5IiB5PSI1MyI+VE88L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN1cHBlckJvdW5kIiB4bGluazp0aXRsZT0idXBwZXJCb3VuZCI+CiAgICAgICAgICAgIDxyZWN0IHg9IjU0OSIgeT0iMzUiIHdpZHRoPSI5NiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI1NDciIHk9IjMzIiB3aWR0aD0iOTYiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjU1NyIgeT0iNTMiPnVwcGVyQm91bmQ8L3RleHQ+PC9hPjxyZWN0IHg9IjI3NyIgeT0iNzkiIHdpZHRoPSIzOCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI3NSIgeT0iNzciIHdpZHRoPSIzOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyODUiIHk9Ijk3Ij5UTzwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3VwcGVyQm91bmQiIHhsaW5rOnRpdGxlPSJ1cHBlckJvdW5kIj4KICAgICAgICAgICAgPHJlY3QgeD0iMzM1IiB5PSI3OSIgd2lkdGg9Ijk2IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjMzMyIgeT0iNzciIHdpZHRoPSI5NiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMzQzIiB5PSI5NyI+dXBwZXJCb3VuZDwvdGV4dD48L2E+PHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtMjA2IDAgaDEwIG0yMCAwIGgxMCBtNjAgMCBoMTAgbTAgMCBoMTAgbTk0IDAgaDEwIG0yMCAwIGgxMCBtMCAwIGgxNjQgbS0xOTQgMCBoMjAgbTE3NCAwIGgyMCBtLTIxNCAwIHExMCAwIDEwIDEwIG0xOTQgMCBxMCAtMTAgMTAgLTEwIG0tMjA0IDEwIHYxMiBtMTk0IDAgdi0xMiBtLTE5NCAxMiBxMCAxMCAxMCAxMCBtMTc0IDAgcTEwIDAgMTAgLTEwIG0tMTg0IDEwIGgxMCBtMzggMCBoMTAgbTAgMCBoMTAgbTk2IDAgaDEwIG0tNDA4IC0zMiBoMjAgbTQwOCAwIGgyMCBtLTQ0OCAwIHExMCAwIDEwIDEwIG00MjggMCBxMCAtMTAgMTAgLTEwIG0tNDM4IDEwIHY1NiBtNDI4IDAgdi01NiBtLTQyOCA1NiBxMCAxMCAxMCAxMCBtNDA4IDAgcTEwIDAgMTAgLTEwIG0tNDE4IDEwIGgxMCBtMzggMCBoMTAgbTAgMCBoMTAgbTk2IDAgaDEwIG0wIDAgaDIzNCBtMjMgLTc2IGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjcwMyAxNyA3MTEgMTMgNzExIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNzAzIDE3IDY5NSAxMyA2OTUgMjEiPjwvcG9seWdvbj4KPC9zdmc+)

### FILL keywords[​](#fill-keywords "Direct link to FILL keywords")

![Flow chart showing the syntax of the FILL keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1NzciIGhlaWdodD0iMjQ1Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDMzIDEgMjkgMSAzNyI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDMzIDkgMjkgOSAzNyI+PC9wb2x5Z29uPjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjc29tZVNhbXBsZUJ5U2VsZWN0UXVlcnkiIHhsaW5rOnRpdGxlPSJzb21lU2FtcGxlQnlTZWxlY3RRdWVyeSI+CiAgICAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIxOSIgd2lkdGg9IjE5MiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMTciIHdpZHRoPSIxOTIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjM5IiB5PSIzNyI+c29tZVNhbXBsZUJ5U2VsZWN0UXVlcnk8L3RleHQ+PC9hPjxyZWN0IHg9IjI0MyIgeT0iMTkiIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI0MSIgeT0iMTciIHdpZHRoPSI1MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyNTEiIHk9IjM3Ij5GSUxMPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzNzMiIHk9IjE5IiB3aWR0aD0iNTgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNzEiIHk9IjE3IiB3aWR0aD0iNTgiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzgxIiB5PSIzNyI+Tk9ORTwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMzczIiB5PSI2MyIgd2lkdGg9IjU2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzcxIiB5PSI2MSIgd2lkdGg9IjU2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM4MSIgeT0iODEiPk5VTEw8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjM3MyIgeT0iMTA3IiB3aWR0aD0iNTYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNzEiIHk9IjEwNSIgd2lkdGg9IjU2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM4MSIgeT0iMTI1Ij5QUkVWPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzNzMiIHk9IjE1MSIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzcxIiB5PSIxNDkiIHdpZHRoPSI3MiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzODEiIHk9IjE2OSI+TElORUFSPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzNzMiIHk9IjE5NSIgd2lkdGg9IjI4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzcxIiB5PSIxOTMiIHdpZHRoPSIyOCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzODEiIHk9IjIxMyI+eDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNDg1IiB5PSIxOSIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNDgzIiB5PSIxNyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjQ5MyIgeT0iMzciPiw8L3RleHQ+CiAgICAgICAgIDxwYXRoIGNsYXNzPSJsaW5lIiBkPSJtMTcgMzMgaDIgbTAgMCBoMTAgbTE5MiAwIGgxMCBtMCAwIGgxMCBtNTAgMCBoMTAgbTYwIDAgaDEwIG01OCAwIGgxMCBtMCAwIGgxNCBtLTExMiAwIGgyMCBtOTIgMCBoMjAgbS0xMzIgMCBxMTAgMCAxMCAxMCBtMTEyIDAgcTAgLTEwIDEwIC0xMCBtLTEyMiAxMCB2MjQgbTExMiAwIHYtMjQgbS0xMTIgMjQgcTAgMTAgMTAgMTAgbTkyIDAgcTEwIDAgMTAgLTEwIG0tMTAyIDEwIGgxMCBtNTYgMCBoMTAgbTAgMCBoMTYgbS0xMDIgLTEwIHYyMCBtMTEyIDAgdi0yMCBtLTExMiAyMCB2MjQgbTExMiAwIHYtMjQgbS0xMTIgMjQgcTAgMTAgMTAgMTAgbTkyIDAgcTEwIDAgMTAgLTEwIG0tMTAyIDEwIGgxMCBtNTYgMCBoMTAgbTAgMCBoMTYgbS0xMDIgLTEwIHYyMCBtMTEyIDAgdi0yMCBtLTExMiAyMCB2MjQgbTExMiAwIHYtMjQgbS0xMTIgMjQgcTAgMTAgMTAgMTAgbTkyIDAgcTEwIDAgMTAgLTEwIG0tMTAyIDEwIGgxMCBtNzIgMCBoMTAgbS0xMDIgLTEwIHYyMCBtMTEyIDAgdi0yMCBtLTExMiAyMCB2MjQgbTExMiAwIHYtMjQgbS0xMTIgMjQgcTAgMTAgMTAgMTAgbTkyIDAgcTEwIDAgMTAgLTEwIG0tMTAyIDEwIGgxMCBtMjggMCBoMTAgbTAgMCBoNDQgbTIwIC0xNzYgaDEwIG0yNCAwIGgxMCBtLTE5NiAwIGwyMCAwIG0tMSAwIHEtOSAwIC05IC0xMCBsMCAtMTIgcTAgLTEwIDEwIC0xMCBtMTc2IDMyIGwyMCAwIG0tMjAgMCBxMTAgMCAxMCAtMTAgbDAgLTEyIHEwIC0xMCAtMTAgLTEwIG0tMTc2IDAgaDEwIG0wIDAgaDE2NiBtLTIxNiAzMiBoMjAgbTIxNiAwIGgyMCBtLTI1NiAwIHExMCAwIDEwIDEwIG0yMzYgMCBxMCAtMTAgMTAgLTEwIG0tMjQ2IDEwIHYxOTAgbTIzNiAwIHYtMTkwIG0tMjM2IDE5MCBxMCAxMCAxMCAxMCBtMjE2IDAgcTEwIDAgMTAgLTEwIG0tMjI2IDEwIGgxMCBtMCAwIGgyMDYgbTIzIC0yMTAgaC0zIj48L3BhdGg+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNTY3IDMzIDU3NSAyOSA1NzUgMzciPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI1NjcgMzMgNTU5IDI5IDU1OSAzNyI+PC9wb2x5Z29uPgo8L3N2Zz4=)

### ALIGN TO keywords[​](#align-to-keywords "Direct link to ALIGN TO keywords")

![Flow chart showing the syntax of the ALIGN TO keywords](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MjMiIGhlaWdodD0iMTU3Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDE3IDEgMTMgMSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDE3IDkgMTMgOSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMSIgeT0iMyIgd2lkdGg9IjY0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjkiIHk9IjEiIHdpZHRoPSI2NCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzOSIgeT0iMjEiPkFMSUdOPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxMTUiIHk9IjMiIHdpZHRoPSIzOCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjExMyIgeT0iMSIgd2lkdGg9IjM4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjEyMyIgeT0iMjEiPlRPPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxOTMiIHk9IjMiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjE5MSIgeT0iMSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjIwMSIgeT0iMjEiPkZJUlNUPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIyNzMiIHk9IjMiIHdpZHRoPSIxMjAiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyNzEiIHk9IjEiIHdpZHRoPSIxMjAiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMjgxIiB5PSIyMSI+T0JTRVJWQVRJT048L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjE5MyIgeT0iNDciIHdpZHRoPSI5MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjE5MSIgeT0iNDUiIHdpZHRoPSI5MiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyMDEiIHk9IjY1Ij5DQUxFTkRBUjwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMzI1IiB5PSI3OSIgd2lkdGg9IjU0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzIzIiB5PSI3NyIgd2lkdGg9IjU0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjMzMyIgeT0iOTciPlRJTUU8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjM5OSIgeT0iNzkiIHdpZHRoPSI1OCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjM5NyIgeT0iNzciIHdpZHRoPSI1OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI0MDciIHk9Ijk3Ij5aT05FPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjdGltZXpvbmUiIHhsaW5rOnRpdGxlPSJ0aW1lem9uZSI+CiAgICAgICAgICAgIDxyZWN0IHg9IjQ3NyIgeT0iNzkiIHdpZHRoPSI3OCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI0NzUiIHk9Ijc3IiB3aWR0aD0iNzgiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjQ4NSIgeT0iOTciPnRpbWV6b25lPC90ZXh0PjwvYT48cmVjdCB4PSIzMjUiIHk9IjEyMyIgd2lkdGg9IjU4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzIzIiB5PSIxMjEiIHdpZHRoPSI1OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzMzMiIHk9IjE0MSI+V0lUSDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNDAzIiB5PSIxMjMiIHdpZHRoPSI3MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQwMSIgeT0iMTIxIiB3aWR0aD0iNzIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDExIiB5PSIxNDEiPk9GRlNFVDwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI29mZnNldCIgeGxpbms6dGl0bGU9Im9mZnNldCI+CiAgICAgICAgICAgIDxyZWN0IHg9IjQ5NSIgeT0iMTIzIiB3aWR0aD0iNTYiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iNDkzIiB5PSIxMjEiIHdpZHRoPSI1NiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNTAzIiB5PSIxNDEiPm9mZnNldDwvdGV4dD48L2E+PHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNjQgMCBoMTAgbTAgMCBoMTAgbTM4IDAgaDEwIG0yMCAwIGgxMCBtNjAgMCBoMTAgbTAgMCBoMTAgbTEyMCAwIGgxMCBtMCAwIGgxODIgbS00MjIgMCBoMjAgbTQwMiAwIGgyMCBtLTQ0MiAwIHExMCAwIDEwIDEwIG00MjIgMCBxMCAtMTAgMTAgLTEwIG0tNDMyIDEwIHYyNCBtNDIyIDAgdi0yNCBtLTQyMiAyNCBxMCAxMCAxMCAxMCBtNDAyIDAgcTEwIDAgMTAgLTEwIG0tNDEyIDEwIGgxMCBtOTIgMCBoMTAgbTIwIDAgaDEwIG0wIDAgaDI0MCBtLTI3MCAwIGgyMCBtMjUwIDAgaDIwIG0tMjkwIDAgcTEwIDAgMTAgMTAgbTI3MCAwIHEwIC0xMCAxMCAtMTAgbS0yODAgMTAgdjEyIG0yNzAgMCB2LTEyIG0tMjcwIDEyIHEwIDEwIDEwIDEwIG0yNTAgMCBxMTAgMCAxMCAtMTAgbS0yNjAgMTAgaDEwIG01NCAwIGgxMCBtMCAwIGgxMCBtNTggMCBoMTAgbTAgMCBoMTAgbTc4IDAgaDEwIG0tMjYwIC0xMCB2MjAgbTI3MCAwIHYtMjAgbS0yNzAgMjAgdjI0IG0yNzAgMCB2LTI0IG0tMjcwIDI0IHEwIDEwIDEwIDEwIG0yNTAgMCBxMTAgMCAxMCAtMTAgbS0yNjAgMTAgaDEwIG01OCAwIGgxMCBtMCAwIGgxMCBtNzIgMCBoMTAgbTAgMCBoMTAgbTU2IDAgaDEwIG0wIDAgaDQgbTQzIC0xMjAgaC0zIj48L3BhdGg+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNjEzIDE3IDYyMSAxMyA2MjEgMjEiPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI2MTMgMTcgNjA1IDEzIDYwNSAyMSI+PC9wb2x5Z29uPgo8L3N2Zz4=)

## Sample units[​](#sample-units "Direct link to Sample units")

The size of sampled groups are specified with the following syntax:

```prism-code
SAMPLE BY n{units}
```

Where the unit for sampled groups may be one of the following:

| unit | description |
| --- | --- |
| `U` | microsecond |
| `T` | millisecond |
| `s` | second |
| `m` | minute |
| `h` | hour |
| `d` | day |
| `w` | week |
| `M` | month |
| `y` | year |

For example, given a table `trades`, the following query returns the number of
trades per hour:

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1h;
```

## FROM-TO[​](#from-to "Direct link to FROM-TO")

note

Versions prior to QuestDB 8.1.0 do not have access to this extension.

Please see the new blog for more information.

When using `SAMPLE BY` with `FILL`, you can fill missing rows within the result set with pre-determined values.

However, this method will only fill rows between existing data in the data set and cannot fill rows outside of this range.

To fill outside the bounds of the existing data, you can specify a fill range using a `FROM-TO` clause. The boundary
timestamps are expected in UTC.

Note that `FROM-TO` clause can be used only on non-keyed SAMPLE BY queries, i.e. queries that have no grouping columns
other than the timestamp.

#### Syntax[​](#syntax-1 "Direct link to Syntax")

Specify the shape of the query using `FROM` and `TO`:

Pre-filling trade data[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%20as%20ts%2C%20count()%0AFROM%20trades%0ASAMPLE%20BY%201d%20FROM%20'2009-01-01'%20TO%20'2009-01-10'%20FILL(NULL)%3B&executeQuery=true)

```prism-code
SELECT timestamp as ts, count()  
FROM trades  
SAMPLE BY 1d FROM '2009-01-01' TO '2009-01-10' FILL(NULL);
```

If no rows exist at the start of the range, QuestDB automatically fills in these rows.

This is distinct from the `WHERE` clause with a simple rule of thumb -
`WHERE` controls what data flows in, `FROM-TO` controls what data flows out.

Use both `FROM` and `TO` in isolation to pre-fill or post-fill data. If `FROM` is not provided, then the lower bound is the start of the dataset, aligned to calendar. The opposite is true omitting `TO`.

#### `WHERE` clause optimisation[​](#where-clause-optimisation "Direct link to where-clause-optimisation")

If the user does not provide a `WHERE` clause, or the `WHERE` clause does not consider the designated timestamp,
QuestDB will add one for you, matching the `FROM-TO` interval.

This means that the query will run optimally, and avoid touching data not relevant to the result.

Therefore, we compile the prior query into something similar to this:

Pre-filling trade data with WHERE optimisation[Demo this query](https://demo.questdb.io/?query=SELECT%20timestamp%20as%20ts%2C%20count()%0AFROM%20trades%0AWHERE%20timestamp%20%3E%3D%20'2009-01-01'%0A%20%20AND%20timestamp%20%3C%20%20'2009-01-10'%0ASAMPLE%20BY%201d%20FROM%20'2009-01-01'%20TO%20'2009-01-10'%20FILL(NULL)%3B&executeQuery=true)

```prism-code
SELECT timestamp as ts, count()  
FROM trades  
WHERE timestamp >= '2009-01-01'  
  AND timestamp <  '2009-01-10'  
SAMPLE BY 1d FROM '2009-01-01' TO '2009-01-10' FILL(NULL);
```

#### Limitations[​](#limitations "Direct link to Limitations")

Here are the current limits to this feature.

* This syntax is not compatible with `FILL(PREV)` or `FILL(LINEAR)`.
* This syntax is for `ALIGN TO CALENDAR` only (default alignment).
* Does not consider any specified `OFFSET`.
* This syntax is for non-keyed `SAMPLE BY` i.e. only designated timestamp and aggregate columns.

## Fill options[​](#fill-options "Direct link to Fill options")

The `FILL` keyword is optional and expects one or more `fillOption` strategies
which will be applied to one or more aggregate columns. The following
restrictions apply:

* Keywords denoting fill strategies may not be combined. Only one option from
  `NONE`, `NULL`, `PREV`, `LINEAR` and constants may be used.
* `LINEAR` strategy is not supported for keyed queries, i.e. queries that
  contain non-aggregated columns other than the timestamp in the SELECT clause.
* The `FILL` keyword must precede alignment described in the
  [sample calculation section](#sample-calculation), i.e.:

```prism-code
SELECT ts, max(price) max  
FROM prices  
SAMPLE BY 1h FILL(LINEAR)  
ALIGN TO ...
```

| fillOption | Description |
| --- | --- |
| `NONE` | No fill applied. If there is no data, the time sample will be skipped in the results. A table could be missing intervals. |
| `NULL` | Fills with `NULL` values. |
| `PREV` | Fills using the previous value. |
| `LINEAR` | Fills by linear interpolation of the 2 surrounding points. |
| `x` | Fills with a constant value - where `x` is the desired value, for example `FILL(100.05)`. |

Consider an example table named `prices` which has no records during the entire
third hour (`2021-01-01T03`):

| ts | price |
| --- | --- |
| 2021-01-01T01:00:00.000000Z | p1 |
| 2021-01-01T02:00:00.000000Z | p2 |
| 2021-01-01T04:00:00.000000Z | p4 |
| 2021-01-01T05:00:00.000000Z | p5 |

The following query returns the maximum price per hour. As there are missing
values, an aggregate cannot be calculated:

```prism-code
SELECT ts, max(price) max  
FROM prices  
SAMPLE BY 1h;
```

A row is missing for the `2021-01-01T03:00:00.000000Z` sample:

| ts | max |
| --- | --- |
| 2021-01-01T01:00:00.000000Z | max1 |
| 2021-01-01T02:00:00.000000Z | max2 |
| 2021-01-01T04:00:00.000000Z | max4 |
| 2021-01-01T05:00:00.000000Z | max5 |

A `FILL` strategy can be employed which fills with the previous value using
`PREV`:

```prism-code
SELECT ts, max(price) max  
FROM prices  
SAMPLE BY 1h FILL(PREV);
```

| ts | max |
| --- | --- |
| 2021-01-01T01:00:00.000000Z | max1 |
| 2021-01-01T02:00:00.000000Z | max2 |
| **2021-01-01T03:00:00.000000Z** | **max2** |
| 2021-01-01T04:00:00.000000Z | max4 |
| 2021-01-01T05:00:00.000000Z | max5 |

Linear interpolation is done using the `LINEAR` fill option:

```prism-code
SELECT ts, max(price) max  
FROM prices  
SAMPLE BY 1h FILL(LINEAR);
```

| ts | max |
| --- | --- |
| 2021-01-01T01:00:00.000000Z | max1 |
| 2021-01-01T02:00:00.000000Z | max2 |
| **2021-01-01T03:00:00.000000Z** | **(max2+max4)/2** |
| 2021-01-01T04:00:00.000000Z | max4 |
| 2021-01-01T05:00:00.000000Z | max5 |

A constant value can be used as a `fillOption`:

```prism-code
SELECT ts, max(price) max  
FROM prices  
SAMPLE BY 1h FILL(100.5);
```

| ts | max |
| --- | --- |
| 2021-01-01T01:00:00.000000Z | max1 |
| 2021-01-01T02:00:00.000000Z | max2 |
| **2021-01-01T03:00:00.000000Z** | **100.5** |
| 2021-01-01T04:00:00.000000Z | max4 |
| 2021-01-01T05:00:00.000000Z | max5 |

Finally, `NULL` may be used as a `fillOption`:

```prism-code
SELECT ts, max(price) max  
FROM prices  
SAMPLE BY 1h FILL(NULL);
```

| ts | max |
| --- | --- |
| 2021-01-01T01:00:00.000000Z | max1 |
| 2021-01-01T02:00:00.000000Z | max2 |
| **2021-01-01T03:00:00.000000Z** | **null** |
| 2021-01-01T04:00:00.000000Z | max4 |
| 2021-01-01T05:00:00.000000Z | max5 |

### Multiple fill values[​](#multiple-fill-values "Direct link to Multiple fill values")

`FILL()` accepts a list of values where each value corresponds to a single
aggregate column in the SELECT clause order:

```prism-code
SELECT min(price), max(price), avg(price), ts  
FROM prices  
SAMPLE BY 1h  
FILL(NULL, 10, PREV);
```

In the above query `min(price)` aggregate will get `FILL(NULL)` strategy
applied, `max(price)` will get `FILL(10)`, and `avg(price)` will get
`FILL(PREV)`.

## Sample calculation[​](#sample-calculation "Direct link to Sample calculation")

The default time calculation of sampled groups is an absolute value, in other
words, sampling by one day is a 24 hour range which is not bound to calendar
dates. To align sampled groups to calendar dates, the `ALIGN TO` keywords can be
used and are described in the [ALIGN TO CALENDAR](#align-to-calendar) section
below.

note

Since QuestDB v7.4.0, the default behaviour for `ALIGN TO` has changed. If you do not specify
an explicit alignment, `SAMPLE BY` expressions will use `ALIGN TO CALENDAR` behaviour.

The prior default behaviour can be retained by specifying `ALIGN TO FIRST OBSERVATION` on a `SAMPLE BY` query.

Alternatively, one can set the `cairo.sql.sampleby.default.alignment.calendar` option to `false` in `server.conf`.

## ALIGN TO FIRST OBSERVATION[​](#align-to-first-observation "Direct link to ALIGN TO FIRST OBSERVATION")

Consider a table `trades` with the following data spanning three calendar days:

```prism-code
CREATE TABLE trades (  
  ts TIMESTAMP,  
  price DOUBLE  
) TIMESTAMP(ts) PARTITION BY DAY WAL;  
  
INSERT INTO trades (ts, price) VALUES  
  ('2021-05-31T23:10:00.000000Z', 100.5),  
  ('2021-06-01T01:10:00.000000Z', 101.2),  
  ('2021-06-01T07:20:00.000000Z', 100.8),  
  ('2021-06-01T13:20:00.000000Z', 101.0),  
  ('2021-06-01T19:20:00.000000Z', 102.1),  
  ('2021-06-02T01:10:00.000000Z', 101.5),  
  ('2021-06-02T07:20:00.000000Z', 100.9);
```

The following query can be used to sample the table by day.

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1d  
ALIGN TO FIRST OBSERVATION;
```

This query will return two rows:

| ts | count |
| --- | --- |
| 2021-05-31T23:10:00.000000Z | 5 |
| 2021-06-01T23:10:00.000000Z | 2 |

The timestamp value for the 24 hour groups start at the first-observed
timestamp, and continue in `1d` intervals.

## ALIGN TO CALENDAR[​](#align-to-calendar "Direct link to ALIGN TO CALENDAR")

The default behaviour for SAMPLE BY, this option aligns data to calendar dates, with two optional parameters:

* [TIME ZONE](#time-zone)
* [WITH OFFSET](#with-offset)

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1d;
```

or:

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1d  
ALIGN TO CALENDAR;
```

Gives the following result:

| ts | count |
| --- | --- |
| 2021-05-31T00:00:00.000000Z | 1 |
| 2021-06-01T00:00:00.000000Z | 4 |
| 2021-06-02T00:00:00.000000Z | 2 |

In this case, the timestamps are floored to the nearest UTC day, and grouped. The counts correspond
to the number of entries occurring within each UTC day.

This is particularly useful for summarising data for charting purposes; see the [candlestick chart](https://dashboard.questdb.io/d-solo/fb13b4ab-b1c9-4a54-a920-b60c5fb0363f/public-dashboard-questdb-io-use-cases-crypto?orgId=1&refresh=750ms&panelId=6) from the example [crypto dashboard](https://questdb.com/dashboards/crypto/).

### TIME ZONE[​](#time-zone "Direct link to TIME ZONE")

A time zone may be provided for sampling with calendar alignment. Details on the
options for specifying time zones with available formats are provided in the
guide for
[working with timestamps and time zones](/docs/concepts/timestamps-timezones/).

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1d  
ALIGN TO CALENDAR TIME ZONE 'Europe/Berlin';
```

In this case, the 24 hour samples begin at `2021-05-31T22:00:00.000000Z`:

| ts | count |
| --- | --- |
| 2021-05-31T22:00:00.000000Z | 5 |
| 2021-06-01T22:00:00.000000Z | 2 |

Additionally, an offset may be applied when aligning sample calculation to
calendar

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1d  
ALIGN TO CALENDAR TIME ZONE 'Europe/Berlin' WITH OFFSET '00:45';
```

In this case, the 24 hour samples begin at `2021-05-31T22:45:00.000000Z`:

| ts | count |
| --- | --- |
| 2021-05-31T22:45:00.000000Z | 5 |
| 2021-06-01T22:45:00.000000Z | 1 |

#### Local timezone output[​](#local-timezone-output "Direct link to Local timezone output")

The timestamp values output from `SAMPLE BY` queries is in UTC. To have UTC
values converted to specific timezones, the
[to\_timezone() function](/docs/query/functions/date-time/#to_timezone) should
be used.

```prism-code
SELECT to_timezone(ts, 'PST') ts, count  
FROM (  
  SELECT ts, count()  
  FROM trades  
  SAMPLE BY 2h  
  ALIGN TO CALENDAR TIME ZONE 'PST'  
);
```

#### Time zone transitions[​](#time-zone-transitions "Direct link to Time zone transitions")

Calendar dates may contain historical time zone transitions or may vary in the
total number of hours due to daylight savings time. Considering the 31st October
2021, in the `Europe/London` calendar day which consists of 25 hours:

> * Sunday, 31 October 2021, 02:00:00 clocks are turned backward 1 hour to
> * Sunday, 31 October 2021, 01:00:00 local standard time

When a `SAMPLE BY` operation crosses time zone transitions in cases such as
this, the first sampled group which spans a transition will include aggregates
by full calendar range. Consider a table `trades` with one trade per hour
spanning five calendar hours:

| ts | price |
| --- | --- |
| 2021-10-31T00:10:00.000000Z | 100.5 |
| 2021-10-31T01:10:00.000000Z | 101.2 |
| 2021-10-31T02:10:00.000000Z | 100.8 |
| 2021-10-31T03:10:00.000000Z | 101.5 |
| 2021-10-31T04:10:00.000000Z | 102.0 |

The following query will sample by hour with the `Europe/London` time zone and
align to calendar ranges:

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1h  
ALIGN TO CALENDAR TIME ZONE 'Europe/London';
```

The record count for the hour which encounters a time zone transition will
contain two records for both hours at the time zone transition:

| ts | count |
| --- | --- |
| 2021-10-31T00:00:00.000000Z | 2 |
| 2021-10-31T01:00:00.000000Z | 1 |
| 2021-10-31T02:00:00.000000Z | 1 |
| 2021-10-31T03:00:00.000000Z | 1 |

Similarly, given one data point per hour on this table, running `SAMPLE BY 1d`
will have a count of `25` for this day when aligned to calendar time zone
`Europe/London`.

### WITH OFFSET[​](#with-offset "Direct link to WITH OFFSET")

Aligning sampling calculation can be provided an arbitrary offset in the format
`'+/-HH:mm'`, for example:

* `'00:30'` plus thirty minutes
* `'+00:30'` plus thirty minutes
* `'-00:15'` minus 15 minutes

The query uses the default offset '00:00' if the parameter is not set.

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1d  
ALIGN TO CALENDAR WITH OFFSET '02:00';
```

In this case, the 24 hour samples begin at `2021-05-31T02:00:00.000000Z`:

| ts | count |
| --- | --- |
| 2021-05-31T02:00:00.000000Z | 2 |
| 2021-06-01T02:00:00.000000Z | 4 |
| 2021-06-02T02:00:00.000000Z | 1 |

### TIME ZONE WITH OFFSET[​](#time-zone-with-offset "Direct link to TIME ZONE WITH OFFSET")

The `TIME ZONE` and `WITH OFFSET` options can be combined.

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1h  
ALIGN TO CALENDAR TIME ZONE 'Europe/London' WITH OFFSET '02:00';
```

The sample then begins from `Europe/London` at `2021-10-31T02:00:00.000000Z`:

| ts | count |
| --- | --- |
| 2021-10-31T02:00:00.000000Z | 1 |
| 2021-10-31T03:00:00.000000Z | 1 |
| 2021-10-31T04:00:00.000000Z | 3 |
| 2021-10-31T05:00:00.000000Z | 2 |

## Examples[​](#examples "Direct link to Examples")

Assume the following table `trades`:

| ts | quantity | price |
| --- | --- | --- |
| 2021-05-31T23:45:10.000000Z | 10 | 100.05 |
| 2021-06-01T00:01:33.000000Z | 5 | 100.05 |
| 2021-06-01T00:15:14.000000Z | 200 | 100.15 |
| 2021-06-01T00:30:40.000000Z | 300 | 100.15 |
| 2021-06-01T00:45:20.000000Z | 10 | 100 |
| 2021-06-01T01:00:50.000000Z | 50 | 100.15 |

This query will return the number of trades per hour:

Hourly interval

```prism-code
SELECT ts, count()  
FROM trades  
SAMPLE BY 1h;
```

| ts | count |
| --- | --- |
| 2021-05-31T23:45:10.000000Z | 3 |
| 2021-06-01T00:45:10.000000Z | 1 |
| 2021-05-31T23:45:10.000000Z | 1 |
| 2021-06-01T00:45:10.000000Z | 1 |

The following will return the trade volume in 30 minute intervals

30 minute interval

```prism-code
SELECT ts, sum(quantity*price)  
FROM trades  
SAMPLE BY 30m;
```

| ts | sum |
| --- | --- |
| 2021-05-31T23:45:10.000000Z | 1000.5 |
| 2021-06-01T00:15:10.000000Z | 16024 |
| 2021-06-01T00:45:10.000000Z | 8000 |
| 2021-06-01T00:15:10.000000Z | 8012 |
| 2021-06-01T00:45:10.000000Z | 8000 |

The following will return the average trade notional (where notional is = q \*
p) by day:

Daily interval

```prism-code
SELECT ts, avg(quantity*price)  
FROM trades  
SAMPLE BY 1d;
```

| ts | avg |
| --- | --- |
| 2021-05-31T23:45:10.000000Z | 6839.416666666667 |

To make this sample align to calendar dates:

Calendar alignment

```prism-code
SELECT ts, avg(quantity*price)  
FROM trades  
SAMPLE BY 1d  
ALIGN TO CALENDAR;
```

| ts | avg |
| --- | --- |
| 2021-05-31T00:00:00.000000Z | 1000.5 |
| 2021-06-01T00:00:00.000000Z | 8007.2 |

## Performance optimization[​](#performance-optimization "Direct link to Performance optimization")

For frequently executed `SAMPLE BY` queries, consider using [materialized views](/docs/concepts/materialized-views/) to pre-compute aggregates. This can significantly improve query performance, especially for complex sampling operations on large datasets.

```prism-code
CREATE MATERIALIZED VIEW hourly_metrics AS  
SELECT   
    timestamp_floor('h', ts) as hour,  
    symbol,  
    avg(price) as avg_price,  
    sum(volume) as total_volume  
FROM trades  
SAMPLE BY 1h;
```

## See also[​](#see-also "Direct link to See also")

This section includes links to additional information such as tutorials:

* [PIVOT](/docs/query/sql/pivot/) - Transform SAMPLE BY results from rows to columns
* [Materialized Views](/docs/concepts/materialized-views/) - Pre-compute SAMPLE BY queries for better performance
* [SQL Extensions for Time-Series Data in QuestDB](https://questdb.com/blog/2022/11/23/sql-extensions-time-series-data-questdb-part-ii/)
* [Three SQL Keywords for Finding Missing Data](https://questdb.com/blog/three-sql-keywords-for-finding-missing-data/)