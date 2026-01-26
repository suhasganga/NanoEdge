###### [websocket::stream::write (2 of 2 overloads)](overload2.html "websocket::stream::write (2 of 2 overloads)")

Write a complete message.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.write.overload2.synopsis)

```programlisting
template<
    class ConstBufferSequence>
std::size_t
write(
    ConstBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.write.overload2.description)

This function is used to write a complete message.

The call blocks until one of the following is true:

* The complete message is written.
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `write_some`
function.

The current setting of the [`binary`](../binary.html "websocket::stream::binary") option controls whether
the message opcode is set to text or binary. If the [`auto_fragment`](../auto_fragment.html "websocket::stream::auto_fragment") option is set,
the message will be split into one or more frames as necessary. The actual
payload contents sent may be transformed as per the WebSocket protocol
settings.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.write.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers containing the message to send. |
| `ec` | Set to indicate what error occurred, if any. |

###### [Return Value](overload2.html#beast.ref.boost__beast__websocket__stream.write.overload2.return_value)

The number of bytes sent from the buffers.