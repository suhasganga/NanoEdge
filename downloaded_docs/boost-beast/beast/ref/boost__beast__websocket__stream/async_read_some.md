##### [websocket::stream::async\_read\_some](async_read_some.html "websocket::stream::async_read_some")

Read some message data asynchronously.

```programlisting
template<
    class DynamicBuffer,
    class ReadHandler = net::default_completion_token_t<                executor_type>>
DEDUCED
async_read_some(
    DynamicBuffer& buffer,
    std::size_t limit,
    ReadHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

template<
    class MutableBufferSequence,
    class ReadHandler = net::default_completion_token_t<                executor_type>>
DEDUCED
async_read_some(
    MutableBufferSequence const& buffers,
    ReadHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...
```