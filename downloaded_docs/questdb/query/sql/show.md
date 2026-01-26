On this page

This keyword provides table, column, and partition information including
metadata. The `SHOW` keyword is useful for checking the
[designated timestamp setting](/docs/concepts/designated-timestamp/) column, the
[partition attachment settings](/docs/query/sql/alter-table-attach-partition/),
and partition storage size on disk.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the SHOW keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1NzMiIGhlaWdodD0iNjE3Ij4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDE3IDEgMTMgMSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDE3IDkgMTMgOSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMSIgeT0iMyIgd2lkdGg9IjY0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjkiIHk9IjEiIHdpZHRoPSI2NCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzOSIgeT0iMjEiPlNIT1c8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjEzNSIgeT0iMyIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTMzIiB5PSIxIiB3aWR0aD0iNzIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTQzIiB5PSIyMSI+VEFCTEVTPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxNzUiIHk9IjQ3IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxNzMiIHk9IjQ1IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTgzIiB5PSI2NSI+Q09MVU1OUzwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTc1IiB5PSI5MSIgd2lkdGg9IjEwNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjE3MyIgeT0iODkiIHdpZHRoPSIxMDYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTgzIiB5PSIxMDkiPlBBUlRJVElPTlM8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjMyMSIgeT0iNDciIHdpZHRoPSI2MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjMxOSIgeT0iNDUiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzMjkiIHk9IjY1Ij5GUk9NPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxNTUiIHk9IjEzNSIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTUzIiB5PSIxMzMiIHdpZHRoPSI3MiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxNjMiIHk9IjE1MyI+Q1JFQVRFPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIyNDciIHk9IjEzNSIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjQ1IiB5PSIxMzMiIHdpZHRoPSI2MiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyNTUiIHk9IjE1MyI+VEFCTEU8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN0YWJsZU5hbWUiIHhsaW5rOnRpdGxlPSJ0YWJsZU5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSI0MjEiIHk9IjQ3IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iNDE5IiB5PSI0NSIgd2lkdGg9Ijg4IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSI0MjkiIHk9IjY1Ij50YWJsZU5hbWU8L3RleHQ+PC9hPjxyZWN0IHg9IjE1NSIgeT0iMTc5IiB3aWR0aD0iNTYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxNTMiIHk9IjE3NyIgd2lkdGg9IjU2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE2MyIgeT0iMTk3Ij5VU0VSPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxNTUiIHk9IjIyMyIgd2lkdGg9Ijc4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTUzIiB5PSIyMjEiIHdpZHRoPSI3OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxNjMiIHk9IjI0MSI+R1JPVVBTPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjdXNlck5hbWUiIHhsaW5rOnRpdGxlPSJ1c2VyTmFtZSI+CiAgICAgICAgICAgIDxyZWN0IHg9IjI5MyIgeT0iMjExIiB3aWR0aD0iODQiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMjkxIiB5PSIyMDkiIHdpZHRoPSI4NCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMzAxIiB5PSIyMjkiPnVzZXJOYW1lPC90ZXh0PjwvYT48cmVjdCB4PSIxMzUiIHk9IjI2NyIgd2lkdGg9IjY0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTMzIiB5PSIyNjUiIHdpZHRoPSI2NCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxNDMiIHk9IjI4NSI+VVNFUlM8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjEzNSIgeT0iMzExIiB3aWR0aD0iNzgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxMzMiIHk9IjMwOSIgd2lkdGg9Ijc4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE0MyIgeT0iMzI5Ij5TRVJWSUNFPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIyNTMiIHk9IjMxMSIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjUxIiB5PSIzMDkiIHdpZHRoPSI4NiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyNjEiIHk9IjMyOSI+QUNDT1VOVDwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI2FjY291bnROYW1lIiB4bGluazp0aXRsZT0iYWNjb3VudE5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSIzNzkiIHk9IjM0MyIgd2lkdGg9IjEwNiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIzNzciIHk9IjM0MSIgd2lkdGg9IjEwNiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMzg3IiB5PSIzNjEiPmFjY291bnROYW1lPC90ZXh0PjwvYT48cmVjdCB4PSIyNTMiIHk9IjM4NyIgd2lkdGg9Ijk0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjUxIiB5PSIzODUiIHdpZHRoPSI5NCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIyNjEiIHk9IjQwNSI+QUNDT1VOVFM8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN1c2VyTmFtZSIgeGxpbms6dGl0bGU9InVzZXJOYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iMzg3IiB5PSI0MTkiIHdpZHRoPSI4NCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIzODUiIHk9IjQxNyIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzOTUiIHk9IjQzNyI+dXNlck5hbWU8L3RleHQ+PC9hPjxyZWN0IHg9IjEzNSIgeT0iNDYzIiB3aWR0aD0iMTE4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTMzIiB5PSI0NjEiIHdpZHRoPSIxMTgiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTQzIiB5PSI0ODEiPlBFUk1JU1NJT05TPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjZW50aXR5TmFtZSIgeGxpbms6dGl0bGU9ImVudGl0eU5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSIyOTMiIHk9IjQ5NSIgd2lkdGg9IjkyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjI5MSIgeT0iNDkzIiB3aWR0aD0iOTIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjMwMSIgeT0iNTEzIj5lbnRpdHlOYW1lPC90ZXh0PjwvYT48cmVjdCB4PSIxMzUiIHk9IjUzOSIgd2lkdGg9IjE0NiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjEzMyIgeT0iNTM3IiB3aWR0aD0iMTQ2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE0MyIgeT0iNTU3Ij5TRVJWRVJfVkVSU0lPTjwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTM1IiB5PSI1ODMiIHdpZHRoPSIxMTAiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIxMzMiIHk9IjU4MSIgd2lkdGg9IjExMCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxNDMiIHk9IjYwMSI+UEFSQU1FVEVSUzwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtNjQgMCBoMTAgbTIwIDAgaDEwIG03MiAwIGgxMCBtMCAwIGgzMTggbS00MzAgMCBoMjAgbTQxMCAwIGgyMCBtLTQ1MCAwIHExMCAwIDEwIDEwIG00MzAgMCBxMCAtMTAgMTAgLTEwIG0tNDQwIDEwIHYyNCBtNDMwIDAgdi0yNCBtLTQzMCAyNCBxMCAxMCAxMCAxMCBtNDEwIDAgcTEwIDAgMTAgLTEwIG0tMzgwIDEwIGgxMCBtODggMCBoMTAgbTAgMCBoMTggbS0xNDYgMCBoMjAgbTEyNiAwIGgyMCBtLTE2NiAwIHExMCAwIDEwIDEwIG0xNDYgMCBxMCAtMTAgMTAgLTEwIG0tMTU2IDEwIHYyNCBtMTQ2IDAgdi0yNCBtLTE0NiAyNCBxMCAxMCAxMCAxMCBtMTI2IDAgcTEwIDAgMTAgLTEwIG0tMTM2IDEwIGgxMCBtMTA2IDAgaDEwIG0yMCAtNDQgaDEwIG02MCAwIGgxMCBtLTI2NiAwIGgyMCBtMjQ2IDAgaDIwIG0tMjg2IDAgcTEwIDAgMTAgMTAgbTI2NiAwIHEwIC0xMCAxMCAtMTAgbS0yNzYgMTAgdjY4IG0yNjYgMCB2LTY4IG0tMjY2IDY4IHEwIDEwIDEwIDEwIG0yNDYgMCBxMTAgMCAxMCAtMTAgbS0yNTYgMTAgaDEwIG03MiAwIGgxMCBtMCAwIGgxMCBtNjIgMCBoMTAgbTAgMCBoNzIgbTIwIC04OCBoMTAgbTg4IDAgaDEwIG0wIDAgaDE2IG0tNDIwIC0xMCB2MjAgbTQzMCAwIHYtMjAgbS00MzAgMjAgdjExMiBtNDMwIDAgdi0xMTIgbS00MzAgMTEyIHEwIDEwIDEwIDEwIG00MTAgMCBxMTAgMCAxMCAtMTAgbS00MDAgMTAgaDEwIG01NiAwIGgxMCBtMCAwIGgyMiBtLTExOCAwIGgyMCBtOTggMCBoMjAgbS0xMzggMCBxMTAgMCAxMCAxMCBtMTE4IDAgcTAgLTEwIDEwIC0xMCBtLTEyOCAxMCB2MjQgbTExOCAwIHYtMjQgbS0xMTggMjQgcTAgMTAgMTAgMTAgbTk4IDAgcTEwIDAgMTAgLTEwIG0tMTA4IDEwIGgxMCBtNzggMCBoMTAgbTQwIC00NCBoMTAgbTAgMCBoOTQgbS0xMjQgMCBoMjAgbTEwNCAwIGgyMCBtLTE0NCAwIHExMCAwIDEwIDEwIG0xMjQgMCBxMCAtMTAgMTAgLTEwIG0tMTM0IDEwIHYxMiBtMTI0IDAgdi0xMiBtLTEyNCAxMiBxMCAxMCAxMCAxMCBtMTA0IDAgcTEwIDAgMTAgLTEwIG0tMTE0IDEwIGgxMCBtODQgMCBoMTAgbTIwIC0zMiBoMTI4IG0tNDIwIC0xMCB2MjAgbTQzMCAwIHYtMjAgbS00MzAgMjAgdjY4IG00MzAgMCB2LTY4IG0tNDMwIDY4IHEwIDEwIDEwIDEwIG00MTAgMCBxMTAgMCAxMCAtMTAgbS00MjAgMTAgaDEwIG02NCAwIGgxMCBtMCAwIGgzMjYgbS00MjAgLTEwIHYyMCBtNDMwIDAgdi0yMCBtLTQzMCAyMCB2MjQgbTQzMCAwIHYtMjQgbS00MzAgMjQgcTAgMTAgMTAgMTAgbTQxMCAwIHExMCAwIDEwIC0xMCBtLTQyMCAxMCBoMTAgbTc4IDAgaDEwIG0yMCAwIGgxMCBtODYgMCBoMTAgbTIwIDAgaDEwIG0wIDAgaDExNiBtLTE0NiAwIGgyMCBtMTI2IDAgaDIwIG0tMTY2IDAgcTEwIDAgMTAgMTAgbTE0NiAwIHEwIC0xMCAxMCAtMTAgbS0xNTYgMTAgdjEyIG0xNDYgMCB2LTEyIG0tMTQ2IDEyIHEwIDEwIDEwIDEwIG0xMjYgMCBxMTAgMCAxMCAtMTAgbS0xMzYgMTAgaDEwIG0xMDYgMCBoMTAgbS0yNzIgLTMyIGgyMCBtMjcyIDAgaDIwIG0tMzEyIDAgcTEwIDAgMTAgMTAgbTI5MiAwIHEwIC0xMCAxMCAtMTAgbS0zMDIgMTAgdjU2IG0yOTIgMCB2LTU2IG0tMjkyIDU2IHEwIDEwIDEwIDEwIG0yNzIgMCBxMTAgMCAxMCAtMTAgbS0yODIgMTAgaDEwIG05NCAwIGgxMCBtMjAgMCBoMTAgbTAgMCBoOTQgbS0xMjQgMCBoMjAgbTEwNCAwIGgyMCBtLTE0NCAwIHExMCAwIDEwIDEwIG0xMjQgMCBxMCAtMTAgMTAgLTEwIG0tMTM0IDEwIHYxMiBtMTI0IDAgdi0xMiBtLTEyNCAxMiBxMCAxMCAxMCAxMCBtMTA0IDAgcTEwIDAgMTAgLTEwIG0tMTE0IDEwIGgxMCBtODQgMCBoMTAgbTIwIC0zMiBoMTQgbS00MDAgLTg2IHYyMCBtNDMwIDAgdi0yMCBtLTQzMCAyMCB2MTMyIG00MzAgMCB2LTEzMiBtLTQzMCAxMzIgcTAgMTAgMTAgMTAgbTQxMCAwIHExMCAwIDEwIC0xMCBtLTQyMCAxMCBoMTAgbTExOCAwIGgxMCBtMjAgMCBoMTAgbTAgMCBoMTAyIG0tMTMyIDAgaDIwIG0xMTIgMCBoMjAgbS0xNTIgMCBxMTAgMCAxMCAxMCBtMTMyIDAgcTAgLTEwIDEwIC0xMCBtLTE0MiAxMCB2MTIgbTEzMiAwIHYtMTIgbS0xMzIgMTIgcTAgMTAgMTAgMTAgbTExMiAwIHExMCAwIDEwIC0xMCBtLTEyMiAxMCBoMTAgbTkyIDAgaDEwIG0yMCAtMzIgaDEyMCBtLTQyMCAtMTAgdjIwIG00MzAgMCB2LTIwIG0tNDMwIDIwIHY1NiBtNDMwIDAgdi01NiBtLTQzMCA1NiBxMCAxMCAxMCAxMCBtNDEwIDAgcTEwIDAgMTAgLTEwIG0tNDIwIDEwIGgxMCBtMTQ2IDAgaDEwIG0wIDAgaDI0NCBtLTQyMCAtMTAgdjIwIG00MzAgMCB2LTIwIG0tNDMwIDIwIHYyNCBtNDMwIDAgdi0yNCBtLTQzMCAyNCBxMCAxMCAxMCAxMCBtNDEwIDAgcTEwIDAgMTAgLTEwIG0tNDIwIDEwIGgxMCBtMTEwIDAgaDEwIG0wIDAgaDI4MCBtMjMgLTU4MCBoLTMiPjwvcGF0aD4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI1NjMgMTcgNTcxIDEzIDU3MSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjU2MyAxNyA1NTUgMTMgNTU1IDIxIj48L3BvbHlnb24+Cjwvc3ZnPg==)

