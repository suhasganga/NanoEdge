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
// Example: HTTP client, synchronous
//
//------------------------------------------------------------------------------
//[example\_http\_client
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
"Usage: http-client-sync    []\n" <<
"Example:\n" <<
" http-client-sync www.example.com 80 /\n" <<
" http-client-sync www.example.com 80 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
int version = argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// These objects perform our I/O
tcp::resolver resolver(ioc);
beast::tcp\_stream stream(ioc);
// Look up the domain name
auto const results = resolver.resolve(host, port);
// Make the connection on the IP address we get from a lookup
stream.connect(results);
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
// Gracefully close the socket
beast::error\_code ec;
stream.socket().shutdown(tcp::socket::shutdown\_both, ec);
// not\_connected happens sometimes
// so don't bother reporting it.
//
if(ec && ec != beast::errc::not\_connected)
throw beast::system\_error{ec};
// If we get here then the connection is closed gracefully
}
catch(std::exception const& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
return EXIT\_SUCCESS;
}
//]