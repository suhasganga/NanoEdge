###### [websocket::stream::async\_handshake (2 of 2 overloads)](overload2.html "websocket::stream::async_handshake (2 of 2 overloads)")

Perform the WebSocket handshake asynchronously in the client role.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.async_handshake.overload2.synopsis)

```programlisting
template<
    class HandshakeHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_handshake(
    response_type& res,
    string_view host,
    string_view target,
    HandshakeHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.async_handshake.overload2.description)

This initiating function is used to asynchronously begin performing the
[WebSocket
handshake](https://en.wikipedia.org/wiki/WebSocket#Protocol_handshake), required before messages can be sent and received.
During the handshake, the client sends the Websocket Upgrade HTTP request,
and the server replies with an HTTP response indicating the result of
the handshake.

This call always returns immediately. The asynchronous operation will
continue until one of the following conditions is true:

* The request is sent and the response is received.
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_read_some`
and `async_write_some`
functions. No other operation may be performed on the stream until this
operation completes.

The handshake is successful if the received HTTP response indicates the
upgrade was accepted by the server, represented by a [status-code](https://tools.ietf.org/html/rfc7230#section-3.1.2)
of [`beast::http::status::switching_protocols`](../../boost__beast__http__status.html "http::status").

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.async_handshake.overload2.parameters)

| Name | Description |
| --- | --- |
| `res` | The HTTP Upgrade response returned by the remote endpoint. The caller may use the response to access any additional information sent by the server. This object will be assigned before the completion handler is invoked. |
| `host` | The name of the remote host. This is required by the HTTP protocol to set the "Host" header field. The implementation will not access the string data after the initiating function returns. |
| `target` | The request-target, in origin-form. The server may use the target to distinguish different services on the same listening port. The implementation will not access the string data after the initiating function returns. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & ec    // Result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Example](overload2.html#beast.ref.boost__beast__websocket__stream.async_handshake.overload2.example)

```programlisting
response_type res;
ws.async_handshake(res, "localhost" , "/" ,
    [&res](error_code ec)
    {
        if (ec)
            std::cerr << "Error: " << ec.message() << "\n" ;
        else
            std::cout << res;

    });
```

###### [See Also](overload2.html#beast.ref.boost__beast__websocket__stream.async_handshake.overload2.see_also)

* [Websocket
  Opening Handshake Client Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.1)
* [Host
  field (RFC7230)](https://tools.ietf.org/html/rfc7230#section-5.4)
* [request-target
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-3.1.1)
* [origin-form
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-5.3.1)