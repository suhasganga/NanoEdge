###### [buffered\_read\_stream::write\_some (1 of 2 overloads)](overload1.html "buffered_read_stream::write_some (1 of 2 overloads)")

Write some data to the stream.

###### [Synopsis](overload1.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload1.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload1.description)

This function is used to write data to the stream. The function call
will block until one or more bytes of the data has been written successfully,
or until an error occurs.

###### [Parameters](overload1.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | One or more data buffers to be written to the stream. |

###### [Return Value](overload1.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload1.return_value)

The number of bytes written.

###### [Exceptions](overload1.html#beast.ref.boost__beast__buffered_read_stream.write_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |