###### [websocket::stream::read\_some (1 of 4 overloads)](overload1.html "websocket::stream::read_some (1 of 4 overloads)")

Read some message data.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__stream.read_some.overload1.synopsis)

```programlisting
template<
    class DynamicBuffer>
std::size_t
read_some(
    DynamicBuffer& buffer,
    std::size_t limit);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__stream.read_some.overload1.description)

This function is used to read some message data.

The call blocks until one of the following is true:

* Some message data is received.
* A close frame is received. In this case the error indicated by the
  function will be [`error::closed`](../../boost__beast__websocket__error.html "websocket::error").
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `read_some`
and `write_some` functions.

Received message data is appended to the buffer. The functions [`got_binary`](../got_binary.html "websocket::stream::got_binary") and [`got_text`](../got_text.html "websocket::stream::got_text") may be used to query
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

###### [Return Value](overload1.html#beast.ref.boost__beast__websocket__stream.read_some.overload1.return_value)

The number of message payload bytes appended to the buffer.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__stream.read_some.overload1.parameters)

| Name | Description |
| --- | --- |
| `buffer` | A dynamic buffer to append message data to. |
| `limit` | An upper limit on the number of bytes this function will append into the buffer. If this value is zero, then a reasonable size will be chosen automatically. |

###### [Exceptions](overload1.html#beast.ref.boost__beast__websocket__stream.read_some.overload1.exceptions)

| Type | Thrown On |
| --- | --- |
| `[link beast.ref.boost__beast__system_error system_error]` | Thrown on failure. |