##### [websocket::stream::reason](reason.html "websocket::stream::reason")

Returns the close reason received from the remote peer.

###### [Synopsis](reason.html#beast.ref.boost__beast__websocket__stream.reason.synopsis)

```programlisting
close_reason const&
reason() const;
```

###### [Description](reason.html#beast.ref.boost__beast__websocket__stream.reason.description)

This is only valid after a read completes with [`error::closed`](../boost__beast__websocket__error.html "websocket::error").