###### [websocket::stream::read (2 of 2 overloads)](overload2.html "websocket::stream::read (2 of 2 overloads)")

Read a complete message.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__stream.read.overload2.synopsis)

```programlisting
template<
    class DynamicBuffer>
std::size_t
read(
    DynamicBuffer& buffer,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__stream.read.overload2.description)

This function is used to read a complete message.

The call blocks until one of the following is true:

* A complete message is received.
* A close frame is received. In this case the error indicated by the
  function will be [`error::closed`](../../boost__beast__websocket__error.html "websocket::error").
* An error occurs.

The algorithm, known as a *composed operation*, is
implemented in terms of calls to the next layer's `read_some`
and `write_some` functions.

Received message data is appended to the buffer. The functions [`got_binary`](../got_binary.html "websocket::stream::got_binary") and [`got_text`](../got_text.html "websocket::stream::got_text") may be used to query
the stream and determine the type of the last received message.

Until the call returns, the implementation will read incoming control
frames and handle them automatically as follows:

* The [`control_callback`](../control_callback.html "websocket::stream::control_callback") will be
  invoked for each control frame.
* For each received ping frame, a pong frame will be automatically
  sent.
* If a close frame is received, the WebSocket closing handshake is
  performed. In this case, when the function returns, the error [`error::closed`](../../boost__beast__websocket__error.html "websocket::error") will be indicated.

###### [Return Value](overload2.html#beast.ref.boost__beast__websocket__stream.read.overload2.return_value)

The number of message payload bytes appended to the buffer.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__stream.read.overload2.parameters)

| Name | Description |
| --- | --- |
| `buffer` | A dynamic buffer to append message data to. |
| `ec` | Set to indicate what error occurred, if any. |