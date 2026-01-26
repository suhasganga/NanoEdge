##### [websocket::async\_teardown (1 of 2 overloads)](overload1.html "websocket::async_teardown (1 of 2 overloads)")

Start tearing down a connection.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__async_teardown.overload1.synopsis)

Defined in header `<boost/beast/websocket/teardown.hpp>`

```programlisting
template<
    class Socket,
    class TeardownHandler>
void
async_teardown(
    role_type role,
    Socket& socket,
    TeardownHandler&& handler);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__async_teardown.overload1.description)

This begins tearing down a connection asynchronously. The implementation
will call the overload of this function based on the `Socket`
parameter used to consruct the socket. When `Stream`
is a user defined type, and not a `net::ip::tcp::socket`
or any `net::ssl::stream`, callers are responsible for providing
a suitable overload of this function.

###### [Remarks](overload1.html#beast.ref.boost__beast__websocket__async_teardown.overload1.remarks)

This function serves as a customization point and is not intended to be
called directly.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__async_teardown.overload1.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the local endpoint |
| `socket` | The socket to tear down. |
| `handler` | The completion handler to invoke when the operation completes. The implementation takes ownership of the handler by performing a decay-copy. The equivalent function signature of the handler must be:   ```table-programlisting void handler(     error_code const & error // result of operation ); ```   If the handler has an associated immediate executor, an immediate completion will be dispatched to it. Otherwise, the handler will not be invoked from within this function. Invocation of the handler will be performed in a manner equivalent to using `net::post`. |