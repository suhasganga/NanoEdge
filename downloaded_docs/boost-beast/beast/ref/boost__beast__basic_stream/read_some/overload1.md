###### [basic\_stream::read\_some (1 of 2 overloads)](overload1.html "basic_stream::read_some (1 of 2 overloads)")

Read some data.

###### [Synopsis](overload1.html#beast.ref.boost__beast__basic_stream.read_some.overload1.synopsis)

```programlisting
template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__basic_stream.read_some.overload1.description)

This function is used to read some data from the stream.

The call blocks until one of the following is true:

* One or more bytes are read from the stream.
* An error occurs.

###### [Parameters](overload1.html#beast.ref.boost__beast__basic_stream.read_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers into which the data will be read. If the size of the buffers is zero bytes, the call always returns immediately with no error. |

###### [Return Value](overload1.html#beast.ref.boost__beast__basic_stream.read_some.overload1.return_value)

The number of bytes read.

###### [Exceptions](overload1.html#beast.ref.boost__beast__basic_stream.read_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [Remarks](overload1.html#beast.ref.boost__beast__basic_stream.read_some.overload1.remarks)

The `read_some` operation
may not receive all of the requested number of bytes. Consider using
the function `net::read` if you need to ensure that the
requested amount of data is read before the blocking operation completes.