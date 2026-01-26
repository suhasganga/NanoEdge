On this page

`EXPLAIN` displays the execution plan of an `INSERT`, `SELECT`, or `UPDATE`
statement.

## Syntax[​](#syntax "Direct link to Syntax")

![Flow chart showing the syntax of the EXPLAIN keyword](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNDUiIGhlaWdodD0iMzciPgogICAgPGRlZnM+CiAgICAgICAgPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KICAgICAgICAgICAgQG5hbWVzcGFjZSAiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciOwogICAgICAgICAgICAubGluZSAgICAgICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogIzYzNjI3Mzt9CiAgICAgICAgICAgIC5ib2xkLWxpbmUgICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXM7IHN0cm9rZS13aWR0aDogMjsgfQogICAgICAgICAgICAudGhpbi1saW5lICAgICAgICAgICB7c3Ryb2tlOiAjNjM2MjczOyBzaGFwZS1yZW5kZXJpbmc6IGNyaXNwRWRnZXN9CiAgICAgICAgICAgIC5maWxsZWQgICAgICAgICAgICAgIHtmaWxsOiAjNjM2MjczOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICB0ZXh0LnRlcm1pbmFsICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICNmZmZmZmY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICAgICAgICB9CiAgICAgICAgICAgIHRleHQubm9udGVybWluYWwgICAgIHtmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIFVidW50dSwgQ2FudGFyZWxsLCBIZWx2ZXRpY2EsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgIGZvbnQtc2l6ZTogMTJweDsKICAgICAgICAgICAgZmlsbDogI2UyODlhNDsKICAgICAgICAgICAgZm9udC13ZWlnaHQ6IG5vcm1hbDsKICAgICAgICAgICAgfQogICAgICAgICAgICB0ZXh0LnJlZ2V4cCAgICAgICAgICB7Zm9udC1mYW1pbHk6IC1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgIlNlZ29lIFVJIiwgUm9ib3RvLCBVYnVudHUsIENhbnRhcmVsbCwgSGVsdmV0aWNhLCBzYW5zLXNlcmlmOwogICAgICAgICAgICBmb250LXNpemU6IDEycHg7CiAgICAgICAgICAgIGZpbGw6ICMwMDE0MUY7CiAgICAgICAgICAgIGZvbnQtd2VpZ2h0OiBub3JtYWw7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgcmVjdCwgY2lyY2xlLCBwb2x5Z29uIHtmaWxsOiBub25lOyBzdHJva2U6IG5vbmU7fQogICAgICAgICAgICByZWN0LnRlcm1pbmFsICAgICAgICB7ZmlsbDogbm9uZTsgc3Ryb2tlOiAjYmUyZjViO30KICAgICAgICAgICAgcmVjdC5ub250ZXJtaW5hbCAgICAge2ZpbGw6IHJnYmEoMjU1LDI1NSwyNTUsMC4xKTsgc3Ryb2tlOiBub25lO30KICAgICAgICAgICAgcmVjdC50ZXh0ICAgICAgICAgICAge2ZpbGw6IG5vbmU7IHN0cm9rZTogbm9uZTt9CiAgICAgICAgICAgIHBvbHlnb24ucmVnZXhwICAgICAgIHtmaWxsOiAjQzdFQ0ZGOyBzdHJva2U6ICMwMzhjYmM7fQogICAgICAgIDwvc3R5bGU+CiAgICA8L2RlZnM+CiAgICA8cG9seWdvbiBwb2ludHM9IjkgMTcgMSAxMyAxIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMTcgMTcgOSAxMyA5IDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxyZWN0IHg9IjMxIiB5PSIzIiB3aWR0aD0iODAiIGhlaWdodD0iMzIiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8cmVjdCB4PSIyOSIgeT0iMSIgd2lkdGg9IjgwIiBoZWlnaHQ9IjMyIiBjbGFzcz0idGVybWluYWwiIHJ4PSIxMCI+PC9yZWN0PgogICAgICAgICA8dGV4dCBjbGFzcz0idGVybWluYWwiIHg9IjM5IiB5PSIyMSI+RVhQTEFJTjwvdGV4dD48YSB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeGxpbms6aHJlZj0iI3N0YXRlbWVudCIgeGxpbms6dGl0bGU9InN0YXRlbWVudCI+CiAgICAgICAgICAgIDxyZWN0IHg9IjEzMSIgeT0iMyIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjMyIj48L3JlY3Q+CiAgICAgICAgICAgIDxyZWN0IHg9IjEyOSIgeT0iMSIgd2lkdGg9Ijg2IiBoZWlnaHQ9IjMyIiBjbGFzcz0ibm9udGVybWluYWwiPjwvcmVjdD4KICAgICAgICAgICAgPHRleHQgY2xhc3M9Im5vbnRlcm1pbmFsIiB4PSIxMzkiIHk9IjIxIj5zdGF0ZW1lbnQ8L3RleHQ+PC9hPjxwYXRoIGNsYXNzPSJsaW5lIiBkPSJtMTcgMTcgaDIgbTAgMCBoMTAgbTgwIDAgaDEwIG0wIDAgaDEwIG04NiAwIGgxMCBtMyAwIGgtMyI+PC9wYXRoPgogICAgICAgICA8cG9seWdvbiBwb2ludHM9IjIzNSAxNyAyNDMgMTMgMjQzIDIxIj48L3BvbHlnb24+CiAgICAgICAgIDxwb2x5Z29uIHBvaW50cz0iMjM1IDE3IDIyNyAxMyAyMjcgMjEiPjwvcG9seWdvbj4KPC9zdmc+)

