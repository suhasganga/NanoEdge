#### [test::connect](boost__beast__test__connect.html "test::connect")

Connect two TCP sockets together.

```programlisting
template<
    class Executor>
bool
connect(
    net::basic_stream_socket< net::ip::tcp, Executor >& s1,
    net::basic_stream_socket< net::ip::tcp, Executor >& s2);
  » more...
```

Return a new stream connected to the given stream.

```programlisting
template<
    class... Args>
basic_stream
connect(
    basic_stream& to,
    Args&&... args);
  » more...
```