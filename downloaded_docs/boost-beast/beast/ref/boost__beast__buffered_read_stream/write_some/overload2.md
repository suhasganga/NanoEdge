###### [buffered\_read\_stream::write\_some (2 of 2 overloads)](overload2.html "buffered_read_stream::write_some (2 of 2 overloads)")

Write some data to the stream.

###### [Synopsis](overload2.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload2.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload2.description)

This function is used to write data to the stream. The function call
will block until one or more bytes of the data has been written successfully,
or until an error occurs.

###### [Parameters](overload2.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | One or more data buffers to be written to the stream. |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](overload2.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload2.return_value)

The number of bytes written.