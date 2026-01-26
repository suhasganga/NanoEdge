On this page

Window functions perform calculations across sets of table rows related to the current row. Unlike aggregate functions that return a single result for a group of rows, window functions return a value for **every row** while considering a "window" of related rows defined by the `OVER` clause.

![Window function animation showing how a sliding window moves through rows, calculating results for each position](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjUyMCIgdmlld0JveD0iMCAwIDEyMDAgNTIwIj4KICA8ZGVmcz4KICAgIDxzdHlsZT4KICAgICAgLnRpdGxlIHsgZm9udDogMTRweCAiSUJNIFBsZXggTW9ubyIsIE1lbmxvLCBtb25vc3BhY2U7IGZpbGw6ICNmZmZmZmY7IH0KICAgICAgLmxhYmVsIHsgZm9udDogMTNweCAiSUJNIFBsZXggU2FucyIsICJIZWx2ZXRpY2EgTmV1ZSIsIEFyaWFsLCBzYW5zLXNlcmlmOyBmaWxsOiAjZDlkOWQ5OyB9CiAgICAgIC5jZWxsIHsgZm9udDogMTNweCAiSUJNIFBsZXggTW9ubyIsIE1lbmxvLCBtb25vc3BhY2U7IGZpbGw6ICNmZmZmZmY7IH0KICAgICAgLnRhYmxlLW91dGxpbmUgeyBmaWxsOiAjMWIxYzI2OyBzdHJva2U6ICM1MTUzNWY7IHN0cm9rZS13aWR0aDogMTsgfQogICAgICAuaGVhZGVyIHsgZmlsbDogIzMyMzQzZTsgfQogICAgICAuZ3JpZCB7IHN0cm9rZTogIzNiM2Q0YTsgc3Ryb2tlLXdpZHRoOiAxOyB9CiAgICAgIC53aW5kb3cgeyBmaWxsOiAjZTI4OWE0OyBvcGFjaXR5OiAwLjM1OyB9CiAgICAgIC5jdXJyZW50IHsgZmlsbDogbm9uZTsgc3Ryb2tlOiAjMGNjMGRmOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgLnJlc3VsdC1oaWdobGlnaHQgeyBmaWxsOiAjZTI4OWE0OyBvcGFjaXR5OiAwLjQ1OyB9CiAgICAgIC5wb2ludGVyIHsgZmlsbDogIzBjYzBkZjsgfQogICAgICAubGluay1saW5lIHsgc3Ryb2tlOiAjMGNjMGRmOyBzdHJva2Utd2lkdGg6IDI7IGZpbGw6IG5vbmU7IH0KICAgICAgLm5vdGUgeyBmb250OiAxMnB4ICJJQk0gUGxleCBTYW5zIiwgIkhlbHZldGljYSBOZXVlIiwgQXJpYWwsIHNhbnMtc2VyaWY7IGZpbGw6ICNiMWI1ZDM7IH0KICAgIDwvc3R5bGU+CiAgICA8bWFya2VyIGlkPSJsaW5rLWFycm93IiBtYXJrZXJXaWR0aD0iMTAiIG1hcmtlckhlaWdodD0iOCIgcmVmWD0iOSIgcmVmWT0iNCIgb3JpZW50PSJhdXRvIiBtYXJrZXJVbml0cz0ic3Ryb2tlV2lkdGgiPgogICAgICA8cG9seWdvbiBwb2ludHM9IjAsMCAxMCw0IDAsOCIgZmlsbD0iIzBjYzBkZiIvPgogICAgPC9tYXJrZXI+CiAgPC9kZWZzPgoKICA8dGV4dCBjbGFzcz0idGl0bGUiIHg9IjYwIiB5PSIzMiI+CiAgICBTRUxFQ1QgdGltZXN0YW1wLCBwcmljZSwgPHRzcGFuIGZpbGw9IiNlMjg5YTQiPmF2ZyhwcmljZSkgT1ZFUiAoT1JERVIgQlkgdGltZXN0YW1wPC90c3Bhbj4KICAgIDx0c3BhbiB4PSI2MCIgZHk9IjE4Ij48dHNwYW4gZmlsbD0iI2UyODlhNCI+Uk9XUyBCRVRXRUVOIDMgUFJFQ0VESU5HIEFORCBDVVJSRU5UIFJPVyk8L3RzcGFuPiBtb3ZpbmdfYXZnPC90c3Bhbj4KICAgIDx0c3BhbiB4PSI2MCIgZHk9IjE4Ij5GUk9NIHRyYWRlcyBMSU1JVCAxMDs8L3RzcGFuPgogIDwvdGV4dD4KICA8dGV4dCBjbGFzcz0ibm90ZSIgeD0iNjAiIHk9IjkwIj5RdWVzdERCIHBpbmsgd2luZG93IHNob3dzIHRoZSBmcmFtZSB1c2VkIGZvciBlYWNoIG1vdmluZyBhdmVyYWdlLjwvdGV4dD4KCiAgPCEtLSBMZWZ0IHRhYmxlOiB0cmFkZXMgLS0+CiAgPHJlY3QgY2xhc3M9InRhYmxlLW91dGxpbmUiIHg9IjYwIiB5PSIxMjAiIHdpZHRoPSI0MjAiIGhlaWdodD0iMzU2Ii8+CiAgPHJlY3QgY2xhc3M9ImhlYWRlciIgeD0iNjAiIHk9IjEyMCIgd2lkdGg9IjQyMCIgaGVpZ2h0PSIzNiIvPgogIDxsaW5lIGNsYXNzPSJncmlkIiB4MT0iMzIwIiB5MT0iMTIwIiB4Mj0iMzIwIiB5Mj0iNDc2Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI2MCIgeTE9IjE1NiIgeDI9IjQ4MCIgeTI9IjE1NiIvPgogIDxsaW5lIGNsYXNzPSJncmlkIiB4MT0iNjAiIHkxPSIxODgiIHgyPSI0ODAiIHkyPSIxODgiLz4KICA8bGluZSBjbGFzcz0iZ3JpZCIgeDE9IjYwIiB5MT0iMjIwIiB4Mj0iNDgwIiB5Mj0iMjIwIi8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI2MCIgeTE9IjI1MiIgeDI9IjQ4MCIgeTI9IjI1MiIvPgogIDxsaW5lIGNsYXNzPSJncmlkIiB4MT0iNjAiIHkxPSIyODQiIHgyPSI0ODAiIHkyPSIyODQiLz4KICA8bGluZSBjbGFzcz0iZ3JpZCIgeDE9IjYwIiB5MT0iMzE2IiB4Mj0iNDgwIiB5Mj0iMzE2Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI2MCIgeTE9IjM0OCIgeDI9IjQ4MCIgeTI9IjM0OCIvPgogIDxsaW5lIGNsYXNzPSJncmlkIiB4MT0iNjAiIHkxPSIzODAiIHgyPSI0ODAiIHkyPSIzODAiLz4KICA8bGluZSBjbGFzcz0iZ3JpZCIgeDE9IjYwIiB5MT0iNDEyIiB4Mj0iNDgwIiB5Mj0iNDEyIi8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI2MCIgeTE9IjQ0NCIgeDI9IjQ4MCIgeTI9IjQ0NCIvPgoKICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9IjcyIiB5PSIxNDQiPnRpbWVzdGFtcDwvdGV4dD4KICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9IjQwOCIgeT0iMTQ0IiB0ZXh0LWFuY2hvcj0iZW5kIj5wcmljZTwvdGV4dD4KCiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcyIiB5PSIxNzciPjA5OjMwOjAwPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI0MDgiIHk9IjE3NyIgdGV4dC1hbmNob3I9ImVuZCI+MTAwPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI3MiIgeT0iMjA5Ij4wOTozMDowMTwvdGV4dD4KICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNDA4IiB5PSIyMDkiIHRleHQtYW5jaG9yPSJlbmQiPjEwMTwvdGV4dD4KICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNzIiIHk9IjI0MSI+MDk6MzA6MDI8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjQwOCIgeT0iMjQxIiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDM8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcyIiB5PSIyNzMiPjA5OjMwOjAzPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI0MDgiIHk9IjI3MyIgdGV4dC1hbmNob3I9ImVuZCI+MTAyPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI3MiIgeT0iMzA1Ij4wOTozMDowNDwvdGV4dD4KICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNDA4IiB5PSIzMDUiIHRleHQtYW5jaG9yPSJlbmQiPjEwNDwvdGV4dD4KICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNzIiIHk9IjMzNyI+MDk6MzA6MDU8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjQwOCIgeT0iMzM3IiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDU8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcyIiB5PSIzNjkiPjA5OjMwOjA2PC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI0MDgiIHk9IjM2OSIgdGV4dC1hbmNob3I9ImVuZCI+MTAzPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI3MiIgeT0iNDAxIj4wOTozMDowNzwvdGV4dD4KICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNDA4IiB5PSI0MDEiIHRleHQtYW5jaG9yPSJlbmQiPjEwNjwvdGV4dD4KICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNzIiIHk9IjQzMyI+MDk6MzA6MDg8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjQwOCIgeT0iNDMzIiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDg8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcyIiB5PSI0NjUiPjA5OjMwOjA5PC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI0MDgiIHk9IjQ2NSIgdGV4dC1hbmNob3I9ImVuZCI+MTA3PC90ZXh0PgoKICA8IS0tIFdpbmRvdyBoaWdobGlnaHQgb24gbGVmdCB0YWJsZSAtLT4KICA8cmVjdCBjbGFzcz0id2luZG93IiB4PSI2MCIgeT0iMTU2IiB3aWR0aD0iNDIwIiBoZWlnaHQ9IjMyIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9InkiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgY2FsY01vZGU9ImRpc2NyZXRlIgogICAgICB2YWx1ZXM9IjE1NjsxNTY7MTU2OzE1NjsxODg7MjIwOzI1MjsyODQ7MzE2OzM0OCIvPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iaGVpZ2h0IiBkdXI9IjEwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGNhbGNNb2RlPSJkaXNjcmV0ZSIKICAgICAgdmFsdWVzPSIzMjs2NDs5NjsxMjg7MTI4OzEyODsxMjg7MTI4OzEyODsxMjgiLz4KICA8L3JlY3Q+CgogIDwhLS0gQ3VycmVudCByb3cgb3V0bGluZSArIHBvaW50ZXIgLS0+CiAgPHJlY3QgY2xhc3M9ImN1cnJlbnQiIHg9IjYwIiB5PSIxNTYiIHdpZHRoPSI0MjAiIGhlaWdodD0iMzIiPgogICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJ0cmFuc2xhdGUiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgY2FsY01vZGU9ImRpc2NyZXRlIgogICAgICB2YWx1ZXM9IjAgMDswIDMyOzAgNjQ7MCA5NjswIDEyODswIDE2MDswIDE5MjswIDIyNDswIDI1NjswIDI4OCIvPgogIDwvcmVjdD4KICA8cG9seWdvbiBjbGFzcz0icG9pbnRlciIgcG9pbnRzPSI0NCwxNzIgNTQsMTY2IDU0LDE3OCI+CiAgICA8YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InRyYW5zbGF0ZSIgZHVyPSIxMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBjYWxjTW9kZT0iZGlzY3JldGUiCiAgICAgIHZhbHVlcz0iMCAwOzAgMzI7MCA2NDswIDk2OzAgMTI4OzAgMTYwOzAgMTkyOzAgMjI0OzAgMjU2OzAgMjg4Ii8+CiAgPC9wb2x5Z29uPgoKICA8IS0tIExpbmsgYmV0d2VlbiBjdXJyZW50IGlucHV0IHJvdyBhbmQgb3V0cHV0IHJvdyAtLT4KICA8bGluZSBjbGFzcz0ibGluay1saW5lIiB4MT0iNDkwIiB5MT0iMTcyIiB4Mj0iNjkwIiB5Mj0iMTcyIiBtYXJrZXItZW5kPSJ1cmwoI2xpbmstYXJyb3cpIj4KICAgIDxhbmltYXRlVHJhbnNmb3JtIGF0dHJpYnV0ZU5hbWU9InRyYW5zZm9ybSIgdHlwZT0idHJhbnNsYXRlIiBkdXI9IjEwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGNhbGNNb2RlPSJkaXNjcmV0ZSIKICAgICAgdmFsdWVzPSIwIDA7MCAzMjswIDY0OzAgOTY7MCAxMjg7MCAxNjA7MCAxOTI7MCAyMjQ7MCAyNTY7MCAyODgiLz4KICA8L2xpbmU+CgogIDwhLS0gUmlnaHQgdGFibGU6IHJlc3VsdHMgLS0+CiAgPHJlY3QgY2xhc3M9InRhYmxlLW91dGxpbmUiIHg9IjcwMCIgeT0iMTIwIiB3aWR0aD0iNDIwIiBoZWlnaHQ9IjM1NiIvPgogIDxyZWN0IGNsYXNzPSJoZWFkZXIiIHg9IjcwMCIgeT0iMTIwIiB3aWR0aD0iNDIwIiBoZWlnaHQ9IjM2Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI4ODAiIHkxPSIxMjAiIHgyPSI4ODAiIHkyPSI0NzYiLz4KICA8bGluZSBjbGFzcz0iZ3JpZCIgeDE9IjEwMDAiIHkxPSIxMjAiIHgyPSIxMDAwIiB5Mj0iNDc2Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIxNTYiIHgyPSIxMTIwIiB5Mj0iMTU2Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIxODgiIHgyPSIxMTIwIiB5Mj0iMTg4Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIyMjAiIHgyPSIxMTIwIiB5Mj0iMjIwIi8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIyNTIiIHgyPSIxMTIwIiB5Mj0iMjUyIi8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIyODQiIHgyPSIxMTIwIiB5Mj0iMjg0Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIzMTYiIHgyPSIxMTIwIiB5Mj0iMzE2Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIzNDgiIHgyPSIxMTIwIiB5Mj0iMzQ4Ii8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSIzODAiIHgyPSIxMTIwIiB5Mj0iMzgwIi8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSI0MTIiIHgyPSIxMTIwIiB5Mj0iNDEyIi8+CiAgPGxpbmUgY2xhc3M9ImdyaWQiIHgxPSI3MDAiIHkxPSI0NDQiIHgyPSIxMTIwIiB5Mj0iNDQ0Ii8+CgogIDx0ZXh0IGNsYXNzPSJsYWJlbCIgeD0iNzEyIiB5PSIxNDQiPnRpbWVzdGFtcDwvdGV4dD4KICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9Ijk4OCIgeT0iMTQ0IiB0ZXh0LWFuY2hvcj0iZW5kIj5wcmljZTwvdGV4dD4KICA8dGV4dCBjbGFzcz0ibGFiZWwiIHg9IjExMDgiIHk9IjE0NCIgdGV4dC1hbmNob3I9ImVuZCI+bW92aW5nX2F2ZzwvdGV4dD4KCiAgPGcgY2xhc3M9InJlc3VsdC1yb3ciPgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcxMiIgeT0iMTc3Ij4wOTozMDowMDwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI5ODgiIHk9IjE3NyIgdGV4dC1hbmNob3I9ImVuZCI+MTAwPC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjExMDgiIHk9IjE3NyIgdGV4dC1hbmNob3I9ImVuZCI+MTAwLjAwPC90ZXh0PgogIDwvZz4KICA8ZyBjbGFzcz0icmVzdWx0LXJvdyIgb3BhY2l0eT0iMCI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiBkdXI9IjEwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGNhbGNNb2RlPSJkaXNjcmV0ZSIKICAgICAgdmFsdWVzPSIwOzE7MTsxOzE7MTsxOzE7MTsxIi8+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNzEyIiB5PSIyMDkiPjA5OjMwOjAxPC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9Ijk4OCIgeT0iMjA5IiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDE8L3RleHQ+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iMTEwOCIgeT0iMjA5IiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDAuNTA8L3RleHQ+CiAgPC9nPgogIDxnIGNsYXNzPSJyZXN1bHQtcm93IiBvcGFjaXR5PSIwIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9Im9wYWNpdHkiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgY2FsY01vZGU9ImRpc2NyZXRlIgogICAgICB2YWx1ZXM9IjA7MDsxOzE7MTsxOzE7MTsxOzEiLz4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI3MTIiIHk9IjI0MSI+MDk6MzA6MDI8L3RleHQ+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iOTg4IiB5PSIyNDEiIHRleHQtYW5jaG9yPSJlbmQiPjEwMzwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSIxMTA4IiB5PSIyNDEiIHRleHQtYW5jaG9yPSJlbmQiPjEwMS4zMzwvdGV4dD4KICA8L2c+CiAgPGcgY2xhc3M9InJlc3VsdC1yb3ciIG9wYWNpdHk9IjAiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgZHVyPSIxMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBjYWxjTW9kZT0iZGlzY3JldGUiCiAgICAgIHZhbHVlcz0iMDswOzA7MTsxOzE7MTsxOzE7MSIvPgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcxMiIgeT0iMjczIj4wOTozMDowMzwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI5ODgiIHk9IjI3MyIgdGV4dC1hbmNob3I9ImVuZCI+MTAyPC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjExMDgiIHk9IjI3MyIgdGV4dC1hbmNob3I9ImVuZCI+MTAxLjUwPC90ZXh0PgogIDwvZz4KICA8ZyBjbGFzcz0icmVzdWx0LXJvdyIgb3BhY2l0eT0iMCI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiBkdXI9IjEwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGNhbGNNb2RlPSJkaXNjcmV0ZSIKICAgICAgdmFsdWVzPSIwOzA7MDswOzE7MTsxOzE7MTsxIi8+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNzEyIiB5PSIzMDUiPjA5OjMwOjA0PC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9Ijk4OCIgeT0iMzA1IiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDQ8L3RleHQ+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iMTEwOCIgeT0iMzA1IiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDIuNTA8L3RleHQ+CiAgPC9nPgogIDxnIGNsYXNzPSJyZXN1bHQtcm93IiBvcGFjaXR5PSIwIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9Im9wYWNpdHkiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgY2FsY01vZGU9ImRpc2NyZXRlIgogICAgICB2YWx1ZXM9IjA7MDswOzA7MDsxOzE7MTsxOzEiLz4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI3MTIiIHk9IjMzNyI+MDk6MzA6MDU8L3RleHQ+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iOTg4IiB5PSIzMzciIHRleHQtYW5jaG9yPSJlbmQiPjEwNTwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSIxMTA4IiB5PSIzMzciIHRleHQtYW5jaG9yPSJlbmQiPjEwMy41MDwvdGV4dD4KICA8L2c+CiAgPGcgY2xhc3M9InJlc3VsdC1yb3ciIG9wYWNpdHk9IjAiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgZHVyPSIxMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBjYWxjTW9kZT0iZGlzY3JldGUiCiAgICAgIHZhbHVlcz0iMDswOzA7MDswOzA7MTsxOzE7MSIvPgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcxMiIgeT0iMzY5Ij4wOTozMDowNjwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI5ODgiIHk9IjM2OSIgdGV4dC1hbmNob3I9ImVuZCI+MTAzPC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjExMDgiIHk9IjM2OSIgdGV4dC1hbmNob3I9ImVuZCI+MTAzLjUwPC90ZXh0PgogIDwvZz4KICA8ZyBjbGFzcz0icmVzdWx0LXJvdyIgb3BhY2l0eT0iMCI+CiAgICA8YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiBkdXI9IjEwcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGNhbGNNb2RlPSJkaXNjcmV0ZSIKICAgICAgdmFsdWVzPSIwOzA7MDswOzA7MDswOzE7MTsxIi8+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iNzEyIiB5PSI0MDEiPjA5OjMwOjA3PC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9Ijk4OCIgeT0iNDAxIiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDY8L3RleHQ+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iMTEwOCIgeT0iNDAxIiB0ZXh0LWFuY2hvcj0iZW5kIj4xMDQuNTA8L3RleHQ+CiAgPC9nPgogIDxnIGNsYXNzPSJyZXN1bHQtcm93IiBvcGFjaXR5PSIwIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9Im9wYWNpdHkiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgY2FsY01vZGU9ImRpc2NyZXRlIgogICAgICB2YWx1ZXM9IjA7MDswOzA7MDswOzA7MDsxOzEiLz4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI3MTIiIHk9IjQzMyI+MDk6MzA6MDg8L3RleHQ+CiAgICA8dGV4dCBjbGFzcz0iY2VsbCIgeD0iOTg4IiB5PSI0MzMiIHRleHQtYW5jaG9yPSJlbmQiPjEwODwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSIxMTA4IiB5PSI0MzMiIHRleHQtYW5jaG9yPSJlbmQiPjEwNS41MDwvdGV4dD4KICA8L2c+CiAgPGcgY2xhc3M9InJlc3VsdC1yb3ciIG9wYWNpdHk9IjAiPgogICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgZHVyPSIxMHMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBjYWxjTW9kZT0iZGlzY3JldGUiCiAgICAgIHZhbHVlcz0iMDswOzA7MDswOzA7MDswOzA7MSIvPgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjcxMiIgeT0iNDY1Ij4wOTozMDowOTwvdGV4dD4KICAgIDx0ZXh0IGNsYXNzPSJjZWxsIiB4PSI5ODgiIHk9IjQ2NSIgdGV4dC1hbmNob3I9ImVuZCI+MTA3PC90ZXh0PgogICAgPHRleHQgY2xhc3M9ImNlbGwiIHg9IjExMDgiIHk9IjQ2NSIgdGV4dC1hbmNob3I9ImVuZCI+MTA2LjAwPC90ZXh0PgogIDwvZz4KCiAgPCEtLSBIaWdobGlnaHQgY3VycmVudCByZXN1bHQgY2VsbCAtLT4KICA8cmVjdCBjbGFzcz0icmVzdWx0LWhpZ2hsaWdodCIgeD0iMTAwMCIgeT0iMTU2IiB3aWR0aD0iMTIwIiBoZWlnaHQ9IjMyIj4KICAgIDxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9InkiIGR1cj0iMTBzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIgY2FsY01vZGU9ImRpc2NyZXRlIgogICAgICB2YWx1ZXM9IjE1NjsxODg7MjIwOzI1MjsyODQ7MzE2OzM0ODszODA7NDEyOzQ0NCIvPgogIDwvcmVjdD4KPC9zdmc+Cg==)

## Syntax[​](#syntax "Direct link to Syntax")

```prism-code
function_name(arguments) OVER (  
    [PARTITION BY column [, ...]]  
    [ORDER BY column [ASC | DESC] [, ...]]  
    [frame_clause]  
)
```

* **`PARTITION BY`**: Divides rows into groups; the function resets for each group
* **`ORDER BY`**: Defines the order of rows within each partition
* **`frame_clause`**: Specifies which rows relative to the current row to include (e.g., `ROWS BETWEEN 3 PRECEDING AND CURRENT ROW`)

Some functions (`first_value`, `last_value`, `lag`, `lead`) also support `IGNORE NULLS` or `RESPECT NULLS` before the `OVER` keyword to control null handling.

For complete syntax details including frame specifications and exclusion options, see [OVER Clause Syntax](/docs/query/functions/window-functions/syntax/).

Window function arithmetic (9.3.1+)

Arithmetic operations on window functions (e.g., `sum(...) OVER (...) / sum(...) OVER (...)`) are supported from version 9.3.1. Earlier versions require wrapping window functions in CTEs or subqueries.

## Quick reference[​](#quick-reference "Direct link to Quick reference")

| Function | Description | Respects Frame |
| --- | --- | --- |
| [`avg()`](/docs/query/functions/window-functions/reference/#avg) | Average value in window (also supports EMA and VWEMA) | Yes (standard) / No (EMA/VWEMA) |
| [`count()`](/docs/query/functions/window-functions/reference/#count) | Count rows or non-null values | Yes |
| [`sum()`](/docs/query/functions/window-functions/reference/#sum) | Sum of values in window | Yes |
| [`ksum()`](/docs/query/functions/window-functions/reference/#ksum) | Sum with Kahan precision | Yes |
| [`min()`](/docs/query/functions/window-functions/reference/#min) | Minimum value in window | Yes |
| [`max()`](/docs/query/functions/window-functions/reference/#max) | Maximum value in window | Yes |
| [`first_value()`](/docs/query/functions/window-functions/reference/#first_value) | First value in window | Yes |
| [`last_value()`](/docs/query/functions/window-functions/reference/#last_value) | Last value in window | Yes |
| [`row_number()`](/docs/query/functions/window-functions/reference/#row_number) | Sequential row number | No |
| [`rank()`](/docs/query/functions/window-functions/reference/#rank) | Rank with gaps for ties | No |
| [`dense_rank()`](/docs/query/functions/window-functions/reference/#dense_rank) | Rank without gaps | No |
| [`lag()`](/docs/query/functions/window-functions/reference/#lag) | Value from previous row | No |
| [`lead()`](/docs/query/functions/window-functions/reference/#lead) | Value from following row | No |

**Respects Frame**: Functions marked "Yes" use the frame clause (`ROWS`/`RANGE BETWEEN`). Functions marked "No" operate on the entire partition regardless of frame specification.

## When to use window functions[​](#when-to-use-window-functions "Direct link to When to use window functions")

Window functions are essential for analytics tasks where you need to:

* Calculate **running totals** or **cumulative sums**
* Compute **moving averages** over time periods
* Find the **maximum or minimum** value within a sequence
* **Rank** items within categories
* Access **previous or next row** values without self-joins
* Compare each row to an **aggregate** of related rows

### Example: Moving average[​](#example-moving-average "Direct link to Example: Moving average")

4-row moving average of price[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20timestamp%2C%0A%20%20%20%20avg(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20ROWS%20BETWEEN%203%20PRECEDING%20AND%20CURRENT%20ROW%0A%20%20%20%20)%20AS%20moving_avg%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%0ALIMIT%20100%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    timestamp,  
    avg(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW  
    ) AS moving_avg  
FROM trades  
WHERE timestamp IN today()  
LIMIT 100;
```

This calculates a moving average over the current row plus three preceding rows, grouped by symbol.

## How window functions work[​](#how-window-functions-work "Direct link to How window functions work")

A window function has three key components:

```prism-code
function_name(arguments) OVER (  
    [PARTITION BY column]      -- Divide into groups  
    [ORDER BY column]          -- Order within groups  
    [frame_specification]      -- Define which rows to include  
)
```

### 1. Partitioning[​](#1-partitioning "Direct link to 1. Partitioning")

`PARTITION BY` divides rows into independent groups. The window function **resets** for each partition—calculations start fresh, as if each group were a separate table.

**When to use it:** When storing multiple instruments in the same table, you typically want calculations isolated per symbol. For example:

* Cumulative volume **per symbol** (not across all instruments)
* Moving average price **per symbol** (not mixing BTC-USD with ETH-USD)
* Intraday high/low **per symbol**

```prism-code
-- Without PARTITION BY: cumulative volume across ALL symbols (mixing instruments)  
sum(volume) OVER (ORDER BY timestamp)  
  
-- With PARTITION BY: cumulative volume resets for each symbol  
sum(volume) OVER (PARTITION BY symbol ORDER BY timestamp)
```

| timestamp | symbol | volume | cumulative (no partition) | cumulative (by symbol) |
| --- | --- | --- | --- | --- |
| 09:00 | BTC-USD | 100 | 100 | 100 |
| 09:01 | ETH-USD | 200 | 300 | 200 |
| 09:02 | BTC-USD | 150 | 450 | 250 |
| 09:03 | ETH-USD | 100 | 550 | 300 |

Without `PARTITION BY`, all rows are treated as a single partition.

### 2. Ordering[​](#2-ordering "Direct link to 2. Ordering")

`ORDER BY` within the `OVER` clause determines the logical order for calculations:

```prism-code
-- Row numbers ordered by timestamp  
row_number() OVER (ORDER BY timestamp)
```

This is independent of the query-level `ORDER BY`.

Time-series optimization

For tables with a designated timestamp, data is already ordered by time. When your window `ORDER BY` matches the designated timestamp, QuestDB skips redundant sorting—no performance penalty.

### 3. Frame specification[​](#3-frame-specification "Direct link to 3. Frame specification")

The frame defines which rows relative to the current row are included in the calculation:

```prism-code
-- Sum of current row plus 2 preceding rows  
sum(price) OVER (  
    ORDER BY timestamp  
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW  
)
```

For complete frame syntax details, see [OVER Clause Syntax](/docs/query/functions/window-functions/syntax/#frame-types-and-behavior).

## Aggregate vs window functions[​](#aggregate-vs-window-functions "Direct link to Aggregate vs window functions")

The key difference: aggregate functions collapse rows into one result, while window functions keep all rows and add a computed column.

**Source data:**

| timestamp | symbol | price |
| --- | --- | --- |
| 09:00 | BTC-USD | 100 |
| 09:01 | BTC-USD | 102 |
| 09:02 | BTC-USD | 101 |

**Aggregate function** — returns one row:

```prism-code
SELECT symbol, avg(price) AS avg_price  
FROM trades  
GROUP BY symbol;
```

| symbol | avg\_price |
| --- | --- |
| BTC-USD | 101 |

**Window function** — returns all rows with computed column:

```prism-code
SELECT timestamp, symbol, price,  
       avg(price) OVER (PARTITION BY symbol) AS avg_price  
FROM trades;
```

| timestamp | symbol | price | avg\_price |
| --- | --- | --- | --- |
| 09:00 | BTC-USD | 100 | 101 |
| 09:01 | BTC-USD | 102 | 101 |
| 09:02 | BTC-USD | 101 | 101 |

Each row keeps its original data **plus** the average—useful for comparing each price to the mean, calculating deviations, or adding running totals alongside the raw values.

## ROWS vs RANGE frames[​](#rows-vs-range-frames "Direct link to ROWS vs RANGE frames")

QuestDB supports two frame types:

### ROWS frame[​](#rows-frame "Direct link to ROWS frame")

Based on physical row count:

```prism-code
ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
```

Includes exactly 4 rows: current row plus 3 before it.

### RANGE frame[​](#range-frame "Direct link to RANGE frame")

Based on values in the `ORDER BY` column (must be a timestamp):

```prism-code
RANGE BETWEEN '1' MINUTE PRECEDING AND CURRENT ROW
```

Includes all rows within 1 minute of the current row's timestamp.

note

RANGE frames have a known limitation: rows with the same ORDER BY value ("peers") do not produce identical results as required by the SQL standard. QuestDB currently processes peers as distinct rows rather than treating them as a group. See [GitHub issue #5177](https://github.com/questdb/questdb/issues/5177) for details.

For complete frame syntax, see [OVER Clause Syntax](/docs/query/functions/window-functions/syntax/).

## Common patterns[​](#common-patterns "Direct link to Common patterns")

### Running total[​](#running-total "Direct link to Running total")

Use the `CUMULATIVE` shorthand for running totals:

Cumulative sum[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20amount%2C%0A%20%20%20%20sum(amount)%20OVER%20(%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20%20%20%20%20CUMULATIVE%0A%20%20%20%20)%20AS%20running_total%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp,  
    amount,  
    sum(amount) OVER (  
        ORDER BY timestamp  
        CUMULATIVE  
    ) AS running_total  
FROM trades  
WHERE timestamp IN today();
```

This is equivalent to `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

### VWAP (Volume-Weighted Average Price)[​](#vwap-volume-weighted-average-price "Direct link to VWAP (Volume-Weighted Average Price)")

For high-frequency market data, VWAP is typically calculated over OHLC time series using the typical price `(high + low + close) / 3`:

VWAP over OHLC data[Demo this query](https://demo.questdb.io/?query=DECLARE%20%40symbol%20%3A%3D%20'BTC-USD'%0A%0AWITH%20ohlc%20AS%20(%0A%20%20%20%20SELECT%0A%20%20%20%20%20%20%20%20timestamp%20AS%20ts%2C%0A%20%20%20%20%20%20%20%20symbol%2C%0A%20%20%20%20%20%20%20%20first(price)%20AS%20open%2C%0A%20%20%20%20%20%20%20%20max(price)%20AS%20high%2C%0A%20%20%20%20%20%20%20%20min(price)%20AS%20low%2C%0A%20%20%20%20%20%20%20%20last(price)%20AS%20close%2C%0A%20%20%20%20%20%20%20%20sum(amount)%20AS%20volume%0A%20%20%20%20FROM%20trades%0A%20%20%20%20WHERE%20timestamp%20IN%20'2024-05-22'%20AND%20symbol%20%3D%20%40symbol%0A%20%20%20%20SAMPLE%20BY%201m%20ALIGN%20TO%20CALENDAR%0A)%0ASELECT%0A%20%20%20%20ts%2C%0A%20%20%20%20symbol%2C%0A%20%20%20%20open%2C%20high%2C%20low%2C%20close%2C%20volume%2C%0A%20%20%20%20sum((high%20%2B%20low%20%2B%20close)%20%2F%203%20*%20volume)%20OVER%20(ORDER%20BY%20ts%20CUMULATIVE)%0A%20%20%20%20%20%20%20%20%2F%20sum(volume)%20OVER%20(ORDER%20BY%20ts%20CUMULATIVE)%20AS%20vwap%0AFROM%20ohlc%0AORDER%20BY%20ts%3B&executeQuery=true)

```prism-code
DECLARE @symbol := 'BTC-USD'  
  
WITH ohlc AS (  
    SELECT  
        timestamp AS ts,  
        symbol,  
        first(price) AS open,  
        max(price) AS high,  
        min(price) AS low,  
        last(price) AS close,  
        sum(amount) AS volume  
    FROM trades  
    WHERE timestamp IN '2024-05-22' AND symbol = @symbol  
    SAMPLE BY 1m ALIGN TO CALENDAR  
)  
SELECT  
    ts,  
    symbol,  
    open, high, low, close, volume,  
    sum((high + low + close) / 3 * volume) OVER (ORDER BY ts CUMULATIVE)  
        / sum(volume) OVER (ORDER BY ts CUMULATIVE) AS vwap  
FROM ohlc  
ORDER BY ts;
```

### Compare to group average[​](#compare-to-group-average "Direct link to Compare to group average")

Price vs symbol average[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20avg(price)%20OVER%20(PARTITION%20BY%20symbol)%20AS%20symbol_avg%2C%0A%20%20%20%20price%20-%20avg(price)%20OVER%20(PARTITION%20BY%20symbol)%20AS%20diff_from_avg%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price) OVER (PARTITION BY symbol) AS symbol_avg,  
    price - avg(price) OVER (PARTITION BY symbol) AS diff_from_avg  
FROM trades  
WHERE timestamp IN today();
```

### Rank within category[​](#rank-within-category "Direct link to Rank within category")

Rank prices per symbol[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20rank()%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20price%20DESC%0A%20%20%20%20)%20AS%20price_rank%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    rank() OVER (  
        PARTITION BY symbol  
        ORDER BY price DESC  
    ) AS price_rank  
FROM trades  
WHERE timestamp IN today();
```

### Access previous row[​](#access-previous-row "Direct link to Access previous row")

Calculate price change[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20timestamp%2C%0A%20%20%20%20price%2C%0A%20%20%20%20lag(price)%20OVER%20(ORDER%20BY%20timestamp)%20AS%20prev_price%2C%0A%20%20%20%20price%20-%20lag(price)%20OVER%20(ORDER%20BY%20timestamp)%20AS%20price_change%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%0A%20%20%20%20AND%20symbol%20%3D%20'BTC-USD'%3B&executeQuery=true)

```prism-code
SELECT  
    timestamp,  
    price,  
    lag(price) OVER (ORDER BY timestamp) AS prev_price,  
    price - lag(price) OVER (ORDER BY timestamp) AS price_change  
FROM trades  
WHERE timestamp IN today()  
    AND symbol = 'BTC-USD';
```

## Next steps[​](#next-steps "Direct link to Next steps")

* **[Function Reference](/docs/query/functions/window-functions/reference/)**: Detailed documentation for each window function
* **[OVER Clause Syntax](/docs/query/functions/window-functions/syntax/)**: Complete syntax for partitioning, ordering, and frame specifications

Looking for WINDOW JOIN?

[WINDOW JOIN](/docs/query/sql/window-join/) is a separate feature for aggregating data from a *different table* within a time window. Use window functions (this page) for calculations within a single table; use WINDOW JOIN to correlate two time-series tables.

## Common mistakes[​](#common-mistakes "Direct link to Common mistakes")

### Using window functions in WHERE[​](#using-window-functions-in-where "Direct link to Using window functions in WHERE")

Window functions cannot be used directly in `WHERE` clauses:

Incorrect - will not work

```prism-code
SELECT symbol, price  
FROM trades  
WHERE avg(price) OVER (ORDER BY timestamp) > 100;
```

Use a CTE or subquery instead:

Correct approach[Demo this query](https://demo.questdb.io/?query=WITH%20prices%20AS%20(%0A%20%20%20%20SELECT%0A%20%20%20%20%20%20%20%20symbol%2C%0A%20%20%20%20%20%20%20%20price%2C%0A%20%20%20%20%20%20%20%20avg(price)%20OVER%20(ORDER%20BY%20timestamp)%20AS%20moving_avg%0A%20%20%20%20FROM%20trades%0A%20%20%20%20WHERE%20timestamp%20IN%20today()%0A)%0ASELECT%20*%20FROM%20prices%0AWHERE%20moving_avg%20%3E%20100%3B&executeQuery=true)

```prism-code
WITH prices AS (  
    SELECT  
        symbol,  
        price,  
        avg(price) OVER (ORDER BY timestamp) AS moving_avg  
    FROM trades  
    WHERE timestamp IN today()  
)  
SELECT * FROM prices  
WHERE moving_avg > 100;
```

### Missing ORDER BY[​](#missing-order-by "Direct link to Missing ORDER BY")

Without `ORDER BY`, the window includes all rows in the partition, which may not be the intended behavior:

All rows show same average

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price) OVER (PARTITION BY symbol) AS avg_price  -- Same value for all rows in partition  
FROM trades;
```

Add `ORDER BY` for cumulative/moving calculations:

Running average[Demo this query](https://demo.questdb.io/?query=SELECT%0A%20%20%20%20symbol%2C%0A%20%20%20%20price%2C%0A%20%20%20%20avg(price)%20OVER%20(%0A%20%20%20%20%20%20%20%20PARTITION%20BY%20symbol%0A%20%20%20%20%20%20%20%20ORDER%20BY%20timestamp%0A%20%20%20%20)%20AS%20running_avg%0AFROM%20trades%0AWHERE%20timestamp%20IN%20today()%3B&executeQuery=true)

```prism-code
SELECT  
    symbol,  
    price,  
    avg(price) OVER (  
        PARTITION BY symbol  
        ORDER BY timestamp  
    ) AS running_avg  
FROM trades  
WHERE timestamp IN today();
```