### Description[​](#description "Direct link to Description")

A query execution plan shows how a statement will be implemented: which table is
going to be accessed and how, what join method are employed, and which
predicates are JIT-compiled etc. `EXPLAIN` output is a tree of nodes containing
properties and subnodes (aka child nodes).

In a plan such as:

| QUERY PLAN |
| --- |
| Async JIT Filter |
| filter: 100 `<` l |
| workers: 1 |
| PageFrame |
| Row forward scan |
| Frame forward scan on: tab |

there are:

* 4 nodes:
  + Async JIT Filter
  + PageFrame
  + Row forward scan
  + Frame forward scan
* 2 properties (both belong to Async JIT Filter node):
  + filter
  + workers

For simplicity, some nodes have special properties shown on the same line as
type; for example, `Filter filter: b.age=10` or `Limit lo: 10`.

The following list contains some plan node types:

* `Async Filter` - a parallelized filter that evaluates expressions with Java
  code. In certain scenarios, it also implements the `LIMIT` keyword.
* `Async JIT Filter` - a parallelized filter that evaluates expressions with
  Just-In-Time-compiled filter. In certain scenarios, it also implements the
  `LIMIT` keyword.
* `Interval forward` - scans one or more table data ranges based on the
  designated timestamp predicates. Scan endpoints are found via a binary search
  on timestamp column.
