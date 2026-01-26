#### [websocket::stream\_base](boost__beast__websocket__stream_base.html "websocket::stream_base")

This class is used as a base for the [`websocket::stream`](boost__beast__websocket__stream.html "websocket::stream") class template to group common
types and constants.

##### [Synopsis](boost__beast__websocket__stream_base.html#beast.ref.boost__beast__websocket__stream_base.synopsis)

Defined in header `<boost/beast/websocket/stream_base.hpp>`

```programlisting
struct stream_base
```

##### [Types](boost__beast__websocket__stream_base.html#beast.ref.boost__beast__websocket__stream_base.types)

| Name | Description |
| --- | --- |
| **[decorator](boost__beast__websocket__stream_base__decorator.html "websocket::stream_base::decorator")** | Stream option used to adjust HTTP fields of WebSocket upgrade request and responses. |
| **[duration](boost__beast__websocket__stream_base/duration.html "websocket::stream_base::duration")** | The type used to represent durations. |
| **[time\_point](boost__beast__websocket__stream_base/time_point.html "websocket::stream_base::time_point")** | The type used to represent time points. |
| **[timeout](boost__beast__websocket__stream_base__timeout.html "websocket::stream_base::timeout")** | Stream option to control the behavior of websocket timeouts. |

##### [Static Member Functions](boost__beast__websocket__stream_base.html#beast.ref.boost__beast__websocket__stream_base.static_member_functions)

| Name | Description |
| --- | --- |
| **[never](boost__beast__websocket__stream_base/never.html "websocket::stream_base::never")** | Returns the special [`time_point`](boost__beast__websocket__stream_base/time_point.html "websocket::stream_base::time_point") value meaning "never". |
| **[none](boost__beast__websocket__stream_base/none.html "websocket::stream_base::none")** | Returns the special duration value meaning "none". |