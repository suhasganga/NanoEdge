##### [http::chunk\_body::chunk\_body](chunk_body.html "http::chunk_body::chunk_body")

Constructor.

```programlisting
explicit
chunk_body(
    ConstBufferSequence const& buffers);
  » more...

chunk_body(
    ConstBufferSequence const& buffers,
    string_view extensions);
  » more...

template<
    class ChunkExtensions>
chunk_body(
    ConstBufferSequence const& buffers,
    ChunkExtensions&& extensions);
  » more...

template<
    class ChunkExtensions,
    class Allocator>
chunk_body(
    ConstBufferSequence const& buffers,
    ChunkExtensions&& extensions,
    Allocator const& allocator);
  » more...
```