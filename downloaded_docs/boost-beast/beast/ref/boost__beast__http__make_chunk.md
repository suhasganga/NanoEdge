#### [http::make\_chunk](boost__beast__http__make_chunk.html "http::make_chunk")

Returns a [`chunk_body`](boost__beast__http__chunk_body.html "http::chunk_body").

##### [Synopsis](boost__beast__http__make_chunk.html#beast.ref.boost__beast__http__make_chunk.synopsis)

Defined in header `<boost/beast/http/chunk_encode.hpp>`

```programlisting
template<
    class ConstBufferSequence,
    class... Args>
chunk_body< ConstBufferSequence >
make_chunk(
    ConstBufferSequence const& buffers,
    Args&&... args);
```

##### [Description](boost__beast__http__make_chunk.html#beast.ref.boost__beast__http__make_chunk.description)

This functions constructs and returns a complete [`chunk_body`](boost__beast__http__chunk_body.html "http::chunk_body") for a chunk body represented
by the specified buffer sequence.

##### [Parameters](boost__beast__http__make_chunk.html#beast.ref.boost__beast__http__make_chunk.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers representing the chunk body. |
| `args` | Optional arguments passed to the [`chunk_body`](boost__beast__http__chunk_body.html "http::chunk_body") constructor. |

##### [Remarks](boost__beast__http__make_chunk.html#beast.ref.boost__beast__http__make_chunk.remarks)

This function is provided as a notational convenience to omit specification
of the class template arguments.