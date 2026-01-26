//
// Copyright (c) 2022 Klemens D. Morgenstern (klemens dot morgenstern at gmx dot net)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE\_1\_0.txt or copy at http://www.boost.org/LICENSE\_1\_0.txt)
//
// Official repository: https://github.com/boostorg/beast
//
//------------------------------------------------------------------------------
//
// Example: HTTP client, coroutine
//
//------------------------------------------------------------------------------
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include 
#include "example/common/root\_certificates.hpp"
#include 
#include 
#include 
#if defined(BOOST\_ASIO\_HAS\_CO\_AWAIT)
namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
namespace ssl = boost::asio::ssl;
//------------------------------------------------------------------------------
// Performs an HTTP GET and prints the response
net::awaitable
do\_session(
std::string host,
std::string port,
std::string target,
int version,
ssl::context& ctx)
{
auto executor = co\_await net::this\_coro::executor;
auto resolver = net::ip::tcp::resolver{ executor };
auto stream = ssl::stream{ executor, ctx };
// Set SNI Hostname (many hosts need this to handshake successfully)
if(! SSL\_set\_tlsext\_host\_name(stream.native\_handle(), host.c\_str()))
{
throw beast::system\_error(
static\_cast(::ERR\_get\_error()),
net::error::get\_ssl\_category());
}
// Set the expected hostname in the peer certificate for verification
stream.set\_verify\_callback(ssl::host\_name\_verification(host));
// Look up the domain name
auto const results = co\_await resolver.async\_resolve(host, port);
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
co\_await beast::get\_lowest\_layer(stream).async\_connect(results);
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Perform the SSL handshake
co\_await stream.async\_handshake(ssl::stream\_base::client);
// Set up an HTTP GET request message
http::request req{ http::verb::get, target, version };
req.set(http::field::host, host);
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Send the HTTP request to the remote host
co\_await http::async\_write(stream, req);
// This buffer is used for reading and must be persisted
beast::flat\_buffer buffer;
// Declare a container to hold the response
http::response res;
// Receive the HTTP response
co\_await http::async\_read(stream, buffer, res);
// Write the message to standard out
std::cout << res << std::endl;
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Gracefully close the stream - do not threat every error as an exception!
auto [ec] = co\_await stream.async\_shutdown(net::as\_tuple);
// ssl::error::stream\_truncated, also known as an SSL "short read",
// indicates the peer closed the connection without performing the
// required closing handshake (for example, Google does this to
// improve performance). Generally this can be a security issue,
// but if your communication protocol is self-terminated (as
// it is with both HTTP and WebSocket) then you may simply
// ignore the lack of close\_notify.
//
// https://github.com/boostorg/beast/issues/38
//
// https://security.stackexchange.com/questions/91435/how-to-handle-a-malicious-ssl-tls-shutdown
//
// When a short read would cut off the end of an HTTP message,
// Beast returns the error beast::http::error::partial\_message.
// Therefore, if we see a short read here, it has occurred
// after the message has been completed, so it is safe to ignore it.
if(ec && ec != net::ssl::error::stream\_truncated)
throw boost::system::system\_error(ec, "shutdown");
}
//------------------------------------------------------------------------------
int
main(int argc, char\*\* argv)
{
try
{
// Check command line arguments.
if(argc != 4 && argc != 5)
{
std::cerr
<< "Usage: http-client-awaitable    []\n"
<< "Example:\n"
<< " http-client-awaitable www.example.com 443 /\n"
<< " http-client-awaitable www.example.com 443 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
auto const version =
argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// The SSL context is required, and holds certificates
ssl::context ctx{ ssl::context::tlsv12\_client };
// This holds the root certificate used for verification
load\_root\_certificates(ctx);
// Verify the remote server's certificate
ctx.set\_verify\_mode(ssl::verify\_peer);
// Launch the asynchronous operation
net::co\_spawn(
ioc,
do\_session(host, port, target, version, ctx),
// If the awaitable exists with an exception, it gets delivered here
// as `e`. This can happen for regular errors, such as connection
// drops.
[](std::exception\_ptr e)
{
if(e)
std::rethrow\_exception(e);
});
// Run the I/O service. The call will return when
// the get operation is complete.
ioc.run();
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
return EXIT\_SUCCESS;
}
#else
int
main(int, char\*[])
{
std::printf("awaitables require C++20\n");
return EXIT\_FAILURE;
}
#endif