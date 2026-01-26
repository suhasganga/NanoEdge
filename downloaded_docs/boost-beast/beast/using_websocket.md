## [WebSocket](using_websocket.html "WebSocket")

The WebSocket Protocol enables two-way communication between a client running
untrusted code in a controlled environment to a remote host that has opted-in
to communications from that code. The protocol consists of an opening handshake
followed by basic message framing, layered over TCP. The goal of this technology
is to provide a mechanism for browser-based applications needing two-way communication
with servers without relying on opening multiple HTTP connections.

Beast provides developers with a robust WebSocket implementation built on Boost.Asio
with a consistent asynchronous model using a modern C++ approach.

|  |  |
| --- | --- |
| [Note] | Note |
| This documentation assumes familiarity with [Boost.Asio](../../../../../libs/asio/index.html) and the protocol specification described in [rfc6455](https://tools.ietf.org/html/rfc6455). Sample code and identifiers appearing in this section is written as if these declarations are in effect:   ```programlisting #include <boost/beast.hpp> #include <boost/asio.hpp> #include <boost/asio/ssl.hpp> ```      ```programlisting namespace net = boost::asio; namespace beast = boost::beast; using namespace boost::beast; using namespace boost::beast::websocket;  net::io_context ioc; tcp_stream sock(ioc); net::ssl::context ctx(net::ssl::context::tlsv12); ``` |

#### [Construction](using_websocket.html#beast.using_websocket.construction)

A WebSocket connection requires a stateful object, represented in Beast by
a single class template [`websocket::stream`](ref/boost__beast__websocket__stream.html "websocket::stream"). The interface uses the layered
stream model. A websocket stream object contains another stream object, called
the "next layer", which it uses to perform I/O. Descriptions of each
template parameter follow:

```programlisting
namespace boost {
namespace beast {
namespace websocket {

template<
    class NextLayer,
    bool deflateSupported = true>
class stream;

} // websocket
} // beast
} // boost
```

**Table 1.30. WebSocket Stream Template Parameters**

| Name | Description |
| --- | --- |
| `NextLayer` | The type of the next layer. An object of this type will be constructed and maintained for the lifetime of the stream. All reads and writes will go through the next layer. This type must meet the requirements of either [*SyncStream*](concepts/streams.html#beast.concepts.streams.SyncStream), [*AsyncStream*](concepts/streams.html#beast.concepts.streams.AsyncStream), or both, depending on the style of I/O that is to be performed. |
| `deflateSupported` | When this value is `true`, the stream will support (but not require) the [permessage-deflate extension](https://tools.ietf.org/html/rfc7692). Whether or not the stream actually requests or accepts the extension during a handshake depends on a separate configurable option.  When the value is `false` the extension is disabled. Streams will never request the extension in the client role or accept a request for the extension in the server role. An additional benefit of disabling the extension is that compilation will be faster, and the resulting program executable will contain less code. |

  

When a stream is constructed, any arguments provided to the constructor are
forwarded to the next layer object's constructor. This declares a stream over
a plain TCP/IP socket using an I/O context:

```programlisting
// This newly constructed WebSocket stream will use the specified
// I/O context and have support for the permessage-deflate extension.

stream<tcp_stream> ws(ioc);
```

|  |  |
| --- | --- |
| [Tip] | Tip |
| Websocket streams use their own protocol-specific timeout feature. When using a websocket stream with the [`tcp_stream`](ref/boost__beast__tcp_stream.html "tcp_stream") or [`basic_stream`](ref/boost__beast__basic_stream.html "basic_stream") class template, timeouts should be disabled on the TCP or basic stream after the connection is established, otherwise the behavior of the stream is undefined. |

As with most I/O objects, a websocket stream is **not thread-safe**.
Undefined behavior results if two different threads access the object concurrently.
For multi-threaded programs, the `tcp_stream`
can be constructed from an executor, in this case a strand. The stream declared
below will use a strand to invoke all completion handlers:

```programlisting
// The `tcp_stream` will be constructed with a new
// strand which uses the specified I/O context.

stream<tcp_stream> ws(net::make_strand(ioc));
```

If the next layer supports move-construction, then the websocket stream can
be constructed from a moved-from object.

```programlisting
// Ownership of the `tcp_stream` is transferred to the websocket stream

stream<tcp_stream> ws(std::move(sock));
```

The next layer may be accessed by calling [`stream::next_layer`](ref/boost__beast__websocket__stream/next_layer/overload1.html "websocket::stream::next_layer (1 of 2 overloads)").

```programlisting
// Calls `close` on the underlying `beast::tcp_stream`
ws.next_layer().close();
```

#### [Using SSL](using_websocket.html#beast.using_websocket.using_ssl)

To use WebSockets over SSL, use an instance of the [`net::ssl::stream`](../../../../../doc/html/boost_asio/reference/ssl__stream.html)
class template as the template type for the stream. The required [`net::io_context`](../../../../../doc/html/boost_asio/reference/io_context.html)
and [`net::ssl::context`](../../../../../doc/html/boost_asio/reference/ssl__context.html)
arguments are forwarded to the wrapped stream's constructor:

```programlisting
// The WebSocket stream will use SSL and a new strand
stream<net::ssl::stream<tcp_stream>> wss(net::make_strand(ioc), ctx);
```

|  |  |
| --- | --- |
| [Important] | Important |
| Code which declares websocket stream objects using Asio SSL types must include the file `<boost/beast/websocket/ssl.hpp>`. |

As before, the underlying SSL stream may be accessed by calling `next_layer`.

```programlisting
// Perform the SSL handshake in the client role
wss.next_layer().handshake(net::ssl::stream_base::client);
```

With multi-layered streams such as the one declared above, accessing an individual
layer can be cumbersome when using chained calls to `next_layer`.
The function [`get_lowest_layer`](ref/boost__beast__get_lowest_layer.html "get_lowest_layer") returns the last
stream in a stack of layers in a layered stream. Here we access the lowest
layer to cancel all outstanding I/O.

```programlisting
// Cancel all pending I/O on the underlying `tcp_stream`
get_lowest_layer(wss).cancel();
```

#### [Non-Blocking Mode](using_websocket.html#beast.using_websocket.non_blocking_mode)

Please note that websocket streams do not support non-blocking modes.