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
// Example: HTTP SSL server, stackless coroutine
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
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
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
// Handles an HTTP server connection
class session
: public boost::asio::coroutine
, public std::enable\_shared\_from\_this
{
ssl::stream stream\_;
beast::flat\_buffer buffer\_;
std::shared\_ptr doc\_root\_;
http::request req\_;
bool keep\_alive\_ = true;
public:
// Take ownership of the socket
explicit
session(
tcp::socket&& socket,
ssl::context& ctx,
std::shared\_ptr const& doc\_root)
: stream\_(std::move(socket), ctx)
, doc\_root\_(doc\_root)
{
}
// Start the asynchronous operation
void
run()
{
// We need to be executing within a strand to perform async operations
// on the I/O objects in this session.Although not strictly necessary
// for single-threaded contexts, this example code is written to be
// thread-safe by default.
net::dispatch(stream\_.get\_executor(),
beast::bind\_front\_handler(&session::loop,
shared\_from\_this(),
beast::error\_code{},
0));
}
#include 
void
loop(beast::error\_code ec, std::size\_t bytes\_transferred)
{
boost::ignore\_unused(bytes\_transferred);
reenter(\*this)
{
// Set the timeout.
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Perform the SSL handshake
yield stream\_.async\_handshake(
ssl::stream\_base::server,
std::bind(
&session::loop, shared\_from\_this(),
std::placeholders::\_1, 0));
if(ec)
return fail(ec, "handshake");
for(;;)
{
// Set the timeout.
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Make the request empty before reading,
// otherwise the operation behavior is undefined.
req\_ = {};
// Read a request
yield http::async\_read(
stream\_, buffer\_, req\_,
beast::bind\_front\_handler(
&session::loop, shared\_from\_this()));
if (ec == http::error::end\_of\_stream) {
// The remote host closed the connection
break;
}
if(ec)
return fail(ec, "read");
yield {
// Handle request
http::message\_generator msg =
handle\_request(\*doc\_root\_, std::move(req\_));
// Determine if we should close the connection
keep\_alive\_ = msg.keep\_alive();
// Send the response
beast::async\_write(
stream\_, std::move(msg),
beast::bind\_front\_handler(
&session::loop, shared\_from\_this()));
}
if(ec)
return fail(ec, "write");
if(! keep\_alive\_)
{
// This means we should close the connection, usually because
// the response indicated the "Connection: close" semantic.
break;
}
}
// Set the timeout.
beast::get\_lowest\_layer(stream\_).expires\_after(std::chrono::seconds(30));
// Perform the SSL shutdown
yield stream\_.async\_shutdown(
std::bind(
&session::loop,
shared\_from\_this(),
std::placeholders::\_1,
0));
if(ec)
return fail(ec, "shutdown");
// At this point the connection is closed gracefully
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
, socket\_(net::make\_strand(ioc))
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
std::make\_shared(
std::move(socket\_),
ctx\_,
doc\_root\_)->run();
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
if (argc != 5)
{
std::cerr <<
"Usage: http-server-stackless-ssl    \n" <<
"Example:\n" <<
" http-server-stackless-ssl 0.0.0.0 8080 . 1\n";
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