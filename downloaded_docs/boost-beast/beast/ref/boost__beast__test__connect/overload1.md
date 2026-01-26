##### [test::connect (1 of 2 overloads)](overload1.html "test::connect (1 of 2 overloads)")

Connect two TCP sockets together.

###### [Synopsis](overload1.html#beast.ref.boost__beast__test__connect.overload1.synopsis)

Defined in header `<boost/beast/_experimental/test/tcp.hpp>`

```programlisting
template<
    class Executor>
bool
connect(
    net::basic_stream_socket< net::ip::tcp, Executor >& s1,
    net::basic_stream_socket< net::ip::tcp, Executor >& s2);
```