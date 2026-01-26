On this page

This page describes methods for configuring QuestDB server settings.

Configuration can be set either:

* In the `server.conf` configuration file available in the
  [root directory](/docs/concepts/deep-dive/root-directory-structure/)
* Using environment variables

When a key is absent from both the config file and the environment variables,
the default value is used.

note

**For Windows users**

When entering path values, use either `\\` or `/` instead of the native path
separator char `\`.

* 👍 `C:\\path\\to\\file\\path`
* 👍 `C:/path/to/file`
* 👎 `C:\path\to\file`

The single backslash is interpreted as an escape sequence start within
[Java properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html).

## Environment variables[​](#environment-variables "Direct link to Environment variables")

All settings in the configuration file can be set or overridden using
environment variables. If a key is set in both the `server.conf` file and via an
environment variable, the environment variable will take precedence and the
value in the server configuration file will be ignored.

To make these configuration settings available to QuestDB via environment
variables, they must be in the following format:

```prism-code
QDB_<KEY_OF_THE_PROPERTY>
```

Where `<KEY_OF_THE_PROPERTY>` is equal to the configuration key name. To
properly format a `server.conf` key as an environment variable it must have:

1. `QDB_` prefix
2. uppercase characters
3. all `.` period characters replaced with `_` underscore

For example, the server configuration key for query timeout must be passed as
described below:

| `server.conf` key | env var |
| --- | --- |
| `query.timeout` | `QDB_QUERY_TIMEOUT` |

note

QuestDB applies these configuration changes on startup and a running instance
must be restarted in order for configuration changes to take effect.

### Examples[​](#examples "Direct link to Examples")

The following configuration property customizes the query timeout:

conf/server.conf

```prism-code
query.timeout=120s
```

Customizing the query timeout via environment variable

```prism-code
export QDB_QUERY_TIMEOUT=120s
```

## Reloadable settings[​](#reloadable-settings "Direct link to Reloadable settings")

Certain configuration settings can be reloaded without having to restart the
server. To reload a setting, edit its value in the `server.conf` file and then
run the `reload_config` SQL function:

Reload server configuration

```prism-code
SELECT reload_config();
```

If the value was reloaded successfully, the `reload_config` function returns
`true` and a message is printed to the server log:

```prism-code
2025-01-02T09:52:40.833848UTC I i.q.DynamicPropServerConfiguration reloaded config option [update, key=http.net.connection.limit, old=100, new=200]
```

Each key has a `reloadable` property that indicates whether the key can be
reloaded. If yes, the `reload_config` function can be used to reload the
configuration.

All reloadable properties can be also queried from the server:

Query reloadable properties

```prism-code
(SHOW PARAMETERS) WHERE reloadable = true;
```

## Keys and default values[​](#keys-and-default-values "Direct link to Keys and default values")

This section lists the configuration keys available to QuestDB by topic or
subsystem. Parameters for specifying buffer and memory page sizes are provided
in the format `n<unit>`, where `<unit>` can be one of the following:

* `m` for **MB**
* `k` for **kB**

For example:

Setting maximum send buffer size to 2MB per TCP socket

```prism-code
http.net.connection.sndbuf=2m
```

### Shared worker[​](#shared-worker "Direct link to Shared worker")

QuestDB uses three specialized worker pools to handle different workloads:

* **Network pool**: handles HTTP, PostgreSQL, and ILP server I/O
* **Query pool**: executes parallel query operations (filters, group-by)
* **Write pool**: manages WAL apply jobs, table writes, materialized view refresh, and housekeeping tasks

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| shared.network.worker.count | max(2, CPU count - 2) if CPU count > 32, max(2, CPU count - 1) if CPU count > 16, otherwise max(2, CPU count) | No | Number of worker threads for the network pool, which handles HTTP, PostgreSQL, and ILP server I/O. Increasing this number will increase network I/O parallelism at the expense of CPU resources. |
| shared.network.worker.affinity | none | No | Comma-delimited list of CPU ids, one per thread specified in `shared.network.worker.count`. By default, threads have no CPU affinity. |
| shared.query.worker.count | max(2, CPU count - 2) if CPU count > 32, max(2, CPU count - 1) if CPU count > 16, otherwise max(2, CPU count) | No | Number of worker threads for the query pool, which executes parallel query operations (filters, group-by). Increasing this number will increase query parallelism at the expense of CPU resources. |
| shared.query.worker.affinity | none | No | Comma-delimited list of CPU ids, one per thread specified in `shared.query.worker.count`. By default, threads have no CPU affinity. |
| shared.write.worker.count | max(2, CPU count - 2) if CPU count > 32, max(2, CPU count - 1) if CPU count > 16, otherwise max(2, CPU count) | No | Number of worker threads for the write pool, which manages WAL apply jobs, table writes, materialized view refresh, and housekeeping tasks. Increasing this number will increase write parallelism at the expense of CPU resources. |
| shared.write.worker.affinity | none | No | Comma-delimited list of CPU ids, one per thread specified in `shared.write.worker.count`. By default, threads have no CPU affinity. |
| shared.worker.haltOnError | false | No | Flag that indicates if the worker thread must stop when an unexpected error occurs. |

### HTTP server[​](#http-server "Direct link to HTTP server")

This section describes configuration settings for the
[Web Console](/docs/getting-started/web-console/overview/) and the REST API available by default on port
`9000`. For details on the use of this component, refer to the
[web console documentation](/docs/getting-started/web-console/overview/) page.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| http.enabled | true | No | Enable or disable HTTP server. |
| http.bind.to | 0.0.0.0:9000 | No | IP address and port of HTTP server. A value of `0` means that the HTTP server will bind to all network interfaces. You can specify IP address of any individual network interface on your system. |
| http.user | N/A | No | Username for HTTP Basic Authentication in QuestDB Open Source. QuestDB Enterprise Edition supports more advanced authentication mechanisms: RBAC |
| http.password | N/A | No | Password for HTTP Basic Authentication in QuestDB Open Source. QuestDB Enterprise Edition supports more advanced authentication mechanisms: RBAC |
| http.net.connection.limit | 64 | No | The maximum number permitted for simultaneous TCP connection to the HTTP server. The rationale of the value is to control server memory consumption. |
| http.query.connection.limit | none | No | Soft limit for simultaneous HTTP query connections. When breached, new connections will be rejected but existing connections won't be closed immediately as long as http.net.connection.limit is not exceeded. |
| http.ilp.connection.limit | none | No | Soft limit for simultaneous ILP connections. When breached, new connections will be rejected but existing connections won't be closed immediately as long as http.net.connection.limit is not exceeded. |
| http.net.connection.timeout | 300000 | No | TCP connection idle timeout in milliseconds. Connection is closed by HTTP server when this timeout lapses. |
| http.net.connection.sndbuf | 2M | No | Maximum send buffer size on each TCP socket. If this value is `-1`, the socket send buffer size remains unchanged from the OS defaults. |
| http.net.connection.rcvbuf | 2M | No | Maximum receive buffer size on each TCP socket. If this value is `-1`, the socket receive buffer size remains unchanged from the OS defaults. |
| http.net.connection.hint | false | No | Windows specific flag to overcome OS limitations on TCP backlog size |
| http.net.connection.queue.timeout | 5000 | No | Amount of time in milliseconds a connection can wait in the listen backlog queue before it is refused. Connections will be aggressively removed from the backlog until the active connection limit is breached. |
| http.net.bind.to | 0.0.0.0:9000 | No | IP address and port of HTTP server. |
| http.connection.pool.initial.capacity | 4 | No | Initial size of pool of reusable objects that hold connection state. The pool should be configured to maximum realistic load so that it does not resize at runtime. |
| http.connection.string.pool.capacity | 128 | No | Initial size of the string pool shared by the HTTP header and multipart content parsers. |
| http.multipart.header.buffer.size | 512 | Yes | Buffer size in bytes used by the HTTP multipart content parser. |
| http.multipart.idle.spin.count | 10000 | No | How long the code accumulates incoming data chunks for column and delimiter analysis. |
| http.receive.buffer.size | 1M | Yes | Size of receive buffer. |
| http.request.header.buffer.size | 64K | Yes | Size of internal buffer allocated for HTTP request headers. The value is rounded up to the nearest power of 2. When HTTP requests contain headers that exceed the buffer size server will disconnect the client with HTTP error in server log. |
| http.worker.count | 0 | No | Number of threads in private worker pool. When `0`, HTTP server will be using shared worker pool of the server. Values above `0` switch on private pool. |
| http.worker.affinity |  | No | Comma separated list of CPU core indexes. The number of items in this list must be equal to the worker count. |
| http.worker.haltOnError | false | No | **Changing the default value is strongly discouraged**. Flag that indicates if the worker thread must stop when an unexpected error occurs. |
| http.send.buffer.size | 2M | Yes | Size of the internal send buffer. Larger buffer sizes result in fewer I/O interruptions the server is making at the expense of memory usage per connection. There is a limit of send buffer size after which increasing it stops being useful in terms of performance. 2MB seems to be optimal value. |
| http.static.index.file.name | index.html | No | Name of index file for the Web Console. |
| http.frozen.clock | false | No | Sets the clock to always return zero. This configuration parameter is used for internal testing. |
| http.allow.deflate.before.send | false | No | Flag that indicates if Gzip compression of outgoing data is allowed. |
| http.keep-alive.timeout | 5 | No | Used together with `http.keep-alive.max` to set the value of HTTP `Keep-Alive` response header. This instructs browser to keep TCP connection open. Has to be `0` when `http.version` is set to `HTTP/1.0`. |
| http.keep-alive.max | 10000 | No | See `http.keep-alive.timeout`. Has to be `0` when `http.version` is set to `HTTP/1.0`. |
| http.static.public.directory | public | No | The name of directory for public web site. |
| http.text.date.adapter.pool.capacity | 16 | No | Size of date adapter pool. This should be set to the anticipated maximum number of `DATE` fields a text input can have. The pool is assigned to connection state and is reused alongside of connection state object. |
| http.text.json.cache.limit | 16384 | No | JSON parser cache limit. Cache is used to compose JSON elements that have been broken up by TCP protocol. This value limits the maximum length of individual tag or tag value. |
| http.text.json.cache.size | 8192 | No | Initial size of JSON parser cache. The value must not exceed `http.text.json.cache.limit` and should be set to avoid cache resizes at runtime. |
| http.text.max.required.delimiter.stddev | 0.1222d | No | The maximum standard deviation value for the algorithm that calculates text file delimiter. Usually when text parser cannot recognise the delimiter it will log the calculated and maximum standard deviation for the delimiter candidate. |
| http.text.max.required.line.length.stddev | 0.8 | No | Maximum standard deviation value for the algorithm that classifies input as text or binary. For the values above configured stddev input will be considered binary. |
| http.text.metadata.string.pool.capacity | 128 | No | The initial size of pool for objects that wrap individual elements of metadata JSON, such as column names, date pattern strings and locale values. |
| http.text.roll.buffer.limit | 4M | No | The limit of text roll buffer. See `http.text.roll.buffer.size` for description. |
| http.text.roll.buffer.size | 1024 | No | Roll buffer is a structure in the text parser that holds a copy of a line that has been broken up by TCP. The size should be set to the maximum length of text line in text input. |
| http.text.analysis.max.lines | 1000 | No | Number of lines to read on CSV import for heuristics which determine column names & types. Lower line numbers may detect CSV schemas quicker, but possibly with less accuracy. 1000 lines is the maximum for this value. |
| http.text.lexer.string.pool.capacity | 64 | No | The initial capacity of string fool, which wraps `STRING` column types in text input. The value should correspond to the maximum anticipated number of STRING columns in text input. |
| http.text.timestamp.adapter.pool.capacity | 64 | No | Size of timestamp adapter pool. This should be set to the anticipated maximum number of `TIMESTAMP` fields a text input can have. The pool is assigned to connection state and is reused alongside of connection state object. |
| http.text.utf8.sink.size | 4096 | No | Initial size of UTF-8 adapter sink. The value should correspond the maximum individual field value length in text input. |
| http.json.query.connection.check.frequency | 1000000 | No | **Changing the default value is strongly discouraged**. The value to throttle check if client socket has been disconnected. |
| http.json.query.float.scale | 4 | No | The scale value of string representation of `FLOAT` values. |
| http.json.query.double.scale | 12 | No | The scale value of string representation of `DOUBLE` values. |
| http.query.cache.enabled | true | No | Enable or disable the query cache. Cache capacity is `number_of_blocks * number_of_rows`. |
| http.query.cache.block.count | 4 | No | Number of blocks for the query cache. |
| http.query.cache.row.count | 16 | No | Number of rows for the query cache. |
| http.security.readonly | false | No | Forces HTTP read only mode when `true`, disabling commands which modify the data or data structure, e.g. INSERT, UPDATE, or CREATE TABLE. |
| http.security.max.response.rows | 2^63-1 | No | Limit the number of response rows over HTTP. |
| http.security.interrupt.on.closed.connection | true | No | Switch to enable termination of SQL processing if the HTTP connection is closed. The mechanism affects performance so the connection is only checked after `circuit.breaker.throttle` calls are made to the check method. The mechanism also reads from the input stream and discards it since some HTTP clients send this as a keep alive in between requests, `circuit.breaker.buffer.size` denotes the size of the buffer for this. |
| http.pessimistic.health.check.enabled | false | No | When enabled, the health check returns HTTP 500 for any unhandled errors since the server started. |
| circuit.breaker.throttle | 2000000 | No | Number of internal iterations such as loops over data before checking if the HTTP connection is still open |
| circuit.breaker.buffer.size | 32 | No | Size of buffer to read from HTTP connection. If this buffer returns zero and the HTTP client is no longer sending data, SQL processing will be terminated. |
| http.server.keep.alive | true | No | If set to `false`, the server will disconnect the client after completion of each request. |
| http.version | HTTP/1.1 | No | Protocol version, other supported value is `HTTP/1.0`. |
| http.context.web.console | / | No | Context path for the Web Console. If other REST services remain on the default context paths they will move to the same context path as the Web Console. InfluxDB Line Protocol (ILP) HTTP services are not affected and remain on their default paths. When default context paths are changed, moving the Web Console will not affect the configured paths. QuestDB creates copies of services on the Web Console paths so that both the Web Console and custom services remain operational. |
| http.context.import | /imp | No | Context path of the file import service. |
| http.context.table.status | /chk | No | Context path for the table statusservice used by the Import UI in the Web Console. |
| http.context.export | /exp | No | Context path for the SQL result CSV export service. |
| http.context.settings | /settings | No | Context path for the service which provides server-side settings to the Web Console. |
| http.context.execute | /exec | No | Context path for the SQL execution service. |
| http.context.warnings | /warnings | No | Context path for the Web Console specific service. |
| http.context.ilp | /write,/api/v2/write | No | Context paths for the Influx Line Protocol (ILP) HTTP services. These are not used by the Web Console. |
| http.context.ilp.ping | /ping | No | Context path for the Influx Line Protocol (ILP) ping endpoint. |
| http.redirect.count | 1 | No | Number of HTTP redirects. All redirects are 301 - Moved Permanently. |
| http.redirect.1 | / -> /index.html | No | Example redirect configuration. Format is 'source -> destination'. |

### Cairo engine[​](#cairo-engine "Direct link to Cairo engine")

This section describes configuration settings for the Cairo SQL engine in
QuestDB.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| config.reload.enabled | true | No | When `false`, disables reload\_config() SQL function. |
| query.timeout.sec | 60 | No | A global timeout (in seconds) for long-running queries. Timeout for each query can override the default by setting HTTP header [`Statement-Timeout`](/docs/query/rest-api/#headers) or Postgres [`options`](/docs/query/pgwire/overview/#list-of-supported-connection-properties). |
| cairo.max.uncommitted.rows | 500000 | No | Maximum number of uncommitted rows per table, when the number of pending rows reaches this parameter on a table, a commit will be issued. |
| cairo.o3.max.lag | 10 minutes | No | The maximum size of in-memory buffer in milliseconds. The buffer is allocated dynamically through analyzing the shape of the incoming data, and `o3MaxLag` is the upper limit. |
| cairo.o3.min.lag | 1 second | No | The minimum size of in-memory buffer in milliseconds. The buffer is allocated dynamically through analyzing the shape of the incoming data, and `o3MinLag` is the lower limit. |
| cairo.sql.backup.root | null | No | Output root directory for backups. |
| cairo.sql.backup.dir.datetime.format | null | No | Date format for backup directory. |
| cairo.sql.backup.dir.tmp.name | tmp | No | Name of tmp directory used during backup. |
| cairo.sql.backup.mkdir.mode | 509 | No | Permission used when creating backup directories. |
| cairo.snapshot.instance.id | empty string | No | Instance id to be included into disk snapshots. |
| cairo.snapshot.recovery.enabled | true | No | When `false`, disables snapshot recovery on database start. |
| cairo.root | db | No | Directory for storing db tables and metadata. This directory is inside the server root directory provided at startup. |
| cairo.commit.mode | nosync | No | How changes to table are flushed to disk upon commit. Choices: `nosync`, `async` (flush call schedules update, returns immediately), `sync` (waits for flush on the appended column files to complete). |
| cairo.rnd.memory.max.pages | 128 | No | Sets the max number of pages for memory used by `rnd_` functions. Supports `rnd_str()` and `rnd_symbol()`. |
| cairo.rnd.memory.page.size | 8K | No | Sets the memory page size used by `rnd_` functions. Supports `rnd_str()` and `rnd_symbol()`. |
| cairo.create.as.select.retry.count | 5 | No | Number of types table creation or insertion will be attempted. |
| cairo.default.map.type | fast | No | Type of map used. Options: `fast` (speed at the expense of storage), `compact`. |
| cairo.default.symbol.cache.flag | true | No | When `true`, symbol values will be cached on Java heap instead of being looked up in the database files. |
| cairo.default.symbol.capacity | 256 | No | Specifies approximate capacity for `SYMBOL` columns. It should be equal to number of unique symbol values stored in the table and getting this value badly wrong will cause performance degradation. Must be power of 2. |
| cairo.file.operation.retry.count | 30 | No | Number of attempts to open files. |
| cairo.idle.check.interval | 300000 | No | Frequency of writer maintenance job in milliseconds. |
| cairo.inactive.reader.ttl | 120000 | No | TTL (Time-To-Live) to close inactive readers in milliseconds. |
| cairo.wal.inactive.writer.ttl | 120000 | No | TTL (Time-To-Live) to close inactive WAL writers in milliseconds. |
| cairo.inactive.writer.ttl | 600000 | No | TTL (Time-To-Live) to close inactive writers in milliseconds. |
| cairo.index.value.block.size | 256 | No | Approximation of number of rows for a single index key, must be power of 2. |
| cairo.max.swap.file.count | 30 | No | Number of attempts to open swap files. |
| cairo.mkdir.mode | 509 | No | File permission mode for new directories. |
| cairo.parallel.index.threshold | 100000 | No | Minimum number of rows before allowing use of parallel indexation. |
| cairo.reader.pool.max.segments | 10 | No | Number of segments in the table reader pool. Each segment holds up to 32 readers. |
| cairo.wal.writer.pool.max.segments | 10 | No | Number of segments in the WAL writer pool. Each segment holds up to 32 writers. |
| cairo.spin.lock.timeout | 1000 | No | Timeout when attempting to get BitmapIndexReaders in millisecond. |
| cairo.character.store.capacity | 1024 | No | Size of the CharacterStore. |
| cairo.character.store.sequence.pool.capacity | 64 | No | Size of the CharacterSequence pool. |
| cairo.column.pool.capacity | 4096 | No | Size of the Column pool in the SqlCompiler. |
| cairo.compact.map.load.factor | 0.7 | No | Load factor for CompactMaps. |
| cairo.expression.pool.capacity | 8192 | No | Size of the ExpressionNode pool in SqlCompiler. |
| cairo.fast.map.load.factor | 0.5 | No | Load factor for all FastMaps. |
| cairo.sql.join.context.pool.capacity | 64 | No | Size of the JoinContext pool in SqlCompiler. |
| cairo.lexer.pool.capacity | 2048 | No | Size of FloatingSequence pool in GenericLexer. |
| cairo.sql.map.key.capacity | 2M | No | Key capacity in FastMap and CompactMap. |
| cairo.sql.map.max.resizes | 2^31 | No | Number of map resizes in FastMap and CompactMap before a resource limit exception is thrown, each resize doubles the previous size. |
| cairo.sql.map.page.size | 4m | No | Memory page size for FastMap and CompactMap. |
| cairo.sql.map.max.pages | 2^31 | No | Memory max pages for CompactMap. |
| cairo.model.pool.capacity | 1024 | No | Size of the QueryModel pool in the SqlCompiler. |
| cairo.sql.sort.key.page.size | 4M | No | Memory page size for storing keys in LongTreeChain. |
| cairo.sql.sort.key.max.pages | 2^31 | No | Max number of pages for storing keys in LongTreeChain before a resource limit exception is thrown. |
| cairo.sql.sort.light.value.page.size | 1048576 | No | Memory page size for storing values in LongTreeChain. |
| cairo.sql.sort.light.value.max.pages | 2^31 | No | Max pages for storing values in LongTreeChain. |
| cairo.sql.hash.join.value.page.size | 16777216 | No | Memory page size of the slave chain in full hash joins. |
| cairo.sql.hash.join.value.max.pages | 2^31 | No | Max pages of the slave chain in full hash joins. |
| cairo.sql.latest.by.row.count | 1000 | No | Number of rows for LATEST BY. |
| cairo.sql.hash.join.light.value.page.size | 1048576 | No | Memory page size of the slave chain in light hash joins. |
| cairo.sql.hash.join.light.value.max.pages | 2^31 | No | Max pages of the slave chain in light hash joins. |
| cairo.sql.sort.value.page.size | 16777216 | No | Memory page size of file storing values in SortedRecordCursorFactory. |
| cairo.sql.sort.value.max.pages | 2^31 | No | Max pages of file storing values in SortedRecordCursorFactory. |
| cairo.work.steal.timeout.nanos | 10000 | No | Latch await timeout in nanos for stealing indexing work from other threads. |
| cairo.parallel.indexing.enabled | true | No | Allows parallel indexation. Works in conjunction with cairo.parallel.index.threshold. |
| cairo.sql.join.metadata.page.size | 16384 | No | Memory page size for JoinMetadata file. |
| cairo.sql.join.metadata.max.resizes | 2^31 | No | Number of map resizes in JoinMetadata before a resource limit exception is thrown, each resize doubles the previous size. |
| cairo.sql.analytic.column.pool.capacity | 64 | No | Size of AnalyticColumn pool in SqlParser. |
| cairo.sql.create.table.model.batch.size | 1000000 | No | Batch size for non-atomic CREATE AS SELECT statements. |
| cairo.sql.column.cast.model.pool.capacity | 16 | No | Size of CreateTableModel pool in SqlParser. |
| cairo.sql.rename.table.model.pool.capacity | 16 | No | Size of RenameTableModel pool in SqlParser. |
| cairo.sql.with.clause.model.pool.capacity | 128 | No | Size of WithClauseModel pool in SqlParser. |
| cairo.sql.insert.model.pool.capacity | 64 | No | Size of InsertModel pool in SqlParser. |
| cairo.sql.insert.model.batch.size | 1000000 | No | Batch size for non-atomic INSERT INTO SELECT statements. |
| cairo.sql.copy.model.pool.capacity | 32 | No | Size of CopyModel pool in SqlParser. |
| cairo.sql.copy.buffer.size | 2M | No | Size of buffer used when copying tables. |
| cairo.sql.double.cast.scale | 12 | No | Maximum number of decimal places that types cast as doubles have. |
| cairo.sql.float.cast.scale | 4 | No | Maximum number of decimal places that types cast as floats have. |
| cairo.sql.copy.formats.file | /text\_loader.json | No | Name of file with user's set of date and timestamp formats. |
| cairo.sql.jit.mode | on | No | JIT compilation for SQL queries. May be disabled by setting this value to `off`. |
| cairo.sql.jit.debug.enabled | false | No | Sets debug flag for JIT compilation. When enabled, assembly will be printed into `stdout`. |
| cairo.sql.jit.max.in.list.size.threshold | 10 | No | Controls whether or not JIT compilation will be used for a query that uses the IN predicate. If the IN list is longer than this threshold, JIT compilation will be cancelled. |
| cairo.sql.jit.bind.vars.memory.page.size | 4K | No | Sets the memory page size for storing bind variable values for JIT compiled filter. |
| cairo.sql.jit.bind.vars.memory.max.pages | 8 | No | Sets the max memory pages for storing bind variable values for JIT compiled filter. |
| cairo.sql.jit.page.address.cache.threshold | 1M | No | Sets minimum cache size to shrink page address cache after query execution. |
| cairo.sql.jit.ir.memory.page.size | 8K | No | Sets the memory page size for storing IR for JIT compilation. |
| cairo.sql.jit.ir.memory.max.pages | 8 | No | Sets max memory pages for storing IR for JIT compilation. |
| cairo.sql.page.frame.min.rows | 1000 | No | Sets the minimum number of rows in page frames used in SQL queries. |
| cairo.sql.page.frame.max.rows | 1000000 | No | Sets the maximum number of rows in page frames used in SQL. queries |
| cairo.sql.sampleby.page.size | 0 | No | SampleBy index query page size. Max values returned in single scan. 0 is default, and it means to use symbol block capacity. |
| cairo.sql.sampleby.default.alignment.calendar | 0 | No | SampleBy default alignment behaviour. true corresponds to ALIGN TO CALENDAR, false corresponds to ALIGN TO FIRST OBSERVATION. |
| cairo.date.locale | en | No | The locale to handle date types. |
| cairo.timestamp.locale | en | No | The locale to handle timestamp types. |
| cairo.o3.column.memory.size | 256k | No | Memory page size per column for O3 operations. Please be aware O3 will use 2x of the set value per column (therefore a default of 2x256kb). |
| cairo.writer.data.append.page.size | 16M | No | mmap sliding page size that table writer uses to append data for each column. |
| cairo.writer.data.index.key.append.page.size | 512K | No | mmap page size for appending index key data; key data is number of distinct symbol values times 4 bytes. |
| cairo.writer.data.index.value.append.page.size | 16M | No | mmap page size for appending value data. |
| cairo.writer.misc.append.page.size | 4K | No | mmap page size for mapping small files, default value is OS page size (4k Linux, 64K windows, 16k OSX M1). Overriding this rounds to the nearest (greater) multiple of the OS page size. |
| cairo.writer.command.queue.capacity | 32 | No | Maximum writer ALTER TABLE and replication command capacity. Shared between all the tables. |
| cairo.writer.tick.rows.count | 1024 | No | Row count to check writer command queue after on busy writing, e.g. tick after X rows written. |
| cairo.writer.alter.busy.wait.timeout | 500 | No | Maximum wait timeout in milliseconds for `ALTER TABLE` SQL statement run via REST and PostgreSQL Wire Protocol interfaces when statement execution is `ASYNCHRONOUS`. |
| cairo.sql.column.purge.queue.capacity | 128 | No | Purge column version job queue. Increase the size if column version not automatically cleanup after execution of UPDATE SQL statement. Reduce to decrease initial memory footprint. |
| cairo.sql.column.purge.task.pool.capacity | 256 | No | Column version task object pool capacity. Increase to reduce GC, reduce to decrease memory footprint. |
| cairo.sql.column.purge.retry.delay | 10000 | No | Initial delay (μs) before re-trying purge of stale column files. |
| cairo.sql.column.purge.retry.delay.multiplier | 10.0 | No | Multiplier used to increases retry delay with each iteration. |
| cairo.sql.column.purge.retry.delay.limit | 60000000 | No | Delay limit (μs), upon reaching which, the re-try delay remains constant. |
| cairo.sql.column.purge.retry.limit.days | 31 | No | Number of days purge system will continue to re-try deleting stale column files before giving up. |
| cairo.volumes | - | No | A comma separated list of *alias -> root-path* pairs defining allowed volumes to be used in [CREATE TABLE IN VOLUME](/docs/query/sql/create-table/#table-target-volume) statements. |
| cairo.system.table.prefix | sys. | No | Prefix of the tables used for QuestDB internal data storage. These tables are hidden from QuestDB web console. |
| cairo.wal.enabled.default | true | No | Setting defining whether WAL table is the default when using `CREATE TABLE`. |
| cairo.o3.partition.split.min.size | 50MB | No | The estimated partition size on disk. This setting is one of the conditions to trigger [auto-partitioning](/docs/getting-started/capacity-planning/#auto-partitioning). |
| cairo.o3.last.partition.max.splits | 20 | No | The number of partition pieces allowed before the last partition piece is merged back to the physical partition. |
| cairo.o3.partition.purge.list.initial.capacity | 1 | No | Number of partition expected on average. Initial value for purge allocation job, extended in runtime automatically. |
| cairo.sql.parallel.groupby.enabled | true | No | Enables parallel GROUP BY execution; requires at least 4 shared worker threads. |
| cairo.sql.parallel.groupby.merge.shard.queue.capacity | <auto> | No | Merge queue capacity for parallel GROUP BY; used for parallel tasks that merge shard hash tables. |
| cairo.sql.parallel.groupby.sharding.threshold | 100000 | No | Threshold for parallel GROUP BY to shard the hash table holding the aggregates. |
| cairo.sql.groupby.allocator.default.chunk.size | 128k | No | Default size for memory buffers in GROUP BY function native memory allocator. |
| cairo.sql.groupby.allocator.max.chunk.size | 4gb | No | Maximum allowed native memory allocation for GROUP BY functions. |
| cairo.sql.unordered.map.max.entry.size | 24 | No | Threshold in bytes for switching from single memory buffer hash table (unordered) to a hash table with separate heap for entries (ordered). |
| cairo.sql.window.max.recursion | 128 | No | Prevents stack overflow errors when evaluating complex nested SQLs. The value is an approximate number of nested SELECT clauses. |
| cairo.sql.query.registry.pool.size | <auto> | No | Pre-sizes the internal data structure that stores active query executions. The value is chosen automatically based on the number of threads in the shared worker pool. |
| cairo.sql.analytic.initial.range.buffer.size | 32 | No | Window function buffer size in record counts. Pre-sizes buffer for every windows function execution to contain window records. |
| cairo.system.writer.data.append.page.size | 256k | No | mmap sliding page size that TableWriter uses to append data for each column specifically for System tables. |
| cairo.file.descriptor.cache.enabled | true | No | enables or disables the file-descriptor cache |
| cairo.partition.encoder.parquet.raw.array.encoding.enabled | false | No | determines whether to export arrays in QuestDB-native binary format (true, less compatible) or Parquet-native format (false, more compatible). |
| cairo.partition.encoder.parquet.version | 1 | No | Output parquet version to use for parquet-encoded partitions. Can be 1 or 2. |
| cairo.partition.encoder.parquet.statistics.enabled | true | No | Controls whether or not statistics are included in parquet-encoded partitions. |
| cairo.partition.encoder.parquet.compression.codec | ZSTD | No | Sets the default compression codec for parquet-encoded partitions. Alternatives include `LZ4_RAW`, `SNAPPY`. |
| cairo.partition.encoder.parquet.compression.level | 9 (ZSTD), 0 (otherwise) | No | Sets the default compression level for parquet-encoded partitions. Dependent on underlying compression codec. |
| cairo.partition.encoder.parquet.row.group.size | 100000 | No | Sets the default row-group size for parquet-encoded partitions. |
| cairo.partition.encoder.parquet.data.page.size | 1048576 | No | Sets the default page size for parquet-encoded partitions. |

### WAL table configurations[​](#wal-table-configurations "Direct link to WAL table configurations")

The following WAL tables settings on parallel threads are configurable for
applying WAL data to the table storage:

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| wal.apply.worker.count | equal to the CPU core count | No | Number of dedicated worker threads assigned to handle WAL table data. |
| wal.apply.worker.affinity | equal to the CPU core count | No | Comma separated list of CPU core indexes. |
| wal.apply.worker.haltOnError | false | No | Flag that indicates if the worker thread must stop when an unexpected error occurs. |
| cairo.wal.purge.interval | 30000 | No | Period in ms of how often WAL-applied files are cleaned up from the disk |
| cairo.wal.segment.rollover.row.count | 200000 | No | Row count of how many rows are written to the same WAL segment before starting a new segment. Triggers in conjunction with `cairo.wal.segment.rollover.size` (whichever is first). |
| cairo.wal.squash.uncommitted.rows.multiplier | 20.0 | No | Multiplier to cairo.max.uncommitted.rows to calculate the limit of rows that can be kept invisible when writing to WAL table under heavy load, when multiple transactions are to be applied. It is used to reduce the number Out-Of-Order (O3) commits when O3 commits are unavoidable by squashing multiple commits together. Setting it very low can increase O3 commit frequency and decrease the throughput. Setting it too high may cause excessive memory usage and increase the latency. |
| cairo.wal.max.lag.txn.count | 20 | No | Maximum number of transactions that can be kept invisible when writing to WAL table. Once the number is reached, full commit occurs. If not set, defaults to the rounded value of cairo.wal.squash.uncommitted.rows.multiplier. |
| cairo.wal.apply.parallel.sql.enabled | true | No | When disabled, SQL executed by the WAL apply job will always run single-threaded. |

### COPY settings[​](#copy-settings "Direct link to COPY settings")

#### Import[​](#import "Direct link to Import")

This section describes configuration settings for using `COPY` to import large
CSV files, or export parquet files.

Settings for `COPY FROM` (import):

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| cairo.sql.copy.root | import | No | Input root directory for CSV imports via `COPY` SQL and for Parquet file reading. This path must not overlap with other directory (e.g. db, conf) of running instance, otherwise import may delete or overwrite existing files. Relative paths are resolved against the server root directory. |
| cairo.sql.copy.work.root | null | No | Temporary import file directory. Defaults to `root_directory/tmp` if not set explicitly. |
| cairo.iouring.enabled | true | No | Enable or disable io\_uring implementation. Applicable to newer Linux kernels only. Can be used to switch io\_uring interface usage off if there's a kernel bug affecting it. |
| cairo.sql.copy.buffer.size | 2 MiB | No | Size of read buffers used in import. |
| cairo.sql.copy.log.retention.days | 3 | No | Number of days to keep import messages in `sys.text_import_log`. |
| cairo.sql.copy.max.index.chunk.size | 100M | No | Maximum size of index chunk file used to limit total memory requirements of import. Indexing phase should use roughly `thread_count * cairo.sql.copy.max.index.chunk.size` of memory. |
| cairo.sql.copy.queue.capacity | 32 | No | Size of copy task queue. Should be increased if there's more than 32 import workers. |

**CSV import configuration for Docker**

For QuestDB instances using Docker:

* `cairo.sql.copy.root` must be defined using one of the following settings:
  + The environment variable `QDB_CAIRO_SQL_COPY_ROOT`.
  + The `cairo.sql.copy.root` in `server.conf`.
* The path for the source CSV file is mounted.
* The source CSV file path and the path defined by `QDB_CAIRO_SQL_COPY_ROOT` are
  identical.
* It is optional to define `QDB_CAIRO_SQL_COPY_WORK_ROOT`.

The following is an example command to start a QuestDB instance on Docker, in
order to import a CSV file:

```prism-code
docker run -p 9000:9000 \  
-v "/tmp/questdb:/var/lib/questdb" \  
-v "/tmp/questdb/my_input_root:/var/lib/questdb/questdb_import" \  
-e QDB_CAIRO_SQL_COPY_ROOT=/var/lib/questdb/questdb_import \  
questdb/questdb
```

Where:

* `-v "/tmp/questdb/my_input_root:/var/lib/questdb/questdb_import"`: Defining a
  source CSV file location to be `/tmp/questdb/my_input_root` on local machine
  and mounting it to `/var/lib/questdb/questdb_import` in the container.
* `-e QDB_CAIRO_SQL_COPY_ROOT=/var/lib/questdb/questdb_import`: Defining the
  copy root directory to be `/var/lib/questdb/questdb_import`.

It is important that the two path are identical
(`/var/lib/questdb/questdb_import` in the example).

#### Export[​](#export "Direct link to Export")

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| cairo.sql.copy.export.root | export | No | Root directory for parquet exports via `COPY-TO` SQL. This path must not overlap with other directory (e.g. db, conf) of running instance, otherwise export may delete or overwrite existing files. Relative paths are resolved against the server root directory. |

Parquet export is also generally impacted by query execution and parquet conversion parameters.

If not overridden, the following default setting will be used.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| cairo.partition.encoder.parquet.raw.array.encoding.enabled | false | No | determines whether to export arrays in QuestDB-native binary format (true, less compatible) or Parquet-native format (false, more compatible). |
| cairo.partition.encoder.parquet.version | 1 | No | Output parquet version to use for parquet-encoded partitions. Can be 1 or 2. |
| cairo.partition.encoder.parquet.statistics.enabled | true | No | Controls whether or not statistics are included in parquet-encoded partitions. |
| cairo.partition.encoder.parquet.compression.codec | ZSTD | No | Sets the default compression codec for parquet-encoded partitions. Alternatives include `LZ4_RAW`, `SNAPPY`. |
| cairo.partition.encoder.parquet.compression.level | 9 (ZSTD), 0 (otherwise) | No | Sets the default compression level for parquet-encoded partitions. Dependent on underlying compression codec. |
| cairo.partition.encoder.parquet.row.group.size | 100000 | No | Sets the default row-group size for parquet-encoded partitions. |
| cairo.partition.encoder.parquet.data.page.size | 1048576 | No | Sets the default page size for parquet-encoded partitions. |

### Parallel SQL execution[​](#parallel-sql-execution "Direct link to Parallel SQL execution")

This section describes settings that can affect the level of parallelism during
SQL execution, and therefore can also have an impact on performance.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| cairo.sql.parallel.filter.enabled | true | No | Enable or disable parallel SQL filter execution. JIT compilation takes place only when this setting is enabled. |
| cairo.sql.parallel.filter.pretouch.enabled | true | No | Enable column pre-touch as part of the parallel SQL filter execution, to improve query performance for large tables. |
| cairo.page.frame.shard.count | 4 | No | Number of shards for both dispatch and reduce queues. Shards reduce queue contention between SQL statements that are executed concurrently. |
| cairo.page.frame.reduce.queue.capacity | 64 | No | Reduce queue is used for data processing and should be large enough to supply tasks for worker threads (shared worked pool). |
| cairo.page.frame.rowid.list.capacity | 256 | No | Row ID list initial capacity for each slot of the reduce queue. Larger values reduce memory allocation rate, but increase minimal RSS size. |
| cairo.page.frame.column.list.capacity | 16 | No | Column list capacity for each slot of the reduce queue. Used by JIT-compiled filter functions. Larger values reduce memory allocation rate, but increase minimal RSS size. |

### Postgres wire protocol[​](#postgres-wire-protocol "Direct link to Postgres wire protocol")

This section describes configuration settings for client connections using
PostgresSQL wire protocol.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| pg.enabled | true | No | Configuration for enabling or disabling the Postres interface. |
| pg.net.bind.to | 0.0.0.0:8812 | No | IP address and port of Postgres wire protocol server. 0 means that the server will bind to all network interfaces. You can specify IP address of any individual network interface on your system. |
| pg.net.connection.limit | 64 | Yes | The maximum number permitted for simultaneous Postgres connections to the server. This value is intended to control server memory consumption. |
| pg.net.connection.timeout | 300000 | No | Connection idle timeout in milliseconds. Connections are closed by the server when this timeout lapses. |
| pg.net.connection.rcvbuf | -1 | No | Maximum send buffer size on each TCP socket. If value is -1 socket send buffer remains unchanged from OS default. |
| pg.net.connection.sndbuf | -1 | No | Maximum receive buffer size on each TCP socket. If value is -1, the socket receive buffer remains unchanged from OS default. |
| pg.net.connection.hint | false | No | Windows specific flag to overcome OS limitations on TCP backlog size |
| pg.net.connection.queue.timeout | 300000 | No | Amount of time in milliseconds a connection can wait in the listen backlog queue before it is refused. Connections will be aggressively removed from the backlog until the active connection limit is breached. |
| pg.security.readonly | false | No | Forces PostgreSQL Wire Protocol read only mode when `true`, disabling commands which modify the data or data structure, e.g. INSERT, UPDATE, or CREATE TABLE. |
| pg.character.store.capacity | 4096 | No | Size of the CharacterStore. |
| pg.character.store.pool.capacity | 64 | No | Size of the CharacterStore pool capacity. |
| pg.connection.pool.capacity | 64 | No | The maximum amount of pooled connections this interface may have. |
| pg.password | quest | Yes | Postgres database password. |
| pg.user | admin | Yes | Postgres database username. |
| pg.readonly.user.enabled | false | Yes | Enable or disable Postgres database read-only user account. When enabled, this additional user can be used to open read-only connections to the database. |
| pg.readonly.password | quest | Yes | Postgres database read-only user password. |
| pg.readonly.user | user | Yes | Postgres database read-only user username. |
| pg.select.cache.enabled | true | No | Enable or disable the SELECT query cache. Cache capacity is `number_of_blocks * number_of_rows`. |
| pg.select.cache.block.count | 16 | No | Number of blocks to cache SELECT query execution plan against text to speed up execution. |
| pg.select.cache.row.count | 16 | No | Number of rows to cache for SELECT query execution plan against text to speed up execution. |
| pg.insert.cache.enabled | true | No | Enable or disable the INSERT query cache. Cache capacity is `number_of_blocks * number_of_rows`. |
| pg.insert.cache.block.count | 8 | No | Number of blocks to cache INSERT query execution plan against text to speed up execution. |
| pg.insert.cache.row.count | 8 | No | Number of rows to cache for INSERT query execution plan against text to speed up execution. |
| pg.update.cache.enabled | true | No | Enable or disable the UPDATE query cache. Cache capacity is `number_of_blocks * number_of_rows`. |
| pg.update.cache.block.count | 8 | No | Number of blocks to cache UPDATE query execution plan against text to speed up execution. |
| pg.update.cache.row.count | 8 | No | Number of rows to cache for UPDATE query execution plan against text to speed up execution. |
| pg.max.blob.size.on.query | 512k | No | For binary values, clients will receive an error when requesting blob sizes above this value. |
| pg.recv.buffer.size | 1M | Yes | Size of the buffer for receiving data. |
| pg.send.buffer.size | 1M | Yes | Size of the buffer for sending data. |
| pg.date.locale | en | No | The locale to handle date types. |
| pg.timestamp.locale | en | No | The locale to handle timestamp types. |
| pg.worker.count | 0 | No | Number of dedicated worker threads assigned to handle PostgreSQL Wire Protocol queries. When `0`, the jobs will use the shared pool. |
| pg.worker.affinity |  | No | Comma-separated list of thread numbers which should be pinned for Postgres ingestion. Example `pg.worker.affinity=1,2,3`. |
| pg.halt.on.error | false | No | Whether ingestion should stop upon internal error. |
| pg.daemon.pool | true | No | Defines whether to run all PostgreSQL Wire Protocol worker threads in daemon mode (`true`) or not (`false`). |
| pg.binary.param.count.capacity | 2 | No | Size of the initial capacity for the pool used for binary bind variables. |
| pg.named.statement.limit | 64 | Yes | Size of the named statement pool. |

### InfluxDB Line Protocol (ILP)[​](#influxdb-line-protocol-ilp "Direct link to InfluxDB Line Protocol (ILP)")

This section describes ingestion settings for incoming messages using InfluxDB
Line Protocol.

| Property | Default | Description |
| --- | --- | --- |
| line.default.partition.by | DAY | Table partition strategy to be used with tables that are created automatically by InfluxDB Line Protocol. Possible values are: `HOUR`, `DAY`, `WEEK`, `MONTH`, and `YEAR`. |
| line.auto.create.new.columns | true | When enabled, automatically creates new columns when they appear in the ingested data. When disabled, messages with new columns will be rejected. |
| line.auto.create.new.tables | true | When enabled, automatically creates new tables when they appear in the ingested data. When disabled, messages for non-existent tables will be rejected. |
| line.log.message.on.error | true | Controls whether malformed ILP messages are printed to the server log when errors occur. |

#### HTTP specific settings[​](#http-specific-settings "Direct link to HTTP specific settings")

ILP over HTTP is the preferred way of ingesting data.

| Property | Default | Description |
| --- | --- | --- |
| line.http.enabled | true | Enable ILP over HTTP. Default port is 9000. Enabled by default within open source versions, defaults to false and must be enabled for Enterprise. |
| line.http.ping.version | v2.2.2 | Version information for the ping response of ILP over HTTP. |
| HTTP properties | Various | See [HTTP settings](/docs/configuration/overview/#http-server) for general HTTP configuration. ILP over HTTP inherits from HTTP settings. |

#### TCP specific settings[​](#tcp-specific-settings "Direct link to TCP specific settings")

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| line.tcp.enabled | true | No | Enable or disable line protocol over TCP. |
| line.tcp.net.bind.to | 0.0.0.0:9009 | No | IP address of the network interface to bind listener to and port. By default, TCP receiver listens on all network interfaces. |
| line.tcp.net.connection.limit | 256 | Yes | The maximum number permitted for simultaneous connections to the server. This value is intended to control server memory consumption. |
| line.tcp.net.connection.timeout | 300000 | No | Connection idle timeout in milliseconds. Connections are closed by the server when this timeout lapses. |
| line.tcp.net.connection.hint | false | No | Windows specific flag to overcome OS limitations on TCP backlog size |
| line.tcp.net.connection.rcvbuf | -1 | No | Maximum buffer receive size on each TCP socket. If value is -1, the socket receive buffer remains unchanged from OS default. |
| line.tcp.net.connection.queue.timeout | 5000 | No | Amount of time in milliseconds a connection can wait in the listen backlog queue before its refused. Connections will be aggressively removed from the backlog until the active connection limit is breached. |
| line.tcp.auth.db.path |  | No | Path which points to the authentication db file. |
| line.tcp.connection.pool.capacity | 64 | No | The maximum amount of pooled connections this interface may have. |
| line.tcp.timestamp | n | No | Input timestamp resolution. Possible values are `n`, `u`, `ms`, `s` and `h`. |
| line.tcp.msg.buffer.size | 32768 | No | Size of the buffer read from queue. Maximum size of write request, regardless of the number of measurements. |
| line.tcp.maintenance.job.interval | 1000 | No | Maximum amount of time (in milliseconds) between maintenance jobs committing any uncommitted data on inactive tables. |
| line.tcp.min.idle.ms.before.writer.release | 500 | No | Minimum amount of idle time (in milliseconds) before a table writer is released. |
| line.tcp.commit.interval.fraction | 0.5 | No | Commit lag fraction. Used to calculate commit interval for the table according to the following formula: `commit_interval = commit_lag ∗ fraction`. The calculated commit interval defines how long uncommitted data will need to remain uncommitted. |
| line.tcp.commit.interval.default | 1000 | No | Default commit interval in milliseconds. |
| line.tcp.max.measurement.size | 32768 | No | Maximum size of any measurement. |
| line.tcp.writer.worker.count |  | No | Number of dedicated I/O worker threads assigned to write data to tables. When `0`, the writer jobs will use the shared pool. |
| line.tcp.writer.worker.affinity |  | No | Comma-separated list of thread numbers which should be pinned for line protocol ingestion over TCP. CPU core indexes are 0-based. |
| line.tcp.writer.worker.sleep.threshold | 1000 | No | Amount of subsequent loop iterations with no work done before the worker goes to sleep. |
| line.tcp.writer.worker.yield.threshold | 10 | No | Amount of subsequent loop iterations with no work done before the worker thread yields. |
| line.tcp.writer.queue.capacity | 128 | No | Size of the queue between the IO jobs and the writer jobs, each queue entry represents a measurement. |
| line.tcp.writer.halt.on.error | false | No | Flag that indicates if the worker thread must stop when an unexpected error occurs. |
| line.tcp.io.worker.count |  | No | Number of dedicated I/O worker threads assigned to parse TCP input. When `0`, the writer jobs will use the shared pool. |
| line.tcp.io.worker.affinity |  | No | Comma-separated list of thread numbers which should be pinned for line protocol ingestion over TCP. CPU core indexes are 0-based. |
| line.tcp.io.worker.sleep.threshold | 1000 | No | Amount of subsequent loop iterations with no work done before the worker goes to sleep. |
| line.tcp.io.worker.yield.threshold | 10 | No | Amount of subsequent loop iterations with no work done before the worker thread yields. |
| line.tcp.disconnect.on.error | true | No | Disconnect TCP socket that sends malformed messages. |
| line.tcp.acl.enabled | true | No | Enable or disable Access Control List (ACL) authentication for InfluxDB Line Protocol over TCP. Enterprise only. |

#### UDP specific settings[​](#udp-specific-settings "Direct link to UDP specific settings")

note

The UDP receiver is deprecated since QuestDB version 6.5.2. We recommend ILP
over HTTP instead, or less frequently
[ILP over TCP](/docs/ingestion/ilp/overview/).

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| line.udp.join | 232.1.2.3 | No | Multicast address receiver joins. This values is ignored when receiver is in "unicast" mode. |
| line.udp.bind.to | 0.0.0.0:9009 | No | IP address of the network interface to bind listener to and port. By default UDP receiver listens on all network interfaces. |
| line.udp.commit.rate | 1000000 | No | For packet bursts the number of continuously received messages after which receiver will force commit. Receiver will commit irrespective of this parameter when there are no messages. |
| line.udp.msg.buffer.size | 2048 | No | Buffer used to receive single message. This value should be roughly equal to your MTU size. |
| line.udp.msg.count | 10000 | No | Only for Linux. On Linux, QuestDB will use the `recvmmsg()` system call. This is the max number of messages to receive at once. |
| line.udp.receive.buffer.size | 8388608 | No | UDP socket buffer size. Larger size of the buffer will help reduce message loss during bursts. |
| line.udp.enabled | false | No | Enable or disable UDP receiver. |
| line.udp.own.thread | false | No | When `true`, UDP receiver will use its own thread and busy spin that for performance reasons. "false" makes receiver use worker threads that do everything else in QuestDB. |
| line.udp.own.thread.affinity | -1 | No | -1 does not set thread affinity. OS will schedule thread and it will be liable to run on random cores and jump between the. 0 or higher pins thread to give core. This property is only valid when UDP receiver uses own thread. |
| line.udp.unicast | false | No | When `true`, UDP will use unicast. Otherwise multicast. |
| line.udp.timestamp | n | No | Input timestamp resolution. Possible values are `n`, `u`, `ms`, `s` and `h`. |
| line.udp.commit.mode | nosync | No | Commit durability. Available values are `nosync`, `sync` and `async`. |

### Database replication[​](#database-replication "Direct link to Database replication")

note

Replication is [Enterprise](https://questdb.com/enterprise/) only.

Replication enables high availability clusters.

For setup instructions, see the
[replication operations](/docs/high-availability/setup/) guide.

For an overview of the concept, see the
[replication concept](/docs/high-availability/overview/) page.

For a tuning guide see, the
[replication tuning guide](/docs/high-availability/tuning/).

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| replication.role | none | No | Defaults to `none` for stand-alone instances. To enable replication set to one of: `primary`, `replica`. |
| replication.object.store |  | No | A configuration string that allows connecting to an object store. The format is **scheme::key1=value;key2=value2;…**. The various keys and values are detailed in a later section. Ignored if replication is disabled. No default given variability. |
| cairo.wal.segment.rollover.size | 2097152 | No | The size of the WAL segment before it is rolled over. Default is `2MiB`. However, defaults to `0` unless `replication.role=primary` is set. |
| cairo.writer.command.queue.capacity | 32 | No | Maximum writer ALTER TABLE and replication command capacity. Shared between all the tables. |
| replication.primary.throttle.window.duration | 10000 | No | The millisecond duration of the sliding window used to process replication batches. Default is `10000` ms. |
| replication.requests.max.concurrent | 0 | No | A limit to the number of concurrent object store requests. The default is `0` for unlimited. |
| replication.requests.retry.attempts | 3 | No | Maximum number of times to retry a failed object store request before logging an error and reattempting later after a delay. Default is `3`. |
| replication.requests.retry.interval | 200 | No | How long to wait before retrying a failed operation. Default is `200` ms. |
| replication.primary.compression.threads | calculated | No | Max number of threads used to perform file compression operations before uploading to the object store. The default value is calculated as half the number of CPU cores. |
| replication.primary.compression.level | 1 | No | Zstd compression level. Defaults to `1`. Valid values are from 1 to 22. |
| replication.replica.poll.interval | 1000 | No | Millisecond polling rate of a replica instance to check for the availability of new changes. |
| replication.primary.sequencer.part.txn.count | 5000 | No | Sets the txn chunking size for each compressed batch. Smaller is better for constrained networks (but more costly). |
| replication.primary.checksum=service-dependent | service-dependent | No | Where a checksum should be calculated for each uploaded artifact. Required for some object stores. Other options: never, always |
| replication.primary.upload.truncated | true | No | Skip trailing, empty column data inside a WAL column file. |
| replication.requests.buffer.size | 32768 | No | Buffer size used for object-storage downloads. |
| replication.summary.interval | 1m | No | Frequency for printing replication progress summary in the logs. |
| replication.metrics.per.table | true | No | Enable per-table replication metrics on the prometheus metrics endpoint. |
| replication.metrics.dropped.table.poll.count | 10 | No | How many scrapes of prometheus metrics endpoint before dropped tables will no longer appear. |
| replication.requests.max.batch.size.fast | 64 | No | Number of parallel requests allowed during the 'fast' process (non-resource constrained). |
| replication.requests.max.batch.size.slow | 2 | No | Number of parallel requests allowed during the 'slow' process (error/resource constrained path). |
| replication.requests.base.timeout | 10s | No | Replication upload/download request timeout. |
| replication.requests.min.throughput | 262144 | No | Expected minimum network speed for replication transfers. Used to expand the timeout and account for network delays. |
| native.async.io.threads | cpuCount | No | The number of async (network) io threads used for replication (and in the future cold storage). The default should be appropriate for most use cases. |
| native.max.blocking.threads | cpuCount \* 4 | No | Maximum number of threads for parallel blocking disk IO read/write operations for replication (and other). These threads are ephemeral: They are spawned per need and shut down after a short duration if no longer in use. These are not cpu-bound threads, hence the relative large number. The default should be appropriate for most use cases. |

### Identity and Access Management (IAM)[​](#identity-and-access-management-iam "Direct link to Identity and Access Management (IAM)")

note

Identity and Access Management is available within
[QuestDB Enterprise](https://questdb.com/enterprise/).

Identity and Access Management (IAM) ensures that data can be accessed only by
authorized users. The below configuration properties relate to various
authentication and authorization features.

For a full explanation of IAM, see the
[Identity and Access Management (IAM) documentation](/docs/security/rbac/).

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| acl.enabled | true | No | Enables/disables Identity and Access Management. |
| acl.admin.user.enabled | true | No | Enables/disables the built-in admin user. |
| acl.admin.user | admin | No | Name of the built-in admin user. |
| acl.admin.password | quest | Yes | The password of the built-in admin user. |
| acl.basic.auth.realm.enabled | false | No | When enabled the browser's basic auth popup window is used instead of the Web Console's login screen. Only present for backwards compatibility. |
| acl.entity.name.max.length | 255 | No | Maximum length of user, group and service account names. |
| acl.password.hash.iteration.count | 100000 | No | QuestDB Enterprise never stores passwords in plain text, it stores password hashes only. This is the number of hash iterations used in password hashing. Higher means safer, almost never should be changed. |
| acl.rest.token.refresh.threshold | 10 | No | When a REST token is created in REFRESH mode, its TTL is extended on every successful authentication, unless the last successful authentication was within this threshold. This setting removes unnecessary overhead of continuously refreshing REST tokens if they are used often. The value is expressed in seconds. |
| tls.enabled | false | No | Enables/disables TLS encryption globally for all QuestDB interfaces (HTTP endpoints, ILP over TCP). |
| tls.cert.path |  | No | Path to certificate used for TLS encryption globally. The certificate should be DER-encoded and saved in PEM format. |
| tls.private.key.path |  | No | Path to private key used for TLS encryption globally. |
| http.tls.enabled | false | No | Enables/disables TLS encryption for the HTTP server only. |
| http.tls.cert.path |  | No | Path to certificate used for TLS encryption for the HTTP server only. The certificate should be DER-encoded and saved in PEM format. |
| http.tls.private.key.path |  | No | Path to private key used for TLS encryption for the HTTP server only. |
| http.min.tls.enabled | false | No | Enables/disables TLS encryption for the minimal HTTP server only. |
| http.min.tls.cert.path |  | No | Path to certificate used for TLS encryption for the minimal HTTP server only. The certificate should be DER-encoded and saved in PEM format. |
| http.min.tls.private.key.path |  | No | Path to private key used for TLS encryption for the minimal HTTP server only. |
| line.tcp.tls.enabled | false | No | Enables/disables TLS encryption for ILP over TCP only. |
| line.tcp.tls.cert.path |  | No | Path to certificate used for TLS encryption for ILP over TCP only. The certificate should be DER-encoded and saved in PEM format. |
| line.tcp.tls.private.key.path |  | No | Path to private key used for TLS encryption for ILP over TCP only. |
| line.tcp.acl.enabled | true | No | Enables/disables authentication for the ILP over TCP endpoint only. |

### OpenID Connect (OIDC)[​](#openid-connect-oidc "Direct link to OpenID Connect (OIDC)")

note

OpenID Connect is [Enterprise](https://questdb.com/enterprise/) only.

OpenID Connect (OIDC) support is part of QuestDB's Identity and Access
Management. The database can be integrated with any OAuth2/OIDC Identity
Provider (IdP).

For detailed information about OIDC, see the
[OpenID Connect (OIDC) integration guide](/docs/security/oidc/).

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| acl.oidc.enabled | false | No | Enables/disables OIDC authentication. When enabled, few other configuration options must also be set. |
| acl.oidc.pkce.enabled | true | No | Enables/disables PKCE for the Authorization Code Flow. This should always be enabled in a production environment, the Web Console is not fully secure without it. |
| acl.oidc.ropc.flow.enabled | false | No | Enables/disables Resource Owner Password Credentials flow. When enabled, this flow also has to be configured in the OIDC Provider. |
| acl.oidc.configuration.url |  | No | URL where the OpenID Provider's configuration information cna be loaded in json format, should always end with `/.well-known/openid-configuration`. |
| acl.oidc.host |  | No | OIDC provider hostname. Required when OIDC is enabled, unless the OIDC configuration URL is set. |
| acl.oidc.port | 443 | No | OIDC provider port number. |
| acl.oidc.tls.enabled | true | No | Whether the OIDC provider requires a secure connection or not. It is highly unlikely in a production environment, but if the OpenID Provider endpoints do not require a secure connection, this option can be set to `false`. |
| acl.oidc.tls.validation.enabled | true | No | Enables/disables TLS certificate validation. If you are working with self-signed certificates that you would like QuestDB to trust, disable this option. Validation is strongly recommended in production environments. QuestDB will check that the certificate is valid, and that it is issued for the server to which it connects. |
| acl.oidc.tls.keystore.path |  | No | Path to a keystore file that contains trusted Certificate Authorities. Will be used when validating the certificate of the OIDC provider. Not required if your OIDC provider's certificate is signed by a public CA. |
| acl.oidc.tls.keystore.password |  | No | Keystore password, required if there is a keystore file and it is password protected. |
| acl.oidc.http.timeout | 30000 | No | OIDC provider HTTP request timeout in milliseconds. |
| acl.oidc.client.id |  | No | Client name assigned to QuestDB in the OIDC server, required when OIDC is enabled. |
| acl.oidc.audience |  | No | OAuth2 audience as set on the tokens issued by the OIDC Provider, defaults to the client id. |
| acl.oidc.redirect.uri |  | No | The redirect URI tells the OIDC server where to redirect the user after successful authentication. If not set, the Web Console defaults it to the location where it was loaded from (`window.location.href`). |
| acl.oidc.scope | openid | No | The OIDC server should ask consent for the list of scopes provided in this property. The scope `openid` is mandatory, and always should be included. |
| acl.oidc.public.keys.endpoint | /pf/JWKS | No | JSON Web Key Set (JWKS) Endpoint, the default value should work for the Ping Identity Platform. This endpoint provides the list of public keys can be used to decode and validate ID tokens issued by the OIDC Provider. |
| acl.oidc.authorization.endpoint | /as/authorization.oauth2 | No | OIDC Authorization Endpoint, the default value should work for the Ping Identity Platform. |
| acl.oidc.token.endpoint | /as/token.oauth2 | No | OIDC Token Endpoint, the default value should work for the Ping Identity Platform. |
| acl.oidc.userinfo.endpoint | /idp/userinfo.openid | No | OIDC User Info Endpoint, the default value should work for the Ping Identity Platform. Used to retrieve additional user information which contains the user's group memberships. |
| acl.oidc.groups.encoded.in.token | false | No | Should be set to false, if the OIDC Provider is configured to encode the group memberships of the user into the id token. When set to true, QuestDB will look for the groups in the token instead of calling the User Info endpoint. |
| acl.oidc.sub.claim | sub | No | The name of the claim in the user information, which contains the name of the user. Could be a username, the user's full name or email. It will be displayed in the Web Console, and logged for audit purposes. |
| acl.oidc.groups.claim | groups | No | The name of the custom claim in the user information, which contains the group memberships of the user. |
| acl.oidc.cache.ttl | 30000 | No | User info cache entry TTL (time to live) in milliseconds, default value is 30 seconds. For improved performance QuestDB caches user info responses for each valid access token, this settings drives how often the access token should be validated and the user info updated. |
| acl.oidc.pg.token.as.password.enabled | false | No | When enabled, the PGWire endpoint supports OIDC authentication. The OAuth2 token should be sent in the password field, while the username field should contain the string `_sso`, or left empty if that is an option. |

### Config Validation[​](#config-validation "Direct link to Config Validation")

The database startup phase checks for configuration issues, such as invalid or
deprecated settings. Issues may be classified as advisories or errors. Advisory
issues are [logged](/docs/concepts/deep-dive/root-directory-structure/#log-directory)
without causing the database to stop its startup sequence: These are usually
setting deprecation warnings. Configuration errors can optionally cause the
database to fail its startup.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| config.validation.strict | false | No | When enabled, startup fails if there are configuration errors. |

*We recommended enabling strict validation.*

### Telemetry[​](#telemetry "Direct link to Telemetry")

QuestDB sends anonymous telemetry data with information about usage which helps
us improve the product over time. We do not collect any personally-identifying
information, and we do not share any of this data with third parties.

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| telemetry.enabled | true | No | Enable or disable anonymous usage metrics collection. |
| telemetry.hide.tables | false | No | Hides telemetry tables from `select * from tables()` output. As a result, telemetry tables will not be visible in the Web Console table view. |
| telemetry.queue.capacity | 512 | No | Capacity of the internal telemetry queue, which is the gateway of all telemetry events. This queue capacity does not require tweaking. |

## Materialized views[​](#materialized-views "Direct link to Materialized views")

info

Materialized View support is now generally available (GA) and ready for production use.

If you are using versions earlier than `8.3.1`, we suggest you upgrade at your earliest convenience.

The following settings are available in `server.conf`:

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| cairo.mat.view.enabled | true | No | Enables or disables SQL support and refresh job for materialized views. |
| cairo.mat.view.parallel.sql.enabled | true | No | When disabled, SQL executed by the materialized view refresh job will always run single-threaded. |
| mat.view.refresh.worker.count | 0 | No | Number of dedicated worker threads assigned to refresh materialized views. When `0`, the jobs will use the shared pool. |
| mat.view.refresh.worker.affinity | Equal to the CPU core count | No | Comma separated list of numerical CPU core indexes. |
| mat.view.refresh.worker.haltOnError | false | No | Flag that indicates if the worker thread must stop when an unexpected error occurs. |

## Logging & Metrics[​](#logging--metrics "Direct link to Logging & Metrics")

The following settings are available in `server.conf`:

| Property | Default | Reloadable | Description |
| --- | --- | --- | --- |
| log.level.verbose | false | No | Converts short-hand log level indicators (E, C, I) into long-hand (ERROR, CRITICAL, INFO) |
| log.timezone | UTC | No | Sets the timezone for log timestamps. Can be a timezone ID such as 'Antarctica/McMurdo', 'SystemDefault' to use system timezone, or the default UTC with 'Z' suffix |

Further settings are available in `log.conf`. For more information, and details
of our Prometheus metrics, please visit the
[Logging & Metrics](/docs/operations/logging-metrics/) documentation.