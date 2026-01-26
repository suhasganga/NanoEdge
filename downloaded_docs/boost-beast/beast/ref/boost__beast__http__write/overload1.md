##### [http::write (1 of 6 overloads)](overload1.html "http::write (1 of 6 overloads)")

Write a complete message to a stream using a serializer.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__write.overload1.synopsis)

Defined in header `<boost/beast/http/write.hpp>`

```programlisting
template<
    class SyncWriteStream,
    bool isRequest,
    class Body,
    class Fields>
std::size_t
write(
    SyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__write.overload1.description)

This function is used to write a complete message to a stream using a caller-provided
HTTP/1 serializer. The call will block until one of the following conditions
is true:

* The function [`serializer::is_done`](../boost__beast__http__serializer/is_done.html "http::serializer::is_done") returns `true`
* An error occurs.

This operation is implemented in terms of one or more calls to the stream's
`write_some` function.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__write.overload1.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *SyncWriteStream* concept. |
| `sr` | The serializer to use. |

###### [Return Value](overload1.html#beast.ref.boost__beast__http__write.overload1.return_value)

The number of bytes written to the stream.

###### [Exceptions](overload1.html#beast.ref.boost__beast__http__write.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload1.html#beast.ref.boost__beast__http__write.overload1.see_also)

[`serializer`](../boost__beast__http__serializer.html "http::serializer")