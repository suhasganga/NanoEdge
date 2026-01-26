##### [http::icy\_stream::read\_some](read_some.html "http::icy_stream::read_some")

Read some data from the stream.

```programlisting
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