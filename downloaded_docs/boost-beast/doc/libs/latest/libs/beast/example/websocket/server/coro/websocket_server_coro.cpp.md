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
// Example: WebSocket server, coroutine
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
// Echoes back all received WebSocket messages
void
do\_session(
websocket::stream& ws,
net::yield\_context yield)
{
beast::error\_code ec;
// Set suggested timeout settings for the websocket
ws.set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::server));
// Set a decorator to change the Server of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-server-coro");
}));
// Accept the websocket handshake
ws.async\_accept(yield[ec]);
if(ec)
return fail(ec, "accept");
for(;;)
{
// This buffer will hold the incoming message
beast::flat\_buffer buffer;
// Read a message
ws.async\_read(buffer, yield[ec]);
// This indicates that the session was closed
if(ec == websocket::error::closed)
break;
if(ec)
return fail(ec, "read");
// Echo the message back
ws.text(ws.got\_text());
ws.async\_write(buffer.data(), yield[ec]);
if(ec)
return fail(ec, "write");
}
}
//------------------------------------------------------------------------------
// Accepts incoming connections and launches the sessions
void
do\_listen(
net::io\_context& ioc,
tcp::endpoint endpoint,
net::yield\_context yield)
{
beast::error\_code ec;
// Open the acceptor
tcp::acceptor acceptor(ioc);
acceptor.open(endpoint.protocol(), ec);
if(ec)
return fail(ec, "open");
// Allow address reuse
acceptor.set\_option(net::socket\_base::reuse\_address(true), ec);
if(ec)
return fail(ec, "set\_option");
// Bind to the server address
acceptor.bind(endpoint, ec);
if(ec)
return fail(ec, "bind");
// Start listening for connections
acceptor.listen(net::socket\_base::max\_listen\_connections, ec);
if(ec)
return fail(ec, "listen");
for(;;)
{
tcp::socket socket(ioc);
acceptor.async\_accept(socket, yield[ec]);
if(ec)
fail(ec, "accept");
else
boost::asio::spawn(
acceptor.get\_executor(),
std::bind(
&do\_session,
websocket::stream<
beast::tcp\_stream>(std::move(socket)),
std::placeholders::\_1),
// we ignore the result of the session,
// most errors are handled with error\_code
boost::asio::detached);
}
}
int main(int argc, char\* argv[])
{
// Check command line arguments.
if (argc != 4)
{
std::cerr <<
"Usage: websocket-server-coro   \n" <<
"Example:\n" <<
" websocket-server-coro 0.0.0.0 8080 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const threads = std::max(1, std::atoi(argv[3]));
// The io\_context is required for all I/O
net::io\_context ioc(threads);
// Spawn a listening port
boost::asio::spawn(ioc,
std::bind(
&do\_listen,
std::ref(ioc),
tcp::endpoint{address, port},
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
// Run the I/O service on the requested number of threads
std::vector v;
v.reserve(threads - 1);
for(auto i = threads - 1; i > 0; --i)
v.emplace\_back(
[&ioc]
{
ioc.run();
});
ioc.run();
return EXIT\_SUCCESS;
}