## Description[​](#description "Direct link to Description")

* `SHOW TABLES` returns all the tables.
* `SHOW COLUMNS` returns all the columns and their metadata for the selected
  table.
* `SHOW PARTITIONS` returns the partition information for the selected table.
* `SHOW CREATE TABLE` returns a DDL query that allows you to recreate the table.
* `SHOW CREATE VIEW` returns a DDL query that allows you to recreate a view.
* `SHOW USER` shows user secret (enterprise-only)
* `SHOW GROUPS` shows all groups the user belongs or all groups in the system
  (enterprise-only)
* `SHOW USERS` shows all users (enterprise-only)
* `SHOW SERVICE ACCOUNT` displays details of a service account (enterprise-only)
* `SHOW SERVICE ACCOUNTS` displays all service accounts or those assigned to the
  user/group (enterprise-only)
* `SHOW PERMISSIONS` displays permissions of user, group or service account
  (enterprise-only)
* `SHOW SERVER_VERSION` displays PostgreSQL compatibility version
* `SHOW PARAMETERS` shows configuration keys and their matching `env_var_name`,
  their values and the source of the value

## Examples[​](#examples "Direct link to Examples")

### SHOW TABLES[​](#show-tables "Direct link to SHOW TABLES")

show tables[Demo this query](https://demo.questdb.io/?query=SHOW%20TABLES%3B&executeQuery=true)

```prism-code
SHOW TABLES;
```

| table\_name |
| --- |
| ethblocks\_json |
| trades |
| weather |
| AAPL\_orderbook |
| trips |

### SHOW COLUMNS[​](#show-columns "Direct link to SHOW COLUMNS")

show columns[Demo this query](https://demo.questdb.io/?query=SHOW%20COLUMNS%20FROM%20trades%3B%0A&executeQuery=true)

```prism-code
SHOW COLUMNS FROM trades;
```

| column | type | indexed | indexBlockCapacity | symbolCached | symbolCapacity | symbolTableSize | designated | upsertKey |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| symbol | SYMBOL | false | 0 | true | 256 | 42 | false | false |
| side | SYMBOL | false | 0 | true | 256 | 2 | false | false |
| price | DOUBLE | false | 0 | false | 0 | 0 | false | false |
| amount | DOUBLE | false | 0 | false | 0 | 0 | false | false |
| timestamp | TIMESTAMP | false | 0 | false | 0 | 0 | true | false |

### SHOW CREATE TABLE[​](#show-create-table "Direct link to SHOW CREATE TABLE")

retrieving table ddl[Demo this query](https://demo.questdb.io/?query=SHOW%20CREATE%20TABLE%20trades%3B&executeQuery=true)

```prism-code
SHOW CREATE TABLE trades;
```

| ddl |
| --- |
| CREATE TABLE trades (symbol SYMBOL CAPACITY 256 CACHE, side SYMBOL CAPACITY 256 CACHE, price DOUBLE, amount DOUBLE, timestamp TIMESTAMP) timestamp(timestamp) PARTITION BY DAY WAL WITH maxUncommittedRows=500000, o3MaxLag=600000000us; |

This is printed with formatting, so when pasted into a text editor that support formatting characters, you will see:

```prism-code
CREATE TABLE trades (  
	symbol SYMBOL CAPACITY 256 CACHE,  
	side SYMBOL CAPACITY 256 CACHE,  
	price DOUBLE,  
	amount DOUBLE,  
	timestamp TIMESTAMP  
) timestamp(timestamp) PARTITION BY DAY WAL  
WITH maxUncommittedRows=500000, o3MaxLag=600000000us;
```

#### Enterprise variant[​](#enterprise-variant "Direct link to Enterprise variant")

[QuestDB Enterprise](https://questdb.com/enterprise/) will include an additional `OWNED BY` clause populated with the current user.

For example,

```prism-code
CREATE TABLE trades (  
	symbol SYMBOL CAPACITY 256 CACHE,  
	side SYMBOL CAPACITY 256 CACHE,  
	price DOUBLE,  
	amount DOUBLE,  
	timestamp TIMESTAMP  
) timestamp(timestamp) PARTITION BY DAY WAL  
WITH maxUncommittedRows=500000, o3MaxLag=600000000us  
OWNED BY 'admin';
```

This clause assigns permissions for the table to that user.

If permissions should be assigned to a different user,
please modify this clause appropriately.

### SHOW CREATE VIEW[​](#show-create-view "Direct link to SHOW CREATE VIEW")

retrieving view ddl

```prism-code
SHOW CREATE VIEW my_view;
```

| ddl |
| --- |
| CREATE VIEW 'my\_view' AS (SELECT ts, symbol, price FROM trades); |

This returns the `CREATE VIEW` statement that would recreate the view,
including any `DECLARE` parameters if the view is parameterized.

### SHOW PARTITIONS[​](#show-partitions "Direct link to SHOW PARTITIONS")

```prism-code
SHOW PARTITIONS FROM my_table;
```

| index | partitionBy | name | minTimestamp | maxTimestamp | numRows | diskSize | diskSizeHuman | readOnly | active | attached | detached | attachable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | WEEK | 2022-W52 | 2023-01-01 00:36:00.0 | 2023-01-01 23:24:00.0 | 39 | 98304 | 96.0 KiB | false | false | true | false | false |
| 1 | WEEK | 2023-W01 | 2023-01-02 00:00:00.0 | 2023-01-08 23:24:00.0 | 280 | 98304 | 96.0 KiB | false | false | true | false | false |
| 2 | WEEK | 2023-W02 | 2023-01-09 00:00:00.0 | 2023-01-15 23:24:00.0 | 280 | 98304 | 96.0 KiB | false | false | true | false | false |
| 3 | WEEK | 2023-W03 | 2023-01-16 00:00:00.0 | 2023-01-18 12:00:00.0 | 101 | 83902464 | 80.0 MiB | false | true | true | false | false |

### SHOW PARAMETERS[​](#show-parameters "Direct link to SHOW PARAMETERS")

```prism-code
SHOW PARAMETERS;
```

The output demonstrates:

* `property_path`: the configuration key
* `env_var_name`: the matching env var for the key
* `value`: the current value of the key
* `value_source`: how the value is set (default, conf or env)
* `sensitive`: if it is a sensitive value (passwords)
* `reloadable`: if the value can be [reloaded without a server restart](/docs/configuration/overview/#reloadable-settings)

| property\_path | env\_var\_name | value | value\_source | sensitive | reloadable |
| --- | --- | --- | --- | --- | --- |
| http.min.net.connection.limit | QDB\_HTTP\_MIN\_NET\_CONNECTION\_LIMIT | 64 | default | false | false |
| line.http.enabled | QDB\_LINE\_HTTP\_ENABLED | true | default | false | false |
| cairo.parquet.export.row.group.size | QDB\_CAIRO\_PARQUET\_EXPORT\_ROW\_GROUP\_SIZE | 100000 | default | false | false |
| http.security.interrupt.on.closed.connection | QDB\_HTTP\_SECURITY\_INTERRUPT\_ON\_CLOSED\_CONNECTION | true | conf | false | false |
| pg.readonly.user.enabled | QDB\_PG\_READONLY\_USER\_ENABLED | true | conf | false | true |
| pg.readonly.password | QDB\_PG\_READONLY\_PASSWORD | \*\*\*\* | default | true | true |
| http.password | QDB\_HTTP\_PASSWORD | \*\*\*\* | default | true | false |

You can optionally chain `SHOW PARAMETERS` with other clauses:

```prism-code
-- This query will return all parameters where the value contains 'tmp', ignoring upper/lower case  
(SHOW PARAMETERS) WHERE value ILIKE '%tmp%';  
  
-- This query will return all parameters where the property_path is not 'cairo.root' or 'cairo.sql.backup.root', ordered by the first column  
(SHOW PARAMETERS) WHERE property_path NOT IN ('cairo.root', 'cairo.sql.backup.root') ORDER BY 1;  
  
-- This query will return all parameters where the value_source is 'env'  
(SHOW PARAMETERS) WHERE value_source = 'env';  
  
-- Show all the parameters that have been modified from their defaults, via conf file or env variable  
(SHOW PARAMETERS) WHERE  value_source <> 'default';
```

### SHOW USER[​](#show-user "Direct link to SHOW USER")

```prism-code
SHOW USER; --as john
```

or

```prism-code
SHOW USER john;
```

| auth\_type | enabled |
| --- | --- |
| Password | false |
| JWK Token | false |
| REST Token | false |

### SHOW USERS[​](#show-users "Direct link to SHOW USERS")

```prism-code
SHOW USERS;
```

| name |
| --- |
| admin |
| john |

### SHOW GROUPS[​](#show-groups "Direct link to SHOW GROUPS")

```prism-code
SHOW GROUPS;
```

or

```prism-code
SHOW GROUPS john;
```

| name |
| --- |
| management |

### SHOW SERVICE ACCOUNT[​](#show-service-account "Direct link to SHOW SERVICE ACCOUNT")

```prism-code
SHOW SERVICE ACCOUNT;
```

or

```prism-code
SHOW SERVICE ACCOUNT ilp_ingestion;
```

| auth\_type | enabled |
| --- | --- |
| Password | false |
| JWK Token | false |
| REST Token | false |

### SHOW SERVICE ACCOUNTS[​](#show-service-accounts "Direct link to SHOW SERVICE ACCOUNTS")

```prism-code
SHOW SERVICE ACCOUNTS;
```

| name |
| --- |
| management |
| svc1\_admin |

```prism-code
SHOW SERVICE ACCOUNTS john;
```

| name |
| --- |
| svc1\_admin |

```prism-code
SHOW SERVICE ACCOUNTS admin_group;
```

| name |
| --- |
| svc1\_admin |

### SHOW PERMISSIONS FOR CURRENT USER[​](#show-permissions-for-current-user "Direct link to SHOW PERMISSIONS FOR CURRENT USER")

```prism-code
SHOW PERMISSIONS;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT |  |  | t | G |

### SHOW PERMISSIONS user[​](#show-permissions-user "Direct link to SHOW PERMISSIONS user")

```prism-code
SHOW PERMISSIONS admin;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT |  |  | t | G |
| INSERT | orders |  | f | G |
| UPDATE | order\_itme | quantity | f | G |

### SHOW PERMISSIONS[​](#show-permissions "Direct link to SHOW PERMISSIONS")

#### For a group[​](#for-a-group "Direct link to For a group")

```prism-code
SHOW PERMISSIONS admin_group;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| INSERT | orders |  | f | G |

#### For a service account[​](#for-a-service-account "Direct link to For a service account")

```prism-code
SHOW PERMISSIONS ilp_ingestion;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT |  |  | t | G |
| INSERT |  |  | f | G |
| UPDATE |  |  | f | G |

### SHOW SERVER\_VERSION[​](#show-server_version "Direct link to SHOW SERVER_VERSION")

Shows PostgreSQL compatibility version.

```prism-code
SHOW SERVER_VERSION;
```

| server\_version |
| --- |
| 12.3 (questdb) |

## See also[​](#see-also "Direct link to See also")

The following functions allow querying tables and views with filters and using
the results as part of a function:

* [table\_columns()](/docs/query/functions/meta/#table_columns)
* [tables()](/docs/query/functions/meta/#tables)
* [table\_partitions()](/docs/query/functions/meta/#table_partitions)
* [views()](/docs/query/functions/meta/#views)