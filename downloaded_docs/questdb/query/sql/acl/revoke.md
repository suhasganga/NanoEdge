On this page

`REVOKE` - revoke permission from user, group or service account.

For full documentation of the Access Control List and Role-based Access Control,
see the [RBAC operations](/docs/security/rbac/) page.

note

Role-based Access Control (RBAC) operations are only available in QuestDB
Enterprise.

---

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the REVOKE keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5NzkiIGhlaWdodD0iMjYxIj4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSIxMSA2MSAzIDU3IDMgNjUiPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSIxOSA2MSAxMSA1NyAxMSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMyIgeT0iNDciIHdpZHRoPSI3NCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSI0NSIgd2lkdGg9Ijc0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjQxIiB5PSI2NSI+UkVWT0tFPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjcGVybWlzc2lvbiIgeGxpbms6dGl0bGU9InBlcm1pc3Npb24iPgogICAgICAgICAgICA8cmVjdCB4PSIxNDciIHk9IjQ3IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMTQ1IiB5PSI0NSIgd2lkdGg9Ijg4IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIxNTUiIHk9IjY1Ij5wZXJtaXNzaW9uPC90ZXh0PjwvYT48cmVjdCB4PSIxNDciIHk9IjMiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjE0NSIgeT0iMSIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE1NSIgeT0iMjEiPiw8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjQ1IiB5PSIxNzkiIHdpZHRoPSI0MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQzIiB5PSIxNzciIHdpZHRoPSI0MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI1MyIgeT0iMTk3Ij5PTjwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3RhYmxlTmFtZSIgeGxpbms6dGl0bGU9InRhYmxlTmFtZSI+CiAgICAgICAgICAgIDxyZWN0IHg9IjEyNSIgeT0iMTc5IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMTIzIiB5PSIxNzciIHdpZHRoPSI4OCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMTMzIiB5PSIxOTciPnRhYmxlTmFtZTwvdGV4dD48L2E+PHJlY3QgeD0iMjUzIiB5PSIxNzkiIHdpZHRoPSIyNiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI1MSIgeT0iMTc3IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMjYxIiB5PSIxOTciPig8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjI5OSIgeT0iMTc5IiB3aWR0aD0iMTA4IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjk3IiB5PSIxNzciIHdpZHRoPSIxMDgiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzA3IiB5PSIxOTciPmNvbHVtbk5hbWU8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjQ2NyIgeT0iMTc5IiB3aWR0aD0iMjQiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI0NjUiIHk9IjE3NyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjQ3NSIgeT0iMTk3Ij4sPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjY29sdW1uTmFtZSIgeGxpbms6dGl0bGU9ImNvbHVtbk5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSI1MTEiIHk9IjE3OSIgd2lkdGg9IjEwMiIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI1MDkiIHk9IjE3NyIgd2lkdGg9IjEwMiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNTE5IiB5PSIxOTciPmNvbHVtbk5hbWU8L3RleHQ+PC9hPjxyZWN0IHg9IjY3MyIgeT0iMTc5IiB3aWR0aD0iMjYiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI2NzEiIHk9IjE3NyIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjY4MSIgeT0iMTk3Ij4pPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxMjUiIHk9IjExMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTIzIiB5PSIxMTEiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSIxMzMiIHk9IjEzMSI+LDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNzc5IiB5PSIxNzkiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9Ijc3NyIgeT0iMTc3IiB3aWR0aD0iNjAiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNzg3IiB5PSIxOTciPkZST008L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNlbnRpdHlOYW1lIiB4bGluazp0aXRsZT0iZW50aXR5TmFtZSI+CiAgICAgICAgICAgIDxyZWN0IHg9Ijg1OSIgeT0iMTc5IiB3aWR0aD0iOTIiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iODU3IiB5PSIxNzciIHdpZHRoPSI5MiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iODY3IiB5PSIxOTciPmVudGl0eU5hbWU8L3RleHQ+PC9hPjxwYXRoIGNsYXNzPSJsaW5lIiBkPSJtMTkgNjEgaDIgbTAgMCBoMTAgbTc0IDAgaDEwIG0yMCAwIGgxMCBtODggMCBoMTAgbS0xMjggMCBsMjAgMCBtLTEgMCBxLTkgMCAtOSAtMTAgbDAgLTI0IHEwIC0xMCAxMCAtMTAgbTEwOCA0NCBsMjAgMCBtLTIwIDAgcTEwIDAgMTAgLTEwIGwwIC0yNCBxMCAtMTAgLTEwIC0xMCBtLTEwOCAwIGgxMCBtMjQgMCBoMTAgbTAgMCBoNjQgbTIyIDQ0IGwyIDAgbTIgMCBsMiAwIG0yIDAgbDIgMCBtLTI3NCAxMzIgbDIgMCBtMiAwIGwyIDAgbTIgMCBsMiAwIG0yMiAwIGgxMCBtNDAgMCBoMTAgbTIwIDAgaDEwIG04OCAwIGgxMCBtMjAgMCBoMTAgbTI2IDAgaDEwIG0wIDAgaDEwIG0xMDggMCBoMTAgbTQwIDAgaDEwIG0yNCAwIGgxMCBtMCAwIGgxMCBtMTAyIDAgaDEwIG0tMTg2IDAgbDIwIDAgbS0xIDAgcS05IDAgLTkgLTEwIGwwIC0xMiBxMCAtMTAgMTAgLTEwIG0xNjYgMzIgbDIwIDAgbS0yMCAwIHExMCAwIDEwIC0xMCBsMCAtMTIgcTAgLTEwIC0xMCAtMTAgbS0xNjYgMCBoMTAgbTAgMCBoMTU2IG0tMjA2IDMyIGgyMCBtMjA2IDAgaDIwIG0tMjQ2IDAgcTEwIDAgMTAgMTAgbTIyNiAwIHEwIC0xMCAxMCAtMTAgbS0yMzYgMTAgdjE0IG0yMjYgMCB2LTE0IG0tMjI2IDE0IHEwIDEwIDEwIDEwIG0yMDYgMCBxMTAgMCAxMCAtMTAgbS0yMTYgMTAgaDEwIG0wIDAgaDE5NiBtMjAgLTM0IGgxMCBtMjYgMCBoMTAgbS00ODYgMCBoMjAgbTQ2NiAwIGgyMCBtLTUwNiAwIHExMCAwIDEwIDEwIG00ODYgMCBxMCAtMTAgMTAgLTEwIG0tNDk2IDEwIHYzMCBtNDg2IDAgdi0zMCBtLTQ4NiAzMCBxMCAxMCAxMCAxMCBtNDY2IDAgcTEwIDAgMTAgLTEwIG0tNDc2IDEwIGgxMCBtMCAwIGg0NTYgbS02MTQgLTUwIGwyMCAwIG0tMSAwIHEtOSAwIC05IC0xMCBsMCAtNDYgcTAgLTEwIDEwIC0xMCBtNjE0IDY2IGwyMCAwIG0tMjAgMCBxMTAgMCAxMCAtMTAgbDAgLTQ2IHEwIC0xMCAtMTAgLTEwIG0tNjE0IDAgaDEwIG0yNCAwIGgxMCBtMCAwIGg1NzAgbS03MTQgNjYgaDIwIG03MTQgMCBoMjAgbS03NTQgMCBxMTAgMCAxMCAxMCBtNzM0IDAgcTAgLTEwIDEwIC0xMCBtLTc0NCAxMCB2NDYgbTczNCAwIHYtNDYgbS03MzQgNDYgcTAgMTAgMTAgMTAgbTcxNCAwIHExMCAwIDEwIC0xMCBtLTcyNCAxMCBoMTAgbTAgMCBoNzA0IG0yMCAtNjYgaDEwIG02MCAwIGgxMCBtMCAwIGgxMCBtOTIgMCBoMTAgbTMgMCBoLTMiPjwvcGF0aD4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI5NjkgMTkzIDk3NyAxODkgOTc3IDE5NyI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9Ijk2OSAxOTMgOTYxIDE4OSA5NjEgMTk3Ij48L3BvbHlnb24+Cjwvc3ZnPg==)

