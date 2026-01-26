On this page

Retrieves the latest entry by timestamp for a given key or combination of keys,
for scenarios where multiple time series are stored in the same table.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the LATEST ON keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5NTUiIGhlaWdodD0iMTkxIj4KICAgIDxkZWZzPgogICAgICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgICAgICAgIEBuYW1lc3BhY2UgImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIjsKICAgICAgICAgICAgLmxpbmUgICAgICAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6ICM2MzYyNzM7fQogICAgICAgICAgICAuYm9sZC1saW5lICAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzOyBzdHJva2Utd2lkdGg6IDI7IH0KICAgICAgICAgICAgLnRoaW4tbGluZSAgICAgICAgICAge3N0cm9rZTogIzYzNjI3Mzsgc2hhcGUtcmVuZGVyaW5nOiBjcmlzcEVkZ2VzfQogICAgICAgICAgICAuZmlsbGVkICAgICAgICAgICAgICB7ZmlsbDogIzYzNjI3Mzsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgdGV4dC50ZXJtaW5hbCAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjZmZmZmZmOwogICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0Lm5vbnRlcm1pbmFsICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNlMjg5YTQ7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgdGV4dC5yZWdleHAgICAgICAgICAge2ZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsICJTZWdvZSBVSSIsIFJvYm90bywgVWJ1bnR1LCBDYW50YXJlbGwsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICBmaWxsOiAjMDAxNDFGOwogICAgICAgICAgICBmb250LXdlaWdodDogbm9ybWFsOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHJlY3QsIGNpcmNsZSwgcG9seWdvbiB7ZmlsbDogbm9uZTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXJtaW5hbCAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogI2JlMmY1Yjt9CiAgICAgICAgICAgIHJlY3Qubm9udGVybWluYWwgICAgIHtmaWxsOiByZ2JhKDI1NSwyNTUsMjU1LDAuMSk7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHJlY3QudGV4dCAgICAgICAgICAgIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICBwb2x5Z29uLnJlZ2V4cCAgICAgICB7ZmlsbDogI0M3RUNGRjsgc3Ryb2tlOiAjMDM4Y2JjO30KICAgICAgICA8L3N0eWxlPgogICAgPC9kZWZzPgogICAgPHBvbHlnb24gcG9pbnRzPSI5IDYxIDEgNTcgMSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjE3IDYxIDkgNTcgOSA2NSI+PC9wb2x5Z29uPgogICAgICAgICA8cmVjdCB4PSIzMSIgeT0iNDciIHdpZHRoPSI3MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjI5IiB5PSI0NSIgd2lkdGg9IjcwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSI2NSI+U0VMRUNUPC90ZXh0PjxhIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4bGluazpocmVmPSIjY29sdW1uTmFtZSIgeGxpbms6dGl0bGU9ImNvbHVtbk5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSIxNDEiIHk9IjQ3IiB3aWR0aD0iMTAyIiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjEzOSIgeT0iNDUiIHdpZHRoPSIxMDIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjE0OSIgeT0iNjUiPmNvbHVtbk5hbWU8L3RleHQ+PC9hPjxyZWN0IHg9IjE0MSIgeT0iMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMTM5IiB5PSIxIiB3aWR0aD0iMjQiIGhlaWdodD0iMzIiIGNsYXNzPSJ0ZXJtaW5hbCIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDx0ZXh0IGNsYXNzPSJ0ZXJtaW5hbCIgeD0iMTQ5IiB5PSIyMSI+LDwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iMjgzIiB5PSI0NyIgd2lkdGg9IjYwIiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iMjgxIiB5PSI0NSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjI5MSIgeT0iNjUiPkZST008L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiN0YWJsZU5hbWUiIHhsaW5rOnRpdGxlPSJ0YWJsZU5hbWUiPgogICAgICAgICAgICA8cmVjdCB4PSIzNjMiIHk9IjQ3IiB3aWR0aD0iODgiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iMzYxIiB5PSI0NSIgd2lkdGg9Ijg4IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIzNzEiIHk9IjY1Ij50YWJsZU5hbWU8L3RleHQ+PC9hPjxyZWN0IHg9IjQ3MSIgeT0iNDciIHdpZHRoPSI3MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjQ2OSIgeT0iNDUiIHdpZHRoPSI3MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI0NzkiIHk9IjY1Ij5MQVRFU1Q8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjU2MSIgeT0iNDciIHdpZHRoPSI0MCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjU1OSIgeT0iNDUiIHdpZHRoPSI0MCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI1NjkiIHk9IjY1Ij5PTjwvdGV4dD4KICAgICAgICAgPHJlY3QgeD0iNjIxIiB5PSI0NyIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNjE5IiB5PSI0NSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjYyOSIgeT0iNjUiPig8L3RleHQ+PGEgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhsaW5rOmhyZWY9IiNjb2x1bW5OYW1lIiB4bGluazp0aXRsZT0iY29sdW1uTmFtZSI+CiAgICAgICAgICAgIDxyZWN0IHg9IjY2NyIgeT0iNDciIHdpZHRoPSIxMDIiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iNjY1IiB5PSI0NSIgd2lkdGg9IjEwMiIgaGVpZ2h0PSIzMiIgY2xhc3M9Im5vbnRlcm1pbmFsIj48L3JlY3Q+CiAgICAgICAgICAgIDx0ZXh0IGNsYXNzPSJub250ZXJtaW5hbCIgeD0iNjc1IiB5PSI2NSI+Y29sdW1uTmFtZTwvdGV4dD48L2E+PHJlY3QgeD0iNzg5IiB5PSI0NyIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iNzg3IiB5PSI0NSIgd2lkdGg9IjI2IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9Ijc5NyIgeT0iNjUiPik8L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjgzNSIgeT0iNDciIHdpZHRoPSI5OCIgaGVpZ2h0PSIzMiIgcng9IjEwIj48L3JlY3Q+CiAgICAgICAgIDxyZWN0IHg9IjgzMyIgeT0iNDUiIHdpZHRoPSI5OCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI4NDMiIHk9IjY1Ij5QQVJUSVRJT048L3RleHQ+CiAgICAgICAgIDxyZWN0IHg9IjcyNyIgeT0iMTU3IiB3aWR0aD0iMzgiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSI3MjUiIHk9IjE1NSIgd2lkdGg9IjM4IiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjczNSIgeT0iMTc1Ij5CWTwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI2NvbHVtbk5hbWUiIHhsaW5rOnRpdGxlPSJjb2x1bW5OYW1lIj4KICAgICAgICAgICAgPHJlY3QgeD0iODA1IiB5PSIxNTciIHdpZHRoPSIxMDIiIGhlaWdodD0iMzIiPjwvcmVjdD4KICAgICAgICAgICAgPHJlY3QgeD0iODAzIiB5PSIxNTUiIHdpZHRoPSIxMDIiIGhlaWdodD0iMzIiIGNsYXNzPSJub250ZXJtaW5hbCI+PC9yZWN0PgogICAgICAgICAgICA8dGV4dCBjbGFzcz0ibm9udGVybWluYWwiIHg9IjgxMyIgeT0iMTc1Ij5jb2x1bW5OYW1lPC90ZXh0PjwvYT48cmVjdCB4PSI4MDUiIHk9IjExMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjMyIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHJlY3QgeD0iODAzIiB5PSIxMTEiIHdpZHRoPSIyNCIgaGVpZ2h0PSIzMiIgY2xhc3M9InRlcm1pbmFsIiByeD0iMTAiPjwvcmVjdD4KICAgICAgICAgPHRleHQgY2xhc3M9InRlcm1pbmFsIiB4PSI4MTMiIHk9IjEzMSI+LDwvdGV4dD4KICAgICAgICAgPHBhdGggY2xhc3M9ImxpbmUiIGQ9Im0xNyA2MSBoMiBtMCAwIGgxMCBtNzAgMCBoMTAgbTIwIDAgaDEwIG0xMDIgMCBoMTAgbS0xNDIgMCBsMjAgMCBtLTEgMCBxLTkgMCAtOSAtMTAgbDAgLTI0IHEwIC0xMCAxMCAtMTAgbTEyMiA0NCBsMjAgMCBtLTIwIDAgcTEwIDAgMTAgLTEwIGwwIC0yNCBxMCAtMTAgLTEwIC0xMCBtLTEyMiAwIGgxMCBtMjQgMCBoMTAgbTAgMCBoNzggbTIwIDQ0IGgxMCBtNjAgMCBoMTAgbTAgMCBoMTAgbTg4IDAgaDEwIG0wIDAgaDEwIG03MCAwIGgxMCBtMCAwIGgxMCBtNDAgMCBoMTAgbTAgMCBoMTAgbTI2IDAgaDEwIG0wIDAgaDEwIG0xMDIgMCBoMTAgbTAgMCBoMTAgbTI2IDAgaDEwIG0wIDAgaDEwIG05OCAwIGgxMCBtMiAwIGwyIDAgbTIgMCBsMiAwIG0yIDAgbDIgMCBtLTI1MCAxMTAgbDIgMCBtMiAwIGwyIDAgbTIgMCBsMiAwIG0yIDAgaDEwIG0zOCAwIGgxMCBtMjAgMCBoMTAgbTEwMiAwIGgxMCBtLTE0MiAwIGwyMCAwIG0tMSAwIHEtOSAwIC05IC0xMCBsMCAtMjQgcTAgLTEwIDEwIC0xMCBtMTIyIDQ0IGwyMCAwIG0tMjAgMCBxMTAgMCAxMCAtMTAgbDAgLTI0IHEwIC0xMCAtMTAgLTEwIG0tMTIyIDAgaDEwIG0yNCAwIGgxMCBtMCAwIGg3OCBtMjMgNDQgaC0zIj48L3BhdGg+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iOTQ1IDE3MSA5NTMgMTY3IDk1MyAxNzUiPjwvcG9seWdvbj4KICAgICAgICAgPHBvbHlnb24gcG9pbnRzPSI5NDUgMTcxIDkzNyAxNjcgOTM3IDE3NSI+PC9wb2x5Z29uPgo8L3N2Zz4=)

