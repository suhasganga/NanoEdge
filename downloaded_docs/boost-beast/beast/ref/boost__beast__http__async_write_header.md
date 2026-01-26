#### [http::async\_write\_header](boost__beast__http__async_write_header.html "http::async_write_header")

Write a header to a stream asynchronously using a serializer.

##### [Synopsis](boost__beast__http__async_write_header.html#beast.ref.boost__beast__http__async_write_header.synopsis)

Defined in header `<boost/beast/http/write.hpp>`

```programlisting
template<
    class AsyncWriteStream,
    bool isRequest,
    class Body,
    class Fields,
    class WriteHandler = net::default_completion_token_t<            executor_type<AsyncWriteStream>>>
DEDUCED
async_write_header(
    AsyncWriteStream& stream,
    serializer< isRequest, Body, Fields >& sr,
    WriteHandler&& handler = net::default_completion_token_t< executor_type< AsyncWriteStream > >{});
```

##### [Description](boost__beast__http__async_write_header.html#beast.ref.boost__beast__http__async_write_header.description)

This function is used to write a header to a stream asynchronously using
a caller-provided HTTP/1 serializer. The function call always returns immediately.
The asynchronous operation will continue until one of the following conditions
is true:

* The function [`serializer::is_header_done`](boost__beast__http__serializer/is_header_done.html "http::serializer::is_header_done") returns `true`
* An error occurs.

This operation is implemented in terms of zero or more calls to the stream's
`async_write_some` function,
and is known as a *composed operation*. The program must
ensure that the stream performs no other writes until this operation completes.

##### [Parameters](boost__beast__http__async_write_header.html#beast.ref.boost__beast__http__async_write_header.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream to which the data is to be written. The type must support the *AsyncWriteStream* concept. |
| `sr` | The serializer to use. The object must remain valid at least until the handler is called; ownership is not transferred. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error,        // result of operation     std::size_t bytes_transferred   // the number of bytes written to the stream ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |

##### [Remarks](boost__beast__http__async_write_header.html#beast.ref.boost__beast__http__async_write_header.remarks)

The implementation will call [`serializer::split`](boost__beast__http__serializer/split.html "http::serializer::split") with the value `true` on the serializer passed in.

##### [Per-Operation Cancellation](boost__beast__http__async_write_header.html#beast.ref.boost__beast__http__async_write_header.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`

if the `stream` also supports
terminal cancellation, `terminal`
cancellation leaves the stream in an undefined state, so that only closing
it is guaranteed to succeed.

##### [See Also](boost__beast__http__async_write_header.html#beast.ref.boost__beast__http__async_write_header.see_also)

[`serializer`](boost__beast__http__serializer.html "http::serializer")