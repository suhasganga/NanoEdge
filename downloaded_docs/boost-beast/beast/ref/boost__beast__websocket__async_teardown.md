#### [websocket::async\_teardown](boost__beast__websocket__async_teardown.html "websocket::async_teardown")

Start tearing down a connection.

```programlisting
template<
    class Socket,
    class TeardownHandler>
void
async_teardown(
    role_type role,
    Socket& socket,
    TeardownHandler&& handler);
  » more...
```

Start tearing down a `net::ip::tcp::socket`.

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
  » more...
```