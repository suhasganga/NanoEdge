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
// Example: HTTP server, asynchronous Unix domain sockets
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
#if defined(BOOST\_ASIO\_HAS\_LOCAL\_SOCKETS)
namespace beast = boost::beast; // from 
namespace http = beast::http; // from 
namespace net = boost::asio; // from 
using stream\_protocol = net::local::stream\_protocol; // from 
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
// Handles an HTTP server connection
class session : public std::enable\_shared\_from\_this
{
beast::basic\_stream<
stream\_protocol,
net::any\_io\_executor,
beast::unlimited\_rate\_policy> stream\_;
beast::flat\_buffer buffer\_;
std::shared\_ptr doc\_root\_;
http::request req\_;
public:
// Take ownership of the stream
session(
stream\_protocol::socket&& socket,
std::shared\_ptr const& doc\_root)
: stream\_(std::move(socket))
, doc\_root\_(doc\_root)
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
net::dispatch(stream\_.get\_executor(),
beast::bind\_front\_handler(
&session::do\_read,
shared\_from\_this()));
}
void
do\_read()
{
// Make the request empty before reading,
// otherwise the operation behavior is undefined.
req\_ = {};
// Set the timeout.
stream\_.expires\_after(std::chrono::seconds(30));
// Read a request
http::async\_read(stream\_, buffer\_, req\_,
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
// This means they closed the connection
if(ec == http::error::end\_of\_stream)
return do\_close();
if(ec)
return fail(ec, "read");
// Send the response
send\_response(
handle\_request(\*doc\_root\_, std::move(req\_)));
}
void
send\_response(http::message\_generator&& msg)
{
bool keep\_alive = msg.keep\_alive();
// Write the response
beast::async\_write(
stream\_,
std::move(msg),
beast::bind\_front\_handler(
&session::on\_write, shared\_from\_this(), keep\_alive));
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
// Read another request
do\_read();
}
void
do\_close()
{
// Send a TCP shutdown
beast::error\_code ec;
stream\_.socket().shutdown(stream\_protocol::socket::shutdown\_send, ec);
// At this point the connection is closed gracefully
}
};
//------------------------------------------------------------------------------
// Accepts incoming connections and launches the sessions
class listener : public std::enable\_shared\_from\_this
{
net::io\_context& ioc\_;
stream\_protocol::acceptor acceptor\_;
std::shared\_ptr doc\_root\_;
public:
listener(
net::io\_context& ioc,
stream\_protocol::endpoint endpoint,
std::shared\_ptr const& doc\_root)
: ioc\_(ioc)
, acceptor\_(net::make\_strand(ioc), std::move(endpoint))
, doc\_root\_(doc\_root)
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
return; // To avoid infinite loop
}
else
{
// Create the session and run it
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
try
{
// Check command line arguments.
if (argc != 4)
{
std::cerr <<
"Usage: http-server-async-local   \n" <<
"Example:\n" <<
" http-server-async-local /tmp/http.sock . 1\n";
return EXIT\_FAILURE;
}
auto const path = argv[1];
auto const doc\_root = std::make\_shared(argv[2]);
auto const threads = std::max(1, std::atoi(argv[3]));
// The io\_context is required for all I/O
net::io\_context ioc{threads};
// Remove previous binding
std::remove(path);
// Create and launch a listening port
std::make\_shared(
ioc,
stream\_protocol::endpoint{path},
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