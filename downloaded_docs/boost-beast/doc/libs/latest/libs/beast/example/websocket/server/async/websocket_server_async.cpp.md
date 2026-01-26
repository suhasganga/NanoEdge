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
// Example: WebSocket server, asynchronous
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
#include 
#include 
#include 
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace websocket = beast::websocket; // from 
namespace net = boost::asio; // from 
using tcp = boost::asio::ip::tcp; // from 
//------------------------------------------------------------------------------
// Report a failure
void
fail(beast::error\_code ec, char const\* what)
{
std::cerr << what << ": " << ec.message() << "\n";
}
// Echoes back all received WebSocket messages
class session : public std::enable\_shared\_from\_this
{
websocket::stream ws\_;
beast::flat\_buffer buffer\_;
public:
// Take ownership of the socket
explicit
session(tcp::socket&& socket)
: ws\_(std::move(socket))
{
}
// Get on the correct executor
void
run()
{
// We need to be executing within a strand to perform async operations
// on the I/O objects in this session. Although not strictly necessary
// for single-threaded contexts, this example code is written to be
// thread-safe by default.
net::dispatch(ws\_.get\_executor(),
beast::bind\_front\_handler(
&session::on\_run,
shared\_from\_this()));
}
// Start the asynchronous operation
void
on\_run()
{
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
" websocket-server-async");
}));
// Accept the websocket handshake
ws\_.async\_accept(
beast::bind\_front\_handler(
&session::on\_accept,
shared\_from\_this()));
}
void
on\_accept(beast::error\_code ec)
{
if(ec)
return fail(ec, "accept");
// Read a message
do\_read();
}
void
do\_read()
{
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
// This indicates that the session was closed
if(ec == websocket::error::closed)
return;
if(ec)
return fail(ec, "read");
// Echo the message
ws\_.text(ws\_.got\_text());
ws\_.async\_write(
buffer\_.data(),
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
// Clear the buffer
buffer\_.consume(buffer\_.size());
// Do another read
do\_read();
}
};
//------------------------------------------------------------------------------
// Accepts incoming connections and launches the sessions
class listener : public std::enable\_shared\_from\_this
{
net::io\_context& ioc\_;
tcp::acceptor acceptor\_;
public:
listener(
net::io\_context& ioc,
tcp::endpoint endpoint)
: ioc\_(ioc)
, acceptor\_(ioc)
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
do\_accept();
}
private:
void
do\_accept()
{
// The new connection gets its own strand
acceptor\_.async\_accept(
net::make\_strand(ioc\_),
beast::bind\_front\_handler(
&listener::on\_accept,
shared\_from\_this()));
}
void
on\_accept(beast::error\_code ec, tcp::socket socket)
{
if(ec)
{
fail(ec, "accept");
}
else
{
// Create the session and run it
std::make\_shared(std::move(socket))->run();
}
// Accept another connection
do\_accept();
}
};
//------------------------------------------------------------------------------
int main(int argc, char\* argv[])
{
// Check command line arguments.
if (argc != 4)
{
std::cerr <<
"Usage: websocket-server-async   \n" <<
"Example:\n" <<
" websocket-server-async 0.0.0.0 8080 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const threads = std::max(1, std::atoi(argv[3]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// Create and launch a listening port
std::make\_shared(ioc, tcp::endpoint{address, port})->run();
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