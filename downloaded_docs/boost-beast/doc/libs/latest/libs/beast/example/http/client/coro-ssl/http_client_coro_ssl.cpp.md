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
// Example: HTTP SSL client, coroutine
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
namespace net = boost::asio; // from 
namespace ssl = boost::asio::ssl; // from 
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
ssl::context& ctx,
net::yield\_context yield)
{
beast::error\_code ec;
// These objects perform our I/O
tcp::resolver resolver(ioc);
ssl::stream stream(ioc, ctx);
// Set SNI Hostname (many hosts need this to handshake successfully)
if(! SSL\_set\_tlsext\_host\_name(stream.native\_handle(), host.c\_str()))
{
ec.assign(static\_cast(::ERR\_get\_error()), net::error::get\_ssl\_category());
std::cerr << ec.message() << "\n";
return;
}
// Set the expected hostname in the peer certificate for verification
stream.set\_verify\_callback(ssl::host\_name\_verification(host));
// Look up the domain name
auto const results = resolver.async\_resolve(host, port, yield[ec]);
if(ec)
return fail(ec, "resolve");
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
get\_lowest\_layer(stream).async\_connect(results, yield[ec]);
if(ec)
return fail(ec, "connect");
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Perform the SSL handshake
stream.async\_handshake(ssl::stream\_base::client, yield[ec]);
if(ec)
return fail(ec, "handshake");
// Set up an HTTP GET request message
http::request req{http::verb::get, target, version};
req.set(http::field::host, host);
req.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
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
// Set the timeout.
beast::get\_lowest\_layer(stream).expires\_after(std::chrono::seconds(30));
// Gracefully close the stream
stream.async\_shutdown(yield[ec]);
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
return fail(ec, "shutdown");
}
//------------------------------------------------------------------------------
int main(int argc, char\*\* argv)
{
// Check command line arguments.
if(argc != 4 && argc != 5)
{
std::cerr <<
"Usage: http-client-coro-ssl    []\n" <<
"Example:\n" <<
" http-client-coro-ssl www.example.com 443 /\n" <<
" http-client-coro-ssl www.example.com 443 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
int version = argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// The SSL context is required, and holds certificates
ssl::context ctx{ssl::context::tlsv12\_client};
// This holds the root certificate used for verification
load\_root\_certificates(ctx);
// Verify the remote server's certificate
ctx.set\_verify\_mode(ssl::verify\_peer);
// Launch the asynchronous operation
boost::asio::spawn(ioc, std::bind(
&do\_session,
std::string(host),
std::string(port),
std::string(target),
version,
std::ref(ioc),
std::ref(ctx),
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