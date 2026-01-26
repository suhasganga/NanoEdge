##### [http::basic\_parser::on\_chunk\_header\_impl](on_chunk_header_impl.html "http::basic_parser::on_chunk_header_impl")

Called each time a new chunk header of a chunk encoded body is received.

###### [Synopsis](on_chunk_header_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_header_impl.synopsis)

```programlisting
void
on_chunk_header_impl(
    std::uint64_t size,
    string_view extensions,
    error_code& ec);
```

###### [Description](on_chunk_header_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_header_impl.description)

This function is invoked each time a new chunk header is received. The
function is only used when the chunked transfer encoding is present.

###### [Parameters](on_chunk_header_impl.html#beast.ref.boost__beast__http__basic_parser.on_chunk_header_impl.parameters)

| Name | Description |
| --- | --- |
| `size` | The size of this chunk, in bytes. |
| `extensions` | A string containing the entire chunk extensions. This may be empty, indicating no extensions are present. |
| `ec` | An output parameter which the function may set to indicate an error. The error will be clear before this function is invoked. |