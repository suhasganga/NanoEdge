##### [websocket::stream::async\_handshake](async_handshake.html "websocket::stream::async_handshake")

Perform the WebSocket handshake asynchronously in the client role.

```programlisting
template<
    class HandshakeHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_handshake(
    string_view host,
    string_view target,
    HandshakeHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...

template<
    class HandshakeHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_handshake(
    response_type& res,
    string_view host,
    string_view target,
    HandshakeHandler&& handler = net::default_completion_token_t< executor_type >{});
  » more...
```