###### [websocket::stream::ping (2 of 2 overloads)](overload2.html "websocket::stream::ping (2 of 2 overloads)")

Send a websocket ping control frame.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.ping.overload2.synopsis)

```programlisting
void
ping(
    ping_data const& payload,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.ping.overload2.description)

This function is used to send a [ping
frame](https://tools.ietf.org/html/rfc6455#section-5.5.2), which usually elicits an automatic pong control frame
response from the peer.

The call blocks until one of the following conditions is true:

* The ping frame is written.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.ping.overload2.parameters)

| Name | Description |
| --- | --- |
| `payload` | The payload of the ping message, which may be empty. |
| `ec` | Set to indicate what error occurred, if any. |