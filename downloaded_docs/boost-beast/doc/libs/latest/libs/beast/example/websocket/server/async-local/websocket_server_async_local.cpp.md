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
// Example: WebSocket server, asynchronous Unix domain sockets
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
// Echoes back all received WebSocket messages
class session : public std::enable\_shared\_from\_this
{
websocket::stream ws\_;
beast::flat\_buffer buffer\_;
public:
// Take ownership of the socket
explicit
session(stream\_protocol::socket&& socket)
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
" websocket-server-async-local");
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
stream\_protocol::acceptor acceptor\_;
public:
listener(
net::io\_context& ioc,
stream\_protocol::endpoint endpoint)
: ioc\_(ioc)
, acceptor\_(ioc, std::move(endpoint))
{
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
on\_accept(beast::error\_code ec, stream\_protocol::socket socket)
{
if(ec)
{
fail(ec, "accept");
return;
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
try
{
// Check command line arguments.
if (argc != 3)
{
std::cerr <<
"Usage: websocket-server-async-local  \n" <<
"Example:\n" <<
" websocket-server-async-local /tmp/ws.sock 1\n";
return EXIT\_FAILURE;
}
auto const path = argv[1];
auto const threads = std::max(1, std::atoi(argv[2]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// Remove previous binding
std::remove(path);
// Create and launch a listening port
std::make\_shared(ioc, stream\_protocol::endpoint{path})->run();
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
catch(std::exception const& e)
{
std::cerr << e.what() << std::endl;
return EXIT\_FAILURE;
}
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