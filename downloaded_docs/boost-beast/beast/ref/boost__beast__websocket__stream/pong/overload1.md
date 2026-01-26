###### [websocket::stream::pong (1 of 2 overloads)](overload1.html "websocket::stream::pong (1 of 2 overloads)")

Send a websocket pong control frame.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.pong.overload1.synopsis)

```programlisting
void
pong(
    ping_data const& payload);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.pong.overload1.description)

This function is used to send a [pong
frame](https://tools.ietf.org/html/rfc6455#section-5.5.3), which is usually sent automatically in response to a ping
frame from the remote peer.

The call blocks until one of the following conditions is true:

* The pong frame is written.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

WebSocket allows pong frames to be sent at any time, without first receiving
a ping. An unsolicited pong sent in this fashion may indicate to the
remote peer that the connection is still active.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.pong.overload1.parameters)

| Name | Description |
| --- | --- |
| `payload` | The payload of the pong message, which may be empty. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.pong.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |