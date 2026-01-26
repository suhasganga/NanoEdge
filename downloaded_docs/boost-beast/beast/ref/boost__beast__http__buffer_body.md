#### [http::buffer\_body](boost__beast__http__buffer_body.html "http::buffer_body")

A *Body* using a caller provided buffer.

##### [Synopsis](boost__beast__http__buffer_body.html#beast.ref.boost__beast__http__buffer_body.synopsis)

Defined in header `<boost/beast/http/buffer_body.hpp>`

```programlisting
struct buffer_body
```

##### [Types](boost__beast__http__buffer_body.html#beast.ref.boost__beast__http__buffer_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__buffer_body/reader.html "http::buffer_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__buffer_body__value_type.html "http::buffer_body::value_type")** | The type of the body member when used in a message. |
| **[writer](boost__beast__http__buffer_body/writer.html "http::buffer_body::writer")** | The algorithm for serializing the body. |

##### [Description](boost__beast__http__buffer_body.html#beast.ref.boost__beast__http__buffer_body.description)

Messages using this body type may be serialized and parsed. To use this class,
the caller must initialize the members of [`buffer_body::value_type`](boost__beast__http__buffer_body__value_type.html "http::buffer_body::value_type") to appropriate values
before each call to read or write during a stream operation.