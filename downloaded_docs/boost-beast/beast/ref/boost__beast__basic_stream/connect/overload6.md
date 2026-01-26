###### [basic\_stream::connect (6 of 10 overloads)](overload6.html "basic_stream::connect (6 of 10 overloads)")

Establishes a connection by trying each endpoint in a sequence.

###### [Synopsis](overload6.html#beast.ref.boost__beast__basic_stream.connect.overload6.synopsis)

```programlisting
template<
    class Iterator>
Iterator
connect(
    Iterator begin,
    Iterator end,
    error_code& ec);
```

###### [Description](overload6.html#beast.ref.boost__beast__basic_stream.connect.overload6.description)

This function attempts to connect the stream to one of a sequence of
endpoints by trying each endpoint until a connection is successfully
established. The underlying socket is automatically opened if needed.
An automatically opened socket is not returned to the closed state upon
failure.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the underlying socket's `connect` function.

###### [Parameters](overload6.html#beast.ref.boost__beast__basic_stream.connect.overload6.parameters)

| Name | Description |
| --- | --- |
| `begin` | An iterator pointing to the start of a sequence of endpoints. |
| `end` | An iterator pointing to the end of a sequence of endpoints. |
| `ec` | Set to indicate what error occurred, if any. If the sequence is empty, set to boost::asio::error::not\_found. Otherwise, contains the error from the last connection attempt. |

###### [Return Value](overload6.html#beast.ref.boost__beast__basic_stream.connect.overload6.return_value)

On success, an iterator denoting the successfully connected endpoint.
Otherwise, the end iterator.