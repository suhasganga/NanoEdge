//
// Copyright (c) 2017 Christopher M. Kohlhoff (chris at kohlhoff dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE\_1\_0.txt or copy at http://www.boost.org/LICENSE\_1\_0.txt)
//
// Official repository: https://github.com/boostorg/beast
//
//------------------------------------------------------------------------------
//
// Example: HTTP server, fast
//
//------------------------------------------------------------------------------
#include "fields\_alloc.hpp"
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
class http\_worker
{
public:
http\_worker(http\_worker const&) = delete;
http\_worker& operator=(http\_worker const&) = delete;
http\_worker(tcp::acceptor& acceptor, const std::string& doc\_root) :
acceptor\_(acceptor),
doc\_root\_(doc\_root)
{
}
void start()
{
accept();
check\_deadline();
}
private:
using alloc\_t = fields\_alloc;
//using request\_body\_t = http::basic\_dynamic\_body>;
using request\_body\_t = http::string\_body;
// The acceptor used to listen for incoming connections.
tcp::acceptor& acceptor\_;
// The path to the root of the document directory.
std::string doc\_root\_;
// The socket for the currently connected client.
tcp::socket socket\_{acceptor\_.get\_executor()};
// The buffer for performing reads
beast::flat\_static\_buffer<8192> buffer\_;
// The allocator used for the fields in the request and reply.
alloc\_t alloc\_{8192};
// The parser for reading the requests
boost::optional> parser\_;
// The timer putting a time limit on requests.
net::steady\_timer request\_deadline\_{
acceptor\_.get\_executor(), (std::chrono::steady\_clock::time\_point::max)()};
// The string-based response message.
boost::optional>> string\_response\_;
// The string-based response serializer.
boost::optional>> string\_serializer\_;
// The file-based response message.
boost::optional>> file\_response\_;
// The file-based response serializer.
boost::optional>> file\_serializer\_;
void accept()
{
// Clean up any previous connection.
beast::error\_code ec;
socket\_.close(ec);
buffer\_.consume(buffer\_.size());
acceptor\_.async\_accept(
socket\_,
[this](beast::error\_code ec)
{
if (ec)
{
accept();
}
else
{
// Request must be fully processed within 60 seconds.
request\_deadline\_.expires\_after(
std::chrono::seconds(60));
read\_request();
}
});
}
void read\_request()
{
// On each read the parser needs to be destroyed and
// recreated. We store it in a boost::optional to
// achieve that.
//
// Arguments passed to the parser constructor are
// forwarded to the message object. A single argument
// is forwarded to the body constructor.
//
// We construct the dynamic body with a 1MB limit
// to prevent vulnerability to buffer attacks.
//
parser\_.emplace(
std::piecewise\_construct,
std::make\_tuple(),
std::make\_tuple(alloc\_));
http::async\_read(
socket\_,
buffer\_,
\*parser\_,
[this](beast::error\_code ec, std::size\_t)
{
if (ec)
accept();
else
process\_request(parser\_->get());
});
}
void process\_request(http::request> const& req)
{
switch (req.method())
{
case http::verb::get:
send\_file(req.target());
break;
default:
// We return responses indicating an error if
// we do not recognize the request method.
send\_bad\_response(
http::status::bad\_request,
"Invalid request-method '" + std::string(req.method\_string()) + "'\r\n");
break;
}
}
void send\_bad\_response(
http::status status,
std::string const& error)
{
string\_response\_.emplace(
std::piecewise\_construct,
std::make\_tuple(),
std::make\_tuple(alloc\_));
string\_response\_->result(status);
string\_response\_->keep\_alive(false);
string\_response\_->set(http::field::server, "Beast");
string\_response\_->set(http::field::content\_type, "text/plain");
string\_response\_->body() = error;
string\_response\_->prepare\_payload();
string\_serializer\_.emplace(\*string\_response\_);
http::async\_write(
socket\_,
\*string\_serializer\_,
[this](beast::error\_code ec, std::size\_t)
{
socket\_.shutdown(tcp::socket::shutdown\_send, ec);
string\_serializer\_.reset();
string\_response\_.reset();
accept();
});
}
void send\_file(beast::string\_view target)
{
// Request path must be absolute and not contain "..".
if (target.empty() || target[0] != '/' || target.find("..") != std::string::npos)
{
send\_bad\_response(
http::status::not\_found,
"File not found\r\n");
return;
}
std::string full\_path = doc\_root\_;
full\_path.append(
target.data(),
target.size());
http::file\_body::value\_type file;
beast::error\_code ec;
file.open(
full\_path.c\_str(),
beast::file\_mode::read,
ec);
if(ec)
{
send\_bad\_response(
http::status::not\_found,
"File not found\r\n");
return;
}
file\_response\_.emplace(
std::piecewise\_construct,
std::make\_tuple(),
std::make\_tuple(alloc\_));
file\_response\_->result(http::status::ok);
file\_response\_->keep\_alive(false);
file\_response\_->set(http::field::server, "Beast");
file\_response\_->set(http::field::content\_type, mime\_type(std::string(target)));
file\_response\_->body() = std::move(file);
file\_response\_->prepare\_payload();
file\_serializer\_.emplace(\*file\_response\_);
http::async\_write(
socket\_,
\*file\_serializer\_,
[this](beast::error\_code ec, std::size\_t)
{
socket\_.shutdown(tcp::socket::shutdown\_send, ec);
file\_serializer\_.reset();
file\_response\_.reset();
accept();
});
}
void check\_deadline()
{
// The deadline may have moved, so check it has really passed.
if (request\_deadline\_.expiry() <= std::chrono::steady\_clock::now())
{
// Close socket to cancel any outstanding operation.
socket\_.close();
// Sleep indefinitely until we're given a new deadline.
request\_deadline\_.expires\_at(
(std::chrono::steady\_clock::time\_point::max)());
}
request\_deadline\_.async\_wait(
[this](beast::error\_code)
{
check\_deadline();
});
}
};
int main(int argc, char\* argv[])
{
try
{
// Check command line arguments.
if (argc != 6)
{
std::cerr << "Usage: http\_server\_fast     {spin|block}\n";
std::cerr << " For IPv4, try:\n";
std::cerr << " http\_server\_fast 0.0.0.0 80 . 100 block\n";
std::cerr << " For IPv6, try:\n";
std::cerr << " http\_server\_fast 0::0 80 . 100 block\n";
return EXIT\_FAILURE;
}
auto const address = net::ip::make\_address(argv[1]);
unsigned short port = static\_cast(std::atoi(argv[2]));
std::string doc\_root = argv[3];
int num\_workers = std::atoi(argv[4]);
bool spin = (std::strcmp(argv[5], "spin") == 0);
net::io\_context ioc{1};
tcp::acceptor acceptor{ioc, {address, port}};
std::list workers;
for (int i = 0; i < num\_workers; ++i)
{
workers.emplace\_back(acceptor, doc\_root);
workers.back().start();
}
if (spin)
for (;;) ioc.poll();
else
ioc.run();
}
catch (const std::exception& e)
{
std::cerr << "Error: " << e.what() << std::endl;
return EXIT\_FAILURE;
}
}