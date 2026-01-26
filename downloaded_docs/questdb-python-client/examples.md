# Examples[¶](#examples "Link to this heading")

## Basics[¶](#basics "Link to this heading")

### HTTP with Token Auth[¶](#http-with-token-auth "Link to this heading")

The following example connects to the database and sends two rows (lines).

The connection is made via HTTPS and uses token based authentication.

The data is sent at the end of the `with` block.

```
from questdb.ingress import Sender, IngressError, TimestampNanos
import sys

def example(host: str = 'localhost', port: int = 9009):
    try:
        conf = f'https::addr={host}:{port};token=the_secure_token;'
        with Sender.from_conf(conf) as sender:
            # Record with provided designated timestamp (using the 'at' param)
            # Notice the designated timestamp is expected in Nanoseconds,
            # but timestamps in other columns are expected in Microseconds.
            # The API provides convenient functions
            sender.row(
                'trades',
                symbols={
                    'symbol': 'ETH-USD',
                    'side': 'sell'},
                columns={
                    'price': 2615.54,
                    'amount': 0.00044,
                   },
                at=TimestampNanos.now())

            # You can call `sender.row` multiple times inside the same `with`
            # block. The client will buffer the rows and send them in batches.

            # You can flush manually at any point.
            sender.flush()

            # If you don't flush manually, the client will flush automatically
            # when a row is added and either:
            #   * The buffer contains 75000 rows (if HTTP) or 600 rows (if TCP)
            #   * The last flush was more than 1000ms ago.
            # Auto-flushing can be customized via the `auto_flush_..` params.

        # Any remaining pending rows will be sent when the `with` block ends.

    except IngressError as e:
        sys.stderr.write(f'Got error: {e}\n')

if __name__ == '__main__':
    example()
```

### TCP Authentication and TLS[¶](#tcp-authentication-and-tls "Link to this heading")

Continuing from the previous example, the connection is authenticated
and also uses TLS.

```
from questdb.ingress import Sender, IngressError, TimestampNanos
import sys

def example(host: str = 'localhost', port: int = 9009):
    try:
        conf = (
            f"tcps::addr={host}:{port};" +
            "username=testUser1;" +
            "token=5UjEMuA0Pj5pjK8a-fa24dyIf-Es5mYny3oE_Wmus48;" +
            "token_x=fLKYEaoEb9lrn3nkwLDA-M_xnuFOdSt9y0Z7_vWSHLU;" +
            "token_y=Dt5tbS1dEDMSYfym3fgMv0B99szno-dFc1rYF9t0aac;")
        with Sender.from_conf(conf) as sender:
            # Record with provided designated timestamp (using the 'at' param)
            # Notice the designated timestamp is expected in Nanoseconds,
            # but timestamps in other columns are expected in Microseconds.
            # The API provides convenient functions
            sender.row(
                'trades',
                symbols={
                    'symbol': 'ETH-USD',
                    'side': 'sell'},
                columns={
                    'price': 2615.54,
                    'amount': 0.00044,
                   },
                at=TimestampNanos.now())

            # You can call `sender.row` multiple times inside the same `with`
            # block. The client will buffer the rows and send them in batches.

            # You can flush manually at any point.
            sender.flush()

            # If you don't flush manually, the client will flush automatically
            # when a row is added and either:
            #   * The buffer contains 75000 rows (if HTTP) or 600 rows (if TCP)
            #   * The last flush was more than 1000ms ago.
            # Auto-flushing can be customized via the `auto_flush_..` params.

        # Any remaining pending rows will be sent when the `with` block ends.

    except IngressError as e:
        sys.stderr.write(f'Got error: {e}\n')

if __name__ == '__main__':
    example()
```

### Explicit Buffers[¶](#explicit-buffers "Link to this heading")

