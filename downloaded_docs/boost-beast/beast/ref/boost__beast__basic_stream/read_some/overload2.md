###### [basic\_stream::read\_some (2 of 2 overloads)](overload2.html "basic_stream::read_some (2 of 2 overloads)")

Read some data.

###### [Synopsis](overload2.html#beast.ref.boost__beast__basic_stream.read_some.overload2.synopsis)

```programlisting
template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__basic_stream.read_some.overload2.description)

This function is used to read some data from the underlying socket.

The call blocks until one of the following is true:

* One or more bytes are read from the stream.
* An error occurs.

###### [Parameters](overload2.html#beast.ref.boost__beast__basic_stream.read_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers into which the data will be read. If the size of the buffers is zero bytes, the call always returns immediately with no error. |
| `ec` | Set to indicate what error occurred, if any. |

###### [Return Value](overload2.html#beast.ref.boost__beast__basic_stream.read_some.overload2.return_value)

The number of bytes read.

###### [Remarks](overload2.html#beast.ref.boost__beast__basic_stream.read_some.overload2.remarks)

The `read_some` operation
may not receive all of the requested number of bytes. Consider using
the function `net::read` if you need to ensure that the
requested amount of data is read before the blocking operation completes.