## Description[​](#description "Direct link to Description")

* `REVOKE [permissions] FROM entity` - revoke database level permissions from an
  entity
* `REVOKE [permissions] ON ALL TABLES FROM entity` - revoke table/column level
  permissions on database level from an entity
* `REVOKE [permissions] ON [table] FROM entity` - revoke table/column level
  permissions on table level from an entity
* `REVOKE [permissions] ON [table(columns)] FROM entity` - revoke column level
  permissions on column level from an entity

### Revoke database level permissions[​](#revoke-database-level-permissions "Direct link to Revoke database level permissions")

```prism-code
REVOKE CREATE TABLE FROM john;
```

### Revoke table level permissions for entire database[​](#revoke-table-level-permissions-for-entire-database "Direct link to Revoke table level permissions for entire database")

```prism-code
REVOKE ADD INDEX, REINDEX ON ALL TABLES FROM john;
```

### Revoke table level permissions on specific tables[​](#revoke-table-level-permissions-on-specific-tables "Direct link to Revoke table level permissions on specific tables")

```prism-code
REVOKE ADD INDEX, REINDEX ON orders FROM john;
```

### Revoke column level permissions for entire database[​](#revoke-column-level-permissions-for-entire-database "Direct link to Revoke column level permissions for entire database")

```prism-code
REVOKE SELECT ON ALL TABLES FROM john;
```

