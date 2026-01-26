###### [websocket::stream::write\_some (1 of 2 overloads)](overload1.html "websocket::stream::write_some (1 of 2 overloads)")

Write some message data.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.write_some.overload1.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write_some(
    bool fin,
    ConstBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.write_some.overload1.description)

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

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.write_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `fin` | `true` if this is the last part of the message. |
| `buffers` | The buffers containing the message part to send. |

###### [Return Value](overload1.html#beast.ref.boost__beast__websocket__stream.write_some.overload1.return_value)

The number of bytes sent from the buffers.

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.write_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |