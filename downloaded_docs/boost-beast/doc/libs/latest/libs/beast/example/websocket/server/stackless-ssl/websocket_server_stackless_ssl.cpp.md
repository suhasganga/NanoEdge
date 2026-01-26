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
// Example: WebSocket SSL server, stackless coroutine
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
// Echoes back all received WebSocket messages
class session
: public boost::asio::coroutine
, public std::enable\_shared\_from\_this
{
websocket::stream> ws\_;
beast::flat\_buffer buffer\_;
public:
// Take ownership of the socket
session(tcp::socket&& socket, ssl::context& ctx)
: ws\_(std::move(socket), ctx)
{
}
// Start the asynchronous operation
void
run()
{
// We need to be executing within a strand to perform async operations
// on the I/O objects in this session. Although not strictly necessary
// for single-threaded contexts, this example code is written to be
// thread-safe by default.
net::dispatch(ws\_.get\_executor(),
beast::bind\_front\_handler(&session::loop,
shared\_from\_this(),
beast::error\_code{},
0));
}
#include 
void
loop(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
reenter(\*this)
{
// Set the timeout.
beast::get\_lowest\_layer(ws\_).expires\_after(std::chrono::seconds(30));
// Perform the SSL handshake
yield ws\_.next\_layer().async\_handshake(
ssl::stream\_base::server,
std::bind(
&session::loop,
shared\_from\_this(),
std::placeholders::\_1,
0));
if(ec)
return fail(ec, "handshake");
// Turn off the timeout on the tcp\_stream, because
// the websocket stream has its own timeout system.
beast::get\_lowest\_layer(ws\_).expires\_never();
// Set suggested timeout settings for the websocket
ws\_.set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::server));
// Set a decorator to change the Server of the handshake
ws\_.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" websocket-server-stackless-ssl");
}));
// Accept the websocket handshake
yield ws\_.async\_accept(
std::bind(
&session::loop,
shared\_from\_this(),
std::placeholders::\_1,
0));
if(ec)
return fail(ec, "accept");
for(;;)
{
// Read a message into our buffer
yield ws\_.async\_read(
buffer\_,
std::bind(
&session::loop,
shared\_from\_this(),
std::placeholders::\_1,
std::placeholders::\_2));
if(ec == websocket::error::closed)
{
// This indicates that the session was closed
return;
}
if(ec)
return fail(ec, "read");
// Echo the message
ws\_.text(ws\_.got\_text());
yield ws\_.async\_write(
buffer\_.data(),
std::bind(
&session::loop,
shared\_from\_this(),
std::placeholders::\_1,
std::placeholders::\_2));
if(ec)
return fail(ec, "write");
// Clear the buffer
buffer\_.consume(buffer\_.size());
}
}
}
#include 
};
//------------------------------------------------------------------------------
// Accepts incoming connections and launches the sessions
class listener
: public boost::asio::coroutine
, public std::enable\_shared\_from\_this
{
net::io\_context& ioc\_;
ssl::context& ctx\_;
tcp::acceptor acceptor\_;
tcp::socket socket\_;
public:
listener(
net::io\_context& ioc,
ssl::context& ctx,
tcp::endpoint endpoint)
: ioc\_(ioc)
, ctx\_(ctx)
, acceptor\_(ioc)
, socket\_(ioc)
{
beast::error\_code ec;
// Open the acceptor
acceptor\_.open(endpoint.protocol(), ec);
if(ec)
{
fail(ec, "open");
return;
}
// Allow address reuse
acceptor\_.set\_option(net::socket\_base::reuse\_address(true), ec);
if(ec)
{
fail(ec, "set\_option");
return;
}
// Bind to the server address
acceptor\_.bind(endpoint, ec);
if(ec)
{
fail(ec, "bind");
return;
}
// Start listening for connections
acceptor\_.listen(
net::socket\_base::max\_listen\_connections, ec);
if(ec)
{
fail(ec, "listen");
return;
}
}
// Start accepting incoming connections
void
run()
{
loop();
}
private:
#include 
void
loop(beast::error\_code ec = {})
{
reenter(\*this)
{
for(;;)
{
yield acceptor\_.async\_accept(
socket\_,
std::bind(
&listener::loop,
shared\_from\_this(),
std::placeholders::\_1));
if(ec)
{
fail(ec, "accept");
}
else
{
// Create the session and run it
std::make\_shared(std::move(socket\_), ctx\_)->run();
}
// Make sure each session gets its own strand
socket\_ = tcp::socket(net::make\_strand(ioc\_));
}
}
}
#include 
};
//------------------------------------------------------------------------------
int main(int argc, char\* argv[])
{
// Check command line arguments.
if (argc != 4)
{
std::cerr <<
"Usage: websocket-server-async-ssl   \n" <<
"Example:\n" <<
" websocket-server-async-ssl 0.0.0.0 8080 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const threads = std::max(1, std::atoi(argv[3]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// The SSL context is required, and holds certificates
ssl::context ctx{ssl::context::tlsv12};
// This holds the self-signed certificate used by the server
load\_server\_certificate(ctx);
// Create and launch a listening port
std::make\_shared(ioc, ctx, tcp::endpoint{address, port})->run();
// Run the I/O service on the requested number of threads
std::vector v;
v.reserve(threads - 1);
for(auto i = threads - 1; i > 0; --i)
v.emplace\_back(
[&ioc]
{
ioc.run();
});
ioc.run();
return EXIT\_SUCCESS;
}