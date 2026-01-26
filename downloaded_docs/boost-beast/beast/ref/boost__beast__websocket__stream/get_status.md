##### [websocket::stream::get\_status](get_status.html "websocket::stream::get_status")

Get the status of the permessage-deflate extension.

###### [Synopsis](get_status.html#beast.ref.boost__beast__websocket__stream.get_status.synopsis)

```programlisting
void
get_status(
    permessage_deflate_status& status) const;
```

###### [Description](get_status.html#beast.ref.boost__beast__websocket__stream.get_status.description)

Used to check the status of the permessage-deflate extension after the
WebSocket handshake.

###### [Parameters](get_status.html#beast.ref.boost__beast__websocket__stream.get_status.parameters)

| Name | Description |
| --- | --- |
| `status` | A reference to a [`permessage_deflate_status`](../boost__beast__websocket__permessage_deflate_status.html "websocket::permessage_deflate_status") object where the status will be stored. |

###### [Example](get_status.html#beast.ref.boost__beast__websocket__stream.get_status.example)

Checking the status of the permessage-deflate extension:

```programlisting
permessage_deflate_status status;
ws.get_status(status);
```