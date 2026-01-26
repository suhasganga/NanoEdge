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
#if defined(BOOST\_ASIO\_HAS\_CO\_AWAIT)
namespace beast = boost::beast;
namespace http = beast::http;
namespace websocket = beast::websocket;
namespace net = boost::asio;
// Echoes back all received WebSocket messages
net::awaitable
do\_session(websocket::stream stream)
{
// Set suggested timeout settings for the websocket
stream.set\_option(
websocket::stream\_base::timeout::suggested(beast::role\_type::server));
// Set a decorator to change the Server of the handshake
stream.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(
http::field::server,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-server-coro");
}));
// Accept the websocket handshake
co\_await stream.async\_accept();
for(;;)
{
// This buffer will hold the incoming message
beast::flat\_buffer buffer;
// Read a message
auto [ec, \_] = co\_await stream.async\_read(buffer, net::as\_tuple);
if(ec == websocket::error::closed)
co\_return;
if(ec)
throw boost::system::system\_error{ ec };
// Echo the message back
stream.text(stream.got\_text());
co\_await stream.async\_write(buffer.data());
}
}
// Accepts incoming connections and launches the sessions
net::awaitable
do\_listen(net::ip::tcp::endpoint endpoint)
{
auto executor = co\_await net::this\_coro::executor;
auto acceptor = net::ip::tcp::acceptor{ executor, endpoint };
for(;;)
{
net::co\_spawn(
executor,
do\_session(websocket::stream{
co\_await acceptor.async\_accept() }),
[](std::exception\_ptr e)
{
if(e)
{
try
{
std::rethrow\_exception(e);
}
catch(std::exception& e)
{
std::cerr << "Error in session: " << e.what() << "\n";
}
}
});
}
}
int
main(int argc, char\* argv[])
{
// Check command line arguments.
if(argc != 4)
{
std::cerr
<< "Usage: websocket-server-awaitable   \n"
<< "Example:\n"
<< " websocket-server-awaitable 0.0.0.0 8080 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const threads = std::max(1, std::atoi(argv[3]));
// The io\_context is required for all I/O
net::io\_context ioc(threads);
// Spawn a listening port
net::co\_spawn(
ioc,
do\_listen(net::ip::tcp::endpoint{ address, port }),
[](std::exception\_ptr e)
{
if(e)
{
try
{
std::rethrow\_exception(e);
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
}
}
});
// Run the I/O service on the requested number of threads
std::vector v;
v.reserve(threads - 1);
for(auto i = threads - 1; i > 0; --i)
v.emplace\_back([&ioc] { ioc.run(); });
ioc.run();
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