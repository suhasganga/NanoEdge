On this page

This documentation provides aid for those venturing outside of the path laid
down by their language clients.

For the introductory InfluxDB Line Protocol materials, including authentication,
see the [ILP overview](/docs/ingestion/ilp/overview/).

For the the basics of ingestion, instead consult the
[Ingestion overview](/docs/ingestion/overview/).

## Syntax[​](#syntax "Direct link to Syntax")

Each InfluxDB Line Protocol message has to end with a new line `\n` character.

```prism-code
table_name,symbolset columnset timestamp\n
```

| Element | Definition |
| --- | --- |
| `table_name` | Name of the table where QuestDB will write data. |
| `symbolset` | A set of comma-separated `name=value` pairs that will be parsed as symbol columns. |
| `columnset` | A set of comma-separated `name=value` pairs that will be parsed as non-symbol columns. |
| `timestamp` | UNIX timestamp. The default unit is nanosecond and is configurable via `line.tcp.timestamp`. The value will be truncated to microsecond resolution when parsed by QuestDB. |

`name` in the `name=value` pair always corresponds to `column name` in the
table.

## Behavior[​](#behavior "Direct link to Behavior")

* When the `table_name` does not correspond to an existing table, QuestDB will
  create the table on the fly using the name provided. Column types will be
  automatically recognized and assigned based on the data.
* The `timestamp` column is automatically created as
  [designated timestamp](/docs/concepts/designated-timestamp/) with the
  [partition strategy](/docs/concepts/partitions/) set to `DAY`. Alternatively,
  use [CREATE TABLE](/docs/query/sql/create-table/) to create the table with
  a different partition strategy before ingestion.
* When the timestamp is empty, QuestDB will use the server timestamp.

## Generic example[​](#generic-example "Direct link to Generic example")

Let's assume the following data:

| timestamp | symbol | price | amount | side |
| --- | --- | --- | --- | --- |
| 1465839830100400000 | BTC-USD | 61432 | 0.5 | buy |
| 1465839830100600000 | ETH-USD | 3421 | 2.1 | sell |
| 1465839830100700000 | BTC-USD | 61435 | 1.2 | buy |

The line protocol syntax for that table is:

```prism-code
trades,symbol=BTC-USD,side=buy price=61432,amount=0.5 1465839830100400000\n  
trades,symbol=ETH-USD,side=sell price=3421,amount=2.1 1465839830100600000\n  
trades,symbol=BTC-USD,side=buy price=61435,amount=1.2 1465839830100700000\n
```

This would create table similar to this SQL statement and populate it.

```prism-code
CREATE TABLE trades (  
  timestamp TIMESTAMP,  
  symbol SYMBOL,  
  price DOUBLE,  
  amount DOUBLE,  
  side SYMBOL  
) TIMESTAMP(timestamp) PARTITION BY DAY;
```

## Designated timestamp[​](#designated-timestamp "Direct link to Designated timestamp")

### Timestamps[​](#timestamps "Direct link to Timestamps")

Designated timestamp is the trailing value of an InfluxDB Line Protocol message.
It is optional, and when present, is a timestamp in Epoch nanoseconds. When the
timestamp is omitted, the server will insert each message using the system clock
as the row timestamp. See `cairo.timestamp.locale` and `line.tcp.timestamp`
[configuration options](/docs/configuration/overview/).

caution

