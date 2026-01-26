###### [websocket::stream::read\_some (4 of 4 overloads)](overload4.html "websocket::stream::read_some (4 of 4 overloads)")

Read some message data.

###### [Synopsis](overload4.html#beast.ref.boost__beast__websocket__stream.read_some.overload4.synopsis)

```programlisting
template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers,
    error_code& ec);
```

###### [Description](overload4.html#beast.ref.boost__beast__websocket__stream.read_some.overload4.description)

This function is used to read some message data.

The call blocks until one of the following is true:

* Some message data is received.
* A close frame is received. In this case the error indicated by the
  function will be [`error::closed`](../../boost__beast__websocket__error.html "websocket::error").
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `read_some`
and `write_some` functions.

The functions [`got_binary`](../got_binary.html "websocket::stream::got_binary") and [`got_text`](../got_text.html "websocket::stream::got_text") may be used to query
the stream and determine the type of the last received message. The function
[`is_message_done`](../is_message_done.html "websocket::stream::is_message_done") may be called
to determine if the message received by the last read operation is complete.

Until the call returns, the implementation will read incoming control
frames and handle them automatically as follows:

* The [`control_callback`](../control_callback.html "websocket::stream::control_callback") will be
  invoked for each control frame.
* For each received ping frame, a pong frame will be automatically
  sent.
* If a close frame is received, the WebSocket closing handshake is
  performed. In this case, when the function returns, the error [`error::closed`](../../boost__beast__websocket__error.html "websocket::error") will be indicated.

###### [Return Value](overload4.html#beast.ref.boost__beast__websocket__stream.read_some.overload4.return_value)

The number of message payload bytes appended to the buffer.

###### [Parameters](overload4.html#beast.ref.boost__beast__websocket__stream.read_some.overload4.parameters)

| Name | Description |
| --- | --- |
| `buffers` | A buffer sequence to write message data into. The previous contents of the buffers will be overwritten, starting from the beginning. |
| `ec` | Set to indicate what error occurred, if any. |

###### [Per-Operation Cancellation](overload4.html#beast.ref.boost__beast__websocket__stream.read_some.overload4.per_operation_cancellation)

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