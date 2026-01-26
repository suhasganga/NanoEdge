### [Timeouts 💡](timeouts.html "Timeouts 💡")

Network programs must handle adverse connection conditions; the most common
is that a connected peer goes offline unexpectedly. Protocols have no way
of identifying this reliably: the peer is offline after all, and unable to
send a message announcing the absence. A peer can go offline for various
reasons:

* The peer experiences a power loss
* The peer becomes disconnected from the network
* The local host becomes disconnected from the network
* The network itself becomes unavailable

To determine when a peer is offline or idle, a program will implement a
[timeout](https://en.wikipedia.org/wiki/Timeout_(computing))
algorithm, which closes the connection after a specified amount of time if
some condition is met. For example, if no data is received for the duration.
A timeout may be used to:

* Drop malicious or poorly performing hosts
* Close idle connections to free up resources
* Determine if a peer is offline or no longer available

Traditionally, programs use a [`net::steady_timer`](../../../../../../doc/html/boost_asio/reference/steady_timer.html)
to determine when a timeout occurs, and then call [`close`](../../../../../../doc/html/boost_asio/reference/basic_socket/close/overload2.html) on the socket to release
the resources. The complexity of managing a separate timer is often a source
of [frustration](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1269r0.html#timers)
for non-experts.

|  |  |
| --- | --- |
| [Note] | Note |
| For portability reasons, networking does not provide timeouts or cancellation features for synchronous stream operations. |

To simplify the handling of timeouts, these provided types wrap a [`net::basic_stream_socket`](../../../../../../doc/html/boost_asio/reference/basic_stream_socket.html)
to provide additional features:

| Name | Features |
| --- | --- |
| [`tcp_stream`](../ref/boost__beast__tcp_stream.html "tcp_stream") | * Timeouts for logical operations * [`net::ip::tcp`](../../../../../../doc/html/boost_asio/reference/ip__tcp.html) protocol * [`net::executor`](../../../../../../doc/html/boost_asio/reference/executor.html) executor * [`unlimited_rate_policy`](../ref/boost__beast__unlimited_rate_policy.html "unlimited_rate_policy")   rate limits |
| [`basic_stream`](../ref/boost__beast__basic_stream.html "basic_stream") | * Timeouts for logical operations * Configurable [*Protocol*](../../../../../../doc/html/boost_asio/reference/Protocol.html)   type * Configurable [*Executor*](../../../../../../doc/html/boost_asio/reference/Executor1.html)   type * Configurable [*RatePolicy*](../concepts/RatePolicy.html "RatePolicy")   type |

##### [Construction](timeouts.html#beast.using_io.timeouts.construction)

The `tcp_stream` is designed
as a replacement for [`net::ip::tcp::socket`](../../../../../../doc/html/boost_asio/reference/ip__tcp/socket.html). Any program which currently
uses a socket, can switch to a `tcp_stream`
and achieve the features above (although some interfaces are different, see
below). Networking now allows I/O objects to construct with any instance
of [*ExecutionContext*](../../../../../../doc/html/boost_asio/reference/ExecutionContext.html)
or [*Executor*](../../../../../../doc/html/boost_asio/reference/Executor1.html)
objects. Here we construct a stream which uses a particular I/O context to
dispatch completion handlers:

```programlisting
// `ioc` will be used to dispatch completion handlers
tcp_stream stream(ioc);
```

Alternatively, we can construct the stream from an executor:

```programlisting
// The resolver is used to look up the IP addresses for a domain name
net::ip::tcp::resolver resolver(ioc);

// The stream will use the same executor as the resolver
tcp_stream stream(resolver.get_executor());
```

The function [`make_strand`](../../../../../../doc/html/boost_asio/reference/make_strand.html) returns a strand constructed
from an execution context or executor. When a [`net::strand`](../../../../../../doc/html/boost_asio/reference/strand.html)
is chosen for the stream's executor, all completion handlers which do not
already have an associated executor will use the strand. This is both a notational
convenience (no need for `strand::wrap`
or `bind_executor` at call
sites) and a measure of safety, as it is no longer possible to forget to
use the strand.

```programlisting
// The strand will be used to invoke all completion handlers
tcp_stream stream(net::make_strand(ioc));
```

##### [Connecting](timeouts.html#beast.using_io.timeouts.connecting)

Before data can be exchanged, the stream needs to be connected to a peer.
The following code sets a timeout for an asynchronous connect operation.
In Beast, functions to connect to a range of endpoints (such as the range
returned by [`net::ip::tcp::resolver::resolve`](../../../../../../doc/html/boost_asio/reference/ip__basic_resolver/resolve/overload3.html)) are members of the class
rather than free functions such as [`net::async_connect`](../../../../../../doc/html/boost_asio/reference/async_connect.html).

```programlisting
// Set the logical operation timer to 30 seconds
stream.expires_after (std::chrono::seconds(30));

// If the connection is not established within 30 seconds,
// the operation will be canceled and the handler will receive
// error::timeout as the error code.

stream.async_connect(resolver.resolve("www.example.com", "http"),
    [](error_code ec, net::ip::tcp::endpoint ep)
    {
        if(ec == error::timeout)
            std::cerr << "async_connect took too long\n";
        else if(! ec)
            std::cout << "Connected to " << ep << "\n";
    }
);

// The timer is still running. If we don't want the next
// operation to time out 30 seconds relative to the previous
// call  to `expires_after`, we need to turn it off before
// starting another asynchronous operation.

stream.expires_never();
```

A server will use an acceptor bound to a particular IP address and port to
listen to and receive incoming connection requests. The acceptor returns
an ordinary socket. A `tcp_stream`
can be move-constructed from the underlying `basic_stream_socket`
thusly:

```programlisting
// The acceptor is used to listen and accept incoming connections.
// We construct the acceptor to use a new strand, and listen
// on the loopback address with an operating-system assigned port.

net::ip::tcp::acceptor acceptor(net::make_strand(ioc));
acceptor.bind(net::ip::tcp::endpoint(net::ip::make_address_v4("127.0.0.1"), 0));
acceptor.listen(0);

// This blocks until a new incoming connection is established.
// Upon success, the function returns a new socket which is
// connected to the peer. The socket will have its own executor,
// which in the call below is a new strand for the I/O context.

net::ip::tcp::socket s = acceptor.accept(net::make_strand(ioc));

// Construct a new tcp_stream from the connected socket.
// The stream will use the strand created when the connection
// was accepted.

tcp_stream stream(std::move(s));
```

##### [Reading and Writing](timeouts.html#beast.using_io.timeouts.reading_and_writing)

Timeouts apply to the logical operation, expressed as a series of asynchronous
calls, rather than just the next call. This code reads a line from the stream
and writes it back. Both the read and the write must complete within 30 seconds
from when the timeout was set; the timer is not reset between operations.

```programlisting
std::string s;

// Set the logical operation timer to 30 seconds.
stream.expires_after (std::chrono::seconds(30));

// Read a line from the stream into the string.
net::async_read_until(stream, net::dynamic_buffer(s), '\n',
    [&s, &stream](error_code ec, std::size_t bytes_transferred)
    {
        if(ec)
            return;

        // read_until can read past the '\n', these will end up in
        // our buffer but we don't want to echo those extra received
        // bytes. `bytes_transferred` will be the number of bytes
        // up to and including the '\n'. We use `buffers_prefix` so
        // that extra data is not written.

        net::async_write(stream, buffers_prefix(bytes_transferred, net::buffer(s)),
            [&s](error_code ec, std::size_t bytes_transferred)
            {
                // Consume the line from the buffer
                s.erase(s.begin(), s.begin() + bytes_transferred);

                if(ec)
                    std::cerr << "Error: " << ec.message() << "\n";
            });
    });
```

Since reads and writes can take place concurrently, it is possible to have
two simultaneous logical operations where each operation either only reads,
or only writes. The beginning of a new read or write operation will use the
most recently set timeout. This will not affect operations that are already
outstanding.

```programlisting
std::string s1;
std::string s2;

// Set the logical operation timer to 15 seconds.
stream.expires_after (std::chrono::seconds(15));

// Read another line from the stream into our dynamic buffer.
// The operation will time out after 15 seconds.

net::async_read_until(stream, net::dynamic_buffer(s1), '\n', handler);

// Set the logical operation timer to 30 seconds.
stream.expires_after (std::chrono::seconds(30));

// Write the contents of the other buffer.
// This operation will time out after 30 seconds.

net::async_write(stream, net::buffer(s2), handler);
```

When a timeout is set, it cancels any previous read or write timeout for
which no outstanding operation is in progress. Algorithms which loop over
logical operations simply need to set the timeout once before the logical
operation, it is not necessary to call `expires_never`
in this case. Here we implement an algorithm which continuously echoes lines
back, with a timeout. This example is implemented as a complete function.

```programlisting
/** This function echoes back received lines from a peer, with a timeout.

    The algorithm terminates upon any error (including timeout).
*/
template <class Protocol, class Executor>
void do_async_echo (basic_stream<Protocol, Executor>& stream)
{
    // This object will hold our state when reading the line.

    struct echo_line
    {
        basic_stream<Protocol, Executor>& stream;

        // The shared pointer is used to extend the lifetime of the
        // string until the last asynchronous operation completes.
        std::shared_ptr<std::string> s;

        // This starts a new operation to read and echo a line
        void operator()()
        {
            // If a line is not sent and received within 30 seconds, then
            // the connection will be closed and this algorithm will terminate.

            stream.expires_after(std::chrono::seconds(30));

            // Read a line from the stream into our dynamic buffer, with a timeout
            net::async_read_until(stream, net::dynamic_buffer(*s), '\n', std::move(*this));
        }

        // This function is called when the read completes
        void operator()(error_code ec, std::size_t bytes_transferred)
        {
            if(ec)
                return;

            net::async_write(stream, buffers_prefix(bytes_transferred, net::buffer(*s)),
                [this](error_code ec, std::size_t bytes_transferred)
                {
                    s->erase(s->begin(), s->begin() + bytes_transferred);

                    if(! ec)
                    {
                        // Run this algorithm again
                        echo_line{stream, std::move(s)}();
                    }
                    else
                    {
                        std::cerr << "Error: " << ec.message() << "\n";
                    }
                });
        }
    };

    // Create the operation and run it
    echo_line{stream, std::make_shared<std::string>()}();
}
```

##### [https\_get](timeouts.html#beast.using_io.timeouts.https_get)

It is important to note that all of the examples thus far which perform reads
and writes with a timeout, make use of the existing networking stream algorithms.
As these algorithms are written generically to work with any object meeting
the stream requirements, they transparently support timeouts when used with
`tcp_stream`. This can be used
to enable timeouts for stream wrappers that do not currently support timeouts.

The following code establishes an encrypted connection, writes an HTTP request,
reads the HTTP response, and closes the connection gracefully. If these operations
take longer than 30 seconds total, a timeout occurs. This code is intended
to show how `tcp_stream` can
be used to enable timeouts across unmodified stream algorithms which were
not originally written to support timing out, and how a blocking algorithm
may be written from asynchronous intermediate operations.

```programlisting
/** Request an HTTP resource from a TLS host and return it as a string, with a timeout.

    This example uses fibers (stackful coroutines) and its own I/O context.
*/
std::string
https_get (std::string const& host, std::string const& target, error_code& ec)
{
    // It is the responsibility of the algorithm to clear the error first.
    ec = {};

    // We use our own I/O context, to make this function blocking.
    net::io_context ioc;

    // This context is used to hold client and server certificates.
    // We do not perform certificate verification in this example.

    net::ssl::context ctx(net::ssl::context::tlsv12);

    // This string will hold the body of the HTTP response, if any.
    std::string result;

    // Note that Networking TS does not come with spawn. This function
    // launches a "fiber" which is a coroutine that has its own separately
    // allocated stack.

    boost::asio::spawn(ioc,
    [&](boost::asio::yield_context yield)
    {
        net::ssl::stream<tcp_stream> stream(ioc, ctx);

        // The resolver will be used to look up the IP addresses for the host name
        net::ip::tcp::resolver resolver(ioc);

        // First, look up the name. Networking has its own timeout for this.
        // The `yield` object is a CompletionToken which specializes the
        // `net::async_result` customization point to make the fiber work.
        //
        // This call will appear to "block" until the operation completes.
        // It isn't really blocking. Instead, the fiber implementation saves
        // the call stack and suspends the function until the asynchronous
        // operation is complete. Then it restores the call stack, and resumes
        // the function to the statement following the async_resolve. This
        // allows an asynchronous algorithm to be expressed synchronously.

        auto const endpoints = resolver.async_resolve(host, "https", {}, yield[ec]);
        if(ec)
            return;

        // The function `get_lowest_layer` retrieves the "bottom most" object
        // in the stack of stream layers. In this case it will be the tcp_stream.
        // This timeout will apply to all subsequent operations collectively.
        // That is to say, they must all complete within the same 30 second
        // window.

        get_lowest_layer(stream).expires_after(std::chrono::seconds(30));

        // `tcp_stream` range connect algorithms are member functions, unlike net::
        get_lowest_layer(stream).async_connect(endpoints, yield[ec]);
        if(ec)
            return;

        // Perform the TLS handshake
        stream.async_handshake(net::ssl::stream_base::client, yield[ec]);
        if(ec)
            return;

        // Send an HTTP GET request for the target
        {
            http::request<http::empty_body> req;
            req.method(http::verb::get);
            req.target(target);
            req.version(11);
            req.set(http::field::host, host);
            req.set(http::field::user_agent, "Beast");
            http::async_write(stream, req, yield[ec]);
            if(ec)
                return;
        }

        // Now read the response
        flat_buffer buffer;
        http::response<http::string_body> res;
        http::async_read(stream, buffer, res, yield[ec]);
        if(ec)
            return;

        // Try to perform the TLS shutdown handshake
        stream.async_shutdown(yield[ec]);

        // `net::ssl::error::stream_truncated`, also known as an SSL "short read",
        // indicates the peer closed the connection without performing the
        // required closing handshake (for example, Google does this to
        // improve performance). Generally this can be a security issue,
        // but if your communication protocol is self-terminated (as
        // it is with both HTTP and WebSocket) then you may simply
        // ignore the lack of close_notify:
        //
        // https://github.com/boostorg/beast/issues/38
        //
        // https://security.stackexchange.com/questions/91435/how-to-handle-a-malicious-ssl-tls-shutdown
        //
        // When a short read would cut off the end of an HTTP message,
        // Beast returns the error beast::http::error::partial_message.
        // Therefore, if we see a short read here, it has occurred
        // after the message has been completed, so it is safe to ignore it.

        if(ec == net::ssl::error::stream_truncated)
            ec = {};
        else if(ec)
            return;

        // Set the string to return to the caller
        result = std::move(res.body());
    },
    // this will capture exceptions thrown by the coroutine,
    // which we're ignoring, since we're using error_codes to capture them.
    asio::detached);

    // `run` will dispatch completion handlers, and block until there is
    // no more "work" remaining. When this call returns, the operations
    // are complete and we can give the caller the result.
    ioc.run();

    return result;
}
```