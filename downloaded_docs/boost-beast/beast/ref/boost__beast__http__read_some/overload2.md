##### [http::read\_some (2 of 2 overloads)](overload2.html "http::read_some (2 of 2 overloads)")

Read part of a message from a stream using a parser.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__read_some.overload2.synopsis)

Defined in header `<boost/beast/http/read.hpp>`

```programlisting
template<
    class SyncReadStream,
    class DynamicBuffer,
    bool isRequest>
std::size_t
read_some(
    SyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__read_some.overload2.description)

This function is used to read part of a message from a stream into an instance
of [`basic_parser`](../boost__beast__http__basic_parser.html "http::basic_parser"). The call will block
until one of the following conditions is true:

* A call to [`basic_parser::put`](../boost__beast__http__basic_parser/put.html "http::basic_parser::put") with a non-empty buffer
  sequence is successful.
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

###### [Parameters](overload2.html#beast.ref.boost__beast__http__read_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream from which the data is to be read. The type must support the *SyncReadStream* requirements. |
| `buffer` | Storage for additional bytes read by the implementation from the stream. This is both an input and an output parameter; on entry, the parser will be presented with any remaining data in the dynamic buffer's readable bytes sequence first. The type must meet the *DynamicBuffer* requirements. |
| `parser` | The parser to use. |
| `ec` | Set to the error, if any occurred. |

###### [Return Value](overload2.html#beast.ref.boost__beast__http__read_some.overload2.return_value)

The number of bytes consumed by the parser.