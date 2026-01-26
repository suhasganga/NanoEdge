##### [http::parser::on\_chunk\_header](on_chunk_header.html "http::parser::on_chunk_header")

Set a callback to be invoked on each chunk header.

###### [Synopsis](on_chunk_header.html#beast.ref.boost__beast__http__parser.on_chunk_header.synopsis)

```programlisting
template<
    class Callback>
void
on_chunk_header(
    Callback& cb);
```

###### [Description](on_chunk_header.html#beast.ref.boost__beast__http__parser.on_chunk_header.description)

The callback will be invoked once for every chunk in the message payload,
as well as once for the last chunk. The invocation happens after the chunk
header is available but before any body octets have been parsed.

The extensions are provided in raw, validated form, use [`chunk_extensions::parse`](../boost__beast__http__basic_chunk_extensions/parse.html "http::basic_chunk_extensions::parse") to parse the extensions
into a structured container for easier access. The implementation type-erases
the callback without requiring a dynamic allocation. For this reason, the
callback object is passed by a non-constant reference.

###### [Example](on_chunk_header.html#beast.ref.boost__beast__http__parser.on_chunk_header.example)

```programlisting
auto callback =
    [](std::uint64_t size, string_view extensions, error_code& ec)
    {
        //...
    };
parser.on_chunk_header(callback);
```

###### [Parameters](on_chunk_header.html#beast.ref.boost__beast__http__parser.on_chunk_header.parameters)

| Name | Description |
| --- | --- |
| `cb` | The function to set, which must be invocable with this equivalent signature:   ```table-programlisting void on_chunk_header(     std::uint64_t size,         // Size of the chunk, zero for the last chunk     string_view extensions,     // The chunk-extensions in raw form     error_code& ec);            // May be set by the callback to indicate an error ``` |