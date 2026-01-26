###### [http::chunk\_body::chunk\_body (3 of 4 overloads)](overload3.html "http::chunk_body::chunk_body (3 of 4 overloads)")

Constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload3.synopsis)

```programlisting
template<
    class ChunkExtensions>
chunk_body(
    ConstBufferSequence const& buffers,
    ChunkExtensions&& extensions);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload3.description)

This constructs buffers representing a complete *chunk*
with the passed chunk extensions and having the size and contents of
the specified buffer sequence. The default allocator is used to provide
storage for the extensions object.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload3.parameters)

| Name | Description |
| --- | --- |
| `buffers` | A buffer sequence representing the chunk body. Although the buffers object may be copied as necessary, ownership of the underlying memory blocks is retained by the caller, which must guarantee that they remain valid while this object is in use. |
| `extensions` | The chunk extensions object. The expression `extensions.str()` must be valid, and the return type must be convertible to [`string_view`](../../boost__beast__string_view.html "string_view"). This object will be copied or moved as needed to ensure that the chunk header object retains ownership of the buffers provided by the chunk extensions object. |

###### [Remarks](overload3.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload3.remarks)

This function participates in overload resolution only if **ChunkExtensions**
meets the requirements stated above.

###### [See Also](overload3.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload3.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>