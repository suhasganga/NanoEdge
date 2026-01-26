###### [http::chunk\_header::chunk\_header (4 of 5 overloads)](overload4.html "http::chunk_header::chunk_header (4 of 5 overloads)")

Constructor.

###### [Synopsis](overload4.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload4.synopsis)

```programlisting
template<
    class ChunkExtensions,
    class Allocator>
chunk_header(
    std::size_t size,
    ChunkExtensions&& extensions,
    Allocator const& allocator);
```

###### [Description](overload4.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload4.description)

This constructs a buffer sequence representing a *chunked-body*
size and terminating CRLF (`"\r\n"`)
with provided chunk extensions. The specified allocator is used to provide
storage for the extensions object.

###### [Parameters](overload4.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload4.parameters)

| Name | Description |
| --- | --- |
| `size` | The size of the chunk body that follows. The value be greater than zero. |
| `extensions` | The chunk extensions object. The expression `extensions.str()` must be valid, and the return type must be convertible to [`string_view`](../../boost__beast__string_view.html "string_view"). This object will be copied or moved as needed to ensure that the chunk header object retains ownership of the buffers provided by the chunk extensions object. |
| `allocator` | The allocator to provide storage for the moved or copied extensions object. |

###### [Remarks](overload4.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload4.remarks)

This function participates in overload resolution only if **ChunkExtensions**
meets the requirements stated above.

###### [See Also](overload4.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload4.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>