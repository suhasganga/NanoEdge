###### [basic\_stream::write\_some (1 of 2 overloads)](overload1.html "basic_stream::write_some (1 of 2 overloads)")

Write some data.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_stream.write_some.overload1.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_stream.write_some.overload1.description)

This function is used to write some data to the stream.

The call blocks until one of the following is true:

* One or more bytes are written to the stream.
* An error occurs.

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_stream.write_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers from which the data will be written. If the size of the buffers is zero bytes, the call always returns immediately with no error. |

###### [Return Value](overload1.html#beast.ref.boost__beast__basic_stream.write_some.overload1.return_value)

The number of bytes written.

###### [Exceptions](overload1.html#beast.ref.boost__beast__basic_stream.write_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [Remarks](overload1.html#beast.ref.boost__beast__basic_stream.write_some.overload1.remarks)

The `write_some` operation
may not transmit all of the requested number of bytes. Consider using
the function `net::write` if you need to ensure that the
requested amount of data is written before the blocking operation completes.