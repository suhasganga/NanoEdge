##### [http::parser::on\_chunk\_body](on_chunk_body.html "http::parser::on_chunk_body")

Set a callback to be invoked on chunk body data.

###### [Synopsis](on_chunk_body.html#beast.ref.boost__beast__http__parser.on_chunk_body.synopsis)

```programlisting
template<
    class Callback>
void
on_chunk_body(
    Callback& cb);
```

###### [Description](on_chunk_body.html#beast.ref.boost__beast__http__parser.on_chunk_body.description)

The provided function object will be invoked one or more times to provide
buffers corresponding to the chunk body for the current chunk. The callback
receives the number of octets remaining in this chunk body including the
octets in the buffer provided.

The callback must return the number of octets actually consumed. Any octets
not consumed will be presented again in a subsequent invocation of the
callback. The implementation type-erases the callback without requiring
a dynamic allocation. For this reason, the callback object is passed by
a non-constant reference.

###### [Example](on_chunk_body.html#beast.ref.boost__beast__http__parser.on_chunk_body.example)

```programlisting
auto callback =
    [](std::uint64_t remain, string_view body, error_code& ec)
    {
        //...
    };
parser.on_chunk_body(callback);
```

###### [Parameters](on_chunk_body.html#beast.ref.boost__beast__http__parser.on_chunk_body.parameters)

| Name | Description |
| --- | --- |
| `cb` | The function to set, which must be invocable with this equivalent signature:   ```table-programlisting std::size_t on_chunk_header(     std::uint64_t remain,       // Octets remaining in this chunk, includes `body`     string_view body,           // A buffer holding some or all of the remainder of the chunk body     error_code& ec);            // May be set by the callback to indicate an error ``` |