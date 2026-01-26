#### [http::async\_read](boost__beast__http__async_read.html "http::async_read")

Read a complete message asynchronously from a stream using a parser.

```programlisting
template<
    class AsyncReadStream,
    class DynamicBuffer,
    bool isRequest,
    class ReadHandler = net::default_completion_token_t<            executor_type<AsyncReadStream>>>
DEDUCED
async_read(
    AsyncReadStream& stream,
    DynamicBuffer& buffer,
    basic_parser< isRequest >& parser,
    ReadHandler&& handler = net::default_completion_token_t< executor_type< AsyncReadStream > >{});
  » more...
```

Read a complete message asynchronously from a stream.

```programlisting
template<
    class AsyncReadStream,
    class DynamicBuffer,
    bool isRequest,
    class Body,
    class Allocator,
    class ReadHandler = net::default_completion_token_t<            executor_type<AsyncReadStream>>>
DEDUCED
async_read(
    AsyncReadStream& stream,
    DynamicBuffer& buffer,
    message< isRequest, Body, basic_fields< Allocator > >& msg,
    ReadHandler&& handler = net::default_completion_token_t< executor_type< AsyncReadStream > >{});
  » more...
```