###### [basic\_stream::connect (3 of 10 overloads)](overload3.html "basic_stream::connect (3 of 10 overloads)")

Establishes a connection by trying each endpoint in a sequence.

###### [Synopsis](overload3.html#beast.ref.boost__beast__basic_stream.connect.overload3.synopsis)

```programlisting
template<
    class EndpointSequence>
Protocol::endpoint
connect(
    EndpointSequence const& endpoints);
```

###### [Description](overload3.html#beast.ref.boost__beast__basic_stream.connect.overload3.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the underlying socket's `connect` function.

###### [Parameters](overload3.html#beast.ref.boost__beast__basic_stream.connect.overload3.parameters)

| Name | Description |
| --- | --- |
| `endpoints` | A sequence of endpoints. |

###### [Return Value](overload3.html#beast.ref.boost__beast__basic_stream.connect.overload3.return_value)

The successfully connected endpoint.

###### [Exceptions](overload3.html#beast.ref.boost__beast__basic_stream.connect.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. If the sequence is empty, the associated error code is `net::error::not_found`. Otherwise, contains the error from the last connection attempt. |