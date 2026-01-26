###### [websocket::stream::handshake (1 of 4 overloads)](overload1.html "websocket::stream::handshake (1 of 4 overloads)")

Perform the WebSocket handshake in the client role.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.handshake.overload1.synopsis)

```programlisting
void
handshake(
    string_view host,
    string_view target);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.handshake.overload1.description)

This function is used to perform the [WebSocket
handshake](https://en.wikipedia.org/wiki/WebSocket#Protocol_handshake), required before messages can be sent and received.
During the handshake, the client sends the Websocket Upgrade HTTP request,
and the server replies with an HTTP response indicating the result of
the handshake.

The call blocks until one of the following conditions is true:

* The request is sent and the response is received.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `read_some`
and `write_some` functions.

The handshake is successful if the received HTTP response indicates the
upgrade was accepted by the server, represented by a [status-code](https://tools.ietf.org/html/rfc7230#section-3.1.2)
of [`beast::http::status::switching_protocols`](../../boost__beast__http__status.html "http::status").

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.handshake.overload1.parameters)

| Name | Description |
| --- | --- |
| `host` | The name of the remote host. This is required by the HTTP protocol to set the "Host" header field. |
| `target` | The request-target, in origin-form. The server may use the target to distinguish different services on the same listening port. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.handshake.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.handshake.overload1.example)

```programlisting
ws.handshake( "localhost" , "/" );
```

###### [See Also](overload1.html#beast.ref.boost__beast__websocket__stream.handshake.overload1.see_also)

* [Websocket
  Opening Handshake Client Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.1)
* [Host
  field (RFC7230)](https://tools.ietf.org/html/rfc7230#section-5.4)
* [request-target
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-3.1.1)
* [origin-form
  (RFC7230)](https://tools.ietf.org/html/rfc7230#section-5.3.1)