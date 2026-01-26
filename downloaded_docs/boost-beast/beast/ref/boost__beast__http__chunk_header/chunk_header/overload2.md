###### [http::chunk\_header::chunk\_header (2 of 5 overloads)](overload2.html "http::chunk_header::chunk_header (2 of 5 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload2.synopsis)

```programlisting
chunk_header(
    std::size_t size,
    string_view extensions);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload2.description)

This constructs a buffer sequence representing a *chunked-body*
size and terminating CRLF (`"\r\n"`)
with provided chunk extensions.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload2.parameters)

| Name | Description |
| --- | --- |
| `size` | The size of the chunk body that follows. The value must be greater than zero. |
| `extensions` | The chunk extensions string. This string must be formatted correctly as per rfc7230, using this BNF syntax:   ```table-programlisting chunk-ext       = *( ";" chunk-ext-name [ "=" chunk-ext-val ] ) chunk-ext-name  = token chunk-ext-val   = token / quoted-string ```   The data pointed to by this string view must remain valid for the lifetime of any operations performed on the object. |

###### [See Also](overload2.html#beast.ref.boost__beast__http__chunk_header.chunk_header.overload2.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1.1>