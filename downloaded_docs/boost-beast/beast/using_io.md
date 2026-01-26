## [Networking](using_io.html "Networking")

This library uses the [Networking
Technical Specification](http://cplusplus.github.io/networking-ts/draft.pdf), scheduled to become an official part of C++
no sooner than the year 2023. Three implementations exist, with cosmetic differences
but otherwise using the same function signatures and type declarations: Boost.Asio,
stand-alone Asio, and networking-ts-impl. This table shows how a variable of
type `io_context` is declared
in each implementation by including the appropriate header and using a suitable
namespace alias:

**Table 1.2. Networking Implementations**

| Name | Namespace and Header Example |
| --- | --- |
| [Boost.Asio](../../../../../libs/asio/index.html) | ```programlisting #include <boost/asio/io_context.hpp> namespace net = boost::asio; net::io_context ioc; ``` |
| [Asio (Standalone)](https://think-async.com/Asio/) | ```programlisting #include <asio/io_context.hpp> namespace net = asio; net::io_context ioc; ``` |
| [networking-ts-impl](https://github.com/chriskohlhoff/networking-ts-impl) | ```programlisting #include <experimental/io_context> namespace net = std::experimental::net; net::io_context ioc; ``` |

  

This document refers to the three implementations above interchangeably and
collectively as **Networking** (or just *networking*).
The Boost.Asio and Asio flavors of Networking provide additional features not
currently proposed for C++, but likely to appear in a future specification,
such as:

* [Serial
  ports](../../../../../doc/html/boost_asio/reference/serial_port.html)
* [UNIX
  domain sockets](../../../../../doc/html/boost_asio/reference/local__stream_protocol.html)
* [POSIX
  signals](../../../../../doc/html/boost_asio/reference/signal_set.html) (e.g. SIGINT, SIGABORT)
* [TLS
  streams](../../../../../doc/html/boost_asio/reference/ssl__stream.html) (such as OpenSSL)

Boost.Beast depends specifically on the Boost.Asio flavor of Networking, although
this may change in the future. While this library offers performant implementations
of the HTTP and WebSocket network protocols, it depends on the networking interfaces
to perform general tasks such as performing domain name resolution (DNS lookup),
establishing outgoing connections, and accepting incoming connections. Callers
are responsible for interacting with networking to initialize objects to the
correct state where they are usable by this library.

In this documentation, the example code, and the implementation, the `net` namespace is used to qualify Networking
identifiers. For Boost.Beast, `net`
will be an alias for the `boost::asio` namespace.

To further ease of use, this library provides an extensive collection of types
and algorithms. This section of the documentation explains these types and
algorithms, provides examples of usage, and also provides refreshers and tutorials
for working with networking.

#### [Abbreviations](using_io.html#beast.using_io.abbreviations)

This documentation assumes familiarity with [Boost.Asio](../../../../../libs/asio/index.html),
which is required to work with Beast. Sample code and identifiers used throughout
are written as if the following declarations are in effect:

```programlisting
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/asio.hpp>
#include <boost/asio/ssl.hpp>
#include <iostream>
#include <thread>
```

```programlisting
//
using namespace boost::beast;
namespace net = boost::asio;
namespace ssl = boost::asio::ssl;
using tcp = net::ip::tcp;

net::io_context ioc;
net::any_io_executor work =
    net::require(ioc.get_executor(),
        net::execution::outstanding_work.tracked);
std::thread t{[&](){ ioc.run(); }};

error_code ec;
tcp::socket sock{ioc};
```