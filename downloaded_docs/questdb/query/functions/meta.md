On this page

These functions provide instance-level information and table, column and
partition information including metadata. They are particularly useful for
learning useful information about your instance, including:

* [Designated timestamp](/docs/concepts/designated-timestamp/) columns
* [Attached, detached, or attachable](/docs/query/sql/alter-table-attach-partition/)
  partitions
* Partition storage size on disk
* Running SQL commands

## build[​](#build "Direct link to build")

**Arguments:**

* `build()` does not require arguments.

**Return value:**

Returns a string with the current QuestDB version and hash.

**Examples:**

```prism-code
SELECT build();
```

| build |
| --- |
| Build Information: QuestDB 7.3.5, JDK 17.0.7, Commit Hash 460b817b0a3705c5633619a8ef9efb5163f1569c |

## functions[​](#functions "Direct link to functions")

**Arguments:**

* `functions()` does not require arguments.

**Return value:**

Returns all available database functions.

**Examples:**

```prism-code
functions();
```

| name | signature | signature\_translated | runtime\_constant | type |
| --- | --- | --- | --- | --- |
| or | or(TT) | or(boolean, boolean) | FALSE | STANDARD |
| and | and(TT) | and(boolean, boolean) | FALSE | STANDARD |
| not | not(T) | not(boolean) | FALSE | STANDARD |

## query\_activity[​](#query_activity "Direct link to query_activity")

**Arguments:**

* `query_activity()` does not require arguments.

**Return value:**

Returns metadata on running SQL queries, including columns such as:

* query\_id - identifier of the query that can be used with
  [cancel query](/docs/query/sql/cancel-query/) command or
  [cancelQuery()](/docs/query/sql/cancel-query/) function
* worker\_id - identifier of worker thread that initiated query processing. Note
  that many multithreaded queries also run on other workers
* worker\_pool - name of worker pool used to execute the query
* username - name of user executing the query
* query\_start - timestamp of when query started
* state\_change - timestamp of latest query state change, such as a cancellation
* state - state of running query, can be `active` or `cancelled`
* query - text of sql query

**Examples:**

```prism-code
SELECT * FROM query_activity();
```

| query\_id | worker\_id | worker\_pool | username | query\_start | state\_change | state | query |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 62179 | 5 | shared | bob | 2024-01-09T10:03:05.557397Z | 2024-01-09T10:03:05.557397 | active | select \* from query\_activity() |
| 57777 | 6 | shared | bob | 2024-01-09T08:58:55.988017Z | 2024-01-09T08:58:55.988017Z | active | SELECT symbol,approx\_percentile(price, 50, 2) from trades |

## memory\_metrics[​](#memory_metrics "Direct link to memory_metrics")

**Arguments:**

* `memory_metrics()` does not require arguments.

**Return value:**

Returns granular memory metrics.

**Examples:**

```prism-code
memory_metrics();
```

| memory\_tag | bytes |
| --- | --- |
| TOTAL\_USED | 142624730 |
| RSS | 328609792 |
| MMAP\_DEFAULT | 196728 |
| NATIVE\_DEFAULT | 256 |
| MMAP\_O3 | 0 |
| NATIVE\_O3 | 96 |

## reader\_pool[​](#reader_pool "Direct link to reader_pool")

**Arguments:**

* `reader_pool()` does not require arguments.

**Return value:**

Returns information about the current state of the reader pool in QuestDB. The
reader pool is a cache of table readers that are kept open to speed up
subsequent reads from the same table. The returned information includes the
table name, the ID of the thread that currently owns the reader, the timestamp
of the last time the reader was accessed, and the current transaction ID with
which the reader is associated.

**Examples:**

```prism-code
SELECT * FROM reader_pool();
```

| table\_name | owner\_thread\_id | last\_access\_timestamp | current\_txn |
| --- | --- | --- | --- |
| sensors | null | 2023-12-01T19:28:14.311703Z | 1 |

## writer\_pool[​](#writer_pool "Direct link to writer_pool")

**Arguments:**

* `writer_pool()` does not require arguments.

**Return value:**

Returns information about the current state of the writer pool in QuestDB. The
writer pool is a cache of table writers that are kept open to speed up
subsequent writes to the same table. The returned information includes the table
name, the ID of the thread that currently owns the writer, the timestamp of the
last time the writer was accessed, and the reason for the ownership.

**Examples:**

