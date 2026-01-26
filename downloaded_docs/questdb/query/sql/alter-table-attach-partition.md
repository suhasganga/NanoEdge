On this page

Restores one or more partitions to the table where they have been detached from
by using the SQL
[ALTER TABLE DETACH PARTITION](/docs/query/sql/alter-table-detach-partition/)
statement.

This feature is part of the manual S3/cold storage solution, allowing restoring
data manually.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of ALTER TABLE with ATTACH PARTITION keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NjUiIGhlaWdodD0iODEiPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgNjEgMSA1NyAxIDY1Ij48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgNjEgOSA1NyA5IDY1Ij48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSI0NyIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjkiIHk9IjQ1IiB3aWR0aD0iNjIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzkiIHk9IjY1Ij5BTFRFUjwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTEzIiB5PSI0NyIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTExIiB5PSI0NSIgd2lkdGg9IjYyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjEyMSIgeT0iNjUiPlRBQkxFPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjdGFibGVOYW1lIiB4bGluazp0aXRsZT0idGFibGVOYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iMTk1IiB5PSI0NyIgd2lkdGg9Ijg4IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjE5MyIgeT0iNDUiIHdpZHRoPSI4OCIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iMjAzIiB5PSI2NSI+dGFibGVOYW1lPC90ZXh0PjwvYT48cmVjdCB4PSIzMDMiIHk9IjQ3IiB3aWR0aD0iNzQiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzMDEiIHk9IjQ1IiB3aWR0aD0iNzQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzExIiB5PSI2NSI+QVRUQUNIPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIzOTciIHk9IjQ3IiB3aWR0aD0iOTgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIzOTUiIHk9IjQ1IiB3aWR0aD0iOTgiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNDA1IiB5PSI2NSI+UEFSVElUSU9OPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSI1MTUiIHk9IjQ3IiB3aWR0aD0iNTIiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI1MTMiIHk9IjQ1IiB3aWR0aD0iNTIiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iNTIzIiB5PSI2NSI+TElTVDwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3BhcnRpdGlvbk5hbWUiIHhsaW5rOnRpdGxlPSJwYXJ0aXRpb25OYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iNjA3IiB5PSI0NyIgd2lkdGg9IjExMCIgaGVpZ2h0PSIzMiI+PC9yZWN0PgogICAgICAgICAgICA8cmVjdCB4PSI2MDUiIHk9IjQ1IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSI2MTUiIHk9IjY1Ij5wYXJ0aXRpb25OYW1lPC90ZXh0PjwvYT48cmVjdCB4PSI2MDciIHk9IjMiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjYwNSIgeT0iMSIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjYxNSIgeT0iMjEiPiw8L3RleHQ+CiAgICAgICAgIDxwYXRoIGNsYXNzPSJsaW5lIiBkPSJtMTcgNjEgaDIgbTAgMCBoMTAgbTYyIDAgaDEwIG0wIDAgaDEwIG02MiAwIGgxMCBtMCAwIGgxMCBtODggMCBoMTAgbTAgMCBoMTAgbTc0IDAgaDEwIG0wIDAgaDEwIG05OCAwIGgxMCBtMCAwIGgxMCBtNTIgMCBoMTAgbTIwIDAgaDEwIG0xMTAgMCBoMTAgbS0xNTAgMCBsMjAgMCBtLTEgMCBxLTkgMCAtOSAtMTAgbDAgLTI0IHEwIC0xMCAxMCAtMTAgbTEzMCA0NCBsMjAgMCBtLTIwIDAgcTEwIDAgMTAgLTEwIGwwIC0yNCBxMCAtMTAgLTEwIC0xMCBtLTEzMCAwIGgxMCBtMjQgMCBoMTAgbTAgMCBoODYgbTIzIDQ0IGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9Ijc1NSA2MSA3NjMgNTcgNzYzIDY1Ij48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iNzU1IDYxIDc0NyA1NyA3NDcgNjUiPjwvcG9seWdvbj4KPC9zdmc+)

The `WHERE` clause is not supported when attaching partitions.

## Description[​](#description "Direct link to Description")

Before executing `ATTACH PARTITION`, the partition folders to be attached must
be made available to QuestDB using one of the following methods:

* Copying the partition folders manually
* Using a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link)

This section describes the details of each method.

### Manual copy[​](#manual-copy "Direct link to Manual copy")

Partition folders can be manually moved from where they are stored into the
table folder in `db`. To make the partitions available for the attach operation,
the files need to be renamed `<partition_name>.attachable`.

For example, in a table partitioned by year, given a partition folder named
`2020.detached`, rename it as `2020.attachable`, and move it to the table
folder.

### Symbolic links[​](#symbolic-links "Direct link to Symbolic links")

