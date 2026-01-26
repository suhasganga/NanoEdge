##### [websocket::stream::read\_size\_hint](read_size_hint.html "websocket::stream::read_size_hint")

Returns a suggested maximum buffer size for the next call to read.

```programlisting
std::size_t
read_size_hint(
    std::size_t initial_size = +tcp_frame_size) const;
  » more...

template<
    class DynamicBuffer>
std::size_t
read_size_hint(
    DynamicBuffer& buffer) const;
  » more...
```