```prism-code
SELECT * FROM writer_pool();
```

| table\_name | owner\_thread\_id | last\_access\_timestamp | ownership\_reason |
| --- | --- | --- | --- |
| sys.column\_versions\_purge\_log | 1 | 2023-12-01T18:50:03.412468Z | QuestDB system |
| telemetry\_config | 1 | 2023-12-01T18:50:03.470604Z | telemetryConfig |
| telemetry | 1 | 2023-12-01T18:50:03.464501Z | telemetry |
| sys.telemetry\_wal | 1 | 2023-12-01T18:50:03.467924Z | telemetry |
| example\_table | null | 2023-12-01T20:33:33.270984Z | null |

## current database, schema, or user[​](#current-database-schema-or-user "Direct link to current database, schema, or user")

`current_database()`, `current_schema()`, and `current_user()` are standard SQL
functions that return information about the current database, schema, schemas,
and user, respectively.

```prism-code
-- Get the current database  
SELECT current_database();  
  
-- Get the current schema  
SELECT current_schema();  
  
-- Get the current user  
SELECT current_user();
```

Each of these functions returns a single value, so you can use them in a SELECT
statement without any arguments.

## tables[​](#tables "Direct link to tables")

`tables()` returns metadata and real-time statistics for all tables in the
database, including write activity, WAL status, and performance metrics.

**Arguments:**

* `tables()` does not require arguments.

**Return value:**

Returns a `table` with the following columns:

### Basic table information[​](#basic-table-information "Direct link to Basic table information")

