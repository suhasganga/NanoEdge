##### [websocket::stream::write\_some](write_some.html "websocket::stream::write_some")

Write some message data.

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    bool fin,
    ConstBufferSequence const& buffers);
  » more...

template<
    class ConstBufferSequence>
std::size_t
write_some(
    bool fin,
    ConstBufferSequence const& buffers,
    error_code& ec);
  » more...
```