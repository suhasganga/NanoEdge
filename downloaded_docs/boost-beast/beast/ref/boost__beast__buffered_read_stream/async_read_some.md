##### [buffered\_read\_stream::async\_read\_some](async_read_some.html "buffered_read_stream::async_read_some")

Start an asynchronous read.

###### [Synopsis](async_read_some.html#beast.ref.boost__beast__buffered_read_stream.async_read_some.synopsis)

```programlisting
template<
    class MutableBufferSequence,
    class ReadHandler = net::default_completion_token_t<executor_type>>
DEDUCED
async_read_some(
    MutableBufferSequence const& buffers,
    ReadHandler&& handler = net::default_completion_token_t< executor_type >{});
```

###### [Description](async_read_some.html#beast.ref.boost__beast__buffered_read_stream.async_read_some.description)

This function is used to asynchronously read data from the stream. The
function call always returns immediately.

###### [Parameters](async_read_some.html#beast.ref.boost__beast__buffered_read_stream.async_read_some.parameters)

| Name | Description |
| --- | --- |
| `buffers` | One or more buffers into which the data will be read. Although the buffers object may be copied as necessary, ownership of the underlying memory blocks is retained by the caller, which must guarantee that they remain valid until the handler is called. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error,      // result of operation     std::size_t bytes_transferred // number of bytes transferred ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed by dispatching to the immediate executor. If no immediate executor is specified, this is equivalent to using `net::post`. |