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
// Example: Advanced server
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
// Return a reasonable mime type based on the extension of a file.
beast::string\_view
mime\_type(beast::string\_view path)
{
using beast::iequals;
auto const ext = [&path]
{
auto const pos = path.rfind(".");
if(pos == beast::string\_view::npos)
return beast::string\_view{};
return path.substr(pos);
}();
if(iequals(ext, ".htm")) return "text/html";
if(iequals(ext, ".html")) return "text/html";
if(iequals(ext, ".php")) return "text/html";
if(iequals(ext, ".css")) return "text/css";
if(iequals(ext, ".txt")) return "text/plain";
if(iequals(ext, ".js")) return "application/javascript";
if(iequals(ext, ".json")) return "application/json";
if(iequals(ext, ".xml")) return "application/xml";
if(iequals(ext, ".swf")) return "application/x-shockwave-flash";
if(iequals(ext, ".flv")) return "video/x-flv";
if(iequals(ext, ".png")) return "image/png";
if(iequals(ext, ".jpe")) return "image/jpeg";
if(iequals(ext, ".jpeg")) return "image/jpeg";
if(iequals(ext, ".jpg")) return "image/jpeg";
if(iequals(ext, ".gif")) return "image/gif";
if(iequals(ext, ".bmp")) return "image/bmp";
if(iequals(ext, ".ico")) return "image/vnd.microsoft.icon";
if(iequals(ext, ".tiff")) return "image/tiff";
if(iequals(ext, ".tif")) return "image/tiff";
if(iequals(ext, ".svg")) return "image/svg+xml";
if(iequals(ext, ".svgz")) return "image/svg+xml";
return "application/text";
}
// Append an HTTP rel-path to a local filesystem path.
// The returned path is normalized for the platform.
std::string
path\_cat(
beast::string\_view base,
beast::string\_view path)
{
if(base.empty())
return std::string(path);
std::string result(base);
#ifdef BOOST\_MSVC
char constexpr path\_separator = '\\';
if(result.back() == path\_separator)
result.resize(result.size() - 1);
result.append(path.data(), path.size());
for(auto& c : result)
if(c == '/')
c = path\_separator;
#else
char constexpr path\_separator = '/';
if(result.back() == path\_separator)
result.resize(result.size() - 1);
result.append(path.data(), path.size());
#endif
return result;
}
// Return a response for the given request.
//
// The concrete type of the response message (which depends on the
// request), is type-erased in message\_generator.
template 
http::message\_generator
handle\_request(
beast::string\_view doc\_root,
http::request>&& req)
{
// Returns a bad request response
auto const bad\_request =
[&req](beast::string\_view why)
{
http::response res{http::status::bad\_request, req.version()};
res.set(http::field::server, BOOST\_BEAST\_VERSION\_STRING);
res.set(http::field::content\_type, "text/html");
res.keep\_alive(req.keep\_alive());
res.body() = std::string(why);
res.prepare\_payload();
return res;
};
// Returns a not found response
auto const not\_found =
[&req](beast::string\_view target)
{
http::response res{http::status::not\_found, req.version()};
res.set(http::field::server, BOOST\_BEAST\_VERSION\_STRING);
res.set(http::field::content\_type, "text/html");
res.keep\_alive(req.keep\_alive());
res.body() = "The resource '" + std::string(target) + "' was not found.";
res.prepare\_payload();
return res;
};
// Returns a server error response
auto const server\_error =
[&req](beast::string\_view what)
{
http::response res{http::status::internal\_server\_error, req.version()};
res.set(http::field::server, BOOST\_BEAST\_VERSION\_STRING);
res.set(http::field::content\_type, "text/html");
res.keep\_alive(req.keep\_alive());
res.body() = "An error occurred: '" + std::string(what) + "'";
res.prepare\_payload();
return res;
};
// Make sure we can handle the method
if( req.method() != http::verb::get &&
req.method() != http::verb::head)
return bad\_request("Unknown HTTP-method");
// Request path must be absolute and not contain "..".
if( req.target().empty() ||
req.target()[0] != '/' ||
req.target().find("..") != beast::string\_view::npos)
return bad\_request("Illegal request-target");
// Build the path to the requested file
std::string path = path\_cat(doc\_root, req.target());
if(req.target().back() == '/')
path.append("index.html");
// Attempt to open the file
beast::error\_code ec;
http::file\_body::value\_type body;
body.open(path.c\_str(), beast::file\_mode::scan, ec);
// Handle the case where the file doesn't exist
if(ec == beast::errc::no\_such\_file\_or\_directory)
return not\_found(req.target());
// Handle an unknown error
if(ec)
return server\_error(ec.message());
// Cache the size since we need it after the move
auto const size = body.size();
// Respond to HEAD request
if(req.method() == http::verb::head)
{
http::response res{http::status::ok, req.version()};
res.set(http::field::server, BOOST\_BEAST\_VERSION\_STRING);
res.set(http::field::content\_type, mime\_type(path));
res.content\_length(size);
res.keep\_alive(req.keep\_alive());
return res;
}
// Respond to GET request
http::response res{
std::piecewise\_construct,
std::make\_tuple(std::move(body)),
std::make\_tuple(http::status::ok, req.version())};
res.set(http::field::server, BOOST\_BEAST\_VERSION\_STRING);
res.set(http::field::content\_type, mime\_type(path));
res.content\_length(size);
res.keep\_alive(req.keep\_alive());
return res;
}
//------------------------------------------------------------------------------
// Report a failure
void
fail(beast::error\_code ec, char const\* what)
{
std::cerr << what << ": " << ec.message() << "\n";
}
// Echoes back all received WebSocket messages
class websocket\_session : public std::enable\_shared\_from\_this
{
websocket::stream ws\_;
beast::flat\_buffer buffer\_;
public:
// Take ownership of the socket
explicit
websocket\_session(tcp::socket&& socket)
: ws\_(std::move(socket))
{
}
// Start the asynchronous accept operation
template
void
do\_accept(http::request> req)
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
" advanced-server");
}));
// Accept the websocket handshake
ws\_.async\_accept(
req,
beast::bind\_front\_handler(
&websocket\_session::on\_accept,
shared\_from\_this()));
}
private:
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
&websocket\_session::on\_read,
shared\_from\_this()));
}
void
on\_read(
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
// This indicates that the websocket\_session was closed
if(ec == websocket::error::closed)
return;
if(ec)
return fail(ec, "read");
// Echo the message
ws\_.text(ws\_.got\_text());
ws\_.async\_write(
buffer\_.data(),
beast::bind\_front\_handler(
&websocket\_session::on\_write,
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
// Handles an HTTP server connection
class http\_session : public std::enable\_shared\_from\_this
{
beast::tcp\_stream stream\_;
beast::flat\_buffer buffer\_;
std::shared\_ptr doc\_root\_;
static constexpr std::size\_t queue\_limit = 8; // max responses
std::queue response\_queue\_;
// The parser is stored in an optional container so we can
// construct it from scratch it at the beginning of each new message.
boost::optional> parser\_;
public:
// Take ownership of the socket
http\_session(
tcp::socket&& socket,
std::shared\_ptr const& doc\_root)
: stream\_(std::move(socket))
, doc\_root\_(doc\_root)
{
static\_assert(queue\_limit > 0,
"queue limit must be positive");
}
// Start the session
void
run()
{
// We need to be executing within a strand to perform async operations
// on the I/O objects in this session. Although not strictly necessary
// for single-threaded contexts, this example code is written to be
// thread-safe by default.
net::dispatch(
stream\_.get\_executor(),
beast::bind\_front\_handler(
&http\_session::do\_read,
this->shared\_from\_this()));
}
private:
void
do\_read()
{
// Construct a new parser for each message
parser\_.emplace();
// Apply a reasonable limit to the allowed size
// of the body in bytes to prevent abuse.
parser\_->body\_limit(10000);
// Set the timeout.
stream\_.expires\_after(std::chrono::seconds(30));
// Read a request using the parser-oriented interface
http::async\_read(
stream\_,
buffer\_,
\*parser\_,
beast::bind\_front\_handler(
&http\_session::on\_read,
shared\_from\_this()));
}
void
on\_read(beast::error\_code ec, std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
// This means they closed the connection
if(ec == http::error::end\_of\_stream)
return do\_close();
if(ec)
return fail(ec, "read");
// See if it is a WebSocket Upgrade
if(websocket::is\_upgrade(parser\_->get()))
{
// Create a websocket session, transferring ownership
// of both the socket and the HTTP request.
std::make\_shared(
stream\_.release\_socket())->do\_accept(parser\_->release());
return;
}
// Send the response
queue\_write(handle\_request(\*doc\_root\_, parser\_->release()));
// If we aren't at the queue limit, try to pipeline another request
if (response\_queue\_.size() < queue\_limit)
do\_read();
}
void
queue\_write(http::message\_generator response)
{
// Allocate and store the work
response\_queue\_.push(std::move(response));
// If there was no previous work, start the write loop
if (response\_queue\_.size() == 1)
do\_write();
}
// Called to start/continue the write-loop. Should not be called when
// write\_loop is already active.
void
do\_write()
{
if(! response\_queue\_.empty())
{
bool keep\_alive = response\_queue\_.front().keep\_alive();
beast::async\_write(
stream\_,
std::move(response\_queue\_.front()),
beast::bind\_front\_handler(
&http\_session::on\_write,
shared\_from\_this(),
keep\_alive));
}
}
void
on\_write(
bool keep\_alive,
beast::error\_code ec,
std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
if(ec)
return fail(ec, "write");
if(! keep\_alive)
{
// This means we should close the connection, usually because
// the response indicated the "Connection: close" semantic.
return do\_close();
}
// Resume the read if it has been paused
if(response\_queue\_.size() == queue\_limit)
do\_read();
response\_queue\_.pop();
do\_write();
}
void
do\_close()
{
// Send a TCP shutdown
beast::error\_code ec;
stream\_.socket().shutdown(tcp::socket::shutdown\_send, ec);
// At this point the connection is closed gracefully
}
};
//------------------------------------------------------------------------------
// Accepts incoming connections and launches the sessions
class listener : public std::enable\_shared\_from\_this
{
net::io\_context& ioc\_;
tcp::acceptor acceptor\_;
std::shared\_ptr doc\_root\_;
public:
listener(
net::io\_context& ioc,
tcp::endpoint endpoint,
std::shared\_ptr const& doc\_root)
: ioc\_(ioc)
, acceptor\_(net::make\_strand(ioc))
, doc\_root\_(doc\_root)
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
// We need to be executing within a strand to perform async operations
// on the I/O objects in this session. Although not strictly necessary
// for single-threaded contexts, this example code is written to be
// thread-safe by default.
net::dispatch(
acceptor\_.get\_executor(),
beast::bind\_front\_handler(
&listener::do\_accept,
this->shared\_from\_this()));
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
// Create the http session and run it
std::make\_shared(
std::move(socket),
doc\_root\_)->run();
}
// Accept another connection
do\_accept();
}
};
//------------------------------------------------------------------------------
int main(int argc, char\* argv[])
{
// Check command line arguments.
if (argc != 5)
{
std::cerr <<
"Usage: advanced-server    \n" <<
"Example:\n" <<
" advanced-server 0.0.0.0 8080 . 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const doc\_root = std::make\_shared(argv[3]);
auto const threads = std::max(1, std::atoi(argv[4]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// Create and launch a listening port
std::make\_shared(
ioc,
tcp::endpoint{address, port},
doc\_root)->run();
// Capture SIGINT and SIGTERM to perform a clean shutdown
net::signal\_set signals(ioc, SIGINT, SIGTERM);
signals.async\_wait(
[&](beast::error\_code const&, int)
{
// Stop the `io\_context`. This will cause `run()`
// to return immediately, eventually destroying the
// `io\_context` and all of the sockets in it.
ioc.stop();
});
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
// (If we get here, it means we got a SIGINT or SIGTERM)
// Block until all the threads exit
for(auto& t : v)
t.join();
return EXIT\_SUCCESS;
}