###### [websocket::stream::text (1 of 2 overloads)](overload1.html "websocket::stream::text (1 of 2 overloads)")

Set the text message write option.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.text.overload1.synopsis)

```programlisting
void
text(
    bool value);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.text.overload1.description)

This controls whether or not outgoing message opcodes are set to binary
or text. The setting is only applied at the start when a caller begins
a new message. Changing the opcode after a message is started will only
take effect after the current message being sent is complete.

The default setting is to send text messages.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.text.overload1.parameters)

| Name | Description |
| --- | --- |
| `value` | `true` if outgoing messages should indicate text, or `false` if they should indicate binary. |

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.text.overload1.example)

Setting the message type to text.

```programlisting
ws.text( true );
```