###### [websocket::stream::binary (1 of 2 overloads)](overload1.html "websocket::stream::binary (1 of 2 overloads)")

Set the binary message write option.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.binary.overload1.synopsis)

```programlisting
void
binary(
    bool value);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.binary.overload1.description)

This controls whether or not outgoing message opcodes are set to binary
or text. The setting is only applied at the start when a caller begins
a new message. Changing the opcode after a message is started will only
take effect after the current message being sent is complete.

The default setting is to send text messages.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.binary.overload1.parameters)

| Name | Description |
| --- | --- |
| `value` | `true` if outgoing messages should indicate binary, or `false` if they should indicate text. |

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.binary.overload1.example)

Setting the message type to binary.

```programlisting
ws.binary( true );
```