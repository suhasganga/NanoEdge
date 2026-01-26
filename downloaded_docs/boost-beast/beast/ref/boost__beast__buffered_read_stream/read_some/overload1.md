###### [buffered\_read\_stream::read\_some (1 of 2 overloads)](overload1.html "buffered_read_stream::read_some (1 of 2 overloads)")

Read some data from the stream.

###### [Synopsis](overload1.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload1.synopsis)

```programlisting
template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload1.description)

This function is used to read data from the stream. The function call
will block until one or more bytes of data has been read successfully,
or until an error occurs.

###### [Parameters](overload1.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | One or more buffers into which the data will be read. |

###### [Return Value](overload1.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload1.return_value)

The number of bytes read.

###### [Exceptions](overload1.html#beast.ref.boost__beast__buffered_read_stream.read_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |