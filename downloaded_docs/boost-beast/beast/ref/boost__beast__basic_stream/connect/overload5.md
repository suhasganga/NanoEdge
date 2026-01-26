###### [basic\_stream::connect (5 of 10 overloads)](overload5.html "basic_stream::connect (5 of 10 overloads)")

Establishes a connection by trying each endpoint in a sequence.

###### [Synopsis](overload5.html#beast.ref.boost__beast__basic_stream.connect.overload5.synopsis)

```programlisting
template<
    class Iterator>
Iterator
connect(
    Iterator begin,
    Iterator end);
```

###### [Description](overload5.html#beast.ref.boost__beast__basic_stream.connect.overload5.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the underlying socket's `connect` function.

###### [Parameters](overload5.html#beast.ref.boost__beast__basic_stream.connect.overload5.parameters)

| Name | Description |
| --- | --- |
| `begin` | An iterator pointing to the start of a sequence of endpoints. |
| `end` | An iterator pointing to the end of a sequence of endpoints. |

###### [Return Value](overload5.html#beast.ref.boost__beast__basic_stream.connect.overload5.return_value)

An iterator denoting the successfully connected endpoint.

###### [Exceptions](overload5.html#beast.ref.boost__beast__basic_stream.connect.overload5.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. If the sequence is empty, the associated error code is `net::error::not_found`. Otherwise, contains the error from the last connection attempt. |