//
// Copyright (c) 2016-2019 Vinnie Falco (vinnie dot falco at gmail dot com)
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
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace websocket = beast::websocket; // from 
namespace net = boost::asio; // from 
using tcp = boost::asio::ip::tcp; // from 
//------------------------------------------------------------------------------
// Report a failure
void
fail(beast::error\_code ec, char const\* what)
{
std::cerr << what << ": " << ec.message() << "\n";
}
// Sends a WebSocket message and prints the response
void
do\_session(
std::string host,
std::string const& port,
std::string const& text,
net::io\_context& ioc,
net::yield\_context yield)
{
beast::error\_code ec;
// These objects perform our I/O
tcp::resolver resolver(ioc);
websocket::stream ws(ioc);
// Look up the domain name
auto const results = resolver.async\_resolve(host, port, yield[ec]);
if(ec)
return fail(ec, "resolve");
// Set a timeout on the operation
beast::get\_lowest\_layer(ws).expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
auto ep = beast::get\_lowest\_layer(ws).async\_connect(results, yield[ec]);
if(ec)
return fail(ec, "connect");
// Update the host\_ string. This will provide the value of the
// Host HTTP header during the WebSocket handshake.
// See https://tools.ietf.org/html/rfc7230#section-5.4
host += ':' + std::to\_string(ep.port());
// Turn off the timeout on the tcp\_stream, because
// the websocket stream has its own timeout system.
beast::get\_lowest\_layer(ws).expires\_never();
// Set suggested timeout settings for the websocket
ws.set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::client));
// Set a decorator to change the User-Agent of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::request\_type& req)
{
req.set(http::field::user\_agent,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-client-coro");
}));
// Perform the websocket handshake
ws.async\_handshake(host, "/", yield[ec]);
if(ec)
return fail(ec, "handshake");
// Send the message
ws.async\_write(net::buffer(std::string(text)), yield[ec]);
if(ec)
return fail(ec, "write");
// This buffer will hold the incoming message
beast::flat\_buffer buffer;
// Read a message into our buffer
ws.async\_read(buffer, yield[ec]);
if(ec)
return fail(ec, "read");
// Close the WebSocket connection
ws.async\_close(websocket::close\_code::normal, yield[ec]);
if(ec)
return fail(ec, "close");
// If we get here then the connection is closed gracefully
// The make\_printable() function helps print a ConstBufferSequence
std::cout << beast::make\_printable(buffer.data()) << std::endl;
}
//------------------------------------------------------------------------------
int main(int argc, char\*\* argv)
{
// Check command line arguments.
if(argc != 4)
{
std::cerr <<
"Usage: websocket-client-coro   \n" <<
"Example:\n" <<
" websocket-client-coro echo.websocket.org 80 \"Hello, world!\"\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const text = argv[3];
// The io\_context is required for all I/O
net::io\_context ioc;
// Launch the asynchronous operation
boost::asio::spawn(ioc, std::bind(
&do\_session,
std::string(host),
std::string(port),
std::string(text),
std::ref(ioc),
std::placeholders::\_1),
// on completion, spawn will call this function
[](std::exception\_ptr ex)
{
// if an exception occurred in the coroutine,
// it's something critical, e.g. out of memory
// we capture normal errors in the ec
// so we just rethrow the exception here,
// which will cause `ioc.run()` to throw
if (ex)
std::rethrow\_exception(ex);
});
// Run the I/O service. The call will return when
// the socket is closed.
ioc.run();
return EXIT\_SUCCESS;
}