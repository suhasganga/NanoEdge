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
// Example: WebSocket SSL client, synchronous
//
//------------------------------------------------------------------------------
#include "example/common/root\_certificates.hpp"
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
// Sends a WebSocket message and prints the response
int main(int argc, char\*\* argv)
{
try
{
// Check command line arguments.
if(argc != 4)
{
std::cerr <<
"Usage: websocket-client-sync-ssl   \n" <<
"Example:\n" <<
" websocket-client-sync-ssl echo.websocket.org 443 \"Hello, world!\"\n";
return EXIT\_FAILURE;
}
std::string host = argv[1];
auto const port = argv[2];
auto const text = argv[3];
// The io\_context is required for all I/O
net::io\_context ioc;
// The SSL context is required, and holds certificates
ssl::context ctx{ssl::context::tlsv12\_client};
// Verify the remote server's certificate
ctx.set\_verify\_mode(ssl::verify\_peer);
// This holds the root certificate used for verification
load\_root\_certificates(ctx);
// These objects perform our I/O
tcp::resolver resolver{ioc};
websocket::stream> ws{ioc, ctx};
// Look up the domain name
auto const results = resolver.resolve(host, port);
// Make the connection on the IP address we get from a lookup
auto ep = net::connect(beast::get\_lowest\_layer(ws), results);
// Set SNI Hostname (many hosts need this to handshake successfully)
if(! SSL\_set\_tlsext\_host\_name(ws.next\_layer().native\_handle(), host.c\_str()))
{
throw beast::system\_error(
static\_cast(::ERR\_get\_error()),
net::error::get\_ssl\_category());
}
// Set the expected hostname in the peer certificate for verification
ws.next\_layer().set\_verify\_callback(ssl::host\_name\_verification(host));
// Update the host\_ string. This will provide the value of the
// Host HTTP header during the WebSocket handshake.
// See https://tools.ietf.org/html/rfc7230#section-5.4
host += ':' + std::to\_string(ep.port());
// Perform the SSL handshake
ws.next\_layer().handshake(ssl::stream\_base::client);
// Set a decorator to change the User-Agent of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::request\_type& req)
{
req.set(http::field::user\_agent,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-client-coro");
}));
// Perform the websocket handshake
ws.handshake(host, "/");
// Send the message
ws.write(net::buffer(std::string(text)));
// This buffer will hold the incoming message
beast::flat\_buffer buffer;
// Read a message into our buffer
ws.read(buffer);
// Close the WebSocket connection
ws.close(websocket::close\_code::normal);
// If we get here then the connection is closed gracefully
// The make\_printable() function helps print a ConstBufferSequence
std::cout << beast::make\_printable(buffer.data()) << std::endl;
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
return EXIT\_SUCCESS;
}