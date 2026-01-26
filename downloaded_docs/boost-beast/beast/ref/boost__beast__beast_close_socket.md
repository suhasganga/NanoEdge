#### [beast\_close\_socket](boost__beast__beast_close_socket.html "beast_close_socket")

Default socket close function.

##### [Synopsis](boost__beast__beast_close_socket.html#beast.ref.boost__beast__beast_close_socket.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class Protocol,
    class Executor>
void
beast_close_socket(
    net::basic_socket< Protocol, Executor >& sock);
```

##### [Description](boost__beast__beast_close_socket.html#beast.ref.boost__beast__beast_close_socket.description)

This function is not meant to be called directly. Instead, it is called automatically
when using [`close_socket`](boost__beast__close_socket.html "close_socket"). To enable closure
of user-defined types or classes derived from a particular user-defined type,
this function should be overloaded in the corresponding namespace for the
type in question.

##### [See Also](boost__beast__beast_close_socket.html#beast.ref.boost__beast__beast_close_socket.see_also)

[`close_socket`](boost__beast__close_socket.html "close_socket")