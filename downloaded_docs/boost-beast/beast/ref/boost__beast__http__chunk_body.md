#### [http::chunk\_body](boost__beast__http__chunk_body.html "http::chunk_body")

A *chunk*.

##### [Synopsis](boost__beast__http__chunk_body.html#beast.ref.boost__beast__http__chunk_body.synopsis)

Defined in header `<boost/beast/http/chunk_encode.hpp>`

```programlisting
template<
    class ConstBufferSequence>
class chunk_body
```

##### [Types](boost__beast__http__chunk_body.html#beast.ref.boost__beast__http__chunk_body.types)

| Name | Description |
| --- | --- |
| **[const\_iterator](boost__beast__http__chunk_body/const_iterator.html "http::chunk_body::const_iterator")** | Required for *ConstBufferSequence* |
| **[value\_type](boost__beast__http__chunk_body/value_type.html "http::chunk_body::value_type")** | Required for *ConstBufferSequence* |

##### [Member Functions](boost__beast__http__chunk_body.html#beast.ref.boost__beast__http__chunk_body.member_functions)

| Name | Description |
| --- | --- |
| **[begin](boost__beast__http__chunk_body/begin.html "http::chunk_body::begin")** | Required for *ConstBufferSequence* |
| **[chunk\_body](boost__beast__http__chunk_body/chunk_body.html "http::chunk_body::chunk_body") [constructor]** | Constructor. |
| **[end](boost__beast__http__chunk_body/end.html "http::chunk_body::end")** | Required for *ConstBufferSequence* |

##### [Description](boost__beast__http__chunk_body.html#beast.ref.boost__beast__http__chunk_body.description)

This implements a *ConstBufferSequence* representing a
*chunk*. The serialized format is as follows:

```programlisting
chunk           = chunk-size [ chunk-ext ] CRLF chunk-data CRLF
chunk-size      = 1*HEXDIG
chunk-ext       = *( ";" chunk-ext-name [ "=" chunk-ext-val ] )
chunk-ext-name  = token
chunk-ext-val   = token / quoted- string
chunk-data      = 1*OCTET ; a sequence of chunk-size octets
```

The chunk extension is optional.

To use this class, pass an instance of it to a stream algorithm as the buffer
sequence.

##### [See Also](boost__beast__http__chunk_body.html#beast.ref.boost__beast__http__chunk_body.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>