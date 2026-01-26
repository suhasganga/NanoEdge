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
// Example: WebSocket SSL client, asynchronous
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
//------------------------------------------------------------------------------
// Report a failure
void
fail(beast::error\_code ec, char const\* what)
{
std::cerr << what << ": " << ec.message() << "\n";
}
// Sends a WebSocket message and prints the response
class session : public std::enable\_shared\_from\_this
{
tcp::resolver resolver\_;
websocket::stream> ws\_;
beast::flat\_buffer buffer\_;
std::string host\_;
std::string text\_;
public:
// Resolver and socket require an io\_context
explicit
session(net::io\_context& ioc, ssl::context& ctx)
: resolver\_(net::make\_strand(ioc))
, ws\_(net::make\_strand(ioc), ctx)
{
}
// Start the asynchronous operation
void
run(
char const\* host,
char const\* port,
char const\* text)
{
// Set SNI Hostname (many hosts need this to handshake successfully)
if(! SSL\_set\_tlsext\_host\_name(ws\_.next\_layer().native\_handle(), host))
{
beast::error\_code ec{
static\_cast(::ERR\_get\_error()),
net::error::get\_ssl\_category()};
std::cerr << ec.message() << "\n";
return;
}
// Set the expected hostname in the peer certificate for verification
ws\_.next\_layer().set\_verify\_callback(ssl::host\_name\_verification(host));
// Save these for later
host\_ = host;
text\_ = text;
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
beast::get\_lowest\_layer(ws\_).expires\_after(std::chrono::seconds(30));
// Make the connection on the IP address we get from a lookup
beast::get\_lowest\_layer(ws\_).async\_connect(
results,
beast::bind\_front\_handler(
&session::on\_connect,
shared\_from\_this()));
}
void
on\_connect(beast::error\_code ec, tcp::resolver::results\_type::endpoint\_type ep)
{
if(ec)
return fail(ec, "connect");
// Set a timeout on the operation
beast::get\_lowest\_layer(ws\_).expires\_after(std::chrono::seconds(30));
// Update the host\_ string. This will provide the value of the
// Host HTTP header during the WebSocket handshake.
// See https://tools.ietf.org/html/rfc7230#section-5.4
host\_ += ':' + std::to\_string(ep.port());
// Perform the SSL handshake
ws\_.next\_layer().async\_handshake(
ssl::stream\_base::client,
beast::bind\_front\_handler(
&session::on\_ssl\_handshake,
shared\_from\_this()));
}
void
on\_ssl\_handshake(beast::error\_code ec)
{
if(ec)
return fail(ec, "ssl\_handshake");
// Turn off the timeout on the tcp\_stream, because
// the websocket stream has its own timeout system.
beast::get\_lowest\_layer(ws\_).expires\_never();
// Set suggested timeout settings for the websocket
ws\_.set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::client));
// Set a decorator to change the User-Agent of the handshake
ws\_.set\_option(websocket::stream\_base::decorator(
[](websocket::request\_type& req)
{
req.set(http::field::user\_agent,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-client-async-ssl");
}));
// Perform the websocket handshake
ws\_.async\_handshake(host\_, "/",
beast::bind\_front\_handler(
&session::on\_handshake,
shared\_from\_this()));
}
void
on\_handshake(beast::error\_code ec)
{
if(ec)
return fail(ec, "handshake");
// Send the message
ws\_.async\_write(
net::buffer(text\_),
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
// Read a message into our buffer
ws\_.async\_read(
buffer\_,
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
// Close the WebSocket connection
ws\_.async\_close(websocket::close\_code::normal,
beast::bind\_front\_handler(
&session::on\_close,
shared\_from\_this()));
}
void
on\_close(beast::error\_code ec)
{
if(ec)
return fail(ec, "close");
// If we get here then the connection is closed gracefully
// The make\_printable() function helps print a ConstBufferSequence
std::cout << beast::make\_printable(buffer\_.data()) << std::endl;
}
};
//------------------------------------------------------------------------------
int main(int argc, char\*\* argv)
{
// Check command line arguments.
if(argc != 4)
{
std::cerr <<
"Usage: websocket-client-async-ssl   \n" <<
"Example:\n" <<
" websocket-client-async-ssl echo.websocket.org 443 \"Hello, world!\"\n";
return EXIT\_FAILURE;
}
auto const host = argv[1];
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
// Launch the asynchronous operation
std::make\_shared(ioc, ctx)->run(host, port, text);
// Run the I/O service. The call will return when
// the socket is closed.
ioc.run();
return EXIT\_SUCCESS;
}