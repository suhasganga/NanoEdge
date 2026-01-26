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
// Example: WebSocket client, coroutine
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
#if defined(BOOST\_ASIO\_HAS\_CO\_AWAIT)
namespace beast = boost::beast;
namespace http = beast::http;
namespace websocket = beast::websocket;
namespace net = boost::asio;
// Sends a WebSocket message and prints the response
net::awaitable
do\_session(std::string host, std::string port, std::string text)
{
auto executor = co\_await net::this\_coro::executor;
auto resolver = net::ip::tcp::resolver{ executor };
auto stream = websocket::stream{ executor };
// Look up the domain name
auto const results = co\_await resolver.async\_resolve(host, port);
// Set a timeout on the operation
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
auto ep = co\_await beast::get\_lowest\_layer(stream).async\_connect(results);
// Update the host\_ string. This will provide the value of the
// Host HTTP header during the WebSocket handshake.
// See https://tools.ietf.org/html/rfc7230#section-5.4
host += ':' + std::to\_string(ep.port());
// Turn off the timeout on the tcp\_stream, because
// the websocket stream has its own timeout system.
beast::get\_lowest\_layer(stream).expires\_never();
// Set suggested timeout settings for the websocket
stream.set\_option(
websocket::stream\_base::timeout::suggested(beast::role\_type::client));
// Set a decorator to change the User-Agent of the handshake
stream.set\_option(websocket::stream\_base::decorator(
[](websocket::request\_type& req)
{
req.set(
http::field::user\_agent,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-client-coro");
}));
// Perform the websocket handshake
co\_await stream.async\_handshake(host, "/");
// Send the message
co\_await stream.async\_write(net::buffer(text));
// This buffer will hold the incoming message
beast::flat\_buffer buffer;
// Read a message into our buffer
co\_await stream.async\_read(buffer);
// Close the WebSocket connection
co\_await stream.async\_close(websocket::close\_code::normal);
// If we get here then the connection is closed gracefully
// The make\_printable() function helps print a ConstBufferSequence
std::cout << beast::make\_printable(buffer.data()) << std::endl;
}
//------------------------------------------------------------------------------
int
main(int argc, char\*\* argv)
{
try
{
// Check command line arguments.
if(argc != 4)
{
std::cerr
<< "Usage: websocket-client-awaitable   \n"
<< "Example:\n"
<< " websocket-client-awaitable echo.websocket.org 80 \"Hello, world!\"\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const text = argv[3];
// The io\_context is required for all I/O
net::io\_context ioc;
// Launch the asynchronous operation
net::co\_spawn(
ioc,
do\_session(host, port, text),
[](std::exception\_ptr e)
{
if(e)
std::rethrow\_exception(e);
});
// Run the I/O service. The call will return when
// the socket is closed.
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