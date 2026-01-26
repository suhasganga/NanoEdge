###### [websocket::stream::accept (5 of 6 overloads)](overload5.html "websocket::stream::accept (5 of 6 overloads)")

Respond to a WebSocket HTTP Upgrade request.

###### [Synopsis](overload5.html#beast.ref.boost__beast__websocket__stream.accept.overload5.synopsis)

```programlisting
template<
    class Body,
    class Allocator>
void
accept(
    http::request< Body, http::basic_fields< Allocator > > const& req);
```

###### [Description](overload5.html#beast.ref.boost__beast__websocket__stream.accept.overload5.description)

This function is used to perform the [WebSocket
handshake](https://en.wikipedia.org/wiki/WebSocket#Protocol_handshake), required before messages can be sent and received.
During the handshake, the client sends the Websocket Upgrade HTTP request,
and the server replies with an HTTP response indicating the result of
the handshake.

The call blocks until one of the following conditions is true:

* The response is sent.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `read_some`
and `write_some` functions.

If a valid upgrade request is received, an HTTP response with a [status-code](https://tools.ietf.org/html/rfc7230#section-3.1.2)
of [`beast::http::status::switching_protocols`](../../boost__beast__http__status.html "http::status") is sent
to the peer, otherwise a non-successful error is associated with the
operation.

###### [Parameters](overload5.html#beast.ref.boost__beast__websocket__stream.accept.overload5.parameters)

| Name | Description |
| --- | --- |
| `req` | An object containing the HTTP Upgrade request. Ownership is not transferred, the implementation will not access this object from other threads. |

###### [Exceptions](overload5.html#beast.ref.boost__beast__websocket__stream.accept.overload5.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload5.html#beast.ref.boost__beast__websocket__stream.accept.overload5.see_also)

* [Websocket
  Opening Handshake Server Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.2)