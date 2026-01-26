###### [websocket::stream::write (1 of 2 overloads)](overload1.html "websocket::stream::write (1 of 2 overloads)")

Write a complete message.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.write.overload1.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write(
    ConstBufferSequence const& buffers);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.write.overload1.description)

This function is used to write a complete message.

The call blocks until one of the following is true:

* The message is written.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

The current setting of the [`binary`](../binary.html "websocket::stream::binary") option controls whether
the message opcode is set to text or binary. If the [`auto_fragment`](../auto_fragment.html "websocket::stream::auto_fragment") option is set,
the message will be split into one or more frames as necessary. The actual
payload contents sent may be transformed as per the WebSocket protocol
settings.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.write.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers containing the message to send. |

###### [Return Value](overload1.html#beast.ref.boost__beast__websocket__stream.write.overload1.return_value)

The number of bytes sent from the buffers.

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.write.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |