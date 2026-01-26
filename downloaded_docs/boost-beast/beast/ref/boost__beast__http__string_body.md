#### [http::string\_body](boost__beast__http__string_body.html "http::string_body")

A *Body* using `std::string`

##### [Synopsis](boost__beast__http__string_body.html#beast.ref.boost__beast__http__string_body.synopsis)

Defined in header `<boost/beast/http/string_body.hpp>`

```programlisting
using string_body = basic_string_body< char >;
```

##### [Types](boost__beast__http__string_body.html#beast.ref.boost__beast__http__string_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__basic_string_body/reader.html "http::basic_string_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__basic_string_body/value_type.html "http::basic_string_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__basic_string_body/writer.html "http::basic_string_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__http__string_body.html#beast.ref.boost__beast__http__string_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__basic_string_body/size.html "http::basic_string_body::size")** | Returns the payload size of the body. |

This body uses `std::basic_string` as a memory-based container
for holding message payloads. Messages using this body type may be serialized
and parsed.