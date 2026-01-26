###### [basic\_stream::connect (8 of 10 overloads)](overload8.html "basic_stream::connect (8 of 10 overloads)")

Establishes a connection by trying each endpoint in a sequence.

###### [Synopsis](overload8.html#beast.ref.boost__beast__basic_stream.connect.overload8.synopsis)

```programlisting
template<
    class EndpointSequence,
    class ConnectCondition>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints,
    ConnectCondition connect_condition,
    error_code& ec);
```

###### [Description](overload8.html#beast.ref.boost__beast__basic_stream.connect.overload8.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the underlying socket's `connect` function.

###### [Parameters](overload8.html#beast.ref.boost__beast__basic_stream.connect.overload8.parameters)

| Name | Description |
| --- | --- |
| `endpoints` | A sequence of endpoints. |
| `connect_condition` | A function object that is called prior to each connection attempt. The signature of the function object must be:   ```table-programlisting bool connect_condition(     error_code const & ec,     typename Protocol::endpoint const & next); ```   The `ec` parameter contains the result from the most recent connect operation. Before the first connection attempt, `ec` is always set to indicate success. The `next` parameter is the next endpoint to be tried. The function object should return true if the next endpoint should be tried, and false if it should be skipped. |
| `ec` | Set to indicate what error occurred, if any. If the sequence is empty, set to `net::error::not_found`. Otherwise, contains the error from the last connection attempt. |

###### [Return Value](overload8.html#beast.ref.boost__beast__basic_stream.connect.overload8.return_value)

On success, the successfully connected endpoint. Otherwise, a default-constructed
endpoint.