| Column | Type | Description |
| --- | --- | --- |
| `id` | INT | Internal table ID |
| `table_name` | STRING | Table name |
| `designatedTimestamp` | STRING | Name of the designated timestamp column, or `null` |
| `partitionBy` | STRING | Partition strategy: `NONE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `YEAR` |
| `walEnabled` | BOOLEAN | Whether WAL (Write-Ahead Log) is enabled |
| `dedup` | BOOLEAN | Whether deduplication is enabled |
| `ttlValue` | INT | TTL (Time-To-Live) value |
| `ttlUnit` | STRING | TTL unit: `HOUR`, `DAY`, `WEEK`, `MONTH`, `YEAR` |
| `matView` | BOOLEAN | Whether this is a materialized view |
| `directoryName` | STRING | Directory name on disk (includes  `(->)` suffix for symlinks) |
| `maxUncommittedRows` | INT | Table's `maxUncommittedRows` setting |
| `o3MaxLag` | LONG | Table's `o3MaxLag` setting in microseconds |

note

`(->)` means the table was created using the
[IN VOLUME](/docs/query/sql/create-table/#table-target-volume) clause.

### Table metrics (table\_\* prefix)[​](#table-metrics-table_-prefix "Direct link to Table metrics (table_* prefix)")

| Column | Type | Description |
| --- | --- | --- |
| `table_suspended` | BOOLEAN | Whether a WAL table is suspended (`false` for non-WAL tables) |
| `table_type` | CHAR | Table type: `T` (table), `M` (materialized view), `V` (view) |
| `table_row_count` | LONG | Approximate row count at last tracked write |
| `table_min_timestamp` | TIMESTAMP | Minimum timestamp of data in the table (updated on WAL merge) |
| `table_max_timestamp` | TIMESTAMP | Maximum timestamp of data in the table (updated on WAL merge) |
| `table_last_write_timestamp` | TIMESTAMP | Approximate timestamp of last TableWriter commit |
| `table_txn` | LONG | TableWriter transaction number at last tracked write |
| `table_memory_pressure_level` | INT | Memory pressure: `0` (none), `1` (reduced parallelism), `2` (backoff). `null` for non-WAL |
| `table_write_amp_count` | LONG | Total write amplification samples recorded |
| `table_write_amp_p50` | DOUBLE | Median write amplification ratio |
| `table_write_amp_p90` | DOUBLE | 90th percentile ratio |
| `table_write_amp_p99` | DOUBLE | 99th percentile ratio |
| `table_write_amp_max` | DOUBLE | Maximum ratio |
| `table_merge_rate_count` | LONG | Total merge throughput samples recorded |
| `table_merge_rate_p50` | LONG | Median throughput in rows/second |
| `table_merge_rate_p90` | LONG | Throughput that 90% of jobs **exceeded** (slowest 10%) |
| `table_merge_rate_p99` | LONG | Throughput that 99% of jobs **exceeded** (slowest 1%) |
| `table_merge_rate_max` | LONG | Maximum throughput in rows/second |

Write amplification measures O3 (out-of-order) merge overhead as `physicalRowsWritten / logicalRows`.
A ratio of `1.0` means no amplification. Higher values indicate O3 merge overhead.

note

Merge rate P99 shows the *lowest* throughput (worst performance), not the highest.

### WAL metrics (wal\_\* prefix)[​](#wal-metrics-wal_-prefix "Direct link to WAL metrics (wal_* prefix)")

| Column | Type | Description |
| --- | --- | --- |
| `wal_pending_row_count` | LONG | Rows written to WAL but not yet applied to table |
| `wal_dedup_row_count_since_start` | LONG | Cumulative rows removed by deduplication (since server start) |
| `wal_txn` | LONG | WAL sequencer transaction number (WAL tables only) |
| `wal_max_timestamp` | TIMESTAMP | Max data timestamp from last WAL commit (WAL tables only) |
| `wal_tx_count` | LONG | Total WAL transactions recorded (since server start) |
| `wal_tx_size_p50` | LONG | Median transaction size in rows |
| `wal_tx_size_p90` | LONG | 90th percentile transaction size in rows |
| `wal_tx_size_p99` | LONG | 99th percentile transaction size in rows |
| `wal_tx_size_max` | LONG | Maximum transaction size in rows |

### Replica metrics (replica\_\* prefix)[​](#replica-metrics-replica_-prefix "Direct link to Replica metrics (replica_* prefix)")

These columns are populated on **replicas only** via replication download tracking:

| Column | Type | Description |
| --- | --- | --- |
| `replica_batch_count` | LONG | Total download batches recorded |
| `replica_batch_size_p50` | LONG | Median batch size in rows |
| `replica_batch_size_p90` | LONG | 90th percentile batch size |
| `replica_batch_size_p99` | LONG | 99th percentile batch size |
| `replica_batch_size_max` | LONG | Maximum batch size |
| `replica_more_pending` | BOOLEAN | `true` if the last download batch was limited and more data is available |

On primary instances, these columns will be `0` or `false`.

### Data precision and limitations[​](#data-precision-and-limitations "Direct link to Data precision and limitations")

These values are approximations, not precise real-time metrics:

* **Null when not tracked**: Values are `null` for tables not written to since server start, or evicted from the tracker
* **Writer stats updated on pool return**: `table_row_count`, `table_last_write_timestamp`, `table_txn` are captured when TableWriter returns to the pool, not on every commit. A writer held for a long time won't update these columns until released.
* **WAL stats updated in real-time**:
  + On WAL commit: `wal_pending_row_count` (incremented), `wal_txn`, `wal_max_timestamp`, `wal_tx_size_*` histogram
  + On WAL apply: `wal_pending_row_count` (decremented), `wal_dedup_row_count_since_start`, `table_min_timestamp`, `table_max_timestamp`, `table_write_amp_*`, `table_merge_rate_*`
* **LRU eviction**: Tracker maintains bounded memory (default 1000 tables). Least recently written tables are evicted when capacity is exceeded
* **Startup hydration**: Values are hydrated from table metadata (`TxReader`) on startup, but diverge as writes occur

**Non-WAL tables**: `wal_txn`, `wal_max_timestamp`, `wal_pending_row_count`, `wal_dedup_row_count_since_start`, `table_min_timestamp`, `table_max_timestamp`, `table_memory_pressure_level`, and histogram columns are `null` or `0`.

**WAL tables**: All columns populated when tracked. `wal_max_timestamp` reflects the max data timestamp from the WAL transaction, not wall-clock time. `table_min_timestamp` and `table_max_timestamp` reflect the actual data range in the table after WAL merge.

### Configuration[​](#configuration "Direct link to Configuration")

| Property | Default | Description |
| --- | --- | --- |
| `cairo.recent.write.tracker.capacity` | 1000 | Maximum number of tables tracked |

Tables exceeding this capacity are evicted based on least recent write activity.

**Examples:**

List all tables

```prism-code
tables();
```

| id | table\_name | designatedTimestamp | partitionBy | walEnabled | directoryName | dedup | ttlValue | ttlUnit | matView |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | my\_table | ts | DAY | false | my\_table | false | 0 | HOUR | false |
| 2 | device\_data | null | NONE | false | device\_data | false | 0 | HOUR | false |
| 3 | short\_lived | null | HOUR | false | short\_lived (->) | false | 1 | HOUR | false |

All tables with a daily partitioning strategy

```prism-code
tables() WHERE partitionBy = 'DAY';
```

| id | table\_name | designatedTimestamp | partitionBy | walEnabled | directoryName | dedup | ttlValue | ttlUnit | matView |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | my\_table | ts | DAY | true | my\_table | false | 0 | HOUR | false |

Recently written tables

```prism-code
SELECT table_name, table_row_count, table_last_write_timestamp  
FROM tables()  
WHERE table_last_write_timestamp IS NOT NULL  
ORDER BY table_last_write_timestamp DESC  
LIMIT 10;
```

Tables with most recent data

```prism-code
SELECT table_name, table_min_timestamp, table_max_timestamp  
FROM tables()  
WHERE table_max_timestamp IS NOT NULL  
ORDER BY table_max_timestamp DESC  
LIMIT 10;
```

WAL apply lag

```prism-code
SELECT  
    table_name,  
    wal_txn - table_txn AS pending_txns,  
    wal_pending_row_count  
