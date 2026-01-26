##### [websocket::teardown (1 of 2 overloads)](overload1.html "websocket::teardown (1 of 2 overloads)")

Tear down a connection.

###### [Synopsis](overload1.html#beast.ref.boost__beast__websocket__teardown.overload1.synopsis)

Defined in header `<boost/beast/websocket/teardown.hpp>`

```programlisting
template<
    class Socket>
void
teardown(
    role_type role,
    Socket& socket,
    error_code& ec);
```

###### [Description](overload1.html#beast.ref.boost__beast__websocket__teardown.overload1.description)

This tears down a connection. The implementation will call the overload
of this function based on the `Socket`
parameter used to consruct the socket. When `Socket`
is a user defined type, and not a `net::ip::tcp::socket`
or any `net::ssl::stream`, callers are responsible for providing
a suitable overload of this function.

###### [Remarks](overload1.html#beast.ref.boost__beast__websocket__teardown.overload1.remarks)

This function serves as a customization point and is not intended to be
called directly.

###### [Parameters](overload1.html#beast.ref.boost__beast__websocket__teardown.overload1.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the local endpoint |
| `socket` | The socket to tear down. |
| `ec` | Set to the error if any occurred. |