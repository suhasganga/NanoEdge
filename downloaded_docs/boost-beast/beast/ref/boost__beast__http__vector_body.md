#### [http::vector\_body](boost__beast__http__vector_body.html "http::vector_body")

A *Body* using `std::vector`

##### [Synopsis](boost__beast__http__vector_body.html#beast.ref.boost__beast__http__vector_body.synopsis)

Defined in header `<boost/beast/http/vector_body.hpp>`

```programlisting
template<
    class T,
    class Allocator = std::allocator<T>>
struct vector_body
```

##### [Types](boost__beast__http__vector_body.html#beast.ref.boost__beast__http__vector_body.types)

| Name | Description |
| --- | --- |
| **[reader](boost__beast__http__vector_body/reader.html "http::vector_body::reader")** | The algorithm for parsing the body. |
| **[value\_type](boost__beast__http__vector_body/value_type.html "http::vector_body::value_type")** | The type of container used for the body. |
| **[writer](boost__beast__http__vector_body/writer.html "http::vector_body::writer")** | The algorithm for serializing the body. |

##### [Static Member Functions](boost__beast__http__vector_body.html#beast.ref.boost__beast__http__vector_body.static_member_functions)

| Name | Description |
| --- | --- |
| **[size](boost__beast__http__vector_body/size.html "http::vector_body::size")** | Returns the payload size of the body. |

##### [Description](boost__beast__http__vector_body.html#beast.ref.boost__beast__http__vector_body.description)

This body uses `std::vector` as a memory-based container for
holding message payloads. Messages using this body type may be serialized
and parsed.