#### [tcp\_stream](boost__beast__tcp_stream.html "tcp_stream")

A TCP/IP stream socket with timeouts and a polymorphic executor.

##### [Synopsis](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.synopsis)

Defined in header `<boost/beast/core/tcp_stream.hpp>`

```programlisting
using tcp_stream = basic_stream< net::ip::tcp, net::any_io_executor, unlimited_rate_policy >;
```

##### [Types](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.types)

| Name | Description |
| --- | --- |
| **[endpoint\_type](boost__beast__basic_stream/endpoint_type.html "basic_stream::endpoint_type")** | The endpoint type. |
| **[executor\_type](boost__beast__basic_stream/executor_type.html "basic_stream::executor_type")** | The type of the executor associated with the stream. |
| **[protocol\_type](boost__beast__basic_stream/protocol_type.html "basic_stream::protocol_type")** | The protocol type. |
| **[rebind\_executor](boost__beast__basic_stream__rebind_executor.html "basic_stream::rebind_executor")** | Rebinds the stream type to another executor. |
| **[socket\_type](boost__beast__basic_stream/socket_type.html "basic_stream::socket_type")** | The type of the underlying socket. |

##### [Member Functions](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.member_functions)

| Name | Description |
| --- | --- |
| **[async\_connect](boost__beast__basic_stream/async_connect.html "basic_stream::async_connect")** | Connect the stream to the specified endpoint asynchronously.  — Establishes a connection by trying each endpoint in a sequence asynchronously. |
| **[async\_read\_some](boost__beast__basic_stream/async_read_some.html "basic_stream::async_read_some")** | Read some data asynchronously. |
| **[async\_write\_some](boost__beast__basic_stream/async_write_some.html "basic_stream::async_write_some")** | Write some data asynchronously. |
| **[basic\_stream](boost__beast__basic_stream/basic_stream.html "basic_stream::basic_stream")** | Constructor.  — Move constructor. |
| **[cancel](boost__beast__basic_stream/cancel.html "basic_stream::cancel")** | Cancel all asynchronous operations associated with the socket. |
| **[close](boost__beast__basic_stream/close.html "basic_stream::close")** | Close the timed stream. |
| **[connect](boost__beast__basic_stream/connect.html "basic_stream::connect")** | Connect the stream to the specified endpoint.  — Establishes a connection by trying each endpoint in a sequence. |
| **[expires\_after](boost__beast__basic_stream/expires_after.html "basic_stream::expires_after")** | Set the timeout for subsequent logical operations. |
| **[expires\_at](boost__beast__basic_stream/expires_at.html "basic_stream::expires_at")** | Set the timeout for subsequent logical operations. |
| **[expires\_never](boost__beast__basic_stream/expires_never.html "basic_stream::expires_never")** | Disable the timeout for subsequent logical operations. |
| **[get\_executor](boost__beast__basic_stream/get_executor.html "basic_stream::get_executor")** | Get the executor associated with the object. |
| **[operator=](boost__beast__basic_stream/operator_eq_.html "basic_stream::operator=")** | Move assignment (deleted). |
| **[rate\_policy](boost__beast__basic_stream/rate_policy.html "basic_stream::rate_policy")** | Returns the rate policy associated with the object. |
| **[read\_some](boost__beast__basic_stream/read_some.html "basic_stream::read_some")** | Read some data. |
| **[release\_socket](boost__beast__basic_stream/release_socket.html "basic_stream::release_socket")** | Release ownership of the underlying socket. |
| **[socket](boost__beast__basic_stream/socket.html "basic_stream::socket")** | Return a reference to the underlying socket. |
| **[write\_some](boost__beast__basic_stream/write_some.html "basic_stream::write_some")** | Write some data. |
| **[~basic\_stream](boost__beast__basic_stream/_dtor_basic_stream.html "basic_stream::~basic_stream") [destructor]** | Destructor. |

This stream wraps a `net::basic_stream_socket` to provide the following
features:

* An *Executor* may be associated with the stream, which
  will be used to invoke any completion handlers which do not already have
  an associated executor. This achieves support for [[P1322R0]
  Networking TS enhancement to enable custom I/O executors](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1322r0.html).
* Timeouts may be specified for each logical asynchronous operation performing
  any reading, writing, or connecting.
* A *RatePolicy* may be associated with the stream,
  to implement rate limiting through the policy's interface.

Although the stream supports multiple concurrent outstanding asynchronous
operations, the stream object is not thread-safe. The caller is responsible
for ensuring that the stream is accessed from only one thread at a time.
This includes the times when the stream, and its underlying socket, are accessed
by the networking implementation. To meet this thread safety requirement,
all asynchronous operations must be performed by the stream within the same
implicit strand (only one thread `net::io_context::run`)
or within the same explicit strand, such as an instance of `net::strand`.

Completion handlers with explicit associated executors (such as those arising
from use of `net::bind_executor`) will be invoked by the stream
using the associated executor. Otherwise, the completion handler will be
invoked by the executor associated with the stream upon construction. The
type of executor used with this stream must meet the following requirements:

