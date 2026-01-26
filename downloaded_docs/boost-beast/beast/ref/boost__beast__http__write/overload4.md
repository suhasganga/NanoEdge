##### [http::write (4 of 6 overloads)](overload4.html "http::write (4 of 6 overloads)")

Write a complete message to a stream.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__write.overload4.synopsis)

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
    message< isRequest, Body, Fields > const& msg);
```

###### [Description](overload4.html#beast.ref.boost__beast__http__write.overload4.description)

This function is used to write a complete message to a stream using HTTP/1.
The call will block until one of the following conditions is true:

* The entire message is written.
* An error occurs.

This operation is implemented in terms of one or more calls to the stream's
`write_some` function. The
algorithm will use a temporary [`serializer`](../boost__beast__http__serializer.html "http::serializer") with an empty chunk
decorator to produce buffers.

###### [Remarks](overload4.html#beast.ref.boost__beast__http__write.overload4.remarks)

This function only participates in overload resolution if [`is_mutable_body_writer`](../boost__beast__http__is_mutable_body_writer.html "http::is_mutable_body_writer") for *Body*
returns `false`.

###### [Parameters](overload4.html#beast.ref.boost__beast__http__write.overload4.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *SyncWriteStream* concept. |
| `msg` | The message to write. |

###### [Return Value](overload4.html#beast.ref.boost__beast__http__write.overload4.return_value)

The number of bytes written to the stream.

###### [Exceptions](overload4.html#beast.ref.boost__beast__http__write.overload4.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload4.html#beast.ref.boost__beast__http__write.overload4.see_also)

[`message`](../boost__beast__http__message.html "http::message")