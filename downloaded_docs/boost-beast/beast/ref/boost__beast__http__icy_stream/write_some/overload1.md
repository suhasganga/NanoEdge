###### [http::icy\_stream::write\_some (1 of 2 overloads)](overload1.html "http::icy_stream::write_some (1 of 2 overloads)")

Write some data to the stream.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__icy_stream.write_some.overload1.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__icy_stream.write_some.overload1.description)

This function is used to write data on the stream. The function call
will block until one or more bytes of data has been written successfully,
or until an error occurs.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__icy_stream.write_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The data to be written. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__icy_stream.write_some.overload1.return_value)

The number of bytes written.

###### [Exceptions](overload1.html#beast.ref.boost__beast__http__icy_stream.write_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [Remarks](overload1.html#beast.ref.boost__beast__http__icy_stream.write_some.overload1.remarks)

The `write_some` operation
may not transmit all of the data to the peer. Consider using the function
`net::write` if you need to ensure that all
data is written before the blocking operation completes.