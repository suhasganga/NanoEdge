##### [websocket::stream::read\_some](read_some.html "websocket::stream::read_some")

Read some message data.

```programlisting
template<
    class DynamicBuffer>
std::size_t
read_some(
    DynamicBuffer& buffer,
    std::size_t limit);
  » more...

template<
    class DynamicBuffer>
std::size_t
read_some(
    DynamicBuffer& buffer,
    std::size_t limit,
    error_code& ec);
  » more...

template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers);
  » more...

template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers,
    error_code& ec);
  » more...
```