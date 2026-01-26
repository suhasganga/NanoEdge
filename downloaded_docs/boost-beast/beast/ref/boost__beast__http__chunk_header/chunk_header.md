##### [http::chunk\_header::chunk\_header](chunk_header.html "http::chunk_header::chunk_header")

Constructor.

```programlisting
explicit
chunk_header(
    std::size_t size);
  » more...

chunk_header(
    std::size_t size,
    string_view extensions);
  » more...

template<
    class ChunkExtensions>
chunk_header(
    std::size_t size,
    ChunkExtensions&& extensions);
  » more...

template<
    class ChunkExtensions,
    class Allocator>
chunk_header(
    std::size_t size,
    ChunkExtensions&& extensions,
    Allocator const& allocator);
  » more...
```

Required for *ConstBufferSequence*

```programlisting
chunk_header(
    chunk_header const&);
  » more...
```