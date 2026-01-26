##### [websocket::stream::accept](accept.html "websocket::stream::accept")

Perform the WebSocket handshake in the server role.

```programlisting
void
accept();
  » more...
```

Read and respond to a WebSocket HTTP Upgrade request.

```programlisting
void
accept(
    error_code& ec);
  » more...

template<
    class ConstBufferSequence>
void
accept(
    ConstBufferSequence const& buffers);
  » more...

template<
    class ConstBufferSequence>
void
accept(
    ConstBufferSequence const& buffers,
    error_code& ec);
  » more...
```

Respond to a WebSocket HTTP Upgrade request.

```programlisting
template<
    class Body,
    class Allocator>
void
accept(
    http::request< Body, http::basic_fields< Allocator > > const& req);
  » more...

template<
    class Body,
    class Allocator>
void
accept(
    http::request< Body, http::basic_fields< Allocator > > const& req,
    error_code& ec);
  » more...
```