##### [basic\_stream::write\_some](write_some.html "basic_stream::write_some")

Write some data.

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers);
  » more...

template<
    class ConstBufferSequence>
std::size_t
write_some(
    ConstBufferSequence const& buffers,
    error_code& ec);
  » more...
```