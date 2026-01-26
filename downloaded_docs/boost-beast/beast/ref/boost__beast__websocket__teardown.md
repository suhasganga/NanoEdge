#### [websocket::teardown](boost__beast__websocket__teardown.html "websocket::teardown")

Tear down a connection.

```programlisting
template<
    class Socket>
void
teardown(
    role_type role,
    Socket& socket,
    error_code& ec);
  » more...
```

Tear down a `net::ip::tcp::socket`.

```programlisting
template<
    class Protocol,
    class Executor>
void
teardown(
    role_type role,
    net::basic_stream_socket< Protocol, Executor >& socket,
    error_code& ec);
  » more...
```