* While
  [`columnset` timestamp type units](/docs/ingestion/ilp/columnset-types/#timestamp)
  are microseconds, the designated timestamp units are nanoseconds by default,
  and can be overridden via the `line.tcp.timestamp` configuration property.
* The native timestamp format used by QuestDB is a Unix timestamp in microsecond
  resolution; timestamps in nanoseconds will be parsed and truncated to
  microseconds. When the `timestamp_ns` type is used for the designated column, the timestamp will retain the nanosecond precision.
* For HTTP, precision parameters can added to a request. These include `n` or
  `ns` for nanoseconds, `u` or `us` formicroseconds, `ms` for milliseconds, `s`
  for seconds, `m` for minutes and `h` for hours. Otherwise, it will default to
  nanoseconds.

```prism-code
curl -i -XPOST 'http://localhost:9000/write?db=mydb&precision=s' \  
--data-binary 'trades,symbol=BTC-USD price=61432 1465839830100400200'
```

Example of InfluxDB Line Protocol message with desginated timestamp value

```prism-code
tracking,loc=north val=200i 1000000000\n
```

Example of InfluxDB Line Protocol message sans timestamp

```prism-code
tracking,loc=north val=200i\n
```

note

We recommend populating designated timestamp via trailing value syntax above.

It is also possible to populate designated timestamp via `columnset`. Please see
[mixed timestamp](/docs/ingestion/ilp/columnset-types/#timestamp) reference.

## Irregularly-structured data[​](#irregularly-structured-data "Direct link to Irregularly-structured data")

InfluxDB line protocol makes it possible to send data under different shapes.
Each new entry may contain certain tags or fields, and others not. QuestDB
supports on-the-fly data structure changes with minimal overhead. Whilst the
example just above highlights structured data, it is possible for InfluxDB line
protocol users to send data as follows:

```prism-code
trades,symbol=BTC-USD price=61432 1465839830100400000\n  
trades,symbol=BTC-USD price=61435 1465839830100700000\n  
trades,symbol=ETH-USD price=3421,amount=2.1 1465839830100800000\n
```

This would result in the following table:

| timestamp | symbol | price | amount |
| --- | --- | --- | --- |
| 1465839830100400000 | BTC-USD | 61432 | NULL |
| 1465839830100700000 | BTC-USD | 61435 | NULL |
| 1465839830100800000 | ETH-USD | 3421 | 2.1 |

tip

Whilst we offer this function for flexibility, we recommend that users try to
minimize structural changes to maintain operational simplicity.

## Duplicate column names[​](#duplicate-column-names "Direct link to Duplicate column names")

If line contains duplicate column names, the value stored in the table will be
that from the first `name=value` pair on each line. For example:

```prism-code
trade,ticker=USD price=30,price=60 1638202821000000000\n
```

Price `30` is stored, `60` is ignored.

## Name restrictions[​](#name-restrictions "Direct link to Name restrictions")

Table name cannot contain any of the following characters: `\n`, `\r`, `?`, `,`,
`”`, `"`, `\`, `/`, `:`, `)`, `(`, `+`, `*`, `%`, `~`, starting `.`, trailing
`.`, or a non-printable char.

Column name cannot contain any of the following characters: `\n`, `\r`, `?`,
`.`, `,`, `”`, `"`, `\\`, `/`, `:`, `)`, `(`, `+`, `-`, `\*` `%%`, `~`, or a
non-printable char.

Both table name and column names are allowed to have spaces . These spaces
have to be escaped with `\`. For example both of these are valid lines.

```prism-code
trade\ table,ticker=USD price=30,details="Latest price" 1638202821000000000\n
```

```prism-code
trade,symbol\ ticker=USD price=30,details="Latest price" 1638202821000000000\n
```

## Symbolset[​](#symbolset "Direct link to Symbolset")

Area of the message that contains comma-separated set of `name=value` pairs for
symbol columns. For example in a message like this:

```prism-code
trade,ticker=BTCUSD,venue=coinbase price=30,price=60 1638202821000000000\n
```

`symbolset` is `ticker=BTCUSD,venue=coinbase`. Please note the mandatory space
between `symbolset` and `columnset`. Naming rules for columns are subject to
[duplicate rules](#duplicate-column-names) and
[name restrictions](#name-restrictions).

### Symbolset values[​](#symbolset-values "Direct link to Symbolset values")

`symbolset` values are always interpreted as [SYMBOL](/docs/concepts/symbol/).
Parser takes values literally so please beware of accidentally using high
cardinality types such as `9092i` or `1.245667`. This will result in a
significant performance loss due to large mapping tables.

`symbolset` values are not quoted. They are allowed to have special characters,
such as  (space), `=`, `,`, `\n`, `\r` and `\`, which must be escaped with a
`\`. Example:

```prism-code
trade,ticker=BTC\\USD\,All,venue=coin\ base price=30 1638202821000000000\n
```

Whenever `symbolset` column does not exist, it will be added on-the-fly with
type `SYMBOL`. On other hand when the column does exist, it is expected to be of
`SYMBOL` type, otherwise the line is rejected.

## Columnset[​](#columnset "Direct link to Columnset")

Area of the message that contains comma-separated set of `name=value` pairs for
non-symbol columns. For example in a message like this:

```prism-code
trade,ticker=BTCUSD priceLow=30,priceHigh=60 1638202821000000000\n
```

`columnset` is `priceLow=30,priceHigh=60`. Naming rules for columns are subject
to [duplicate rules](#duplicate-column-names) and
[name restrictions](#name-restrictions).

### Columnset values[​](#columnset-values "Direct link to Columnset values")

`columnset` supports several values types, which are used to either derive type
of new column or mapping strategy when column already exists. These types are
limited by existing InfluxDB Line Protocol specification. Wider QuestDB type
system is available by creating table via SQL upfront. The following are
supported value types:
[Integer](/docs/ingestion/ilp/columnset-types/#integer),
[Long256](/docs/ingestion/ilp/columnset-types/#long256),
[Float](/docs/ingestion/ilp/columnset-types/#float),
[String](/docs/ingestion/ilp/columnset-types/#string) and
[Timestamp](/docs/ingestion/ilp/columnset-types/#timestamp)

## Inserting NULL values[​](#inserting-null-values "Direct link to Inserting NULL values")

To insert a NULL value, skip the column (or symbol) for that row.

For example:

```prism-code
table1 a=10.5 1647357688714369403  
table1 b=1.25 1647357698714369403
```

Will insert as:

| a | b | timestamp |
| --- | --- | --- |
| 10.5 | *NULL* | 2022-03-15T15:21:28.714369Z |
| *NULL* | 1.25 | 2022-03-15T15:21:38.714369Z |

## InfluxDB Line Protocol Datatypes and Casts[​](#influxdb-line-protocol-datatypes-and-casts "Direct link to InfluxDB Line Protocol Datatypes and Casts")

### Varchar vs Symbols[​](#varchar-vs-symbols "Direct link to Varchar vs Symbols")

Strings may be recorded as either the `VARCHAR` type or the `SYMBOL` type.

Inspecting a sample message we can see how a space `' '` separator splits
`SYMBOL` columns to the left from the rest of the columns.

```prism-code
table_name,col1=symbol_val1,col2=symbol_val2 col3="varchar val",col4=10.5  
                                            ┬  
                                            ╰───────── separator
```

In this example, columns `col1` and `col2` are strings written to the database
as `SYMBOL`s, whilst `col3` is written out as a `VARCHAR`.

`SYMBOL`s are strings which are automatically
[interned](https://en.wikipedia.org/wiki/String_interning) by the database on a
per-column basis. You should use this type if you expect the string to be
re-used over and over, such as is common with identifiers.

For one-off strings use `VARCHAR` columns which aren't interned.

### Casts[​](#casts "Direct link to Casts")

QuestDB types are a superset of those supported by InfluxDB Line Protocol. This
means that when sending data you should be aware of the performed conversions.

See:

* [QuestDB Types in SQL](/docs/query/datatypes/overview/)
* [InfluxDB Line Protocol types and cast conversion tables](/docs/ingestion/ilp/columnset-types/)

## Constructing well-formed messages[​](#constructing-well-formed-messages "Direct link to Constructing well-formed messages")

Different library implementations will perform different degrees of content
validation upfront before sending messages out. To avoid encountering issues,
follow these guidelines:

* **All strings must be UTF-8 encoded.**
* **Each column should only be specified once per row..**
* **Symbol columns must be written out before other columns.**
* **Table and column names can't have invalid characters.** These should not
  contain `?`, `.`,`,`, `'`, `"`, `\`, `/`, `:`, `(`, `)`, `+`, `-`, `*`, `%`,
  `~`,`' '` (space), `\0` (nul terminator),
  [ZERO WIDTH NO-BREAK SPACE](https://unicode-explorer.com/c/FEFF).
* **Write timestamp column via designated API**, or at the end of the message if
  you are using raw sockets. If you have multiple timestamp columns write
  additional ones as column values.
* **Don't change column type between rows.**

## Error handling[​](#error-handling "Direct link to Error handling")

QuestDB will always log any InfluxDB Line Protocol errors in its
[server logs](/docs/concepts/deep-dive/root-directory-structure/#log-directory).

It is recommended that sending applications reuse TCP connections. If QuestDB
receives an invalid message, it will discard invalid lines, produce an error
message in the logs and forcibly *disconnect* the sender to prevent further data
loss.

Data may be discarded because of:

* missing new line characters at the end of messages
* an invalid data format such as unescaped special characters
* invalid column / table name characters
* schema mismatch with existing tables
* message size overflows on the input buffer
* system errors such as no space left on the disk

Detecting malformed input can be achieved through QuestDB logs by searching for
`LineTcpMeasurementScheduler` and `LineTcpConnectionContext`, for example:

```prism-code
2022-02-03T11:01:51.007235Z I i.q.c.l.t.LineTcpMeasurementScheduler could not create table [tableName=trades, ex=`column name contains invalid characters [colName=trade_%]`, errno=0]
```

The following input is tolerated by QuestDB:

* a column is specified twice or more on the same line, QuestDB will pick the
  first occurrence and ignore the rest
* missing columns, their value will be defaulted to `null`/`0.0`/`false`
  depending on the type of the column
* missing designated timestamp, the current server time will be used to generate
  the timestamp
* the timestamp is specified as a column instead of appending it to the end of
  the line
* timestamp appears as a column and is also present at the end of the line, the
  value sent as a field will be used

With sufficient client-side validation, the lack of errors to the client and
confirmation isn't necessarily a concern: QuestDB will log out any issues and
disconnect on error. The database will process any valid lines up to that point
and insert rows.

To resume WAL table ingestion after recovery from errors, see
[ALTER TABLE RESUME WAL](/docs/query/sql/alter-table-resume-wal/) for more
information.

### If you don't immediately see data[​](#if-you-dont-immediately-see-data "Direct link to If you don't immediately see data")

If you don't see your inserted data, this is usually a result of one of two
things:

* You prepared the messages, but forgot to call `.flush()` or similar in your
  client library, so no data was sent.
* The internal timers and buffers within QuestDB did not commit the data yet.
  For development (and development only), you may want to tweak configuration
  settings to commit data more frequently.

  ```prism-code
  cairo.max.uncommitted.rows=1
  ```

  Refer to
  [InfluxDB Line Protocol's configuration](/docs/configuration/overview/#influxdb-line-protocol-ilp)
  documentation for more on these configuration settings.