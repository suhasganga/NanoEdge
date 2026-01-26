##### [websocket::stream::async\_pong](async_pong.html "websocket::stream::async_pong")

Send a websocket pong control frame asynchronously.

###### [Synopsis](async_pong.html#beast.ref.boost__beast__websocket__stream.async_pong.synopsis)

```programlisting
template<
    class PongHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_pong(
    ping_data const& payload,
    PongHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](async_pong.html#beast.ref.boost__beast__websocket__stream.async_pong.description)

This function is used to asynchronously send a [pong
frame](https://tools.ietf.org/html/rfc6455#section-5.5.3), which is usually sent automatically in response to a ping
frame from the remote peer.

* The pong frame is written.
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_write_some`
function. The program must ensure that no other calls to [`ping`](ping.html "websocket::stream::ping"), [`pong`](pong.html "websocket::stream::pong"), [`async_ping`](async_ping.html "websocket::stream::async_ping"), or [`async_pong`](async_pong.html "websocket::stream::async_pong") are performed until
this operation completes.

If a close frame is sent or received before the pong frame is sent, the
error received by this completion handler will be `net::error::operation_aborted`.

WebSocket allows pong frames to be sent at any time, without first receiving
a ping. An unsolicited pong sent in this fashion may indicate to the remote
peer that the connection is still active.

###### [Parameters](async_pong.html#beast.ref.boost__beast__websocket__stream.async_pong.parameters)

| Name | Description |
| --- | --- |
| `payload` | The payload of the pong message, which may be empty. The implementation will not access the contents of this object after the initiating function returns. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & ec     // Result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Per-Operation Cancellation](async_pong.html#beast.ref.boost__beast__websocket__stream.async_pong.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::total`

`total`cancellation succeeds
if the operation is suspended due to ongoing control operations such as
a ping/pong.

`terminal` cancellation succeeds
when supported by the underlying stream.

`terminal` cancellation leaves
the stream in an undefined state, so that only closing it is guaranteed
to succeed.