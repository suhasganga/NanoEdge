##### [websocket::stream::write](write.html "websocket::stream::write")

Write a complete message.

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write(
    ConstBufferSequence const& buffers);
  » more...

template<
    class ConstBufferSequence>
std::size_t
write(
    ConstBufferSequence const& buffers,
    error_code& ec);
  » more...
```