[Symbolic links](https://en.wikipedia.org/wiki/Symbolic_link) can be used to
attach partition folders that exist potentially in a different volume as cold
storage. The partitions attached in this way will be **read-only**. To make
detached partition folders in cold storage available for attaching, for each
partition folder, create a symbolic link with the name
format`<partition_name>.attachable` from the table's folder, and set the target
path to the detached partition folder.

In Windows, symbolic links require admin privileges, and thus this method is not
recommended.

note

SQL statements that hit partitions attached via symbolic links may have slower
runtime if their volumes have a slower disk.

#### Properties using symbolic links[​](#properties-using-symbolic-links "Direct link to Properties using symbolic links")

Partitions attached via the symbolic link approach are **read-only** for the
following operations:

* [`DETACH PARTITION`](/docs/query/sql/alter-table-detach-partition/) and
  [`DROP PARTITION`](/docs/query/sql/alter-table-drop-partition/): Once the
  partition folders are unlinked, the symbolic links are removed, but the
  content remains. Detaching a partition that was attached via symbolic link
  does not create a copy `<partition_name>.detached`.
* [`UPDATE`](/docs/query/sql/update/): Attempts to update the read-only
  partitions result in an error.
* [`INSERT`](/docs/query/sql/insert/): Attemps to insert data into a
  read-only partition result in a critical-level log message being logged by the
  server, and the insertion is a no-op. If
  [Prometheus monitoring](/docs/integrations/other/prometheus/) is configured, an
  alert will be triggered.

For read-only partitions, the following operations are supported:

* [`ADD COLUMN`](/docs/query/sql/alter-table-add-column/)
* [`DROP COLUMN`](/docs/query/sql/alter-table-drop-column/)
* [`RENAME COLUMN`](/docs/query/sql/alter-table-rename-column/)
* [`ADD INDEX`](/docs/query/sql/alter-table-alter-column-add-index/)
* [`DROP INDEX`](/docs/query/sql/alter-table-alter-column-drop-index/)

## Example[​](#example "Direct link to Example")

### Manual copy[​](#manual-copy-1 "Direct link to Manual copy")

Assuming the QuestDB data directory is `/var/lib/questdb/db`, for a table `x`
with AWS S3 for cold storage:

1. Copy files from S3:

   ```prism-code
   cd /var/lib/questdb/db/x  
   # Table x is the original table where the partition were detached from.  
     
   mkdir 2019-02-01.attachable && aws s3 cp s3://questdb-internal/blobs/20190201.tar.gz - | tar xvfz - -C 2019-02-01.attachable --strip-components 1  
   mkdir 2019-02-02.attachable && aws s3 cp s3://questdb-internal/blobs/20190202.tar.gz - | tar xvfz - -C 2019-02-01.attachable --strip-components 1
   ```
2. Execute the SQL `ALTER TABLE ATTACH PARTITION` command:

   ```prism-code
   ALTER TABLE x ATTACH PARTITION LIST '2019-02-01', '2019-02-02';
   ```
3. After the SQL is executed, the partitions will be available to read.

### Symbolic link[​](#symbolic-link "Direct link to Symbolic link")

The following example creates a table `tab` with some data, detaches all but the
last partition, and demonstrates how to attach the partitions using symbolic
links.

These SQL statements create table `tab` partitioned by year, and insert seven
rows that result in a total of seven partitions:

```prism-code
CREATE TABLE tab (name STRING, age INT, dob TIMESTAMP) TIMESTAMP(dob) PARTITION BY YEAR;  
  
INSERT INTO tab VALUES('B', 1, '2022-11-08T12:00:00.000000Z');  
INSERT INTO tab VALUES('C', 2, '2023-11-08T12:00:00.000000Z');  
INSERT INTO tab VALUES('D', 3, '2024-11-08T12:00:00.000000Z');  
INSERT INTO tab VALUES('E', 4, '2025-11-08T12:00:00.000000Z');  
INSERT INTO tab VALUES('F', 5, '2026-11-08T12:00:00.000000Z');  
INSERT INTO tab VALUES('A', 0, '2027-11-08T12:00:00.000000Z');  
INSERT INTO tab VALUES('0', 0, '2028-11-08T12:00:00.000000Z');
```

This SQL statement detaches partitions 2022, 2023, 2024, 2025, 2026, and 2027:

```prism-code
ALTER TABLE tab DETACH PARTITION WHERE dob < '2028';
```

Assuming QuestDB's root directory to be `/opt/homebrew/var/questdb/db`, the
content of the table folder is:

```prism-code
2022.detached  
2023.detached  
2024.detached  
2025.detached  
2026.detached  
2027.detached  
2028.5  
_cv  
_meta  
_todo_  
_txn  
_txn_scoreboard  
seq
```

You can now move those `<partition_name.detached>` folders to a different path,
potentially a different volume:

```prism-code
mv /opt/homebrew/var/questdb/db/tab/*.detached /cold_storage/tab
```

When you want to attach these partitions back, create a symlink for every
partition to be attached from the table folder
`/opt/homebrew/var/questdb/db/tab`:

```prism-code
ln -s /cold_storage/tab/2022.detached 2022.attachable  
ln -s /cold_storage/tab/2023.detached 2023.attachable  
ln -s /cold_storage/tab/2024.detached 2024.attachable  
ln -s /cold_storage/tab/2025.detached 2025.attachable  
ln -s /cold_storage/tab/2026.detached 2026.attachable  
ln -s /cold_storage/tab/2027.detached 2027.attachable
```

The content of the table folder should look like this now:

```prism-code
2022.attachable -> /cold_storage/tab/2022.detached  
2023.attachable -> /cold_storage/tab/2023.detached  
2024.attachable -> /cold_storage/tab/2024.detached  
2025.attachable -> /cold_storage/tab/2025.detached  
2026.attachable -> /cold_storage/tab/2026.detached  
2027.attachable -> /cold_storage/tab/2027.detached  
2028.5  
_cv  
_meta  
_todo_  
_txn  
_txn_scoreboard  
seq
```

After the symbolic links have been created, the partitions can be attached with
the following SQL statement:

```prism-code
ALTER TABLE tab ATTACH PARTITION LIST '2022', '2023', '2024', '2025', '2026', '2027';
```

The SQL reference to the partitions does not include the suffix `.attachable`.

## Limitation[​](#limitation "Direct link to Limitation")

* S3/Cold storage interaction is manual. Partitions can only be attached to the
  same table they were detached from. The table name must be the same. Moving
  partitions between tables or database instances is not supported.
* The operation will fail if a partition already exists. We are working on
  functionality to allow merging data in the same partition for attaching.