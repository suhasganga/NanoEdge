##### [websocket::stream::read](read.html "websocket::stream::read")

Read a complete message.

```programlisting
template<
    class DynamicBuffer>
std::size_t
read(
    DynamicBuffer& buffer);
  » more...

template<
    class DynamicBuffer>
std::size_t
read(
    DynamicBuffer& buffer,
    error_code& ec);
  » more...
```