###### [websocket::stream::ping (1 of 2 overloads)](overload1.html "websocket::stream::ping (1 of 2 overloads)")

Send a websocket ping control frame.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.ping.overload1.synopsis)

```programlisting
void
ping(
    ping_data const& payload);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.ping.overload1.description)

This function is used to send a [ping
frame](https://tools.ietf.org/html/rfc6455#section-5.5.2), which usually elicits an automatic pong control frame
response from the peer.

The call blocks until one of the following conditions is true:

* The ping frame is written.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.ping.overload1.parameters)

| Name | Description |
| --- | --- |
| `payload` | The payload of the ping message, which may be empty. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.ping.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |