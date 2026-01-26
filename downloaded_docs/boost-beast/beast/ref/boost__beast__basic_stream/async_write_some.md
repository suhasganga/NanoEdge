##### [basic\_stream::async\_write\_some](async_write_some.html "basic_stream::async_write_some")

Write some data asynchronously.

###### [Synopsis](async_write_some.html#beast.ref.boost__beast__basic_stream.async_write_some.synopsis)

```programlisting
template<
    class ConstBufferSequence,
    class WriteHandler = net::default_completion_token_t<Executor>>
DEDUCED
async_write_some(
    ConstBufferSequence const& buffers,
    WriteHandler&& handler = net::default_completion_token_t< Executor >{});
```

###### [Description](async_write_some.html#beast.ref.boost__beast__basic_stream.async_write_some.description)

This function is used to asynchronously write data to the underlying socket.

This call always returns immediately. The asynchronous operation will continue
until one of the following conditions is true:

* One or more bytes are written to the stream.
* An error occurs.

The algorithm, known as a *composed asynchronous operation*,
is implemented in terms of calls to the next layer's `async_write_some`
function. The program must ensure that no other calls to [`async_write_some`](async_write_some.html "basic_stream::async_write_some") are performed
until this operation completes.

If the timeout timer expires while the operation is outstanding, the operation
will be canceled and the completion handler will be invoked with the error
[`error::timeout`](../boost__beast__error.html "error").

###### [Parameters](async_write_some.html#beast.ref.boost__beast__basic_stream.async_write_some.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The buffers from which the data will be written. If the size of the buffers is zero bytes, the operation always completes immediately with no error. Although the buffers object may be copied as necessary, ownership of the underlying memory blocks is retained by the caller, which must guarantee that they remain valid until the handler is called. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code error,               // Result of operation.     std::size_t bytes_transferred   // Number of bytes written. ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Remarks](async_write_some.html#beast.ref.boost__beast__basic_stream.async_write_some.remarks)

The `async_write_some` operation
may not transmit all of the requested number of bytes. Consider using the
function `net::async_write` if you need to ensure that
the requested amount of data is sent before the asynchronous operation
completes.

###### [Per-Operation Cancellation](async_write_some.html#beast.ref.boost__beast__basic_stream.async_write_some.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::partial`
* `net::cancellation_type::total`

if they are also supported by the socket's `async_write_some`
operation.