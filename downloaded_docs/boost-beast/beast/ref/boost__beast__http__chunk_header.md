#### [http::chunk\_header](boost__beast__http__chunk_header.html "http::chunk_header")

A *chunk* header.

##### [Synopsis](boost__beast__http__chunk_header.html#beast.ref.boost__beast__http__chunk_header.synopsis)

Defined in header `<boost/beast/http/chunk_encode.hpp>`

```programlisting
class chunk_header
```

##### [Types](boost__beast__http__chunk_header.html#beast.ref.boost__beast__http__chunk_header.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](boost__beast__http__chunk_header/const_iterator.html "http::chunk_header::const_iterator")** | Required for *ConstBufferSequence* |
| **[value\_type](boost__beast__http__chunk_header/value_type.html "http::chunk_header::value_type")** | Required for *ConstBufferSequence* |

##### [Member Functions](boost__beast__http__chunk_header.html#beast.ref.boost__beast__http__chunk_header.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__http__chunk_header/begin.html "http::chunk_header::begin")** | Required for *ConstBufferSequence* |
| **[chunk\_header](boost__beast__http__chunk_header/chunk_header.html "http::chunk_header::chunk_header") [constructor]** | Constructor.  — Required for *ConstBufferSequence* |
| **[end](boost__beast__http__chunk_header/end.html "http::chunk_header::end")** | Required for *ConstBufferSequence* |

##### [Description](boost__beast__http__chunk_header.html#beast.ref.boost__beast__http__chunk_header.description)

This implements a *ConstBufferSequence* representing the
header of a *chunk*. The serialized format is as follows:

```programlisting
chunk-header    = 1*HEXDIG chunk-ext CRLF
chunk-ext       = *( ";" chunk-ext-name [ "=" chunk-ext-val ] )
chunk-ext-name  = token
chunk-ext-val   = token / quoted-string
```

The chunk extension is optional. After the header and chunk body have been
serialized, it is the callers responsibility to also serialize the final
CRLF (`"\r\n"`).

This class allows the caller to emit piecewise chunk bodies, by first serializing
the chunk header using this class and then serializing the chunk body in
a series of one or more calls to a stream write operation.

To use this class, pass an instance of it to a stream algorithm as the buffer
sequence:

```programlisting
// writes "400;x\r\n"
net::write(stream, chunk_header{1024, "x" });
```

##### [See Also](boost__beast__http__chunk_header.html#beast.ref.boost__beast__http__chunk_header.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>