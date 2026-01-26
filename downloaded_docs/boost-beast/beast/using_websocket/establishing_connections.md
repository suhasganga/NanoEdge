### [Connecting](establishing_connections.html "Connecting")

Before messages can be exchanged, a websocket stream first needs to be connected,
and then to have the websocket handshake performed. The stream delegates
the task of establishing the connection to the next layers. For example,
if the next layer is a connectible stream or socket object, it can be accessed
to call the necessary function for connecting. Here we make an outbound connection
as a client would do.

```programlisting
stream<tcp_stream> ws(ioc);
net::ip::tcp::resolver resolver(ioc);

// Connect the socket to the IP address returned from performing a name lookup
get_lowest_layer(ws).connect(resolver.resolve("example.com", "ws"));
```

To accept incoming connections, an acceptor is used. The websocket stream
may be constructed from the socket returned by the acceptor when an incoming
connection is established.

```programlisting
net::ip::tcp::acceptor acceptor(ioc);
acceptor.bind(net::ip::tcp::endpoint(net::ip::tcp::v4(), 0));
acceptor.listen();

// The socket returned by accept() will be forwarded to the tcp_stream,
// which uses it to perform a move-construction from the net::ip::tcp::socket.

stream<tcp_stream> ws(acceptor.accept());
```

Alternatively, the incoming connection may be accepted directly into the
socket owned by the websocket stream, using this overload of the acceptor
member function.

```programlisting
// The stream will use the strand for invoking all completion handlers
stream<tcp_stream> ws(net::make_strand(ioc));

// This overload of accept uses the socket provided for the new connection.
// The function `tcp_stream::socket` provides access to the low-level socket
// object contained in the tcp_stream.

acceptor.accept(get_lowest_layer(ws).socket());
```