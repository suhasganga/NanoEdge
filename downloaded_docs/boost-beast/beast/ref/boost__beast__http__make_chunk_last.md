#### [http::make\_chunk\_last](boost__beast__http__make_chunk_last.html "http::make_chunk_last")

Returns a [`chunk_last`](boost__beast__http__chunk_last.html "http::chunk_last").

```programlisting
chunk_last< chunk_crlf >
make_chunk_last();
  » more...

template<
    class Trailer,
    class... Args>
chunk_last< Trailer >
make_chunk_last(
    Trailer const& trailer,
    Args&&... args);
  » more...
```