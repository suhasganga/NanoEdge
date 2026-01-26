On this page

`GRANT` - grants permissions to a user, group or service account.

For full documentation of the Access Control List and Role-based Access Control,
see the [RBAC operations](/docs/security/rbac/) page.

note

Role-based Access Control (RBAC) operations are only available in QuestDB
Enterprise.

---

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the GRANT keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5MDciIGhlaWdodD0iMzQzIj4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDYxIDEgNTcgMSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDYxIDkgNTcgOSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMSIgeT0iNDciIHdpZHRoPSI2NiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI5IiB5PSI0NSIgd2lkdGg9IjY2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSI2NSI+R1JBTlQ8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNwZXJtaXNzaW9uIiB4bGluazp0aXRsZT0icGVybWlzc2lvbiI+CiAgICAgICAgICAgIDxyZWN0IHg9IjEzNyIgeT0iNDciIHdpZHRoPSI4OCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIxMzUiIHk9IjQ1IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjE0NSIgeT0iNjUiPnBlcm1pc3Npb248L3RleHQ+PC9hPjxyZWN0IHg9IjEzNyIgeT0iMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTM1IiB5PSIxIiB3aWR0aD0iMjQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTQ1IiB5PSIyMSI+LDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMjg1IiB5PSI0NyIgd2lkdGg9IjQwIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjgzIiB5PSI0NSIgd2lkdGg9IjQwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjI5MyIgeT0iNjUiPk9OPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzNjUiIHk9IjQ3IiB3aWR0aD0iNDQiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzNjMiIHk9IjQ1IiB3aWR0aD0iNDQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzczIiB5PSI2NSI+QUxMPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI0MjkiIHk9IjQ3IiB3aWR0aD0iNzIiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI0MjciIHk9IjQ1IiB3aWR0aD0iNzIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDM3IiB5PSI2NSI+VEFCTEVTPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjdGFibGVOYW1lIiB4bGluazp0aXRsZT0idGFibGVOYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iMzg1IiB5PSIxNzkiIHdpZHRoPSI4OCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSIzODMiIHk9IjE3NyIgd2lkdGg9Ijg4IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzOTMiIHk9IjE5NyI+dGFibGVOYW1lPC90ZXh0PjwvYT48cmVjdCB4PSI1MTMiIHk9IjE3OSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNTExIiB5PSIxNzciIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI1MjEiIHk9IjE5NyI+KDwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI2NvbHVtbk5hbWUiIHhsaW5rOnRpdGxlPSJjb2x1bW5OYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iNTc5IiB5PSIxNzkiIHdpZHRoPSIxMDIiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iNTc3IiB5PSIxNzciIHdpZHRoPSIxMDIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjU4NyIgeT0iMTk3Ij5jb2x1bW5OYW1lPC90ZXh0PjwvYT48cmVjdCB4PSI1NzkiIHk9IjEzNSIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNTc3IiB5PSIxMzMiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI1ODciIHk9IjE1MyI+LDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNzIxIiB5PSIxNzkiIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjcxOSIgeT0iMTc3IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNzI5IiB5PSIxOTciPik8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjM4NSIgeT0iOTEiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjM4MyIgeT0iODkiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzOTMiIHk9IjEwOSI+LDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iODQ3IiB5PSI0NyIgd2lkdGg9IjM4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iODQ1IiB5PSI0NSIgd2lkdGg9IjM4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9Ijg1NSIgeT0iNjUiPlRPPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjZW50aXR5TmFtZSIgeGxpbms6dGl0bGU9ImVudGl0eU5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSIyMjciIHk9IjI3NyIgd2lkdGg9IjkyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjIyNSIgeT0iMjc1IiB3aWR0aD0iOTIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjIzNSIgeT0iMjk1Ij5lbnRpdHlOYW1lPC90ZXh0PjwvYT48cmVjdCB4PSIzNTkiIHk9IjMwOSIgd2lkdGg9IjU4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMzU3IiB5PSIzMDciIHdpZHRoPSI1OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIzNjciIHk9IjMyNyI+V0lUSDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNDM3IiB5PSIzMDkiIHdpZHRoPSI2NiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQzNSIgeT0iMzA3IiB3aWR0aD0iNjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDQ1IiB5PSIzMjciPkdSQU5UPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI1MjMiIHk9IjMwOSIgd2lkdGg9Ijc2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNTIxIiB5PSIzMDciIHdpZHRoPSI3NiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI1MzEiIHk9IjMyNyI+T1BUSU9OPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI2NTkiIHk9IjMwOSIgd2lkdGg9IjU4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNjU3IiB5PSIzMDciIHdpZHRoPSI1OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI2NjciIHk9IjMyNyI+V0lUSDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNzM3IiB5PSIzMDkiIHdpZHRoPSIxMjIiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI3MzUiIHk9IjMwNyIgd2lkdGg9IjEyMiIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI3NDUiIHk9IjMyNyI+VkVSSUZJQ0FUSU9OPC90ZXh0PgogICAgICAgICA8cGF0aCBjbGFzcz0ibGluZSIgZD0ibTE3IDYxIGgyIG0wIDAgaDEwIG02NiAwIGgxMCBtMjAgMCBoMTAgbTg4IDAgaDEwIG0tMTI4IDAgbDIwIDAgbS0xIDAgcS05IDAgLTkgLTEwIGwwIC0yNCBxMCAtMTAgMTAgLTEwIG0xMDggNDQgbDIwIDAgbS0yMCAwIHExMCAwIDEwIC0xMCBsMCAtMjQgcTAgLTEwIC0xMCAtMTAgbS0xMDggMCBoMTAgbTI0IDAgaDEwIG0wIDAgaDY0IG00MCA0NCBoMTAgbTQwIDAgaDEwIG0yMCAwIGgxMCBtNDQgMCBoMTAgbTAgMCBoMTAgbTcyIDAgaDEwIG0wIDAgaDI4NiBtLTQ2MiAwIGgyMCBtNDQyIDAgaDIwIG0tNDgyIDAgcTEwIDAgMTAgMTAgbTQ2MiAwIHEwIC0xMCAxMCAtMTAgbS00NzIgMTAgdjExMiBtNDYyIDAgdi0xMTIgbS00NjIgMTEyIHEwIDEwIDEwIDEwIG00NDIgMCBxMTAgMCAxMCAtMTAgbS00MzIgMTAgaDEwIG04OCAwIGgxMCBtMjAgMCBoMTAgbTI2IDAgaDEwIG0yMCAwIGgxMCBtMTAyIDAgaDEwIG0tMTQyIDAgbDIwIDAgbS0xIDAgcS05IDAgLTkgLTEwIGwwIC0yNCBxMCAtMTAgMTAgLTEwIG0xMjIgNDQgbDIwIDAgbS0yMCAwIHExMCAwIDEwIC0xMCBsMCAtMjQgcTAgLTEwIC0xMCAtMTAgbS0xMjIgMCBoMTAgbTI0IDAgaDEwIG0wIDAgaDc4IG0yMCA0NCBoMTAgbTI2IDAgaDEwIG0tMjc0IDAgaDIwIG0yNTQgMCBoMjAgbS0yOTQgMCBxMTAgMCAxMCAxMCBtMjc0IDAgcTAgLTEwIDEwIC0xMCBtLTI4NCAxMCB2MTQgbTI3NCAwIHYtMTQgbS0yNzQgMTQgcTAgMTAgMTAgMTAgbTI1NCAwIHExMCAwIDEwIC0xMCBtLTI2NCAxMCBoMTAgbTAgMCBoMjQ0IG0tNDAyIC0zNCBsMjAgMCBtLTEgMCBxLTkgMCAtOSAtMTAgbDAgLTY4IHEwIC0xMCAxMCAtMTAgbTQwMiA4OCBsMjAgMCBtLTIwIDAgcTEwIDAgMTAgLTEwIGwwIC02OCBxMCAtMTAgLTEwIC0xMCBtLTQwMiAwIGgxMCBtMjQgMCBoMTAgbTAgMCBoMzU4IG0tNTIyIC00NCBoMjAgbTU0MiAwIGgyMCBtLTU4MiAwIHExMCAwIDEwIDEwIG01NjIgMCBxMCAtMTAgMTAgLTEwIG0tNTcyIDEwIHYxNjIgbTU2MiAwIHYtMTYyIG0tNTYyIDE2MiBxMCAxMCAxMCAxMCBtNTQyIDAgcTEwIDAgMTAgLTEwIG0tNTUyIDEwIGgxMCBtMCAwIGg1MzIgbTIwIC0xODIgaDEwIG0zOCAwIGgxMCBtMiAwIGwyIDAgbTIgMCBsMiAwIG0yIDAgbDIgMCBtLTcwMiAyMzAgbDIgMCBtMiAwIGwyIDAgbTIgMCBsMiAwIG0yIDAgaDEwIG05MiAwIGgxMCBtMjAgMCBoMTAgbTAgMCBoMjUwIG0tMjgwIDAgaDIwIG0yNjAgMCBoMjAgbS0zMDAgMCBxMTAgMCAxMCAxMCBtMjgwIDAgcTAgLTEwIDEwIC0xMCBtLTI5MCAxMCB2MTIgbTI4MCAwIHYtMTIgbS0yODAgMTIgcTAgMTAgMTAgMTAgbTI2MCAwIHExMCAwIDEwIC0xMCBtLTI3MCAxMCBoMTAgbTU4IDAgaDEwIG0wIDAgaDEwIG02NiAwIGgxMCBtMCAwIGgxMCBtNzYgMCBoMTAgbTQwIC0zMiBoMTAgbTAgMCBoMjEwIG0tMjQwIDAgaDIwIG0yMjAgMCBoMjAgbS0yNjAgMCBxMTAgMCAxMCAxMCBtMjQwIDAgcTAgLTEwIDEwIC0xMCBtLTI1MCAxMCB2MTIgbTI0MCAwIHYtMTIgbS0yNDAgMTIgcTAgMTAgMTAgMTAgbTIyMCAwIHExMCAwIDEwIC0xMCBtLTIzMCAxMCBoMTAgbTU4IDAgaDEwIG0wIDAgaDEwIG0xMjIgMCBoMTAgbTIzIC0zMiBoLTMiPjwvcGF0aD4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI4OTcgMjkxIDkwNSAyODcgOTA1IDI5NSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9Ijg5NyAyOTEgODg5IDI4NyA4ODkgMjk1Ij48L3BvbHlnb24+Cjwvc3ZnPg==)

