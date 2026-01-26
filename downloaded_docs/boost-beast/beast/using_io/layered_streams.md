### [Layered Streams](layered_streams.html "Layered Streams")

Networking's [`net::ssl::stream`](../../../../../../doc/html/boost_asio/reference/ssl__stream.html)
is a class template meeting the requirements of both synchronous and asynchronous
read and write streams, implemented in terms of a "next layer"
object whose type is determined by a class template parameter. The SSL stream
constructs an instance of the next layer object internally, while allowing
external access through the observer `net::ssl::stream::next_layer()`.
This declares an SSL stream which uses a regular TCP/IP socket as the next
layer:

```programlisting
net::ssl::stream<net::ip::tcp::socket> ss(ioc, ctx);
```

Objects using this design pattern are referred to in networking as "a
stack of stream layers". In Beast we use the term *layered
stream*, although the property of having a next layer is not exclusive
to streams. As with the SSL stream, [`websocket::stream`](../ref/boost__beast__websocket__stream.html "websocket::stream") is a class template parameterized
on a next layer object. This declares a websocket stream which uses a regular
TCP/IP socket as the next layer:

```programlisting
websocket::stream<net::ip::tcp::socket> ws(ioc);
```

If a Secure WebSockets stream is desired, this is accomplished simply by
changing the type of the next layer and adjusting the constructor arguments
to match:

```programlisting
websocket::stream<net::ssl::stream<net::ip::tcp::socket>> ws(ioc, ctx);
```

Higher level abstractions can be developed in this fashion by nesting stream
layers to arbitrary degree. The stack of stream layers effectively forms
a compile-time singly linked list. The object at the end of this list is
called the *lowest layer*, and is special from the others
because it typically represents the underlying socket.

Beast comes with several layered stream wrappers, as well as facilities for
authoring and working with layered streams:

**Table 1.6. Layered Stream Algorithms and Types**

| Name | Description |
| --- | --- |
| [`basic_stream`](../ref/boost__beast__basic_stream.html "basic_stream") [`tcp_stream`](../ref/boost__beast__tcp_stream.html "tcp_stream") | This stream can be used for synchronous and asynchronous reading and writing. It allows timeouts to be set on logical operations, and can have an executor associated with the stream which is used to invoke completion handlers. This lets you set a strand on the stream once, which is then used for all asynchronous operations automatically. |
| [`buffered_read_stream`](../ref/boost__beast__buffered_read_stream.html "buffered_read_stream") | A buffered read stream meets the requirements for synchronous and asynchronous read and write streams, and additionally implements configurable buffering for reads. |
| [`close_socket`](../ref/boost__beast__close_socket.html "close_socket") | This function closes a socket by performing an unqualified call to the [`beast_close_socket`](../ref/boost__beast__beast_close_socket.html "beast_close_socket") customization point, allowing sockets to be closed in generic contexts in an extensible fashion. |
| [`get_lowest_layer`](../ref/boost__beast__get_lowest_layer.html "get_lowest_layer") | Returns the lowest layer in a stack of stream layers by recursively calling the `next_layer` member function on each object until reaching an object which lacks the member. This example puts a layered stream into non-blocking mode by retrieving the TCP/IP socket in the lowest layer and changing the socket option:   ```programlisting // Set non-blocking mode on a stack of stream // layers with a regular socket at the lowest layer. template <class Stream> void set_non_blocking (Stream& stream) {     error_code ec;     // A compile error here means your lowest layer is not the right type!     get_lowest_layer(stream).non_blocking(true, ec);     if(ec)         throw system_error{ec}; } ``` |
| [`http::icy_stream`](../ref/boost__beast__http__icy_stream.html "http::icy_stream") | An ICY stream transparently converts the non-standard "ICY 200 OK" HTTP response from Shoutcast servers into a conforming 200 level HTTP response. |
| [`lowest_layer_type`](../ref/boost__beast__lowest_layer_type.html "lowest_layer_type") | A metafunction to return the type of the lowest layer used in a type representing a stack of stream layers. This is the type of reference returned by [`get_lowest_layer`](../ref/boost__beast__get_lowest_layer.html "get_lowest_layer") |