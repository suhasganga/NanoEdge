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
// Example: WebSocket server, fast
//
//------------------------------------------------------------------------------
/\* This server contains the following ports:
Synchronous 
Asynchronous 
Coroutine 
This program is optimized for the Autobahn|Testsuite
benchmarking and WebSocket compliants testing program.
See:
https://github.com/crossbario/autobahn-testsuite
\*/
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
using tcp = boost::asio::ip::tcp; // from 
//------------------------------------------------------------------------------
// Report a failure
void
fail(beast::error\_code ec, char const\* what)
{
std::cerr << (std::string(what) + ": " + ec.message() + "\n");
}
// Adjust settings on the stream
template
void
setup\_stream(websocket::stream& ws)
{
// These values are tuned for Autobahn|Testsuite, and
// should also be generally helpful for increased performance.
websocket::permessage\_deflate pmd;
pmd.client\_enable = true;
pmd.server\_enable = true;
pmd.compLevel = 3;
ws.set\_option(pmd);
ws.auto\_fragment(false);
// Autobahn|Testsuite needs this
ws.read\_message\_max(64 \* 1024 \* 1024);
}
//------------------------------------------------------------------------------
void
do\_sync\_session(websocket::stream& ws)
{
beast::error\_code ec;
setup\_stream(ws);
// Set a decorator to change the Server of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server, std::string(
BOOST\_BEAST\_VERSION\_STRING) + "-Sync");
}));
ws.accept(ec);
if(ec)
return fail(ec, "accept");
for(;;)
{
beast::flat\_buffer buffer;
ws.read(buffer, ec);
if(ec == websocket::error::closed)
break;
if(ec)
return fail(ec, "read");
ws.text(ws.got\_text());
ws.write(buffer.data(), ec);
if(ec)
return fail(ec, "write");
}
}
void
do\_sync\_listen(
net::io\_context& ioc,
tcp::endpoint endpoint)
{
beast::error\_code ec;
tcp::acceptor acceptor{ioc, endpoint};
for(;;)
{
tcp::socket socket{ioc};
acceptor.accept(socket, ec);
if(ec)
return fail(ec, "accept");
std::thread(std::bind(
&do\_sync\_session,
websocket::stream(
std::move(socket)))).detach();
}
}
//------------------------------------------------------------------------------
// Echoes back all received WebSocket messages
class async\_session : public std::enable\_shared\_from\_this
{
websocket::stream ws\_;
beast::flat\_buffer buffer\_;
public:
// Take ownership of the socket
explicit
async\_session(tcp::socket&& socket)
: ws\_(std::move(socket))
{
setup\_stream(ws\_);
}
// Start the asynchronous operation
void
run()
{
// Set suggested timeout settings for the websocket
ws\_.set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::server));
// Set a decorator to change the Server of the handshake
ws\_.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server, std::string(
BOOST\_BEAST\_VERSION\_STRING) + "-Async");
}));
// Accept the websocket handshake
ws\_.async\_accept(
beast::bind\_front\_handler(
&async\_session::on\_accept,
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
&async\_session::on\_read,
shared\_from\_this()));
}
void
on\_read(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
// This indicates that the async\_session was closed
if(ec == websocket::error::closed)
return;
if(ec)
return fail(ec, "read");
// Echo the message
ws\_.text(ws\_.got\_text());
ws\_.async\_write(
buffer\_.data(),
beast::bind\_front\_handler(
&async\_session::on\_write,
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
// Accepts incoming connections and launches the sessions
class async\_listener : public std::enable\_shared\_from\_this
{
net::io\_context& ioc\_;
tcp::acceptor acceptor\_;
public:
async\_listener(
net::io\_context& ioc,
tcp::endpoint endpoint)
: ioc\_(ioc)
, acceptor\_(net::make\_strand(ioc))
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
&async\_listener::on\_accept,
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
// Create the async\_session and run it
std::make\_shared(std::move(socket))->run();
}
// Accept another connection
do\_accept();
}
};
//------------------------------------------------------------------------------
void
do\_coro\_session(
websocket::stream& ws,
net::yield\_context yield)
{
beast::error\_code ec;
setup\_stream(ws);
// Set suggested timeout settings for the websocket
ws.set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::server));
// Set a decorator to change the Server of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server, std::string(
BOOST\_BEAST\_VERSION\_STRING) + "-Fiber");
}));
ws.async\_accept(yield[ec]);
if(ec)
return fail(ec, "accept");
for(;;)
{
beast::flat\_buffer buffer;
ws.async\_read(buffer, yield[ec]);
if(ec == websocket::error::closed)
break;
if(ec)
return fail(ec, "read");
ws.text(ws.got\_text());
ws.async\_write(buffer.data(), yield[ec]);
if(ec)
return fail(ec, "write");
}
}
void
do\_coro\_listen(
net::io\_context& ioc,
tcp::endpoint endpoint,
net::yield\_context yield)
{
beast::error\_code ec;
tcp::acceptor acceptor(ioc);
acceptor.open(endpoint.protocol(), ec);
if(ec)
return fail(ec, "open");
acceptor.set\_option(net::socket\_base::reuse\_address(true), ec);
if(ec)
return fail(ec, "set\_option");
acceptor.bind(endpoint, ec);
if(ec)
return fail(ec, "bind");
acceptor.listen(net::socket\_base::max\_listen\_connections, ec);
if(ec)
return fail(ec, "listen");
for(;;)
{
tcp::socket socket(ioc);
acceptor.async\_accept(socket, yield[ec]);
if(ec)
{
fail(ec, "accept");
continue;
}
boost::asio::spawn(
acceptor.get\_executor(),
std::bind(
&do\_coro\_session,
websocket::stream<
beast::tcp\_stream>(std::move(socket)),
std::placeholders::\_1), boost::asio::detached);
}
}
//------------------------------------------------------------------------------
int main(int argc, char\* argv[])
{
// Check command line arguments.
if (argc != 4)
{
std::cerr <<
"Usage: websocket-server-fast   \n" <<
"Example:\n"
" websocket-server-fast 0.0.0.0 8080 1\n"
" Connect to:\n"
" starting-port+0 for synchronous,\n"
" starting-port+1 for asynchronous,\n"
" starting-port+2 for coroutine.\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const threads = std::max(1, std::atoi(argv[3]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// Create sync port
std::thread(beast::bind\_front\_handler(
&do\_sync\_listen,
std::ref(ioc),
tcp::endpoint{
address,
static\_cast(port + 0u)}
)).detach();
// Create async port
std::make\_shared(
ioc,
tcp::endpoint{
address,
static\_cast(port + 1u)})->run();
// Create coro port
boost::asio::spawn(ioc,
std::bind(
&do\_coro\_listen,
std::ref(ioc),
tcp::endpoint{
address,
static\_cast(port + 2u)},
std::placeholders::\_1), boost::asio::detached);
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