#### [http::serializer](boost__beast__http__serializer.html "http::serializer")

Provides buffer oriented HTTP message serialization functionality.

##### [Synopsis](boost__beast__http__serializer.html#beast.ref.boost__beast__http__serializer.synopsis)

Defined in header `<boost/beast/http/serializer.hpp>`

```programlisting
template<
    bool isRequest,
    class Body,
    class Fields = fields>
class serializer
```

##### [Types](boost__beast__http__serializer.html#beast.ref.boost__beast__http__serializer.types)

| Name | Description |
| --- | --- |
| **[value\_type](boost__beast__http__serializer/value_type.html "http::serializer::value_type")** | The type of message this serializer uses. |

##### [Member Functions](boost__beast__http__serializer.html#beast.ref.boost__beast__http__serializer.member_functions)

| Name | Description |
| --- | --- |
| **[consume](boost__beast__http__serializer/consume.html "http::serializer::consume")** | Consume buffer octets in the serialization. |
| **[get](boost__beast__http__serializer/get.html "http::serializer::get")** | Returns the message being serialized. |
| **[is\_done](boost__beast__http__serializer/is_done.html "http::serializer::is_done")** | Return `true` if serialization is complete. |
| **[is\_header\_done](boost__beast__http__serializer/is_header_done.html "http::serializer::is_header_done")** | Return `true` if serialization of the header is complete. |
| **[limit](boost__beast__http__serializer/limit.html "http::serializer::limit")** | Returns the serialized buffer size limit.  — Set the serialized buffer size limit. |
| **[next](boost__beast__http__serializer/next.html "http::serializer::next")** | Returns the next set of buffers in the serialization. |
| **[operator=](boost__beast__http__serializer/operator_eq_.html "http::serializer::operator=")** | Assignment. |
| **[serializer](boost__beast__http__serializer/serializer.html "http::serializer::serializer") [constructor]** | Move Constructor.  — Copy Constructor.  — Constructor. |
| **[split](boost__beast__http__serializer/split.html "http::serializer::split")** | Returns `true` if we will pause after writing the complete header.  — Set whether the header and body are written separately. |
| **[writer\_impl](boost__beast__http__serializer/writer_impl.html "http::serializer::writer_impl")** | Provides low-level access to the associated *BodyWriter* |

##### [Description](boost__beast__http__serializer.html#beast.ref.boost__beast__http__serializer.description)

An object of this type is used to serialize a complete HTTP message into
a sequence of octets. To use this class, construct an instance with the message
to be serialized. The implementation will automatically perform chunk encoding
if the contents of the message indicate that chunk encoding is required.

Chunked output produced by the serializer never contains chunk extensions
or trailers, and the location of chunk boundaries is not specified. If callers
require chunk extensions, trailers, or control over the exact contents of
each chunk they should use the serializer to write just the message header,
and then assume control over serializing the chunked payload by using the
chunk buffer sequence types [`chunk_body`](boost__beast__http__chunk_body.html "http::chunk_body"), [`chunk_crlf`](boost__beast__http__chunk_crlf.html "http::chunk_crlf"), [`chunk_header`](boost__beast__http__chunk_header.html "http::chunk_header"), and [`chunk_last`](boost__beast__http__chunk_last.html "http::chunk_last").

##### [Remarks](boost__beast__http__serializer.html#beast.ref.boost__beast__http__serializer.remarks)

Moving or copying the serializer after the first call to [`serializer::next`](boost__beast__http__serializer/next.html "http::serializer::next") results in undefined behavior.
Try to heap-allocate the serializer object if you need to move the serializer
between multiple async operations (for example, between a call to `async_write_header` and `async_write`).

##### [Template Parameters](boost__beast__http__serializer.html#beast.ref.boost__beast__http__serializer.template_parameters)

| Type | Description |
| --- | --- |
| `isRequest` | `true` if the message is a request. |
| `Body` | The body type of the message. |
| `Fields` | The type of fields in the message. |