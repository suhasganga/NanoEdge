###### [websocket::stream::write\_some (2 of 2 overloads)](overload2.html "websocket::stream::write_some (2 of 2 overloads)")

Write some message data.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.write_some.overload2.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    bool fin,
    ConstBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.write_some.overload2.description)

This function is used to send part of a message.

The call blocks until one of the following is true:

* The message data is written.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

If this is the beginning of a new message, the message opcode will be
set to text or binary based on the current setting of the [`binary`](../binary.html "websocket::stream::binary") (or [`text`](../text.html "websocket::stream::text")) option. The actual payload
sent may be transformed as per the WebSocket protocol settings.

This function always writes a complete WebSocket frame (not WebSocket
message) upon successful completion, so it is well defined to perform
ping, pong, and close operations after this operation completes.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.write_some.overload2.parameters)

| Name | Description |
| --- | --- |
| `fin` | `true` if this is the last part of the message. |
| `buffers` | The buffers containing the message part to send. |
| `ec` | Set to indicate what error occurred, if any. |

###### [Return Value](overload2.html#beast.ref.boost__beast__websocket__stream.write_some.overload2.return_value)

The number of bytes sent from the buffers.

###### [Return Value](overload2.html#beast.ref.boost__beast__websocket__stream.write_some.overload2.return_value0)

The number of bytes consumed in the input buffers.