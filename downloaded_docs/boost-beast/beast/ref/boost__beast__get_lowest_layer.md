#### [get\_lowest\_layer](boost__beast__get_lowest_layer.html "get_lowest_layer")

Return the lowest layer in a stack of stream layers.

##### [Synopsis](boost__beast__get_lowest_layer.html#beast.ref.boost__beast__get_lowest_layer.synopsis)

Defined in header `<boost/beast/core/stream_traits.hpp>`

```programlisting
template<
    class T>
lowest_layer_type< T >&
get_lowest_layer(
    T& t);
```

##### [Description](boost__beast__get_lowest_layer.html#beast.ref.boost__beast__get_lowest_layer.description)

If `t.next_layer()`
is well-defined, returns `get_lowest_layer(t.next_layer())`.
Otherwise, it returns `t`.

A stream layer is an object of class type which wraps another object through
composition, and meets some or all of the named requirements of the wrapped
type while optionally changing behavior. Examples of stream layers include
`net::ssl::stream`
or [`beast::websocket::stream`](boost__beast__websocket__stream.html "websocket::stream"). The owner of a stream layer
can interact directly with the wrapper, by passing it to stream algorithms.
Or, the owner can obtain a reference to the wrapped object by calling `next_layer()`
and accessing its members. This is necessary when it is desired to access
functionality in the next layer which is not available in the wrapper. For
example, [`websocket::stream`](boost__beast__websocket__stream.html "websocket::stream") permits reading and writing,
but in order to establish the underlying connection, members of the wrapped
stream (such as `connect`)
must be invoked directly.

Usually the last object in the chain of composition is the concrete socket
object (for example, a `net::basic_socket`
or a class derived from it). The function [`get_lowest_layer`](boost__beast__get_lowest_layer.html "get_lowest_layer") exists to easily
obtain the concrete socket when it is desired to perform an action that is
not prescribed by a named requirement, such as changing a socket option,
cancelling all pending asynchronous I/O, or closing the socket (perhaps by
using [`close_socket`](boost__beast__close_socket.html "close_socket")).

##### [Example](boost__beast__get_lowest_layer.html#beast.ref.boost__beast__get_lowest_layer.example)

```programlisting
// Set non-blocking mode on a stack of stream
// layers with a regular socket at the lowest layer.
template < class Stream>
void set_non_blocking (Stream& stream)
{
    error_code ec;
    // A compile error here means your lowest layer is not the right type!
    get_lowest_layer(stream).non_blocking( true , ec);
    if (ec)
        throw system_error{ec};
}
```

##### [Parameters](boost__beast__get_lowest_layer.html#beast.ref.boost__beast__get_lowest_layer.parameters)

| Name | Description |
| --- | --- |
| `t` | The layer in a stack of layered objects for which the lowest layer is returned. |

##### [See Also](boost__beast__get_lowest_layer.html#beast.ref.boost__beast__get_lowest_layer.see_also)

[`close_socket`](boost__beast__close_socket.html "close_socket"),
[`lowest_layer_type`](boost__beast__lowest_layer_type.html "lowest_layer_type")