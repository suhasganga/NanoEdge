###### [websocket::stream::set\_option (3 of 3 overloads)](overload3.html "websocket::stream::set_option (3 of 3 overloads)")

Set the permessage-deflate extension options.

###### [Synopsis](overload3.html#beast.ref.boost__beast__websocket__stream.set_option.overload3.synopsis)

```programlisting
void
set_option(
    permessage_deflate const& o);
```

###### [Description](overload3.html#beast.ref.boost__beast__websocket__stream.set_option.overload3.description)

###### [Exceptions](overload3.html#beast.ref.boost__beast__websocket__stream.set_option.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `invalid_argument` | if `deflateSupported == false`, and either `client_enable` or `server_enable` is `true`. |

###### [Remarks](overload3.html#beast.ref.boost__beast__websocket__stream.set_option.overload3.remarks)

These settings should be configured before performing the WebSocket handshake.