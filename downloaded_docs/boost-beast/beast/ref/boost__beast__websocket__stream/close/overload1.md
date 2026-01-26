###### [websocket::stream::close (1 of 2 overloads)](overload1.html "websocket::stream::close (1 of 2 overloads)")

Perform the WebSocket closing handshake and close the underlying stream.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.close.overload1.synopsis)

```programlisting
void
close(
    close_reason const& cr);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.close.overload1.description)

This function sends a [close
frame](https://tools.ietf.org/html/rfc6455#section-5.5.1) to begin the WebSocket closing handshake and waits for
a corresponding close frame in response. Once received, it calls [`teardown`](../../boost__beast__websocket__teardown.html "websocket::teardown")
to gracefully shut down the underlying stream.

After beginning the closing handshake, the program should not write further
message data, pings, or pongs. However, it can still read incoming message
data. A read returning [`error::closed`](../../boost__beast__websocket__error.html "websocket::error") indicates a successful
connection closure.

The call blocks until one of the following conditions is true:

* The closing handshake completes, and [`teardown`](../../boost__beast__websocket__teardown.html "websocket::teardown") finishes.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.close.overload1.parameters)

| Name | Description |
| --- | --- |
| `cr` | The reason for the close. If the close reason specifies a close code other than [`beast::websocket::close_code::none`](../../boost__beast__websocket__close_code.html "websocket::close_code"), the close frame is sent with the close code and optional reason string. Otherwise, the close frame is sent with no payload. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.close.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |

###### [See Also](overload1.html#beast.ref.boost__beast__websocket__stream.close.overload1.see_also)

* [Websocket
  Closing Handshake (RFC6455)](https://tools.ietf.org/html/rfc6455#section-7.1.2)