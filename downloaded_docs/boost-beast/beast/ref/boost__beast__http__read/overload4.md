##### [http::read (4 of 4 overloads)](overload4.html "http::read (4 of 4 overloads)")

Read a complete message from a stream.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__read.overload4.synopsis)

Defined in header `<boost/beast/http/read.hpp>`

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest,
    class Body,
    class Allocator>
std::size_t
read(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    message< isRequest, Body, basic_fields< Allocator > >& msg,
    error_code& ec);
```

###### [Description](overload4.html#beast.ref.boost__beast__http__read.overload4.description)

This function is used to read a complete message from a stream into an
instance of [`message`](../boost__beast__http__message.html "http::message"). The call will block until
one of the following conditions is true:

* The entire message is read in.
* An error occurs.

This operation is implemented in terms of one or more calls to the stream's
`read_some` function. The
implementation may read additional bytes from the stream that lie past
the end of the message being read. These additional bytes are stored in
the dynamic buffer, which must be preserved for subsequent reads.

If the end of file error is received while reading from the stream, then
the error returned from this function will be:

* [`error::end_of_stream`](../boost__beast__http__error.html "http::error")
  if no bytes were parsed, or
* [`error::partial_message`](../boost__beast__http__error.html "http::error")
  if any bytes were parsed but the message was incomplete, otherwise:
* A successful result. The next attempt to read will return [`error::end_of_stream`](../boost__beast__http__error.html "http::error")

###### [Parameters](overload4.html#beast.ref.boost__beast__http__read.overload4.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream from which the data is to be read. The type must meet the *SyncReadStream* requirements. |
| `buffer` | Storage for additional bytes read by the implementation from the stream. This is both an input and an output parameter; on entry, the parser will be presented with any remaining data in the dynamic buffer's readable bytes sequence first. The type must meet the *DynamicBuffer* requirements. |
| `msg` | The container in which to store the message contents. This message container should not have previous contents, otherwise the behavior is undefined. The type must be meet the *MoveAssignable* and *MoveConstructible* requirements. |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](overload4.html#beast.ref.boost__beast__http__read.overload4.return_value)

The number of bytes consumed by the parser.

###### [Remarks](overload4.html#beast.ref.boost__beast__http__read.overload4.remarks)

The implementation will call [`basic_parser::eager`](../boost__beast__http__basic_parser/eager.html "http::basic_parser::eager") with the value `true` on the parser passed in.