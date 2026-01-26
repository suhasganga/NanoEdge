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
// Example: HTTP client, asynchronous
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
class session : public std::enable\_shared\_from\_this
{
tcp::resolver resolver\_;
beast::tcp\_stream stream\_;
beast::flat\_buffer buffer\_; // (Must persist between reads)
http::request req\_;
http::response res\_;
public:
// Objects are constructed with a strand to
// ensure that handlers do not execute concurrently.
explicit
session(net::io\_context& ioc)
: resolver\_(net::make\_strand(ioc))
, stream\_(net::make\_strand(ioc))
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
stream\_.expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
stream\_.async\_connect(
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
// Set a timeout on the operation
stream\_.expires\_after(std::chrono::seconds(30));
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
// Gracefully close the socket
stream\_.socket().shutdown(tcp::socket::shutdown\_both, ec);
// not\_connected happens sometimes so don't bother reporting it.
if(ec && ec != beast::errc::not\_connected)
return fail(ec, "shutdown");
// If we get here then the connection is closed gracefully
}
};
//------------------------------------------------------------------------------
int main(int argc, char\*\* argv)
{
// Check command line arguments.
if(argc != 4 && argc != 5)
{
std::cerr <<
"Usage: http-client-async    []\n" <<
"Example:\n" <<
" http-client-async www.example.com 80 /\n" <<
" http-client-async www.example.com 80 / 1.0\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
auto const port = argv[2];
auto const target = argv[3];
int version = argc == 5 && !std::strcmp("1.0", argv[4]) ? 10 : 11;
// The io\_context is required for all I/O
net::io\_context ioc;
// Launch the asynchronous operation
std::make\_shared(ioc)->run(host, port, target, version);
// Run the I/O service. The call will return when
// the get operation is complete.
ioc.run();
return EXIT\_SUCCESS;
}