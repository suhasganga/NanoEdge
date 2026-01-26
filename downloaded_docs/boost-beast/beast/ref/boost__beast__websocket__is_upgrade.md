#### [websocket::is\_upgrade](boost__beast__websocket__is_upgrade.html "websocket::is_upgrade")

Returns `true` if the specified
HTTP request is a WebSocket Upgrade.

##### [Synopsis](boost__beast__websocket__is_upgrade.html#beast.ref.boost__beast__websocket__is_upgrade.synopsis)

Defined in header `<boost/beast/websocket/rfc6455.hpp>`

```programlisting
template<
    class Allocator>
bool
is_upgrade(
    beast::http::header< true, http::basic_fields< Allocator > > const& req);
```

##### [Description](boost__beast__websocket__is_upgrade.html#beast.ref.boost__beast__websocket__is_upgrade.description)

This function returns `true` when
the passed HTTP Request indicates a WebSocket Upgrade. It does not validate
the contents of the fields: it just trivially accepts requests which could
only possibly be a valid or invalid WebSocket Upgrade message.

Callers who wish to manually read HTTP requests in their server implementation
can use this function to determine if the request should be routed to an
instance of [`websocket::stream`](boost__beast__websocket__stream.html "websocket::stream").

##### [Example](boost__beast__websocket__is_upgrade.html#beast.ref.boost__beast__websocket__is_upgrade.example)

```programlisting
void handle_connection(net::ip::tcp::socket& sock)
{
    boost::beast::flat_buffer buffer;
    boost::beast::http::request<boost::beast::http::string_body> req;
    boost::beast::http::read(sock, buffer, req);
    if (boost::beast::websocket::is_upgrade(req))
    {
        boost::beast::websocket::stream< decltype (sock)> ws{std::move(sock)};
        ws.accept(req);
    }
}
```

##### [Parameters](boost__beast__websocket__is_upgrade.html#beast.ref.boost__beast__websocket__is_upgrade.parameters)

| Name | Description |
| --- | --- |
| `req` | The HTTP Request object to check. |

##### [Return Value](boost__beast__websocket__is_upgrade.html#beast.ref.boost__beast__websocket__is_upgrade.return_value)

`true` if the request is a WebSocket
Upgrade.