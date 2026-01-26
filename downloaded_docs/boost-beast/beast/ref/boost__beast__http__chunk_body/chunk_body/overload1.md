###### [http::chunk\_body::chunk\_body (1 of 4 overloads)](overload1.html "http::chunk_body::chunk_body (1 of 4 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload1.synopsis)

```programlisting
chunk_body(
    ConstBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload1.description)

This constructs buffers representing a complete *chunk*
with no chunk extensions and having the size and contents of the specified
buffer sequence.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | A buffer sequence representing the chunk body. Although the buffers object may be copied as necessary, ownership of the underlying memory blocks is retained by the caller, which must guarantee that they remain valid while this object is in use. |

###### [See Also](overload1.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload1.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>