* Function objects submitted to the executor shall never run concurrently
  with each other.

The executor type `net::strand` meets these requirements. Use of
a strand as the executor in the stream class template offers an additional
notational convenience: the strand does not need to be specified in each
individual initiating function call.

Unlike other stream wrappers, the underlying socket is accessed through the
[`socket`](boost__beast__basic_stream/socket.html "basic_stream::socket") member function instead of
`next_layer`. This causes the
[`basic_stream`](boost__beast__basic_stream.html "basic_stream")
to be returned in calls to [`get_lowest_layer`](boost__beast__get_lowest_layer.html "get_lowest_layer").

##### [Usage](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.usage)

To use this stream declare an instance of the class. Then, before each logical
operation for which a timeout is desired, call [`expires_after`](boost__beast__basic_stream/expires_after.html "basic_stream::expires_after") with a duration, or
call [`expires_at`](boost__beast__basic_stream/expires_at.html "basic_stream::expires_at") with a time point. Alternatively,
call [`expires_never`](boost__beast__basic_stream/expires_never.html "basic_stream::expires_never") to disable the timeout
for subsequent logical operations. A logical operation is any series of one
or more direct or indirect calls to the timeout stream's asynchronous read,
asynchronous write, or asynchronous connect functions.

When a timeout is set and a mixed operation is performed (one that includes
both reads and writes, for example) the timeout applies to all of the intermediate
asynchronous operations used in the enclosing operation. This allows timeouts
to be applied to stream algorithms which were not written specifically to
allow for timeouts, when those algorithms are passed a timeout stream with
a timeout set.

When a timeout occurs the socket will be closed, canceling any pending I/O
operations. The completion handlers for these canceled operations will be
invoked with the error [`beast::error::timeout`](boost__beast__error.html "error").

##### [Examples](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.examples)

This function reads an HTTP request with a timeout, then sends the HTTP response
with a different timeout.

```programlisting
void process_http_1 (tcp_stream& stream, net::yield_context yield)
{
    flat_buffer buffer;
    http::request<http::empty_body> req;

    // Read the request, with a 15 second timeout
    stream.expires_after(std::chrono::seconds(15));
    http::async_read(stream, buffer, req, yield);

    // Calculate the response
    http::response<http::string_body> res = make_response(req);

    // Send the response, with a 30 second timeout.
    stream.expires_after (std::chrono::seconds(30));
    http::async_write (stream, res, yield);
}
```

The example above could be expressed using a single timeout with a simple
modification. The function that follows first reads an HTTP request then
sends the HTTP response, with a single timeout that applies to the entire
combined operation of reading and writing:

```programlisting
void process_http_2 (tcp_stream& stream, net::yield_context yield)
{
    flat_buffer buffer;
    http::request<http::empty_body> req;

    // Require that the read and write combined take no longer than 30 seconds
    stream.expires_after(std::chrono::seconds(30));

    http::async_read(stream, buffer, req, yield);

    http::response<http::string_body> res = make_response(req);
    http::async_write (stream, res, yield);
}
```

Some stream algorithms, such as `ssl::stream::async_handshake`
perform both reads and writes. A timeout set before calling the initiating
function of such composite stream algorithms will apply to the entire composite
operation. For example, a timeout may be set on performing the SSL handshake
thusly:

```programlisting
void do_ssl_handshake (net::ssl::stream<tcp_stream>& stream, net::yield_context yield)
{
    // Require that the SSL handshake take no longer than 10 seconds
    stream.expires_after(std::chrono::seconds(10));

    stream.async_handshake(net::ssl::stream_base::client, yield);
}
```

##### [Blocking I/O](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.blocking_i_o)

Synchronous functions behave identically as that of the wrapped `net::basic_stream_socket`.
Timeouts are not available when performing blocking calls.

##### [Template Parameters](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.template_parameters)

| Type | Description |
| --- | --- |
| `Protocol` | A type meeting the requirements of *Protocol* representing the protocol the protocol to use for the basic stream socket. A common choice is `net::ip::tcp`. |
| `Executor` | A type meeting the requirements of *Executor* to be used for submitting all completion handlers which do not already have an associated executor. If this type is omitted, the default of `net::any_io_executor` will be used. |

##### [Thread Safety](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.thread_safety)

*Distinct objects*: Safe.

*Shared objects*: Unsafe. The application must also ensure
that all asynchronous operations are performed within the same implicit or
explicit strand.

##### [See Also](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.see_also)

* [[P1322R0]
  Networking TS enhancement to enable custom I/O executors](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1322r0.html).

This rate policy object does not apply any rate limit.

* *RatePolicy*

##### [See Also](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.see_also0)

[`beast::basic_stream`](boost__beast__basic_stream.html "basic_stream"),
[`beast::tcp_stream`](boost__beast__tcp_stream.html "tcp_stream")

##### [See Also](boost__beast__tcp_stream.html#beast.ref.boost__beast__tcp_stream.see_also1)

[`basic_stream`](boost__beast__basic_stream.html "basic_stream")