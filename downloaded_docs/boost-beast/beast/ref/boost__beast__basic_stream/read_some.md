##### [basic\_stream::read\_some](read_some.html "basic_stream::read_some")

Read some data.

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