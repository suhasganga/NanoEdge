# Sending Data over ILP[¶](#sending-data-over-ilp "Link to this heading")

## Overview[¶](#overview "Link to this heading")

The [`Sender`](api.html#questdb.ingress.Sender "questdb.ingress.Sender") class is a client that inserts
rows into QuestDB via the
[ILP protocol](https://questdb.com/docs/reference/api/ilp/overview/), with
support for both ILP over TCP and the newer and recommended ILP over HTTP.
The sender also supports TLS and authentication.

```
from questdb.ingress import Sender, TimestampNanos
import pandas as pd

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    # Adding by rows
    sender.row(
        'trades',
        symbols={'symbol': 'ETH-USD', 'side': 'sell'},
        columns={'price': 2615.54, 'amount': 0.00044},
        at=TimestampNanos.now())
    # It is highly recommended to auto-flush or to flush in batches,
    # rather than for every row
    sender.flush()

    # Whole dataframes at once
    df = pd.DataFrame({
        'symbol': pd.Categorical(['ETH-USD', 'BTC-USD']),
        'side': pd.Categorical(['sell', 'sell']),
        'price': [2615.54, 39269.98],
        'amount': [0.00044, 0.001],
        'timestamp': pd.to_datetime(['2021-01-01', '2021-01-02'])})

    sender.dataframe(df, table_name='trades', at='timestamp')
```

The `Sender` object holds an internal buffer which will be flushed and sent
at when the `with` block ends.

You can read more on [Preparing Data](#sender-preparing-data) and [Flushing](#sender-flushing).

## Constructing the Sender[¶](#constructing-the-sender "Link to this heading")

### From Configuration[¶](#from-configuration "Link to this heading")

The `Sender` class is generally initialized from a
[configuration string](conf.html#sender-conf).

```
from questdb.ingress import Sender

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    ...
```

See the [Configuration](conf.html#sender-conf) guide for more details.

### From Env Variable[¶](#from-env-variable "Link to this heading")

You can also initialize the sender from an environment variable:

```
export QDB_CLIENT_CONF='http::addr=localhost:9000;'
```

The content of the environment variable is the same
[configuration string](conf.html#sender-conf) as taken by the
[`Sender.from_conf`](api.html#questdb.ingress.Sender.from_conf "questdb.ingress.Sender.from_conf") method,
but moving it to an environment variable is more secure and allows you to avoid
hardcoding sensitive information such as passwords and tokens in your code.

```
from questdb.ingress import Sender

with Sender.from_env() as sender:
    ...
```

### Programmatic Construction[¶](#programmatic-construction "Link to this heading")

If you prefer, you can also construct the sender programmatically.
See [Programmatic Construction](#sender-programmatic-construction).

## Preparing Data[¶](#preparing-data "Link to this heading")

### Appending Rows[¶](#appending-rows "Link to this heading")

You can append as many rows as you like by calling the
[`Sender.row`](api.html#questdb.ingress.Sender.row "questdb.ingress.Sender.row") method. The full method arguments are
documented in the [`Buffer.row`](api.html#questdb.ingress.Buffer.row "questdb.ingress.Buffer.row") method.

### Appending Pandas Dataframes[¶](#appending-pandas-dataframes "Link to this heading")

The sender can also append data from a Pandas dataframe.

This is [orders of magnitude](https://github.com/questdb/py-tsbs-benchmark/blob/main/README.md)
faster than appending rows one by one.

```
from questdb.ingress import Sender, IngressError

import sys
import pandas as pd

def example(host: str = 'localhost', port: int = 9000):
    df = pd.DataFrame({
            'symbol': pd.Categorical(['ETH-USD', 'BTC-USD']),
            'side': pd.Categorical(['sell', 'sell']),
            'price': [2615.54, 39269.98],
            'amount': [0.00044, 0.001],
            'timestamp': pd.to_datetime(['2021-01-01', '2021-01-02'])})
    try:
        with Sender.from_conf(f"http::addr={host}:{port};") as sender:
            sender.dataframe(
                df,
                table_name='trades',  # Table name to insert into.
                symbols=['symbol', 'side'],  # Columns to be inserted as SYMBOL types.
                at='timestamp')  # Column containing the designated timestamps.

    except IngressError as e:
        sys.stderr.write(f'Got error: {e}\n')

if __name__ == '__main__':
    example()
```

For more details see [`Sender.dataframe`](api.html#questdb.ingress.Sender.dataframe "questdb.ingress.Sender.dataframe")
and for full argument options see
[`Buffer.dataframe`](api.html#questdb.ingress.Buffer.dataframe "questdb.ingress.Buffer.dataframe").

### String vs Symbol Columns[¶](#string-vs-symbol-columns "Link to this heading")

QuestDB has a concept of symbols which are a more efficient way of storing
categorical data (identifiers). Internally, symbols are deduplicated and
stored as integers.

When sending data, you can specify a column as a symbol by using the
`symbols` parameter of the `row` or `dataframe` methods.

Alternatively, if a column is expected to hold a collection of one-off strings,
you can use the `strings` parameter.

Here is an example of sending a row with a symbol and a string:

```
from questdb.ingress import Sender, TimestampNanos
import datetime

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.row(
        'trades',
        symbols={
            'symbol': 'ETH-USD', 'side': 'sell'},
        columns={
            'price': 2615.54,
            'amount': 0.00044}
        at=datetime.datetime(2021, 1, 1, 12, 0, 0))
```

### Decimal Columns[¶](#decimal-columns "Link to this heading")

Starting with QuestDB server version 9.2.0, you can ingest data into the
database’s native `DECIMAL(precision, scale)` column type. This is useful when
you need exact precision for financial calculations or other scenarios where
floating-point rounding errors are unacceptable.

Decimal ingestion requires [protocol version 3](conf.html#sender-conf-protocol-version)
(must be [configured explicitly for TCP/TCPS](conf.html#sender-conf-protocol-version)).
Unlike other column types, `DECIMAL` columns cannot be auto-created and must be
[pre-created](troubleshooting.html#troubleshooting-decimal) with the appropriate
`DECIMAL(precision, scale)` definition. See the
[QuestDB DECIMAL documentation](https://questdb.com/docs/reference/sql/datatypes/#decimal)
and [troubleshooting guide](troubleshooting.html#troubleshooting-flushing) for more details.

To send decimal values, use Python’s [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") type in the
`row` method or pandas DataFrames:

```
from decimal import Decimal
from questdb.ingress import Sender, TimestampNanos
import pandas as pd

# CREATE TABLE prices (
#     symbol SYMBOL,
#     price DECIMAL(18, 6),
#     timestamp TIMESTAMP_NS
# ) TIMESTAMP(timestamp) PARTITION BY DAY;

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.row(
        'prices',
        symbols={'symbol': 'BTC-USD'},
        columns={'price': Decimal('50123.456789')},
        at=TimestampNanos.now())

    df = pd.DataFrame({
        'symbol': ['BTC-USD', 'ETH-USD'],
        'price': [Decimal('50123.456789'), Decimal('2615.123456')]
    })
    sender.dataframe(df, table_name='prices', symbols=['symbol'],
                    at=TimestampNanos.now())
```

When using pandas DataFrames, you can also use PyArrow decimal types for better
performance:

```
import pyarrow as pa

df = pd.DataFrame({
    'symbol': ['BTC-USD', 'ETH-USD'],
    'price': pd.Series([50123.456789, 2615.123456],
                      dtype=pd.ArrowDtype(pa.decimal128(12, 6)))
})
```

### Populating Designated Timestamps[¶](#populating-designated-timestamps "Link to this heading")

The `at` parameter of the `row` and `dataframe` methods is used to specify
the [designated timestamp](https://questdb.com/docs/concept/designated-timestamp/)
of the rows. The designated timestamp column determines the order in which data
is stored as rows and is used for
partitioning <https://questdb.com/docs/concept/partitions/>.

#### Set by client[¶](#set-by-client "Link to this heading")

It can be either a [`TimestampNanos`](api.html#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos")
object, a [`TimestampMicros`](api.html#questdb.ingress.TimestampMicros "questdb.ingress.TimestampMicros") object or a
[datetime.datetime](https://docs.python.org/3/library/datetime.html) object.

In case of dataframes you can also specify the timestamp column name or index.
If so, the column type should be a Pandas `datetime64`, with or without
timezone information.

QuestDB stores timestamps as either microseconds (`TIMESTAMP` QuestDB column
type) or nanoseconds (`TIMESTAMP_NS` QuestDB column type) as a numeric value
from unix epoch in UTC. Any timezone information is dropped when sent to
the database.

Note

Nanosecond timestamp support is only available from QuestDB 9.1.0 onwards.

#### Set by server[¶](#set-by-server "Link to this heading")

If you prefer, you can specify `at=ServerTimestamp` which will instruct
QuestDB to set the timestamp on your behalf for each row as soon as it’s
received by the server.

```
from questdb.ingress import Sender, ServerTimestamp

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.row(
        'trades',
        symbols={'symbol': 'ETH-USD', 'side': 'sell'},
        columns={'price': 2615.54, 'amount': 0.00044},
        at=ServerTimestamp)  # Legacy feature, not recommended.
```

Warning

Using `ServerTimestamp` is not recommended as it removes the ability
for QuestDB to deduplicate rows and is considered a *legacy feature*.

## Flushing[¶](#flushing "Link to this heading")

The sender accumulates data into an internal buffer. Calling
[`Sender.flush`](api.html#questdb.ingress.Sender.flush "questdb.ingress.Sender.flush") will send the buffered data
to QuestDB, and clear the buffer.

Flushing can be done explicitly or automatically.

### Explicit Flushing[¶](#explicit-flushing "Link to this heading")

An explicit call to [`Sender.flush`](api.html#questdb.ingress.Sender.flush "questdb.ingress.Sender.flush") will
send any pending data immediately.

```
conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.row(
        'trades',
        symbols={'symbol': 'ETH-USD', 'side': 'sell'},
        columns={'price': 2615.54, 'amount': 0.00044},
        at=TimestampNanos.now())
    sender.flush()
    sender.row(
        'trades',
        symbols={'symbol': 'BTC-USD', 'side': 'sell'},
        columns={'price': 39269.98, 'amount': 0.001},
        at=TimestampNanos.now())
    sender.flush()
```

Note that the last sender.flush() is entirely optional as flushing
also happens at the end of the `with` block.

### Auto-flushing[¶](#auto-flushing "Link to this heading")

To avoid accumulating very large buffers, the sender will - by default -
occasionally flush the buffer automatically.

Auto-flushing is triggered when:

* appending a row to the internal sender buffer
* and the buffer either:

  > + Reaches 75’000 rows (for HTTP) or 600 rows (for TCP).
  > + Hasn’t been flushed for 1 second (there are no timers).

Here is an example [configuration string](conf.html#sender-conf) that auto-flushes
sets up a sender to flush every 10 rows and disables
the interval-based auto-flushing logic.

`http::addr=localhost:9000;auto_flush_rows=10;auto_flush_interval=off;`

Here is a configuration string with auto-flushing
completely disabled:

`http::addr=localhost:9000;auto_flush=off;`

See the [Auto-flushing](conf.html#sender-conf-auto-flush) section for more details. and note that
`auto_flush_interval` [does NOT start a timer](conf.html#sender-conf-auto-flush-interval).

## Error Reporting[¶](#error-reporting "Link to this heading")

**TL;DR: Use HTTP for better error reporting**

The sender will do its best to check for errors before sending data to the
server.

When using the HTTP protocol, the server will send back an error message if
the data is invalid or if there is a problem with the server. This will be
raised as an [`IngressError`](api.html#questdb.ingress.IngressError "questdb.ingress.IngressError") exception.

The HTTP layer will also attempt retries, configurable via the
[retry\_timeout](conf.html#sender-conf-request) parameter.`

When using the TCP protocol errors are *not* sent back from the server and
must be searched for in the logs. See the [Errors during flushing](troubleshooting.html#troubleshooting-flushing)
section for more details.

## HTTP Transactions[¶](#http-transactions "Link to this heading")

When using the HTTP protocol, the sender can be configured to send a batch of
rows as a single transaction.

**Transactions are limited to a single table.**

```
conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    with sender.transaction('weather_sensor') as txn:
        txn.row(
            'trades',
            symbols={'symbol': 'ETH-USD', 'side': 'sell'},
            columns={'price': 2615.54, 'amount': 0.00044},
            at=TimestampNanos.now())
        txn.row(
            'trades',
            symbols={'symbol': 'BTC-USD', 'side': 'sell'},
            columns={'price': 39269.98, 'amount': 0.001},
            at=TimestampNanos.now())
```

If auto-flushing is enabled, any pending data will be flushed before the
transaction is started.

Auto-flushing is disabled during the scope of the transaction.

The transaction is automatically completed a the end
of the `with` block.

* If the there are no errors, the transaction is committed and sent to the
  server without delays.
* If an exception is raised with the block, the transaction is rolled back and
  the exception is propagated.

You can also terminate a transaction explicity by calling the
[`commit`](api.html#questdb.ingress.SenderTransaction.commit "questdb.ingress.SenderTransaction.commit") or the
[`rollback`](api.html#questdb.ingress.SenderTransaction.rollback "questdb.ingress.SenderTransaction.rollback") methods.

While transactions that span multiple tables are not supported by QuestDB, you
can reuse the same sender for mutliple tables.

You can also create parallel transactions by creating multiple sender objects
across multiple threads.

## Table and Column Auto-creation[¶](#table-and-column-auto-creation "Link to this heading")

When sending data to a table that does not exist, the server will
create the table automatically.

This also applies to columns that do not exist.

The server will use the first row of data to determine the column types.

If the table already exists, the server will validate that the columns match
the existing table.

If you’re using QuestDB enterprise you might need to grant further permissions
to the authenticated user.

```
CREATE SERVICE ACCOUNT ingest;
GRANT ilp, create table TO ingest;
GRANT add column, insert ON all tables TO ingest;
--  OR
GRANT add column, insert ON table1, table2 TO ingest;
```

Read more setup details in the
[Enterprise quickstart](https://questdb.com/docs/guides/enterprise-quick-start/#4-ingest-data-influxdb-line-protocol)
and the [role-based access control](https://questdb.com/docs/operations/rbac/) guides.

## Good Practices[¶](#good-practices "Link to this heading")

### Create tables in advance[¶](#create-tables-in-advance "Link to this heading")

If you’re not happy with the default [table auto creation](#sender-auto-creation)
logic, create the tables in advance. This will allow you to:

* Specify the column types explicitly.
* Configure de-duplication rules for the table.

### Specify your own timestamps[¶](#specify-your-own-timestamps "Link to this heading")

Always specify your own timestamps using the `at` parameter.

If you use the `ServerTimestamp` option, QuestDB will not be able to
deduplicate rows, should you ever need to send them again.

Instead, if you don’t have an a timestamp immediately available, use
`TimestampNanos.now()` to set the timestamp to the current time.

This is lighter-weight than using a fully-fledged `datetime.datetime` object.

### Prefer ILP/HTTP[¶](#prefer-ilp-http "Link to this heading")

Use the ILP/HTTP protocol instead of ILP/TCP for better error reporting and
transaction control.

### Reuse Sender Objects[¶](#reuse-sender-objects "Link to this heading")

Create longer-lived sender objects, as these are not automatically pooled.

Instead of creating a new sender object for every request, create a single
sender object and reuse it across multiple requests.

```
from questdb.ingress import Sender

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    # Use the sender object for multiple requests
    sender.row(...)
    sender.row(...) # remember auto-flush may trigger after any row
    sender.row(...)
    sender.flush() # you can flush explicitly at any point too
    # ...
    sender.row(...)
    sender.dataframe(...) # auto-flush may trigger within a dataframe too
    sender.flush()
```

### Use transactions[¶](#use-transactions "Link to this heading")

Use [transactions](#sender-transaction) if you want to ensure that a group
of rows is sent as a single transaction.

This feature will guarantee that the rows are sent to the server as one,
even if you’re using auto-flushing.

### Tune for Performance[¶](#tune-for-performance "Link to this heading")

If you need better performance:

* Tune for larger batches of rows. Tweak the auto-flush settings, or
  call [`Sender.flush`](api.html#questdb.ingress.Sender.flush "questdb.ingress.Sender.flush") less frequently.
* Use the [`Sender.dataframe`](api.html#questdb.ingress.Sender.dataframe "questdb.ingress.Sender.dataframe") method To
  send dataframes instead of appending rows one by one.
* Try multi-threading: The `Sender` logic is designed to release the Python
  GIL whenever possible, so you should notice an uplift in performance if you
  were bottlenecked by network I/O.
* Avoid sending data which is very much out of order: The server will re-order
  data by timestamp as it arrives. This is generally cheap for data that only
  affects the recent past, but if you are sending data that is very much out of
  order (for example, from different days), you may want to consider
  re-ordering it before sending. For bulk data uploads of historical data,
  consider using the [CSV import](https://questdb.com/docs/guides/import-csv)
  feature for best performance.

## Advanced Usage[¶](#advanced-usage "Link to this heading")

### Independent Buffers[¶](#independent-buffers "Link to this heading")

All examples so far have shown appending data to the sender’s internal buffer.

You can also create independent buffers and send them independently.

This is useful for more complex applications whishing to decouple the
serialisation logic from the sending logic.

Note that the sender’s auto-flushing logic will not apply to independent
buffers.

```
from questdb.ingress import Buffer, Sender, TimestampNanos

buf = Buffer()
buf.row(
    'trades',
    symbols={'symbol': 'ETH-USD', 'side': 'sell'},
    columns={'price': 2615.54, 'amount': 0.00044},
    at=TimestampNanos.now())
buf.row(
    'trades',
    symbols={'symbol': 'BTC-USD', 'side': 'sell'},
    columns={'price': 39269.98, 'amount': 0.001},
    at=TimestampNanos.now())

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.flush(buf, transactional=True)
```

The `transactional` parameter is optional and defaults to `False`.
When set to `True`, the buffer is guaranteed to be committed as a single
transaction, but must only contain rows for a single table.

You should not mix using a transaction block with flushing an independent buffer transactionally.

### Multiple Databases[¶](#multiple-databases "Link to this heading")

Handling buffers explicitly is also useful when sending data to multiple
databases via the `.flush(buf, clear=False)` option.

```
from questdb.ingress import Buffer, Sender, TimestampNanos

buf = Buffer()
buf.row(
    'trades',
    symbols={'symbol': 'ETH-USD', 'side': 'sell'},
    columns={'price': 2615.54, 'amount': 0.00044},
    at=TimestampNanos.now())

conf1 = 'http::addr=db1.host.com:9000;'
conf2 = 'http::addr=db2.host.com:9000;'
with Sender.from_conf(conf1) as sender1, Sender.from_conf(conf2) as sender2:
    sender1.flush(buf1, clear=False)
    sender2.flush(buf2, clear=False)

buf.clear()
```

This uses the `clear=False` parameter which otherwise defaults to `True`.

### Threading Considerations[¶](#threading-considerations "Link to this heading")

Neither buffer API nor the sender object are thread-safe, but can be shared
between threads if you take care of exclusive access (such as using a lock)
yourself.

Independent buffers also allows you to prepare separate buffers in different
threads and then send them later through a single exclusively locked sender.

Alternatively you can also create multiple senders, one per thread.

Notice that the `questdb` python module is mostly implemented in native code
and is designed to release the Python GIL whenever possible, so you can expect
good performance in multi-threaded scenarios.

As an example, appending a dataframe to a buffer releases the GIL (unless any
of the columns reference python objects).

All network activity also fully releases the GIL.

### Optimising HTTP Performance[¶](#optimising-http-performance "Link to this heading")

The sender’s network communication is implemented in native code and thus does
not require access to the GIL, allowing for true parallelism when used using
multiple threads.

For simplicity of design and best error feedback, the .flush() method blocks
until the server has acknowledged the data.

If you need to send a large number of smaller requests (in other words, if you
need to flush very frequently) or are in a high-latency network, you
can significantly improve performance by creating and sending using multiple
sender objects in parallel.

```
from questdb.ingress import Sender, TimestampNanos
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import datetime

def send_data(df):
    conf_string = 'http::addr=localhost:9000;'
    with Sender.from_conf(conf_string) as sender:
        sender.dataframe(
            df,
            table_name='trades',
            symbols=['symbol', 'side'],
            at='timestamp')

dfs = [
        pd.DataFrame({
        'symbol': pd.Categorical(['ETH-USD', 'BTC-USD']),
        'side': pd.Categorical(['sell', 'sell']),
        'price': [2615.54, 39269.98],
        'amount': [0.00044, 0.001],
        'timestamp': pd.to_datetime(['2021-01-01', '2021-01-02'])}
        ),
        pd.DataFrame({
        'symbol': pd.Categorical(['BTC-USD', 'BTC-USD']),
        'side': pd.Categorical(['buy', 'sell']),
        'price': [39268.76, 39270.02],
        'amount': [0.003, 0.010],
        'timestamp': pd.to_datetime(['2021-01-03', '2021-01-03'])}
        ),
]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_data, df)
        for df in dfs]
    for future in futures:
        future.result()
```

For maxium performance you should also cache the sender objects and reuse them
across multiple requests, since internally they maintain a connection pool.

### Sender Lifetime Control[¶](#sender-lifetime-control "Link to this heading")

Instead of using a `with Sender .. as sender:` block you can also manually
control the lifetime of the sender object.

```
from questdb.ingress import Sender

conf = 'http::addr=localhost:9000;'
sender = Sender.from_conf(conf)
sender.establish()
# ...
sender.close()
```

The [`establish`](api.html#questdb.ingress.Sender.establish "questdb.ingress.Sender.establish") method is needs to be
called exactly once, but the [`close`](api.html#questdb.ingress.Sender.close "questdb.ingress.Sender.close") method
is idempotent and can be called multiple times.

## Table and Column Names[¶](#table-and-column-names "Link to this heading")

The client will validate table and column names while constructing the buffer.

Table names and column names must not be empty and must adhere to the following:

### Table Names[¶](#table-names "Link to this heading")

Cannot contain the following characters: `?`, `,`, `'`, `"`, `\`,
`/`, `:`, `)`, `(`, `+`, `*`, `%`, `~`, carriage return
(`\r`), newline (`\n`), null character (`\0`), and Unicode characters from
`\u{0001}` to `\u{000F}` and `\u{007F}`.
Additionally, the Unicode character for zero-width no-break space (UTF-8 BOM,
`\u{FEFF}`) is not allowed.

A dot (`.`) is allowed except at the start or end of the name,
and cannot be consecutive (e.g., `valid.name` is valid, but `.invalid`,
`invalid.`, and `in..valid` are not).

### Column Names[¶](#column-names "Link to this heading")

Cannot contain the following characters: `?`, `.`, `,`, `'`, `"`,
`\`, `/`, `:`, `)`, `(`, `+`, `-`, `*`, `%`, `~`,
carriage return (`\r`), newline (`\n`), null character (`\0`),
and Unicode characters from `\u{0001}` to `\u{000F}` and `\u{007F}`.
Like table names, the Unicode character for zero-width no-break space
(UTF-8 BOM, `\u{FEFF}`) is not allowed.

Unlike table names, a dot (`.`) is not allowed in column names at all.

## Programmatic Construction[¶](#sender-programmatic-construction "Link to this heading")

### Sender Constructor[¶](#sender-constructor "Link to this heading")

You can also specify the configuration parameters programmatically:

```
from questdb.ingress import Sender, Protocol
from datetime import timedelta

with Sender(Protocol.Tcp, 'localhost', 9009,
        auto_flush=True,
        auto_flush_interval=timedelta(seconds=10)) as sender:
    ...
```

See the [Configuration](conf.html#sender-conf) section for a full list of configuration parameters:
each configuration parameter can be passed as named arguments to the constructor.

Python type mappings:

* Parameters that require strings take a `str`.
* Parameters that require numbers can also take an `int`.
* Millisecond durations can take an `int` or a `datetime.timedelta`.
* Any `'on'` / `'off'` / `'unsafe_off'` parameters can also be specified
  as a `bool`.
* Paths can also be specified as a `pathlib.Path`.

Note

The constructor arguments have changed between 1.x and 2.x.
If you are upgrading, take a look at the [changelog](changelog.html#changelog).

### Customising `.from_conf()` and `.from_env()`[¶](#customising-from-conf-and-from-env "Link to this heading")

If you want to further customise the behaviour of the `.from_conf()` or
`.from_env()` methods, you can pass additional parameters to these methods.
The parameters are the same as the ones for the `Sender` constructor, as
documented above.

For example, here is a [configuration string](conf.html#sender-conf) that is loaded
from an environment variable and then customised to specify a 10 second
auto-flush interval:

```
export QDB_CLIENT_CONF='http::addr=localhost:9000;'
```

```
from questdb.ingress import Sender, Protocol
from datetime import timedelta

with Sender.from_env(auto_flush_interval=timedelta(seconds=10)) as sender:
    ...
```

## Protocol Version[¶](#protocol-version "Link to this heading")

Explicitly specifies the version of InfluxDB Line Protocol to use for sender.

Valid options are:

* `protocol_version=1`
* `protocol_version=2`
* `protocol_version=3`
* `protocol_version=auto` (default, if unspecified)

Behavior details:

| Value | Behavior |
| --- | --- |
| `1` | * Plain text serialization * Compatible with InfluxDB servers * No array type support |
| `2` | * Binary encoding for f64 * Full support for array * requires QuestDB server version 9.0.0 or higher |
| `3` | * Decimal support * requires QuestDB server version 9.2.0 or higher |
| `auto` | * **HTTP/HTTPS**: Auto-detects server capability during   handshake (supports version negotiation) * **TCP/TCPS**: Defaults to version 1 for compatibility |

Here is a configuration string with `protocol_version=3` for `TCP`:

```
tcp::addr=localhost:9000;protocol_version=3;
```

See the [Protocol Version](conf.html#sender-conf-protocol-version) section for more details.

## ILP/TCP or ILP/HTTP[¶](#ilp-tcp-or-ilp-http "Link to this heading")

The sender supports `tcp`, `tcps`, `http`, and `https` protocols.

**You should prefer to use the new ILP/HTTP protocol instead of ILP/TCP in most
cases as it provides better feedback on errors and transaction control.**

ILP/HTTP is available from:

* QuestDB 7.3.10 and later.
* QuestDB Enterprise 1.2.7 and later.

ILP/HTTP Also supports [protocol version](#sender-protocol-version)
auto-detection.

| Protocol | Protocol version auto-detection |
| --- | --- |
| ILP/HTTP | **Yes**: The client will communcate to the server using the latest version supported by both client and the server. |
| ILP/TCP | **No**: You need to [configure](conf.html#sender-conf-protocol-version) `protocol_version=N` to to match a version supported by the server. |

Note

The client will disable features that require a newer
protocol versions than the one used to communicate with the server.

Since TCP does not block for a response it is useful for high-throughput
scenarios in higher latency networks or on older versions of QuestDB which do
not support ILP/HTTP quite yet.

It should be noted that you can achieve equivalent or better performance to TCP
with HTTP by [using multiple sender objects in parallel](#sender-http-performance).

Either way, you can easily switch between the two protocols by changing:

* The `<protocol>` part of the [configuration string](conf.html#sender-conf).
* The port number (ILP/TCP default is 9009, ILP/HTTP default is 9000).
* Any [authentication parameters](conf.html#sender-conf-auth) such as `username`, `token`, et cetera.