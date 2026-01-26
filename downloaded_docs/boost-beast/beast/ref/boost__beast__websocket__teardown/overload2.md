##### [websocket::teardown (2 of 2 overloads)](overload2.html "websocket::teardown (2 of 2 overloads)")

Tear down a `net::ip::tcp::socket`.

###### [Synopsis](overload2.html#beast.ref.boost__beast__websocket__teardown.overload2.synopsis)

Defined in header `<boost/beast/websocket/teardown.hpp>`

```programlisting
template<
    class Protocol,
    class Executor>
void
teardown(
    role_type role,
    net::basic_stream_socket< Protocol, Executor >& socket,
    error_code& ec);
```

###### [Description](overload2.html#beast.ref.boost__beast__websocket__teardown.overload2.description)

This tears down a connection. The implementation will call the overload
of this function based on the `Stream`
parameter used to consruct the socket. When `Stream`
is a user defined type, and not a `net::ip::tcp::socket`
or any `net::ssl::stream`, callers are responsible for providing
a suitable overload of this function.

###### [Remarks](overload2.html#beast.ref.boost__beast__websocket__teardown.overload2.remarks)

This function serves as a customization point and is not intended to be
called directly.

###### [Parameters](overload2.html#beast.ref.boost__beast__websocket__teardown.overload2.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the local endpoint |
| `socket` | The socket to tear down. |
| `ec` | Set to the error if any occurred. |