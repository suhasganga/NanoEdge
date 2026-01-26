##### [websocket::stream::handshake](handshake.html "websocket::stream::handshake")

Perform the WebSocket handshake in the client role.

```programlisting
void
handshake(
    string_view host,
    string_view target);
  » more...

void
handshake(
    response_type& res,
    string_view host,
    string_view target);
  » more...

void
handshake(
    string_view host,
    string_view target,
    error_code& ec);
  » more...

void
handshake(
    response_type& res,
    string_view host,
    string_view target,
    error_code& ec);
  » more...
```