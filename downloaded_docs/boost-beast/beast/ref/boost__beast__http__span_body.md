#### [http::span\_body](boost__beast__http__span_body.html "http::span_body")

A *Body* using [`span`](boost__beast__span.html "span").

##### [Synopsis](boost__beast__http__span_body.html#beast.ref.boost__beast__http__span_body.synopsis)

Defined in header `<boost/beast/http/span_body.hpp>`

```programlisting
template<
    class T>
struct span_body
```

##### [Types](boost__beast__http__span_body.html#beast.ref.boost__beast__http__span_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__span_body/reader.html "http::span_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__span_body/value_type.html "http::span_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__span_body/writer.html "http::span_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__http__span_body.html#beast.ref.boost__beast__http__span_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__span_body/size.html "http::span_body::size")** | Returns the payload size of the body. |

##### [Description](boost__beast__http__span_body.html#beast.ref.boost__beast__http__span_body.description)

This body uses [`span`](boost__beast__span.html "span") as a memory-based container
for holding message payloads. The container represents a non-owning reference
to a contiguous area of memory. Messages using this body type may be serialized
and parsed.

Unlike [`buffer_body`](boost__beast__http__buffer_body.html "http::buffer_body"), only one buffer may
be provided during a parse or serialize operation.