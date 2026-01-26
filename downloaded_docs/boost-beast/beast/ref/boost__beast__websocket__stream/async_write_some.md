##### [websocket::stream::async\_write\_some](async_write_some.html "websocket::stream::async_write_some")

Write some message data asynchronously.

###### [Synopsis](async_write_some.html#beast.ref.boost__beast__websocket__stream.async_write_some.synopsis)

```programlisting
template<
    class ConstBufferSequence,
    class WriteHandler = net::default_completion_token_t<                executor_type>>
DEDUCED
async_write_some(
    bool fin,
    ConstBufferSequence const& buffers,
    WriteHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](async_write_some.html#beast.ref.boost__beast__websocket__stream.async_write_some.description)

This function is used to asynchronously write part of a message.

This call always returns immediately. The asynchronous operation will continue
until one of the following conditions is true:

* The message data is written.
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_write_some`
function. The program must ensure that no other calls to [`write`](write.html "websocket::stream::write"), [`write_some`](write_some.html "websocket::stream::write_some"), [`async_write`](async_write.html "websocket::stream::async_write"), or [`async_write_some`](async_write_some.html "websocket::stream::async_write_some") are performed
until this operation completes.

If this is the beginning of a new message, the message opcode will be set
to text or binary based on the current setting of the [`binary`](binary.html "websocket::stream::binary") (or [`text`](text.html "websocket::stream::text")) option. The actual payload
sent may be transformed as per the WebSocket protocol settings.

This function always writes a complete WebSocket frame (not WebSocket message)
upon successful completion, so it is well defined to perform ping, pong,
and close operations in parallel to this operation.

###### [Parameters](async_write_some.html#beast.ref.boost__beast__websocket__stream.async_write_some.parameters)

| Name | Description |
| --- | --- |
| `fin` | `true` if this is the last part of the message. |
| `buffers` | The buffers containing the message part to send. The implementation will make copies of this object as needed, but ownership of the underlying memory is not transferred. The caller is responsible for ensuring that the memory locations pointed to by buffers remains valid until the completion handler is called. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & ec,           // Result of operation     std::size_t bytes_transferred   // Number of bytes sent from the                                     // buffers. If an error occurred,                                     // this will be less than the buffer_size. ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Per-Operation Cancellation](async_write_some.html#beast.ref.boost__beast__websocket__stream.async_write_some.per_operation_cancellation)

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