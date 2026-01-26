###### [websocket::stream::accept (3 of 6 overloads)](overload3.html "websocket::stream::accept (3 of 6 overloads)")

Read and respond to a WebSocket HTTP Upgrade request.

###### [Synopsis](overload3.html#beast.ref.boost__beast__websocket__stream.accept.overload3.synopsis)

```programlisting
template<
    class ConstBufferSequence>
void
accept(
    ConstBufferSequence const& buffers);
```

###### [Description](overload3.html#beast.ref.boost__beast__websocket__stream.accept.overload3.description)

This function is used to perform the [WebSocket
handshake](https://en.wikipedia.org/wiki/WebSocket#Protocol_handshake), required before messages can be sent and received.
During the handshake, the client sends the Websocket Upgrade HTTP request,
and the server replies with an HTTP response indicating the result of
the handshake.

The call blocks until one of the following conditions is true:

* The request is received and the response is sent.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `read_some`
and `write_some` functions.

If a valid upgrade request is received, an HTTP response with a [status-code](https://tools.ietf.org/html/rfc7230#section-3.1.2)
of [`beast::http::status::switching_protocols`](../../boost__beast__http__status.html "http::status") is sent
to the peer, otherwise a non-successful error is associated with the
operation.

If the request size exceeds the capacity of the stream's internal buffer,
the error [`error::buffer_overflow`](../../boost__beast__websocket__error.html "websocket::error") will be indicated.
To handle larger requests, an application should read the HTTP request
directly using [`http::read`](../../boost__beast__http__read.html "http::read")  and then pass the request
to the appropriate overload of [`accept`](../accept.html "websocket::stream::accept") or [`async_accept`](../async_accept.html "websocket::stream::async_accept")

###### [Parameters](overload3.html#beast.ref.boost__beast__websocket__stream.accept.overload3.parameters)

| Name | Description |
| --- | --- |
| `buffers` | Caller provided data that has already been received on the stream. The implementation will copy the caller provided data before the function returns. |

###### [Exceptions](overload3.html#beast.ref.boost__beast__websocket__stream.accept.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload3.html#beast.ref.boost__beast__websocket__stream.accept.overload3.see_also)

* [Websocket
  Opening Handshake Server Requirements (RFC6455)](https://tools.ietf.org/html/rfc6455#section-4.2)