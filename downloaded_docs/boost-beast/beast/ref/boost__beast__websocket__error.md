#### [websocket::error](boost__beast__websocket__error.html "websocket::error")

Error codes returned from [`boost::beast::websocket::stream`](boost__beast__websocket__stream.html "websocket::stream") operations.

##### [Synopsis](boost__beast__websocket__error.html#beast.ref.boost__beast__websocket__error.synopsis)

Defined in header `<boost/beast/websocket/error.hpp>`

```programlisting
enum error
```

##### [Values](boost__beast__websocket__error.html#beast.ref.boost__beast__websocket__error.values)

| Name | Description |
| --- | --- |
| `closed` | The WebSocket stream was gracefully closed at both endpoints. |
| `buffer_overflow` | The WebSocket operation caused a dynamic buffer overflow. |
| `partial_deflate_block` | The WebSocket stream produced an incomplete deflate block. |
| `message_too_big` | The WebSocket message exceeded the locally configured limit. |
| `bad_http_version` | The WebSocket handshake was not HTTP/1.1.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_method` | The WebSocket handshake method was not GET.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_host` | The WebSocket handshake Host field is missing.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_connection` | The WebSocket handshake Connection field is missing.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_connection_upgrade` | The WebSocket handshake Connection field is missing the upgrade token.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_upgrade` | The WebSocket handshake Upgrade field is missing.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_upgrade_websocket` | The WebSocket handshake Upgrade field is missing the websocket token.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_sec_key` | The WebSocket handshake Sec-WebSocket-Key field is missing.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_sec_key` | The WebSocket handshake Sec-WebSocket-Key field is invalid.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_sec_version` | The WebSocket handshake Sec-WebSocket-Version field is missing.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_sec_version` | The WebSocket handshake Sec-WebSocket-Version field is invalid.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `no_sec_accept` | The WebSocket handshake Sec-WebSocket-Accept field is missing.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_sec_accept` | The WebSocket handshake Sec-WebSocket-Accept field is invalid.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `upgrade_declined` | The WebSocket handshake was declined by the remote peer.  Error codes with this value will compare equal to [`condition::handshake_failed`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_opcode` | The WebSocket frame contained an illegal opcode.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_data_frame` | The WebSocket data frame was unexpected.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_continuation` | The WebSocket continuation frame was unexpected.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_reserved_bits` | The WebSocket frame contained illegal reserved bits.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_control_fragment` | The WebSocket control frame was fragmented.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_control_size` | The WebSocket control frame size was invalid.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_unmasked_frame` | The WebSocket frame was unmasked.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_masked_frame` | The WebSocket frame was masked.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_size` | The WebSocket frame size was not canonical.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_frame_payload` | The WebSocket frame payload was not valid utf8.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_close_code` | The WebSocket close frame reason code was invalid.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_close_size` | The WebSocket close frame payload size was invalid.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |
| `bad_close_payload` | The WebSocket close frame payload was not valid utf8.  Error codes with this value will compare equal to [`condition::protocol_violation`](boost__beast__websocket__condition.html "websocket::condition") |