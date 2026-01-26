#### [http::basic\_dynamic\_body](boost__beast__http__basic_dynamic_body.html "http::basic_dynamic_body")

A *Body* using a *DynamicBuffer*

##### [Synopsis](boost__beast__http__basic_dynamic_body.html#beast.ref.boost__beast__http__basic_dynamic_body.synopsis)

Defined in header `<boost/beast/http/basic_dynamic_body.hpp>`

```programlisting
template<
    class DynamicBuffer>
struct basic_dynamic_body
```

##### [Types](boost__beast__http__basic_dynamic_body.html#beast.ref.boost__beast__http__basic_dynamic_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__basic_dynamic_body/reader.html "http::basic_dynamic_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__basic_dynamic_body/value_type.html "http::basic_dynamic_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__basic_dynamic_body/writer.html "http::basic_dynamic_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__http__basic_dynamic_body.html#beast.ref.boost__beast__http__basic_dynamic_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__basic_dynamic_body/size.html "http::basic_dynamic_body::size")** | Returns the payload size of the body. |

##### [Description](boost__beast__http__basic_dynamic_body.html#beast.ref.boost__beast__http__basic_dynamic_body.description)

This body uses a *DynamicBuffer* as a memory-based container
for holding message payloads. Messages using this body type may be serialized
and parsed.