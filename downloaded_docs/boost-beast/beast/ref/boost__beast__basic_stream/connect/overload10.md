###### [basic\_stream::connect (10 of 10 overloads)](overload10.html "basic_stream::connect (10 of 10 overloads)")

Establishes a connection by trying each endpoint in a sequence.

###### [Synopsis](overload10.html#beast.ref.boost__beast__basic_stream.connect.overload10.synopsis)

```programlisting
template<
    class Iterator,
    class ConnectCondition>
Iterator
connect(
    Iterator begin,
    Iterator end,
    ConnectCondition connect_condition,
    error_code& ec);
```

###### [Description](overload10.html#beast.ref.boost__beast__basic_stream.connect.overload10.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the underlying socket's `connect` function.

###### [Parameters](overload10.html#beast.ref.boost__beast__basic_stream.connect.overload10.parameters)

| Name | Description |
| --- | --- |
| `begin` | An iterator pointing to the start of a sequence of endpoints. |
| `end` | An iterator pointing to the end of a sequence of endpoints. |
| `connect_condition` | A function object that is called prior to each connection attempt. The signature of the function object must be:   ```table-programlisting bool connect_condition(     error_code const & ec,     typename Protocol::endpoint const & next); ```   The `ec` parameter contains the result from the most recent connect operation. Before the first connection attempt, `ec` is always set to indicate success. The `next` parameter is the next endpoint to be tried. The function object should return true if the next endpoint should be tried, and false if it should be skipped. |
| `ec` | Set to indicate what error occurred, if any. If the sequence is empty, set to `net::error::not_found`. Otherwise, contains the error from the last connection attempt. |

###### [Return Value](overload10.html#beast.ref.boost__beast__basic_stream.connect.overload10.return_value)

On success, an iterator denoting the successfully connected endpoint.
Otherwise, the end iterator.