FROM tables()  
WHERE walEnabled  
  AND wal_txn IS NOT NULL  
  AND wal_txn > table_txn  
ORDER BY pending_txns DESC;
```

Suspended tables

```prism-code
SELECT table_name, table_suspended, table_memory_pressure_level  
FROM tables()  
WHERE walEnabled AND table_suspended;
```

Memory pressure

```prism-code
SELECT table_name, table_memory_pressure_level  
FROM tables()  
WHERE table_memory_pressure_level > 0  
ORDER BY table_memory_pressure_level DESC;
```

Deduplication activity

```prism-code
SELECT table_name, wal_dedup_row_count_since_start, wal_tx_count,  
       wal_dedup_row_count_since_start * 100.0 / NULLIF(wal_tx_count, 0) AS dedup_ratio  
FROM tables()  
WHERE wal_dedup_row_count_since_start > 0  
ORDER BY wal_dedup_row_count_since_start DESC;
```

Large transactions

```prism-code
SELECT table_name, wal_tx_count, wal_tx_size_p50, wal_tx_size_p99, wal_tx_size_max  
FROM tables()  
WHERE walEnabled AND wal_tx_count > 0  
ORDER BY wal_tx_size_p99 DESC;
```

High variance (spiky workloads)

```prism-code
SELECT table_name, wal_tx_size_p50, wal_tx_size_max,  
       wal_tx_size_max / NULLIF(wal_tx_size_p50, 0) AS spike_ratio  
FROM tables()  
WHERE walEnabled AND wal_tx_size_max > wal_tx_size_p50 * 10;
```

High write amplification (O3 overhead)

```prism-code
SELECT table_name,  
       table_write_amp_count,  
       table_write_amp_p50,  
       table_write_amp_p99,  
       table_write_amp_max  
FROM tables()  
WHERE walEnabled  
  AND table_write_amp_p50 > 2.0  
ORDER BY table_write_amp_p99 DESC;
```

Slow merge performance

```prism-code
SELECT table_name,  
       table_merge_rate_p99 AS slowest_throughput,  
       table_merge_rate_p50 AS median_throughput,  
       table_merge_rate_max AS best_throughput  
FROM tables()  
WHERE walEnabled  
  AND table_merge_rate_count > 0  
ORDER BY table_merge_rate_p99 ASC;
```

Replica download statistics

```prism-code
SELECT table_name, replica_batch_count, replica_batch_size_p50,  
       replica_batch_size_p90, replica_batch_size_max, replica_more_pending  
FROM tables()  
WHERE replica_batch_count > 0  
ORDER BY replica_batch_count DESC;
```

Table configuration overview

```prism-code
SELECT table_name,  
       partitionBy,  
       walEnabled,  
       dedup,  
       maxUncommittedRows,  
       o3MaxLag / 1000000 AS o3MaxLagSeconds  
FROM tables()  
WHERE walEnabled  
ORDER BY table_name;
```

Health dashboard query

```prism-code
SELECT  
    table_name,  
    table_row_count,  
    wal_pending_row_count,  
    CASE  
        WHEN table_suspended THEN 'SUSPENDED'  
        WHEN table_memory_pressure_level = 2 THEN 'BACKOFF'  
        WHEN table_memory_pressure_level = 1 THEN 'PRESSURE'  
        ELSE 'OK'  
    END AS status,  
    wal_txn - table_txn AS lag_txns,  
    table_write_amp_p50 AS write_amp,  
    table_merge_rate_p99 AS slowest_merge  
