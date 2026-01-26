//
// Copyright (c) 2016-2019 Vinnie Falco (vinnie dot falco at gmail dot com)
// Copyright (c) 2025 Mohammad Nejati
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE\_1\_0.txt or copy at http://www.boost.org/LICENSE\_1\_0.txt)
//
// Official repository: https://github.com/boostorg/beast
//
//------------------------------------------------------------------------------
//
// Example: WebSocket client, asynchronous Unix domain sockets
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
#if defined(BOOST\_ASIO\_HAS\_LOCAL\_SOCKETS)
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace websocket = beast::websocket; // from 
namespace net = boost::asio; // from 
using stream\_protocol = net::local::stream\_protocol; // from 
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
websocket::stream ws\_;
beast::flat\_buffer buffer\_;
std::string host\_;
std::string text\_;
public:
// Resolver and socket require an io\_context
explicit
session(net::io\_context& ioc)
: ws\_(net::make\_strand(ioc))
{
}
// Start the asynchronous operation
void
run(
char const\* path,
char const\* host,
char const\* port,
char const\* text)
{
// Save for later
host\_ = std::string{host} + ":" + port;
text\_ = text;
// Make the connection
beast::get\_lowest\_layer(ws\_).async\_connect(
stream\_protocol::endpoint{path},
beast::bind\_front\_handler(
&session::on\_connect,
shared\_from\_this()));
}
void
on\_connect(beast::error\_code ec)
{
if(ec)
return fail(ec, "connect");
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
" websocket-client-async-local");
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
if(argc != 5)
{
std::cerr <<
"Usage: websocket-client-async-local    \n" <<
"Example:\n" <<
" websocket-client-async-local /tmp/ws.sock localhost 80 \"Hello, world!\"\n";
return EXIT\_FAILURE;
}
auto const path = argv[1];
auto const host = argv[2];
auto const port = argv[3];
auto const text = argv[4];
// The io\_context is required for all I/O
net::io\_context ioc;
// Launch the asynchronous operation
std::make\_shared(ioc)->run(path, host, port, text);
// Run the I/O service. The call will return when
// the socket is closed.
ioc.run();
return EXIT\_SUCCESS;
}
#else
int
main(int, char\*[])
{
std::cerr <<
"Local sockets not available on this platform" << std::endl;
return EXIT\_FAILURE;
}
#endif