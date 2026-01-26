##### [http::write (5 of 6 overloads)](overload5.html "http::write (5 of 6 overloads)")

Write a complete message to a stream.

###### [Synopsis](overload5.html#beast.ref.boost__beast__http__write.overload5.synopsis)

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
    message< isRequest, Body, Fields >& msg,
    error_code& ec);
```

###### [Description](overload5.html#beast.ref.boost__beast__http__write.overload5.description)

This function is used to write a complete message to a stream using HTTP/1.
The call will block until one of the following conditions is true:

* The entire message is written.
* An error occurs.

This operation is implemented in terms of one or more calls to the stream's
`write_some` function. The
algorithm will use a temporary [`serializer`](../boost__beast__http__serializer.html "http::serializer") with an empty chunk
decorator to produce buffers.

###### [Remarks](overload5.html#beast.ref.boost__beast__http__write.overload5.remarks)

This function only participates in overload resolution if [`is_mutable_body_writer`](../boost__beast__http__is_mutable_body_writer.html "http::is_mutable_body_writer") for *Body*
returns `true`.

###### [Parameters](overload5.html#beast.ref.boost__beast__http__write.overload5.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *SyncWriteStream* concept. |
| `msg` | The message to write. |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](overload5.html#beast.ref.boost__beast__http__write.overload5.return_value)

The number of bytes written to the stream.

###### [See Also](overload5.html#beast.ref.boost__beast__http__write.overload5.see_also)

[`message`](../boost__beast__http__message.html "http::message")