FROM tables()  
WHERE walEnabled  
ORDER BY  
    table_suspended DESC,  
    table_memory_pressure_level DESC,  
    wal_pending_row_count DESC;
```

## table\_storage[​](#table_storage "Direct link to table_storage")

`table_storage()` - Returns information about the storage and structure of all
user tables and materialized views in the database.

Provides detailed storage information about all user tables and materialized
views within QuestDB. It returns one row per table, including information about
partitioning, row counts, and disk usage.

* The `table_storage()` function excludes system tables; it only lists
  user-created tables.
* The `diskSize` value represents the total size of all files associated with
  the table on disk, including data, index, and metadata files.
* The `partitionBy` column indicates the partitioning strategy used for the
  table. It can be `NONE` if the table is not partitioned.

**Return values:**

The function returns the following columns:

* `tableName` (`string`): The name of the table or materialized view.
* `walEnabled` (`boolean`): Indicates whether Write-Ahead Logging (WAL) is
  enabled for the table.
* `partitionBy` (`string`): The partitioning type of the table (e.g., NONE, DAY,
  MONTH, YEAR, etc.).
* `partitionCount` (`long`): The number of partitions the table has.
* `rowCount` (`long`): The total number of rows in the table.
* `diskSize` (`long`): The total disk space used by the table, in bytes.

**Examples:**

Retrieve storage information for all tables.

Checking our demo tables[Demo this query](https://demo.questdb.io/?query=SELECT%20*%20FROM%20table_storage()%3B&executeQuery=true)

```prism-code
SELECT * FROM table_storage();
```

* The query retrieves storage details for all tables in the database.
* The `diskSize` column shows the total disk space used by each table in bytes.

| tableName | walEnabled | partitionBy | partitionCount | rowCount | diskSize |
| --- | --- | --- | --- | --- | --- |
| trips | true | MONTH | 126 | 1634599313 | 261536158948 |
| AAPL\_orderbook | true | HOUR | 16 | 3024878 | 2149403527 |
| weather | false | NONE | 1 | 137627 | 9972598 |
| trades | true | DAY | 954 | 1000848308 | 32764798760 |
| ethblocks\_json | true | DAY | 3328 | 20688364 | 28311960478 |

---

Filter tables with WAL enabled.

WAL only tables[Demo this query](https://demo.questdb.io/?query=SELECT%20tableName%2C%20rowCount%2C%20diskSize%0AFROM%20table_storage()%0AWHERE%20walEnabled%20%3D%20true%3B&executeQuery=true)

```prism-code
SELECT tableName, rowCount, diskSize  
FROM table_storage()  
WHERE walEnabled = true;
```

| tableName | rowCount | diskSize |
| --- | --- | --- |
| trips | 1634599313 | 261536158948 |
| AAPL\_orderbook | 3024878 | 2149403527 |
| trades | 1000850255 | 32764804264 |
| ethblocks\_json | 20688364 | 28311960478 |

---

Show tables partitioned by `HOUR`.

Show tables partitioned by hour[Demo this query](https://demo.questdb.io/?query=SELECT%20tableName%2C%20partitionCount%2C%20rowCount%0AFROM%20table_storage()%0AWHERE%20partitionBy%20%3D%20'HOUR'%3B&executeQuery=true)

```prism-code
SELECT tableName, partitionCount, rowCount  
FROM table_storage()  
WHERE partitionBy = 'HOUR';
```

## wal\_tables[​](#wal_tables "Direct link to wal_tables")

note

For monitoring and observability, use [`tables()`](#tables) instead.
`tables()` provides all the same information plus additional metrics
(pending rows, memory pressure, deduplication stats, throughput histograms),
and is fully in-memory. `wal_tables()` reads from disk and is less suitable
for frequent polling.

`wal_tables()` returns the WAL status for all
[WAL tables](/docs/concepts/write-ahead-log/) or materialized views in the
database.

**Arguments:**

* `wal_tables()` does not require arguments.

**Return value:**

Returns a `table` including the following information:

* `name` - table or materialized view name
* `suspended` - suspended status flag
* `writerTxn` - the last committed transaction in TableWriter (equivalent to `table_txn` in `tables()`)
* `writerLagTxnCount` - the number of transactions that are kept invisible when
  writing to the table; these transactions will be eventually moved to the table
  data and become visible for readers (equivalent to `wal_txn - table_txn`)
* `sequencerTxn` - the last committed transaction in the sequencer (equivalent to `wal_txn` in `tables()`)

**Examples:**

List all tables

```prism-code
wal_tables();
```

| name | suspended | writerTxn | writerLagTxnCount | sequencerTxn |
| --- | --- | --- | --- | --- |
| sensor\_wal | false | 2 | 1 | 4 |
| weather\_wal | false | 3 | 0 | 3 |
| test\_wal | true | 7 | 1 | 9 |

## table\_columns[​](#table_columns "Direct link to table_columns")

`table_columns('tableName')` returns the schema of a table or a materialized
view.

**Arguments:**

* `tableName` is the name of an existing table or materialized view as a string.

**Return value:**

Returns a `table` with the following columns:

* `column` - name of the available columns in the table
* `type` - type of the column
* `indexed` - if indexing is applied to this column
* `indexBlockCapacity` - how many row IDs to store in a single storage block on
  disk
* `symbolCached` - whether this `symbol` column is cached
* `symbolCapacity` - how many distinct values this column of `symbol` type is
  expected to have
* `designated` - if this is set as the designated timestamp column for this
  table
* `upsertKey` - if this column is a part of UPSERT KEYS list for table
  [deduplication](/docs/concepts/deduplication/)

For more details on the meaning and use of these values, see the
[CREATE TABLE](/docs/query/sql/create-table/) documentation.

**Examples:**

Get all columns in a table

```prism-code
table_columns('my_table');
```

| column | type | indexed | indexBlockCapacity | symbolCached | symbolCapacity | designated | upsertKey |
| --- | --- | --- | --- | --- | --- | --- | --- |
| symb | SYMBOL | true | 1048576 | false | 256 | false | false |
| price | DOUBLE | false | 0 | false | 0 | false | false |
| ts | TIMESTAMP | false | 0 | false | 0 | true | false |
| s | VARCHAR | false | 0 | false | 0 | false | false |

Get designated timestamp column

```prism-code
SELECT column, type, designated FROM table_columns('my_table') WHERE designated = true;
```

| column | type | designated |
| --- | --- | --- |
| ts | TIMESTAMP | true |

Get the count of column types

```prism-code
SELECT type, count() FROM table_columns('my_table');
```

| type | count |
| --- | --- |
| SYMBOL | 1 |
| DOUBLE | 1 |
| TIMESTAMP | 1 |
| VARCHAR | 1 |

## table\_partitions[​](#table_partitions "Direct link to table_partitions")

`table_partitions('tableName')` returns information for the partitions of a
table or a materialized view with the option to filter the partitions.

**Arguments:**

* `tableName` is the name of an existing table or materialized view as a string.

**Return value:**

Returns a table with the following columns:

* `index` - *INTEGER*, index of the partition (*NaN* when the partition is not
  attached)
* `partitionBy` - *STRING*, one of *NONE*, *HOUR*, *DAY*, *WEEK*, *MONTH* and
  *YEAR*
* `name` - *STRING*, name of the partition, e.g. `2023-03-14`,
  `2023-03-14.detached`, `2023-03-14.attachable`
* `minTimestamp` - *LONG*, min timestamp of the partition (*NaN* when the table
  is not partitioned)
* `maxTimestamp` - *LONG*, max timestamp of the partition (*NaN* when the table
  is not partitioned)
* `numRows` - *LONG*, number of rows in the partition
* `diskSize` - *LONG*, size of the partition in bytes
* `diskSizeHuman` - *STRING*, size of the partition meant for humans to read
  (same output as function
  [size\_pretty](/docs/query/functions/numeric/#size_pretty))
* `readOnly` - *BOOLEAN*, true if the partition is
  [attached via soft link](/docs/query/sql/alter-table-attach-partition/#symbolic-links)
* `active` - *BOOLEAN*, true if the partition is the last partition, and whether
  we are writing to it (at least one record)
* `attached` - *BOOLEAN*, true if the partition is
  [attached](/docs/query/sql/alter-table-attach-partition/)
* `detached` - *BOOLEAN*, true if the partition is
  [detached](/docs/query/sql/alter-table-detach-partition/) (`name` of the
  partition will contain the `.detached` extension)
* `attachable` - *BOOLEAN*, true if the partition is detached and can be
  attached (`name` of the partition will contain the `.attachable` extension)

**Examples:**

Create table my\_table

```prism-code
CREATE TABLE my_table AS (  
    SELECT  
        rnd_symbol('EURO', 'USD', 'OTHER') symbol,  
        rnd_double() * 50.0 price,  
        rnd_double() * 20.0 amount,  
        to_timestamp('2023-01-01', 'yyyy-MM-dd') + x * 6 * 3600 * 100000L timestamp  
    FROM long_sequence(700)  
), INDEX(symbol capacity 32) TIMESTAMP(timestamp) PARTITION BY WEEK;
```

Get all partitions from my\_table

```prism-code
table_partitions('my_table');
```

| index | partitionBy | name | minTimestamp | maxTimestamp | numRows | diskSize | diskSizeHuman | readOnly | active | attached | detached | attachable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | WEEK | 2022-W52 | 2023-01-01 00:36:00.0 | 2023-01-01 23:24:00.0 | 39 | 98304 | 96.0 KiB | false | false | true | false | false |
| 1 | WEEK | 2023-W01 | 2023-01-02 00:00:00.0 | 2023-01-08 23:24:00.0 | 280 | 98304 | 96.0 KiB | false | false | true | false | false |
| 2 | WEEK | 2023-W02 | 2023-01-09 00:00:00.0 | 2023-01-15 23:24:00.0 | 280 | 98304 | 96.0 KiB | false | false | true | false | false |
| 3 | WEEK | 2023-W03 | 2023-01-16 00:00:00.0 | 2023-01-18 12:00:00.0 | 101 | 83902464 | 80.0 MiB | false | true | true | false | false |

Get size of a table in disk

```prism-code
SELECT size_pretty(sum(diskSize)) FROM table_partitions('my_table');
```

| size\_pretty |
| --- |
| 80.3 MB |

Get active partition of a table

```prism-code
SELECT * FROM table_partitions('my_table') WHERE active = true;
```

| index | partitionBy | name | minTimestamp | maxTimestamp | numRows | diskSize | diskSizeHuman | readOnly | active | attached | detached | attachable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | WEEK | 2023-W03 | 2023-01-16 00:00:00.0 | 2023-01-18 12:00:00.0 | 101 | 83902464 | 80.0 MiB | false | true | true | false | false |

## materialized\_views[​](#materialized_views "Direct link to materialized_views")

`materialized_views()` returns the list of all materialized views in the
database.

**Arguments:**

* `materialized_views()` does not require arguments.

**Return value:**

Returns a `table` including the following information:

* `view_name` - materialized view name
* `refresh_type` - refresh strategy type
* `base_table_name` - base table name
* `last_refresh_start_timestamp` - last time when an incremental refresh for the
  view was started
* `last_refresh_finish_timestamp` - last time when an incremental refresh for
  the view finished
* `view_sql` - query used to populate view data
* `view_table_dir_name` - view directory name
* `invalidation_reason` - message explaining why the view was marked as invalid
* `view_status` - view status: 'valid', 'refreshing', or 'invalid'
* `refresh_base_table_txn` - the last base table transaction used to refresh the
  materialized view
* `base_table_txn` - the last committed transaction in the base table
* `refresh_limit_value` - how many units back in time the refresh limit goes
* `refresh_limit_unit` - how long each unit is
* `timer_start` - start date for the scheduled refresh timer
* `timer_interval_value` - how many interval units between each refresh
* `timer_interval_unit` - how long each unit is

**Examples:**

List all materialized views

```prism-code
materialized_views();
```

| view\_name | refresh\_type | base\_table\_name | last\_refresh\_start\_timestamp | last\_refresh\_finish\_timestamp | view\_sql | view\_table\_dir\_name | invalidation\_reason | view\_status | refresh\_base\_table\_txn | base\_table\_txn | refresh\_limit\_value | refresh\_limit\_unit | timer\_start | timer\_interval\_value | timer\_interval\_unit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trades\_OHLC\_15m | immediate | trades | 2025-05-30T16:40:37.562421Z | 2025-05-30T16:40:37.568800Z | SELECT timestamp, symbol, first(price) AS open, max(price) as high, min(price) as low, last(price) AS close, sum(amount) AS volume FROM trades SAMPLE BY 15m | trades\_OHLC\_15m~27 | null | valid | 55141609 | 55141609 | 0 | null | null | 0 | null |
| trades\_latest\_1d | immediate | trades | 2025-05-30T16:40:37.554274Z | 2025-05-30T16:40:37.562049Z | SELECT timestamp, symbol, side, last(price) AS price, last(amount) AS amount, last(timestamp) as latest FROM trades SAMPLE BY 1d | trades\_latest\_1d~28 | null | valid | 55141609 | 55141609 | 0 | null | null | 0 | null |

## views[​](#views "Direct link to views")

`views()` returns the list of all views in the database.

**Arguments:**

* `views()` does not require arguments.

**Return value:**

Returns a `table` including the following information:

* `view_name` - view name
* `view_sql` - query used to define the view (without CREATE VIEW wrapper)
* `view_table_dir_name` - internal directory name
* `invalidation_reason` - message explaining why the view was marked as invalid,
  empty if valid
* `view_status` - view status: `valid` or `invalid`
* `view_status_update_time` - timestamp of last status change

**Examples:**

List all views

```prism-code
views();
```

| view\_name | view\_sql | view\_table\_dir\_name | invalidation\_reason | view\_status | view\_status\_update\_time |
| --- | --- | --- | --- | --- | --- |
| hourly\_summary | SELECT ts, symbol, sum(qty) FROM trades SAMPLE BY 1h | hourly\_summary~1 |  | valid | 2025-05-30T10:15:00.000000Z |
| price\_view | SELECT symbol, last(price) FROM trades SAMPLE BY 1d | price\_view~2 |  | valid | 2025-05-30T10:20:00.000000Z |

Find invalid views

```prism-code
SELECT view_name, invalidation_reason  
FROM views()  
WHERE view_status = 'invalid';
```

List views ordered by name

```prism-code
SELECT * FROM views() ORDER BY view_name;
```

## version/pg\_catalog.version[​](#versionpg_catalogversion "Direct link to version/pg_catalog.version")

`version()` or `pg_catalog.version()` returns the supported version of the
PostgreSQL Wire Protocol.

**Arguments:**

* `version()` or `pg_catalog.version()` does not require arguments.

**Return value:**

Returns `string`.

**Examples:**

```prism-code
SELECT version();  
  
