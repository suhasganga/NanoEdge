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
// Example: WebSocket SSL server, synchronous
//
//------------------------------------------------------------------------------
#include "example/common/server\_certificate.hpp"
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
namespace ssl = boost::asio::ssl; // from 
using tcp = boost::asio::ip::tcp; // from 
//------------------------------------------------------------------------------
// Echoes back all received WebSocket messages
void
do\_session(tcp::socket socket, ssl::context& ctx)
{
try
{
// Construct the websocket stream around the socket
websocket::stream> ws{socket, ctx};
// Perform the SSL handshake
ws.next\_layer().handshake(ssl::stream\_base::server);
// Set a decorator to change the Server of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-server-sync-ssl");
}));
// Accept the websocket handshake
ws.accept();
for(;;)
{
// This buffer will hold the incoming message
beast::flat\_buffer buffer;
// Read a message
ws.read(buffer);
// Echo the message back
ws.text(ws.got\_text());
ws.write(buffer.data());
}
}
catch(beast::system\_error const& se)
{
// This indicates that the session was closed
if(se.code() != websocket::error::closed)
std::cerr << "Error: " << se.code().message() << std::endl;
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
}
}
//------------------------------------------------------------------------------
int main(int argc, char\* argv[])
{
try
{
// Check command line arguments.
if (argc != 3)
{
std::cerr <<
"Usage: websocket-server-sync-ssl  \n" <<
"Example:\n" <<
" websocket-server-sync-ssl 0.0.0.0 8080\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
// The io\_context is required for all I/O
net::io\_context ioc{1};
// The SSL context is required, and holds certificates
ssl::context ctx{ssl::context::tlsv12};
// This holds the self-signed certificate used by the server
load\_server\_certificate(ctx);
// The acceptor receives incoming connections
tcp::acceptor acceptor{ioc, {address, port}};
for(;;)
{
// This will receive the new connection
tcp::socket socket{ioc};
// Block until we get a connection
acceptor.accept(socket);
// Launch the session, transferring ownership of the socket
std::thread(
&do\_session,
std::move(socket),
std::ref(ctx)).detach();
}
}
catch (const std::exception& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
}