#### [websocket::stream\_base::timeout](boost__beast__websocket__stream_base__timeout.html "websocket::stream_base::timeout")

Stream option to control the behavior of websocket timeouts.

##### [Synopsis](boost__beast__websocket__stream_base__timeout.html#beast.ref.boost__beast__websocket__stream_base__timeout.synopsis)

Defined in header `<boost/beast/websocket/stream_base.hpp>`

```programlisting
struct timeout
```

##### [Static Member Functions](boost__beast__websocket__stream_base__timeout.html#beast.ref.boost__beast__websocket__stream_base__timeout.static_member_functions)

| Name | Description |
| --- | --- |
| **[suggested](boost__beast__websocket__stream_base__timeout/suggested.html "websocket::stream_base::timeout::suggested")** | Construct timeout settings with suggested values for a role. |

##### [Data Members](boost__beast__websocket__stream_base__timeout.html#beast.ref.boost__beast__websocket__stream_base__timeout.data_members)

| Name | Description |
| --- | --- |
| **[handshake\_timeout](boost__beast__websocket__stream_base__timeout/handshake_timeout.html "websocket::stream_base::timeout::handshake_timeout")** | Time limit on handshake, accept, and close operations: |
| **[idle\_timeout](boost__beast__websocket__stream_base__timeout/idle_timeout.html "websocket::stream_base::timeout::idle_timeout")** | The time limit after which a connection is considered idle. |
| **[keep\_alive\_pings](boost__beast__websocket__stream_base__timeout/keep_alive_pings.html "websocket::stream_base::timeout::keep_alive_pings")** | Automatic ping setting. |

##### [Description](boost__beast__websocket__stream_base__timeout.html#beast.ref.boost__beast__websocket__stream_base__timeout.description)

Timeout features are available for asynchronous operations only.