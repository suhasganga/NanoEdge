#### [async\_teardown](boost__beast__async_teardown.html "async_teardown")

Start tearing down a `net::ssl::stream`.

##### [Synopsis](boost__beast__async_teardown.html#beast.ref.boost__beast__async_teardown.synopsis)

Defined in header `<boost/beast/websocket/ssl.hpp>`

```programlisting
template<
    class AsyncStream,
    class TeardownHandler>
void
async_teardown(
    role_type role,
    net::ssl::stream< AsyncStream >& stream,
    TeardownHandler&& handler);
```

##### [Description](boost__beast__async_teardown.html#beast.ref.boost__beast__async_teardown.description)

This begins tearing down a connection asynchronously. The implementation
will call the overload of this function based on the `Stream`
parameter used to consruct the socket. When `Stream`
is a user defined type, and not a `net::ip::tcp::socket`
or any `net::ssl::stream`,
callers are responsible for providing a suitable overload of this function.

##### [Remarks](boost__beast__async_teardown.html#beast.ref.boost__beast__async_teardown.remarks)

This function serves as a customization point and is not intended to be called
directly.

##### [Parameters](boost__beast__async_teardown.html#beast.ref.boost__beast__async_teardown.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the local endpoint |
| `stream` | The stream to tear down. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error // result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |

##### [Per-Operation Cancellation](boost__beast__async_teardown.html#beast.ref.boost__beast__async_teardown.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::partial`
* `net::cancellation_type::total`

if they are also supported by the socket's `async_teardown`
and `async_shutdown` operation.