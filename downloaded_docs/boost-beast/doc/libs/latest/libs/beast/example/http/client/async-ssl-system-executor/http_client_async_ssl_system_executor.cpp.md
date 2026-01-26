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
// Example: HTTP SSL client, asynchronous, using system\_executor
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
class session : public std::enable\_shared\_from\_this
{
tcp::resolver resolver\_;
ssl::stream stream\_;
beast::flat\_buffer buffer\_; // (Must persist between reads)
http::request req\_;
http::response res\_;
// Objects are constructed with a strand to
// ensure that handlers do not execute concurrently.
session(net::strand strand, ssl::context& ctx)
: resolver\_(strand)
, stream\_(strand, ctx)
{
}
public:
// Delegate construction to a prive constructor to be able to use
// the same strand for both I/O object.
explicit
session(ssl::context& ctx)
: session(net::make\_strand(net::system\_executor()), ctx)
{
}
// Start the asynchronous operation
void
run(
char const\* host,
char const\* port,
char const\* target,
int version)
{
// Set SNI Hostname (many hosts need this to handshake successfully)
if(! SSL\_set\_tlsext\_host\_name(stream\_.native\_handle(), host))
{
beast::error\_code ec{
static\_cast(::ERR\_get\_error()),
net::error::get\_ssl\_category()};
std::cerr << ec.message() << "\n";
return;
}
// Set the expected hostname in the peer certificate for verification
stream\_.set\_verify\_callback(ssl::host\_name\_verification(host));
// Set up an HTTP GET request message
req\_.version(version);
req\_.method(http::verb::get);
req\_.target(target);
req\_.set(http::field::host, host);
req\_.set(http::field::user\_agent, BOOST\_BEAST\_VERSION\_STRING);
// Look up the domain name
resolver\_.async\_resolve(
host,
port,
beast::bind\_front\_handler(
&session::on\_resolve,
shared\_from\_this()));
}
void
on\_resolve(
beast::error\_code ec,
tcp::resolver::results\_type results)
{
if(ec)
return fail(ec, "resolve");
// Set a timeout on the operation
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
beast::get\_lowest\_layer(stream\_).async\_connect(
results,
beast::bind\_front\_handler(
&session::on\_connect,
shared\_from\_this()));
}
void
on\_connect(beast::error\_code ec, tcp::resolver::results\_type::endpoint\_type)
{
if(ec)
return fail(ec, "connect");
// Perform the SSL handshake
stream\_.async\_handshake(
ssl::stream\_base::client,
beast::bind\_front\_handler(
&session::on\_handshake,
shared\_from\_this()));
}
void
on\_handshake(beast::error\_code ec)
{
if(ec)
return fail(ec, "handshake");
// Set a timeout on the operation
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Send the HTTP request to the remote host
http::async\_write(stream\_, req\_,
beast::bind\_front\_handler(
&session::on\_write,
shared\_from\_this()));
}
void
on\_write(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
if(ec)
return fail(ec, "write");
// Receive the HTTP response
http::async\_read(stream\_, buffer\_, res\_,
beast::bind\_front\_handler(
&session::on\_read,
shared\_from\_this()));
}
void
on\_read(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
if(ec)
return fail(ec, "read");
// Write the message to standard out
std::cout << res\_ << std::endl;
// Set a timeout on the operation
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Gracefully close the stream
stream\_.async\_shutdown(
beast::bind\_front\_handler(
&session::on\_shutdown,
shared\_from\_this()));
}
void
on\_shutdown(beast::error\_code ec)
{
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
};
//------------------------------------------------------------------------------
int main(int argc, char\*\* argv)
{
// Check command line arguments.
if(argc != 4 && argc != 5)
{
std::cerr <<
"Usage: http-client-async-ssl-system-executor    []\n" <<
"Example:\n" <<
" http-client-async-ssl-system-executor www.example.com 443 /\n" <<
" http-client-async-ssl-system-executor www.example.com 443 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
int version = argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The SSL context is required, and holds certificates
ssl::context ctx{ssl::context::tlsv12\_client};
// This holds the root certificate used for verification
load\_root\_certificates(ctx);
// Verify the remote server's certificate
ctx.set\_verify\_mode(ssl::verify\_peer);
// Launch the asynchronous operation
std::make\_shared(ctx)->run(host, port, target, version);
// The async operations will run on the system\_executor.
// Because the main thread has nothing to do in this example, we just wait
// for the system\_executor to run out of work.
net::query(net::system\_executor(), net::execution::context).join();
return EXIT\_SUCCESS;
}