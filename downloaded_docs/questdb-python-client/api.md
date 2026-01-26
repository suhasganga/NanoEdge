# API Reference[¶](#api-reference "Link to this heading")

## questdb.ingress[¶](#questdb-ingress "Link to this heading")

*class* questdb.ingress.Sender[¶](#questdb.ingress.Sender "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Ingest data into QuestDB.

    See the [Sending Data over ILP](sender.html#sender) documentation for more information.

    \_\_enter\_\_() → [Sender](#questdb.ingress.Sender "questdb.ingress.Sender")[¶](#questdb.ingress.Sender.__enter__ "Link to this definition")
    :   Call [`Sender.establish()`](#questdb.ingress.Sender.establish "questdb.ingress.Sender.establish") at the start of a `with` block.

    \_\_exit\_\_(*exc\_type*, *\_exc\_val*, *\_exc\_tb*)[¶](#questdb.ingress.Sender.__exit__ "Link to this definition")
    :   Flush pending and disconnect at the end of a `with` block.

        If the `with` block raises an exception, any pending data will
        *NOT* be flushed.

        This is implemented by calling [`Sender.close()`](#questdb.ingress.Sender.close "questdb.ingress.Sender.close").

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[¶](#questdb.ingress.Sender.__init__ "Link to this definition")

    auto\_flush[¶](#questdb.ingress.Sender.auto_flush "Link to this definition")
    :   Auto-flushing is enabled.

        Consult the .auto\_flush\_rows, .auto\_flush\_bytes and
        .auto\_flush\_interval properties for the current active thresholds.

    auto\_flush\_bytes[¶](#questdb.ingress.Sender.auto_flush_bytes "Link to this definition")
    :   Byte-count threshold for the auto-flush logic, or None if disabled.

    auto\_flush\_interval[¶](#questdb.ingress.Sender.auto_flush_interval "Link to this definition")
    :   Time interval threshold for the auto-flush logic, or None if disabled.

    auto\_flush\_rows[¶](#questdb.ingress.Sender.auto_flush_rows "Link to this definition")
    :   Row count threshold for the auto-flush logic, or None if disabled.

    close(*flush=True*)[¶](#questdb.ingress.Sender.close "Link to this definition")
    :   Disconnect.

        This method is idempotent and can be called repeatedly.

        Once a sender is closed, it can’t be re-used.

        Parameters:
        :   **flush** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – If `True`, flush the internal buffer before closing.

    dataframe(*df*, *\**, *table\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *table\_name\_col: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *symbols: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | List[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | List[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = 'auto'*, *at: [ServerTimestampType](#questdb.ingress.ServerTimestampType "questdb.ingress.ServerTimestampType") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.Sender.dataframe "Link to this definition")
    :   Write a Pandas DataFrame to the internal buffer.

        Example:

        ```
        import pandas as pd
        import questdb.ingress as qi

        df = pd.DataFrame({
            'car': pd.Categorical(['Nic 42', 'Eddi', 'Nic 42', 'Eddi']),
            'position': [1, 2, 1, 2],
            'speed': [89.3, 98.2, 3, 4],
            'lat_gforce': [0.1, -0.2, -0.6, 0.4],
            'accelleration': [0.1, -0.2, 0.6, 4.4],
            'tyre_pressure': [2.6, 2.5, 2.6, 2.5],
            'ts': [
                pd.Timestamp('2022-08-09 13:56:00'),
                pd.Timestamp('2022-08-09 13:56:01'),
                pd.Timestamp('2022-08-09 13:56:02'),
                pd.Timestamp('2022-08-09 13:56:03')]})

        with qi.Sender.from_env() as sender:
            sender.dataframe(df, table_name='race_metrics', at='ts')
        ```

        This method builds on top of the [`Buffer.dataframe()`](#questdb.ingress.Buffer.dataframe "questdb.ingress.Buffer.dataframe") method.
        See its documentation for details on arguments.

        Additionally, this method also supports auto-flushing the buffer
        as specified in the `Sender`’s `auto_flush` constructor argument.
        Auto-flushing is implemented incrementally, meanting that when
        calling `sender.dataframe(df)` with a large `df`, the sender may
        have sent some of the rows to the server already whist the rest of the
        rows are going to be sent at the next auto-flush or next explicit call
        to [`Sender.flush()`](#questdb.ingress.Sender.flush "questdb.ingress.Sender.flush").

        In case of data errors with auto-flushing enabled, some of the rows
        may have been transmitted to the server already.

    establish()[¶](#questdb.ingress.Sender.establish "Link to this definition")
    :   Prepare the sender for use.

        If using ILP/HTTP this will initialize the HTTP connection pool.

        If using ILP/TCP this will cause connection to the server and
        block until the connection is established.

        If the TCP connection is set up with authentication and/or TLS, this
        method will return only *after* the handshake(s) is/are complete.

    flush(*buffer=None*, *clear=True*, *transactional=False*)[¶](#questdb.ingress.Sender.flush "Link to this definition")
    :   If called with no arguments, immediately flushes the internal buffer.

        Alternatively you can flush a buffer that was constructed explicitly
        by passing `buffer`.

        The buffer will be cleared by default, unless `clear` is set to
        `False`.

        This method does nothing if the provided or internal buffer is empty.

        Parameters:
        :   * **buffer** – The buffer to flush. If `None`, the internal buffer
              is flushed.
            * **clear** – If `True`, the flushed buffer is cleared (default).
              If `False`, the flushed buffer is left in the internal buffer.
              Note that `clear=False` is only supported if `buffer` is also
              specified.
            * **transactional** – If `True` ensures that the flushed buffer
              contains row for a single table, ensuring all data can be written
              transactionally. This feature requires ILP/HTTP and is not available
              when connecting over TCP. *Default: False.*

        The Python GIL is released during the network IO operation.

    *static* from\_conf(*conf\_str*, *\**, *bind\_interface=None*, *username=None*, *password=None*, *token=None*, *token\_x=None*, *token\_y=None*, *auth\_timeout=None*, *tls\_verify=None*, *tls\_ca=None*, *tls\_roots=None*, *max\_buf\_size=None*, *retry\_timeout=None*, *request\_min\_throughput=None*, *request\_timeout=None*, *auto\_flush=None*, *auto\_flush\_rows=None*, *auto\_flush\_bytes=None*, *auto\_flush\_interval=None*, *protocol\_version=None*, *init\_buf\_size=None*, *max\_name\_len=None*)[¶](#questdb.ingress.Sender.from_conf "Link to this definition")
    :   Construct a sender from a [configuration string](conf.html#sender-conf).

        The additional arguments are used to specify additional parameters
        which are not present in the configuration string.

        Note that any parameters already present in the configuration string
        cannot be overridden.

    *static* from\_env(*\**, *bind\_interface=None*, *username=None*, *password=None*, *token=None*, *token\_x=None*, *token\_y=None*, *auth\_timeout=None*, *tls\_verify=None*, *tls\_ca=None*, *tls\_roots=None*, *max\_buf\_size=None*, *retry\_timeout=None*, *request\_min\_throughput=None*, *request\_timeout=None*, *auto\_flush=None*, *auto\_flush\_rows=None*, *auto\_flush\_bytes=None*, *auto\_flush\_interval=None*, *protocol\_version=None*, *init\_buf\_size=None*, *max\_name\_len=None*)[¶](#questdb.ingress.Sender.from_env "Link to this definition")
    :   Construct a sender from the `QDB_CLIENT_CONF` environment variable.

        The environment variable must be set to a valid
        [configuration string](conf.html#sender-conf).

        The additional arguments are used to specify additional parameters
        which are not present in the configuration string.

        Note that any parameters already present in the configuration string
        cannot be overridden.

    init\_buf\_size[¶](#questdb.ingress.Sender.init_buf_size "Link to this definition")
    :   The initial capacity of the sender’s internal buffer.

    max\_name\_len[¶](#questdb.ingress.Sender.max_name_len "Link to this definition")
    :   Maximum length of a table or column name.

    new\_buffer()[¶](#questdb.ingress.Sender.new_buffer "Link to this definition")
    :   Make a new configured buffer.

        The buffer is set up with the configured init\_buf\_size and
        max\_name\_len.

    protocol\_version[¶](#questdb.ingress.Sender.protocol_version "Link to this definition")
    :   The protocol version used by the sender.

        Protocol version 1 is retained for backwards compatibility with
        older QuestDB versions.

        Protocol version 2 introduces binary floating point support and
        the array datatype.

    row(*table\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *symbols: Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *columns: Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [TimestampMicros](#questdb.ingress.TimestampMicros "questdb.ingress.TimestampMicros") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at: [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [ServerTimestampType](#questdb.ingress.ServerTimestampType "questdb.ingress.ServerTimestampType")*)[¶](#questdb.ingress.Sender.row "Link to this definition")
    :   Write a row to the internal buffer.

        This may be sent automatically depending on the `auto_flush` setting
        in the constructor.

        Refer to the [`Buffer.row()`](#questdb.ingress.Buffer.row "questdb.ingress.Buffer.row") documentation for details on arguments.

        **Note**: Support for NumPy arrays (`numpy.array`) requires QuestDB server version 9.0.0 or higher.

    transaction(*table\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[¶](#questdb.ingress.Sender.transaction "Link to this definition")
    :   Start a [HTTP Transactions](sender.html#sender-transaction) block.

*class* questdb.ingress.Buffer[¶](#questdb.ingress.Buffer "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Construct QuestDB InfluxDB Line Protocol (ILP) messages.
    Version 1 is compatible with the InfluxDB Line Protocol.

    The [`Buffer.row()`](#questdb.ingress.Buffer.row "questdb.ingress.Buffer.row") method is used to add a row to the buffer.

    You can call this many times.

    ```
    from questdb.ingress import Buffer

    buf = Buffer()
    buf.row(
        'table_name1',
        symbols={'s1', 'v1', 's2', 'v2'},
        columns={'c1': True, 'c2': 0.5})

    buf.row(
        'table_name2',
        symbols={'questdb': '❤️'},
        columns={'like': 100000})

    # Append any additional rows then, once ready, call
    sender.flush(buffer)  # a `Sender` instance.

    # The sender auto-cleared the buffer, ready for reuse.

    buf.row(
        'table_name1',
        symbols={'s1', 'v1', 's2', 'v2'},
        columns={'c1': True, 'c2': 0.5})

    # etc.
    ```

    Buffer Constructor Arguments:
    :   * protocol\_version (`int`): The protocol version to use.
        * `init_buf_size` (`int`): Initial capacity of the buffer in bytes.
          Defaults to `65536` (64KiB).
        * `max_name_len` (`int`): Maximum length of a column name.
          Defaults to `127` which is the same default value as QuestDB.
          This should match the `cairo.max.file.name.length` setting of the
          QuestDB instance you’re connecting to.

    **Note**: Protocol version `2` requires QuestDB server version 9.0.0 or higher.

    ```
    # These two buffer constructions are equivalent.
    buf1 = Buffer()
    buf2 = Buffer(init_buf_size=65536, max_name_len=127)
    ```

    To avoid having to manually set these arguments every time, you can call
    the sender’s `new_buffer()` method instead.

    ```
    from questdb.ingress import Sender, Buffer

    sender = Sender('http', 'localhost', 9009,
        init_buf_size=16384, max_name_len=64)
    buf = sender.new_buffer()
    assert buf.init_buf_size == 16384
    assert buf.max_name_len == 64
    ```

    capacity() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[¶](#questdb.ingress.Buffer.capacity "Link to this definition")
    :   The current buffer capacity.

    clear()[¶](#questdb.ingress.Buffer.clear "Link to this definition")
    :   Reset the buffer.

        Note that flushing a buffer will (unless otherwise specified)
        also automatically clear it.

        This method is designed to be called only in conjunction with
        `sender.flush(buffer, clear=False)`.

    dataframe(*df*, *\**, *table\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *table\_name\_col: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *symbols: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | List[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | List[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = 'auto'*, *at: [ServerTimestampType](#questdb.ingress.ServerTimestampType "questdb.ingress.ServerTimestampType") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.Buffer.dataframe "Link to this definition")
    :   Add a pandas DataFrame to the buffer.

        Also see the [`Sender.dataframe()`](#questdb.ingress.Sender.dataframe "questdb.ingress.Sender.dataframe") method if you’re
        not using the buffer explicitly. It supports the same parameters
        and also supports auto-flushing.

        This feature requires the `pandas`, `numpy` and `pyarrow`
        package to be installed.

        Adding a dataframe can trigger auto-flushing behaviour,
        even between rows of the same dataframe. To avoid this, you can
        use HTTP and transactions (see [`Sender.transaction()`](#questdb.ingress.Sender.transaction "questdb.ingress.Sender.transaction")).

        Parameters:
        :   * **df** ([*pandas.DataFrame*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.3.3)")) – The pandas DataFrame to serialize to the buffer.
            * **table\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* *None*) –

              The name of the table to which the rows belong.

              If `None`, the table name is taken from the `table_name_col`
              parameter. If both `table_name` and `table_name_col` are
              `None`, the table name is taken from the DataFrame’s index
              name (`df.index.name` attribute).
            * **table\_name\_col** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None*) –

              The name or index of the column in the DataFrame
              that contains the table name.

              If `None`, the table name is taken
              from the `table_name` parameter. If both `table_name` and
              `table_name_col` are `None`, the table name is taken from the
              DataFrame’s index name (`df.index.name` attribute).

              If `table_name_col` is an integer, it is interpreted as the index
              of the column starting from `0`. The index of the column can be
              negative, in which case it is interpreted as an offset from the end
              of the DataFrame. E.g. `-1` is the last column.
            * **symbols** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*] or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]*) –

              The columns to be serialized as symbols.

              If `'auto'` (default), all columns of dtype `'categorical'` are
              serialized as symbols. If `True`, all `str` columns are
              serialized as symbols. If `False`, no columns are serialized as
              symbols.

              The list of symbols can also be specified explicitly as a `list`
              of column names (`str`) or indices (`int`). Integer indices
              start at `0` and can be negative, offset from the end of the
              DataFrame. E.g. `-1` is the last column.

              Only columns containing strings can be serialized as symbols.
            * **at** ([*TimestampNanos*](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos")*,* [*datetime.datetime*](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* *None*) –

              The designated timestamp of the rows.

              You can specify a single value for all rows or column name or index.
              If `ServerTimestamp`, timestamp is assigned by the server for all rows.
              To pass in a timestamp explicitly as an integer use the
              `TimestampNanos` wrapper type. To get the current timestamp,
              use `TimestampNanos.now()`.
              When passing a `datetime.datetime` object, the timestamp is
              converted to nanoseconds.
              A `datetime` object is assumed to be in the local timezone unless
              one is specified explicitly (so call
              `datetime.datetime.now(tz=datetime.timezone.utc)` instead
              of `datetime.datetime.utcnow()` for the current timestamp to
              avoid bugs).

              To specify a different timestamp for each row, pass in a column name
              (`str`) or index (`int`, 0-based index, negative index
              supported): In this case, the column needs to be of dtype
              `datetime64[ns]` (assumed to be in the **UTC timezone** and not
              local, due to differences in Pandas and Python datetime handling) or
              `datetime64[ns, tz]`. When a timezone is specified in the column,
              it is converted to UTC automatically.

              A timestamp column can also contain `None` values. The server will
              assign the current timestamp to those rows.

              **Note**: All timestamps are always converted to nanoseconds and in
              the UTC timezone. Timezone information is dropped before sending and
              QuestDB will not store any timezone information.

        **Note**: It is an error to specify both `table_name` and
        `table_name_col`.

        **Note**: The “index” column of the DataFrame is never serialized,
        even if it is named.

        Example:

        ```
        import pandas as pd
        import questdb.ingress as qi

        buf = qi.Buffer(protocol_version=2)
        # ...

        df = pd.DataFrame({
            'location': ['London', 'Managua', 'London'],
            'temperature': [24.5, 35.0, 25.5],
            'humidity': [0.5, 0.6, 0.45],
            'ts': pd.date_range('2021-07-01', periods=3)})
        buf.dataframe(
            df, table_name='weather', at='ts', symbols=['location'])

        # ...
        sender.flush(buf)
        ```

        **Pandas to ILP datatype mappings**

        See also

        <https://questdb.com/docs/reference/api/ilp/columnset-types/>

        Pandas Mappings[¶](#id1 "Link to this table")

        | Pandas `dtype` | Nulls | ILP Datatype |
        | --- | --- | --- |
        | `'bool'` | N | `BOOLEAN` |
        | `'boolean'` | N **α** | `BOOLEAN` |
        | `'object'` (`bool` objects) | N **α** | `BOOLEAN` |
        | `'uint8'` | N | `INTEGER` |
        | `'int8'` | N | `INTEGER` |
        | `'uint16'` | N | `INTEGER` |
        | `'int16'` | N | `INTEGER` |
        | `'uint32'` | N | `INTEGER` |
        | `'int32'` | N | `INTEGER` |
        | `'uint64'` | N | `INTEGER` **β** |
        | `'int64'` | N | `INTEGER` |
        | `'UInt8'` | Y | `INTEGER` |
        | `'Int8'` | Y | `INTEGER` |
        | `'UInt16'` | Y | `INTEGER` |
        | `'Int16'` | Y | `INTEGER` |
        | `'UInt32'` | Y | `INTEGER` |
        | `'Int32'` | Y | `INTEGER` |
        | `'UInt64'` | Y | `INTEGER` **β** |
        | `'Int64'` | Y | `INTEGER` |
        | `'object'` (`int` objects) | Y | `INTEGER` **β** |
        | `'float32'` **γ** | Y (`NaN`) | `FLOAT` |
        | `'float64'` | Y (`NaN`) | `FLOAT` |
        | `'object'` (`float` objects) | Y (`NaN`) | `FLOAT` |
        | `'string'` (`str` objects) | Y | `STRING` (default), `SYMBOL` via `symbols` arg. **δ** |
        | `'string[pyarrow]'` | Y | `STRING` (default), `SYMBOL` via `symbols` arg. **δ** |
        | `'category'` (`str` objects) **ε** | Y | `SYMBOL` (default), `STRING` via `symbols` arg. **δ** |
        | `'object'` (`str` objects) | Y | `STRING` (default), `SYMBOL` via `symbols` arg. **δ** |
        | `'datetime64[ns]'` | Y | `TIMESTAMP` **ζ** |
        | `'datetime64[ns, tz]'` | Y | `TIMESTAMP` **ζ** |
        | `'object'` (`Decimal` objects) | Y (`NaN`) | `DECIMAL` |

        Note

        * **α**: Note some pandas dtypes allow nulls (e.g. `'boolean'`),
          where the QuestDB database does not.
        * **β**: The valid range for integer values is -2^63 to 2^63-1.
          Any `'uint64'`, `'UInt64'` or python `int` object values
          outside this range will raise an error during serialization.
        * **γ**: Upcast to 64-bit float during serialization.
        * **δ**: Columns containing strings can also be used to specify the
          table name. See `table_name_col`.
        * **ε**: We only support categories containing strings. If the
          category contains non-string values, an error will be raised.
        * **ζ**: The ‘.dataframe()’ method only supports datetimes with
          nanosecond precision. The designated timestamp column (see `at`
          parameter) maintains the nanosecond precision, whilst values
          stored as columns have their precision truncated to microseconds.
          All dates are sent as UTC and any additional timezone information
          is dropped. If no timezone is specified, we follow
          the pandas convention of assuming the timezone is UTC.
          Datetimes before 1970-01-01 00:00:00 UTC are not supported.
          If a datetime value is specified as `None` (`NaT`), it is
          interpreted as the current QuestDB server time set on receipt of
          message.

        **Error Handling and Recovery**

        In case an exception is raised during dataframe serialization, the
        buffer is left in its previous state.
        The buffer remains in a valid state and can be used for further calls
        even after an error.

        For clarification, as an example, if an invalid `None`
        value appears at the 3rd row for a `bool` column, neither the 3rd nor
        the preceding rows are added to the buffer.

        **Note**: This differs from the [`Sender.dataframe()`](#questdb.ingress.Sender.dataframe "questdb.ingress.Sender.dataframe") method, which
        modifies this guarantee due to its `auto_flush` logic.

        **Performance Considerations**

        The Python GIL is released during serialization if it is not needed.
        If any column requires the GIL, the entire serialization is done whilst
        holding the GIL.

        Column types that require the GIL are:

        * Columns of `str`, `float` or `int` or `float` Python objects.
        * The `'string[python]'` dtype.

    init\_buf\_size[¶](#questdb.ingress.Buffer.init_buf_size "Link to this definition")
    :   The initial capacity of the buffer when first created.

        This may grow over time, see `capacity()`.

    max\_name\_len[¶](#questdb.ingress.Buffer.max_name_len "Link to this definition")
    :   Maximum length of a table or column name.

    reserve(*additional: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[¶](#questdb.ingress.Buffer.reserve "Link to this definition")
    :   Ensure the buffer has at least additional bytes of future capacity.

        Parameters:
        :   **additional** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Additional bytes to reserve.

    row(*table\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *symbols: Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *columns: Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [TimestampMicros](#questdb.ingress.TimestampMicros "questdb.ingress.TimestampMicros") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at: [ServerTimestampType](#questdb.ingress.ServerTimestampType "questdb.ingress.ServerTimestampType") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.Buffer.row "Link to this definition")
    :   Add a single row (line) to the buffer.

        ```
        # All fields specified.
        buffer.row(
            'table_name',
            symbols={'sym1': 'abc', 'sym2': 'def', 'sym3': None},
            columns={
                'col1': True,
                'col2': 123,
                'col3': 3.14,
                'col4': 'xyz',
                'col5': TimestampMicros(123456789),
                'col6': datetime(2019, 1, 1, 12, 0, 0),
                'col7': numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                'col8': None},
            at=TimestampNanos(123456789))

        # Only symbols specified. Designated timestamp assigned by the db.
        buffer.row(
            'table_name',
            symbols={'sym1': 'abc', 'sym2': 'def'}, at=Server.Timestamp)

        # Float columns and timestamp specified as `datetime.datetime`.
        # Pay special attention to the timezone, which if unspecified is
        # assumed to be the local timezone (and not UTC).
        buffer.row(
            'sensor data',
            columns={
                'temperature': 24.5,
                'humidity': 0.5},
            at=datetime.datetime.now(tz=datetime.timezone.utc))
        ```

        Python strings passed as values to `symbols` are going to be encoded
        as the `SYMBOL` type in QuestDB, whilst Python strings passed as
        values to `columns` are going to be encoded as the `STRING` type.

        Refer to the
        [QuestDB documentation](https://questdb.com/docs/concept/symbol/) to
        understand the difference between the `SYMBOL` and `STRING` types
        (TL;DR: symbols are interned strings).

        Column values can be specified with Python types directly and map as so:

        | Python type | Serialized as ILP type |
        | --- | --- |
        | `bool` | [BOOLEAN](https://questdb.com/docs/reference/api/ilp/columnset-types#boolean) |
        | `decimal` | [DECIMAL](https://questdb.com/docs/reference/api/ilp/columnset-types#decimal) |
        | `int` | [INTEGER](https://questdb.com/docs/reference/api/ilp/columnset-types#integer) |
        | `float` | [FLOAT](https://questdb.com/docs/reference/api/ilp/columnset-types#float) |
        | `str` | [STRING](https://questdb.com/docs/reference/api/ilp/columnset-types#string) |
        | `numpy.ndarray` | [ARRAY](https://questdb.com/docs/reference/api/ilp/columnset-types#array) |
        | `datetime.datetime` and `TimestampMicros` | [TIMESTAMP](https://questdb.com/docs/reference/api/ilp/columnset-types#timestamp) |
        | `None` | *Column is skipped and not serialized.* |

        **Note**: Support for NumPy arrays (`numpy.array`) requires QuestDB server version 9.0.0 or higher.

        If the destination table was already created, then the columns types
        will be cast to the types of the existing columns whenever possible
        (Refer to the QuestDB documentation pages linked above).

        Adding a row can trigger auto-flushing behaviour.

        Parameters:
        :   * **table\_name** – The name of the table to which the row belongs.
            * **symbols** – A dictionary of symbol column names to `str` values.
              As a convenience, you can also pass a `None` value which will
              have the same effect as skipping the key: If the column already
              existed, it will be recorded as `NULL`, otherwise it will not be
              created.
            * **columns** – A dictionary of column names to `bool`, `int`,
              `float`, `str`, `TimestampMicros` or `datetime` values.
              As a convenience, you can also pass a `None` value which will
              have the same effect as skipping the key: If the column already
              existed, it will be recorded as `NULL`, otherwise it will not be
              created.
            * **at** – The timestamp of the row. This is required!
              If `ServerTimestamp`, timestamp is assigned by QuestDB.
              If `datetime`, the timestamp is converted to nanoseconds.
              A nanosecond unix epoch timestamp can be passed
              explicitly as a `TimestampNanos` object.

*class* questdb.ingress.SenderTransaction[¶](#questdb.ingress.SenderTransaction "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A transaction for a specific table.

    Transactions are not supported with ILP/TCP, only ILP/HTTP.

    The sender API can only operate on one transaction at a time.

    To create a transaction:

    ```
    with sender.transaction('table_name') as txn:
        txn.row(..)
        txn.dataframe(..)
    ```

    \_\_enter\_\_()[¶](#questdb.ingress.SenderTransaction.__enter__ "Link to this definition")

    \_\_exit\_\_(*exc\_type*, *\_exc\_value*, *\_traceback*)[¶](#questdb.ingress.SenderTransaction.__exit__ "Link to this definition")

    commit()[¶](#questdb.ingress.SenderTransaction.commit "Link to this definition")
    :   Commit the transaction.

        A commit is also automatic at the end of a successful with block.

        This will flush the buffer.

    dataframe(*df*, *\**, *symbols: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | List[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | List[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = 'auto'*, *at: [ServerTimestampType](#questdb.ingress.ServerTimestampType "questdb.ingress.ServerTimestampType") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.SenderTransaction.dataframe "Link to this definition")
    :   Write a dataframe for the table in the transaction.

        The table name is taken from the transaction.

    rollback()[¶](#questdb.ingress.SenderTransaction.rollback "Link to this definition")
    :   Roll back the transaction.

        A rollback is also automatic at the end of a failed with block.

        This will clear the buffer.

    row(*\**, *symbols: Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *columns: Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [TimestampMicros](#questdb.ingress.TimestampMicros "questdb.ingress.TimestampMicros") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at: [ServerTimestampType](#questdb.ingress.ServerTimestampType "questdb.ingress.ServerTimestampType") | [TimestampNanos](#questdb.ingress.TimestampNanos "questdb.ingress.TimestampNanos") | [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.SenderTransaction.row "Link to this definition")
    :   Write a row for the table in the transaction.

        The table name is taken from the transaction.

        **Note**: Support for NumPy arrays (`numpy.array`) requires QuestDB server version 9.0.0 or higher.

*class* questdb.ingress.IngressError(*code*, *msg*)[¶](#questdb.ingress.IngressError "Link to this definition")
:   Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")

    An error whilst using the `Sender` or constructing its `Buffer`.

    \_\_init\_\_(*code*, *msg*)[¶](#questdb.ingress.IngressError.__init__ "Link to this definition")

    *property* code*: [IngressErrorCode](#questdb.ingress.IngressErrorCode "questdb.ingress.IngressErrorCode")*[¶](#questdb.ingress.IngressError.code "Link to this definition")
    :   Return the error code.

*class* questdb.ingress.IngressErrorCode(*\*values*)[¶](#questdb.ingress.IngressErrorCode "Link to this definition")
:   Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")

    Category of Error.

    ArrayError *= 11*[¶](#questdb.ingress.IngressErrorCode.ArrayError "Link to this definition")

    AuthError *= 6*[¶](#questdb.ingress.IngressErrorCode.AuthError "Link to this definition")

    BadDataFrame *= 14*[¶](#questdb.ingress.IngressErrorCode.BadDataFrame "Link to this definition")

    ConfigError *= 10*[¶](#questdb.ingress.IngressErrorCode.ConfigError "Link to this definition")

    CouldNotResolveAddr *= 0*[¶](#questdb.ingress.IngressErrorCode.CouldNotResolveAddr "Link to this definition")

    DecimalError *= 13*[¶](#questdb.ingress.IngressErrorCode.DecimalError "Link to this definition")

    HttpNotSupported *= 8*[¶](#questdb.ingress.IngressErrorCode.HttpNotSupported "Link to this definition")

    InvalidApiCall *= 1*[¶](#questdb.ingress.IngressErrorCode.InvalidApiCall "Link to this definition")

    InvalidName *= 4*[¶](#questdb.ingress.IngressErrorCode.InvalidName "Link to this definition")

    InvalidTimestamp *= 5*[¶](#questdb.ingress.IngressErrorCode.InvalidTimestamp "Link to this definition")

    InvalidUtf8 *= 3*[¶](#questdb.ingress.IngressErrorCode.InvalidUtf8 "Link to this definition")

    ProtocolVersionError *= 12*[¶](#questdb.ingress.IngressErrorCode.ProtocolVersionError "Link to this definition")

    ServerFlushError *= 9*[¶](#questdb.ingress.IngressErrorCode.ServerFlushError "Link to this definition")

    SocketError *= 2*[¶](#questdb.ingress.IngressErrorCode.SocketError "Link to this definition")

    TlsError *= 7*[¶](#questdb.ingress.IngressErrorCode.TlsError "Link to this definition")

    \_\_str\_\_() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[¶](#questdb.ingress.IngressErrorCode.__str__ "Link to this definition")
    :   Return the name of the enum.

*class* questdb.ingress.Protocol(*\*values*)[¶](#questdb.ingress.Protocol "Link to this definition")
:   Bases: [`TaggedEnum`](#questdb.ingress.TaggedEnum "questdb.ingress.TaggedEnum")

    Protocol to use for sending data to QuestDB.

    See [ILP/TCP or ILP/HTTP](sender.html#sender-which-protocol) for more information.

    Http *= ('http', 2)*[¶](#questdb.ingress.Protocol.Http "Link to this definition")

    Https *= ('https', 3)*[¶](#questdb.ingress.Protocol.Https "Link to this definition")

    Tcp *= ('tcp', 0)*[¶](#questdb.ingress.Protocol.Tcp "Link to this definition")

    Tcps *= ('tcps', 1)*[¶](#questdb.ingress.Protocol.Tcps "Link to this definition")

    *property* tls\_enabled[¶](#questdb.ingress.Protocol.tls_enabled "Link to this definition")

*class* questdb.ingress.TimestampMicros[¶](#questdb.ingress.TimestampMicros "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A timestamp in microseconds since the UNIX epoch (UTC).

    You may construct a `TimestampMicros` from an integer or a
    `datetime.datetime`, or simply call the [`TimestampMicros.now()`](#questdb.ingress.TimestampMicros.now "questdb.ingress.TimestampMicros.now")
    method.

    ```
    # Recommended way to get the current timestamp.
    TimestampMicros.now()

    # The above is equivalent to:
    TimestampMicros(time.time_ns() // 1000)

    # You can provide a numeric timestamp too. It can't be negative.
    TimestampMicros(1657888365426838)
    ```

    `TimestampMicros` can also be constructed from a `datetime.datetime`
    object.

    ```
    TimestampMicros.from_datetime(
        datetime.datetime.now(tz=datetime.timezone.utc))
    ```

    We recommend that when using `datetime` objects, you explicitly pass in
    the timezone to use. This is because `datetime` objects without an
    associated timezone are assumed to be in the local timezone and it is easy
    to make mistakes (e.g. passing `datetime.datetime.utcnow()` is a likely
    bug).

    *classmethod* from\_datetime(*dt: [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.TimestampMicros.from_datetime "Link to this definition")
    :   Construct a `TimestampMicros` from a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") object.

    *classmethod* now()[¶](#questdb.ingress.TimestampMicros.now "Link to this definition")
    :   Construct a `TimestampMicros` from the current time as UTC.

    value[¶](#questdb.ingress.TimestampMicros.value "Link to this definition")
    :   Number of microseconds (Unix epoch timestamp, UTC).

*class* questdb.ingress.TimestampNanos[¶](#questdb.ingress.TimestampNanos "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A timestamp in nanoseconds since the UNIX epoch (UTC).

    You may construct a `TimestampNanos` from an integer or a
    `datetime.datetime`, or simply call the [`TimestampNanos.now()`](#questdb.ingress.TimestampNanos.now "questdb.ingress.TimestampNanos.now")
    method.

    ```
    # Recommended way to get the current timestamp.
    TimestampNanos.now()

    # The above is equivalent to:
    TimestampNanos(time.time_ns())

    # You can provide a numeric timestamp too. It can't be negative.
    TimestampNanos(1657888365426838016)
    ```

    `TimestampNanos` can also be constructed from a `datetime` object.

    ```
    TimestampNanos.from_datetime(
        datetime.datetime.now(tz=datetime.timezone.utc))
    ```

    We recommend that when using `datetime` objects, you explicitly pass in
    the timezone to use. This is because `datetime` objects without an
    associated timezone are assumed to be in the local timezone and it is easy
    to make mistakes (e.g. passing `datetime.datetime.utcnow()` is a likely
    bug).

    *classmethod* from\_datetime(*dt: [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*)[¶](#questdb.ingress.TimestampNanos.from_datetime "Link to this definition")
    :   Construct a `TimestampNanos` from a `datetime.datetime` object.

    *classmethod* now()[¶](#questdb.ingress.TimestampNanos.now "Link to this definition")
    :   Construct a `TimestampNanos` from the current time as UTC.

    value[¶](#questdb.ingress.TimestampNanos.value "Link to this definition")
    :   Number of nanoseconds (Unix epoch timestamp, UTC).

*class* questdb.ingress.TlsCa(*\*values*)[¶](#questdb.ingress.TlsCa "Link to this definition")
:   Bases: [`TaggedEnum`](#questdb.ingress.TaggedEnum "questdb.ingress.TaggedEnum")

    Verification mechanism for the server’s certificate.

    Here `webpki` refers to the
    [WebPKI library](https://github.com/rustls/webpki-roots) and
    `os` refers to the operating system’s certificate store.

    See [TLS](conf.html#sender-conf-tls) for more information.

    OsRoots *= ('os\_roots', 1)*[¶](#questdb.ingress.TlsCa.OsRoots "Link to this definition")

    PemFile *= ('pem\_file', 3)*[¶](#questdb.ingress.TlsCa.PemFile "Link to this definition")

    WebpkiAndOsRoots *= ('webpki\_and\_os\_roots', 2)*[¶](#questdb.ingress.TlsCa.WebpkiAndOsRoots "Link to this definition")

    WebpkiRoots *= ('webpki\_roots', 0)*[¶](#questdb.ingress.TlsCa.WebpkiRoots "Link to this definition")

*class* questdb.ingress.ServerTimestampType[¶](#questdb.ingress.ServerTimestampType "Link to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A placeholder value to indicate that the data should be inserted
    using a server-generated-timestamp.

    Don’t instantiate this class directly, use the singleton
    [`ServerTimestamp`](#questdb.ingress.ServerTimestamp "questdb.ingress.ServerTimestamp") instead.

    This feature is mostly provided for legacy compatibility.
    We recommend always specifying an explicit timestamp.

    Using `ServerTimestamp` will prevent QuestDB’s deduplication
    feature from working as it would generate unique rows on resubmission.

questdb.ingress.ServerTimestamp[¶](#questdb.ingress.ServerTimestamp "Link to this definition")
:   A placeholder value to indicate that the data should be inserted
    using a server-generated-timestamp.

    Don’t instantiate this class directly, use the singleton
    [`ServerTimestamp`](#questdb.ingress.ServerTimestamp "questdb.ingress.ServerTimestamp") instead.

    This feature is mostly provided for legacy compatibility.
    We recommend always specifying an explicit timestamp.

    Using `ServerTimestamp` will prevent QuestDB’s deduplication
    feature from working as it would generate unique rows on resubmission.

*class* questdb.ingress.TaggedEnum(*new\_class\_name*, */*, *names*, *\**, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[¶](#questdb.ingress.TaggedEnum "Link to this definition")
:   Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")

    Base class for tagged enums.

    *property* c\_value[¶](#questdb.ingress.TaggedEnum.c_value "Link to this definition")

    *classmethod* parse(*tag*)[¶](#questdb.ingress.TaggedEnum.parse "Link to this definition")
    :   Parse from the tag name.

    *property* tag[¶](#questdb.ingress.TaggedEnum.tag "Link to this definition")
    :   Short name.