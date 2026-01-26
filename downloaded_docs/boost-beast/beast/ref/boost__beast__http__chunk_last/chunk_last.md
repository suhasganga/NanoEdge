##### [http::chunk\_last::chunk\_last](chunk_last.html "http::chunk_last::chunk_last")

Constructor.

```programlisting
chunk_last();
  » more...

explicit
chunk_last(
    Trailer const& trailer);
  » more...

template<
    class Allocator>
chunk_last(
    Trailer const& trailer,
    Allocator const& allocator);
  » more...
```

Required for *ConstBufferSequence*

```programlisting
chunk_last(
    chunk_last const&);
  » more...
```