#### [close\_socket](boost__beast__close_socket.html "close_socket")

Close a socket or socket-like object.

##### [Synopsis](boost__beast__close_socket.html#beast.ref.boost__beast__close_socket.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class Socket>
void
close_socket(
    Socket& sock);
```

##### [Description](boost__beast__close_socket.html#beast.ref.boost__beast__close_socket.description)

This function attempts to close an object representing a socket. In this
context, a socket is an object for which an unqualified call to the function
`void beast_close_socket(Socket&)` is well-defined. The function `beast_close_socket` is a *customization
point*, allowing user-defined types to provide an algorithm for
performing the close operation by overloading this function for the type
in question.

Since the customization point is a function call, the normal rules for finding
the correct overload are applied including the rules for argument-dependent
lookup ("ADL"). This permits classes derived from a type for which
a customization is provided to inherit the customization point.

An overload for the networking class template `net::basic_socket`
is provided, which implements the close algorithm for all socket-like objects
(hence the name of this customization point). When used in conjunction with
[`get_lowest_layer`](boost__beast__get_lowest_layer.html "get_lowest_layer"),
a generic algorithm operating on a layered stream can perform a closure of
the underlying socket without knowing the exact list of concrete types.

##### [Example 1](boost__beast__close_socket.html#beast.ref.boost__beast__close_socket.example_1)

The following generic function synchronously sends a message on the stream,
then closes the socket.

```programlisting
template < class WriteStream>
void hello_and_close (WriteStream& stream)
{
    net::write(stream, net::const_buffer( "Hello, world!" , 13));
    close_socket(get_lowest_layer(stream));
}
```

To enable closure of user defined types, it is necessary to provide an overload
of the function `beast_close_socket`
for the type.

##### [Example 2](boost__beast__close_socket.html#beast.ref.boost__beast__close_socket.example_2)

The following code declares a user-defined type which contains a private
socket, and provides an overload of the customization point which closes
the private socket.

```programlisting
class my_socket
{
    net::ip::tcp::socket sock_;

public :
    my_socket(net::io_context& ioc)
        : sock_(ioc)
    {
    }

    friend void beast_close_socket(my_socket& s)
    {
        error_code ec;
        s.sock_.close(ec);
        // ignore the error
    }
};
```

##### [Parameters](boost__beast__close_socket.html#beast.ref.boost__beast__close_socket.parameters)

| Name | Description |
| --- | --- |
| `sock` | The socket to close. If the customization point is not defined for the type of this object, or one of its base classes, then a compiler error results. |

##### [See Also](boost__beast__close_socket.html#beast.ref.boost__beast__close_socket.see_also)

[`beast_close_socket`](boost__beast__beast_close_socket.html "beast_close_socket")