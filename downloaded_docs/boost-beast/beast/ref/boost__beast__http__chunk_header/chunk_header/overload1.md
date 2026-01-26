###### [http::chunk\_header::chunk\_header (1 of 5 overloads)](overload1.html "http::chunk_header::chunk_header (1 of 5 overloads)")

Constructor.

###### [Synopsis](overload1.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload1.synopsis)

```programlisting
chunk_header(
    std::size_t size);
```

###### [Description](overload1.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload1.description)

This constructs a buffer sequence representing a *chunked-body*
size and terminating CRLF (`"\r\n"`)
with no chunk extensions.

###### [Parameters](overload1.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload1.parameters)

| Name | Description |
| --- | --- |
| `size` | The size of the chunk body that follows. The value must be greater than zero. |

###### [See Also](overload1.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload1.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1>