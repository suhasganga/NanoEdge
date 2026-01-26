#### [websocket::frame\_type](boost__beast__websocket__frame_type.html "websocket::frame_type")

The type of received control frame.

##### [Synopsis](boost__beast__websocket__frame_type.html#beast.ref.boost__beast__websocket__frame_type.synopsis)

Defined in header `<boost/beast/websocket/stream.hpp>`

```programlisting
enum frame_type
```

##### [Values](boost__beast__websocket__frame_type.html#beast.ref.boost__beast__websocket__frame_type.values)

| Name | Description |
| --- | --- |
| `close` | A close frame was received. |
| `ping` | A ping frame was received. |
| `pong` | A pong frame was received. |

##### [Description](boost__beast__websocket__frame_type.html#beast.ref.boost__beast__websocket__frame_type.description)

Values of this type are passed to the control frame callback set using [`stream::control_callback`](boost__beast__websocket__stream/control_callback.html "websocket::stream::control_callback").