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
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace net = boost::asio; // from 
using tcp = boost::asio::ip::tcp; // from 
//------------------------------------------------------------------------------
// Report a failure
void
fail(beast::error\_code ec, char const\* what)
{
std::cerr << what << ": " << ec.message() << "\n";
}
// Performs an HTTP GET and prints the response
void
do\_session(
std::string const& host,
std::string const& port,
std::string const& target,
int version,
net::io\_context& ioc,
net::yield\_context yield)
{
beast::error\_code ec;
// These objects perform our I/O
tcp::resolver resolver(ioc);
beast::tcp\_stream stream(ioc);
// Look up the domain name
auto const results = resolver.async\_resolve(host, port, yield[ec]);
if(ec)
return fail(ec, "resolve");
// Set the timeout.
stream.expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
stream.async\_connect(results, yield[ec]);
if(ec)
return fail(ec, "connect");
// Set up an HTTP GET request message
http::request req{http::verb::get, target, version};
req.set(http::field::host, host);
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// Set the timeout.
stream.expires\_after(std::chrono::seconds(30));
// Send the HTTP request to the remote host
http::async\_write(stream, req, yield[ec]);
if(ec)
return fail(ec, "write");
// This buffer is used for reading and must be persisted
beast::flat\_buffer b;
// Declare a container to hold the response
http::response res;
// Receive the HTTP response
http::async\_read(stream, b, res, yield[ec]);
if(ec)
return fail(ec, "read");
// Write the message to standard out
std::cout << res << std::endl;
// Gracefully close the socket
stream.socket().shutdown(tcp::socket::shutdown\_both, ec);
// not\_connected happens sometimes
// so don't bother reporting it.
//
if(ec && ec != beast::errc::not\_connected)
return fail(ec, "shutdown");
// If we get here then the connection is closed gracefully
}
//------------------------------------------------------------------------------
int main(int argc, char\*\* argv)
{
// Check command line arguments.
if(argc != 4 && argc != 5)
{
std::cerr <<
"Usage: http-client-coro    []\n" <<
"Example:\n" <<
" http-client-coro www.example.com 80 /\n" <<
" http-client-coro www.example.com 80 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
int version = argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// Launch the asynchronous operation
boost::asio::spawn(ioc, std::bind(
&do\_session,
std::string(host),
std::string(port),
std::string(target),
version,
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
// the get operation is complete.
ioc.run();
return EXIT\_SUCCESS;
}