* `CachedWindow` - container for window functions that copies data to memory and
  sorts it, e.g. [row\_number()](/docs/query/functions/window-functions/reference/#row_number)
* `Window` - container for window functions optimized for frames ordered by
  designated timestamp. Instead of copying the underlying dataset to memory it
  buffers just enough per-partition values to compute function result.
* `Count` - returns the count of records in subnode.
* `Cursor-order scan` - scans table records using row ids taken from an index,
  in index order - first all row ids linked to index value A, then B, etc.
* `PageFrame` - full or partial table scan. It contains two children:
  + row cursor - which iterates over rows inside a frame (e.g.
    `Row forward scan`).
  + frame cursor - which iterates over table partitions or partition chunks
    (e.g. `Frame forward scan`).
* `Filter` - standalone (non-JIT-compiled, non-parallelized) filter.
* `Frame forward/backward scan` - scans table partitions in a specified
  direction.
* `GroupBy` - group by with or without key(s). If `vectorized` field shows
  `true`, then the node is parallelized and uses vectorized calculations.
* `Hash` - subnode of this node is used to build a hash table that is later
  looked up (usually in a `JOIN` clause but also applies to `EXCEPT` or
  `INTERSECT`).
* `Index forward/backward scan` - scans all row ids associated with a given
  `symbol` value from start to finish or vice versa.
* `Limit` - standalone node implementing the `LIMIT` keyword. Other nodes can
  implement `LIMIT` internally, e.g. the `Sort` node.
* `Row forward/backward scan` - scans data frame (usually partitioned) records
  in a specified direction.
* `Sort` - sorts data. If low or hi property is specified, then the sort buffer
  size is limited and a number of rows are skipped after sorting.
* `SampleBy` - `SAMPLE BY` keyword implementation. If the `fill` is not shown,
  it means `fill(none)`.
* `Selected Record` - used to reorder or rename columns. It does not do any
  significant processing on its own.
* `Table-order scan` - scans table records using row ids taken from an index in
  table (physical) order - from the lowest to highest row id.
* `VirtualRecord` - adds expressions to a subnode's columns.

Other node types should be easy to link to SQL and database concepts, e.g.
`Except`, `Hash Join` or `Lt Join`.

Many nodes, especially join and sort, have 'light' and 'heavy' variants, e.g.
`Hash Join Light` and `Hash Join`. The former is used when child node(s) support
efficient random access lookups (e.g. `PageFrame`) so storing row id in the
buffer is enough; otherwise, the whole record needs to be copied and the 'heavy'
factory is used.

## Examples[​](#examples "Direct link to Examples")

To illustrate how `EXPLAIN` works, consider the `trades` table
[in the QuestDB demo instance](https://demo.questdb.io/):

```prism-code
CREATE TABLE trades (  
  symbol SYMBOL CAPACITY 256 CACHE,  
  side SYMBOL CAPACITY 256 CACHE,  
  price DOUBLE,  
  amount DOUBLE,  
  timestamp TIMESTAMP  
) TIMESTAMP (timestamp) PARTITION BY DAY
```

### Using `EXPLAIN` for the plan for `SELECT`[​](#using-explain-for-the-plan-for-select "Direct link to using-explain-for-the-plan-for-select")

The following query highlight the plan for `ORDER BY` for the table:

Explain Order By[Demo this query](https://demo.questdb.io/?query=EXPLAIN%20SELECT%20*%20FROM%20trades%20ORDER%20BY%20timestamp%20DESC%3B&executeQuery=true)

```prism-code
EXPLAIN SELECT * FROM trades ORDER BY timestamp DESC;
```

```prism-code
PageFrame  
    Row backward scan  
    Frame backward scan on: trades
```

The plan shows that no sort is required and the result is produced by scanning
the table backward. The scanning direction is possible because the data in the
`trades` table is stored in timestamp order.

Now, let's check the plan for `trades` with a simple filter:

Explain Simple Filter[Demo this query](https://demo.questdb.io/?query=EXPLAIN%20SELECT%20*%20FROM%20trades%20WHERE%20amount%20%3E%20100.0%3B&executeQuery=true)

```prism-code
EXPLAIN SELECT * FROM trades WHERE amount > 100.0;
```

```prism-code
Async JIT Filter workers: 47  
  filter: 100.0<amount [pre-touch]  
    PageFrame  
        Row forward scan  
        Frame forward scan on: trades
```

In this example, the plan shows that the `trades` table undergoes a full scan
(`PageFrame` and subnodes) and the data is processed by the parallelized
JIT-compiled filter.

### Using `EXPLAIN` for the plan for `CREATE` and `INSERT`[​](#using-explain-for-the-plan-for-create-and-insert "Direct link to using-explain-for-the-plan-for-create-and-insert")

Apart from `SELECT`, `EXPLAIN` also works on `CREATE` and `INSERT` statements.
Single-row inserts are straightforward. The examples in this section show the
plan for more complicated `CREATE` and `INSERT` queries.

Explain Create Table[Demo this query](https://demo.questdb.io/?query=EXPLAIN%20CREATE%20TABLE%20trades%20AS%0A(%0A%20%20SELECT%0A%20%20%20%20rnd_symbol('a'%2C%20'b')%20symbol%2C%0A%20%20%20%20rnd_symbol('Buy'%2C%20'Sell')%20side%2C%0A%20%20%20%20rnd_double()%20price%2C%0A%20%20%20%20rnd_double()%20amount%2C%0A%20%20%20%20x%3A%3Atimestamp%20timestamp%0A%20%20FROM%20long_sequence(10)%0A)%20TIMESTAMP(timestamp)%20PARTITION%20BY%20DAY%3B&executeQuery=true)

```prism-code
EXPLAIN CREATE TABLE trades AS  
(  
  SELECT  
    rnd_symbol('a', 'b') symbol,  
    rnd_symbol('Buy', 'Sell') side,  
    rnd_double() price,  
    rnd_double() amount,  
    x::timestamp timestamp  
  FROM long_sequence(10)  
) TIMESTAMP(timestamp) PARTITION BY DAY;
```

```prism-code
Create table: trades  
    VirtualRecord  
      functions: [rnd_symbol([a,b]),rnd_symbol([Buy,Sell]),memoize(rnd_double()),memoize(rnd_double()),x::timestamp]  
        long_sequence count: 10
```

The plan above shows that the data is fetched from a `long_sequence` cursor,
with random data generating functions called in `VirtualRecord`.

The same applies to the following query:

Explain Insert Into

```prism-code
EXPLAIN INSERT INTO trades  
  SELECT  
    rnd_symbol('a', 'b') symbol,  
    rnd_symbol('Buy', 'Sell') side,  
    rnd_double() price,  
    rnd_double() amount,  
    x::timestamp timestamp  
  FROM long_sequence(10);
```

```prism-code
Insert into table: trades  
    VirtualRecord  
      functions: [rnd_symbol([a,b]),rnd_symbol([Buy,Sell]),memoize(rnd_double()),memoize(rnd_double()),x::timestamp]  
        long_sequence count: 10
```

Of course, statements could be much more complex than that. Consider the
following `UPDATE` query:

```prism-code
EXPLAIN UPDATE trades SET amount = 0 WHERE timestamp IN '2022-11-11';
```

```prism-code
Update table: trades  
  VirtualRecord  
    functions: [0]  
      PageFrame  
        Row forward scan  
        Interval forward scan on: trades  
          intervals: [static=[1668124800000000,1668211199999999]
```

The important bit here is `Interval forward scan`. It means that the table is
forward scanned only between points designated by the
`timestamp IN '2022-11-11'` predicate, that is between
`2022-11-11 00:00:00,000000` and `2022-11-11 23:59:59,999999` (shown as raw
epoch micro values in the plan above). `VirtualRecord` is only used to pass 0
constant for each row coming from `PageFrame`.

## Limitations:[​](#limitations "Direct link to Limitations:")

To minimize resource usage, the `EXPLAIN` command does not execute the
statement, to avoid paying a potentially large upfront cost for certain queries
(especially those involving hash join or sort).

`EXPLAIN` provides a useful indication of the query execution, but it does not
guarantee to show the actual execution plan. This is because elements determined
during query runtime are missing.

While `EXPLAIN` shows the number of workers that could be used by a parallelized
node it is only the upper limit. Depending on the data volume and system load, a
query can use fewer workers.

note

Under the hood, the plan nodes are called `Factories`. Most plan nodes can be
mapped to implementation by adding the `RecordCursorFactory` or
`FrameCursorFactory` suffix, e.g.

* `PageFrame` -> `PageFrameRecordCursorFactory`
* `Async JIT Filter` -> `AsyncJitFilteredRecordCursorFactory`
* `SampleByFillNoneNotKeyed` -> `SampleByFillNoneNotKeyedRecordCursorFactory`
  while some are a bit harder to identify, e.g.
* `GroupByRecord vectorized: false` ->
  `io.questdb.griffin.engine.groupby.GroupByRecordCursorFactory`
* `GroupByRecord vectorized: true` ->
  `io.questdb.griffin.engine.groupby.vect.GroupByRecordCursorFactory`

Other classes can be identified by searching for the node name in the `toPlan()`
methods.

## See also[​](#see-also "Direct link to See also")

This section includes links to additional information such as tutorials:

* [EXPLAIN Your SQL Query Plan](https://questdb.com/blog/explain-sql-query-plan/)
* [Exploring Query Plan Scan Nodes with SQL EXPLAIN](https://questdb.com/blog/exploring-query-plan-scan-nodes-sql-explain/)