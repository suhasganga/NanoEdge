#### [http::async\_write\_some](boost__beast__http__async_write_some.html "http::async_write_some")

Write part of a message to a stream asynchronously using a serializer.

##### [Synopsis](boost__beast__http__async_write_some.html#beast.ref.boost__beast__http__async_write_some.synopsis)

Defined in header `<boost/beast/http/write.hpp>`

```programlisting
template<
    class AsyncWriteStream,
    bool isRequest,
    class Body,
    class Fields,
    class WriteHandler = net::default_completion_token_t<            executor_type<AsyncWriteStream>>>
DEDUCED
async_write_some(
    AsyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr,
    WriteHandler&& handler = net::default_completion_token_t< executor_type< AsyncWriteStream > >{});
```

##### [Description](boost__beast__http__async_write_some.html#beast.ref.boost__beast__http__async_write_some.description)

This function is used to write part of a message to a stream asynchronously
using a caller-provided HTTP/1 serializer. The function call always returns
immediately. The asynchronous operation will continue until one of the following
conditions is true:

* One or more bytes have been transferred.
* The function [`serializer::is_done`](boost__beast__http__serializer/is_done.html "http::serializer::is_done") returns `true`
* An error occurs on the stream.

This operation is implemented in terms of zero or more calls to the stream's
`async_write_some` function,
and is known as a *composed operation*. The program must
ensure that the stream performs no other writes until this operation completes.

The amount of data actually transferred is controlled by the behavior of
the underlying stream, subject to the buffer size limit of the serializer
obtained or set through a call to [`serializer::limit`](boost__beast__http__serializer/limit.html "http::serializer::limit"). Setting a limit and performing
bounded work helps applications set reasonable timeouts. It also allows application-level
flow control to function correctly. For example when using a TCP/IP based
stream.

##### [Parameters](boost__beast__http__async_write_some.html#beast.ref.boost__beast__http__async_write_some.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *AsyncWriteStream* concept. |
| `sr` | The serializer to use. The object must remain valid at least until the handler is called; ownership is not transferred. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error,        // result of operation     std::size_t bytes_transferred   // the number of bytes written to the stream ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |

##### [Per-Operation Cancellation](boost__beast__http__async_write_some.html#beast.ref.boost__beast__http__async_write_some.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`

if the `stream` also supports
terminal cancellation, `terminal`
cancellation leaves the stream in an undefined state, so that only closing
it is guaranteed to succeed.

##### [See Also](boost__beast__http__async_write_some.html#beast.ref.boost__beast__http__async_write_some.see_also)

[`serializer`](boost__beast__http__serializer.html "http::serializer")