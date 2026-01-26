##### [http::write\_some (1 of 2 overloads)](overload1.html "http::write_some (1 of 2 overloads)")

Write part of a message to a stream using a serializer.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__write_some.overload1.synopsis)

Defined in header `<boost/beast/http/write.hpp>`

```programlisting
template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write_some(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__write_some.overload1.description)

This function is used to write part of a message to a stream using a caller-provided
HTTP/1 serializer. The call will block until one of the following conditions
is true:

* One or more bytes have been transferred.
* The function [`serializer::is_done`](../boost__beast__http__serializer/is_done.html "http::serializer::is_done") returns `true`
* An error occurs on the stream.

This operation is implemented in terms of one or more calls to the stream's
`write_some` function.

The amount of data actually transferred is controlled by the behavior of
the underlying stream, subject to the buffer size limit of the serializer
obtained or set through a call to [`serializer::limit`](../boost__beast__http__serializer/limit.html "http::serializer::limit"). Setting a limit and performing
bounded work helps applications set reasonable timeouts. It also allows
application-level flow control to function correctly. For example when
using a TCP/IP based stream.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__write_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *SyncWriteStream* concept. |
| `sr` | The serializer to use. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__write_some.overload1.return_value)

The number of bytes written to the stream.

###### [Exceptions](overload1.html#beast.ref.boost__beast__http__write_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload1.html#beast.ref.boost__beast__http__write_some.overload1.see_also)

[`serializer`](../boost__beast__http__serializer.html "http::serializer")