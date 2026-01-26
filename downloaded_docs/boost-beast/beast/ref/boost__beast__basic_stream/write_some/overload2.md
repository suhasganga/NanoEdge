###### [basic\_stream::write\_some (2 of 2 overloads)](overload2.html "basic_stream::write_some (2 of 2 overloads)")

Write some data.

###### [Synopsis](overload2.html#beast.ref.boost__beast__basic_stream.write_some.overload2.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__basic_stream.write_some.overload2.description)

This function is used to write some data to the stream.

The call blocks until one of the following is true:

* One or more bytes are written to the stream.
* An error occurs.

###### [Parameters](overload2.html#beast.ref.boost__beast__basic_stream.write_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers from which the data will be written. If the size of the buffers is zero bytes, the call always returns immediately with no error. |
| `ec` | Set to indicate what error occurred, if any. |

###### [Return Value](overload2.html#beast.ref.boost__beast__basic_stream.write_some.overload2.return_value)

The number of bytes written.

###### [Exceptions](overload2.html#beast.ref.boost__beast__basic_stream.write_some.overload2.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [Remarks](overload2.html#beast.ref.boost__beast__basic_stream.write_some.overload2.remarks)

The `write_some` operation
may not transmit all of the requested number of bytes. Consider using
the function `net::write` if you need to ensure that the
requested amount of data is written before the blocking operation completes.