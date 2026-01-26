#### [http::chunk\_extensions](boost__beast__http__chunk_extensions.html "http::chunk_extensions")

A set of chunk extensions.

##### [Synopsis](boost__beast__http__chunk_extensions.html#beast.ref.boost__beast__http__chunk_extensions.synopsis)

Defined in header `<boost/beast/http/chunk_encode.hpp>`

```programlisting
using chunk_extensions = basic_chunk_extensions< std::allocator< char > >;
```

##### [Types](boost__beast__http__chunk_extensions.html#beast.ref.boost__beast__http__chunk_extensions.types)

| Name | Description |
| --- | --- |
| **[value\_type](boost__beast__http__basic_chunk_extensions/value_type.html "http::basic_chunk_extensions::value_type")** | The type of value when iterating. |

##### [Member Functions](boost__beast__http__chunk_extensions.html#beast.ref.boost__beast__http__chunk_extensions.member_functions)

| Name | Description |
| --- | --- |
| **[basic\_chunk\_extensions](boost__beast__http__basic_chunk_extensions/basic_chunk_extensions.html "http::basic_chunk_extensions::basic_chunk_extensions")** | Constructor. |
| **[begin](boost__beast__http__basic_chunk_extensions/begin.html "http::basic_chunk_extensions::begin")** |  |
| **[clear](boost__beast__http__basic_chunk_extensions/clear.html "http::basic_chunk_extensions::clear")** | Clear the chunk extensions. |
| **[end](boost__beast__http__basic_chunk_extensions/end.html "http::basic_chunk_extensions::end")** |  |
| **[insert](boost__beast__http__basic_chunk_extensions/insert.html "http::basic_chunk_extensions::insert")** | Insert an extension name with an empty value.  — Insert an extension value. |
| **[parse](boost__beast__http__basic_chunk_extensions/parse.html "http::basic_chunk_extensions::parse")** | Parse a set of chunk extensions. |
| **[str](boost__beast__http__basic_chunk_extensions/str.html "http::basic_chunk_extensions::str")** | Return the serialized representation of the chunk extension. |

This container stores a set of chunk extensions suited for use with [`chunk_header`](boost__beast__http__chunk_header.html "http::chunk_header")
and [`chunk_body`](boost__beast__http__chunk_body.html "http::chunk_body"). The container may be
iterated to access the extensions in their structured form.

Meets the requirements of ChunkExtensions