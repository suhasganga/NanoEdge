###### [websocket::stream::read\_some (3 of 4 overloads)](overload3.html "websocket::stream::read_some (3 of 4 overloads)")

Read some message data.

###### [Synopsis](overload3.html#beast.ref.boost__beast__websocket__stream.read_some.overload3.synopsis)

```programlisting
template<
    class MutableBufferSequence>
std::size_t
read_some(
    MutableBufferSequence const& buffers);
```

###### [Description](overload3.html#beast.ref.boost__beast__websocket__stream.read_some.overload3.description)

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

###### [Return Value](overload3.html#beast.ref.boost__beast__websocket__stream.read_some.overload3.return_value)

The number of message payload bytes appended to the buffer.

###### [Parameters](overload3.html#beast.ref.boost__beast__websocket__stream.read_some.overload3.parameters)

| Name | Description |
| --- | --- |
| `buffers` | A buffer sequence to write message data into. The previous contents of the buffers will be overwritten, starting from the beginning. |

###### [Exceptions](overload3.html#beast.ref.boost__beast__websocket__stream.read_some.overload3.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |