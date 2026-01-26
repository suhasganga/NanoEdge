##### [websocket::stream::got\_text](got_text.html "websocket::stream::got_text")

Returns `true` if the latest
message data indicates text.

###### [Synopsis](got_text.html#beast.ref.boost__beast__websocket__stream.got_text.synopsis)

```programlisting
bool
got_text() const;
```

###### [Description](got_text.html#beast.ref.boost__beast__websocket__stream.got_text.description)

This function informs the caller of whether the last received message frame
represents a message with the text opcode.

If there is no last message frame, the return value is undefined.