##### [http::icy\_stream::async\_write\_some](async_write_some.html "http::icy_stream::async_write_some")

Start an asynchronous write.

###### [Synopsis](async_write_some.html#beast.ref.boost__beast__http__icy_stream.async_write_some.synopsis)

```programlisting
template<
    class ConstBufferSequence,
    class WriteHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_write_some(
    ConstBufferSequence const& buffers,
    WriteHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](async_write_some.html#beast.ref.boost__beast__http__icy_stream.async_write_some.description)

This function is used to asynchronously write one or more bytes of data
to the stream. The function call always returns immediately.

###### [Parameters](async_write_some.html#beast.ref.boost__beast__http__icy_stream.async_write_some.parameters)

| Name | Description |
| --- | --- |
| `buffers` | The data to be written to the stream. Although the buffers object may be copied as necessary, ownership of the underlying buffers is retained by the caller, which must guarantee that they remain valid until the handler is called. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(   error_code const & error,          // Result of operation.   std::size_t bytes_transferred     // Number of bytes written. ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |

###### [Remarks](async_write_some.html#beast.ref.boost__beast__http__icy_stream.async_write_some.remarks)

The `async_write_some` operation
may not transmit all of the data to the peer. Consider using the function
`net::async_write` if you need to ensure that
all data is written before the asynchronous operation completes.