##### [websocket::async\_teardown (2 of 2 overloads)](overload2.html "websocket::async_teardown (2 of 2 overloads)")

Start tearing down a `net::ip::tcp::socket`.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__async_teardown.overload2.synopsis)

Defined in header `<boost/beast/websocket/teardown.hpp>`

```programlisting
template<
    class Protocol,
    class Executor,
    class TeardownHandler>
void
async_teardown(
    role_type role,
    net::basic_stream_socket< Protocol, Executor >& socket,
    TeardownHandler&& handler);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__async_teardown.overload2.description)

This begins tearing down a connection asynchronously. The implementation
will call the overload of this function based on the `Stream`
parameter used to consruct the socket. When `Stream`
is a user defined type, and not a `net::ip::tcp::socket`
or any `net::ssl::stream`, callers are responsible for providing
a suitable overload of this function.

###### [Remarks](overload2.html#beast.ref.boost__beast__websocket__async_teardown.overload2.remarks)

This function serves as a customization point and is not intended to be
called directly.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__async_teardown.overload2.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the local endpoint |
| `socket` | The socket to tear down. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error // result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |

###### [Per-Operation Cancellation](overload2.html#beast.ref.boost__beast__websocket__async_teardown.overload2.per_operation_cancellation)

This asynchronous operation supports cancellation for the following net::cancellation\_type
values:

* `net::cancellation_type::terminal`
* `net::cancellation_type::partial`
* `net::cancellation_type::total`

if they are also supported by the socket's `async_wait`
operation.