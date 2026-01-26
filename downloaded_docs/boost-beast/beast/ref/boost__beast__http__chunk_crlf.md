#### [http::chunk\_crlf](boost__beast__http__chunk_crlf.html "http::chunk_crlf")

A chunked encoding crlf.

##### [Synopsis](boost__beast__http__chunk_crlf.html#beast.ref.boost__beast__http__chunk_crlf.synopsis)

Defined in header `<boost/beast/http/chunk_encode.hpp>`

```programlisting
struct chunk_crlf
```

##### [Types](boost__beast__http__chunk_crlf.html#beast.ref.boost__beast__http__chunk_crlf.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](boost__beast__http__chunk_crlf/const_iterator.html "http::chunk_crlf::const_iterator")** | Required for *ConstBufferSequence* |
| **[value\_type](boost__beast__http__chunk_crlf/value_type.html "http::chunk_crlf::value_type")** | Required for *ConstBufferSequence* |

##### [Member Functions](boost__beast__http__chunk_crlf.html#beast.ref.boost__beast__http__chunk_crlf.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__http__chunk_crlf/begin.html "http::chunk_crlf::begin")** | Required for *ConstBufferSequence* |
| **[chunk\_crlf](boost__beast__http__chunk_crlf/chunk_crlf.html "http::chunk_crlf::chunk_crlf") [constructor]** | Constructor.  — Required for *ConstBufferSequence* |
| **[end](boost__beast__http__chunk_crlf/end.html "http::chunk_crlf::end")** | Required for *ConstBufferSequence* |

##### [Description](boost__beast__http__chunk_crlf.html#beast.ref.boost__beast__http__chunk_crlf.description)

This implements a *ConstBufferSequence* holding the CRLF
(`"\r\n"`) used as a
delimiter in a *chunk*.

To use this class, pass an instance of it to a stream algorithm as the buffer
sequence:

```programlisting
// writes "\r\n"
net::write(stream, chunk_crlf{});
```

##### [See Also](boost__beast__http__chunk_crlf.html#beast.ref.boost__beast__http__chunk_crlf.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>