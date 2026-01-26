#### [websocket::permessage\_deflate\_status](boost__beast__websocket__permessage_deflate_status.html "websocket::permessage_deflate_status")

permessage-deflate extension status.

##### [Synopsis](boost__beast__websocket__permessage_deflate_status.html#beast.ref.boost__beast__websocket__permessage_deflate_status.synopsis)

Defined in header `<boost/beast/websocket/stream.hpp>`

```programlisting
struct permessage_deflate_status
```

##### [Data Members](boost__beast__websocket__permessage_deflate_status.html#beast.ref.boost__beast__websocket__permessage_deflate_status.data_members)

| Name | Description |
| --- | --- |
| **[active](boost__beast__websocket__permessage_deflate_status/active.html "websocket::permessage_deflate_status::active")** | `true` if the permessage-deflate extension is active |
| **[client\_window\_bits](boost__beast__websocket__permessage_deflate_status/client_window_bits.html "websocket::permessage_deflate_status::client_window_bits")** | The number of window bits used by the client. |
| **[server\_window\_bits](boost__beast__websocket__permessage_deflate_status/server_window_bits.html "websocket::permessage_deflate_status::server_window_bits")** | The number of window bits used by the server. |

##### [Description](boost__beast__websocket__permessage_deflate_status.html#beast.ref.boost__beast__websocket__permessage_deflate_status.description)

These settings indicate the status of the permessage-deflate extension, showing
if it is active and the window bits in use.

Objects of this type are used with [`beast::websocket::stream::get_status`](boost__beast__websocket__stream/get_status.html "websocket::stream::get_status").