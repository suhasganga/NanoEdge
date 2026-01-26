##### [websocket::stream::close](close.html "websocket::stream::close")

Perform the WebSocket closing handshake and close the underlying stream.

```programlisting
void
close(
    close_reason const& cr);
  » more...

void
close(
    close_reason const& cr,
    error_code& ec);
  » more...
```