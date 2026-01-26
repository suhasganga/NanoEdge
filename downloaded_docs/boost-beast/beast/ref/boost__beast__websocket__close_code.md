#### [websocket::close\_code](boost__beast__websocket__close_code.html "websocket::close_code")

Close status codes.

##### [Synopsis](boost__beast__websocket__close_code.html#beast.ref.boost__beast__websocket__close_code.synopsis)

Defined in header `<boost/beast/websocket/rfc6455.hpp>`

```programlisting
enum close_code
```

##### [Values](boost__beast__websocket__close_code.html#beast.ref.boost__beast__websocket__close_code.values)

| Name | Description |
| --- | --- |
| `normal` | Normal closure; the connection successfully completed whatever purpose for which it was created. |
| `going_away` | The endpoint is going away, either because of a server failure or because the browser is navigating away from the page that opened the connection. |
| `protocol_error` | The endpoint is terminating the connection due to a protocol error. |
| `unknown_data` | The connection is being terminated because the endpoint received data of a type it cannot accept (for example, a text-only endpoint received binary data). |
| `bad_payload` | The endpoint is terminating the connection because a message was received that contained inconsistent data (e.g., non-UTF-8 data within a text message). |
| `policy_error` | The endpoint is terminating the connection because it received a message that violates its policy. This is a generic status code, used when codes 1003 and 1009 are not suitable. |
| `too_big` | The endpoint is terminating the connection because a data frame was received that is too large. |
| `needs_extension` | The client is terminating the connection because it expected the server to negotiate one or more extension, but the server didn't. |
| `internal_error` | The server is terminating the connection because it encountered an unexpected condition that prevented it from fulfilling the request. |
| `service_restart` | The server is terminating the connection because it is restarting. |
| `try_again_later` | The server is terminating the connection due to a temporary condition, e.g. it is overloaded and is casting off some of its clients. |
| `none` | Used internally to mean "no error".  This code is reserved and may not be sent. |
| `reserved1` | Reserved for future use by the WebSocket standard.  This code is reserved and may not be sent. |
| `no_status` | No status code was provided even though one was expected.  This code is reserved and may not be sent. |
| `abnormal` | Connection was closed without receiving a close frame.  This code is reserved and may not be sent. |
| `reserved2` | Reserved for future use by the WebSocket standard.  This code is reserved and may not be sent. |
| `reserved3` | Reserved for future use by the WebSocket standard.  This code is reserved and may not be sent. |

##### [Description](boost__beast__websocket__close_code.html#beast.ref.boost__beast__websocket__close_code.description)

These codes accompany close frames.

##### [See Also](boost__beast__websocket__close_code.html#beast.ref.boost__beast__websocket__close_code.see_also)

[RFC 6455 7.4.1
Defined Status Codes](https://tools.ietf.org/html/rfc6455#section-7.4.1)