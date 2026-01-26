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
// Example: Advanced server, flex (plain + SSL)
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
if(ec == net::ssl::error::stream\_truncated)
return;
std::cerr << what << ": " << ec.message() << "\n";
}
//------------------------------------------------------------------------------
// Echoes back all received WebSocket messages.
// This uses the Curiously Recurring Template Pattern so that
// the same code works with both SSL streams and regular sockets.
template
class websocket\_session
{
// Access the derived class, this is part of
// the Curiously Recurring Template Pattern idiom.
Derived&
derived()
{
return static\_cast(\*this);
}
beast::flat\_buffer buffer\_;
// Start the asynchronous operation
template
void
do\_accept(http::request> req)
{
// Set suggested timeout settings for the websocket
derived().ws().set\_option(
websocket::stream\_base::timeout::suggested(
beast::role\_type::server));
// Set a decorator to change the Server of the handshake
derived().ws().set\_option(
websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(http::field::server,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" advanced-server-flex");
}));
// Accept the websocket handshake
derived().ws().async\_accept(
req,
beast::bind\_front\_handler(
&websocket\_session::on\_accept,
derived().shared\_from\_this()));
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
derived().ws().async\_read(
buffer\_,
beast::bind\_front\_handler(
&websocket\_session::on\_read,
derived().shared\_from\_this()));
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
derived().ws().text(derived().ws().got\_text());
derived().ws().async\_write(
buffer\_.data(),
beast::bind\_front\_handler(
&websocket\_session::on\_write,
derived().shared\_from\_this()));
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
public:
// Start the asynchronous operation
template
void
run(http::request> req)
{
// Accept the WebSocket upgrade request
do\_accept(std::move(req));
}
};
//------------------------------------------------------------------------------
// Handles a plain WebSocket connection
class plain\_websocket\_session
: public websocket\_session
, public std::enable\_shared\_from\_this
{
websocket::stream ws\_;
public:
// Create the session
explicit
plain\_websocket\_session(
beast::tcp\_stream&& stream)
: ws\_(std::move(stream))
{
}
// Called by the base class
websocket::stream&
ws()
{
return ws\_;
}
};
//------------------------------------------------------------------------------
// Handles an SSL WebSocket connection
class ssl\_websocket\_session
: public websocket\_session
, public std::enable\_shared\_from\_this
{
websocket::stream> ws\_;
public:
// Create the ssl\_websocket\_session
explicit
ssl\_websocket\_session(ssl::stream&& stream)
: ws\_(std::move(stream))
{
}
// Called by the base class
websocket::stream>&
ws()
{
return ws\_;
}
};
//------------------------------------------------------------------------------
template
void
make\_websocket\_session(
beast::tcp\_stream stream,
http::request> req)
{
std::make\_shared(
std::move(stream))->run(std::move(req));
}
template
void
make\_websocket\_session(
ssl::stream stream,
http::request> req)
{
std::make\_shared(
std::move(stream))->run(std::move(req));
}
//------------------------------------------------------------------------------
// Handles an HTTP server connection.
// This uses the Curiously Recurring Template Pattern so that
// the same code works with both SSL streams and regular sockets.
template
class http\_session
{
std::shared\_ptr doc\_root\_;
// Access the derived class, this is part of
// the Curiously Recurring Template Pattern idiom.
Derived&
derived()
{
return static\_cast(\*this);
}
static constexpr std::size\_t queue\_limit = 8; // max responses
std::queue response\_queue\_;
// The parser is stored in an optional container so we can
// construct it from scratch it at the beginning of each new message.
boost::optional> parser\_;
protected:
beast::flat\_buffer buffer\_;
public:
// Construct the session
http\_session(
beast::flat\_buffer buffer,
std::shared\_ptr const& doc\_root)
: doc\_root\_(doc\_root)
, buffer\_(std::move(buffer))
{
}
void
do\_read()
{
// Construct a new parser for each message
parser\_.emplace();
// Apply a reasonable limit to the allowed size
// of the body in bytes to prevent abuse.
parser\_->body\_limit(10000);
// Set the timeout.
beast::get\_lowest\_layer(
derived().stream()).expires\_after(std::chrono::seconds(30));
// Read a request using the parser-oriented interface
http::async\_read(
derived().stream(),
buffer\_,
\*parser\_,
beast::bind\_front\_handler(
&http\_session::on\_read,
derived().shared\_from\_this()));
}
void
on\_read(beast::error\_code ec, std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
// This means they closed the connection
if(ec == http::error::end\_of\_stream)
return derived().do\_eof();
if(ec)
return fail(ec, "read");
// See if it is a WebSocket Upgrade
if(websocket::is\_upgrade(parser\_->get()))
{
// Disable the timeout.
// The websocket::stream uses its own timeout settings.
beast::get\_lowest\_layer(derived().stream()).expires\_never();
// Create a websocket session, transferring ownership
// of both the socket and the HTTP request.
return make\_websocket\_session(
derived().release\_stream(),
parser\_->release());
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
derived().stream(),
std::move(response\_queue\_.front()),
beast::bind\_front\_handler(
&http\_session::on\_write,
derived().shared\_from\_this(),
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
return derived().do\_eof();
}
// Resume the read if it has been paused
if(response\_queue\_.size() == queue\_limit)
do\_read();
response\_queue\_.pop();
do\_write();
}
};
//------------------------------------------------------------------------------
// Handles a plain HTTP connection
class plain\_http\_session
: public http\_session
, public std::enable\_shared\_from\_this
{
beast::tcp\_stream stream\_;
public:
// Create the session
plain\_http\_session(
beast::tcp\_stream&& stream,
beast::flat\_buffer&& buffer,
std::shared\_ptr const& doc\_root)
: http\_session(
std::move(buffer),
doc\_root)
, stream\_(std::move(stream))
{
}
// Start the session
void
run()
{
this->do\_read();
}
// Called by the base class
beast::tcp\_stream&
stream()
{
return stream\_;
}
// Called by the base class
beast::tcp\_stream
release\_stream()
{
return std::move(stream\_);
}
// Called by the base class
void
do\_eof()
{
// Send a TCP shutdown
beast::error\_code ec;
stream\_.socket().shutdown(tcp::socket::shutdown\_send, ec);
// At this point the connection is closed gracefully
}
};
//------------------------------------------------------------------------------
// Handles an SSL HTTP connection
class ssl\_http\_session
: public http\_session
, public std::enable\_shared\_from\_this
{
ssl::stream stream\_;
public:
// Create the http\_session
ssl\_http\_session(
beast::tcp\_stream&& stream,
ssl::context& ctx,
beast::flat\_buffer&& buffer,
std::shared\_ptr const& doc\_root)
: http\_session(
std::move(buffer),
doc\_root)
, stream\_(std::move(stream), ctx)
{
}
// Start the session
void
run()
{
// Set the timeout.
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Perform the SSL handshake
// Note, this is the buffered version of the handshake.
stream\_.async\_handshake(
ssl::stream\_base::server,
buffer\_.data(),
beast::bind\_front\_handler(
&ssl\_http\_session::on\_handshake,
shared\_from\_this()));
}
// Called by the base class
ssl::stream&
stream()
{
return stream\_;
}
// Called by the base class
ssl::stream
release\_stream()
{
return std::move(stream\_);
}
// Called by the base class
void
do\_eof()
{
// Set the timeout.
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Perform the SSL shutdown
stream\_.async\_shutdown(
beast::bind\_front\_handler(
&ssl\_http\_session::on\_shutdown,
shared\_from\_this()));
}
private:
void
on\_handshake(
beast::error\_code ec,
std::size\_t bytes\_used)
{
if(ec)
return fail(ec, "handshake");
// Consume the portion of the buffer used by the handshake
buffer\_.consume(bytes\_used);
do\_read();
}
void
on\_shutdown(beast::error\_code ec)
{
if(ec)
return fail(ec, "shutdown");
// At this point the connection is closed gracefully
}
};
//------------------------------------------------------------------------------
// Detects SSL handshakes
class detect\_session : public std::enable\_shared\_from\_this
{
beast::tcp\_stream stream\_;
ssl::context& ctx\_;
std::shared\_ptr doc\_root\_;
beast::flat\_buffer buffer\_;
public:
explicit
detect\_session(
tcp::socket&& socket,
ssl::context& ctx,
std::shared\_ptr const& doc\_root)
: stream\_(std::move(socket))
, ctx\_(ctx)
, doc\_root\_(doc\_root)
{
}
// Launch the detector
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
&detect\_session::on\_run,
this->shared\_from\_this()));
}
void
on\_run()
{
// Set the timeout.
stream\_.expires\_after(std::chrono::seconds(30));
beast::async\_detect\_ssl(
stream\_,
buffer\_,
beast::bind\_front\_handler(
&detect\_session::on\_detect,
this->shared\_from\_this()));
}
void
on\_detect(beast::error\_code ec, bool result)
{
if(ec)
return fail(ec, "detect");
if(result)
{
// Launch SSL session
std::make\_shared(
std::move(stream\_),
ctx\_,
std::move(buffer\_),
doc\_root\_)->run();
return;
}
// Launch plain session
std::make\_shared(
std::move(stream\_),
std::move(buffer\_),
doc\_root\_)->run();
}
};
// Accepts incoming connections and launches the sessions
class listener : public std::enable\_shared\_from\_this
{
net::io\_context& ioc\_;
ssl::context& ctx\_;
tcp::acceptor acceptor\_;
std::shared\_ptr doc\_root\_;
public:
listener(
net::io\_context& ioc,
ssl::context& ctx,
tcp::endpoint endpoint,
std::shared\_ptr const& doc\_root)
: ioc\_(ioc)
, ctx\_(ctx)
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
// Create the detector http\_session and run it
std::make\_shared(
std::move(socket),
ctx\_,
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
"Usage: advanced-server-flex    \n" <<
"Example:\n" <<
" advanced-server-flex 0.0.0.0 8080 . 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const doc\_root = std::make\_shared(argv[3]);
auto const threads = std::max(1, std::atoi(argv[4]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// The SSL context is required, and holds certificates
ssl::context ctx{ssl::context::tlsv12};
// This holds the self-signed certificate used by the server
load\_server\_certificate(ctx);
// Create and launch a listening port
std::make\_shared(
ioc,
ctx,
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