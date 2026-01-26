##### [websocket::stream::async\_accept](async_accept.html "websocket::stream::async_accept")

Perform the WebSocket handshake asynchronously in the server role.

```programlisting
template<
    class AcceptHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_accept(
    AcceptHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

template<
    class ConstBufferSequence,
    class AcceptHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_accept(
    ConstBufferSequence const& buffers,
    AcceptHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

template<
    class Body,
    class Allocator,
    class AcceptHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_accept(
    http::request< Body, http::basic_fields< Allocator > > const& req,
    AcceptHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...
```