## Description[​](#description "Direct link to Description")

* `GRANT [permissions] TO entity` - grant database level permissions on database
  level to an entity
* `GRANT [permissions] ON ALL TABLES TO entity` - grant table/column level
  permissions on database level to an entity
* `GRANT [permissions] ON [table] TO entity` - grant table/column level
  permissions on table level to an entity
* `GRANT [permissions] ON [table(columns)] TO entity` - grant column level
  permissions on column level to an entity

### Grant database level permissions[​](#grant-database-level-permissions "Direct link to Grant database level permissions")

```prism-code
GRANT CREATE TABLE, SNAPSHOT TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| CREATE TABLE |  |  | f | G |
| SNAPSHOT |  |  | f | G |

### Grant table level permissions for entire database[​](#grant-table-level-permissions-for-entire-database "Direct link to Grant table level permissions for entire database")

```prism-code
GRANT ADD INDEX, REINDEX ON ALL TABLES TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| ADD INDEX |  |  | f | G |
| REINDEX |  |  | f | G |

### Grant table level permissions on specific tables[​](#grant-table-level-permissions-on-specific-tables "Direct link to Grant table level permissions on specific tables")

```prism-code
GRANT ADD INDEX, REINDEX ON orders, trades TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| ADD INDEX | trades |  | f | G |
| REINDEX | trades |  | f | G |
| ADD INDEX | orders |  | f | G |
| REINDEX | orders |  | f | G |

### Grant column level permissions for entire database[​](#grant-column-level-permissions-for-entire-database "Direct link to Grant column level permissions for entire database")

```prism-code
GRANT SELECT ON ALL TABLES TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT |  |  | f | G |