--The above equals to:  
  
SELECT pg_catalog.version();
```

| version |
| --- |
| PostgreSQL 12.3, compiled by Visual C++ build 1914, 64-bit, QuestDB |

## hydrate\_table\_metadata('table1', 'table2' ...)[​](#hydrate_table_metadatatable1-table2- "Direct link to hydrate_table_metadata('table1', 'table2' ...)")

`hydrate\_table\_metadata' re-reads table metadata from disk to update the static
metadata cache.

warning

This function should only be used when directed by QuestDB support. Misuse could
cause corruption of the metadata cache, requiring the database to be restarted.

**Arguments:**

A variable list of strings, corresponding to table names.

Alternatively, a single asterisk, '\*', representing all tables.

**Return value:**

Returns `boolean`. `true` if successful, `false` if unsuccessful.

**Examples:**

Simply pass table names as arguments to the function.

```prism-code
SELECT hydrate_table_metadata('trades', 'trips');
```

| hydrate\_table\_metadata |
| --- |
| true |

If you want to re-read metadata for all user tables, simply use an asterisk:

```prism-code
SELECT hydrate_table_metadata('*');
```

## flush\_query\_cache()[​](#flush_query_cache "Direct link to flush_query_cache()")

`flush\_query\_cache' invalidates cached query execution plans.

**Arguments:**

* `flush_query_cache()` does not require arguments.

**Return value:**

Returns `boolean`. `true` if successful, `false` if unsuccessful.

**Examples:**

Flush cached query execution plans

```prism-code
SELECT flush_query_cache();
```

## reload\_config()[​](#reload_config "Direct link to reload_config()")

`reload_config' reloads server configuration file's contents (`server.conf`)
without server restart. The list of reloadable settings can be found
[here](/docs/configuration/overview/#reloadable-settings).

**Arguments:**

* `reload_config()` does not require arguments.

**Return value:**

Returns `boolean`. `true` if any configuration properties were reloaded, `false`
if none were reloaded.

**Examples:**

Edit `server.conf` and run `reload_config`:

Reload server configuration

```prism-code
SELECT reload_config();
```