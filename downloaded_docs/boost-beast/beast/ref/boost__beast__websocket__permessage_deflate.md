#### [websocket::permessage\_deflate](boost__beast__websocket__permessage_deflate.html "websocket::permessage_deflate")

permessage-deflate extension options.

##### [Synopsis](boost__beast__websocket__permessage_deflate.html#beast.ref.boost__beast__websocket__permessage_deflate.synopsis)

Defined in header `<boost/beast/websocket/option.hpp>`

```programlisting
struct permessage_deflate
```

##### [Data Members](boost__beast__websocket__permessage_deflate.html#beast.ref.boost__beast__websocket__permessage_deflate.data_members)

| Name | Description |
| --- | --- |
| **[client\_enable](boost__beast__websocket__permessage_deflate/client_enable.html "websocket::permessage_deflate::client_enable")** | `true` to offer the extension in the client role |
| **[client\_max\_window\_bits](boost__beast__websocket__permessage_deflate/client_max_window_bits.html "websocket::permessage_deflate::client_max_window_bits")** | Maximum client window bits to offer. |
| **[client\_no\_context\_takeover](boost__beast__websocket__permessage_deflate/client_no_context_takeover.html "websocket::permessage_deflate::client_no_context_takeover")** | `true` if client\_no\_context\_takeover desired |
| **[compLevel](boost__beast__websocket__permessage_deflate/compLevel.html "websocket::permessage_deflate::compLevel")** | Deflate compression level 0..9. |
| **[memLevel](boost__beast__websocket__permessage_deflate/memLevel.html "websocket::permessage_deflate::memLevel")** | Deflate memory level, 1..9. |
| **[msg\_size\_threshold](boost__beast__websocket__permessage_deflate/msg_size_threshold.html "websocket::permessage_deflate::msg_size_threshold")** | The minimum size a message should have to be compressed. |
| **[server\_enable](boost__beast__websocket__permessage_deflate/server_enable.html "websocket::permessage_deflate::server_enable")** | `true` to offer the extension in the server role |
| **[server\_max\_window\_bits](boost__beast__websocket__permessage_deflate/server_max_window_bits.html "websocket::permessage_deflate::server_max_window_bits")** | Maximum server window bits to offer. |
| **[server\_no\_context\_takeover](boost__beast__websocket__permessage_deflate/server_no_context_takeover.html "websocket::permessage_deflate::server_no_context_takeover")** | `true` if server\_no\_context\_takeover desired |

##### [Description](boost__beast__websocket__permessage_deflate.html#beast.ref.boost__beast__websocket__permessage_deflate.description)

These settings control the permessage-deflate extension, which allows messages
to be compressed.

##### [Remarks](boost__beast__websocket__permessage_deflate.html#beast.ref.boost__beast__websocket__permessage_deflate.remarks)

These settings should be configured before performing the WebSocket handshake.

Objects of this type are used with [`beast::websocket::stream::set_option`](boost__beast__websocket__stream/set_option.html "websocket::stream::set_option").