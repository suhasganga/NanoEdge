###### [http::chunk\_body::chunk\_body (2 of 4 overloads)](overload2.html "http::chunk_body::chunk_body (2 of 4 overloads)")

Constructor.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload2.synopsis)

```programlisting
chunk_body(
    ConstBufferSequence const& buffers,
    string_view extensions);
```

###### [Description](overload2.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload2.description)

This constructs buffers representing a complete *chunk*
with the passed chunk extensions and having the size and contents of
the specified buffer sequence.

###### [Parameters](overload2.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | A buffer sequence representing the chunk body. Although the buffers object may be copied as necessary, ownership of the underlying memory blocks is retained by the caller, which must guarantee that they remain valid while this object is in use. |
| `extensions` | The chunk extensions string. This string must be formatted correctly as per rfc7230, using this BNF syntax:   ```table-programlisting chunk-ext       = *( ";" chunk-ext-name [ "=" chunk-ext-val ] ) chunk-ext-name  = token chunk-ext-val   = token / quoted-string ```   The data pointed to by this string view must remain valid for the lifetime of any operations performed on the object. |

###### [See Also](overload2.html#beast.ref.boost__beast__http__chunk_body.chunk_body.overload2.see_also)

<https://tools.ietf.org/html/rfc7230#section-4.1.1>