where:

* `columnName` used in the `LATEST ON` part of the clause is a `TIMESTAMP`
  column.
* `columnName` list used in the `PARTITION BY` part of the clause is a list of
  columns of one of the following types: `SYMBOL`, `STRING`, `BOOLEAN`, `SHORT`,
  `INT`, `LONG`, `LONG256`, `CHAR`, `DECIMAL`.

## Description[​](#description "Direct link to Description")

`LATEST ON` is used as part of a [SELECT statement](/docs/query/sql/select/)
for returning the most recent records per unique time series identified by the
`PARTITION BY` column values.

`LATEST ON` requires a
[designated timestamp](/docs/concepts/designated-timestamp/) column. Use
[sub-queries](#latest-on-over-sub-query) for tables without the designated
timestamp.

The query syntax has an impact on the [execution order](#execution-order) of the
`LATEST ON` clause and the `WHERE` clause.

To illustrate how `LATEST ON` is intended to be used, consider the `trades` table
[in the QuestDB demo instance](https://demo.questdb.io/). This table has a
`symbol` column as `SYMBOL` type which specifies the traded instrument. We can
find the most recent trade for each symbol with the following query:

```prism-code
SELECT symbol, timestamp, price  
FROM trades  
LATEST ON timestamp PARTITION BY symbol;
```

| symbol | timestamp | price |
| --- | --- | --- |
| BTC-USD | 2024-06-30T23:59:56.000000Z | 61432.5 |
| ETH-USD | 2024-06-30T23:59:54.000000Z | 3421.8 |
| SOL-USD | 2024-06-30T23:59:42.000000Z | 142.3 |

The above query returns the latest value within each time series stored in the
table. Those time series are determined based on the values in the column(s)
specified in the `LATEST ON` clause. In our example those time series are
represented by different symbols. Then the column used in the `LATEST ON`
part of the clause stands for the designated timestamp column for the table.
This allows the database to find the latest value within each time series.

## Examples[​](#examples "Direct link to Examples")

For the next examples, we can create a table called `balances` with the
following SQL:

```prism-code
CREATE TABLE balances (  
    cust_id SYMBOL,  
    balance_ccy SYMBOL,  
    balance DOUBLE,  
    ts TIMESTAMP  
) TIMESTAMP(ts) PARTITION BY DAY;  
  
insert into balances values ('1', 'USD', 600.5, '2020-04-21T16:03:43.504432Z');  
insert into balances values ('2', 'USD', 950, '2020-04-21T16:08:34.404665Z');  
insert into balances values ('2', 'EUR', 780.2, '2020-04-21T16:11:22.704665Z');  
insert into balances values ('1', 'USD', 1500, '2020-04-21T16:11:32.904234Z');  
insert into balances values ('1', 'EUR', 650.5, '2020-04-22T16:11:32.904234Z');  
insert into balances values ('2', 'USD', 900.75, '2020-04-22T16:12:43.504432Z');  
insert into balances values ('2', 'EUR', 880.2, '2020-04-22T16:18:34.404665Z');  
insert into balances values ('1', 'USD', 330.5, '2020-04-22T16:20:14.404997Z');
```

This provides us with a table with the following content:

| cust\_id | balance\_ccy | balance | ts |
| --- | --- | --- | --- |
| 1 | USD | 600.5 | 2020-04-21T16:01:22.104234Z |
| 2 | USD | 950 | 2020-04-21T16:03:43.504432Z |
| 2 | EUR | 780.2 | 2020-04-21T16:08:34.404665Z |
| 1 | USD | 1500 | 2020-04-21T16:11:22.704665Z |
| 1 | EUR | 650.5 | 2020-04-22T16:11:32.904234Z |
| 2 | USD | 900.75 | 2020-04-22T16:12:43.504432Z |
| 2 | EUR | 880.2 | 2020-04-22T16:18:34.404665Z |
| 1 | USD | 330.5 | 2020-04-22T16:20:14.404997Z |

### Single column[​](#single-column "Direct link to Single column")

When a single `symbol` column is specified in `LATEST ON` queries, the query
will end after all distinct symbol values are found.

Latest records by customer ID

```prism-code
SELECT * FROM balances  
LATEST ON ts PARTITION BY cust_id;
```

The query returns two rows with the most recent records per unique `cust_id`
value:

| cust\_id | balance\_ccy | balance | ts |
| --- | --- | --- | --- |
| 2 | EUR | 880.2 | 2020-04-22T16:18:34.404665Z |
| 1 | USD | 330.5 | 2020-04-22T16:20:14.404997Z |

### Multiple columns[​](#multiple-columns "Direct link to Multiple columns")

When multiple columns are specified in `LATEST ON` queries, the returned results
are the most recent **unique combinations** of the column values. This example
query returns `LATEST ON` customer ID and balance currency:

Latest balance by customer and currency

```prism-code
SELECT cust_id, balance_ccy, balance  
FROM balances  
LATEST ON ts PARTITION BY cust_id, balance_ccy;
```

The results return the most recent records for each unique combination of
`cust_id` and `balance_ccy`.

| cust\_id | balance\_ccy | balance | inactive | ts |
| --- | --- | --- | --- | --- |
| 1 | EUR | 650.5 | FALSE | 2020-04-22T16:11:32.904234Z |
| 2 | USD | 900.75 | FALSE | 2020-04-22T16:12:43.504432Z |
| 2 | EUR | 880.2 | FALSE | 2020-04-22T16:18:34.404665Z |
| 1 | USD | 330.5 | FALSE | 2020-04-22T16:20:14.404997Z |

#### Performance considerations[​](#performance-considerations "Direct link to Performance considerations")

When the `LATEST ON` clause contains a single `symbol` column, QuestDB will know
all distinct values upfront and stop scanning table contents once the latest
entry has been found for each distinct symbol value.

When the `LATEST ON` clause contains multiple columns, QuestDB has to scan the
entire table to find distinct combinations of column values.

Although scanning is fast, performance will degrade on hundreds of millions of
records. If there are multiple columns in the `LATEST ON` clause, this will
result in a full table scan.

### LATEST ON over sub-query[​](#latest-on-over-sub-query "Direct link to LATEST ON over sub-query")

For this example, we can create another table called `unordered_balances` with
the following SQL:

```prism-code
CREATE TABLE unordered_balances (  
    cust_id SYMBOL,  
    balance_ccy SYMBOL,  
    balance DOUBLE,  
    ts TIMESTAMP  
);  
  
insert into unordered_balances values ('2', 'USD', 950, '2020-04-21T16:08:34.404665Z');  
insert into unordered_balances values ('1', 'USD', 330.5, '2020-04-22T16:20:14.404997Z');  
insert into unordered_balances values ('2', 'USD', 900.75, '2020-04-22T16:12:43.504432Z');  
insert into unordered_balances values ('1', 'USD', 1500, '2020-04-21T16:11:32.904234Z');  
insert into unordered_balances values ('1', 'USD', 600.5, '2020-04-21T16:03:43.504432Z');  
insert into unordered_balances values ('1', 'EUR', 650.5, '2020-04-22T16:11:32.904234Z');  
insert into unordered_balances values ('2', 'EUR', 880.2, '2020-04-22T16:18:34.404665Z');  
insert into unordered_balances values ('2', 'EUR', 780.2, '2020-04-21T16:11:22.704665Z');
```

Note that this table doesn't have a designated timestamp column and also
contains time series that are unordered by `ts` column.

Due to the absent designated timestamp column, we can't use `LATEST ON` directly
on this table, but it's possible to use `LATEST ON` over a sub-query:

Latest balance by customer over unordered data

```prism-code
(SELECT * FROM unordered_balances)  
LATEST ON ts PARTITION BY cust_id;
```

Just like with the `balances` table, the query returns two rows with the most
recent records per unique `cust_id` value:

| cust\_id | balance\_ccy | balance | ts |
| --- | --- | --- | --- |
| 2 | EUR | 880.2 | 2020-04-22T16:18:34.404665Z |
| 1 | USD | 330.5 | 2020-04-22T16:20:14.404997Z |

### Execution order[​](#execution-order "Direct link to Execution order")

The following queries illustrate how to change the execution order in a query by
using brackets.

#### WHERE first[​](#where-first "Direct link to WHERE first")

```prism-code
SELECT * FROM balances  
WHERE balance > 800  
LATEST ON ts PARTITION BY cust_id;
```

This query executes `WHERE` before `LATEST ON` and returns the most recent
balance which is above 800. The execution order is as follows:

* filter out all balances below 800
* find the latest balance by `cust_id`

| cust\_id | balance\_ccy | balance | ts |
| --- | --- | --- | --- |
| 1 | USD | 1500 | 2020-04-22T16:11:22.704665Z |
| 2 | EUR | 880.2 | 2020-04-22T16:18:34.404665Z |

#### LATEST ON first[​](#latest-on-first "Direct link to LATEST ON first")

```prism-code
(SELECT * FROM balances LATEST ON ts PARTITION BY cust_id) --note the brackets  
WHERE balance > 800;
```

This query executes `LATEST ON` before `WHERE` and returns the most recent
records, then filters out those below 800. The steps are:

1. Find the latest balances by customer ID.
2. Filter out balances below 800. Since the latest balance for customer 1 is
   equal to 330.5, it is filtered out in this step.

| cust\_id | balance\_ccy | balance | inactive | ts |
| --- | --- | --- | --- | --- |
| 2 | EUR | 880.2 | FALSE | 2020-04-22T16:18:34.404665Z |

#### Combination[​](#combination "Direct link to Combination")

It's possible to combine a time-based filter with the balance filter from the
previous example to query the latest values for the `2020-04-21` date and filter
out those below 800.

```prism-code
(balances WHERE ts in '2020-04-21' LATEST ON ts PARTITION BY cust_id)  
WHERE balance > 800;
```

Since QuestDB allows you to omit the `SELECT * FROM` part of the query, we
omitted it to keep the query compact.

Such a combination is very powerful since it allows you to find the latest
values for a time slice of the data and then apply a filter to them in a single
query.