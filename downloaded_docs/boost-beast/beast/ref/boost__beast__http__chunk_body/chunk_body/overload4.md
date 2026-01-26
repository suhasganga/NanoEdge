###### [http::chunk\_body::chunk\_body (4 of 4 overloads)](overload4.html "http::chunk_body::chunk_body (4 of 4 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload4.synopsis)

```programlisting
template<
    class ChunkExtensions,
    class Allocator>
chunk_body(
    ConstBufferSequence const& buffers,
    ChunkExtensions&& extensions,
    Allocator const& allocator);
```

###### [Description](overload4.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload4.description)

This constructs buffers representing a complete *chunk*
with the passed chunk extensions and having the size and contents of
the specified buffer sequence. The specified allocator is used to provide
storage for the extensions object.

###### [Parameters](overload4.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload4.parameters)

| Name | Description |
| --- | --- |
| `buffers` | A buffer sequence representing the chunk body. Although the buffers object may be copied as necessary, ownership of the underlying memory blocks is retained by the caller, which must guarantee that they remain valid while this object is in use. |
| `extensions` | The chunk extensions object. The expression `extensions.str()` must be valid, and the return type must be convertible to [`string_view`](../../boost__beast__string_view.html "string_view"). This object will be copied or moved as needed to ensure that the chunk header object retains ownership of the buffers provided by the chunk extensions object. |
| `allocator` | The allocator to provide storage for the moved or copied extensions object. |

###### [Remarks](overload4.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload4.remarks)

This function participates in overload resolution only if **ChunkExtensions**
meets the requirements stated above.

###### [See Also](overload4.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload4.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>