### Grant column level permissions on specific tables[​](#grant-column-level-permissions-on-specific-tables "Direct link to Grant column level permissions on specific tables")

```prism-code
GRANT SELECT ON orders TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | orders |  | f | G |

### Grant column level permissions on specific columns[​](#grant-column-level-permissions-on-specific-columns "Direct link to Grant column level permissions on specific columns")

```prism-code
GRANT SELECT ON orders(id, name), trades(id, quantity) TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | trades | id | f | G |
| SELECT | trades | quantity | f | G |
| SELECT | orders | id | f | G |
| SELECT | orders | name | f | G |

### Grant option[​](#grant-option "Direct link to Grant option")

If the `WITH GRANT OPTION` clause is present, then the target entity is allowed
to grant the permissions to other entities. If the entity already has
permissions matching those being granted, their grant option is overwritten.

```prism-code
GRANT SELECT ON ALL TABLES TO john WITH GRANT OPTION;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT |  |  | t | G |

```prism-code
GRANT SELECT ON ALL TABLES TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT |  |  | f | G |

### Verification[​](#verification "Direct link to Verification")

By default, `GRANT` does not check whether entities exist, making it possible to
grant permissions to users, groups or service accounts that are later created.

To make sure that the target entity of the grant statement exists, use
[verification](/docs/security/rbac/#grant-verification). The
`WITH VERIFICATION` clause enables checks on the target entity and causes the
`GRANT` statement to fail if the entity does not exist.

```prism-code
GRANT SELECT ON orders TO john WITH VERIFICATION;
```

### Implicit permissions[​](#implicit-permissions "Direct link to Implicit permissions")

In QuestDB, the timestamp column of a table is crucial for time-series
operations like `ASOF` and `LT` joins, `SAMPLE BY` and interval scans. If a user
can access some columns but not the timestamp column, they cannot execute most
queries.

Therefore when a table has a designated timestamp, granting `SELECT` or `UPDATE`
permissions on any column will automatically extend those permissions to the
timestamp column. These are known as
[implicit permissions](/docs/security/rbac/#implicit-permissions), and they're
indicated by an `I` in the `origin` column of the `SHOW PERMISSIONS` output.

For example, if you grant `UPDATE` permission on the `id` column of the
`products` table, the timestamp column also receives `UPDATE` permission:

```prism-code
CREATE TABLE products(id int, name string, ts timestamp) timestamp(ts);  
GRANT UPDATE ON products(id) TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| UPDATE | products | id | f | G |
| UPDATE | products | ts | f | I |

### Optimization[​](#optimization "Direct link to Optimization")

When granting permissions on the table or column level, sometimes it might seem
like there is no effect when cross-checking with the `SHOW permissions` command.
If QuestDB detects that the permission is already granted on a higher level, it
optimizes and removes any child permissions. Doing so keeps the access list
model simple and permission checks faster.

For example, granting the same permission on the database and table level shows
will show the permission on database level only:

```prism-code
GRANT INSERT ON ALL TABLES TO john;  
GRANT INSERT ON products TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| INSERT |  |  | f | G |

Granting the same permission on the table and column level shows permission on
the table level only:

```prism-code
GRANT SELECT ON products TO john;  
GRANT SELECT ON products(id) TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | products |  | f | G |

### Grant ahead of table or column creation[​](#grant-ahead-of-table-or-column-creation "Direct link to Grant ahead of table or column creation")

Grant permissions ahead of table or column creation:

```prism-code
GRANT SELECT ON countries TO john;  
GRANT UPDATE ON countries(id) TO john;  
GRANT UPDATE ON countries(description) TO john;
```

Such permissions do not show on `SHOW PERMISSIONS` output.

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |

However, when the table is created, then the applicable permissions appear:

```prism-code
CREATE TABLE countries (id INT, name STRING, iso_code STRING);
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | countries |  | f | G |
| UPDATE | countries | id | f | G |

When 'missing' columns are later added to the table, then more permissions
appear:

```prism-code
ALTER TABLE countries ADD COLUMN description string;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | countries |  | f | G |
| UPDATE | countries | id | f | G |
| UPDATE | countries | description | f | G |

### Grant when table or column is dropped and recreated[​](#grant-when-table-or-column-is-dropped-and-recreated "Direct link to Grant when table or column is dropped and recreated")

Granted permissions are not automatically revoked when related tables or columns
are dropped. Instead, they have no effect until table or column is recreated.

```prism-code
CREATE TABLE countries (id INT, name STRING, iso_code STRING);  
GRANT SELECT ON countries TO john;  
GRANT UPDATE ON countries(iso_code) TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | countries |  | f | G |
| UPDATE | countries | iso\_code | f | G |

Now, if the table is dropped, then permission stops being visible:

```prism-code
DROP TABLE countries;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |

When the table is later recreated, permission are in full effect again :

```prism-code
CREATE TABLE countries (id INT, name STRING, iso_code int, alpha2 STRING);
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | countries |  | f | G |
| UPDATE | countries |  | f | G |

note

Only the table and/or column name is used when applying permission. The type is
ignored. In the example above `iso_code` was initially of string type, then
recreated as int.

### Owner grants[​](#owner-grants "Direct link to Owner grants")

In QuestDB there are no owners of database objects. Instead, there are
[owner grants](/docs/security/rbac/#owner-grants).

An owner grant means:

* if a user creates a table, the user automatically gets all table level
  permissions with the grant option on the table
* if a user adds a new column to an existing table, the user automatically gets
  all column level permissions with the grant option on the column