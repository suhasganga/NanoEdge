##### [http::write (2 of 6 overloads)](overload2.html "http::write (2 of 6 overloads)")

Write a complete message to a stream using a serializer.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__write.overload2.synopsis)

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
    serializer< isRequest, Body, Fields >& sr,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__write.overload2.description)

This function is used to write a complete message to a stream using a caller-provided
HTTP/1 serializer. The call will block until one of the following conditions
is true:

* The function [`serializer::is_done`](../boost__beast__http__serializer/is_done.html "http::serializer::is_done") returns `true`
* An error occurs.

This operation is implemented in terms of one or more calls to the stream's
`write_some` function.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__write.overload2.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *SyncWriteStream* concept. |
| `sr` | The serializer to use. |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](overload2.html#beast.ref.boost__beast__http__write.overload2.return_value)

The number of bytes written to the stream.

###### [See Also](overload2.html#beast.ref.boost__beast__http__write.overload2.see_also)

[`serializer`](../boost__beast__http__serializer.html "http::serializer")