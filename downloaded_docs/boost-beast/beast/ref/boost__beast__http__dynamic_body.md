#### [http::dynamic\_body](boost__beast__http__dynamic_body.html "http::dynamic_body")

A dynamic message body represented by a [`multi_buffer`](boost__beast__multi_buffer.html "multi_buffer").

##### [Synopsis](boost__beast__http__dynamic_body.html#beast.ref.boost__beast__http__dynamic_body.synopsis)

Defined in header `<boost/beast/http/dynamic_body.hpp>`

```programlisting
using dynamic_body = basic_dynamic_body< multi_buffer >;
```

##### [Types](boost__beast__http__dynamic_body.html#beast.ref.boost__beast__http__dynamic_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__basic_dynamic_body/reader.html "http::basic_dynamic_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__basic_dynamic_body/value_type.html "http::basic_dynamic_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__basic_dynamic_body/writer.html "http::basic_dynamic_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__http__dynamic_body.html#beast.ref.boost__beast__http__dynamic_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__basic_dynamic_body/size.html "http::basic_dynamic_body::size")** | Returns the payload size of the body. |

This body uses a *DynamicBuffer* as a memory-based container
for holding message payloads. Messages using this body type may be serialized
and parsed.

##### [Description](boost__beast__http__dynamic_body.html#beast.ref.boost__beast__http__dynamic_body.description)

Meets the requirements of *Body*.