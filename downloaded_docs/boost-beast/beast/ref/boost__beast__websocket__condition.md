#### [websocket::condition](boost__beast__websocket__condition.html "websocket::condition")

Error conditions corresponding to sets of error codes.

##### [Synopsis](boost__beast__websocket__condition.html#beast.ref.boost__beast__websocket__condition.synopsis)

Defined in header `<boost/beast/websocket/error.hpp>`

```programlisting
enum condition
```

##### [Values](boost__beast__websocket__condition.html#beast.ref.boost__beast__websocket__condition.values)

| Name | Description |
| --- | --- |
| `handshake_failed` | The WebSocket handshake failed.  This condition indicates that the WebSocket handshake failed. If the corresponding HTTP response indicates the keep-alive behavior, then the handshake may be reattempted. |
| `protocol_violation` | A WebSocket protocol violation occurred.  This condition indicates that the remote peer on the WebSocket connection sent data which violated the protocol. |