###### [buffered\_read\_stream::read\_some (2 of 2 overloads)](overload2.html "buffered_read_stream::read_some (2 of 2 overloads)")

Read some data from the stream.

###### [Synopsis](overload2.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload2.synopsis)

```programlisting
template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload2.description)

This function is used to read data from the stream. The function call
will block until one or more bytes of data has been read successfully,
or until an error occurs.

###### [Parameters](overload2.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | One or more buffers into which the data will be read. |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](overload2.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload2.return_value)

The number of bytes read, or 0 on error.