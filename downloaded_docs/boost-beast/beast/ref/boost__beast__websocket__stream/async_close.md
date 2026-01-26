##### [websocket::stream::async\_close](async_close.html "websocket::stream::async_close")

Perform the WebSocket closing handshake asynchronously and close the underlying
stream.

###### [Synopsis](async_close.html#beast.ref.boost__beast__websocket__stream.async_close.synopsis)

```programlisting
template<
    class CloseHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_close(
    close_reason const& cr,
    CloseHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](async_close.html#beast.ref.boost__beast__websocket__stream.async_close.description)

This function sends a [close
frame](https://tools.ietf.org/html/rfc6455#section-5.5.1) to begin the WebSocket closing handshake and waits for a
corresponding close frame in response. Once received, it calls [`async_teardown`](../boost__beast__websocket__async_teardown.html "websocket::async_teardown") to gracefully shut
down the underlying stream asynchronously.

After beginning the closing handshake, the program should not write further
message data, pings, or pongs. However, it can still read incoming message
data. A read returning [`error::closed`](../boost__beast__websocket__error.html "websocket::error") indicates a successful
connection closure.

This call always returns immediately. The asynchronous operation will continue
until one of the following conditions is true:

* The closing handshake completes, and [`async_teardown`](../boost__beast__websocket__async_teardown.html "websocket::async_teardown") finishes.
* An error occurs.

If a timeout occurs, [`close_socket`](../boost__beast__close_socket.html "close_socket") will be called to
close the underlying stream.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_write_some`
function. No other operations except for message reading operations should
be initiated on the stream after a close operation is started.

###### [Parameters](async_close.html#beast.ref.boost__beast__websocket__stream.async_close.parameters)

| Name | Description |
| --- | --- |
| `cr` | The reason for the close. If the close reason specifies a close code other than [`beast::websocket::close_code::none`](../boost__beast__websocket__close_code.html "websocket::close_code"), the close frame is sent with the close code and optional reason string. Otherwise, the close frame is sent with no payload. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & ec     // Result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Per-Operation Cancellation](async_close.html#beast.ref.boost__beast__websocket__stream.async_close.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::total`

`total`cancellation succeeds
if the operation is suspended due to ongoing control operations such as
a ping/pong.

`terminal` cancellation succeeds
when supported by the underlying stream.

###### [Remarks](async_close.html#beast.ref.boost__beast__websocket__stream.async_close.remarks)

`terminal` cancellation may
close the underlying socket.

###### [See Also](async_close.html#beast.ref.boost__beast__websocket__stream.async_close.see_also)

* [Websocket
  Closing Handshake (RFC6455)](https://tools.ietf.org/html/rfc6455#section-7.1.2)