### Revoke column level permissions on specific tables[​](#revoke-column-level-permissions-on-specific-tables "Direct link to Revoke column level permissions on specific tables")

```prism-code
REVOKE SELECT ON orders, trades FROM john;
```

### Revoke column level permissions on specific columns[​](#revoke-column-level-permissions-on-specific-columns "Direct link to Revoke column level permissions on specific columns")

```prism-code
REVOKE SELECT ON orders(id, name) FROM john;
```

### Implicit permissions[​](#implicit-permissions "Direct link to Implicit permissions")

If the target table has implicit timestamp permissions, then revoking `SELECT`
or `UPDATE` permission on all other table columns also revokes it on the
designated timestamp column:

```prism-code
CREATE TABLE products(id INT, name STRING, ts TIMESTAMP) TIMESTAMP(ts);  
GRANT SELECT ON products(id) TO john;  
GRANT SELECT, UPDATE ON products(name) TO john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| UPDATE | products | name | f | G |
| UPDATE | products | ts | f | I |
| SELECT | products | id | f | G |
| SELECT | products | name | f | G |
| SELECT | products | ts | f | I |

Revoking a permission from all columns revokes the implicitly granted permission
from the designated timestamp column:

```prism-code
REVOKE UPDATE ON products(name) FROM john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | products | id | f | G |
| SELECT | products | name | f | G |
| SELECT | products | ts | f | I |

However, if there is even a single column which still has the permission, then
the implicit permission is kept:

```prism-code
REVOKE SELECT ON products(id) FROM john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | products | name | f | G |
| SELECT | products | ts | f | I |

### Permission level readjustment[​](#permission-level-readjustment "Direct link to Permission level readjustment")

If the user has a database- or table-level permission, then revoking it on a
lower level triggers
[permission level re-adjustment](/docs/security/rbac/#permission-level-re-adjustment).
Permission is switched to lower level and `materialized`:

* database level permission is pushed to table level, so e.g. SELECT will not
  apply to any new tables
* table level permission is pushed to column level, so e.g. SELECT will not
  apply to any new table columns

For example, assume we have the following tables: `orders`, `trades` and
`products`, and revoking a permission from a table which was granted on database
level previously.

```prism-code
GRANT SELECT ON ALL TABLES TO john;  
REVOKE SELECT ON trades FROM john;
```

Database level permission is replaced with table level on all existing tables,
except the one being revoked.

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | orders |  | f | G |
| SELECT | products |  | f | G |

As a consequence permission, which was granted for all tables previously, will
not apply to any newly-created tables:

```prism-code
CREATE TABLE new_tab( id INT );
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | orders |  | f | G |
| SELECT | products |  | f | G |

Permission level re-adjustment can also happen from the table level to the
column level. For example, the following column level revoke replaces the table
level permission on the products table with column level permissions:

```prism-code
REVOKE SELECT on products(id) FROM john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | orders |  | f | G |
| SELECT | products | name | f | G |

### Revoke permissions inherited from group[​](#revoke-permissions-inherited-from-group "Direct link to Revoke permissions inherited from group")

Permissions of groups are applied after user permissions, thus it is not
possible to revoke them directly from the user.

```prism-code
CREATE group admins;  
GRANT SELECT on products to admins;  
ADD USER john to admins;  
REVOKE SELECT on products from john;
```

| permission | table\_name | column\_name | grant\_option | origin |
| --- | --- | --- | --- | --- |
| SELECT | products |  | f | G |

To do so, either:

* the user has to be removed from the group where the permission is inherited
  from
* or the permission has to be revoked from the group

```prism-code
REVOKE SELECT on products FROM admins;  
-- or  
REMOVE USER john FROM admins;
```