For more [advanced use cases](sender.html#sender-advanced) where the same messages
need to be sent to multiple questdb instances or you want to decouple
serialization and sending (as may be in a multi-threaded application) construct
[`Buffer`](api.html#questdb.ingress.Buffer "questdb.ingress.Buffer") objects explicitly, then pass them to
the [`Sender.flush`](api.html#questdb.ingress.Sender.flush "questdb.ingress.Sender.flush") method.

Note that this bypasses [auto-flushing](sender.html#sender-auto-flush).

```
from questdb.ingress import Sender, TimestampNanos

def example(host: str = 'localhost', port: int = 9000):
    with Sender.from_conf(f"http::addr={host}:{port};") as sender:
        buffer = sender.new_buffer()
        buffer.row(
            'line_sender_buffer_example',
            symbols={'id': 'Hola'},
            columns={'price': 111222233333, 'qty': 3.5},
            at=TimestampNanos(111222233333))
        buffer.row(
            'line_sender_example',
            symbols={'id': 'Adios'},
            columns={'price': 111222233343, 'qty': 2.5},
            at=TimestampNanos(111222233343))
        sender.flush(buffer)

if __name__ == '__main__':
    example()
```

### Ticking Data and Auto-Flush[¶](#ticking-data-and-auto-flush "Link to this heading")

The following example somewhat mimics the behavior of a loop in an application.

It creates random ticking data at a random interval and uses non-default
auto-flush settings.

```
from questdb.ingress import Sender, TimestampNanos
import random
import uuid
import time

def example(host: str = 'localhost', port: int = 9009):
    table_name: str = str(uuid.uuid1())
    conf: str = (
        f"tcp::addr={host}:{port};" +
        "auto_flush_bytes=1024;" +   # Flush if the internal buffer exceeds 1KiB
        "auto_flush_rows=off;"       # Disable auto-flushing based on row count
        "auto_flush_interval=5000;") # Flush if last flushed more than 5s ago
    with Sender.from_conf(conf) as sender:
        total_rows = 0
        try:
            print("Ctrl^C to terminate...")
            while True:
                time.sleep(random.randint(0, 750) / 1000)  # sleep up to 750 ms

                print('Inserting row...')
                sender.row(
                    table_name,
                    symbols={
                        'src': random.choice(('ALPHA', 'BETA', 'OMEGA')),
                        'dst': random.choice(('ALPHA', 'BETA', 'OMEGA'))},
                    columns={
                        'price': random.randint(200, 500),
                        'qty': random.randint(1, 5)},
                    at=TimestampNanos.now())
                total_rows += 1

                # If the internal buffer is empty, then auto-flush triggered.
                if len(sender) == 0:
                    print('Auto-flush triggered.')

        except KeyboardInterrupt:
            print(f"table: {table_name}, total rows sent: {total_rows}")
            print("bye!")

if __name__ == '__main__':
    example()
```

## Data Frames[¶](#data-frames "Link to this heading")

### Pandas Basics[¶](#pandas-basics "Link to this heading")

The following example shows how to insert data from a Pandas DataFrame to the
`'trades'` table.

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

For details on all options, see the
[`Buffer.dataframe`](api.html#questdb.ingress.Buffer.dataframe "questdb.ingress.Buffer.dataframe") method.

### `pd.Categorical` and multiple tables[¶](#pd-categorical-and-multiple-tables "Link to this heading")

The next example shows some more advanced features inserting data from Pandas.

* The data is sent to multiple tables.
* It uses the `pd.Categorical` type to determine the table to insert and also
  uses it for the sensor name.
* Columns of type `pd.Categorical` are sent as `SYMBOL` types.
* The `at` parameter is specified using a column index: -1 is the last column.

```
from questdb.ingress import Sender, IngressError

import sys
import pandas as pd

def example(host: str = 'localhost', port: int = 9000):
    df = pd.DataFrame({
            'metric': pd.Categorical(
                ['humidity', 'temp_c', 'voc_index', 'temp_c']),
            'sensor': pd.Categorical(
                ['paris-01', 'london-02', 'london-01', 'paris-01']),
            'value': [
                0.83, 22.62, 100.0, 23.62],
            'ts': [
                pd.Timestamp('2022-08-06 07:35:23.189062'),
                pd.Timestamp('2022-08-06 07:35:23.189062'),
                pd.Timestamp('2022-08-06 07:35:23.189062'),
                pd.Timestamp('2022-08-06 07:35:23.189062')]})
    try:
        with Sender.from_conf(f"http::addr={host}:{port};") as sender:
            sender.dataframe(
                df,
                table_name_col='metric',  # Table name from 'metric' column.
                symbols='auto',  # Category columns as SYMBOL. (Default)
                at=-1)  # Last column contains the designated timestamps.

    except IngressError as e:
        sys.stderr.write(f'Got error: {e}\n')

if __name__ == '__main__':
    example()
```

After running this example, the rows will be split across the `'humidity'`,
`'temp_c'` and `'voc_index'` tables.

For details on all options, see the
[`Buffer.dataframe`](api.html#questdb.ingress.Buffer.dataframe "questdb.ingress.Buffer.dataframe") method.

### Loading Pandas from a Parquet File[¶](#loading-pandas-from-a-parquet-file "Link to this heading")

The following example shows how to load a Pandas DataFrame from a Parquet file.

The example also relies on the dataframe’s index name to determine the table
name.

```
from questdb.ingress import Sender
import pandas as pd

def write_parquet_file():
    df = pd.DataFrame({
        'location': pd.Categorical(
            ['BP-5541', 'UB-3355', 'SL-0995', 'BP-6653']),
        'provider': pd.Categorical(
            ['BP Pulse', 'Ubitricity', 'Source London', 'BP Pulse']),
        'speed_kwh': pd.Categorical(
            [50, 7, 7, 120]),
        'connector_type': pd.Categorical(
            ['Type 2 & 2+CCS', 'Type 1 & 2', 'Type 1 & 2', 'Type 2 & 2+CCS']),
        'current_type': pd.Categorical(
            ['dc', 'ac', 'ac', 'dc']),
        'price_pence':
            [54, 34, 32, 59],
        'in_use':
            [True, False, False, True],
        'ts': [
            pd.Timestamp('2022-12-30 12:15:00'),
            pd.Timestamp('2022-12-30 12:16:00'),
            pd.Timestamp('2022-12-30 12:18:00'),
            pd.Timestamp('2022-12-30 12:19:00')]})
    name = 'ev_chargers'
    df.index.name = name  # We set the dataframe's index name here!
    filename = f'{name}.parquet'
    df.to_parquet(filename)
    return filename

def example(host: str = 'localhost', port: int = 9000):
    filename = write_parquet_file()

    df = pd.read_parquet(filename)
    with Sender.from_conf(f"http::addr={host}:{port};") as sender:
        # Note: Table name is looked up from the dataframe's index name.
        sender.dataframe(df, at='ts')

if __name__ == '__main__':
    example()
```

For details on all options, see the
[`Buffer.dataframe`](api.html#questdb.ingress.Buffer.dataframe "questdb.ingress.Buffer.dataframe") method.

### Decimal Types (QuestDB 9.2.0+)[¶](#decimal-types-questdb-9-2-0 "Link to this heading")

The following example shows how to insert data with decimal precision using
Python’s [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") type.

Requires QuestDB server 9.2.0+ and [protocol version 3](conf.html#sender-conf-protocol-version)
(must be [configured explicitly for TCP/TCPS](conf.html#sender-conf-protocol-version)).
`DECIMAL` columns must be [pre-created](sender.html#sender-auto-creation) (auto-creation not supported).
See the [troubleshooting guide](troubleshooting.html#troubleshooting-flushing) for common errors.

First, create the table with `DECIMAL` columns:

```
CREATE TABLE financial_data (
    symbol SYMBOL,
    price DECIMAL(18, 6),
    quantity DECIMAL(12, 4),
    timestamp TIMESTAMP_NS
) TIMESTAMP(timestamp) PARTITION BY DAY;
```

Then insert data using Python decimals:

```
from decimal import Decimal
from questdb.ingress import Sender, TimestampNanos
import pandas as pd

# First, create the table with DECIMAL columns using SQL:
#
# CREATE TABLE financial_data (
#     symbol SYMBOL,
#     price DECIMAL(18, 6),
#     quantity DECIMAL(12, 4),
#     timestamp TIMESTAMP_NS
# ) TIMESTAMP(timestamp) PARTITION BY DAY;

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    # Using row() method with Python Decimal
    sender.row(
        'financial_data',
        symbols={'symbol': 'BTC-USD'},
        columns={
            'price': Decimal('50123.456789'),
            'quantity': Decimal('1.2345')
        },
        at=TimestampNanos.now())
    
    # Using dataframe() with Python Decimal objects
    df = pd.DataFrame({
        'symbol': ['BTC-USD', 'ETH-USD'],
        'price': [Decimal('50123.456789'), Decimal('2615.123456')],
        'quantity': [Decimal('1.2345'), Decimal('10.5678')]
    })
    sender.dataframe(df, table_name='financial_data',
                    symbols=['symbol'], at=TimestampNanos.now())
```

For better performance with DataFrames, use PyArrow decimal types:

```
from questdb.ingress import Sender, TimestampNanos
import pandas as pd
import pyarrow as pa

# First, create the table with DECIMAL columns using SQL:
#
# CREATE TABLE financial_data (
#     symbol SYMBOL,
#     price DECIMAL(18, 6),
#     quantity DECIMAL(12, 4),
#     timestamp TIMESTAMP_NS
# ) TIMESTAMP(timestamp) PARTITION BY DAY;

df = pd.DataFrame({
    'symbol': ['BTC-USD', 'ETH-USD'],
    'price': pd.Series(
        [50123.456789, 2615.123456],
        dtype=pd.ArrowDtype(pa.decimal128(18, 6))),
    'quantity': pd.Series(
        [1.2345, 10.5678],
        dtype=pd.ArrowDtype(pa.decimal128(12, 4)))
})

conf = 'http::addr=localhost:9000;'
with Sender.from_conf(conf) as sender:
    sender.dataframe(df, table_name='financial_data',
                    symbols=['symbol'], at=TimestampNanos.now())
```

Note

For HTTP/HTTPS, protocol version 3 is auto-negotiated.
For TCP/TCPS, explicitly configure: `tcp::addr=localhost:9009;protocol_version=3;`

For more details, see the
[QuestDB DECIMAL documentation](https://questdb.com/docs/reference/sql/datatypes/#decimal).