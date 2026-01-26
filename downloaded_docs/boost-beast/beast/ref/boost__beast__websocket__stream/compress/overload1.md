###### [websocket::stream::compress (1 of 2 overloads)](overload1.html "websocket::stream::compress (1 of 2 overloads)")

Set the compress message write option.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.compress.overload1.synopsis)

```programlisting
void
compress(
    bool value);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.compress.overload1.description)

This controls whether or not outgoing messages should be compressed.
The setting is only applied when

* The template parameter `deflateSupported`
  is true
* Compression is enable. This is controlled with [`stream::set_option`](../set_option.html "websocket::stream::set_option")
* Client and server have negotiated permessage-deflate settings
* The message is larger than [`permessage_deflate::msg_size_threshold`](../../boost__beast__websocket__permessage_deflate/msg_size_threshold.html "websocket::permessage_deflate::msg_size_threshold")

This function permits adjusting per-message compression. Changing the
opcode after a message is started will only take effect after the current
message being sent is complete.

The default setting is to compress messages whenever the conditions above
are true.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.compress.overload1.parameters)

| Name | Description |
| --- | --- |
| `value` | `true` if outgoing messages should be compressed |

###### [Example](overload1.html#beast.ref.boost__beast__websocket__stream.compress.overload1.example)

Disabling compression for a single message.

```programlisting
ws.compress( false );
ws.write(net::buffer(s), ec);
ws.compress( true );
```