###### [websocket::stream::async\_accept (3 of 3 overloads)](overload3.html "websocket::stream::async_accept (3 of 3 overloads)")

Perform the WebSocket handshake asynchronously in the server role.

###### [Synopsis](overload3.html#beast.ref.boost__beast__websocket__stream.async_accept.overload3.synopsis)

```programlisting
template<
    class Body,
    class Allocator,
    class AcceptHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_accept(
    http::request< Body, http::basic_fields< Allocator > > const& req,
    AcceptHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](overload3.html#beast.ref.boost__beast__websocket__stream.async_accept.overload3.description)

This initiating function is used to asynchronously begin performing the
[WebSocket
handshake](https://en.wikipedia.org/wiki/WebSocket#Protocol_handshake), required before messages can be sent and received.
During the handshake, the client sends the Websocket Upgrade HTTP request,
and the server replies with an HTTP response indicating the result of
the handshake.

This call always returns immediately. The asynchronous operation will
continue until one of the following conditions is true:

* The request is received and the response is sent.
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_read_some`
and `async_write_some`
functions. No other operation may be performed on the stream until this
operation completes.

If a valid upgrade request is received, an HTTP response with a [status-code](https://tools.ietf.org/html/rfc7230#section-3.1.2)
of [`beast::http::status::switching_protocols`](../../boost__beast__http__status.html "http::status") is sent
to the peer, otherwise a non-successful error is associated with the
operation.

###### [Parameters](overload3.html#beast.ref.boost__beast__websocket__stream.async_accept.overload3.parameters)

| Name | Description |
| --- | --- |
| `req` | An object containing the HTTP Upgrade request. Ownership is not transferred, the implementation will not access this object from other threads. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & ec    // Result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [See Also](overload3.html#beast.ref.boost__beast__websocket__stream.async_accept.overload3.see_also)

* [Websocket
  Opening Handshake Server Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.2)