###### [http::chunk\_header::chunk\_header (3 of 5 overloads)](overload3.html "http::chunk_header::chunk_header (3 of 5 overloads)")

Constructor.

###### [Synopsis](overload3.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload3.synopsis)

```programlisting
template<
    class ChunkExtensions>
chunk_header(
    std::size_t size,
    ChunkExtensions&& extensions);
```

###### [Description](overload3.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload3.description)

This constructs a buffer sequence representing a *chunked-body*
size and terminating CRLF (`"\r\n"`)
with provided chunk extensions. The default allocator is used to provide
storage for the extensions object.

###### [Parameters](overload3.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload3.parameters)

| Name | Description |
| --- | --- |
| `size` | The size of the chunk body that follows. The value must be greater than zero. |
| `extensions` | The chunk extensions object. The expression `extensions.str()` must be valid, and the return type must be convertible to [`string_view`](../../boost__beast__string_view.html "string_view"). This object will be copied or moved as needed to ensure that the chunk header object retains ownership of the buffers provided by the chunk extensions object. |

###### [Remarks](overload3.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload3.remarks)

This function participates in overload resolution only if **ChunkExtensions**
meets the requirements stated above.

###### [See Also](overload3.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload3.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>