###### [websocket::stream::async\_read\_some (1 of 2 overloads)](overload1.html "websocket::stream::async_read_some (1 of 2 overloads)")

Read some message data asynchronously.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.async_read_some.overload1.synopsis)

```programlisting
template<
    class DynamicBuffer,
    class ReadHandler = net::default_completion_token_t<                executor_type>>
DEDUCED
async_read_some(
    DynamicBuffer& buffer,
    std::size_t limit,
    ReadHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.async_read_some.overload1.description)

This function is used to asynchronously read some message data.

This call always returns immediately. The asynchronous operation will
continue until one of the following conditions is true:

* Some message data is received.
* A close frame is received. In this case the error indicated by the
  function will be [`error::closed`](../../boost__beast__websocket__error.html "websocket::error").
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_read_some`
and `async_write_some`
functions. The program must ensure that no other calls to [`read`](../read.html "websocket::stream::read"), [`read_some`](../read_some.html "websocket::stream::read_some"), [`async_read`](../async_read.html "websocket::stream::async_read"), or [`async_read_some`](../async_read_some.html "websocket::stream::async_read_some") are performed
until this operation completes.

Received message data is appended to the buffer. The functions [`got_binary`](../got_binary.html "websocket::stream::got_binary") and [`got_text`](../got_text.html "websocket::stream::got_text") may be used to query
the stream and determine the type of the last received message. The function
[`is_message_done`](../is_message_done.html "websocket::stream::is_message_done") may be called
to determine if the message received by the last read operation is complete.

Until the operation completes, the implementation will read incoming
control frames and handle them automatically as follows:

* The [`control_callback`](../control_callback.html "websocket::stream::control_callback") will be
  invoked for each control frame.
* For each received ping frame, a pong frame will be automatically
  sent.
* If a close frame is received, the WebSocket close procedure is performed.
  In this case, when the function returns, the error [`error::closed`](../../boost__beast__websocket__error.html "websocket::error") will be indicated.

Pong frames and close frames sent by the implementation while the read
operation is outstanding do not prevent the application from also writing
message data, sending pings, sending pongs, or sending close frames.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.async_read_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffer` | A dynamic buffer to append message data to. |
| `limit` | An upper limit on the number of bytes this function will append into the buffer. If this value is zero, then a reasonable size will be chosen automatically. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & ec,       // Result of operation     std::size_t bytes_written   // Number of bytes appended to buffer ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Per-Operation Cancellation](overload1.html#beast.ref.boost__beast__websocket__stream.async_read_some.overload1.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::total`

`total`cancellation succeeds
if the operation is suspended due to ongoing control operations such
as a ping/pong.

`terminal` cancellation
succeeds when supported by the underlying stream.

`terminal` cancellation
leaves the stream in an undefined state, so that only closing it is guaranteed
to succeed.