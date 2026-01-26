//
// Copyright (c) 2022 Klemens D. Morgenstern (klemens dot morgenstern at gmx dot net)
// Copyright (c) 2024 Mohammad Nejati
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
#if defined(BOOST\_ASIO\_HAS\_CO\_AWAIT)
namespace beast = boost::beast;
namespace http = beast::http;
namespace websocket = beast::websocket;
namespace net = boost::asio;
namespace ssl = boost::asio::ssl;
using executor\_type = net::strand;
using stream\_type = typename beast::tcp\_stream::rebind\_executor::other;
using acceptor\_type = typename net::ip::tcp::acceptor::rebind\_executor::other;
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
/\*\* A thread-safe task group that tracks child tasks, allows emitting
cancellation signals to them, and waiting for their completion.
\*/
class task\_group
{
std::mutex mtx\_;
net::steady\_timer cv\_;
std::list css\_;
public:
task\_group(net::any\_io\_executor exec)
: cv\_{ std::move(exec), net::steady\_timer::time\_point::max() }
{
}
task\_group(task\_group const&) = delete;
task\_group(task\_group&&) = delete;
/\*\* Adds a cancellation slot and a wrapper object that will remove the child
task from the list when it completes.
@param completion\_token The completion token that will be adapted.
@par Thread Safety
@e Distinct @e objects: Safe.@n
@e Shared @e objects: Safe.
\*/
template
auto
adapt(CompletionToken&& completion\_token)
{
auto lg = std::lock\_guard{ mtx\_ };
auto cs = css\_.emplace(css\_.end());
class remover
{
task\_group\* tg\_;
decltype(css\_)::iterator cs\_;
public:
remover(
task\_group\* tg,
decltype(css\_)::iterator cs)
: tg\_{ tg }
, cs\_{ cs }
{
}
remover(remover&& other) noexcept
: tg\_{ std::exchange(other.tg\_, nullptr) }
, cs\_{ other.cs\_ }
{
}
~remover()
{
if(tg\_)
{
auto lg = std::lock\_guard{ tg\_->mtx\_ };
if(tg\_->css\_.erase(cs\_) == tg\_->css\_.end())
tg\_->cv\_.cancel();
}
}
};
return net::bind\_cancellation\_slot(
cs->slot(),
net::consign(
std::forward(completion\_token),
remover{ this, cs }));
}
/\*\* Emits the signal to all child tasks and invokes the slot's
handler, if any.
@param type The completion type that will be emitted to child tasks.
@par Thread Safety
@e Distinct @e objects: Safe.@n
@e Shared @e objects: Safe.
\*/
void
emit(net::cancellation\_type type)
{
auto lg = std::lock\_guard{ mtx\_ };
for(auto& cs : css\_)
cs.emit(type);
}
/\*\* Starts an asynchronous wait on the task\_group.
The completion handler will be called when:
@li All the child tasks completed.
@li The operation was cancelled.
@param completion\_token The completion token that will be used to
produce a completion handler. The function signature of the completion
handler must be:
@code
void handler(
boost::system::error\_code const& error // result of operation
);
@endcode
@par Thread Safety
@e Distinct @e objects: Safe.@n
@e Shared @e objects: Safe.
\*/
template<
typename CompletionToken =
net::default\_completion\_token\_t>
auto
async\_wait(
CompletionToken&& completion\_token =
net::default\_completion\_token\_t{})
{
return net::
async\_compose(
[this, scheduled = false](
auto&& self, boost::system::error\_code ec = {}) mutable
{
if(!scheduled)
self.reset\_cancellation\_state(
net::enable\_total\_cancellation());
if(!self.cancelled() && ec == net::error::operation\_aborted)
ec = {};
{
auto lg = std::lock\_guard{ mtx\_ };
if(!css\_.empty() && !ec)
{
scheduled = true;
return cv\_.async\_wait(std::move(self));
}
}
if(!std::exchange(scheduled, true))
return net::post(net::append(std::move(self), ec));
self.complete(ec);
},
completion\_token,
cv\_);
}
};
template
net::awaitable
run\_websocket\_session(
Stream& stream,
beast::flat\_buffer& buffer,
http::request req)
{
auto cs = co\_await net::this\_coro::cancellation\_state;
auto ws = websocket::stream{ stream };
// Set suggested timeout settings for the websocket
ws.set\_option(
websocket::stream\_base::timeout::suggested(beast::role\_type::server));
// Set a decorator to change the Server of the handshake
ws.set\_option(websocket::stream\_base::decorator(
[](websocket::response\_type& res)
{
res.set(
http::field::server,
std::string(BOOST\_BEAST\_VERSION\_STRING) +
" advanced-server-flex");
}));
// Accept the websocket handshake
co\_await ws.async\_accept(req);
while(!cs.cancelled())
{
// Read a message
auto [ec, \_] = co\_await ws.async\_read(buffer, net::as\_tuple);
if(ec == websocket::error::closed || ec == ssl::error::stream\_truncated)
co\_return;
if(ec)
throw boost::system::system\_error{ ec };
// Echo the message back
ws.text(ws.got\_text());
co\_await ws.async\_write(buffer.data());
// Clear the buffer
buffer.consume(buffer.size());
}
// A cancellation has been requested, gracefully close the session.
auto [ec] = co\_await ws.async\_close(
websocket::close\_code::service\_restart, net::as\_tuple);
if(ec && ec != ssl::error::stream\_truncated)
throw boost::system::system\_error{ ec };
}
template
net::awaitable
run\_session(
Stream& stream,
beast::flat\_buffer& buffer,
beast::string\_view doc\_root)
{
auto cs = co\_await net::this\_coro::cancellation\_state;
while(!cs.cancelled())
{
http::request\_parser parser;
parser.body\_limit(10000);
auto [ec, \_] =
co\_await http::async\_read(stream, buffer, parser, net::as\_tuple);
if(ec == http::error::end\_of\_stream)
co\_return;
if(websocket::is\_upgrade(parser.get()))
{
// The websocket::stream uses its own timeout settings.
beast::get\_lowest\_layer(stream).expires\_never();
co\_await run\_websocket\_session(
stream, buffer, parser.release());
co\_return;
}
auto res = handle\_request(doc\_root, parser.release());
if(!res.keep\_alive())
{
co\_await beast::async\_write(stream, std::move(res));
co\_return;
}
co\_await beast::async\_write(stream, std::move(res));
}
}
net::awaitable
detect\_session(
stream\_type stream,
ssl::context& ctx,
beast::string\_view doc\_root)
{
beast::flat\_buffer buffer;
// Allow total cancellation to change the cancellation state of this
// coroutine, but only allow terminal cancellation to propagate to async
// operations. This setting will be inherited by all child coroutines.
co\_await net::this\_coro::reset\_cancellation\_state(
net::enable\_total\_cancellation(), net::enable\_terminal\_cancellation());
// We want to be able to continue performing new async operations, such as
// cleanups, even after the coroutine is cancelled. This setting will be
// inherited by all child coroutines.
co\_await net::this\_coro::throw\_if\_cancelled(false);
stream.expires\_after(std::chrono::seconds(30));
if(co\_await beast::async\_detect\_ssl(stream, buffer))
{
ssl::stream ssl\_stream{ std::move(stream), ctx };
auto bytes\_transferred = co\_await ssl\_stream.async\_handshake(
ssl::stream\_base::server, buffer.data());
buffer.consume(bytes\_transferred);
co\_await run\_session(ssl\_stream, buffer, doc\_root);
if(!ssl\_stream.lowest\_layer().is\_open())
co\_return;
// Gracefully close the stream
auto [ec] = co\_await ssl\_stream.async\_shutdown(net::as\_tuple);
if(ec && ec != ssl::error::stream\_truncated)
throw boost::system::system\_error{ ec };
}
else
{
co\_await run\_session(stream, buffer, doc\_root);
if(!stream.socket().is\_open())
co\_return;
stream.socket().shutdown(net::ip::tcp::socket::shutdown\_send);
}
}
net::awaitable
listen(
task\_group& task\_group,
ssl::context& ctx,
net::ip::tcp::endpoint endpoint,
beast::string\_view doc\_root)
{
auto cs = co\_await net::this\_coro::cancellation\_state;
auto executor = co\_await net::this\_coro::executor;
auto acceptor = acceptor\_type{ executor, endpoint };
// Allow total cancellation to propagate to async operations.
co\_await net::this\_coro::reset\_cancellation\_state(
net::enable\_total\_cancellation());
while(!cs.cancelled())
{
auto socket\_executor = net::make\_strand(executor.get\_inner\_executor());
auto [ec, socket] =
co\_await acceptor.async\_accept(socket\_executor, net::as\_tuple);
if(ec == net::error::operation\_aborted)
co\_return;
if(ec)
throw boost::system::system\_error{ ec };
net::co\_spawn(
std::move(socket\_executor),
detect\_session(stream\_type{ std::move(socket) }, ctx, doc\_root),
task\_group.adapt(
[](std::exception\_ptr e)
{
if(e)
{
try
{
std::rethrow\_exception(e);
}
catch(std::exception& e)
{
std::cerr << "Error in session: " << e.what() << "\n";
}
}
}));
}
}
net::awaitable
handle\_signals(task\_group& task\_group)
{
auto executor = co\_await net::this\_coro::executor;
auto signal\_set = net::signal\_set{ executor, SIGINT, SIGTERM };
auto sig = co\_await signal\_set.async\_wait();
if(sig == SIGINT)
{
std::cout << "Gracefully cancelling child tasks...\n";
task\_group.emit(net::cancellation\_type::total);
// Wait a limited time for child tasks to gracefully cancell
auto [ec] = co\_await task\_group.async\_wait(
net::as\_tuple(net::cancel\_after(std::chrono::seconds{ 10 })));
if(ec == net::error::operation\_aborted) // Timeout occurred
{
std::cout << "Sending a terminal cancellation signal...\n";
task\_group.emit(net::cancellation\_type::terminal);
co\_await task\_group.async\_wait();
}
std::cout << "Child tasks completed.\n";
}
else // SIGTERM
{
net::query(
executor.get\_inner\_executor(),
net::execution::context).stop();
}
}
int
main(int argc, char\* argv[])
{
// Check command line arguments.
if(argc != 5)
{
std::cerr << "Usage: advanced-server-flex-awaitable    \n"
<< "Example:\n"
<< " advanced-server-flex-awaitable 0.0.0.0 8080 . 1\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
auto const port = static\_cast(std::atoi(argv[2]));
auto const endpoint = net::ip::tcp::endpoint{ address, port };
auto const doc\_root = beast::string\_view{ argv[3] };
auto const threads = std::max(1, std::atoi(argv[4]));
// The io\_context is required for all I/O
net::io\_context ioc{ threads };
// The SSL context is required, and holds certificates
ssl::context ctx{ ssl::context::tlsv12 };
// This holds the self-signed certificate used by the server
load\_server\_certificate(ctx);
// Track coroutines
task\_group task\_group{ ioc.get\_executor() };
// Create and launch a listening coroutine
net::co\_spawn(
net::make\_strand(ioc),
listen(task\_group, ctx, endpoint, doc\_root),
task\_group.adapt(
[](std::exception\_ptr e)
{
if(e)
{
try
{
std::rethrow\_exception(e);
}
catch(std::exception& e)
{
std::cerr << "Error in listener: " << e.what() << "\n";
}
}
}));
// Create and launch a signal handler coroutine
net::co\_spawn(
net::make\_strand(ioc), handle\_signals(task\_group), net::detached);
// Run the I/O service on the requested number of threads
std::vector v;
v.reserve(threads - 1);
for(auto i = threads - 1; i > 0; --i)
v.emplace\_back([&ioc] { ioc.run(); });
ioc.run();
// Block until all the threads exit
for(auto& t : v)
t.join();
return EXIT\_SUCCESS;
}
#else
int
main(int, char\*[])
{
std::printf("awaitables require C++20\n");
return EXIT\_FAILURE;
}
#endif