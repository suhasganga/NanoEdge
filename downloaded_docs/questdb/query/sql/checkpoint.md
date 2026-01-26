On this page

Checkpoint SQL toggles the database into and out of "checkpoint mode". In this
mode the databases file system can be safely backed up using external tools,
such as disk snapshots or copy utilities.

*Looking for a detailed guide backup creation and restoration? Check out our
[Backup and Restore](/docs/operations/backup/) guide!*

caution

QuestDB currently does not support creating checkpoints on Windows.

If you are a Windows user and require backup functionality, please
[comment on this issue](https://github.com/questdb/questdb/issues/4811).

## CHECKPOINT syntax[​](#checkpoint-syntax "Direct link to CHECKPOINT syntax")

![Flow chart showing the syntax of the CHECKPOINT keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNTMiIGhlaWdodD0iODEiPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjkiIHk9IjEiIHdpZHRoPSIxMTAiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzkiIHk9IjIxIj5DSEVDS1BPSU5UPC90ZXh0PgogICAgICAgICA8cmVjdCB4PSIxODEiIHk9IjMiIHdpZHRoPSI3MiIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjE3OSIgeT0iMSIgd2lkdGg9IjcyIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE4OSIgeT0iMjEiPkNSRUFURTwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMTgxIiB5PSI0NyIgd2lkdGg9IjgwIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTc5IiB5PSI0NSIgd2lkdGg9IjgwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjE4OSIgeT0iNjUiPlJFTEVBU0U8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjMwMSIgeT0iMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjk5IiB5PSIxIiB3aWR0aD0iMjQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMzA5IiB5PSIyMSI+OzwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyAxNyBoMiBtMCAwIGgxMCBtMTEwIDAgaDEwIG0yMCAwIGgxMCBtNzIgMCBoMTAgbTAgMCBoOCBtLTEyMCAwIGgyMCBtMTAwIDAgaDIwIG0tMTQwIDAgcTEwIDAgMTAgMTAgbTEyMCAwIHEwIC0xMCAxMCAtMTAgbS0xMzAgMTAgdjI0IG0xMjAgMCB2LTI0IG0tMTIwIDI0IHEwIDEwIDEwIDEwIG0xMDAgMCBxMTAgMCAxMCAtMTAgbS0xMTAgMTAgaDEwIG04MCAwIGgxMCBtMjAgLTQ0IGgxMCBtMjQgMCBoMTAgbTMgMCBoLTMiPjwvcGF0aD4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSIzNDMgMTcgMzUxIDEzIDM1MSAyMSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjM0MyAxNyAzMzUgMTMgMzM1IDIxIj48L3BvbHlnb24+Cjwvc3ZnPg==)

## CHECKPOINT overview[​](#checkpoint-overview "Direct link to CHECKPOINT overview")

To enable online backups, data in QuestDB is mutated via either file append or
via copy-on-write. Checkpoint leverages these storage methods to achieve
reliable and consistent restorations from your database backups.

### What happens during CHECKPOINT CREATE?[​](#what-happens-during-checkpoint-create "Direct link to What happens during CHECKPOINT CREATE?")

When initiatied, `CHECKPOINT CREATE`:

* Disables background jobs that housekeep stale files and data blocks
* Takes snapshot of table transactions across the whole database (all tables)
* Creates a new on-disk data structure that captures append offsets and versions
  of files that represent data for the above transactions. Typically this data
  is stored in the `/var/lib/questdb/.checkpoint` directory.
  + **Do not alter contents of this directory manually**!
* Calls [`sync()`](https://man7.org/linux/man-pages/man2/sync.2.html) to
  synchronously flush filesystem caches to disk

### What happens after a checkpoint has been created?[​](#what-happens-after-a-checkpoint-has-been-created "Direct link to What happens after a checkpoint has been created?")

Once a checkpoint is created, QuestDB continues taking in writes. However, it
will consume more disk space. How much more depends on the shape of the data
that is being written. Data that is written via the append method will yeild
almost no additional disk space consumption other that of the data itself. In
contrast, the copy-on-write method will make data copies, which are usually
copies of non-recent table partitions. This will lead to an increase in disk
space consumption.

**It is strongly recommended that you minimize the time database is in
checkpoint mode and monitor the free disk space closely. The recommended way to
achive this is to utilize file system SNAPSHOTS as described in
[our backup and restore guide](/docs/operations/backup/).**

Also note that QuestDB can only enter checkpoint mode once. After that period of
time, the next checkpoint operation must be to exit checkpoint mode. Attempts to
create a new checkpoint when once exists will fail with the appropriate message.

When in checkpoint mode, you can safely access the file system to take your
snapshot.

### What happens after my snapshot is complete?[​](#what-happens-after-my-snapshot-is-complete "Direct link to What happens after my snapshot is complete?")

After your snapshot is complete, checkpoint mode must be exited via the
`CHECKPOINT RELEASE` SQL. Once executed, QuestDB will reinstate the usual
housekeeping and reclaim disk space.

The database restore is preformed semi-automatically on the database startup.
This is done deliberately to avoid the restore procedure running accidentally on
the source database instance. The database will attempt a restore when empty an
file, typically `/var/lib/questdb/_restore` is present.

The restore procedure will use `/var/lib/questdb/.checkpoint` to adjust the
database files and remove extra data copies. After the restore is successful the
database is avaialble as normal with no extra intervantion required.

## CHECKPOINT examples[​](#checkpoint-examples "Direct link to CHECKPOINT examples")

To enter checkpoint mode:

```prism-code
CHECKPOINT CREATE
```

To exit checkpoint mode:

```prism-code
CHECKPOINT RELEASE
```