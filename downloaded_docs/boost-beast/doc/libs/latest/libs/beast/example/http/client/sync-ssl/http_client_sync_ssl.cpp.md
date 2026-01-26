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
// Example: HTTP SSL client, synchronous
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
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace net = boost::asio; // from 
namespace ssl = net::ssl; // from 
using tcp = net::ip::tcp; // from 
// Performs an HTTP GET and prints the response
int main(int argc, char\*\* argv)
{
try
{
// Check command line arguments.
if(argc != 4 && argc != 5)
{
std::cerr <<
"Usage: http-client-sync-ssl    []\n" <<
"Example:\n" <<
" http-client-sync-ssl www.example.com 443 /\n" <<
" http-client-sync-ssl www.example.com 443 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
int version = argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// The SSL context is required, and holds certificates
ssl::context ctx(ssl::context::tlsv12\_client);
// This holds the root certificate used for verification
load\_root\_certificates(ctx);
// Verify the remote server's certificate
ctx.set\_verify\_mode(ssl::verify\_peer);
// These objects perform our I/O
tcp::resolver resolver(ioc);
ssl::stream stream(ioc, ctx);
// Set SNI Hostname (many hosts need this to handshake successfully)
if(! SSL\_set\_tlsext\_host\_name(stream.native\_handle(), host))
{
throw beast::system\_error(
static\_cast(::ERR\_get\_error()),
net::error::get\_ssl\_category());
}
// Set the expected hostname in the peer certificate for verification
stream.set\_verify\_callback(ssl::host\_name\_verification(host));
// Look up the domain name
auto const results = resolver.resolve(host, port);
// Make the connection on the IP address we get from a lookup
beast::get\_lowest\_layer(stream).connect(results);
// Perform the SSL handshake
stream.handshake(ssl::stream\_base::client);
// Set up an HTTP GET request message
http::request req{http::verb::get, target, version};
req.set(http::field::host, host);
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// Send the HTTP request to the remote host
http::write(stream, req);
// This buffer is used for reading and must be persisted
beast::flat\_buffer buffer;
// Declare a container to hold the response
http::response res;
// Receive the HTTP response
http::read(stream, buffer, res);
// Write the message to standard out
std::cout << res << std::endl;
// Gracefully close the stream
beast::error\_code ec;
stream.shutdown(ec);
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
if(ec != net::ssl::error::stream\_truncated)
throw beast::system\_error{ec};
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
return EXIT\_SUCCESS;
}