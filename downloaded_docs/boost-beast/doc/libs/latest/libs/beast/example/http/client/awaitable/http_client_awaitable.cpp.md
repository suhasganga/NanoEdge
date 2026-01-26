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
#include 
#if defined(BOOST\_ASIO\_HAS\_CO\_AWAIT)
namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
// Performs an HTTP GET and prints the response
net::awaitable
do\_session(std::string host, std::string port, std::string target, int version)
{
auto executor = co\_await net::this\_coro::executor;
auto resolver = net::ip::tcp::resolver{ executor };
auto stream = beast::tcp\_stream{ executor };
// Look up the domain name
auto const results = co\_await resolver.async\_resolve(host, port);
// Set the timeout.
stream.expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
co\_await stream.async\_connect(results);
// Set up an HTTP GET request message
http::request req{ http::verb::get, target, version };
req.set(http::field::host, host);
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// Set the timeout.
stream.expires\_after(std::chrono::seconds(30));
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
// Gracefully close the socket
beast::error\_code ec;
stream.socket().shutdown(net::ip::tcp::socket::shutdown\_both, ec);
// not\_connected happens sometimes
// so don't bother reporting it.
//
if(ec && ec != beast::errc::not\_connected)
throw boost::system::system\_error(ec, "shutdown");
// If we get here then the connection is closed gracefully
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
std::cerr << "Usage: http-client-awaitable    []\n"
<< "Example:\n"
<< " http-client-awaitable www.example.com 80 /\n"
<< " http-client-awaitable www.example.com 80 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
auto const version =
argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// Launch the asynchronous operation
net::co\_spawn(
ioc,
do\_session(host, port, target, version),
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