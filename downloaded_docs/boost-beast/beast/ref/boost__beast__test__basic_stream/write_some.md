##### [test::basic\_stream::write\_some](write_some.html "test::basic_stream::write_some")

Write some data to the stream.

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