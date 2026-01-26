###### [basic\_stream::connect (4 of 10 overloads)](overload4.html "basic_stream::connect (4 of 10 overloads)")

Establishes a connection by trying each endpoint in a sequence.

###### [Synopsis](overload4.html#beast.ref.boost__beast__basic_stream.connect.overload4.synopsis)

```programlisting
template<
    class EndpointSequence>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints,
    error_code& ec);
```

###### [Description](overload4.html#beast.ref.boost__beast__basic_stream.connect.overload4.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the underlying socket's `connect` function.

###### [Parameters](overload4.html#beast.ref.boost__beast__basic_stream.connect.overload4.parameters)

| Name | Description |
| --- | --- |
| `endpoints` | A sequence of endpoints. |
| `ec` | Set to indicate what error occurred, if any. If the sequence is empty, set to `net::error::not_found`. Otherwise, contains the error from the last connection attempt. |

###### [Return Value](overload4.html#beast.ref.boost__beast__basic_stream.connect.overload4.return_value)

On success, the successfully connected endpoint. Otherwise, a default-constructed
endpoint.