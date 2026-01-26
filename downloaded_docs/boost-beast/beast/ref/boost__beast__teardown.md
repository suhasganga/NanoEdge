#### [teardown](boost__beast__teardown.html "teardown")

Tear down a `net::ssl::stream`.

##### [Synopsis](boost__beast__teardown.html#beast.ref.boost__beast__teardown.synopsis)

Defined in header `<boost/beast/websocket/ssl.hpp>`

```programlisting
template<
    class SyncStream>
void
teardown(
    role_type role,
    net::ssl::stream< SyncStream >& stream,
    error_code& ec);
```

##### [Description](boost__beast__teardown.html#beast.ref.boost__beast__teardown.description)

This tears down a connection. The implementation will call the overload of
this function based on the `Stream`
parameter used to consruct the socket. When `Stream`
is a user defined type, and not a `net::ip::tcp::socket`
or any `net::ssl::stream`,
callers are responsible for providing a suitable overload of this function.

##### [Remarks](boost__beast__teardown.html#beast.ref.boost__beast__teardown.remarks)

This function serves as a customization point and is not intended to be called
directly.

##### [Parameters](boost__beast__teardown.html#beast.ref.boost__beast__teardown.parameters)

| Name | Description |
| --- | --- |
| `role` | The role of the local endpoint |
| `stream` | The stream to tear down. |
| `ec` | Set to the error if any occurred. |