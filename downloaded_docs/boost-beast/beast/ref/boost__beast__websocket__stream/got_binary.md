##### [websocket::stream::got\_binary](got_binary.html "websocket::stream::got_binary")

Returns `true` if the latest
message data indicates binary.

###### [Synopsis](got_binary.html#beast.ref.boost__beast__websocket__stream.got_binary.synopsis)

```programlisting
bool
got_binary() const;
```

###### [Description](got_binary.html#beast.ref.boost__beast__websocket__stream.got_binary.description)

This function informs the caller of whether the last received message frame
represents a message with the binary opcode.

If there is no last message frame, the return value is undefined.