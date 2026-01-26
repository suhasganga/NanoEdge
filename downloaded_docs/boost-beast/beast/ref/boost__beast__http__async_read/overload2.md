##### [http::async\_read (2 of 2 overloads)](overload2.html "http::async_read (2 of 2 overloads)")

Read a complete message asynchronously from a stream.

###### [Synopsis](overload2.html#beast.ref.boost__beast__http__async_read.overload2.synopsis)

Defined in header `<boost/beast/http/read.hpp>`

```programlisting
template<
    class AsyncReadStream,
    class DynamicBuffer,
    bool isRequest,
    class Body,
    class Allocator,
    class ReadHandler = net::default_completion_token_t<            executor_type<AsyncReadStream>>>
DEDUCED
async_read(
    AsyncReadStream& stream,
    DynamicBuffer& buffer,
    message< isRequest, Body, basic_fields< Allocator > >& msg,
    ReadHandler&& handler = net::default_completion_token_t< executor_type< AsyncReadStream > >{});
```

###### [Description](overload2.html#beast.ref.boost__beast__http__async_read.overload2.description)

This function is used to asynchronously read a complete message from a
stream into an instance of [`message`](../boost__beast__http__message.html "http::message"). The function call always
returns immediately. The asynchronous operation will continue until one
of the following conditions is true:

* The entire message is read in.
* An error occurs.

This operation is implemented in terms of zero or more calls to the next
layer's `async_read_some`
function, and is known as a *composed operation*. The
program must ensure that the stream performs no other reads until this
operation completes. The implementation may read additional bytes from
the stream that lie past the end of the message being read. These additional
bytes are stored in the dynamic buffer, which must be preserved for subsequent
reads.

If the end of file error is received while reading from the stream, then
the error returned from this function will be:

* [`error::end_of_stream`](../boost__beast__http__error.html "http::error")
  if no bytes were parsed, or
* [`error::partial_message`](../boost__beast__http__error.html "http::error")
  if any bytes were parsed but the message was incomplete, otherwise:
* A successful result. The next attempt to read will return [`error::end_of_stream`](../boost__beast__http__error.html "http::error")

###### [Parameters](overload2.html#beast.ref.boost__beast__http__async_read.overload2.parameters)

| Name | Description |
| --- | --- |
| `stream` | The stream from which the data is to be read. The type must meet the *AsyncReadStream* requirements. |
| `buffer` | Storage for additional bytes read by the implementation from the stream. This is both an input and an output parameter; on entry, the parser will be presented with any remaining data in the dynamic buffer's readable bytes sequence first. The type must meet the *DynamicBuffer* requirements. The object must remain valid at least until the handler is called; ownership is not transferred. |
| `msg` | The container in which to store the message contents. This message container should not have previous contents, otherwise the behavior is undefined. The type must be meet the *MoveAssignable* and *MoveConstructible* requirements. The object must remain valid at least until the handler is called; ownership is not transferred. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error,        // result of operation     std::size_t bytes_transferred   // the number of bytes consumed by the parser ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |

###### [Remarks](overload2.html#beast.ref.boost__beast__http__async_read.overload2.remarks)

The implementation will call [`basic_parser::eager`](../boost__beast__http__basic_parser/eager.html "http::basic_parser::eager") with the value `true` on the parser passed in.

###### [Per-Operation Cancellation](overload2.html#beast.ref.boost__beast__http__async_read.overload2.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`

if the `stream` also supports
terminal cancellation, `terminal`
cancellation leaves the stream in an undefined state, so that only closing
it is guaranteed to succeed.